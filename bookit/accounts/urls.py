from django.urls import path
from .views import CreateUserAPIView, LoginAPIView

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
