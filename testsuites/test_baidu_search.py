import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        # 为什么两个参数的时候，这么写就不对呢？
        # #BrowserEngine.open_browser(self)

        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)


    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()
        # BrowserEngine.quit_browser(self)
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

        homepage = HomePage(self.driver) # 初始化页面的对象实例，来自浏览器引擎类，
        # 最重要的是保持前后driver的一致性
        time.sleep(5)
        homepage.type_search("selenium\n") # 调用页面对象中的方法
        #homepage.send_submit_btn() # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img() # 调用基类截图方法，homepage 继承了基类

        try:
            #assert 'selenium' in self.driver.title
            assert 'selenium' in homepage.get_page_title() # 调用页面对象继承基类中的获取页面标题方法
            print("Test pass")
        except Exception as e:
            print("Test fail",format(e))


    def test_search2(self):
        homepage = HomePage(self.driver)
        time.sleep(1)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()


if __name__ == '__main__':
    unittest.main()

