import selenium
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import _find_element


class text_to_change(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = _find_element(driver, self.locator).text
        return actual_text != self.text

driver = webdriver.Firefox()
driver.get("file:///Users/stephenwebel1/Desktop/workspace/contact-generator/project/index.html")

element = driver.find_element_by_id("size")
element.send_keys("5000",Keys.ENTER)
output = driver.find_element_by_id("output")

WebDriverWait(driver, 10).until(
	text_to_change((By.ID, "output"), output.text)
)

print(output.text)
userJsonAr = json.loads(output.text)
for user in userJsonAr['results']:
	print(user)

# clean up
element.clear()
driver.close()
