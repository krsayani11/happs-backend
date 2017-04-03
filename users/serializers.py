from rest_framework import serializers
from .models import User, Friends

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'username', 'user_id', 'authentication_token')

class FriendsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Friends
		fields = ('created', 'creator', 'friend')
