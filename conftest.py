import pytest
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def driver():
    """ CHROME """
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    """ FIREFOX """
    # option = webdriver.FirefoxOptions()
    # option.set_preference("dom.webdriver.enabled", False)  # убирает флажок что авто ПО управляет браузером
    # # option.set_preference("general.useragent.override", "user-agent=Mozilla/5.0 (X11; Linux x86_64)"
    # #                                                     " AppleWebKit/537.36 (KHTML, like Gecko)"
    # #                                                     " Chrome/51.0.2704.103"
    # #                                                     " Safari/537.36")  # подмена user-agent
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=option)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def set_up():
    print('\n__Start test__')
    yield
    print('__Finish test__')


@pytest.fixture
def data():
    street = 'Тестовая линия'
    house_numbers = '1'
    name = 'Александр'
    number_phone = '1111111111'
    return {"street": street, "house_numbers": house_numbers, "name": name, "number_phone": number_phone}
