import time
from playsound import playsound
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

webdriver = './chromedriver.exe'

driver = Chrome(webdriver)

url = "http://flashscore.dk"
driver.get(url)
# Click the specified league tab
league = 'Europa League'
# league = 'Superliga'
# fck - celtic id : g_1_Khu1qDqN
# fcn - horsens id : g_1_ERhak9L3
time.sleep(2)
league_link = driver.find_element_by_link_text(league)
league_link.click()
# click the match with the specified id
time.sleep(2)
window_before = driver.window_handles[0]
match_link = driver.find_element_by_xpath("//div[@id='g_1_Khu1qDqN']")
match_link.click()
# click the lineup fan, if present. Otherwise try again in 5 seconds.
time.sleep(2)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)



def scanForLineup():
    try:
        print("Scanning for lineups...")
        lineup_link = driver.find_element_by_link_text('Opstilling')
        lineup_link.click()
        playsound('ready.mp3')
        print("success!")
    except NoSuchElementException:
        time.sleep(5)
        scanForLineup()

scanForLineup()

print("done!")
