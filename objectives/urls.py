from django.urls import path
from . import views

app_name = 'objectives'
urlpatterns = [
    path('', views.index, name='index'),
]