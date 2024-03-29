from pages.apartment_page import ApartmentPage
from pages.business_page import BusinessPage
from pages.dacha_page import DachaPage
from pages.main_page import MainPage
from base.base_class import Base
import allure


@allure.epic("Test suite sending application")
class TestSuiteSendApplication:
    @allure.description("Test sending application - apartment")
    def test_connect_tariff_apartment(self, driver, data):
        """Поиск и отправка заявки на подключение в квартиру"""
        url = 'https://piter-online.net/'
        street = data['street']
        house_numbers = data['house_numbers']
        # name = data['name']
        number_phone = data['number_phone']
        base = Base(driver, url)
        base.open()
        mp = MainPage(driver, url)
        mp.close_window_cookies()
        mp.filling_out_the_form_apartment(street, house_numbers)
        ap = ApartmentPage(driver, url)
        status_code = ap.send_application_apartment(number_phone)
        # status_code = op.send_application_apartment(name, number_phone)
        assert int(status_code) == 200, 'status code not 200'

    @allure.description("Test sending application - office")
    def test_connect_tariff_office(self, driver, data):
        """Поиск и отправка заявки на подключение в офис"""
        url = 'https://piter-online.net/'
        base = Base(driver, url)
        base.open()
        street = data['street']
        house_numbers = data['house_numbers']
        name = data['name']
        number_phone = data['number_phone']
        mp = MainPage(driver, url)
        mp.close_window_cookies()
        mp.filling_out_the_form_office(street, house_numbers)
        bp = BusinessPage(driver, url)
        status_code = bp.send_application_business(name, number_phone)
        assert int(status_code) == 200, 'status code not 200'

    @allure.description("Test sending application - dacha")
    def test_connect_tariff_dacha(self, driver, data):
        """Поиск и отправка заявки на подключение на дачу"""
        url = 'https://piter-online.net/'
        base = Base(driver, url)
        base.open()
        street = data['street']
        house_numbers = data['house_numbers']
        name = data['name']
        number_phone = data['number_phone']
        mp = MainPage(driver, url)
        mp.close_window_cookies()
        mp.filling_out_the_form_dacha(street, house_numbers)
        dp = DachaPage(driver, url)
        status_code = dp.send_application_dacha(name, number_phone)
        assert int(status_code) == 200, 'status code not 200'
