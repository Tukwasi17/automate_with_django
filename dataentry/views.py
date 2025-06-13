from django.shortcuts import render, redirect
from django.conf import settings
from uploads.models import Upload
from .utils import get_all_custom_models, check_csv_errors
#from django.core.management import call_command
from django.contrib import messages
from .tasks import import_data_task

# Create your views here.
def import_data(request):
    if request.method == 'POST':
        #taken for file path
        file_path = request.FILES.get('file_path')
        # taken for 'post'
        model_name = request.POST.get('model_name')
        #print('file_path=> ', file_path)
        #print('model_name=> ', model_name)
        #Store this file inside the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        #construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        file_path = base_url+relative_path
        #print(file_path)
        #print(relative_path)
        #print(base_url)

        #check csv errors
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import_data')

        # Handle the import data task here
        import_data_task.delay(file_path, model_name)
        # Show the message to the user
        messages.success(request, 'Your data is being imported , you will be notefied once the data is imported')
        return redirect('import_data')
    else:
        #
        custom_models = get_all_custom_models()
        #print(all_models)
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)