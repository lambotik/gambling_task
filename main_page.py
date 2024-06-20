import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from base_page import BasePage

load_dotenv()


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[@class="MiniUserInfo__buttons"]/div[1]')
    INPUT_NAME = (By.XPATH, '//input[@name="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON2 = (By.XPATH, '//div[@class="Dialog__actions"]/div[1]')
    USER_ICON_NAME = (By.XPATH, '//div[@class="panel MiniUserInfo__nickname_text"]/span')
    CASINO_BUTTON = (By.XPATH, '//div[text()="Casino"]')
    FIRST_GAME = (By.XPATH, '//div[@class="viewable-monitor"][1]')
    PLAY_BUTTON = (By.XPATH, '//div[@class="panel WidgetCasinoGameListItemContainer__play"]')
    WIDGET_TITLE = (By.XPATH, '//div[text()="Astro Wild"]')


class MainPage(BasePage):
    locators = MainPageLocators()
    link = 'https://poker.evenbetpoker.com/html5-evenbetpoker/d/?tables/all'

    def login_user(self):
        self.element_is_present_and_clickable(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(os.getenv('LOGIN'))
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(os.getenv('PASSWORD'))
        self.element_is_present_and_clickable(self.locators.LOGIN_BUTTON2).click()

    def check_user_icon_name(self):
        icon_name = self.element_is_visible(self.locators.USER_ICON_NAME).text
        login = os.getenv('LOGIN')
        assert icon_name == login

    def select_game(self):
        self.element_is_present_and_clickable(self.locators.CASINO_BUTTON).click()
        self.element_is_present_and_clickable(self.locators.FIRST_GAME).click()
        self.element_is_present_and_clickable(self.locators.PLAY_BUTTON).click()
        astro_widget = self.element_is_visible(self.locators.WIDGET_TITLE).text
        return astro_widget
