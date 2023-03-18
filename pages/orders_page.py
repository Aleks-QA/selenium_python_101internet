import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class OrderPage(Base):
    """Оформление заявки(в квартиру)"""

    # LOCATORS

    INPUT_NAME = (By.XPATH, '//input[@datatest="providers_provider_order_input_name"]')
    INPUT_NUMBER_PHONE = (By.XPATH, '//input[@datatest="providers_provider_order_input_tel"]')
    BUTTON_SUBMIT_YOUR_APPLICATION = (By.XPATH, '//div[@data-test="order_form_input_connect_button"]')
    TEXT_STATUS = (By.XPATH, '//form/div/div[1]/div[1]')

    # METHODS

    def send_application_apartment(self, name, number_phone):
        """Заявка: Подключение интернета в квартиру"""
        with allure.step('Send_application_apartment'):
            self.element_is_clickable(self.INPUT_NAME).send_keys(name)
            self.element_is_clickable(self.INPUT_NUMBER_PHONE).send_keys(number_phone)
            time.sleep(1)
            self.element_is_clickable(self.BUTTON_SUBMIT_YOUR_APPLICATION).click()
            # self.text_present_in_element(self.TEXT_STATUS, 'Ваша заявка на подключение принята в работу.')

            request = self.driver.wait_for_request('/api/orders', 30)
            status_code = request.response.status_code
            print("Статус код заявки: ", request, request.response.status_code)
            return status_code
