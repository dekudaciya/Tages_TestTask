from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # открытие страницы
    def open(self):
        self.browser.get(self.url)

    # поиск элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # поиск элемента, что он не появится в течении заданного времени
    def is_element_present_wait(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # поиск всех ссылок
    def get_all_links(self):
        return self.browser.find_elements(By.TAG_NAME, "A")

    # поиск всех ссылок
    def get_links_for_tel_or_mail(self):
        return self.browser.find_elements(*BasePageLocators.TEL_AND_MAILTO_LINKS)

    # очищение поля
    def clear_field(self, item):
        item.send_keys(Keys.CONTROL + "a")
        item.send_keys(Keys.DELETE)
