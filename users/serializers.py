from rest_framework import serializers
from .models import User, Friends, Friendship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'user_id', 'authentication_token', 'picture')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('members')

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('person', 'friends', 'status')
