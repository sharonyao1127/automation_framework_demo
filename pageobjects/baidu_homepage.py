from framework.base_page import BasePage

class HomePage(BasePage):
    input_box = "id => kw"
    search_submit_btn = "xpath=>//*[@id = 'su']"
    #元素定位写法，=>和base_page.py中find_element()方法元素定位切割有关系，网上有些人写根据逗号切割或者等号切割，
    # 在实际使用xpath定位，发现单独逗号或者单独等号切割都不精确，造成元素定位失败

    def type_search(self,text):
        self.type(self.input_box,text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)