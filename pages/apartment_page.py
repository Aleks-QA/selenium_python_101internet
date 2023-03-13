from random import randint
import allure
from utilities.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class ApartmentPage(Base):
    """Подключение интернета в квартиру"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    BUTTON_CLOSE_INFO_WINDOW_APARTMENT = '//div[@datatest="close_popup1_from_quiz_input_tel"]/span'
    BUTTON_RANDOM_CONNECT_TARIFF_APARTMENT = f'//div[@data-test="countRates"]/div/div/div/div[{randint(1, 22)}]//a[contains(text(),"Подключить")]'

    # GETTERS

    def get_button_close_info_window_apartment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_CLOSE_INFO_WINDOW_APARTMENT)))

    def get_button_connect_tariff_apartment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_RANDOM_CONNECT_TARIFF_APARTMENT)))

    # ACTIONS

    def click_button_close_info_window_apartment(self):
        self.get_button_close_info_window_apartment().click()

    def click_button_connect_tariff_apartment(self):
        self.get_button_connect_tariff_apartment().click()

    # METHODS

    def tariff_selection_apartment(self):
        """Выбор тарифа по заданному адресу(apartment)"""
        with allure.step('Tariff_selection_apartment'):
            Logger.add_start_step(method='tariff_selection_apartment')
            url = self.get_current_url()
            print('Нажимаем на подключение тарифа')
            self.click_button_connect_tariff_apartment()
            Logger.add_end_step(url, method='tariff_selection_apartment')