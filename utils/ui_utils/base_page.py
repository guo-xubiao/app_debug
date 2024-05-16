import time
from appium import webdriver

class BasePage:
    def __init__(self, driver: webdriver.Remote = None):
        self.driver = driver

    def find(self, by, locator):
        """查找单个元素"""
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        """查找多个元素"""
        return self.driver.find_elements(by, locator)

    def click(self, by: object, locator: object) -> object:
        """点击元素"""
        self.find(by, locator).click()

    def input(self, by, locator, text):
        """向元素输入文本"""
        self.find(by, locator).send_keys(text)

    def get_text(self, by, locator):
        """获取元素文本"""
        return self.find(by, locator).text

    def get_attribute(self, by, locator, attribute):
        """获取元素属性"""
        return self.find(by, locator).get_attribute(attribute)

    def swipe(self, start_x, start_y, end_x, end_y):
        """滑动操作"""
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_left(self):
        """向左滑动"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.swipe(x * 0.9, y * 0.5, x * 0.1, y * 0.5)

    def swipe_right(self):
        """向右滑动"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.swipe(x * 0.1, y * 0.5, x * 0.9, y * 0.5)

    def swipe_up(self):
        """向上滑动"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.1)

    def swipe_down(self):
        """向下滑动"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.swipe(x * 0.5, y * 0.1, x * 0.5, y * 0.9)

    def swipe_to_find(self, by, locator, direction='left', max_swipes=10):
        """滑动查找元素"""
        element = None
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        if direction == 'left':
            start_x = x * 0.9
            end_x = x * 0.1
            start_y = y * 0.5

        elif direction == 'right':
            start_x = x * 0.1
            end_x = x * 0.9
            start_y = y * 0.5

        elif direction == 'up':
            start_x = x * 0.5
            end_x = x * 0.5
            start_y = y * 0.9

        elif direction == 'down':
            start_x = x * 0.5
            end_x = x * 0.5
            start_y = y * 0.1

        for _ in range(max_swipes):
            if element := self.finds(by, locator):
                return element[0]

            self.swipe(start_x, start_y, end_x, start_y)

        return None

    def wait_for_element(self, by, locator, timeout=10):
        """等待元素出现"""
        element = None
        start_time = time.time()

        while time.time() - start_time < timeout:
            element = self.find(by, locator)

            if element:
                return element

            time.sleep(1)

        return None

    def wait_for_elements(self, by, locator, timeout=10):
        """等待元素出现"""
        elements = None
        start_time = time.time()

        while time.time() - start_time < timeout:
            elements = self.finds(by, locator)

            if elements and len(elements) > 0:
                return elements

            time.sleep(1)

        return None

    def get_screenshot(self, filename):
        """
        获取当前页面的截图
        """
        self.driver.save_screenshot(filename)
