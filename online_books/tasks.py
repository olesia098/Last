import time
from django.core.mail import send_mail
from online_books.celery import app


@app.task
def send_confirmation_email(code, email):
    time.sleep(10)
    full_link = f'http://localhost:8000/v1/api/client/activate/{code}'
    send_mail(
        'Привет', # title
        full_link, # body
        '5kanolesya@gmail.com', # from email
        [email] # to email
    )