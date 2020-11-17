from page.order_page import OrderPage
class OrderBusiness(object):
    order = OrderPage()
    def SubmitOrder(self):
        self.order.toWodeSettingHouseDetail()
        self.order.toImmediatelyOrder()
        self.order.toSubmitOrders()
        self.order.toPayBack()
        self.order.toGiveUpPay()
        self.order.toOrderDetailBack()
        self.order.toTime()
        self.order.toHouseDetail()
        self.order.toPersionalCenterBack()
        self.order.toCenterAllOrder()
        self.order.OrderListBack()
