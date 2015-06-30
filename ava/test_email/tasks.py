import re
from django.core.mail import get_connection, EmailMultiAlternatives
from ava.celery_app import app

from ava.test.testrunner import TestRunner
from ava.test_email.models import EmailTest
from ava.test import helpers


@app.task(name='test_email.tasks.run_email_test')
def run_email_test(email_test_id):
    test = EmailTest.objects.filter(pk=email_test_id).first()
    if test:
        runner = EmailTestSender(test)
        runner.run()


class EmailTestSender(TestRunner):
    """
    A helper class for generating and sending messages for an email test.
    """

    LINK_REPLACE = re.compile(r'{{\s*url\s*}}')

    connection = None

    def execute_test(self):
        """
        Sends messages to all targets of the test.
        """
        # Get the connection that will be used when generating and sending
        # messages.
        self.connection = get_connection(fail_silently=False)
        # Build up the list of targets for the email messages.
        targets = self.get_targets()
        # Build up the list of messages themselves.
        messages = (self.build_email(target) for target in targets)
        # Send the messages
        print('Email: Sending...')
        self.connection.send_messages(messages)
        print('Email: Sent')

    def get_targets(self):
        """
        Gets the list of email targets for the current test.
        """
        targets = self.test.targets.all()
        print('Email Targets: [' + ','.join([target.target.identifier for target in targets]) + ']')
        return targets

    def build_email(self, target):
        """
        Builds up an individual email message to send.
        
        :param target: The email identifier that the message will be sent to.
        """
        url = helpers.generate_tracking_link('email-test-tracking', target.token)

        message = EmailMultiAlternatives(subject=self.test.subject,
                                         body=self.get_text_body(target, url),
                                         from_email=self.test.fromaddr,
                                         to=[target.target.identifier],
                                         connection=self.connection)

        html_body = self.get_html_body(target, url)
        if html_body:
            message.attach_alternative(html_body, 'text/html')

        return message

    def get_text_body(self, url):
        """
        Gets the text body of an email message.

        """

        body = self.test.body
        body = self.LINK_REPLACE.sub(url, body)
        return body

    def get_html_body(self, url):
        """
        Gets the HTML body of an email message.

        """

        body = self.test.html_body
        if body:
            body = self.LINK_REPLACE.sub(url, body)
        return body
