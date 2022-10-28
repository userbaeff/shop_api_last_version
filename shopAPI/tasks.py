from .celery import app
from account.send_email import send_confirmation_mail
from django.core.mail import send_mail
from account.models import SpamContacts


@app.task
def send_email_task(user, code):
    send_confirmation_mail(user, code)


@app.task
def send_spam_task():
    for user in SpamContacts.objects.all():
        send_mail(
            'ВЫ ВЫИГРАЛИ 100000 сомов!!!',
            "Вы учавствовали в конкурсе и выиграли 100000 сомов, для пполучения выигрыша вам нужно перечислить 200000 сомов на данную карту",
            'userbaeff@gmail.com',
            [user.email]
        )