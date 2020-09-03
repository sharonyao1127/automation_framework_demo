
import time
import unittest
from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()
        #self.driver.find_element_by_xpath("//div[@id='s-top-left']/a[@href='http://news.baidu.com']").click()

        # 初始化一个百度新闻主页，并点击体育链接
        newhome = NewsHomePage(self.driver)
        newhome.click_sports()
        time.sleep(3)
        # self.driver.find_element_by_xpath("//div[@id='channel-all']//li[7]//a[1]").click()

        # 初始化一个体育主页，并点击NBA
        sportsnewhome = SportNewsHomePage(self.driver)

        sportsnewhome.click_nba_link()
        # self.driver.find_element_by_xpath("//div[@class='schedule clearfix']//li[1]").click()
        sportsnewhome.get_windows_img()

if __name__ == '__main__':
    unittest.main()











