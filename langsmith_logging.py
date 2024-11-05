import os
from dotenv import load_dotenv

load_dotenv()

def configure_langsmith_tracking(project_name=None, enable_tracking=True):
    """
    Langsmith 추적을 위한 환경 변수를 설정하거나 해제하는 함수

    Parameters:
        project_name (str): 프로젝트 이름을 환경 변수로 설정합니다.
        enable_tracking (bool): True일 경우 추적 활성화, False일 경우 비활성화.
    
    Returns:
        None
    """
    # API Key 확인
    api_key = os.getenv("LANGCHAIN_API_KEY")
    if not api_key:
        print("Langsmith API Key가 설정되지 않았습니다. API Key를 설정하세요.")
        return

    # 추적 활성화 설정
    if enable_tracking:
        os.environ["LANGCHAIN_API_KEY"] = api_key
        os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"  # Langsmith API 엔드포인트
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        if project_name:
            os.environ["LANGCHAIN_PROJECT"] = project_name
        print(f"Langsmith 추적이 활성화되었습니다. [프로젝트명: {project_name}]")
    else:
        os.environ["LANGCHAIN_TRACING_V2"] = "false"
        print("Langsmith 추적이 비활성화되었습니다.")