import smtplib
from email.mime.text import MIMEText
from my_tokens import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER

def enviar_correo(destinatario, asunto, mensaje):
    # Tu mail
    from_email = EMAIL_ADDRESS
    to_email = destinatario

    msg = MIMEText(mensaje)
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = asunto

    server = smtplib.SMTP(SMTP_SERVER, 587)
    server.starttls()
    # Tu password de tu mail
    server.login(from_email, EMAIL_PASSWORD)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
