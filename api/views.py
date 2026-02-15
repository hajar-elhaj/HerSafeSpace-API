from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import MoodEntry, SelfCare, AnonymousPost, Comment
from .serializers import MoodEntrySerializer, SelfCareSerializer, AnonymousPostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow owners of an object to edit or delete it, Meanwhile read access is allowed for anyone
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #means the request is GET
            return True # Anyone can read
        return obj.user == request.user # returns True if it's the owner who made the request and false if it's not

class MoodEntryViewSet(viewsets.ModelViewSet):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Only logged-in users and owner

    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user) # Users only see their own mood entries
    
    # overriding the perform_create method to automatically assign the logged-in user and prevent spoofing
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Automatically assign the logged-in user


class SelfCareViewSet(viewsets.ModelViewSet):
    queryset = SelfCare.objects.all()
    serializer_class = SelfCareSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return SelfCare.objects.filter(user=self.request.user) # Users only see their own self-care entries
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnonymousPostViewSet(viewsets.ModelViewSet):
    queryset = AnonymousPost.objects.all()
    serializer_class = AnonymousPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # User must be logged in to post
    
    def get_queryset(self):
        return AnonymousPost.objects.all() # All users can see posts
    
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user) # Users can only edit/delete their own posts


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.request.query_params.get('post') # filtering by post id if passed in query params
        if post_id:
            return Comment.objects.filter(post__id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Assign the logged-in user automatically