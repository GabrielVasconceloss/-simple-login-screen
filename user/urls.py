from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('home/', views.Home.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/',  views.login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('platform/', views.platform, name='platform'),
]