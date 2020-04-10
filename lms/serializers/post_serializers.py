from rest_framework import serializers
from lms.models.post_models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
