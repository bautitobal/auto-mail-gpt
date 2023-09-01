import imaplib
import email
from email.header import decode_header
from my_tokens import EMAIL_ADDRESS, EMAIL_PASSWORD, IMAP_SERVER

# Acá los datos de tu correo
def leer_correos():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    # Mail + password
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "UNSEEN")
    correos = []

    for num in messages[0].split():
        status, msg_data = mail.fetch(num, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()

        correos.append({
            "asunto": subject,
            "cuerpo": body,
            "destinatario": msg["From"]
        })

    mail.logout()
    return correos

def obtener_contenido(correo):
    return correo["asunto"], correo["cuerpo"]
