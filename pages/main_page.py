import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base


class MainPage(Base):
    # LOCATORS

    PROMPT_LIST = (By.XPATH, '//div[@id="forSelectField"]')
    DROPDOWN_TYPE_CONNECT = (By.XPATH, '//div[@class="justify-content-center row"]//span[text()="Тип подключения"]')
    DROPDOWN_TYPE_CONNECT_APARTMENT = (By.XPATH, '//div[@id="forSelectField"]/div[1]/div/div/div//li[1]')
    DROPDOWN_TYPE_CONNECT_OFFICE = (By.XPATH, '//div[@id="forSelectField"]/div[1]/div/div/div//li[2]')
    DROPDOWN_TYPE_CONNECT_DACHA = (By.XPATH, '//div[@id="forSelectField"]/div[1]/div/div/div//li[3]')
    BUTTON_SHOW_TARIFF = (By.XPATH, '//div[@class="justify-content-center row"]//div[text()="показать тарифы"]')
    BUTTON_CLOSE_INFO_WINDOW = (By.XPATH, '//div[@datatest="close_popup1_from_quiz_input_tel"]/span')
    WINDOW_COOKIES = (By.XPATH, "//span[contains(text(),'cookies')]/../..")
    INPUT_STREET = (By.XPATH, '//div[@class="justify-content-center row"]/div/div[1]//input['
                              '@datatest="main_input_street_home_new"]')
    INPUT_HOUSE_NUMBER = (By.XPATH, '//div[@class="justify-content-center row"]/div/div[2]//input['
                                    '@datatest="main_input_street_home_new"]')

    # METHODS

    def close_window_cookies(self):
        """Скрыть окно согласия на использование файлов cookie, если оно присутствует"""
        with allure.step('Close_window_cookies'):
            try:
                self.remove_element(self.WINDOW_COOKIES, 0.5)
            except TimeoutException:
                pass

    def filling_out_the_form_apartment(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения в КВАРТИРУ)"""
        with allure.step('Filling_out_the_form_apartment'):
            self.element_is_clickable(self.INPUT_STREET).send_keys(street)
            self.element_is_visible(self.PROMPT_LIST)
            self.element_is_clickable(self.INPUT_STREET).send_keys(Keys.RETURN)
            self.element_is_clickable(self.INPUT_HOUSE_NUMBER).send_keys(house_numbers)
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT).click()
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT_APARTMENT).click()
            time.sleep(1)
            self.element_is_clickable(self.BUTTON_SHOW_TARIFF).click()

    def filling_out_the_form_office(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения в ОФИС)"""
        with allure.step('Filling_out_the_form_office'):
            self.element_is_clickable(self.INPUT_STREET).send_keys(street)
            self.element_is_visible(self.PROMPT_LIST)
            self.element_is_clickable(self.INPUT_STREET).send_keys(Keys.RETURN)
            self.element_is_clickable(self.INPUT_HOUSE_NUMBER).send_keys(house_numbers)
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT).click()
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT_OFFICE).click()
            time.sleep(1)
            self.element_is_clickable(self.BUTTON_SHOW_TARIFF).click()

    def filling_out_the_form_dacha(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения на ДАЧУ)"""
        with allure.step('Filling_out_the_form_dacha'):
            self.element_is_clickable(self.INPUT_STREET).send_keys(street)
            self.element_is_visible(self.PROMPT_LIST)
            self.element_is_clickable(self.INPUT_STREET).send_keys(Keys.RETURN)
            self.element_is_clickable(self.INPUT_HOUSE_NUMBER).send_keys(house_numbers)
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT).click()
            self.element_is_clickable(self.DROPDOWN_TYPE_CONNECT_DACHA).click()
            time.sleep(1)
            self.element_is_clickable(self.BUTTON_SHOW_TARIFF).click()
