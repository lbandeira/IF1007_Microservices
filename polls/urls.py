from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('test/', views.test, name = 'test'),
    path('signup/', views.signup, name='signup'),
]