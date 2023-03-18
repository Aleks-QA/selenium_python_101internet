import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class BusinessPage(Base):
    """Подключение интернета в офис"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    INPUT_CONTACT_PERSON = '[datatest="business_order_input_person"]'
    INPUT_NUMBER_PHONE = '[datatest="business_order_input_tel"]'
    BUTTON_SEND_REQUEST = '//form/div/div/div/div[1]/div[4]/div[1]'

    # GETTERS

    def get_input_contact_person(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_CONTACT_PERSON)))

    def get_input_number_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.INPUT_NUMBER_PHONE)))

    def get_button_send_request(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_SEND_REQUEST)))

    # ACTIONS

    def input_contact_person(self, contact_person_name):
        self.get_input_contact_person().send_keys(contact_person_name)

    def input_number_phone(self, number_phone):
        self.get_input_number_phone().send_keys(number_phone)

    def click_button_send_request(self):
        self.get_button_send_request().click()

    # METHODS

    def send_application_business(self, name, number_phone):
        """Заявка: Подключение интернета в офис"""
        with allure.step('Send_application_business'):
            Logger.add_start_step(method='send_application_business')
            print('Вводим имя')
            self.input_contact_person(name)
            print('Вводим номер телефона')
            self.input_number_phone(number_phone)
            time.sleep(1)
            print('Нажимаем "Отправить заявку"')
            self.click_button_send_request()

            request = self.driver.wait_for_request('/api/orders', 30)
            status_code = request.response.status_code
            print("Статус код заявки: ", request, request.response.status_code)
            Logger.add_end_step(self.driver.current_url, method='send_application_business')
            return status_code
