
from django.urls import path

from . import views

urlpatterns = [
    path('createURL', views.createURL, name='create'),
    path('<hash>', views.getURL, name='getURL')
]