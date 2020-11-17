from business.FeedBusiness import FeedBusiness
import unittest
class feedTest(unittest.TestCase):
    feed = FeedBusiness()
    def test_feed(self):
        self.feed.Feed()
