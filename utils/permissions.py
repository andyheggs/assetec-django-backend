from rest_framework.permissions import BasePermission, SAFE_METHODS

# Custom permission to only allow owners of an object to edit it.
class IsOwnerOrReadOnly(BasePermission):
    
    # Check object-level permission
    def has_object_permission(self, request, view, obj):
        
        # If request method is considered safe (e.g., GET, HEAD, OPTIONS), allow auth
        if request.method in SAFE_METHODS:
            return True
        
        # Otherwise, only allow access if user is owner of the object
        return request.user == obj.owner