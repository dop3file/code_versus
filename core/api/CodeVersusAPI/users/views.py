from typing import Optional

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import action

from .serializers import UserSerializer
from .models import CustomUser, VerificationCode
from .mailing import send_code_message
from .services import verify_email
from CodeVersusAPI.permissions import IsAuthCustom


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        registration_code = VerificationCode(
            user=user
        )
        registration_code.save()
        send_code_message(
            title="Registration",
            receiver=user.email,
            code=registration_code.id
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        queryset = CustomUser.objects.filter(pk=user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=["post"], detail=False, permission_classes=(permissions.AllowAny,))
    def verify_email(self, request):
        code = request.data.get("code")
        verify_email(code)
        return Response({"result": "success"}, status=200)




