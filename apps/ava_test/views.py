from django.views import generic
from django.shortcuts import get_object_or_404

from apps.ava_test.models import Test, TestType
from apps.ava_test_email.models import EmailTest
from apps.ava_test_twitter.models import TwitterTest

class TestIndexView(generic.ListView):
    template_name = 'test/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test']=None
        return Test.objects.filter(user=self.request.user)

class TestOrgIndexView(generic.ListView):
    template_name = 'test/vieworg.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(TestOrgIndexView, self).get_context_data(**kwargs)
        context['test_modules'] = TestType.objects.all()
        pk = self.kwargs.get('pk')
        if pk:
            testorg = get_object_or_404(Organisation, pk=pk)
            context['tests_new'] = self.test_count_by_status(Test.NEW,testorg)
            context['tests_running'] = self.test_count_by_status(Test.RUNNING,testorg)
            context['tests_complete'] = self.test_count_by_status(Test.COMPLETE,testorg)
            context['tests_error'] = self.test_count_by_status(Test.ERROR,testorg)
            context['tests_scheduled'] = self.test_count_by_status(Test.SCHEDULED,testorg)
    #       context['tests_new'] = self.test_count_by_status(teststatus=Test.NEW,test)
        context['organisation_id'] = self.request.session['organisation']
        return context

    def test_count_by_status(self, status, organisation):
        count = TwitterTest.objects.filter(user=self.request.user, org=organisation, teststatus=status).count()
        count = count + EmailTest.objects.filter(user=self.request.user, org=organisation, teststatus=status).count()
        return count

    def get_queryset(self):
        self.request.session['test']=None
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(Organisation, pk=pk)
            self.request.session['organisation']=pk
        return Test.objects.filter(user=self.request.user,org=test)



