import time
import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger



class MainPage(Base):
    url = 'https://piter-online.net/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    INPUT_STREET = '//div[@class="justify-content-center row"]/div/div[1]//input[@datatest="main_input_street_home_new"]'
    INPUT_HOUSE_NUMBER = '//div[@class="justify-content-center row"]/div/div[2]//input[@datatest="main_input_street_home_new"]'
    DROPDOWN_TYPE_CONNECT = '//div[@class="justify-content-center row"]//span[text()="Тип подключения"]'
    # DROPDOWN_RANDOM_TYPE_CONNECT = f'//div[@id="forSelectField"]/div[1]/div/div/div//li[{randint(1, 3)}]'
    DROPDOWN_TYPE_CONNECT_APARTMENT = '//div[@id="forSelectField"]/div[1]/div/div/div//li[1]'
    DROPDOWN_TYPE_CONNECT_OFFICE = '//div[@id="forSelectField"]/div[1]/div/div/div//li[2]'
    DROPDOWN_TYPE_CONNECT_DACHA = '//div[@id="forSelectField"]/div[1]/div/div/div//li[3]'
    # DROPDOWN_SELECT_TYPE_CONNECT = '//div[@id="forSelectField"]/div[2]/div/div/div//li[порядковый номер типа подключения]'
    BUTTON_SHOW_TARIFF = '//div[@class="justify-content-center row"]//div[text()="показать тарифы"]'
    BUTTON_CLOSE_INFO_WINDOW = '//div[@datatest="close_popup1_from_quiz_input_tel"]/span'

    # GETTERS

    def get_input_street(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_STREET)))

    def get_input_house_numbers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT_HOUSE_NUMBER)))

    def get_dropdown_type_connect(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_TYPE_CONNECT)))

    # def get_dropdown_random_type_connect(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_RANDOM_TYPE_CONNECT)))

    def get_dropdown_type_connect_office(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_TYPE_CONNECT_OFFICE)))

    def get_dropdown_type_connect_dacha(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_TYPE_CONNECT_DACHA)))
    def get_dropdown_type_connect_apartment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_TYPE_CONNECT_APARTMENT)))

    def get_button_show_tariff(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_SHOW_TARIFF)))

    # ACTIONS

    def input_street(self, street):
        self.get_input_street().send_keys(street)

    def input_house_numbers(self, house_numbers):
        self.get_input_house_numbers().send_keys(house_numbers)

    def click_dropdown_type_connect(self):
        self.get_dropdown_type_connect().click()

    # def click_dropdown_random_type_connect(self):
    #     self.get_dropdown_random_type_connect().click()

    def click_dropdown_type_connect_apartment(self):
        self.get_dropdown_type_connect_apartment().click()

    def click_dropdown_type_connect_office(self):
        self.get_dropdown_type_connect_office().click()

    def click_dropdown_type_connect_dacha(self):
        self.get_dropdown_type_connect_dacha().click()

    def click_button_show_tariff(self):
        self.get_button_show_tariff().click()

    # METHODS

    def filling_out_the_form_apartment(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения в КВАРТИРУ)"""
        with allure.step('Filling_out_the_form'):
            Logger.add_start_step(method='filling_out_the_form')
            self.driver.get(self.url)
            self.get_current_url()
            print('Указываем улицу')
            self.input_street(street)
            time.sleep(2)
            print('Нажимаем Enter')
            self.get_input_street().send_keys(Keys.RETURN)
            print('Указываем дом')
            self.input_house_numbers(house_numbers)
            print('Нажимаем на выпадающий список тип подключения')
            self.click_dropdown_type_connect()
            print('Выбираем тип подключения')
            self.click_dropdown_type_connect_apartment()
            time.sleep(1)
            print('Нажимаем показать тарифы')
            self.click_button_show_tariff()
            Logger.add_end_step(self.driver.current_url, method='filling_out_the_form')

    def filling_out_the_form_office(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения в ОФИС)"""
        with allure.step('Filling_out_the_form'):
            Logger.add_start_step(method='filling_out_the_form')
            self.driver.get(self.url)
            self.get_current_url()
            print('Указываем улицу')
            self.input_street(street)
            time.sleep(2)
            print('Нажимаем Enter')
            self.get_input_street().send_keys(Keys.RETURN)
            print('Указываем дом')
            self.input_house_numbers(house_numbers)
            print('Нажимаем на выпадающий список тип подключения')
            self.click_dropdown_type_connect()
            print('Выбираем тип подключения')
            self.click_dropdown_type_connect_office()
            time.sleep(1)
            print('Нажимаем показать тарифы')
            self.click_button_show_tariff()
            Logger.add_end_step(self.driver.current_url, method='filling_out_the_form')

    def filling_out_the_form_dacha(self, street, house_numbers):
        """Заполнение формы поиска(Тип подключения на ДАЧУ)"""
        with allure.step('Filling_out_the_form'):
            Logger.add_start_step(method='filling_out_the_form')
            self.driver.get(self.url)
            self.get_current_url()
            print('Указываем улицу')
            self.input_street(street)
            time.sleep(2)
            print('Нажимаем Enter')
            self.get_input_street().send_keys(Keys.RETURN)
            print('Указываем дом')
            self.input_house_numbers(house_numbers)
            print('Нажимаем на выпадающий список тип подключения')
            self.click_dropdown_type_connect()
            print('Выбираем тип подключения')
            self.click_dropdown_type_connect_dacha()
            time.sleep(1)
            print('Нажимаем показать тарифы')
            self.click_button_show_tariff()
            Logger.add_end_step(self.driver.current_url, method='filling_out_the_form')
