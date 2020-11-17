from base.App import DriverClient


class FavaoritePage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    def toFavoriteButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_2").click()

    # 随便逛逛
    def toAround(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()

    # 点击列表页中的第一个房屋，进入房屋详情页

    def toFirstHouse(self):
        self.driver.find_element_by_xpath(
            "(//android.view.ViewGroup[@content-desc='o_bnb_inn_product_app'])[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]").click()

    # 进入房屋详情页点击收藏ICON

    def toHouseDetailFav(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()

        # 房屋详情页操作返回

    def toHouseDetailBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup[1]").click()

        # 首页："开始搜索"

    def toSearchHouse(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView").click()

        #  收藏模块-全部城市

    def toFavCity(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]").click()
        # 收藏模块-收藏icon

    def toFavPageIcon(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]").click()
        #  收藏模块-全部城市-返回

    def toFavCityBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()

    # 收藏模块，点击收藏icon-取消按钮

    def toFavIconCancle(self):
        self.driver.find_element_by_id("android:id/button2").click()

    # 收藏模块，点击收藏icon-确认按钮

    def toFavIconOK(self):
        self.driver.find_element_by_id("android:id/button1").click()

    # 房东
    # 收藏模块-点击房东tab

    def toFavLandlord(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()

    # 点击首页【开始搜索】按钮

    def toMainSearchButton(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[7]/android.view.ViewGroup").click()

        #  点击列表页中第一个房子的房东头像

    def toSerachHouseClickLandlord(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]").click()

    # 在房东主页点击收藏ICon

    def toLandlordDetailClickFav(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/landlord_detail_follow_image").click()

    # 在房东主页操作返回

    def toLandlordDetailClickBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/landlord_detail_back_image").click()

        # 在列表页操作返回

    def toSearchhouseClickBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]").click()

    # 在收藏房东模块，点击房东头像

    def toFavClickLandlord(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup").click()

    # 在房东详情页取消收藏

    def toLandlordClickCancleIcon(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/landlord_detail_follow_image").click()

    def toTime(self):
        self.driver.implicitly_wait(5)

    #  我的-设置-进入房屋详情页面
    def toWodeSettingHouseDetail(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/iv_setting").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/idDirect").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/idContent").send_keys("7695293")
        self.driver.find_element_by_id("com.tujia.hotel:id/idButton").click()

    # 从设置页面操作返回
    def toWodeBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 收藏模块-发现-随便逛逛
    def toFeedAround(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()

    # 收藏按钮
    def toFavButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_2").click()

    # 发现按钮
    def toFeedButton(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tj_widget_radio_3").click()

    # 在feed页面收藏文章
    def toFeedListFavorite(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/iv_collection").click()

    # 收藏文章后-弹出弹出框-点击：“确认” 按钮
    def toFeedFavDialog(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/dialog_btn_cancel").click()

    # 在收藏-文章详情页面取消收藏
    def toFavClickDetail(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]").click()

    # 在文章详情页取消
    def toFeedCancleFav(self):
        self.driver.find_element_by_id(
            "com.tujia.hotel:id/find_article_detail_view_rl_bottom_collection_container").click()

    # 在文章详情页返回
    def toFeedDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/find_article_detail_title_bar_iv_back").click()

    # 点击 Feed tab页
    def toFeedTab(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]").click()

    # 关闭[发布文章送积分]弹窗
    def toFeedPopup(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/start_popup_close").click()

    # 向下滑动
    def swipe_down(self, t=500, n=2):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    # 在从列表页进入房屋详情页
    def toSearchHouseClickHouseDetail(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]").click()
    #在房屋详情页面中  点击 联系房东
    def toHouseDetailClickLandlord(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]").click()