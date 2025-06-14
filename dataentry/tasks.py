from awd_main.celery import app
import time
from django.core.management import call_command
from .utils import send_email_notification
from django.conf import settings


@app.task
def celery_test_task():
    time.sleep(5)# simulation of any task that's going to take 10seconds
    # send an email
    mail_subject = 'Test subject'
    message = 'This a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)

    return 'Email sent successfully!.'


@app.task
def import_data_task(file_path, model_name):
    #trigger the import data command
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    # notify the user by email
    mail_subject = 'Import Data Completed'
    message = 'Your data import has been successful!'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Data imported successfully!'