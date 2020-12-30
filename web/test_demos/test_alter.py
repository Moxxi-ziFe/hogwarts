from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlter:
    def test_alter(self, driver):
        driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        driver.switch_to.frame('iframeResult')
        element_drag = driver.find_element(By.ID, 'draggable')
        element_drop = driver.find_element(By.ID, 'droppable')
        action = ActionChains(driver)
        action.click_and_hold(element_drag).move_to_element(element_drop).release(element_drag).perform()
        driver.switch_to.alert.accept()
        driver.switch_to.default_content()
        driver.find_element(By.ID, 'submitBTN').click()
        sleep(5)
