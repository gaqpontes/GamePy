from django.urls import path
from . import views

app_name = 'integrations'
urlpatterns = [
    path('', views.index, name=f'{app_name}-index'),
]