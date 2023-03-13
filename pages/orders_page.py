import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class OrderPage(Base):
    """Оформление заявки"""
    # url = 'https://piter-online.net/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    INPUT_NAME = '//input[@datatest="providers_provider_order_input_name"]'
    INPUT_NUMBER_PHONE = '//input[@datatest="providers_provider_order_input_tel"]'
    BUTTON_SUBMIT_YOUR_APPLICATION = '//div[@data-test="order_form_input_connect_button"]'
    TEXT_STATUS = '//form/div/div[1]/div[1]'

    # GETTERS

    def get_input_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_NAME)))

    def get_input_number_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_NUMBER_PHONE)))

    def get_button_submit_application(self):
        # WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located((By.XPATH, self.BUTTON_SUBMIT_YOUR_APPLICATION)))
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_SUBMIT_YOUR_APPLICATION)))

    def assert_text_status(self):
        return WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.XPATH, self.TEXT_STATUS),
                                             'Ваша заявка на подключение принята в работу.'))

    # ACTIONS

    def input_name(self, name):
        self.get_input_name().send_keys(name)

    def input_number_phone(self, number_phone):
        self.get_input_number_phone().send_keys(number_phone)

    def click_button_submit_application(self):
        self.move_to_element(self.get_button_submit_application())
        self.get_button_submit_application().click()

    # METHODS

    def send_application_apartment(self, name, number_phone):
        """Заявка: Подключение интернета в квартиру"""
        # self.get_current_url()
        print('Вводим имя')
        self.input_name(name)
        print("Вводим номер телефона")
        self.input_number_phone(number_phone)
        time.sleep(0.5)
        print("Нажимаем кнопку 'Оставить заявку'")
        self.click_button_submit_application()

        request = self.driver.wait_for_request('/api/orders', 30)
        status_code = request.response.status_code
        print("Статус код заявки: ", request, request.response.status_code)

        print("Ждем сообщения: Ваша заявка на подключение принята в работу.")
        self.assert_text_status()

        return status_code