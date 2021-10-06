# hey im aliakbar zohour welcome to my project 

# imports
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore,init

# initing 
init()
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
# start coding 
name = input(Fore.YELLOW+' [*] '+Fore.WHITE+'Enter Name : ')
msg = input(Fore.YELLOW+' [*] '+Fore.WHITE+'Enter Masage : ')
count = int(input(Fore.GREEN+' [?] '+Fore.WHITE+'How Many times ??? : '))

input(Fore.RED+' [~] '+Fore.WHITE+'Enter Anything . . .')
# selenium 
# xpath relative
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
# massage box selection 
msg_box = driver.find_element_by_class_name('_13NKt')
# loop for send massages 
for i in range(count):
    msg_box.send_keys(msg)
    btn = driver.find_elements_by_class_name('_4sWnG')
    btn.click()