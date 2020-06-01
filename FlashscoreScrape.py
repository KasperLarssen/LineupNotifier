import time
import sys
from playsound import playsound
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

webdriver = './chromedriver.exe'
league = input('Vælg en liga: ')
club = input('Vælg et hold: ')
driver = Chrome(webdriver)
url = "http://flashscore.dk"
driver.get(url)
# driver.minimize_window()
# Click the specified league tab
time.sleep(2)
league_link = driver.find_element_by_link_text(league)
league_link.click()
# click the match with the specified id
time.sleep(2)
window_before = driver.window_handles[0]
match_links = driver.find_elements_by_xpath("//*[contains(@id, 'g_1_')]")
clubfound = False
for x in match_links:
    if club in x.text:
        x.click()
        clubfound = True
        break
if(not clubfound):
    print("Det indtastede klubnavn kunne ikke findes. Prøv igen")
    sys.exit()


# click the lineup fan, if present. Otherwise try again in 5 seconds.
time.sleep(2)
#window_after = driver.window_handles[1]
#driver.switch_to_window(window_after)

def scanForLineup():
    try:
        print("Scanning for lineups...")
        #doesn't work right now. cant find the Opstilling
        lineup_link = driver.find_element_by_link_text('Opstilling')
        # lineup_link = driver.find_element_by_xpath("*//*[contains(text(),'Opstilling')]")


        lineup_link.click()
        playsound('ready.mp3')
        print("success!")
    except NoSuchElementException:
        time.sleep(5)
        scanForLineup()


scanForLineup()

print("done!")
