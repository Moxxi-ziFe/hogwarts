from appium.webdriver.common.mobileby import MobileBy

from frame.frame_demo.Base_page import BasePage
from frame.frame_demo.Market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        # 制造弹窗
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        #
        # self.find(MobileBy.XPATH, "//*[@text='行情' and @resource-id='com.xueqiu.android:id/tab_name']").click()
        self.parse_yaml("./main.yml", "goto_market")
        return MarketPage(self.driver)
