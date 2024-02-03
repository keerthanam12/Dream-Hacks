from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.logout_page, name="logout"),
    path('logout', views.login_page, name="login"),
    
    
    

]
