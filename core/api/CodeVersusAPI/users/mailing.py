import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from CodeVersusAPI.settings import MAIL_ADDRESS, MAIL_PASSWORD
from CodeVersusAPI.exceptions import InvalidEmail


def send_message(title_msg: str, receiver: str, message: str):
    msg = MIMEMultipart()
    msg['From'] = MAIL_ADDRESS
    msg['To'] = receiver
    msg['Subject'] = title_msg
    msg.attach(MIMEText(message, 'html'))

    text = msg.as_string()
    try:
        with smtplib.SMTP_SSL("smtp.mail.ru", 465) as server:
            server.login(MAIL_ADDRESS, MAIL_PASSWORD)
            server.sendmail(MAIL_ADDRESS, receiver, text)
    except Exception:
        raise InvalidEmail


def send_code_message(title: str, receiver: str, code: str):
    title_msg = f"CodeVersus | {title}"
    message = f"""\
    <html>
      <head></head>
      <body>
        <h1>{title}</h1><br>
        <p>Your code - {code}</p>
      </body>
    </html>
    """
    send_message(title_msg, receiver, message)