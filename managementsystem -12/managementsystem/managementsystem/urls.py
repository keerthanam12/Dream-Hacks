from django.urls import path
from . import views
from .views import assignment_list, take_assignment



urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.logout_page, name="logout"),
    path('logout', views.login_page, name="login"),
    path('assignments1', views.assignment_list, name='assignment_list'),
    path('assignments1/<int:assignment_id>', views.take_assignment, name='take_assignment'),
    
    path('assignments1/<int:assignment_id>', views.assignment_detail, name='assignment_detail')

    

]
