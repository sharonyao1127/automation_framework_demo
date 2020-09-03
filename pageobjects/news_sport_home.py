from framework.base_page import BasePage
import time

class SportNewsHomePage(BasePage):
    # NBA入口
    nba_link = "xpath=>//div[@class='schedule clearfix']//li[1]"
    time.sleep(1)

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)


