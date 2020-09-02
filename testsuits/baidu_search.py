import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        # 为什么两个参数的时候，这么写就不对呢？
        # #BrowserEngine.open_browser(self)

        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # self.driver.quit()
        BrowserEngine.quit_browser(self)
        # 原代码执行完成之后未打印关闭浏览器日志，
        # 在baidu_search.py中将tearDown方法中关闭浏览器代码改为
        # 调用BrowserEngine类的quit_browser方法：BrowserEngine.quit_browser(self)

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """

        # self.driver.find_element_by_id('kw').send_keys("selenium\n")
        # time.sleep(1)

        # 调用基类的方法
        homepage = HomePage(self.driver)
        homepage.type_search("selenium\n")
        time.sleep(2)

        try:
            assert 'selenium' in self.driver.title
            print("Test pass")
        except Exception as e:
            print("Test fail",format(e))



if __name__ == '__main__':
    unittest.main()

