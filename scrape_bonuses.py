import requests
from bs4 import BeautifulSoup
import logging
import re

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as selenium_TimeoutException
from selenium.common.exceptions import StaleElementReferenceException as se_StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException as se_NoSuchElementException
from selenium.webdriver.common.keys import Keys

EBB_homepage_url = "https://everybankbonus.com/bonuses"

DoC_bank_funding_page_url = ''

state_input = 'IL'
state_xpath = "//li[@data-value='{}']".format(state_input)

log = logging.getLogger(__name__)

try:
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
except Exception as e:
    log.exception("Error occurred when starting Selenium chrome webdriver")

driver.set_window_position(80, 0)
driver.set_window_size(1024, 768)

# driver.get(EBB_homepage_url)
#
# driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 10)
#
# # if popup window is on page, click 'dismiss'
# if driver.find_element_by_xpath("//div[@class='jss10 jss36 jss11 jss120 jss121 jss124']"):
#     print('popup window')
#     # driver.switch_to.alert.dismiss()
#     # TODO: Expected condition here to wait until the button element is visible
#     driver.implicitly_wait(10)
#     # wait.until(EC.presence_of_all_elements_located(By.XPATH, "//button[@class='jss67 jss41 jss43 jss44 jss46 jss47 jss355']"))
#     driver.find_element_by_xpath("//button[@class='jss67 jss41 jss43 jss44 jss46 jss47 jss355']").click()
#
# # check whether the filter pane is open or closed
# if driver.find_element_by_xpath("//button[@class='jss67 jss106 jss109 bonuses2__OpenFilterFab-e8w5h-3 lahltg']"):
#     driver.find_element_by_xpath("//button[@class='jss67 jss106 jss109 bonuses2__OpenFilterFab-e8w5h-3 lahltg']").click()
#
#
# # TODO: Use state URL path instead: "https://everybankbonus.com/bonuses?states={}".format(state)
# driver.find_element_by_xpath("//input[@id='downshift-multiple-input']").send_keys(state_input)
# driver.find_element_by_xpath("//input[@id='downshift-multiple-input']").send_keys(Keys.RETURN)
#
# driver.find_element_by_xpath("//button[@class='jss67 jss41 jss52 jss54 jss55 jss57 SideFilter__UpdateButton-sc-13omzq3-4 dcajYV']").click()

EBB_state_page = "https://everybankbonus.com/bonuses?states={}".format(state_input)
driver.get(EBB_state_page)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# if popup window is on page, click 'dismiss'
if driver.find_element_by_xpath("//div[@class='jss10 jss36 jss11 jss120 jss121 jss124']"):
    print('popup window')
    # driver.switch_to.alert.dismiss()
    # TODO: Expected condition here to wait until the button element is visible
    driver.implicitly_wait(10)
    # wait.until(EC.presence_of_all_elements_located(By.XPATH, "//button[@class='jss67 jss41 jss43 jss44 jss46 jss47 jss355']"))
    driver.find_element_by_xpath("//div[@class='jss10 jss36 jss11 jss120 jss121 jss124']/div[@class='jss354']/button[@class='jss67 jss41 jss43 jss44 jss46 jss47 jss355']").click()
    # driver.find_element_by_xpath("//span[@class='jss42']").click()

# Click 'More' until all bonuses are displayed on the page
total_showing_text = driver.find_element_by_xpath("//h6[@class='jss227 jss244 jss251 bonuses2__ShowingCountTypo-e8w5h-22 eqaqbT']").text
total_num_bonuses = int(re.search(r"(?:of\s*)(\d*)", total_showing_text).group(1))
showing_num_bonuses = int(re.search(r"(?:Showing\s*)(\d*)", total_showing_text).group(1))
num_more_clicks = round((total_num_bonuses - showing_num_bonuses)/10)
print('num_more_clicks', num_more_clicks)
for i in range(num_more_clicks):
    driver.find_element_by_xpath("//button[@class='jss67 jss41 jss52 jss54 jss55 jss57 bonuses2__MoreButton-e8w5h-21 dBqZTv']").click()

# print([i.text for i in driver.find_elements_by_css_selector('td')])

# for bonus in find_all_divs_under_"//div[@class='bonuses2__BonusesDiv-e8w5h-6 dMSxJl']":
#     click 'details': "//button[@class='jss67 jss41 jss49 BonusDetailDialogue__StyledButton-sc-1j8lk29-0 kpYlIk']"
#     scrape td.text under all tr elements
#     scrape bonus details


soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.prettify())




# driver.close()
