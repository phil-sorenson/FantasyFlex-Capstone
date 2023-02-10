from django.urls import path
from . import views


urlpatterns = [
    path ('login', views.login),
    # path('<int:user_id>', views.UserData)
]