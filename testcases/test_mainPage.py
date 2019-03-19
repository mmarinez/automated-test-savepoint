import unittest
import pageobjects.TwitterMainPage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/?lang=en")

    def test_search_in_python_org(self):
        pass
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
        