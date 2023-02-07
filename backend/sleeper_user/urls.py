from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import RegisterView, MyTokenObtainPairView

urlpatterns = [
    path ('login', views.login_user),
    path('<int:user_id>', views.UserData)
]