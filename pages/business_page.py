import time
import allure
from selenium.webdriver.common.by import By
from base.base_class import Base


class BusinessPage(Base):
    """Подключение интернета в офис"""

    # LOCATORS

    INPUT_CONTACT_PERSON = (By.CSS_SELECTOR, '[datatest="business_order_input_person"]')
    INPUT_NUMBER_PHONE = (By.CSS_SELECTOR, '[datatest="business_order_input_tel"]')
    BUTTON_SEND_REQUEST = (By.XPATH, '//form/div/div/div/div[1]/div[4]/div[1]')

    # METHODS

    def send_application_business(self, name, number_phone):
        """Заявка: Подключение интернета в офис"""
        with allure.step('Send_application_business'):
            self.element_is_clickable(self.INPUT_CONTACT_PERSON).send_keys(name)
            self.element_is_clickable(self.INPUT_NUMBER_PHONE).send_keys(number_phone)
            time.sleep(2)
            self.element_is_clickable(self.BUTTON_SEND_REQUEST).click()

            status_code = self.wait_for_request_and_get_status_code("/api/orders")
            return status_code
