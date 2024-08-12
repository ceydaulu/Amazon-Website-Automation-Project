from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        element = self.find(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        return self.wait_element(locator).text

    def get_nth_element(self, index, *locator):
        return self.driver.find_elements(*locator)[index]

    def send_text(self, text, *locator):
        self.find(*locator).send_keys(text)

    def is_element_visible(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            print(f"Element with {locator} is visible.")
            return True
        except WebDriverException:
            print(f"Element with {locator} is not visible.")
            return False

    def is_element_invisible(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))
            print(f"Element with {locator} is invisible.")
            return True
        except WebDriverException:
            print(f"Element with {locator} is still visible.")
            return False

    def is_element_clickable(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

            return True
        except WebDriverException:

            return False
