# Rest Imports
from rest_framework import permissions


class IsFish(permissions.BasePermission):
    message = "Flipping fish did it"
    SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return request.method in self.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return request.method in self.SAFE_METHODS

# # Implementation
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read/edit it.
    """

    def has_object_permission(self, request, view, obj):
        # permissions are only allowed to the owner of the item.
        return obj.owner is request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in self.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the item.
        return obj.owner is request.user


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owner or admin of an object.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only available to admin or the owner of the item.
        if request.user.is_superuser:
            return True

        if request.user == obj.owner:
            return True

        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in self.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin.
        return request.user.is_superuser


#
class IsAccessDenied(permissions.BasePermission):
    """
    Custom permission to allow nothing
    """

    def has_permission(self, request, view):
        # Write permissions are only allowed to the owner of the item.
        return False


#
#
class IsCreateDenied(permissions.BasePermission):
    """
    Custom permission to prevent create.
    """

    def has_permission(self, request, view):
        # Create permission is removed.
        return request.method is not 'POST'


#
# class IsRetrieveDenied(permissions.BasePermission):
#     """
#     Custom permission to prevent retrieve.
#     """
#
#     def has_permission(self, request, view):
#         # Retrieve permission is removed.
#         return request.method != 'GET'
#
#
class IsUpdateDenied(permissions.BasePermission):
    """
    Custom permission to prevent update.
    """
    BANNED_METHODS = ('PUT')

    def has_permission(self, request, view):
        if request.method in self.BANNED_METHODS:
            return False

            # def has_permission(self, request, view):
            #     # Update permissions is removed.
            #     return request.method is not 'PUT'


class IsDeleteDenied(permissions.BasePermission):
    SAFE_METHODS = ('GET','PUT','POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        # Only accept post request.
        return request.method in self.SAFE_METHODS


class IsCreateOrRetrieveOnly(permissions.BasePermission):
    SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return request.method in self.SAFE_METHODS


class IsAdminOrCreateDenied(permissions.BasePermission):
    """
    Custom permission to prevent create, unless admin.
    """

    def has_permission(self, request, view):
        # Create permission is removed if not admin
        return request.user.is_superuser or \
               request.method != 'PUSH'


class IsAdminOrRetrieveDenied(permissions.BasePermission):
    """
    Custom permission to prevent retrieve, unless admin.
    """

    def has_permission(self, request, view):
        # Retrieve permission is removed if not admin
        return request.user.is_superuser or \
               request.method != 'GET'


class IsAdminOrUpdateDenied(permissions.BasePermission):
    """
    Custom permission to prevent update, unless admin.
    """

    def has_object_permission(self, request, view, obj):
        # Update permission is removed if not admin

        if request.user.is_superuser:
            return True

        if request.method != 'PUT':
            return True

        return False


class IsAdminOrDeleteDenied(permissions.BasePermission):
    """
    Custom permission to prevent delete, unless admin.
    """
    # SAFE_METHODS = ('GET', 'PUT','POST', 'HEAD', 'OPTIONS')
    #
    # def has_permission(self, request, view):
    #     if request.user.is_superuser:
    #         return True
    #
    #     return request.method in self.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return request.method != 'DELETE'





class IsCreateOnly(permissions.BasePermission):
    """
    Custom permission to only enable create.
    """
    SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        return request.method in self.SAFE_METHODS


class IsRetrieveOnly(permissions.BasePermission):
    """
    Custom permissions to only enable retrieve.
    """
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        # Only accept get request.
        return request.method in self.SAFE_METHODS


class IsUpdateOnly(permissions.BasePermission):
    """
    Custom permission to only enable update.
    """
    SAFE_METHODS = ('PUT', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        # Only accept put request.
        return request.method in self.SAFE_METHODS


class IsDeleteOnly(permissions.BasePermission):
    """
    Custom permissions to only enable delete.
    """
    SAFE_METHODS = ('DELETE', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        # Only accept delete request.
        return request.method in self.SAFE_METHODS
