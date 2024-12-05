import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from utility.logging import LangsmithTracker

import os
from dotenv import load_dotenv


load_dotenv()

if "tracker" not in st.session_state:
    st.session_state["tracker"] = LangsmithTracker(
        project_name="[Project] PDF RAG"
    ).configure_tracking()


# 캐시 디렉토리 생성
if not os.path.exists(".cache"):
    os.mkdir(".cache")

if not os.path.exists(".cache/files"):
    os.mkdir(".cache/files")

if not os.path.exists(".cache/embeddings"):
    os.mkdir(".cache/embeddings")


st.title("PDF 자료를 기반으로 하는 챗봇입니다. 질문 🙋🙋‍♀️🙋‍♂️")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "chain" not in st.session_state:
    st.session_state["chain"] = None

with st.sidebar:
    clear_button = st.button("대화 초기화")
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])
    selectedd_model = st.selectbox(
        "LLM 선택", ["gpt-4o", "gpt4-turbo", "gpt-4o-mini"], index=0
    )


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


# 파일을 캐시에 저장(캐시에 저장된 파일의 경우 빠르지만 그렇지않고 처음 업로드할때는 시간이 오래 걸린다.)
@st.cache_resource(show_spinner="업로드한 파일을 처리 중입니다.")
def embed_file(file):
    # 업로드한 파일을 캐시 디렉토리에 저장
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    with open(file_path, "wb") as f:
        f.write(file_content)

    # 1단계: 문서 로드(Load Documents)
    loader = PyMuPDFLoader(file_path=file_path)
    docs = loader.load()

    # 2단계: 문서 분할(split documents)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split_documents = text_splitter.split_documents(docs)

    # 3단계: 임베딩(Embedding) 생성
    embeddings = OpenAIEmbeddings()

    # 4단계: DB 생성(Create DB) 및 저장, VectorStore 생성, FAISS는 메모리 공간에 저장합니다.
    vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)

    # 5단계: 검색기(Retriever) 생성
    retriever = vectorstore.as_retriever()

    return retriever


# chain 생성
def create_chain(retriever, model_name="gpt-4o-mini"):
    # 6단계: 프롬프트 생성(Create Prompt)
    prompt = load_prompt("prompts/05.pdf-rag.yml")

    # 7단계: LLM 생성
    llm = ChatOpenAI(model=model_name, temperature=0)

    # 8단계: Chain 생성, context=chunk 묶음, quetion=user_prompt
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


# 세션 메세지 초기화
if clear_button:
    st.session_state["messages"] = []

# 메세지 출력을 호출
print_messages()


# 새로운 메세지를 추가
def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


# 파일이 업로드 되었을때
if uploaded_file:
    # 파일 캐시에 저장 후 retriever 생성
    retirever = embed_file(uploaded_file)
    chain = create_chain(retriever=retirever, model_name=selectedd_model)
    st.session_state["chain"] = chain


user_prompt = st.chat_input("궁금한 내용을 질문하세요!")

# 경고 메시지를 띄우기 위한 빈 영역
warnning_message = st.empty()

if user_prompt:
    chain = st.session_state["chain"]

    if chain is not None:
        st.chat_message("user").write(user_prompt)
        response = chain.stream(user_prompt)

        # strem 출력 방식
        with st.chat_message("assistant"):
            container = st.empty()
            ai_answer = ""
            for token in response:
                ai_answer += token
                container.markdown(ai_answer)

        add_message("user", user_prompt)
        add_message("assistant", ai_answer)
    else:
        warnning_message.error("파일을 업로드 해주세요.")
