from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnTag(permissions.BasePermission):
    """Allow user to get and edit only their own tags"""
    
    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to get or update their own tag"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner.id == request.user.id


class UpdateOwnInfo(permissions.BasePermission):
    """Allow user to get and edit only their own info"""
    
    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to get or update their own tag"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner.id == request.user.id        