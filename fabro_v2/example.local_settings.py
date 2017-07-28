import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fabro_v2',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    },
    'old': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'old_fabro',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    },

}
