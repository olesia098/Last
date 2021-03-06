from django.urls import path
from client.views import *

urlpatterns =[
    path('register/', RegisterView.as_view()),
    path('activate/<uuid:activation_code>/', ActivateView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
]