from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.logout_page, name="logout"),
    path('logout', views.login_page, name="login"),
    path('assignments/', views.assignment_list, name='assignments'),
    path('assignments/<int:assignment_id>/', views.assignment_details, name='assignment_details'),
    path('submit_quiz/<int:assignment_id>/', views.submit_quiz, name='submit_quiz'),
    

]
