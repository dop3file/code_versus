from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework import viewsets, authentication, permissions

from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (permissions.IsAdminUser,)
        elif self.action in ["create"]:
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.filter(pk=user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




