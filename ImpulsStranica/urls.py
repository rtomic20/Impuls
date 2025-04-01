from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

class LogoutViewAllowGET(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
app_name = "ImpulsStranica"

glavnic_urls = [
    path('', views.home, name='home'),
]

korisnik_funk=[
    path('ulogiran/', views.ulogiran_view, name='ulogiran'),
    path('logout/', LogoutViewAllowGET.as_view(next_page='ImpulsStranica:home'), name='logout'),
]
registracija_urls = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]

urlpatterns = glavnic_urls + registracija_urls+ korisnik_funk