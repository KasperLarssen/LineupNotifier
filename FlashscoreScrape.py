from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

webdriver = './chromedriver.exe'

driver = Chrome(webdriver)

url = "http://flashscore.dk"
driver.get(url)
# time.sleep(1)
superliga_link = driver.find_element_by_link_text('Superliga')
superliga_link.click()
# time.sleep(1)
window_before = driver.window_handles[0]
match_link = driver.find_element_by_xpath("//div[@id='g_1_ERhak9L3']")
match_link.click()
# time.sleep(1)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
lineup_link = driver.find_element_by_link_text('Opstilling')
lineup_link.click()


