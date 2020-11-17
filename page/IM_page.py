from base.App import DriverClient


# import os
class ImPage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    # 消息按钮
    def toImButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_4").click()

    # 在IMlist页面点击系统通知
    def toNotice(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/unreadOrderPanel").click()

    def toNoticeBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    #  在系统详情页面点击一键已读
    def toMarkRead(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/head_right_title").click()

    #  在系统通知页面点击查看详情
    def toNoticeOrderDetail(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/noticedetail").click()

    #  在订单详情页面返回
    def toNoticeOrderDetailBack(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]").click()

    #  在系统详情页面返回到消息列表
    def toNoticeDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    #  在消息列表页点击优惠促销
    def toPromotionPanel(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/unreadPromotePanel").click()

    #  在优惠详情页面操作返回
    def toPromotionPanelDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    #   在优惠列表详情页面点击查看详情
    def toPromotionDetailClickOrder(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/promotion_detail").click()

    #   在【优惠订】详情页面点击返回
    def toPromotionOrderDetailBack(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]").click()

    # 在消息列表获取第一个IM，并且进入IM详情页面
    def toImListFirst(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()

    # 在消息框输入发送内容
    def toImInput(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/messageContentInput").send_keys("你好")

    # 在IM聊天页面点击发送
    def toImInputSendButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/messageSendButton").click()

    #  在IM聊天详情页返回
    def toImDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/leftButton").click()

    #  在IM聊天页面权限验证
    def toImPermission(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/ok").click()

    #  在IM聊天页面设备权限验证
    def toImDevicePermission(self):
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_button").click()

    def toTime(self):
        self.driver.implicitly_wait(3)
