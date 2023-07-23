import time

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from celery import shared_task


@shared_task()
def send_verification_email_task(verification_code: str, recipient_email: str, message_title: str):
    email_msg = EmailMessage(
        subject="Registration | Code Versus",
        from_email=settings.EMAIL_HOST_USER,
        body=render_to_string("mail.html", {
            "title": f"{message_title} | CodeVersus",
            "code": verification_code,
        }),
        to=[recipient_email]
    )
    email_msg.content_subtype = "html"
    email_msg.send()