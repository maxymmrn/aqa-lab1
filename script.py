import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
    
    def testPageTitle(self):
        self.browser.get('https://pub.dev')
        self.assertIn('Dart packages', self.browser.title)
    
    def testSearchIcon(self):
        self.browser.get('https://pub.dev')
        search_icon = self.browser.find_element(By.CLASS_NAME, 'icon')
        search_icon.click()
        self.assertIn('Page 1', self.browser.title)


if __name__ == '__main__':
    unittest.main()
