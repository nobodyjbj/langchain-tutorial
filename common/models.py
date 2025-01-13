from enum import Enum


class LLMs(Enum):
    GPT4o_MINI = "gpt-4o-mini"
    GPT4o = "gpt-4o"
    GPT4 = GPT4o_MINI

    O1_PREVIEW = "o1-preview"
    O1_MINI = "o1-mini"
    O1 = O1_MINI

    CLAUDE_SONNET = "claude-3-5-sonnet-20241022"
    CLAUDE_HAIKU = "claude-3-5-haiku-20241022"
    CLAUDE = CLAUDE_SONNET

    UPSTAGE_SOLAR_MINI = "solar-mini"
    UPSTAGE_SOLAR_PRO = "solar-pro"
    UPSTAGE = UPSTAGE_SOLAR_PRO


class Embeddings(Enum):
    OPENAI_EMBEDDING_SMALL = "text-embedding-3-small"
    OPENAI_EMBEDDING_LARGE = "text-embedding-3-large"
    OPENAI_EMBEDDING = OPENAI_EMBEDDING_SMALL

    UPSTAGE_EMBEDDING_QUERY = "embedding-query"
    UPSTAGE_EMBEDDING_PASSAGE = "embedding-passage"
    UPSTAGE_EMBEDDING = UPSTAGE_EMBEDDING_PASSAGE


def get_model_name(model: LLMs | Embeddings) -> str:
    """
    Enum 클래스로부터 모델의 최종 value 값을 추출하여 반환합니다.

    Args:
        model (LLMs | Embeddings): LLMs 또는 Embeddings Enum 클래스

    Returns:
        str: 모델의 최종 value 값. 유효하지 않은 Enum인 경우 None 반환
    """
    try:
        # value가 Enum 멤버인 경우 최종 값을 반환
        current_value = model.value
        while isinstance(current_value, Enum):
            current_value = current_value.value
        return current_value
    except AttributeError:
        return None
