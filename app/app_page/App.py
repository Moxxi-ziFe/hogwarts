"""
App.py 模块， 存放app相关操作
eg. 启动应用， 重启应用， 停止应用， 进入到首页
"""
import yaml
from appium import webdriver

from app.app_page.Base_page import BasePage
from app.app_page.Main_page import MainPage

with open('../config_datas/caps.yml') as datas:
    my_config = yaml.safe_load(datas)
    caps = my_config["desirecaps"]
    ip = my_config["server"]["ip"]
    port = my_config["server"]["port"]


class App(BasePage):
    def start(self):
        #  启动app
        if not self.driver:
            # desire_cap = {
            #     "platformName": "android",
            #     "deviceName": "127.0.0.1:7555",
            #     "appPackage": "com.tencent.wework",
            #     "appActivity": ".launch.LaunchSplashActivity",
            #     "noReset": "true",
            #     "skipDeviceInitialization": "true",
            #     "skipServerInitialization": "true"
            # }
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage(self.driver)
