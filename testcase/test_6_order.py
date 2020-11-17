from business.OrderBusiness import OrderBusiness
import unittest
class OrderTest(unittest.TestCase):
    order = OrderBusiness()
    def test_Order(self):
        self.order.SubmitOrder()