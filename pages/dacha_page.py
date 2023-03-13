import time
from random import randint
import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class DachaPage(Base):
    """Загородный дом"""

    # url = 'https://piter-online.net/leningradskaya-oblast/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    """Интернет в загородный дом"""
    INPUT_NAME_DACHA = '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_name"]'
    INPUT_NUMBER_PHONE_DACHA = '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_tel"]'
    BUTTON_CONNECT_DACHA = '//*[@id="root"]/div/div[1]/div[3]//div[@data-test="order_form_input_connect_button"]'

    # DROPDOWN_TYPE_INTERNET_DACHA = f'//div[@id="forSelectField"]/div[1]/div/div/div//li[{randint(1, 5)}]'
    # DROPDOWN_ITEM_TYPE_INTERNET_DACHA = '//*[@id="forSelectField"]/div[1]/div/div/div/ul/li[порядковый номер]'

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

    # def click_button_close_info_window_apartment(self):
    #     self.get_button_close_info_window_apartment().click()
    #
    # def click_button_connect_tariff_apartment(self):
    #     self.get_button_connect_tariff_apartment().click()

    def input_name_dacha(self, name):
        self.get_input_name_dacha().send_keys(name)

    def input_number_phone_dacha(self, number_phone):
        self.get_input_number_phone_dacha().send_keys(number_phone)

    def click_button_connect_dacha(self):
        self.get_button_connect_dacha().click()

    # METHODS
    #
    # def tariff_selection_apartment(self, url):
    #     """Выбор тарифа по заданному адресу(apartment)"""
    #     self.get_current_url()
    #     self.driver.get(url)
    #     print('Нажимаем на подключение тарифа')
    #     self.click_button_connect_tariff_apartment()

    def send_application_dacha(self, name, number_phone):
        """Заявка: Интернет в загородный дом"""
        # self.get_current_url()
        print('Вводим имя')
        self.input_name_dacha(name)
        print('Вводим номер телефона')
        self.input_number_phone_dacha(number_phone)
        print('Нажимаем "Подключиться"')
        self.click_button_connect_dacha()

        request = self.driver.wait_for_request('/api/orders', 30)
        status_code = request.response.status_code
        print("Статус код заявки: ", request, request.response.status_code)

        return status_code
