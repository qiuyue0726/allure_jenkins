import allure
from selenium import webdriver
class Test_001:

    def setup_class(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://www.baidu.com')


    @allure.step('第二步')
    def test_001(self):
        print('123456')

    @allure.step('第一步')
    def test_002(self):
        self.test_001()
        allure.attach(self.driver.get_screenshot_as_png(),'截图',allure.attachment_type.PNG)
        print('\n test_001')
