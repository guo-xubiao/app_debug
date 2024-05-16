import pytest
from appium import webdriver


@pytest.fixture(scope="module")
def appium_driver():
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "SM-G988N",
        "appPackage": "cn.itcast.mobliesafe",
        "appActivity": "cn.itcast.mobliesafe.chapter01.SplashActivity",
        "noReset": True
    }

    # 初始化 Appium WebDriver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    yield driver

    # 在测试结束后关闭 WebDriver 连接
    driver.quit()