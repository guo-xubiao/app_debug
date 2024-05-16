from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestSzzx:
    def test_szzx(self, appium_driver):
        base_page = BasePage(appium_driver)
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget"
                                 ".LinearLayout[9]/android.widget.ImageView")
        base_page.click('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.RelativeLayout['
                                 '2]/android.widget.RelativeLayout/android.widget.ToggleButton')
        base_page.click('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                 '.widget.RelativeLayout['
                                 '3]/android.widget.RelativeLayout/android.widget.ToggleButton')
        logger.info('"设置中心" 功能测试成功')
