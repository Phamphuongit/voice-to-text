from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

def get_element(element_path, wait):
    el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element_path)))
    return el

def click_element(el, print_text: str):
    el.click()
    print(print_text)

def get_text(el, wait):
    # el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element_path)))
    return el.text