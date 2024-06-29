import os
from enum import Enum

import httpx
from datasets import Dataset
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from bisheng_ragas import evaluate
from bisheng_ragas.llms.langchain import LangchainLLM
from bisheng_ragas.metrics import AnswerCorrectnessBisheng

load_dotenv('/opt/.env', override=True)


class LLM(Enum):
    GPT_4_TURBO_2024_04_09: str = "gpt-4-turbo-2024-04-09"
    GPT_3_5_TURBO: str = "gpt-3.5-turbo"
    QWEN_1_5_72B: str = "qwen1.5-72b"
    QWEN_1_5_110B_CHAT: str = "qwen1.5-110b-chat"
    MOONSHOT_V1_8K: str = "moonshot-v1-8k"
    MOONSHOT_V1_32K: str = "moonshot-v1-32k"
    MOONSHOT_V1_128K: str = "moonshot-v1-128k"
    COMMAND_R_PLUS_104B: str = "command-r-plus-104b"


def llm_factory(
    model: LLM,
    temperature: float = 0.0,
    **kwargs,
) -> ChatOpenAI:
    if model == LLM.GPT_4_TURBO_2024_04_09:
        return ChatOpenAI(
            model="gpt-4-turbo-2024-04-09",
            http_client=httpx.Client(proxies=os.getenv('OPENAI_PROXY')),
            http_async_client=httpx.AsyncClient(proxies=os.getenv('OPENAI_PROXY')),
            temperature=temperature,
        )
    elif model == LLM.GPT_3_5_TURBO:
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            http_client=httpx.Client(proxies=os.getenv('OPENAI_PROXY')),
            temperature=temperature,
        )
    elif model == LLM.QWEN_1_5_72B:
        return ChatOpenAI(
            model="qwen1.5",
            base_url=os.getenv('QWEN1.5_BASE_URL'),
            temperature=temperature,
        )
    elif model == LLM.QWEN_1_5_110B_CHAT:
        return ChatOpenAI(
            model="qwen1.5-110b-chat",
            base_url=os.getenv('QWEN1.5_110B_BASE_URL'),
            api_key=os.getenv('QWEN1.5_110B_API_KEY'),
            temperature=temperature,
        )
    elif model == LLM.MOONSHOT_V1_8K:
        return ChatOpenAI(
            model="moonshot-v1-8k",
            api_key=os.getenv('KIMI_API_KEY'),
            base_url=os.getenv('KIMI_BASE_URL'),
            temperature=temperature,
        )
    elif model == LLM.MOONSHOT_V1_32K:
        return ChatOpenAI(
            model="moonshot-v1-32k",
            api_key=os.getenv('KIMI_API_KEY'),
            base_url=os.getenv('KIMI_BASE_URL'),
            temperature=temperature,
        )
    elif model == LLM.MOONSHOT_V1_128K:
        return ChatOpenAI(
            model="moonshot-v1-128k",
            api_key=os.getenv('KIMI_API_KEY'),
            base_url=os.getenv('KIMI_BASE_URL'),
            temperature=temperature,
        )
    elif model == LLM.COMMAND_R_PLUS_104B:
        return ChatOpenAI(
            model="command-r-plus-104b",
            base_url=os.getenv('COMMAND_R_PLUS_BASE_URL'),
            api_key=os.getenv('COMMAND_R_PLUS_API_KEY'),
        )


data_samples = {
    'question': ['When was the first super bowl?', 'Who won the most super bowls?'],
    'answer': [
        'The first superbowl was held on Jan 15, 1967',
        'The most super bowls have been won by The New England Patriots',
    ],
    'ground_truths': [
        ['The first superbowl was held on January 15, 1967.'],
        ['The New England Patriots have won the Super Bowl a record six times'],
    ],
}
_llm = llm_factory(model=LLM.GPT_4_TURBO_2024_04_09)

llm = LangchainLLM(_llm)
answer_correctness_bisheng = AnswerCorrectnessBisheng(llm=llm)

dataset = Dataset.from_dict(data_samples)
score = evaluate(dataset, metrics=[answer_correctness_bisheng])
print(score.to_pandas())
