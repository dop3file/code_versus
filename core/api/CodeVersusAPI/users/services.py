from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import VerificationCode, CustomUser
from CodeVersusAPI.exceptions import InvalidEmail


class RegistrationLogic:
    @staticmethod
    def verify_email(code: str):
        verification_code = VerificationCode.objects.get(id=code)
        if verification_code is None:
            raise InvalidEmail
        user: CustomUser = verification_code.user
        user.is_activate = True
        user.save()

    @staticmethod
    def send_verification_email(verification_code: str, recipient_email: str):
        email_msg = EmailMessage(
            subject="Registration | Code Versus",
            from_email=settings.EMAIL_HOST_USER,
            body=render_to_string("mail.html", {
                "title": "Registartion | CodeVersus",
                "code": verification_code,
            }),
            to=[recipient_email]
        )
        email_msg.content_subtype = "html"
        email_msg.send()


