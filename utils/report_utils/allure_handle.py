# 封装的allure的一些操作
import allure

class AllureHandle:
    def __init__(self):
        pass

    @staticmethod
    def attach_screenshot(driver, name="Screenshot"):
        """在报告中添加截图"""
        allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def attach_page_source(driver, name="Page Source"):
        """在报告中添加页面源码"""
        allure.attach(driver.page_source, name=name, attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def attach_text(text, name="Text"):
        """在报告中添加文本"""
        allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def add_step(step_name, step_description=""):
        """添加测试步骤"""
        allure.step(step_name)
        if step_description:
            allure.attach(step_description, name="Description", attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def add_description(description):
        """添加测试描述"""
        allure.description(description)

    @staticmethod
    def add_label(label_name, label_value):
        """添加测试标签"""
        allure.label(label_name, label_value)


