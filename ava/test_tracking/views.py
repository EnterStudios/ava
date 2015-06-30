import json
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from ava.test_email.models import EmailTestTarget
from ava.test_twitter.models import TwitterTestTarget
from django.http.response import Http404


class RecordTestResultView(generic.TemplateView):
    class Meta:
        abstract = True

    TRACKING_FIELDS = {
        'ipaddress': 'REMOTE_ADDR',
        'method': 'REQUEST_METHOD',
        'host': 'HTTP_HOST',
        'path': 'PATH_INFO',
        'contentlength': 'CONTENT_LENGTH',
        'contenttype': 'CONTENT_TYPE',
        'ua': 'HTTP_USER_AGENT',
        'referrer': 'HTTP_REFERER',
        'via': 'HTTP_VIA',
    }

    # Remember the page template to display when the link is clicked.
    page_template = None

    def get(self, request, *args, **kwargs):
        # Get the token, erroring if it's not present.
        token = kwargs['token']
        if not token:
            raise Http404
        # Get the current test target from the tracking token.
        target = self.get_target(token)
        # Save the tracking information.
        self.save_tracking_info(token, target)
        # Get the test currently being executed.
        test = self.get_test(target)
        if test:
            # If there's a redirect URL for the test, go to it instead of
            # displaying a page.
            redirect_url = self.get_redirect_url(test, kwargs)
            if redirect_url:
                return redirect(redirect_url)
            # If the test says to use a specific page template, record that now
            # for when the page gets rendered.
            if test.page_template:
                self.page_template = test.page_template
        # Continue to render the page.
        return super(RecordTestResultView, self).get(request, *args, **kwargs)

    def get_template_names(self):
        if self.page_template:
            return self.page_template
        return 'tracking/success.html'

    def get_target(self, token):
        """
        Gets the target of a test, based on the supplied tracking token.
        :param token: The tracking token of the test target.
        """
        raise NotImplementedError

    def build_tracking_info(self, target):
        """
        Gets the tracking information that will be saved against a test target.
        :param target: An object representing the target of a test.
        """
        tracking_info = {'target': target}
        # Fill in as many fields as possible from the request meta information.
        for field_name, meta_name in self.TRACKING_FIELDS.items():
            if meta_name in self.request.META:
                tracking_info[field_name] = self.request.META[meta_name]
        # Return the tracking info dict.
        return tracking_info

    def save_tracking_info(self, token, target):
        """
        Saves tracking information for the specified target.
        :param token: The tracking token of the test target.
        :param target: An object representing the target of a test.
        """
        raise NotImplementedError

    def get_test(self, target):
        """
        Gets the test that a test target is assigned to.
        :param target: An object representing the target of a test.
        """
        raise NotImplementedError

    def get_redirect_url(self, test, kwargs):
        # If the redirect URL is blank or null, there is no URL.
        redirect_url = (test.redirect_url or '').strip()
        if not redirect_url:
            return None
        # If the redirect URL looks like a JSON object, check for multiple
        # URL targets based on extra data in the incoming URL.
        if redirect_url[0] == '{' and redirect_url[-1] == '}':
            url_data = json.loads(test.redirect_url)
            # If there's extra data in the incoming URL, check for a matching
            # item in the JSON object.
            if 'extra' in kwargs:
                extra = kwargs['extra']
                if extra in url_data:
                    return url_data[extra]
            # If there's no match, check for a default URL in the JSON object.
            if 'default' in url_data:
                return url_data['default']
            # If there's no default URL, don't redirect.
            return None
        else:
            # Redirect URL is not a JSON object, so treat it like a raw URL.
            return redirect_url


class RecordEmailTestResultView(RecordTestResultView):
    """
    Records information about a URL that was clicked in a test email.
    """

    def get_target(self, token):
        return get_object_or_404(EmailTestTarget, token=token)

    def save_tracking_info(self, token, target):
        result_info = self.build_tracking_info(target)
        target.results.create(**result_info)

    def get_test(self, target):
        return target.emailtest


class RecordTwitterTestResultView(RecordTestResultView):
    """
    Records information about a URL that was clicked in a test tweet.
    """

    def get_target(self, token):
        return get_object_or_404(TwitterTestTarget, token=token)

    def save_tracking_info(self, token, target):
        result_info = self.build_tracking_info(target)
        target.results.create(**result_info)

    def get_test(self, target):
        return target.emailtest
