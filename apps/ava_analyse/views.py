from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.ava_test.models import Test
from apps.ava_test.forms import  TestForm


class TestIndexView(generic.ListView):
    template_name = 'test/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        self.request.session['test']=None
        return Test.objects.filter(user=self.request.user)

class TestDetailView(generic.DetailView):
    model = Test
    context_object_name = 'test'
    template_name = 'test/view.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            test = get_object_or_404(Test, pk=pk)
            request.session['test']=test.id
        return super(TestDetailView,self).get(self, request, *args, **kwargs)

class TestDeleteView(DeleteView):
    model = Test
    template_name = 'confirm_delete.html'
    success_url = '/test/'

class TestCreateView(CreateView):
    model = Test
    template_name = 'test/list_modal.html'
    success_url = '/test/'
    form_class = TestForm
    page_title = 'Add a new test'
    button_value = 'Add test'
    item_type = 'test'

    def get_context_data(self, **kwargs):
        context = super(TestCreateView, self).get_context_data(**kwargs)
        context['form'] = self.get_form_class()
        context['form_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class TestUpdateView(UpdateView):
    model = Test
    template_name = 'item.html'
    success_url = '/test/'
    form_class = TestForm
    page_title = 'Update test details'
    button_value = 'Save changes'

    def get_context_data(self, **kwargs):
        context = super(TestUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['button_value'] = self.button_value
        return context

