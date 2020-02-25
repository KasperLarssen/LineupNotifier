import time
import sys
from playsound import playsound
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

webdriver = './chromedriver.exe'
print("Først vælges en liga, f.eks. \"LaLiga\", \"Superliga\", \"Champions League\".")
print("Dernæst vælges et hold, f.eks. \"Real Madrid\", \"FC København\", \"Juventus\"")
league = input("Vælg en liga: ")
club = input('Vælg et hold fra denne liga: ')
driver = Chrome(webdriver)
url = "http://flashscore.dk"
driver.get(url)
# Click the specified league tab
time.sleep(2)
try:
    league_link = driver.find_element_by_link_text(league)
except NoSuchElementException:
    print("Den indtastede liga kunne ikke findes.")
    sys.exit()
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
    print("Det indtastede klubnavn kunne ikke findes. :'(")
    sys.exit()

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
