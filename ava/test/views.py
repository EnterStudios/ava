from django.shortcuts import get_object_or_404
from django.views import generic

from ava.test.models import Test
from ava.test_email.models import EmailTest
from ava.test_twitter.models import TwitterTest
from ava.core_project.models import Project


class TestDashboardView(generic.ListView):
    template_name = 'test/test_dashboard.html'
    model = Test
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(TestDashboardView, self).get_context_data(**kwargs)

        context['project_list'] = Project.objects.filter(owner=self.request.user)

        context['tests_new'] = self.test_count_by_status(Test.NEW)
        context['tests_running'] = self.test_count_by_status(Test.RUNNING)
        context['tests_complete'] = self.test_count_by_status(Test.COMPLETE)
        context['tests_error'] = self.test_count_by_status(Test.ERROR)
        context['tests_scheduled'] = self.test_count_by_status(Test.SCHEDULED)

        return context

    def test_count_by_status(self, status):
        count = TwitterTest.objects.filter(user=self.request.user, teststatus=status).count()
        count = count + EmailTest.objects.filter(user=self.request.user, teststatus=status).count()
        return count

    def get_queryset(self):
        return Test.objects.filter(user=self.request.user)


class TestProjectDashboardView(generic.ListView):
    template_name = 'test/test_project_dashboard.html'
    model = Test
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(TestProjectDashboardView, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        if pk:
            project = get_object_or_404(Project, pk=pk)
            context['project'] = project

        context['tests_new'] = self.test_count_by_status(Test.NEW)
        context['tests_running'] = self.test_count_by_status(Test.RUNNING)
        context['tests_complete'] = self.test_count_by_status(Test.COMPLETE)
        context['tests_error'] = self.test_count_by_status(Test.ERROR)
        context['tests_scheduled'] = self.test_count_by_status(Test.SCHEDULED)

        context['email_test_list'] = EmailTest.objects.filter(user=self.request.user)
        context['twitter_test_list'] = TwitterTest.objects.filter(user=self.request.user)
        return context

    def test_count_by_status(self, status):
        count = TwitterTest.objects.filter(user=self.request.user, teststatus=status).count()
        count = count + EmailTest.objects.filter(user=self.request.user, teststatus=status).count()
        return count

    def get_queryset(self):
        return Test.objects.filter(user=self.request.user)
