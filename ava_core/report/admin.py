from django.contrib import admin

from .models import ReportResponse, Suspicious, Question

admin.site.register(Question)
admin.site.register(Suspicious)
admin.site.register(ReportResponse)
