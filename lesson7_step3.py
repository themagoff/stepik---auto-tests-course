from selenium import webdriver
from selenium.webdriver.support.ui import Select



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)
sum_int = num1 + num2
sum_str = str(sum_int)
dropdown = Select(browser.find_element_by_id("dropdown"))
dropdown.select_by_value(sum_str) 
submit = browser.find_element_by_css_selector(".btn.btn-default")
submit.click()
