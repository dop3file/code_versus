import redis


class OpenAIMessages:
    def __init__(self):
        self.list_name = "messages"

    def add_message(self, message: str):
        r.rpush(self.list_name, message)

    def get_all_messages(self):
        return r.lrange(self.list_name, 0, -1)

