from rest_framework import serializers
from .models import MoodEntry, SelfCare, AnonymousPost, Comment

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = '__all__'

class SelfCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfCare
        fields = '__all__'

class AnonymousPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'