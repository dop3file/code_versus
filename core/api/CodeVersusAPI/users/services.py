from .models import VerificationCode, CustomUser, VerificationCodeType
from CodeVersusAPI.exceptions import InvalidEmail
from .tasks import send_verification_email_task


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
    def verify_reset_password(code: str, new_password: str):
        print(code, new_password)
        verification_code = VerificationCode.objects.get(id=code, code_type=VerificationCodeType.RESET.value)
        current_user = verification_code.user
        current_user.set_password(new_password)
        current_user.save()

    @staticmethod
    def reset_password(recipient_email: str):
        try:
            current_user = CustomUser.objects.get(email=recipient_email)
        except CustomUser.DoesNotExist:
            raise InvalidEmail
        verification_code = VerificationCode(user=current_user, code_type=VerificationCodeType.RESET.value)
        verification_code.save()
        send_verification_email_task.delay(verification_code.id, recipient_email, "Reset Password")


