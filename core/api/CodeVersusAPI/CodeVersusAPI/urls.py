from django.contrib import admin
from django.urls import path

from tasks.views import TaskAPIList, TaskAPIDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', TaskAPIList.as_view()),
    path('api/v1/tasks/<int:pk>/', TaskAPIDetails.as_view()),
]
