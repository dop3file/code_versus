from CodeVersusAPI.settings import OPEN_AI_KEY

import openai


class AIHandler:
    def __init__(self):
        openai.api_key = OPEN_AI_KEY
        self.messages = []

        self.promts = {
            "question": "Сгенерируй мне вопрос и ответ для senior программиста разработчика(сложный вопрос и на одну из тем {}, проектирование, алгоритмы, бекенд технологии и главное чтоб на вопрос был четкий ответ) и раздели вопрос и ответ линией что б я мог их разделить и записать в базу И БЕЗ ПОВТОРЯЮЩИХСЯ ВОПРОСОВ ПОЖАЛУЙСТА"
        }

    def send_prompt(self, name_promt: str, *args) -> str:
        message = self.promts[name_promt].format(*args)
        self.messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        return reply