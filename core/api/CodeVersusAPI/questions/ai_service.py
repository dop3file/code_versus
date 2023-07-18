from CodeVersusAPI.settings import OPEN_AI_KEY
from CodeVersusAPI.redis_handler import OpenAIMessages

import openai


class OpenAIHandler:
    def __init__(self):
        openai.api_key = OPEN_AI_KEY
        self.messages = OpenAIMessages()

    def get_answer(self, message: str):
        self.messages.add_message(message)
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages.get_all_messages())
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        self.messages.add_message(reply)