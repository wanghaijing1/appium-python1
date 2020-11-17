from base.App import DriverClient

class LoginPage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    # 点击同意弹出框
    def toYes(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tv_yes").click()

    # 点击跳过
    def toskip(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/first_guide_text_splash_skip").click()

    #  一加手机弹出框
    def toPermission(self):
        # 一加手机弹窗框
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        # # 小米手机权限弹出框
        # self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_onetime_button").click()

    # 一加手机取消弹出窗
    def toCancleButton(self):
        self.driver.find_element_by_id("android:id/button3").click()

   # 首页自动弹出登录弹出框-关闭
    def toLoginAlertClose(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/iv_close_dlg").click()

   #关闭一键登录的权限弹出框
    def toOneLoginPermissionClose(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/ok").click()

    # 关闭电话权限
    def toPhonePermission(self):
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()

    # [小米手机]关闭位置权限
    def toLocationPermission(self):
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button").click()

    # 我的
    def toWode(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_5").click()

    # 登录/注册 按钮
    def toRegisteAndLogin(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/user_name").click()

    # 账号密码登录
    def toAccount_login(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tv_account_login").click()

    # 赋值用户名
    def sendAccout(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/et_account_input").send_keys("15810651002")

    # 赋值密码
    def sendPwa(self):
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_id("com.tujia.hotel:id/et_pwd_input").send_keys("tujia1234")

    # 登录按钮
    def toLoginButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tv_login").click()

    # 智能验证
    def totapAssertCircle(self):
        self.driver.find_element_by_id("SM_TXT_1").click()

    # 跳转到首页
    def toMain(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_1").click()

    def toTime(self):
        self.driver.implicitly_wait(8)
    #升级弹出框
    def toUpgradeAlert(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tv_remind_later").click()
