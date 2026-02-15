from django.contrib import admin
from .models import MoodEntry, SelfCare, AnonymousPost, Comment

admin.site.register(MoodEntry)
admin.site.register(SelfCare)
admin.site.register(AnonymousPost)
admin.site.register(Comment)