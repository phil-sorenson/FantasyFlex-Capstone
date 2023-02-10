from django.urls import path
from . import views


urlpatterns = [
    path('login/<str:username>', views.login),
    path('users', views.logged_user)
]
