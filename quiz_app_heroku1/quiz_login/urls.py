
from django.urls import path
from .import views

urlpatterns = [

    path('', views.login_1, name='login'),
]