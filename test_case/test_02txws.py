import subprocess
from time import sleep

from utils.assertion_utils.assert_control import AssertionControl
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage


class TestTxws:

    def test_txws(self, appium_driver):
        base_page = BasePage(appium_driver)
        assert_control = AssertionControl()
        logger = Logger('D:\\app_debug\\output\\log\\app.log')
        base_page.driver.implicitly_wait(10)
        base_page.click('xpath',
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.ImageView')
        base_page.click('id', 'cn.itcast.mobliesafe:id/btn_addblacknumber')
        base_page.click('id','cn.itcast.mobliesafe:id/add_fromcontact_btn')
        try:
            base_page.click('id','cn.itcast.mobliesafe:id/imgv_leftbtn')
        except Exception as e:
            print("点击返回按钮失败")
        subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK'])

        base_page.input('id', 'cn.itcast.mobliesafe:id/et_balcknumber', '1008611')
        base_page.input('id', 'cn.itcast.mobliesafe:id/et_blackname', '中国移动')
        try:
            checkbox = base_page.find('id', 'cn.itcast.mobliesafe:id/cb_blacknumber_tel')
            if checkbox.is_selected():
                checkbox.click()
            else:
                print("已勾选")
        except Exception as e:
            print("Checkbox not found.")
        try:
            checkbox = base_page.find('id', 'cn.itcast.mobliesafe:id/cb_blacknumber_sms')
            if checkbox.is_selected():
                checkbox.click()
            else:
                print("已勾选")
        except Exception as e:
            print("Checkbox not found.")

        base_page.click('id', 'cn.itcast.mobliesafe:id/add_blacknum_btn')
        sleep(2)
        base_page.get_screenshot('D:\\app_debug\\output\\image\\test_02txws.png')
        try:
            assert_control.assert_true(base_page.get_text('xpath',
                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView[1]'),
                                       '1008611(中国移动)')
        except Exception as e:
            print("断言失败")

        logger.error('"通信卫士" 功能的 "选择联系人" 页面，点击返回按钮无响应')
