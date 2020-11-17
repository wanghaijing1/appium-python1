from base.App import DriverClient


class PersonalCenterPage():
    def __init__(cls):
        cls.driver = DriverClient().getDriver()

    # 点击红包进入红包列表页
    def RedPackage(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tvRedPackage").click()

    # 红包列表页操作返回
    def RedPackageBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 进入红包明细页面
    def RedPackageDetail(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/head_right_title").click()

    # 红包明细页面返回
    def RedPackageDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 点击积分商城进入积分明细页面
    def Score(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tvScoreLable").click()

    #  积分明细页面操作返回
    def ScoreDetailBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 点击余额
    def Balance(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/tvBalance").click()

    # 在余额页面操作返回
    def BalanceBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]").click()

    # 内容管理
    def ContentManager(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[1]").click()

    # 内容管理-返回
    def ContentManagerBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 浏览历史
    def History(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[2]").click()

    # 浏览历史-返回
    def HistoryBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]").click()

    # 常用信息
    def Information(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[3]").click()

    # 常用信息-添加入住人
    def InsertPersonInformation(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/addBtn").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/name").send_keys("王海静")
        self.driver.find_element_by_id("com.tujia.hotel:id/etFamilyName").send_keys("wang")
        self.driver.find_element_by_id("com.tujia.hotel:id/etFirstName").send_keys("haijing")
        self.driver.find_element_by_id("com.tujia.hotel:id/tvAddCardType").click()
        # 选择护照
        self.driver.find_element_by_id("com.tujia.hotel:id/tvPassport").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/etCardNum").send_keys("1122334455")
        self.driver.find_element_by_id("com.tujia.hotel:id/etPhone").send_keys("15810651002")
        self.driver.find_element_by_id("com.tujia.hotel:id/etEmail").send_keys("1122@qq.com")
        self.driver.find_element_by_id("com.tujia.hotel:id/genderFemale").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/birthday").click()
        self.driver.find_element_by_id("android:id/button1").click()
        # 保存
        self.driver.find_element_by_id("com.tujia.hotel:id/head_right_title").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView").click()

    def detelePersonInformation(self):
        # 点击删除入住人按钮
        self.driver.find_element_by_id("com.tujia.hotel:id/deleteBtn").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/confirm").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/deleteBtn").click()
        self.driver.find_element_by_id("com.tujia.hotel:id/cancel").click()

    def InformationBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 开具发票
    def Invoices(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[4]").click()

    # 开具发票-返回
    def InvoicesBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]").click()

    # 邀请好友
    def InviteFriends(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[5]").click()

    # 邀请好友-返回
    def InviteFriendsBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 在线客服
    def OnlineService(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[6]").click()

    # 在线客服-返回
    def OnlineServiceBack(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]").click()

    # 卡包
    def Card(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[7]").click()

    # 卡包-返回
    def CardBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 邀请房东
    def InviteLandlord(self):
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[8]").click()

    # 邀请房东-返回
    def InviteLandlordBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    #  安全中心
    def SecurityCenter(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[9]").click()

    #  安全中心-返回
    def SecurityCenterBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    # 托管加盟
    def Trusteeship(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.RelativeLayout[10]").click()

    # 托管加盟-页面返回
    def TrusteeshipBack(self):
        self.driver.find_element_by_id("com.tujia.hotel:id/header_btn_left").click()

    def toTime(self):
        self.driver.implicitly_wait(3)




