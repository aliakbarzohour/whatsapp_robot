# hey im aliakbar zohour welcome to my project 

# imports
from selenium import webdriver

# initing 
driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
# start coding 
name = input('Enter Name : ')
msg = input('Enter Masage : ')
count = int(input('How Many times ??? : '))

input('Enter Anything . . .')

# selenium 

# xpath relative
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
# massage box selection 
msg_box = driver.find_element_by_class_name('_13NKt ')
# loop for send massages 
for i in range(count):
    msg_box.send_keys(msg)
    btn = driver.find_elements_by_class_name('_4sWnG')
    btn.click()