from selenium import webdriver


class TestH5:
    def test_h5(self):
        driver = webdriver.Chrome()
        driver.get("https://ceshiren.com/")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
