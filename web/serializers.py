from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'