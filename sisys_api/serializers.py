#from requests import request
from rest_framework import serializers

from sisys_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class TagSerializer(serializers.ModelSerializer):
    """Serializes tag items"""

    class Meta:
        model = models.Tag
        fields = ('id', 'text')
        extra_kwargs = {'owner': {'read_only': True}}


class TagCurrentUserSerializer(serializers.PrimaryKeyRelatedField):
    """Serializer tag items by current user"""
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(TagCurrentUserSerializer, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user)

class InfoSerializer(serializers.ModelSerializer):
    """Serializes info items"""

    tags = TagCurrentUserSerializer(queryset=models.Tag.objects, many=True)

    class Meta:
        model = models.Info
        fields = ('id',
            'owner',
            'created_on',
            'updated_on',
            'title',
            'text',
            'tags')
        extra_kwargs = {'owner': {'read_only': True}}