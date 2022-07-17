import settings
import email_templates
from redmail import EmailSender

class Email:

    def __init__(self):
        pass


    def receipt(self, obj):
        # https://productivity.godaddy.com/settings#/mailbox/23657326
        self.send_outlook('Enrollment receipt',email_templates.receipt(obj), obj["recipients"])


    def course_welcome(self,obj):
        self.send_outlook('Welcome to Phostrino', email_templates.course_welcome(obj), obj["recipients"])



    def send_outlook(self,subject,body, recipients):
        email = EmailSender(
                host='smtp.office365.com',
                port='587',
                username=settings.COMPANY_EMAIL,
                password=settings.COMPANY_EMAIL_PASSWORD
            )

        email.send(
            subject=subject,
            sender=settings.COMPANY_EMAIL,
            receivers= recipients,
            html=body
        )

    def phostrino_alert(self,subject,body, recipients):
        if settings.ERROR_REPORT:
            self.send_outlook(subject,body,recipients)
