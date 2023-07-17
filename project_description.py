import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait

"""
ОПИСАНИЕ РАБОТЫ ДАННОГО ПРОЕКТА

conftest.py - содержит настройки для работы веб-драйвера 

base/base_class.py - содержит ключевые методы для работы с веб-элементами,
вынесены в родительский класс для пере-использования в тестах

pages/ - тут описана каждая веб-страница в виде объекта класса, в классе описаны локаторы и методы для работы с ними 

tests/ - содержит тесты, описанные бизнес-логикой тест-кейса
"""


# --------------------------------------  пример tests/test_button.py  -----------------------------------------------

class TestExample:
    """
    tests/ - СОДЕРЖИТ ТЕСТЫ, ОПИСАННЫЕ БИЗНЕС-ЛОГИКОЙ ТЕСТ-КЕЙСОВ
    ШАГИ:
    1 - Пользователь открывает браузер
    2 - Пользователь нажимает на кнопку
    3 - Пользователь ожидает определенное сообщение
    """
    def test_method_get_count(self, driver):  # передаем экземпляр webdriver из conftest.py
        url = 'https://demoqa.com/buttons'
        # создаем объект класса и передаем базовый url и экземпляр webdriver в конструктор из base_class.py
        base = BaseExample(driver, url)
        # 1 - Пользователь открывает браузер;
        base.open()
        # 2 - Пользователь нажимает на кнопку
        pd = PageExample(driver, url)
        message = pd.click_button()
        # message = pd.click_button_old()  # без использования методов из базового класса
        # 3 - Пользователь ожидает сообщение
        assert message == "You have done a dynamic click", 'Invalid message after pressing the button'


# --------------------------------------  пример base/base_class.py  -------------------------------------------------

class BaseExample:
    """
    base/base_class.py - ПРИМЕР БАЗОВЫХ МЕТОДОВ
    В КЛАССЕ "Base" ОПИСАНЫ ОСНОВНЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С WEBDRIVER
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=20):
        """Проверяет, что элемент виден и включен, поэтому его можно щелкнуть"""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=20):
        """Проверка того, что элемент присутствует в DOM страницы и является видимым"""
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


# --------------------------------------   пример pages/main_page.py  ------------------------------------------------

class PageExample(BaseExample):  # наследуем базовые методы
    """
    pages/ - ТУТ ПРИМЕР ОФОРМЛЕНИЯ ВЕБ-СТРАНИЦ В ВИДЕ ОБЬЕКТОВ КЛАССА
    ОПИСЫВАЕТСЯ ВЗАИМОДЕЙСТВИЕ ПОЛЬЗОВАТЕЛЯ С ВЕБ-СТРАНИЦЕЙ
    """
    # locators
    BUTTON = (By.XPATH, '//*[@id="app"]/div/div//div[3]/button')
    TEXT_MESSAGE = (By.XPATH, '//p[@id="dynamicClickMessage"]')

    # methods
    """
    СРАВНЕНИЕ ОБЪЕМА КОДА БЕЗ УЧЕТА ПОДКЛЮЧЕНИЯ ОТЧЕТОВ, 125 VS 203 символов 
    """
    def click_button(self):
        """  Работа с элементами используя методы из базового класса  """
        self.element_is_clickable(self.BUTTON, 20).click()
        message = self.element_is_visible(self.TEXT_MESSAGE, 20).text
        return message

    def click_button_old(self):
        """  Работа с элементами если их нет в базовом классе  """
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.BUTTON)).click()
        message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.TEXT_MESSAGE)).text
        return message


# --------------------------------------   пример conftest.py   ------------------------------------------------------

@pytest.fixture(scope="session")
def driver():
    """
    Описываем часть, которая будет выполняться перед тестами.
    После yield мы вызываем функцию quit, которая завершает сессию и убивает экземпляр webdriver.
    """
    options = Options()
    driver_example = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
    driver_example.maximize_window()
    yield driver_example
    driver_example.quit()
