from django.contrib import admin
from django.urls import path

from tasks.views import TaskAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/task', TaskAPIView.as_view())
]
