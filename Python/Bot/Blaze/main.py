import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_binary

a = []
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()
driver.get("https://blaze.com/pt/games/crash")

time.sleep(5)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='crash-previous']"))
    )
except:
    pass

previous = driver.find_element(By.XPATH, "//div[@class='crash-previous']")
previous_values = previous.find_element(By.XPATH, "//div[@class='entries']")

span_list = previous_values.find_elements(By.TAG_NAME, "span")

for v in span_list:
    a.append(v.text)

driver.quit()
print(a[::-1])
