from appium.webdriver.common.mobileby import MobileBy

from frame.frame_demo.Base_page import BasePage
from frame.frame_demo.Search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return SearchPage(self.driver)
