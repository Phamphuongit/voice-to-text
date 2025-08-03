from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

def click_element(element_path, wait, print_text: str):
    el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element_path)))
    el.click()
    print(print_text)

def get_text(element_path, wait):
    el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element_path)))
    return el.text