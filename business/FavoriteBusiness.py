from page.favorite_page import FavaoritePage


class FavoriteBusiness(object):
    fb = FavaoritePage()

    # 收藏房屋
    def FavoriteHouse(self):
        self.fb.toWodeSettingHouseDetail()
        self.fb.toHouseDetailFav()
        self.fb.toHouseDetailBack()
        self.fb.toWodeBack()
        self.fb.toFavoriteButton()
        self.fb.toFavCity()
        self.fb.toFavCityBack()
        self.fb.toFavPageIcon()
        self.fb.toFavIconCancle()
        self.fb.toFavPageIcon()
        self.fb.toFavIconOK()
        self.fb.toTime()
        # 收藏房东
        # self.fb.toFavLandlord()
        # self.fb.toAround()
        # self.fb.toMainSearchButton()
        # # 第一种，在列表页点击房东头像直接进入
        # self.fb.toSerachHouseClickLandlord()
        # # 第二种：先进入房屋详情页面， 在房屋详情页面点击：联系房东
        # # self.fb.toSearchHouseClickHouseDetail()
        # # self.fb.swipe_down()
        # # self.fb.toHouseDetailClickLandlord()
        # self.fb.toLandlordDetailClickFav()
        # self.fb.toLandlordDetailClickBack()
        # self.fb.toSearchhouseClickBack()
        # self.fb.toFavoriteButton()
        # self.fb.toFavClickLandlord()
        # self.fb.toLandlordClickCancleIcon()
        # self.fb.toLandlordDetailClickBack()

        # 收藏文章
        # self.fb.toTime()
        # self.fb.toFeedTab()
        # self.fb.toFeedAround()
        # self.fb.toFeedButton()
        # self.fb.toFeedPopup()
        # self.fb.toFeedListFavorite()
        # self.fb.toFeedFavDialog()
        # self.fb.toFavButton()
        # self.fb.toFavClickDetail()
        # self.fb.toFeedCancleFav()
        # self.fb.toFeedDetailBack()
