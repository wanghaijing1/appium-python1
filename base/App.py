from appium import webdriver
from utils.AppUtils import AppUtils
class Driver_configure(object):
    __instance = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Driver_configure, cls)
            a = AppUtils()
            apkpath = a.getApp()
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            #小米
            desired_caps['deviceName'] = 'f9bc5ef8'
            desired_caps['platformVersion'] = '10'
            # 获取apk下当前的相对路径
            desired_caps['app'] = apkpath
            print(apkpath)
            desired_caps['noReset'] = True
            desired_caps['appPackage'] = 'com.tujia.hotel'
            desired_caps['appActivity'] = 'com.tujia.hotel.main.StartActivity'
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            cls._instance.driver.implicitly_wait(10)
            return cls._instance
        else:
            return cls._instance

class DriverClient(Driver_configure):
    def getDriver(self):
        return self.driver
