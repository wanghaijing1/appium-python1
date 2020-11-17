from page.login_page import LoginPage
class LoginBusiness():
    loginPage = LoginPage()
    def LoginService(self):
        self.loginPage.toYes()
        self.loginPage.toskip()
        self.loginPage.toUpgradeAlert()
        self.loginPage.toLoginAlertClose()
        self.loginPage.toOneLoginPermissionClose()
        self.loginPage.toLocationPermission()
        self.loginPage.toWode()
        self.loginPage.toRegisteAndLogin()
        self.loginPage.toAccount_login()
        self.loginPage.sendAccout()
        self.loginPage.sendPwa()
        self.loginPage.toLoginButton()
        self.loginPage.totapAssertCircle()
        self.loginPage.toTime()