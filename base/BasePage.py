#封装一些公共的方法和常用的弹框的验证
from base.App import DriverClient
import os
class BasePage:
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    def toAdb(self):
        os.system('adb uninstall "io.appium.android.ime"')
        os.system('adb uninstall "io.appium.settings"')
        os.system('adb uninstall "io.appium.unlock"')

    # 卸载app
    def  toDeleteAPP(self):
        self.driver.remove_app("com.tujia.hotel")

    def toTime(self):
        self.driver.implicitly_wait(10)

    # 向上滑动
    def swipeUp(self, t=500, n=1):
            s = self.driver.get_window_size()
            x1 = s['width'] * 0.5
            y1 = s['height'] * 0.75
            y2 = s['height'] * 0.25
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def swipe_down(self, t=500, n=1):
            s = self.driver.get_window_size()
            x1 = s['width'] * 0.5  # x坐标
            y1 = s['height'] * 0.25  # 起点y坐标
            y2 = s['height'] * 0.75  # 终点y坐标
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动
    def swipe_left(self, t=500, n=1):
            s = self.driver.get_window_size()
            x1 = s['width'] * 0.75
            y1 = s['height'] * 0.5
            x2 = s['width'] * 0.25
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)

    # 向右
    def swipe_right(self, t=500, n=1):
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.25
            y1 = l['height'] * 0.5
            x2 = l['width'] * 0.75
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)






