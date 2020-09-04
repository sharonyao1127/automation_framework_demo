
import unittest
import testsuites
from testsuites.test_baidu_search import BaiduSearch
from testsuites.test_get_page_title import GetPageTitle
import HTMLTestRunner
import os
import time


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
# python3 用open
fp = open(HtmlFile,'wb')
# fp = file(HtmlFile, "wb")


# 构建suite
# 1、加载测试用例到suite中去，但缺点是用例多的时候，需要一个一个手动添加
# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch('test_search2'))
# suite.addTest(GetPageTitle('test_get_title'))

# 2、一次性加载一个类文件下所有测试用例到suite中去
# makeSuite()虽然比上面的addTest()有一定效率提升，但实际的项目脚本不可能都在一个测试类文件中，可以去unittest看看其他方法
# suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))

# 3、利用discover（）方法去加载一个路径下所有的测试用例
# testsuites是可以包名，也可以是一个文件夹名称，在实际脚本开发过程中，最后都采用这个方法来批量管理和执行几百上千的测试用例。
suite = unittest.TestLoader().discover('testsuites')



if __name__ == '__main__':
    # # 执行用例
    # runner = unittest.TextTestRunner()

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    # 注意HTMLTestRunner.py的版本，放在python安装目录下的Lib下即可
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"某某项目测试报告",description = u"用例测试情况",verbosity=2)
    # 开始执行测试套件
    runner.run(suite)
