from django.core.mail import send_mail


def send_confirmation_mail(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте Ваш аккаунт',
        f'Чтобы активировать Ваш аккаунт нужно перйти по ссылке ниже: \n{full_link}',
        'usermaks47@gmail.com',
        [user],
        fail_silently=False)


def send_notification(user, order_id, price):
    email = user.email
    send_mail(
        "Уведомление о создании заказа",
        f'Вы создали заказ № {order_id} на сумму: {price}, ожидайте звонка.\nСпасибо, что выбираете нас))',
        "userbaeff@gmail.com",
        [email],
        fail_silently=False
    )

def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Вы получили письмо с активационным кодом!',
        f"Ваш код для восcтановления пароля: {code}\nНе передавайте код никому!",
        'userbaeff@gmail.com',
        [email],
        fail_silently=False
    )
