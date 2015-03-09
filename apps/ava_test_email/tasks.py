from django.core.mail import get_connection, EmailMultiAlternatives
from apps.ava_core.celery import task_manager
from apps.ava_test.testrunner import TestRunner
from apps.ava_test_email.models import EmailTest


@task_manager.task(name='ava_test_email.tasks.run_email_test')
def run_email_test(email_test_id):
    test = EmailTest.objects.filter(pk=email_test_id).first()
    if test:
        runner = EmailTestSender(test)
        runner.run()

class EmailTestSender(TestRunner):
    '''
    A helper class for generating and sending messages for an email test.
    '''
    connection = None
    
    def execute_test(self):
        '''
        Sends messages to all targets of the test.
        '''
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
        '''
        Gets the list of email targets for the current test.
        '''
        #targets = self.test.
        targets = self.test.targets.all()
        print 'Email Targets: [' + ','.join([target.target.identifier for target in targets]) + ']'
        return targets
    
    def build_email(self, target):
        '''
        Builds up an individual email message to send.
        
        :param target: The email identifier that the message will be sent to.
        '''
        message = EmailMultiAlternatives(subject=self.test.subject,
                                         body=self.get_text_body(target),
                                         from_email=self.test.fromaddr,
                                         to=[target.target.identifier],
                                         connection=self.connection)
        
        html_body = self.get_html_body(target)
        if html_body:
            message.attach_alternative(html_body, 'text/html')
        
        return message
    
    def get_text_body(self, target):
        '''
        Gets the text body of an email message.
        
        :param target: The email test target that the message will be sent to.
        '''
        return self.test.body
    
    def get_html_body(self, target):
        '''
        Gets the HTML body of an email message.
        
        :param target: The email test target that the message will be sent to.
        '''
        return None

