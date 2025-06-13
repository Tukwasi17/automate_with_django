from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    #execute a time consuning task here
    celery_test_task.delay()
    return HttpResponse('<h3>function executed successfully</h3>')