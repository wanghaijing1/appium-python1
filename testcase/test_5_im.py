from business.IMBusiness import IMBusiness
import unittest
class ImTest(unittest.TestCase):
    im = IMBusiness()
    def test_im(self):
        self.im.IM()
