from django.shortcuts import render
from rest_framework import generics
from .serializers import UserAPIListSerializer
from django.contrib.auth import get_user_model
# Create your views here.
class UserListAPIView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserAPIListSerializer