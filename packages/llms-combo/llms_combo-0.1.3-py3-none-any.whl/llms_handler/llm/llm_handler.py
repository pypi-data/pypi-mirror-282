# Author Jaredhao
# Email 9190632@qq.com
# Created 2024/4/17 17:17
import asyncio

from llms_handler import KIMI
from llms_handler.llm.baichuan.baichuan import Baichuan
from llms_handler.llm.qianwen.qwen import QWEN
from llms_handler.llm.zhipu.glm import GLMService


# Importing the language model classes from their respective modules

class LLMHandler:
    def __init__(self):
        # Mapping of model keys to their respective class constructors
        self.models = {
            'kimi': KIMI,
            'baichuan': Baichuan,
            'qwen': QWEN,
            'glm': GLMService
        }


    def direct(self, messages,model_key='baichuan'):
        if model_key not in self.models:
            raise ValueError(f"Unsupported model key: {model_key}. Supported keys: {list(self.models.keys())}")

        self.model = self.models[model_key]()
        response = self.model.direct(messages)
        return response

    async def chat(self, messages,model_key='baichuan'):
        if model_key not in self.models:
            raise ValueError(f"Unsupported model key: {model_key}. Supported keys: {list(self.models.keys())}")

        # Instantiate the model based on the provided key
        self.model = self.models[model_key]()
        # Generic chat method that dynamically calls the chat method of the instantiated model
        async for response in self.model.chat(messages):
            yield response


# Example of how to use LLMHandler
async def main():
    handler = LLMHandler()  # You could replace 'kimi' with 'baichuan', 'qwen', or 'glm'
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    async for response in handler.chat(messages, 'kimi'):
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
