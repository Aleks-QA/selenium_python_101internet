import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Base:
    def __init__(self, driver):
        self.driver = driver
        # self.url = url


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

    def place_the_cursor_css(self, locator_css):
        """Навести курсор на элемент CSS"""
        hoverable = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator_css)))
        ActionChains(self.driver).move_to_element(hoverable).perform()

    def place_the_cursor_xpath(self, locator_xpath):
        """Навести курсор на элемент XPATH"""
        hoverable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_xpath)))
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

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        # жди 10 секунд пока локатор не будет представлен
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        # жди 10 секунд пока все элементы не будут представлен
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        # найти элемент и взять текст из дом дерева(не обязательно чтобы был виден)
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        # найти элементы и взять текст из дом дерева(не обязательно чтобы был виден)
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        # использование элемента который не виден
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        # кликабельный
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        # перемещать нас к нужному элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # =======================================================================================

    def element_is_visible(self, locator, timeout=5):
        """Ожидание проверки того, что элемент присутствует в DOM страницы и виден."""
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """Ожидание проверки того, что все элементы присутствуют в DOM страницы и видны."""
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """Ожидание проверки наличия элемента в DOM страницы."""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """Ожидание проверки наличия хотя бы одного элемента на веб-странице."""
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """Ожидание проверки того, что элемент либо невидим, либо отсутствует в DOM."""
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """Ожидание проверки, что элемент видно и включен, поэтому вы можете щелкнуть его."""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to(self, page_type):
        if page_type == 'window':
            self.driver.switch_to.window(self.driver.window_handles[1])
        elif page_type == 'alert_text':
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        elif page_type == 'alert_button':
            alert_window = self.driver.switch_to.alert
            return alert_window

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_drag_and_drop_by_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    # =======================================================================================


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