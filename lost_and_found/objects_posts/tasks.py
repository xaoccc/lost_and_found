from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import redirect

from lost_and_found import settings


@shared_task
def send_register_email(request):
    subject = 'Login Notification',
    message = 'You have logged in successfully.',
    email_from = settings.EMAIL_HOST_USER,
    recipient_list = [request.user.email],
    send_mail( subject, message, email_from, recipient_list )

    return redirect('index')

