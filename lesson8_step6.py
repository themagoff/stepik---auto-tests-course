from selenium import webdriver
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

input = browser.find_element_by_tag_name("button")
input.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

value = browser.find_element_by_id("input_value").text
result = calc(value)

input2 = browser.find_element_by_id("answer")
input2.send_keys(result)

input3 = browser.find_element_by_tag_name("button")
input3.click()
