from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from tasks.views import TaskViewset
from users.views import CustomUserViewSet
from questions.views import QuestionViewset, AnswerViewSet


task_router = routers.DefaultRouter()
task_router.register(r"tasks", TaskViewset)
user_router = routers.SimpleRouter()
user_router.register(r"users", CustomUserViewSet, basename="user")
questions_router = routers.SimpleRouter()
questions_router.register(r"questions", QuestionViewset, basename="question")
answer_router = routers.SimpleRouter()
answer_router.register(r"answers", AnswerViewSet, basename="answers")


PREFIX = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(PREFIX, include(task_router.urls)),
    path(f"{PREFIX}auth/", include("rest_framework.urls")),
    path(f"{PREFIX}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(f"{PREFIX}token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(f"{PREFIX}token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(PREFIX, include(user_router.urls)),
    path(PREFIX, include(questions_router.urls)),
    path(PREFIX, include(answer_router.urls))
]
