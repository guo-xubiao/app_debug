from utils.assertion_utils.assert_control import AssertionControl
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestRjgj:

    def test_rjgj(self, appium_driver):
        base_page = BasePage(appium_driver)
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        base_page.click("xpath",
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android"
                        ".widget.LinearLayout[3]/android.widget.ImageView")
        base_page.click("xpath",
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android"
                        ".widget.LinearLayout[4]/android.widget.RelativeLayout")
        base_page.click("id","cn.itcast.mobliesafe:id/tv_setting_app")

        logger.info('"软件管家" 功能测试通过')