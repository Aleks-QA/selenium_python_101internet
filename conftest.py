import pytest
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
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
    return {"street": street, "house_numbers": house_numbers, "name": name, "number_phone": number_phone }