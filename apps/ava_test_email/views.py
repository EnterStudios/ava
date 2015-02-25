from django.views import generic
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from apps.ava_core_org.models import Organisation
from apps.ava_test_email.models import EmailTest, EmailTestTarget
from apps.ava_test_email.forms import EmailTestForm
from apps.ava_core_people.models import Person, Identifier


class EmailTestIndex(ListView):
    template_name = 'email/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test'] = None
        return EmailTest.objects.filter(user=self.request.user)


class EmailTestDetail(DetailView):
    model = EmailTest
    context_object_name = 'test'
    template_name = 'email/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(EmailTest, pk=pk)
            request.session['test'] = test.id
        return super(EmailTestDetailView, self).get(self, request, *args, **kwargs)


class EmailTestDelete(DeleteView):
    model = EmailTest
    template_name = 'confirm_delete.html'
    success_url = '/test/email/'


class EmailTestCreate(CreateView):
    model = EmailTest
    template_name = 'email/emailtest.html'
    form_class = EmailTestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.add_targets()
        return super(EmailTestCreate, self).form_valid(form)

    def add_targets(self):
        test = self.object
        organisation = test.org
        people = organisation.person_set.all()
        for p in people:
            ids = p.identifier_set.all()
            for i in ids:
                if i.identifiertype == Identifier.EMAIL:
                    obj, created = EmailTestTarget.objects.get_or_create(target=i, emailtest=test)
                    test = EmailTestTarget
        return "OK"


class EmailTestUpdate(UpdateView):
    model = EmailTest
    template_name = 'email/emailtest.html'
    form_class = EmailTestForm


class EmailSendEmail(generic.View):
    success_url = '/test/email/'

    def get(self, request, *args, **kwargs):
        pk = request.session['test']
        org_pk = request.session['organisation']
        email = get_object_or_404(EmailTest, pk=pk)
        org = get_object_or_404(Organisation, pk=org_pk)
        targets = []
        people = Person.objects.filter(organisation=org)
        for p in people:
            identifiers = p.identifier_set.all()
            for i in identifiers:
                if i.identifiertype == Identifier.EMAIL:
                    targets.append("'" + i.identifier + "'")

        # currently sends to all people in organisation - this will need addressing

        targetString = ",".join(targets)
        targetString = '[' + targetString + ']'

        print "Targets:: " + targetString

        # send_mail(email.subject, email.body, email.fromaddr, targetString, fail_silently=False)
        send_mail(email.subject, email.body, 'laura@trustme.io', ['laura@safestack.io', 'hello@avasecure.com'],
                  fail_silently=False)
        return HttpResponseRedirect(reverse('emailtestindex'))
