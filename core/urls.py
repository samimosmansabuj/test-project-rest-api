
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import AuthTokenView, CreateUserView, AuthTokenView, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('token/', AuthTokenView.as_view(), name='token_obtain_pair'),
    path('user/create/', CreateUserView.as_view(), name='create_user'),
    
    path('products/', include(router.urls)),
]

# urlpatterns += router.urls

