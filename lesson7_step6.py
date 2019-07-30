from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

value = browser.find_element_by_id("input_value").text
result = calc(value)
print (result)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

input1 = browser.find_element_by_id("answer")
input1.send_keys(result)
input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
input3 = browser.find_element_by_id("robotsRule")
input3.click()

button.click()
