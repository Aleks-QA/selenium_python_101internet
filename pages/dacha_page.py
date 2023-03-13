import time
from random import randint
import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class DachaPage(Base):
    """Подключение интернета в загородный дом"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    INPUT_NAME_DACHA = '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_name"]'
    INPUT_NUMBER_PHONE_DACHA = '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_tel"]'
    BUTTON_CONNECT_DACHA = '//*[@id="root"]/div/div[1]/div[3]//div[@data-test="order_form_input_connect_button"]'

    # GETTERS

    def get_input_name_dacha(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_NAME_DACHA)))

    def get_input_number_phone_dacha(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_NUMBER_PHONE_DACHA)))

    def get_button_connect_dacha(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_CONNECT_DACHA)))

    # ACTIONS

    def input_name_dacha(self, name):
        self.get_input_name_dacha().send_keys(name)

    def input_number_phone_dacha(self, number_phone):
        self.get_input_number_phone_dacha().send_keys(number_phone)

    def click_button_connect_dacha(self):
        self.get_button_connect_dacha().click()

    # METHODS

    def send_application_dacha(self, name, number_phone):
        """Заявка: Интернет в загородный дом"""
        with allure.step('Send_application_dacha'):
            Logger.add_start_step(method='send_application_dacha')
            print('Вводим имя')
            self.input_name_dacha(name)
            print('Вводим номер телефона')
            self.input_number_phone_dacha(number_phone)
            print('Нажимаем "Подключиться"')
            self.click_button_connect_dacha()

            request = self.driver.wait_for_request('/api/orders', 30)
            status_code = request.response.status_code
            print("Статус код заявки: ", request, request.response.status_code)
            Logger.add_end_step(self.driver.current_url, method='send_application_dacha')
            return status_code
