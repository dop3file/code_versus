from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.views import Response

from .serializers import QuestionSerializer
from .services import QuestionService

    
class QuestionViewset(ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)

    @action(methods=["get"], detail=False, permission_classes=(AllowAny,))
    def generate(self, request):
        language = request.data.get("language")
        count = request.data.get("count")
        question = QuestionService.generate_question(language, count)
        return Response(question)

    @action(methods=["get"], detail=True, permission_classes=(AllowAny,))
    def answer(self, request, pk: int):
        question = QuestionService.get_answer(pk)
        return Response(question)


