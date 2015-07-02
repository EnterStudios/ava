from django.contrib import admin

from . import models

admin.site.register(models.TwitterTest)
admin.site.register(models.TwitterAccount)
admin.site.register(models.TweetTemplate)
admin.site.register(models.TweetLink)
