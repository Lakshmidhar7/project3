from Pageactions.commonfunctions import AutoFunctions
from pageobjects.Automationobjects import AutomationCheck
import time
import yaml
from selenium.webdriver.common.by import By


with open('../Testdata/auto_mate.yaml', 'r')as file:
    auto_mate = yaml.full_load(file)

cfunctions = AutoFunctions()
g_functions = AutomationCheck()

cfunctions.open_url('https://testautomationpractice.blogspot.com/?m=1')
cfunctions.maximize()
time.sleep(5)
cfunctions.click_on_pro(g_functions.right_inner)
cfunctions.browser.find_element(By.XPATH, g_functions.field_xpath).clear()
cfunctions.input_select_on_input(g_functions.field_xpath, auto_mate['field1'])
txt_box = cfunctions.browser.find_element(By.XPATH, g_functions.click_xpath)
cfunctions.double_click(txt_box)
time.sleep(2)
source_drag = cfunctions.browser.find_element(By.XPATH, g_functions.drag_xpath)
target_drop = cfunctions.browser.find_element(By.XPATH, g_functions.drop_xpath)
cfunctions.click_hold_move(source_drag, target_drop)
time.sleep(4)
source_img = cfunctions.browser.find_element(By.XPATH, g_functions.mary_xpath)
target_img = cfunctions.browser.find_element(By.XPATH, g_functions.trash_xpath)
cfunctions.drag_and_drop(source_img, target_img)
time.sleep(3)
slider_ele = cfunctions.browser.find_element(By.XPATH, g_functions.slider_xpath)
cfunctions.slider_element(slider_ele, 120, 0)
time.sleep(4)
resizeable_ele = cfunctions.browser.find_element(By.XPATH, g_functions.resizable_xpath)
cfunctions.scrollDown()
cfunctions.scrollDown()
cfunctions.move_element(resizeable_ele, 50, 5)
time.sleep(5)
cfunctions.input_select_on_input(g_functions.age_xpath, auto_mate['age'])
time.sleep(5)
cfunctions.browser.close()

