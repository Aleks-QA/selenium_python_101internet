import allure
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.apartment_page import ApartmentPage
from pages.business_page import BusinessPage
from pages.orders_page import OrderPage
from pages.dacha_page import DachaPage
from pages.main_page import MainPage
from base.base_class import Base


@allure.description("Test sending application")
def test_connect_tariff(set_up, data):
    """Поиск и отправка заявки"""
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # от лишних сообщений в терминале
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

    driver.maximize_window()
    base = Base(driver)

    street = data['street']
    house_numbers = data['house_numbers']
    name = data['name']
    number_phone = data['number_phone']

    mp = MainPage(driver)
    mp.filling_out_the_form(street, house_numbers)  # Выбираем рандомный тип подключения

    dp = DachaPage(driver)
    bp = BusinessPage(driver)
    ap = ApartmentPage(driver)
    op = OrderPage(driver)

    get_url = base.get_current_url()

    list_type = ['rates', 'business', 'sat']
    list_get_url = get_url.replace('/', ' ').replace('?', ' ').split(' ')

    count = 0
    while count < len(list_type):
        if list_type[count] in list_get_url:
            rez = count
            break
        count += 1

    i = 0
    while i < 5:
        i += 1
        print(f"\n__Sending application №{i}__")
        driver.get(get_url)
        if rez == 0:
            print("Заявка на подключение интернета в квартиру")
            ap.tariff_selection_apartment()
            status_code = op.send_application_apartment(name, number_phone)
            assert int(status_code) == 201, 'status code not 201'
        elif rez == 1:
            print("Заявка на подключение интернета в офис")
            status_code = bp.send_application_business(name, number_phone)
            assert int(status_code) == 201, 'status code not 201'
        elif rez == 2:
            print("Заявка на подключение интернета на дачу")
            status_code = dp.send_application_dacha(name, number_phone)
            assert int(status_code) == 201, 'status code not 201'
