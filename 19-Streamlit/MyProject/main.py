import streamlit as st
from langchain_core.messages.chat import ChatMessage

# 제목을 작성하는 방법입니다.
st.title("나만의 ChatGPT")

# 채팅창을 만드는 방법입니다.
prompt = st.chat_input("궁금한 내용을 질문하세요!")

# 대화기록을 저장하기위한 용도입니다.
# 처음 한 번만 st.session_state["messages"] 를 생성합니다. 새로고침 되더라도 st.session_state["messages"] 에 저장됩니다.
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# sesstion_state["messages"] 에 내용이 있다면 출력해줍니다.
def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


# 메세지 출력을 호출합니다.
print_messages()


# 새로운 메세지를 추가합니다.
def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


if prompt:
    st.chat_message("user").write(prompt)  # with 문법 간소화
    st.chat_message("assistant").write(prompt)

    # 대화 기록 {role, message} 형태로 st.session_state["messages"] 에 저장합니다.
    # st.session_state["messages"].append({"user", prompt})
    # st.session_state["messages"].append({"assistant", prompt})

    add_message("user", prompt)
    add_message("assistant", prompt)
