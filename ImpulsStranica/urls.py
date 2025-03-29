from django.urls import path
from . import views

app_name = "ImpulsStranica"

glavnic_urls = [
    path('', views.home, name='home'),
]

registracija_urls = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]

urlpatterns = glavnic_urls + registracija_urls