from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from twython import Twython
from apps.ava_core_identity.models import Identifier, Identity

from apps.ava_test_twitter.models import TwitterTest
from apps.ava_test_twitter.forms import TwitterTestForm


class TwitterTestIndex(ListView):
    template_name = 'twitter/test_twitter_index.html'
    context_object_name = 'list'

    ''' TODO Left in as we will need this concept of ownership soon... this is a reminder '''
    # def get_queryset(self):
    #    return TwitterTest.objects.filter(user=self.request.user)


class TwitterTestDetail(DetailView):
    model = TwitterTest
    context_object_name = 'test'
    template_name = 'twitter/test_twitter_detail.html'


class TwitterTestDelete(DeleteView):
    model = TwitterTest
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('twitter-test-index')


class TwitterTestCreate(CreateView):
    model = TwitterTest
    template_name = 'twitter/test_twitter.html'
    form_class = TwitterTestForm


class TwitterTestUpdate(UpdateView):
    model = TwitterTest
    template_name = 'twitter/test_twitter.html'
    form_class = TwitterTestForm


''' TODO HERE BE DRAGONS - this pretty much needs blasting from orbit and re-writing '''


class TwitterTestSendTweet(generic.View):
    success_url = '/test/twitter/'

    # def get(self, request, *args, **kwargs):
    #
    #     targets = []
    #
    #     ''' TODO this is currently sending to all twitter identifiers in the database.... this is not good '''
    #     identities = Identity.objects.all
    #     for identity in identities:
    #         identifiers = identity.identifier_set.all()
    #         for i in identifiers:
    #             if i.identifiertype == Identifier.TWITTER:
    #                 targets.append("'" + i.identifier + "'")
    #
    #     ''' TODO Example: Fields key :: twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) '''
    #
    #     twitter = Twython('', '', '', '')
    #
    #     twitter.update_status(status='Testing')
    #
    #     return reverse('twitter-test-index')
