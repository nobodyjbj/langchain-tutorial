import os


def logging(project_name=None, set_enable=True):

    if set_enable:
        result = os.environ.get("LANGCHAIN_API_KEY")
        if result is None or result.strip() == "":
            print(
                "LangChain API Key가 설정되지 않았습니다. 참고: https://wikidocs.net/250954"
            )
            return
        os.environ["LANGCHAIN_ENDPOINT"] = (
            "https://api.smith.langchain.com"  # LangSmith API 엔드포인트
        )
        os.environ["LANGCHAIN_TRACING_V2"] = "true"  # true: 활성화
        os.environ["LANGCHAIN_PROJECT"] = project_name  # 프로젝트명
        print(f"Langsmith 추적이 활성화되었습니다. [프로젝트명: {project_name}]")
    else:
        os.environ["LANGCHAIN_TRACING_V2"] = "false"  # false: 비활성화
        print("LangSmith 추적을 하지 않습니다.")


def env_variable(key, value):
    os.environ[key] = value
