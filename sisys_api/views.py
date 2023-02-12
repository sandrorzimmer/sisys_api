from tokenize import TokenError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
#from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from sisys_api import serializers
from sisys_api import models
from sisys_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)

    def get_queryset(self):
        """Users get only their own profile"""
        user = self.request.user
        return models.UserProfile.objects.filter(name=user.name)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class TagViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating tag items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnTag, IsAuthenticated)
    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()

    def get_queryset(self):
        """User get only their own tags"""
        user = self.request.user
        return models.Tag.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Sets the owner to the logged in user"""
        serializer.save(owner=self.request.user)

class InfoFilter(filters.FilterSet):
    class Meta:
        model = models.Info
        fields = {
            'title': ['icontains'],
            'text': ['icontains'],
            'tags': ['exact'],
        }

class InfoViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating info items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnInfo, IsAuthenticated)
    serializer_class = serializers.InfoSerializer
    queryset = models.Info.objects.all()
    #filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_backends = (filters.DjangoFilterBackend,)
    #filterset_fields = ['title', 'text', 'tags']
    #search_fields = ('title', 'text')
    filterset_class = InfoFilter
    ordering_fields = ('title', 'text')
    ordering = ('title',)

    def get_queryset(self):
        """User get only their own info"""
        user = self.request.user
        return models.Info.objects.filter(owner=user)

    def perform_create(self, serializer):
        """Sets the owner to the logged in user"""
        serializer.save(owner=self.request.user)

###        