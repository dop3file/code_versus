from .ai_service import AIHandler
from .models import Question, Answer
from CodeVersusAPI.exceptions import NotFoundException


ai_handler = AIHandler()


class QuestionService:
    @staticmethod
    def generate_question(language: str, count: int):
        prompt = ai_handler.send_prompt("question", count, language)
        new_question = Question(
            title=prompt.split("Вопрос:")[1].split("\n")[0].strip().rstrip()
        )
        new_question.save()
        new_answer = Answer(
            title=prompt.split("Ответ:")[1].strip().rstrip(),
            question=new_question
        )
        new_answer.save()
        return {
            "id": new_question.pk,
            "title": new_question.title
        }

    @staticmethod
    def get_answer(question_id: int):
        try:
            answer = Answer.objects.get(question_id=question_id)
        except Answer.DoesNotExist:
            raise NotFoundException
        print(answer.title)
        return {
            "title": answer.title
        }


