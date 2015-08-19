from email.mime.text import MIMEText
from smtplib import SMTP


class Mail:
    remitente = "lahermandad@gmail.com"
    clave = "festivalAcolor"

    def __init__(self):
        super(self)

    def __init__(self, usuario, clave):
        self.remitente = usuario
        self.clave = clave


    def sendMesagge(self, destinatarios, asunto, mensaje):
        mime_message = MIMEText(mensaje, "html", _charset="utf-8")
        mime_message["From"] = self.remitente
        mime_message["To"] = destinatarios
        mime_message["Subject"] = asunto

        smtp = SMTP("mail.recursospython.com")
        smtp.login(self.remitente, self.clave)
        smtp.sendmail(self.remitente, destinatarios, mime_message.as_string())
        smtp.quit()
