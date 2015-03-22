import json
from django.views import generic
from django.shortcuts import get_object_or_404
from apps.ava_test.models import TestResult
from apps.ava_test_email.models import EmailTestTarget
from apps.ava_test_twitter.models import TwitterTestTarget

class RecordTestResultView(generic.TemplateView):
    class Meta:
        abstract = True
    
    TRACKING_FIELDS = {
                       'ipaddress':     'REMOTE_ADDR',
                       'method':        'REQUEST_METHOD',
                       'host':          'HTTP_HOST',
                       'path':          'PATH_INFO',
                       'contentlength': 'CONTENT_LENGTH',
                       'contenttype':   'CONTENT_TYPE',
                       'ua':            'HTTP_USER_AGENT',
                       'referrer':      'HTTP_REFERER',
                       'via':           'HTTP_VIA',
                      }

    def get(self, request, *args, **kwargs):
        token = self.kwargs.get('token')
        if token:
            self.record_token(token)
        return super(RecordTestResultView, self).get(request, *args, **kwargs)
    
    def get_template_names(self):
        return 'tracking/success.html'
    
    def get_result_info(self, target):
        result_info = {'target':target}
        
        for field_name, meta_name in self.TRACKING_FIELDS.iteritems():
            if meta_name in self.request.META:
                result_info[field_name] = self.request.META[meta_name]

        return result_info
    
    def record_token(self, token):
        pass

class RecordEmailTestResultView(RecordTestResultView):
    def record_token(self, token):
        target = get_object_or_404(EmailTestTarget, token=token)
        result_info = self.get_result_info(target)
        target.results.create(**result_info)

class RecordTwitterTestResultView(RecordTestResultView):
    def record_token(self, token):
        target = get_object_or_404(TwitterTestTarget, token=token)
        result_info = self.get_result_info(target)
        target.results.create(**result_info)
