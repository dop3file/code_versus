from CodeVersusAPI.settings import OPEN_AI_KEY

import openai


class OpenAIHandler:
    def __init__(self):
        openai.api_key = OPEN_AI_KEY
        self.messages = []

        self.promts = {
            "question": "Сгенерируй мне {} вопросов и ответ для senior {} разработчика(сложный вопрос) и раздели вопрос и ответ"
        }

    def send_prompt(self, name_promt: str, *args):
        message = self.promts[name_promt].format(*args)
        self.messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        self.messages.append(reply)