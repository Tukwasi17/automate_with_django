from django.apps import apps

def get_all_custom_models():
    # excluding the name 
    default_models = ['ContentType', 'Session', 'LogEntry', 'Group', 'Permission', 'User', 'Upload']
    # try to get all the apps
    custom_models = []
    for model in apps.get_models():
        # get the only the name
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
        #print(model)
    return custom_models    