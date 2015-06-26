from apps.ava_test.models import Test


class TestRunner(object):
    """
    An abstract base class that helps to run AVA tests.
    
    The run() method on this class ensures that tests are only executed if they
    have not done so already, and will ensure that the test state is updated
    as appropriate.
    """

    class Meta:
        abstract = True

    test = None

    def __init__(self, test):
        """
        Creates a new TestRunner instance.
        
        :param test: The AVA test that is being run.
        """
        self.test = test

    def set_test_status(self, status):
        """
        Updates the status of the current test.
        
        :param status: The status to assign to the current test.
        """
        self.test.teststatus = status
        self.test.save()

    def run(self):
        """
        Executes the current test, setting the test status as appropriate.
        """
        if not self.test or not self.test.teststatus in (Test.NEW, Test.SCHEDULED):
            return False

        try:
            self.set_test_status(Test.RUNNING)
            self.execute_test()
        except Exception as e:
            print 'Exception: ' + unicode(e)
            self.set_test_status(Test.ERROR)
            return False
        else:
            self.set_test_status(Test.COMPLETE)
            return True

    def execute_test(self):
        """
        Performs the actual test.
        
        This method should be overridded in subclasses in order to provide the
        relevant test functionality.
        """
