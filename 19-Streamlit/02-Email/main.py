import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import load_prompt, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerpAPIWrapper
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import glob


load_dotenv()


class EmailSummury(BaseModel):  # BaseModel 기능을 상속받음
    sender_name: str = Field(description="발신자 이름")
    sender_department: str = Field(description="발신자 부서")
    sender_email: str = Field(description="발신자 이메일")
    subject: str = Field(description="메일 제목")
    summury: str = Field(description="메일 본문의 중요 내용 요약")
    keyword: str = Field(description="메일 본문의 핵심 키워드")
    date: str = Field(description="회의 일정 일시")


# 제목을 작성하는 방법
st.title("이메일 요약기💬")

# 채팅창을 만드는 방법
user_prompt = st.chat_input("궁금한 내용을 질문하세요!")

# 대화기록을 저장하기위한 용도
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 사이드바 생성
with st.sidebar:
    clear_button = st.button("대화 초기화")
    prompt_files = glob.glob("prompts/*.yml")


# sesstion_state["messages"] 에 내용이 있다면 출력
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


# Email 파싱 체인
@st.cache_resource(show_spinner="이메일을 파싱중입니다.")
def create_email_parsing_chain():
    output_parser = PydanticOutputParser(pydantic_object=EmailSummury)

    template = """
        당신은 AI 어시드던트입니다. 아래 내용에 대한 질문을 한글로 대답해주세요.
        
        #Qustion:
        다음의 이메일 내용 중에서 주요 내용을 추출해주세요.
        
        #EMAIL CONVERSATION:
        {email_conversation}
        
        #FORMAT:
        {format_instruction}
    """

    prompt = PromptTemplate.from_template(
        template=template,
        partial_variables={
            "format_instruction": output_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    chain = prompt | llm | output_parser

    return chain


# 리포트 생성 체인
def create_report_chain():
    prompt = load_prompt("prompts/email.yml")

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

    # 1) Email 파싱 체인 생성 및 실행
    email_parsing_chain = create_email_parsing_chain()
    email_parsing_response = email_parsing_chain.invoke(
        {"email_conversation": user_prompt}
    )

    # 2) Email 검색 과정
    params = {"engine": "google", "gl": "kr", "hl": "ko", "num": "3"}
    search = SerpAPIWrapper(params=params)
    search_query = f"{email_parsing_response.keyword}"
    search_result = search.run(search_query)
    search_result = eval(search_result)
    search_result_string = "\n".join(search_result)

    # 3) Email 요약 리포트 생성
    report_chain = create_report_chain()
    report_chain_input = {
        "sender": email_parsing_response.sender_name,
        "additional_information": search_result_string,
        "department": email_parsing_response.sender_department,
        "email": email_parsing_response.sender_email,
        "subject": email_parsing_response.subject,
        "summury": email_parsing_response.summury,
        "date": email_parsing_response.date,
    }

    response = report_chain.stream(report_chain_input)

    # strem 출력 방식
    with st.chat_message("assistant"):
        container = st.empty()
        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

    # 대화 기록 저장
    add_message("user", user_prompt)
    add_message("assistant", ai_answer)
