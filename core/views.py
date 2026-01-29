from django.shortcuts import render
from .serializers import CreateUserSerializer, AuthTokenSerializer, ProductSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from .models import Product
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permisons import IsAdminCreateOnly
# from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError

class CreateUserView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "User created successfully",
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )

class AuthTokenView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "success": True,
                    "data": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST
        )

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminCreateOnly]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "status": True,
                    "data": serializer.data,
                }
            )
        except ValidationError as ve:
            error = {key: str(value[0]) for key, value in ve.detail.items()}
            return Response(
                {
                    "status": False,
                    "errors": error,
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "errors": str(e),
                }, status=status.HTTP_400_BAD_REQUEST
            )

