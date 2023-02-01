import time
from dataclasses import dataclass


@dataclass
class FeedBackMessage:
    name: str
    phone: str
    company: str
    email: str
    message: str

# Пример данных для тестовой обратной связи
nameUser = str(time.time())
Message = FeedBackMessage(
    nameUser,
    nameUser[:10],
    "fakemail.org",
    nameUser + "@fakemail.org",
    "Тестовое сообщение для автоматизации"
)

# невалидные данные для типа 'text'
type_text = [
    " ",
    "!",
    #"<javascript>alert();</javascript>",
    "-",
    #"DROP DATABASE;"
]

# невалидные данные для типа 'phone'
type_phone = [
    " ",
    "  ",
    "q",
    "qwertyuiop",
    "1",
    "12345678901",
    "123456789",
    "123456789O",
    "!!!"
]

# невалидные данные для типа 'email'
type_email = [
    " ",
    "  ",
    "q",
    "@",
    "1",
    "12345678901",
    "!!!",
    "@@ru",
    "@@.ru",
    "qwe@",
    "qwe@qwe"
    " @qwe.ru",
    "qwe.ru"
]