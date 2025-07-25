from django.urls import path
from . import views

app_name = 'objectives'
urlpatterns = [
    path('', views.index, name=f'{app_name}-index'),
    path('<uuid:objective_id>', views.complete_objective, name=f'{app_name}-complete'),
]