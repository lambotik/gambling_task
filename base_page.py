from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link
        self.timeout = 10

    def open(self):
        self.driver.get(self.link)

    def element_is_present_and_clickable(self, locator):
        return (Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}") and
                self.element_is_clickable(locator))

    def element_is_visible(self, locator):
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def element_is_present(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def element_is_clickable(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}")

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center'});", element)
