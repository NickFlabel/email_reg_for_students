from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view()),
    path('activate/<str:token>/', views.activate),
    path('login', LoginView.as_view())
]
