from rest_framework import serializers
from .models import MoodEntry, SelfCare, AnonymousPost, Comment

class MoodEntrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  #user field is hidden from being manually set or edited and it's automatically set to whoever is logged in

    class Meta:
        model = MoodEntry
        fields = ['id', 'user', 'mood', 'note', 'created_at']
        read_only_fields = ['id', 'created_at', 'user'] # These fields cannot be modified by the client.


class SelfCareSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SelfCare
        fields = ['id', 'user', 'activity', 'category', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']


class AnonymousPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AnonymousPost
        fields = ['id', 'category', 'content', 'created_at']  #user is fully anonymous (not showing in the output)
        read_only_fields = ['id', 'created_at', 'user']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at'] #user is fully anonymous (not showing in the output)
        read_only_fields = ['id', 'created_at', 'user']