from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from api.serializers import Userserializer
from django.contrib.auth.models import User

# Create your views here.
class UsersView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=Userserializer
    queryset=User.objects.all()
