from django.contrib import admin

from .models import Friend, ScoreCard, ActivityLog, LearningProfile, LearningHistory, LearningQueue

admin.site.register(ScoreCard)
admin.site.register(Friend)
admin.site.register(ActivityLog)
admin.site.register(LearningHistory)
admin.site.register(LearningProfile)
admin.site.register(LearningQueue)
