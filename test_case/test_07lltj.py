from utils.assertion_utils.assert_control import AssertionControl
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestLltj:

    def test_lltj(self, appium_driver):
        base_page = BasePage(appium_driver)
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        base_page.click("xpath",
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android"
                        ".widget.LinearLayout[7]/android.widget.ImageView")
        try:
            base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                     ".FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
                                     ".LinearLayout[2]/android.widget.Spinner/android.widget.LinearLayout")
            base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget"
                                     ".LinearLayout[3]")

            base_page.click("id", "cn.itcast.mobliesafe:id/btn_operator_finish")
        except Exception as e:
            print("运营商已选择，不需要执行")

            base_page.click("id", "cn.itcast.mobliesafe:id/btn_correction_flow")

        logger.info('"流量统计" 功能测试通过')