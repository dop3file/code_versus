from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from tasks.views import TaskViewset


router = routers.SimpleRouter()
router.register(r"tasks", TaskViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    # path("api/v1/tasks/", TaskViewset.as_view({"get": "list", "post": "create"})),
    # path("api/v1/tasks/<int:pk>/", TaskViewset.as_view({"put": "update"})),
]
