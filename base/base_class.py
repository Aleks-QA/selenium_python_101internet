import datetime
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class Base:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Get current url')
    def get_current_url(self):
        """Метод возвращающий URL"""
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')
        return get_url

    @allure.step('Get screenshot')
    def get_screenshot(self):
        """Сделать скриншот"""
        now_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(
            '.\\screen\\' + name_screenshot)
        print('Сделан скриншот')

    @allure.step('Finding a substring in a string')
    def find_substring(self, substring, string):
        """Поиск подстроки в строке"""
        if substring in string:
            rez = 0
        else:
            rez = -1
        assert rez == 0, 'substring not found'

    @allure.step('Checking that the element is present in the DOM of the page and is visible.')
    def element_is_visible(self, locator, timeout=20):
        """Ожидание проверки того, что элемент присутствует в DOM страницы и виден."""
        # self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Checking that all elements are present in the DOM of the page and are visible')
    def elements_are_visible(self, locator, timeout=20):
        """Ожидание проверки того, что все элементы присутствуют в DOM страницы и видны."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Check if an element exists in the DOM of the page.')
    def element_is_present(self, locator, timeout=20):
        """Ожидание проверки наличия элемента в DOM страницы."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Check if an element exists in the DOM of the page.')
    def elements_are_present(self, locator, timeout=20):
        """Ожидание проверки наличия хотя бы одного элемента на веб-странице."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Checks that the element is either invisible or not in the DOM.')
    def element_is_not_visible(self, locator, timeout=20):
        """Ожидание проверки того, что элемент либо невидим, либо отсутствует в DOM."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Checks that the item is visible and enabled, so you can click it.')
    def element_is_clickable(self, locator, timeout=20):
        """Ожидание проверки, что элемент видно и включен, поэтому вы можете щелкнуть его."""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('To check the presence of this text in the specified element.')
    def text_present_in_element(self, locator, text, timeout=20):
        """Ожидание проверки наличия данного текста в указанном элементе."""
        return wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Go to specified element')
    def go_to_element(self, element):
        """Перейти к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Double click')
    def action_double_click(self, element):
        """Двойной клик"""
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step('Right click')
    def action_right_click(self, element):
        """Клик правой кнопкой"""
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step('Delete a visible item')
    def remove_element(self, locator, timeout=20):
        """Удалить видимый элемент"""
        element = self.element_is_visible(locator, timeout)
        self.driver.execute_script("arguments[0].remove();", element)

    # @allure.step('Move cursor to element')
    # def move_to_element(self, x_path_element):
    #     """Переместиться к элементу + скролл"""
    #     scroll_by = 'window.scrollBy(0, -200);'
    #     self.driver.execute_script(scroll_by)
    #     action = ActionChains(self.driver)
    #     action.move_to_element(x_path_element).perform()


    # ====================================ОЖИДАНИЯ===================================================
    #
    # def wait_page_loaded(self, timeout=60, check_js_complete=True,
    #                      check_page_changes=False, check_images=False,
    #                      wait_for_element=None,
    #                      wait_for_xpath_to_disappear='',
    #                      sleep_time=2):
    #     """ This function waits until the page will be completely loaded.
    #         We use many different ways to detect is page loaded or not:
    #         1) Check JS status
    #         2) Check modification in source code of the page
    #         3) Check that all images uploaded completely
    #            (Note: this check is disabled by default)
    #         4) Check that expected elements presented on the page
    #     """
    #
    #     page_loaded = False
    #     double_check = False
    #     k = 0
    #
    #     if sleep_time:
    #         time.sleep(sleep_time)
    #
    #     # Get source code of the page to track changes in HTML:
    #     source = ''
    #     try:
    #         source = self._web_driver.page_source
    #     except:
    #         pass
    #
    #     # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    #     while not page_loaded:
    #         time.sleep(0.5)
    #         k += 1
    #
    #         if check_js_complete:
    #             # Scroll down and wait when page will be loaded:
    #             try:
    #                 self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #                 page_loaded = self._web_driver.execute_script("return document.readyState == 'complete';")
    #             except Exception as e:
    #                 pass
    #
    #         if page_loaded and check_page_changes:
    #             # Check if the page source was changed
    #             new_source = ''
    #             try:
    #                 new_source = self._web_driver.page_source
    #             except:
    #                 pass
    #
    #             page_loaded = new_source == source
    #             source = new_source
    #
    #         # Wait when some element will disappear:
    #         if page_loaded and wait_for_xpath_to_disappear:
    #             bad_element = None
    #
    #             try:
    #                 bad_element = WebDriverWait(self._web_driver, 0.1).until(
    #                     EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
    #                 )
    #             except:
    #                 pass  # Ignore timeout errors
    #
    #             page_loaded = not bad_element
    #
    #         if page_loaded and wait_for_element:
    #             try:
    #                 page_loaded = WebDriverWait(self._web_driver, 0.1).until(
    #                     EC.element_to_be_clickable(wait_for_element._locator)
    #                 )
    #             except:
    #                 pass  # Ignore timeout errors
    #
    #         assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)
    #
    #         # Check two times that page completely loaded:
    #         if page_loaded and not double_check:
    #             page_loaded = False
    #             double_check = True
    #
    #         # Go up:
    #         self._web_driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
