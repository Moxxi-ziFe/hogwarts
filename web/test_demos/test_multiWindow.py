import time

# from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMultiWindow:
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(2)

    def test_window(self, driver):
        driver.get("https://baidu.com/")
        driver.find_element(By.XPATH, '//*[@id="u1"]/a').click()
        # print(setup.current_window_handle)
        driver.find_element(By.CSS_SELECTOR,
                            '#passport-login-pop-dialog > div > div > div > div.tang-pass-footerBar > a').click()
        # print(setup.current_window_handle)
        # print(setup.window_handles)
        driver.switch_to_window(driver.window_handles[-1])
        # print(setup.current_window_handle)
        driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("username")
        driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("17800000000")
        driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys("password")
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()
        driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('username')
        driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('password')
        driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()
        time.sleep(5)
