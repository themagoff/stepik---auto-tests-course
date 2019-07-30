from selenium import webdriver
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("123")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("123")
input3 = browser.find_element_by_name("email")
input3.send_keys("123")

input4 = browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')
input4.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()
