import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод возвращающий URL"""
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')
        return get_url

    def get_screenshot(self):
        """Создание скриншотов"""
        now_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            '.\\screen\\' + name_screenshot)
        print('Сделан скриншот')

    def place_the_cursor_css(self, selector_css):
        """Навести курсор на элемент CSS"""
        hoverable = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector_css)))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def place_the_cursor_xpath(self, selector_xpath):
        """Навести курсор на элемент XPATH"""
        hoverable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector_xpath)))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def move_to_element(self, x_path_element):
        """Переместиться к элементу + скролл"""
        scroll_by = 'window.scrollBy(0, -200);'
        self.driver.execute_script(scroll_by)
        action = ActionChains(self.driver)
        action.move_to_element(x_path_element).perform()

    def find_substring(self, substring, string):
        """Поиск подстроки в строке"""
        if substring in string:
            rez = 0
            print("Подстрока входит в строку!")
        else:
            rez = -1
            print('Подстрока не входит в строку!')
        assert rez == 0, 'substring not found'