from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS


def create_retriever(file_path):
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
