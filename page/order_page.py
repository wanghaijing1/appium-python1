from base.App import DriverClient


class OrderPage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    # 现在预订
    def toImmediatelyOrder(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[4]").click()

    #  提交订单
    def toSubmitOrders(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()

    #  在支付页返回
    def toPayBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/pay_library_activity_online_payment_iv_back").click()

    # 暂时放弃
    def toGiveUpPay(self):
        self.driver.find_element_by_id(
            "com.tujia.hotel:id/pay_library_view_second_confirm_dialog_tv_left_button").click()

    #  在订单详情页返回
    def toOrderDetailBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]").click()

    # 在房屋详情页操作返回
    def toHouseDetail(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[1]").click()

    def toPersionalCenterBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 个人中心页面查看全部订单
    def toCenterAllOrder(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/order_subTitle").click()

    # 在订单列表页操作返回
    def OrderListBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/order_list_left_back_btn").click()

    def toTime(self):
        self.driver.implicitly_wait(10)

    # 在订单详情页面点击取消按钮
    def toOrderDetailClickCancleButton(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]").click()

    # 在取消订单页面，点击：订单待支付弹窗
    def toOrderDetailPopup(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.widget.Button").click()

    # 在取消订单页面，点击继续按钮
    def toOrderDetailContinueButton(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[10]/android.view.View").click()

    # 在取消订单页面，选择取消原因
    def toOrderDetailCancleReason(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]").click()

    # 在取消订单页面，进行提交
    def toOrderDetailSubject(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View").click()

    def toWodeSettingHouseDetail(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_5").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/iv_setting").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/idDirect").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/idContent").send_keys("28509657")
        self.driver.find_element_by_id("com.tujia.hotel:id/idButton").click()
