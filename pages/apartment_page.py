import time
from random import randint
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class ApartmentPage(Base):
    """Подключение интернета в квартиру"""

    # LOCATORS

    BUTTON_CLOSE_INFO_WINDOW_APARTMENT = (By.XPATH, '//div[@datatest="close_popup1_from_quiz_input_tel"]/span')
    LIST_TARIFF = (By.XPATH, '//div[@datatest="providers_form_inspect_connect_tariff_button"]')
    INPUT_NUMBER = (By.XPATH, '//input[@datatest="popup_tariff_order_input_tel"]')
    BUTTON_SEND_APPLICATION = (By.XPATH, '//div[@data-test="popup_tariff_order_form_input_connect_button"]')

    # METHODS

    def get_locator_random_tariff(self):
        """Получение локатора случайного тарифа"""
        count = self.get_count_elements(self.LIST_TARIFF)  # метод получающий количество элементов
        locator = (By.XPATH, f'//div[{randint(1, count)}]/div/div/div/div/div/div/a[contains(text(),"Подключить")]')
        return locator

    def fill_pop_up_window(self, number):
        """Заполнение всплывающего окна и отправка заявки"""
        self.element_is_visible(self.INPUT_NUMBER).send_keys(number)
        self.element_is_clickable(self.BUTTON_SEND_APPLICATION).click()

    def send_application_apartment(self, number):
        """Выбор тарифа(в квартиру)"""
        with allure.step('Selection_tariff_apartment'):
            self.element_is_visible(self.BUTTON_CLOSE_INFO_WINDOW_APARTMENT)
            time.sleep(2)
            self.element_is_clickable(self.BUTTON_CLOSE_INFO_WINDOW_APARTMENT).click()
            random_tariff = self.get_locator_random_tariff()
            self.go_to_element(random_tariff)
            self.element_is_clickable(random_tariff).click()
            self.fill_pop_up_window(number)

            status_code = self.wait_for_request_and_get_status_code("/api/orders")
            return status_code
