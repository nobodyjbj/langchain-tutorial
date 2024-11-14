import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate, load_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# 제목을 작성하는 방법
st.title("나만의 ChatGPT")

# 채팅창을 만드는 방법
user_prompt = st.chat_input("궁금한 내용을 질문하세요!")

# 대화기록을 저장하기위한 용도
# 처음 한 번만 st.session_state["messages"] 를 생성. 새로고침 되더라도 st.session_state["messages"] 에 저장됨
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 사이드바 생성
with st.sidebar:
    clear_button = st.button("대화 초기화")

    selected_mode = st.selectbox(
        "프롬프트를 선택해주세요.", ("기본모드", "요약모드", "코딩모드"), index=0
    )


# sesstion_state["messages"] 에 내용이 있다면 출력
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


# chain 생성
def create_chain(prompt_type):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "당신은 친절한 AI 어시던트입니다."),
            ("user", "#Question:\n{question}"),
        ]
    )

    if prompt_type == "코딩모드":
        prompt = load_prompt("prompts/coding.yml")
    elif prompt_type == "요약모드":
        prompt = hub.pull("teddynote/chain-of-density-korean")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    return chain


# 세션 메세지 초기화
if clear_button:
    st.session_state["messages"] = []

# 메세지 출력을 호출
print_messages()


# 새로운 메세지를 추가
def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


if user_prompt:
    st.chat_message("user").write(user_prompt)  # with 문법 간소화

    chain = create_chain(selected_mode)
    response = chain.stream({"question": user_prompt})

    # invoke 출력 방식
    # ai_answer = chain.invoke({"question": user_prompt})
    # st.chat_message("assistant").write(ai_answer)

    # strem 출력 방식
    with st.chat_message("assistant"):
        container = st.empty()
        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

    # 대화 기록 {role, message} 형태로 st.session_state["messages"] 에 저장
    add_message("user", user_prompt)
    add_message("assistant", ai_answer)
