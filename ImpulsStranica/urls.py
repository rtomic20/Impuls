from django.urls import path
from .views import home
app_name="ImpulsStranica"

glavnic_urls=[
    path('',home,name='home')
]

urlpatterns = glavnic_urls

