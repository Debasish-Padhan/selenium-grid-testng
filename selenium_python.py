import unittest 
import time
from selenium import webdriver 

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
	    command_executor = 'http://selenium-hub:4444',
	    desired_capabilities = {'browserName': 'chrome','javascriptEnabled': True})

    def open_google(self):
        driver = self.driver
        driver.get("https://google.com")
        time.sleep(10)

    def open_flipkart(self):
        driver = self.driver
        driver.get("https://flipkart.com")
        time.sleep(10)

    def open_amazon(self):
        driver = self.driver
        driver.get("https://amazon.com")
        time.sleep(10)

    def open_myntra(self):
        driver = self.driver
        driver.get("https://myntra.com")
        time.sleep(10)

    def open_limeroad(self):
        driver = self.driver
        driver.get("https://limeroad.com")
        time.sleep(10)

    def open_shoppersstop(self):
        driver = self.driver
        driver.get("https://shoppersstop.com")
        time.sleep(10)

    def open_snapdeal(self):
        driver = self.driver
        driver.get("https://snapdeal.com")
        time.sleep(10)

    def open_shopclues(self):
        driver = self.driver
        driver.get("https://shopclues.com")
        time.sleep(10)

    def open_meesho(self):
        driver = self.driver
        driver.get("https://meesho.com")
        time.sleep(10)

    def open_tatacliq(self):
        driver = self.driver
        driver.get("https://tatacliq.com")
        time.sleep(10)

    def test_website(self):
        self.open_google()
        self.open_flipkart()
        self.open_amazon()
        self.open_myntra()
        self.open_limeroad()
        self.open_shoppersstop()
        self.open_snapdeal()
        self.open_shopclues()
        self.open_meesho()
        self.open_tatacliq()

    def tearDown(self):
        self.driver.close()
	
if __name__ == "__main__":
    unittest.main()
