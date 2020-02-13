import requests
from bs4 import BeautifulSoup
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as selenium_TimeoutException
from selenium.common.exceptions import StaleElementReferenceException as se_StaleElementReferenceException
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

driver.get(EBB_homepage_url)

driver.implicitly_wait(10)


# if popup window is on page, click 'dismiss'
if driver.find_element_by_xpath("//div[@class='jss10 jss36 jss11 jss120 jss121 jss124']"):
    print('popup window')
    driver.find_element_by_xpath("//button[@class='jss67 jss41 jss43 jss44 jss46 jss47 jss355']").click()

# check whether the filter pane is open or closed
if driver.find_element_by_xpath("//button[@class='jss67 jss106 jss109 bonuses2__OpenFilterFab-e8w5h-3 lahltg']"):
    driver.find_element_by_xpath("//button[@class='jss67 jss106 jss109 bonuses2__OpenFilterFab-e8w5h-3 lahltg']").click()

driver.find_element_by_xpath("//input[@id='downshift-multiple-input']").send_keys(state_input)
driver.find_element_by_xpath("//input[@id='downshift-multiple-input']").send_keys(Keys.RETURN)

# driver.find_element_by_xpath("//div[@id='select-']").click()
# driver.find_element_by_xpath(state_xpath).click()
# driver.find_element_by_xpath("//button[@class='jss67 jss41 jss52 jss54 jss55 jss57 jss65 Landing__FindBonusButton-sc-1u30fgc-12 gShgCR']").click()
# print(driver.find_element_by_xpath("//span[@class='jss749']").text())


soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup.prettify())





# driver.close()
