
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import AuthTokenView, CreateUserView, AuthTokenView

urlpatterns = [
    path('token/', AuthTokenView.as_view(), name='token_obtain_pair'),
    path('user/create/', CreateUserView.as_view(), name='create_user'),
]
