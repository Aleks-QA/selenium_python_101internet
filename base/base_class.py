import datetime
import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Get current url')
    def get_current_url(self):
        """Метод возвращающий URL"""
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')
        return get_url

    @allure.step('Get screenshot')
    def get_screenshot(self):
        """Сделать скриншот"""
        now_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)
        print('Сделан скриншот')

    @allure.step('Get the number of items')
    def get_count_elements(self, locator, timeout=20):
        """Получить количество элементов на странице"""
        elements = wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return len(elements)

    @allure.step('Checking that the element is present in the DOM of the page and is visible.')
    def element_is_visible(self, locator, timeout=20):
        """Проверка того, что элемент присутствует в DOM страницы и является видимым"""
        try:
            # self.go_to_element(self.element_is_present(locator))
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Checking that all elements are present in the DOM of the page and are visible')
    def elements_are_visible(self, locator, timeout=20):
        """Проверка того, что все элементы присутствуют в DOM страницы и являются видимыми"""
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Check if an element exists in the DOM of the page.')
    def element_is_present(self, locator, timeout=20):
        """Проверка, существует ли элемент в DOM страницы."""
        try:
            return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Checking if elements exist in the page DOM')
    def elements_are_present(self, locator, timeout=20):
        """Проверка, существуют ли элементы в DOM страницы"""
        try:
            return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Checks that the element is either invisible or not in the DOM.')
    def element_is_not_visible(self, locator, timeout=20):
        """Проверяет, что элемент либо невидим, либо отсутствует в DOM."""
        try:
            return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Checks that the item is visible and enabled, so you can click it.')
    def element_is_clickable(self, locator, timeout=20):
        """Проверяет, что элемент виден и включен, поэтому его можно щелкнуть."""
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Checks if this text is present in the specified element.')
    def text_present_in_element(self, locator, text, timeout=20):
        """Проверяет, присутствует ли данный текст в указанном элементе."""
        try:
            return wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Go to specified element')
    def go_to_element(self, locator, timeout=20):
        """
        Перейти к указанному элементу
        Документация к методу scrollIntoView - https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
        """
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",
                                       self.element_is_present(locator, timeout))
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Double click')
    def action_double_click(self, element):
        """Двойной клик"""
        try:
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Right click')
    def action_right_click(self, element):
        """Клик правой кнопкой"""
        try:
            action = ActionChains(self.driver)
            action.context_click(element)
            action.perform()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Delete a visible item')
    def remove_element(self, locator, timeout=20):
        """Удалить видимый элемент"""
        try:
            element = self.element_is_visible(locator, timeout)
            self.driver.execute_script("arguments[0].remove();", element)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise

    @allure.step('Wait for request and get status code')
    def wait_for_request_and_get_status_code(self, pattern_request, timeout=5):
        """
            Этот метод будет ждать, пока не увидит запрос, соответствующий шаблону.
            Возвращает статус код этого запроса
            Пример pattern_request: "/api/sites/webhook"
            Требуется библиотека Python: Selenium Wire
        """
        try:
            request = self.driver.wait_for_request(pattern_request, timeout)
            status_code = request.response.status_code
            print("Status code: ", request, request.response.status_code)
            return status_code
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_screen", attachment_type=AttachmentType.PNG)
            raise
