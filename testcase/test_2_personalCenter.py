from business.PersonalCenterBusiness import PersonalCenterBusiness
import unittest
class PersonalCenterTest(unittest.TestCase):
    per = PersonalCenterBusiness()
    def test_PersonalCenter(self):
        self.per.PersonalCenter()