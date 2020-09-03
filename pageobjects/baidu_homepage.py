from framework.base_page import BasePage


# 页面对象，百度主页的元素定位和简单的操作函数
# 页面类主要是元素定位和页面操作写成函数，供测试类调用

class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id = 'su']"
    # 元素定位写法，=>和base_page.py中find_element()方法元素定位切割有关系，网上有些人写根据逗号切割或者等号切割，
    # 在实际使用xpath定位，发现单独逗号或者单独等号切割都不精确，造成元素定位失败

    news_link = "xpath=>//div[@id='s-top-left']/a[@href='http://news.baidu.com']"
    def type_search(self,text):
        self.type(self.input_box,text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)


    # 定义百度新闻入口
    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)


