import time
import traceback
import pytest

from pynput.keyboard import Key, Controller

from data_for_tets import Message
from pages.main_page import MainPage

LINK = "https://tages.ru/"


@pytest.mark.test_main_page
class TestMainPage:

    def test_clickability_of_all_links_and_sections(self, browser):

        # инициализируем Page Object
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # получаем все ссылки со страницы
        listA = page.get_all_links()

        print("\n")

        # проверяем видимость ссылок, если они видны, то кликабельны
        for itemA in listA:
            if itemA.get_attribute("href") is None or itemA.is_displayed() is False:
                print("Link {0} class:'{1}' is not click ability.".format(itemA.get_attribute("href"),
                                                                          itemA.get_attribute("class")))

    def test_email_and_tel_calls(self, browser):

        # инициализируем Page Object
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # получаем ссылки на телефоны и почту
        listA = page.get_links_for_tel_or_mail()

        print("\n")

        # проверяем вызовы ссылок (код зависит от окружения!)
        for itemA in listA:
            try:
                print("Link {0}.".format(itemA.get_attribute("href")))
                itemA.click()
                try:
                    keyboard = Controller()
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                    time.sleep(2)
                    print("The application selection window is closed")
                except Exception:
                    traceback.print_exc()
                    print("There is no alert window.")
            except Exception:
                print("Going to another page.")

    def test_validation_of_feedback_form(self, browser):

        # инициализируем Page Object
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # проверяем поля обратной связи
        page.should_be_feedback_fields()

        # сразу нажимаем кнопку отправить в форме обратной связи
        page.click_feedback_button()

        # получаем все поля формы
        listFields = page.get_all_fields_feeedback_form()

        # проверяем пустые поля
        for itemF in listFields:
            page.should_field_error(itemF)

        # проверяем обязательные поля в зависимости от данных
        for itemF in listFields:
            page.check_field_error_text(itemF)

    def test_request_feedback(self, browser):

        # инициализируем Page Object
        page = MainPage(browser, LINK)

        # открываем страницу
        page.open()

        # проверяем поля обратной связи
        page.should_be_feedback_fields()

        # вводим данные сообщения
        page.feedback_data_entry(Message.name, Message.phone, Message.company, Message.email, Message.message)

        # нажимаем кнопку отправить
        page.click_feedback_button()

        # ожидаем подтверждения отправления
        page.should_be_icon_success_request()
