from time import sleep

from selenium.webdriver.common.by import By


class TestFileUpload:
    def test_file_upload(self, driver):
        driver.get("https://image.baidu.com")
        driver.find_element(By.XPATH, '//*[@id="sttb"]').click()
        driver.find_element(By.ID, 'stfile').send_keys(
            r'C:\Users\89174\PycharmProjects\Hogwarts_Moxxi\Datas\图片.jpg')
        sleep(5)
