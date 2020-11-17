from business.FavoriteBusiness import FavoriteBusiness
import unittest


class FavoriteTest(unittest.TestCase):
    lb = FavoriteBusiness()

    # 收藏房屋
    def test_FavoriteHouse(self):
        self.lb.FavoriteHouse()

