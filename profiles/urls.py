from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
	url(r'^$', ProfileView.as_view(), name='profile'),
    
	
]