import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome()
    # Можно точно указать, где расположен драйвер для селениума
    # browser = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe")
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox()
    # Можно точно указать, где расположен драйвер для селениума
    # browser = webdriver.Firefox(executable_path = r"D:\geckodriver\geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser..")
    browser.quit()
