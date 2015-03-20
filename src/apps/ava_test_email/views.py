from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps.ava_test_email.models import EmailTest, EmailTestTarget
from apps.ava_test.models import Test
from apps.ava_test_email.forms import EmailTestForm
from apps.ava_core_identity.models import Person, Identifier
from apps.ava_test_email.tasks import run_email_test


class EmailTestIndex(generic.ListView):
    template_name = 'email/test_email_index.html'
    context_object_name = 'list'
    model = EmailTest

class EmailTestDetail(generic.DetailView):
    model = EmailTest
    context_object_name = 'test'
    template_name = 'email/test_email_detail.html'
    
    test = None

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            self.test = get_object_or_404(EmailTest, pk=pk)
            request.session['test'] = self.test.id
        return super(EmailTestDetail, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(EmailTestDetail, self).get_context_data(**kwargs)
        status_names = dict(EmailTest.STATUS_CHOICES)
        context_data['test_status'] = status_names[self.test.teststatus]
        return context_data


class EmailTestDelete(DeleteView):
    model = EmailTest
    template_name = 'confirm_delete.html'
    
    def get_success_url(self):
        return reverse('email-test-index')


class EmailTestCreate(generic.CreateView):
    model = EmailTest
    template_name = 'email/test_email.html'
    form_class = EmailTestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.teststatus = Test.NEW
        form.instance.testtype =
        result = super(EmailTestCreate, self).form_valid(form)
        self.success_url = form.instance.get_absolute_url()
        self.add_targets(form.instance)
        return result

    def add_targets(self, test):
        #TODO: Get list of targets from project
        people = Person.objects.all()
        for person in people:
            for identity in person.identity.all():
                for identifier in identity.identifier_set.filter(identifiertype = Identifier.EMAIL):
                    obj, created = EmailTestTarget.objects.get_or_create(target=identifier, emailtest=test)
        return "OK"


class EmailTestUpdate(UpdateView):
    model = EmailTest
    template_name = 'email/test_email.html'
    form_class = EmailTestForm


class EmailSendEmail(generic.View):

    def get(self, request, *args, **kwargs):
        # Make sure that the test exists.
        pk = kwargs['pk']
        email = get_object_or_404(EmailTest, pk=pk)
        #TODO: Permissions - check if user is allowed to start the test.
        # Only run tests that haven't been run yet.
        if email.teststatus in (EmailTest.NEW, EmailTest.SCHEDULED):
            # Mark the test as scheduled, so that the front-end says the right thing.
            email.teststatus = EmailTest.SCHEDULED
            email.save()
            #Queue the emails.
            run_email_test.delay(email.id)
        # Return to the test detail page.
        return HttpResponseRedirect(reverse('email-test-detail', kwargs={'pk':email.id}))
