import os
from dotenv import load_dotenv

load_dotenv()


class LangsmithTracker:
    def __init__(self, project_name=None, enable_tracking=True):
        """
        Langsmith 추적 설정을 위한 클래스

        Parameters:
            project_name (str): 프로젝트 이름을 환경 변수로 설정합니다.
            enable_tracking (bool): True일 경우 추적 활성화, False일 경우 비활성화.
        """
        self.project_name = project_name
        self.enable_tracking = enable_tracking
        self.api_key = os.getenv("LANGCHAIN_API_KEY")
        self.endpoint = "https://api.smith.langchain.com"  # Langsmith API 엔드포인트

    def configure_tracking(self):
        """
        Langsmith 추적을 설정하거나 해제하는 메서드
        """
        # API Key 확인
        if not self.api_key:
            print("Langsmith API Key가 설정되지 않았습니다. API Key를 설정하세요.")
            return

        # 추적 활성화 설정
        if self.enable_tracking:
            os.environ["LANGCHAIN_API_KEY"] = self.api_key
            os.environ["LANGCHAIN_ENDPOINT"] = self.endpoint
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            if self.project_name:
                os.environ["LANGCHAIN_PROJECT"] = self.project_name
            print(
                f"Langsmith 추적이 활성화되었습니다. [프로젝트명: {self.project_name}]"
            )
        else:
            os.environ["LANGCHAIN_TRACING_V2"] = "false"
            print("Langsmith 추적이 비활성화되었습니다.")

    def enable(self):
        """
        추적을 활성화하고 설정을 업데이트
        """
        self.enable_tracking = True
        self.configure_tracking()

    def disable(self):
        """
        추적을 비활성화하고 설정을 업데이트
        """
        self.enable_tracking = False
        self.configure_tracking()
