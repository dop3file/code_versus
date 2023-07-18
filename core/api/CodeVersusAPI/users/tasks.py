import time

from celery import shared_task
from .services import RegistrationLogic


@shared_task()
def send_verification_email_task(verification_code: str, recipient_email: str):
    return RegistrationLogic.send_verification_email(verification_code, recipient_email)