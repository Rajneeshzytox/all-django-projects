from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.signin, name='sign In'),
    path('logout/', views.signout, name='sign Out'),
    path('registration/', views.signup, name='sign up'),
]