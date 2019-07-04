from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('test/', views.test, name = 'test'),
    path('equipamento_list/', views.equipamento_list, name = 'equipamento_list'),
    path('search/', views.SearchResultsView, name='search_results'),
    path('signup/', views.signup, name='signup'),

   
]