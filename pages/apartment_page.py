from random import randint
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class ApartmentPage(Base):
    """Подключение интернета в квартиру"""

    # LOCATORS

    BUTTON_CLOSE_INFO_WINDOW_APARTMENT = (By.XPATH, '//div[@datatest="close_popup1_from_quiz_input_tel"]/span')
    BUTTON_RANDOM_CONNECT_TARIFF_APARTMENT = (
        By.XPATH, f'//div[@data-test="countRates"]/div/div/div/div[{randint(1, 22)}]//a[contains(text(),"Подключить")]')

    # METHODS

    def selection_tariff_apartment(self):
        """Выбор тарифа по заданному адресу(apartment)"""
        with allure.step('Selection_tariff_apartment'):
            self.element_is_visible(self.BUTTON_CLOSE_INFO_WINDOW_APARTMENT)
            self.element_is_clickable(self.BUTTON_CLOSE_INFO_WINDOW_APARTMENT).click()
            self.element_is_clickable(self.BUTTON_RANDOM_CONNECT_TARIFF_APARTMENT).click()
