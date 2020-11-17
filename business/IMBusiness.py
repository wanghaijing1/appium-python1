from page.IM_page import ImPage

class IMBusiness(object):
    im = ImPage()
    def IM(self):
        # 系统通知
        self.im.toImButton()
        self.im.toNotice()
        # self.im.toMarkRead()
        self.im.toNoticeOrderDetail()
        self.im.toNoticeOrderDetailBack()
        self.im.toNoticeDetailBack()
        # 优惠促销
        self.im.toPromotionPanel()
        self.im.toPromotionDetailClickOrder()
        self.im.toTime()
        self.im.toPromotionOrderDetailBack()
        self.im.toPromotionPanelDetailBack()
        # self.im.toImListFirst()
        # self.im.toImPermission()
        # self.im.toImDevicePermission()
        # self.im.toTime()
        # self.im.toImInput()
        # self.im.toImInputSendButton()
        # self.im.toImDetailBack()

