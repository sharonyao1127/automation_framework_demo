from framework.base_page import  BasePage



class NewsHomePage(BasePage):
    # 点击体育新闻入口
    sports_link = "xpath=>//div[@id='channel-all']//li[7]//a[1]"


    def click_sports(self):
        self.switch_page()
        self.click(self.sports_link)
        self.sleep(2)