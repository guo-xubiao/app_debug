from time import sleep

from utils.assertion_utils.assert_control import AssertionControl
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestGjgj:

    def test_gjgj(self, appium_driver):
        base_page = BasePage(appium_driver)
        assert_control = AssertionControl()
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        base_page.click("xpath",
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android"
                        ".widget.LinearLayout[8]/android.widget.ImageView")

        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout["
                              "2]/android.widget.RelativeLayout")
        base_page.input("id","cn.itcast.mobliesafe:id/et_num_numbelongto","10001")
        base_page.click("id","cn.itcast.mobliesafe:id/btn_searchnumbelongto")
        assert_control.assert_true(base_page.get_text("id","cn.itcast.mobliesafe:id/tv_searchresult")=="归属地： 客服电话","测试失败")
        base_page.click("id","cn.itcast.mobliesafe:id/imgv_leftbtn")
        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout["
                                 "3]/android.widget.RelativeLayout")
        base_page.click("id", "cn.itcast.mobliesafe:id/mcp_smsbackup")
        base_page.click("id", "cn.itcast.mobliesafe:id/imgv_leftbtn")
        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout["
                                 "4]/android.widget.RelativeLayout")

        base_page.click("id", "cn.itcast.mobliesafe:id/mcp_reducition")
        base_page.get_screenshot('D:\\app_debug\\output\\image\\test_08gjgj.png')
        base_page.click("id", "android:id/button1")
        sleep(2)
        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout["
                                 "5]/android.widget.RelativeLayout")

        msge1 = base_page.get_text("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                            "/android.widget.FrameLayout/android.widget.LinearLayout/android.support"
                                            ".v4.view.ViewPager/android.widget.FrameLayout/android.widget"
                                            ".LinearLayout/android.widget.ListView/android.widget.RelativeLayout["
                                            "2]/android.widget.TextView")

        base_page.click("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android"
                                 ".widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android"
                                 ".widget.RelativeLayout[2]/android.widget.ImageView[2]")

        base_page.click("id", "cn.itcast.mobliesafe:id/tv_lock")

        msge2 = base_page.get_text("id", "cn.itcast.mobliesafe:id/tv_appname")

        assert_control.assert_true(msge1==msge2,"测试失败")

        base_page.click("id", "cn.itcast.mobliesafe:id/imgv_lock")
        base_page.click("id", "cn.itcast.mobliesafe:id/tv_unlock")
        sleep(2)
        assert_control.assert_true(msge2 == msge1, "测试失败")
        logger.error('"高级工具" 功能 "短信还原" 页面点击 "一键还原" 按钮后提示：很抱歉，“手机安全卫士“已停止运行。')




