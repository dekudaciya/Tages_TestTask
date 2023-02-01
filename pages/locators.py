from selenium.webdriver.common.by import By


class BasePageLocators:
    # ссылки на телефоны и почту
    TEL_AND_MAILTO_LINKS = (By.CSS_SELECTOR, "A[href^='tel:'],A[href^='mailto:']")


class MainPageLocators:
    # кнопка Отправить в обратной связи
    BUTTON_FEEDBACK = (By.CSS_SELECTOR, "form button.form__send-form-button")
    # поле 'Имя'
    FEEDBACK_FIELD_NAME = (By.CSS_SELECTOR, "form input.form__input[type=text][placeholder*=Имя]")
    # поле 'Телефон'
    FEEDBACK_FIELD_PHONE = (By.CSS_SELECTOR, "form input.form__input[type=phone]")
    # поле 'Компания'
    FEEDBACK_FIELD_COMPANY = (By.CSS_SELECTOR, "form input.form__input[type=text][placeholder*=Компания]")
    # поле 'Почта'
    FEEDBACK_FIELD_MAIL = (By.CSS_SELECTOR, "form input.form__input[type=email]")
    # поле 'Комментарий'
    FEEDBACK_FIELD_MESSAGE = (By.CSS_SELECTOR, "form textarea.form__input")
    # все поля формы
    FEEDBACK_ALL_FIELDS = (By.CSS_SELECTOR, "form input, form textarea")
    # все поля формы
    FEEDBACK_SUCCESS_REQUEST_ICON = (By.CSS_SELECTOR, "div.form__success-badge-icon")
