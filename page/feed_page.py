from base.App import DriverClient


class FeedPage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    # 发现按钮
    def toFeedButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_3").click()

    # 在feed列表页点击卡片进入feed详情页
    def toFeedListClickCard(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/img_card_theme").click()

    # 在feed详情页收藏文章
    def toFeedDetailFav(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/find_article_detail_view_iv_bottom_collection_icon").click()

    # 在feed详情页点赞文章
    def toFeedDetailLike(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/find_article_like_icon").click()

    # 在feed详情页分享文章
    def toFeedDetailShare(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/find_article_detail_view_iv_bottom_share_icon").click()

    # 在feed详情页面操作返回
    def toFeedDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/load_panel_back_image").click()

    # 在feed列表页点击收藏
    def toFeedListFav(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/iv_collection").click()

    # 在feed列表页点赞
    def toFeedListLike(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/ckb_great").click()

    # 在Feed列表页点击+号
    def toFeedListClickPlus(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tv_publish").click()

    # 在Feed列表页点击+号后进行刷新
    def toFeedClickPlusRerach(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/buttonError").click()

    # 在feed流页面增加权限
    def toFeedClickPlusPermission(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/ok").click()

    def toDevicePermission(self):
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_button").click()

    # 在+号详情页操作返回
    def toFeedPlusDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/image_close").click()

    # 点击 收藏热榜tab
    def toFeedListClickCMS1(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[2]").click()


    # 点击 民宿片场tab
    def toFeedListClickCMS2(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[3]").click()

    #  点击 亲子好房tab
    def toFeedListClickCMS3(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[4]").click()

    #  点击 出去嗨tab
    def toFeedListClickCMS4(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[5]").click()

    #    关闭[发布文章送积分]弹窗
    def toFeedPopup(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/start_popup_close").click()

    #   第一次点赞文章，弹出确认框，点击[确认] 关闭按钮
    def toFeedLikeOK(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/dialog_btn_cancel").click()

    #   在文章详情页分享-取消按钮
    def toFeedShareCancle(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/article_share_cancel").click()
