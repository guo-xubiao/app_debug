from utils.assertion_utils.assert_control import AssertionControl
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestSjfd:

    def test_sjfd(self, appium_driver):
        base_page = BasePage(appium_driver)
        assert_control = AssertionControl()
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        try:
            base_page.click('id', 'android:id/button1')
        except Exception as e:
            print("非首次打开，不需要执行")

        try:
            base_page.click('id', 'com.android.settings:id/action_button')
        except Exception as e:
            print("非首次打开，不需要执行")

        base_page.click('xpath',
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.ImageView')
        try:
            base_page.input('id', 'cn.itcast.mobliesafe:id/et_firstpwd', '123456')
            base_page.input('id', 'cn.itcast.mobliesafe:id/et_affirm_password', '123456')
            base_page.click('id', 'cn.itcast.mobliesafe:id/btn_ok')
        except Exception as e:
            print("非首次打开，不需要执行")

        base_page.input('id', 'cn.itcast.mobliesafe:id/et_inter_password', '123456')
        base_page.click('id', 'cn.itcast.mobliesafe:id/btn_comfirm')
        try:
            base_page.click('id', 'cn.itcast.mobliesafe:id/rl_inter_setup_wizard')
        except Exception as e:
            print("非首次打开，不需要执行")

        try:
            base_page.swipe_left()
        except Exception as e:
            print("非首次打开，不需要执行")

        try:
            base_page.click('id', 'cn.itcast.mobliesafe:id/btn_bind_sim')
        except Exception as e:
            print("非首次打开，不需要执行")

        try:
            base_page.swipe_left()
        except Exception as e:
            print("非首次打开，不需要执行")

        base_page.click('id', 'cn.itcast.mobliesafe:id/btn_addcontact')
        base_page.click('id', 'cn.itcast.mobliesafe:id/imgv_leftbtn')
        try:
            base_page.input('id', 'cn.itcast.mobliesafe:id/et_inputphone', '10086')
            base_page.swipe_left()
            base_page.swipe_left()
        except Exception as e:
            print("非首次打开，不需要执行")
        if not base_page.get_text('id', 'cn.itcast.mobliesafe:id/tv_lostfind_protectstauts') == "防盗保护已经开启":
            base_page.click('id', 'cn.itcast.mobliesafe:id/togglebtn_lostfind')
        assert_control.assert_true(
            base_page.get_text('id', 'cn.itcast.mobliesafe:id/tv_lostfind_protectstauts') == "防盗保护已经开启",
            "断言失败")

        logger.info('"手机防盗" 功能测试通过')
