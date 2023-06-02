from rest_framework import serializers
from api import models
from django.contrib.auth.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

