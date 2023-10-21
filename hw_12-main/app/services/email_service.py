import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# генерація унікальний токен підтвердження для користувача
verification_token = generate_unique_token()

# відправлення листа з посиланням для підтвердження
def send_verification_email(email, verification_token):
    # Параметри SMTP-сервера та ваші дані
    smtp_server = "smtp.yourserver.com"
    smtp_port = 587
    smtp_username = "your_username"
    smtp_password = "your_password"

    # створення повідомлення
    msg = MIMEMultipart()
    msg["From"] = "your_email@yourserver.com"
    msg["To"] = email
    msg["Subject"] = "Підтвердження електронної адреси"

    # текст повідомлення
    body = f"Для підтвердження електронної адреси перейдіть за посиланням: http://yourapp.com/verify?token={verification_token}"
    msg.attach(MIMEText(body, "plain"))

    # підключитися до SMTP-сервера і надіслати повідомлення
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail("your_email@yourserver.com", email, text)
        server.quit()
        print("Лист успішно відправлено")
    except Exception as e:
        print(f"Помилка відправки листа: {str(e)}")

# викликати функцію для надсилання листа з посиланням
send_verification_email("user@example.com", verification_token)
