from django.shortcuts import render
from .serializers import CreateUserSerializer, AuthTokenSerializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

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

