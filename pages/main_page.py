from data_for_tets import type_text, type_phone, type_email
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # Отправляем заполненную форму
    def click_feedback_button(self):
        button = self.browser.find_element(*MainPageLocators.BUTTON_FEEDBACK)
        button.click()

    def feedback_data_entry(self, name, phone, company, email, message):
        # заполняем поле имя
        input_name = self.browser.find_element(*MainPageLocators.FEEDBACK_FIELD_NAME)
        input_name.send_keys(name)
        # заполняем поле телефон
        input_phone = self.browser.find_element(*MainPageLocators.FEEDBACK_FIELD_PHONE)
        input_phone.send_keys(phone)
        # заполняем поле компания
        input_company = self.browser.find_element(*MainPageLocators.FEEDBACK_FIELD_COMPANY)
        input_company.send_keys(company)
        # заполняем поле email
        input_email = self.browser.find_element(*MainPageLocators.FEEDBACK_FIELD_MAIL)
        input_email.send_keys(email)
        # заполняем поле сообщение
        textarea_message = self.browser.find_element(*MainPageLocators.FEEDBACK_FIELD_MESSAGE)
        textarea_message.send_keys(message)

    # проверка доступности полей обратной связи
    def should_be_feedback_fields(self):
        self.should_be_feedback_button()
        self.should_be_name_input()
        self.should_be_phone_input()
        self.should_be_company_input()
        self.should_be_mail_input()
        self.should_be_message_textarea()

    # проверка, что есть кнопка 'отправить' в обратной связи
    def should_be_feedback_button(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_FEEDBACK), "Feedback button is not " \
                                                                                        "presented "

    # проверка, что есть поле 'имя' в обратной связи
    def should_be_name_input(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FIELD_NAME), "Field 'Name' is not " \
                                                                                       "presented "

    # проверка, что есть поле 'телефон' в обратной связи
    def should_be_phone_input(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FIELD_PHONE), "Field 'Phone' is not " \
                                                                               "presented "

    # проверка, что есть поле 'компания' в обратной связи
    def should_be_company_input(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FIELD_COMPANY), "Field 'Company' is not " \
                                                                                "presented "

    # проверка, что есть поле 'почта' в обратной связи
    def should_be_mail_input(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FIELD_MAIL), "Field 'Mail' is not " \
                                                                                  "presented "

    # проверка, что есть поле 'сообщение' в обратной связи
    def should_be_message_textarea(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FIELD_MESSAGE), "Field 'Message' is not " \
                                                                               "presented "

    # получение всех полей формы для заполнения
    def get_all_fields_feeedback_form(self):
        return self.browser.find_elements(*MainPageLocators.FEEDBACK_ALL_FIELDS)

    # проверка, что поле отмеченное * при незаполнении имеет класс ошибки
    def should_field_error(self, itemF):
        placeholder = itemF.get_attribute("placeholder")
        if '*' in placeholder:
            clas = itemF.get_attribute("class")
            assert 'form__input_error' in clas, "Required field {0} is not checked ".format(placeholder)

    # проверка, что появилась иконка об успешной отправке сообщения
    def should_be_icon_success_request(self):
        assert self.is_element_present_wait(*MainPageLocators.FEEDBACK_SUCCESS_REQUEST_ICON), "Unsuccessful Feedback Request "

    # проверка полей на невалидные значения
    def check_field_error_text(self, itemF):
        placeholder = itemF.get_attribute("placeholder")
        if '*' in placeholder:
            text_type = itemF.get_attribute("type")
            if text_type == "text":
                self.check_field(itemF, type_text)
            elif text_type == "phone":
                self.check_field(itemF, type_phone)
            elif text_type == "email":
                self.check_field(itemF, type_email)

    # проверка поля на данные
    def check_field(self, itemF, text_type):
        for str in text_type:
            itemF.send_keys(str)
            self.click_feedback_button()
            str_class = itemF.get_attribute("class")
            assert 'form__input_error' in str_class, "In the '{0}', you can insert the value '{1}' ".format(itemF.get_attribute("placeholder"), str)
            self.clear_field(itemF)
