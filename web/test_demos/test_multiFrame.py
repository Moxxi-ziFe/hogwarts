from selenium.webdriver.common.by import By


class TestMultiFrame:
    def test_frame(self, driver):
        driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        driver.switch_to.frame('iframeResult')
        print(driver.find_element(By.ID, 'draggable').text)
        driver.switch_to.default_content()
        # driver.switch_to.parent_frame()
        print(driver.find_element(By.ID, 'submitBTN').text)
