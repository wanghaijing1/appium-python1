from business.LoginBusiness import LoginBusiness
import unittest
class loginTest(unittest.TestCase):
    loginBusiness = LoginBusiness()
    def test_Login(self):
        self.loginBusiness.LoginService()

