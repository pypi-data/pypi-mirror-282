# Author Jaredhao
# Email 9190632@qq.com
# Created 2024/4/18 11:23
import asyncio
from openai import OpenAI

MOONSHOT_SERVER = "https://api.moonshot.cn/v1"


class KIMI:
    def __init__(self, MOONSHOT_API_KEY):
        self.client = OpenAI(
            api_key=MOONSHOT_API_KEY,
            base_url=MOONSHOT_SERVER,
        )

    def direct(self, messages, len=32):
        _model = "moonshot-v1-32k"
        if len == 128:
            _model = "moonshot-v1-128k"
        response = self.client.chat.completions.create(
            model=_model,
            messages=messages,
            temperature=0.1,
        )
        result = response.choices[0].message.content
        return result

    async def chat(self, messages):
        response = self.client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=messages,
            temperature=0.1,
            stream=True,
        )

        for idx, chunk in enumerate(response):
            # print("Chunk received, value: ", chunk)
            chunk_message = chunk.choices[0].delta
            if not chunk_message.content:
                continue
            yield chunk_message.content

