from django.contrib import admin

from apps.ava_test_twitter.models import *

admin.site.register(TwitterTest)
admin.site.register(TwitterTestType)
admin.site.register(TwitterAccount)
admin.site.register(TweetTemplate)
admin.site.register(TweetLink)

