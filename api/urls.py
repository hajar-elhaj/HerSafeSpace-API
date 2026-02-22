from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodEntryViewSet, SelfCareViewSet, AnonymousPostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'moods', MoodEntryViewSet, basename='mood')
router.register(r'selfcare', SelfCareViewSet, basename='selfcare')
router.register(r'posts', AnonymousPostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]