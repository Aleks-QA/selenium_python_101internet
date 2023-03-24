import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class DachaPage(Base):
    """Подключение интернета в загородный дом"""

    # LOCATORS

    INPUT_NAME_DACHA = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_name"]')
    INPUT_NUMBER_PHONE_DACHA = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]//input[@datatest="order_form_input_tel"]')
    BUTTON_CONNECT_DACHA = (
        By.XPATH, '//*[@id="root"]/div/div[1]/div[3]//div[@data-test="order_form_input_connect_button"]')

    # METHODS

    def send_application_dacha(self, name, number_phone):
        """Заявка: Интернет в загородный дом"""
        with allure.step('Send_application_dacha'):
            self.element_is_clickable(self.INPUT_NAME_DACHA).send_keys(name)
            self.element_is_clickable(self.INPUT_NUMBER_PHONE_DACHA).send_keys(number_phone)
            time.sleep(1)
            self.element_is_clickable(self.BUTTON_CONNECT_DACHA).click()
            request = self.driver.wait_for_request('/api_external/sites/webhook', 10)
            status_code = request.response.status_code
            print("Статус код заявки: ", request, request.response.status_code)
            return status_code
