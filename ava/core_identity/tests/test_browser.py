from django.test import LiveServerTestCase

from selenium import webdriver


class AdminTest(LiveServerTestCase):
    urls = 'axiom.urls'

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_people_index(self):
        # user opens web browser, navigates to admin page
        self.browser.get(self.live_server_url + '/people/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('[people] .all', body.text)
