from Pageactions.commonfunctions import AutoFunctions
from pageobjects.Automationobjects import AutomationCheck
import time
import yaml
#from pageobjects.Automationobjects import AdvancedEvents, SearchEvents, DropdownEvents
from selenium.webdriver.common.by import By

with open('../Testdata/auto_mate.yaml', 'r')as file:
    auto_mate = yaml.full_load(file)


cfunctions = AutoFunctions()
g_functions = AutomationCheck()

cfunctions.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunctions.maximize()
time.sleep(5)
cfunctions.input_select_on_input(g_functions.wickey_xpath, auto_mate['serchstr'])
cfunctions.click_on_pro(g_functions.search_xpath)
cfunctions.click_on_pro(g_functions.alert_xpath)
cfunctions.alerts_browser()
cfunctions.click_on_pro(g_functions.datepic_xpath)
cfunctions.click_on_pro(g_functions.month_xpath)
cfunctions.input_select_on_input(g_functions.speed_xpath, auto_mate['speed'])
cfunctions.input_select_on_input(g_functions.file_xpath, auto_mate['file'])
cfunctions.input_select_on_input(g_functions.sec_no_xpath, auto_mate['number'])
cfunctions.input_select_on_input(g_functions.sec_product_xpath, auto_mate['product'])
cfunctions.input_select_on_input(g_functions.sec_animal_xpath, auto_mate['animal'])
time.sleep(3)
cfunctions.switch_to_frame(g_functions.frame_xpath)
cfunctions.input_select_on_input(g_functions.first_name_xpath, auto_mate['firstname'])
cfunctions.input_select_on_input(g_functions.last_name_xpath, auto_mate['lastname'])
cfunctions.input_select_on_input(g_functions.phoneno_xpath, auto_mate['phoneNo'])
cfunctions.input_select_on_input(g_functions.country_xpath, auto_mate['country'])
cfunctions.input_select_on_input(g_functions.city_xpath, auto_mate['city'])
cfunctions.input_select_on_input(g_functions.email_xpath, auto_mate['email'])
time.sleep(2)
cfunctions.click_on_pro(g_functions.gender_xpath)
cfunctions.click_on_pro(g_functions.date_xpath)
cfunctions.click_on_pro(g_functions.best_time_xpath)
# time.sleep(3)
# cfunctions.click_on_pro(g_functions.right_inner)
# cfunctions.browser.find_element(By.XPATH, g_functions.field_xpath).clear()
# cfunctions.browser.find_element(g_functions.field_xpath, auto_mate['field1'])
# txt_box = cfunctions.browser.find_element(g_functions.click_xpath)
# cfunctions.double_click(txt_box)
