import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.')) # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    # __init__里面的构造函数，意思就是创建一个对象就会自动有一个driver变量；
    # 在实际脚本过程中unittest中的setUp方法里，browser = BrowserEngine(
    #     self)，只是创建了一个BrowserEngine对象而已，对象一创建，就掉构造函数，就有driver这个属性，
    # 接下来语句self.driver = browser.get_browser(), 就告诉了driver是哪一个具体的浏览器实例。
    # 理解下类的创建和函数的调用，分别和参数的关系。

    # read the browser type from config.ini file,return the driver
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is：%s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting Ie browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        # 注意，log 写在前面
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()










