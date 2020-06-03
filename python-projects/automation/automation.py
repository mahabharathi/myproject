from selenium import webdriver
import time


chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


button_text= chrome_browser.find_elements_by_class_name('btn btn-default')
print(button_text)

assert('Show Message' in chrome_browser.page_source)

user_message= chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am extra cool')
show_message_button= chrome_browser.find_elements_by_class_name('btn btn-default')
show_message_button.click()
