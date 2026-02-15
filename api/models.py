from django.db import models
from django.contrib.auth.models import User

# MoodEntry model - tracks user moods
class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('confident', 'Confident'),
        ('relaxed', 'Relaxed'),
        ('motivated', 'Motivated'),
        ('frustrated', 'Frustrated'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('anxious', 'Anxious'),
        ('neutral', 'Neutral'),
        ('bored', 'Bored'),
        ('irritated', 'Irritated'),
        ('nervous', 'Nervous'),
        ('stressed', 'Stressed'),
        ('overwhelmed', 'Overwhelmed'),
        ('lonely', 'Lonely'),
        ('jealous', 'Jealous'),
        ('disappointed', 'Disappointed'),
        ('hopeless', 'Hopeless'),
        ('insecure', 'Insecure'),
        ('tired', 'Tired'),
        ('drained', 'Drained'),
        ('unsure', 'Unsure'),
        ('sensitive', 'Sensitive'),
        ('vulnerable', 'Vulnerable'),
        ('thoughtful', 'Thoughtful'),
        ('ashamed', 'Ashamed'),
        ('guilty', 'Guilty'),
        ('defensive', 'Defensive'),
        ('detached', 'Detached'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moods')
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.created_at.strftime('%Y-%m-%d')}"

# SelfCare model - tracks self-care activities
class SelfCare(models.Model):
    CATEGORY_CHOICES = [
        ('exercise', 'Exercise'),
        ('meditation', 'Meditation'),
        ('reading', 'Reading'),
        ('hobby', 'Hobby'),
        ('journaling', 'Journaling'),
        ('sleep', 'Sleep'),
        ('walk', 'Walk'),
        ('healthy_meal', 'Healthy Meal'),
        ('hydration', 'Hydration'),
        ('socializing', 'Socializing'),
        ('therapy', 'Therapy'),
        ('skincare', 'Skincare'),
        ('music', 'Music'),
        ('nature', 'Nature'),
        ('other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selfcare')
    activity = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity} ({self.category})"

# AnonymousPost model - users can post anonymously
class AnonymousPost(models.Model):
    CATEGORY_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('self_care', 'Self-Care'),
        ('relationship', 'Relationship'),
        ('career', 'Career'),
        ('hobby', 'Hobby'),
        ('lifestyle', 'Lifestyle'),
        ('fitness', 'Fitness'),
        ('nutrition', 'Nutrition'),
        ('education', 'Education'),
        ('spirituality', 'Spirituality'),
        ('travel', 'Travel'),
        ('technology', 'Technology'),
        ('finance', 'Finance'),
        ('productivity', 'Productivity'),
        ('creativity', 'Creativity'),
        ('wellness', 'Wellness'),
        ('entertainment', 'Entertainment'),
        ('parenting', 'Parenting'),
        ('community', 'Community'),
        ('childhood', 'Childhood'),
        ('therapy', 'Therapy'),
        ('other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # hidden
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.content[:30]}..."

# Comment model - comments on anonymous posts
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(AnonymousPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # hidden
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.id} by {self.user.username if self.user else 'Anonymous'}"