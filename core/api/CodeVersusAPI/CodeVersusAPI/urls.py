from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from tasks.views import TaskViewset


task_router = routers.DefaultRouter()
task_router.register(r"tasks", TaskViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("rest_framework.urls")),
    path("api/v1/", include(task_router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
