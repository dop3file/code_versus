from .models import VerificationCode, CustomUser
from CodeVersusAPI.exceptions import InvalidEmail


def verify_email(code: str):
    verification_code = VerificationCode.objects.get(id=code)
    if verification_code is None:
        raise InvalidEmail
    user: CustomUser = verification_code.user
    user.is_activate = True
    user.save()
