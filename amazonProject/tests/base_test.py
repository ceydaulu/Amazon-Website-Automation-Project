import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'
    expected_title = "Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev, mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--disable-plugins")
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-blink-features")
        chrome_options.add_argument("--disable-dev-shn-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()