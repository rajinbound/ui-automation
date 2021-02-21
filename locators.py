from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Raj")
driver.find_element_by_name("email").send_keys("rax@dxxx.com")
#driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("exampleCheck1").click() #find by ID and click on the check box

'''
Customised CSS Syntax
tagname[attribute="value"] --tag name is optional
Reg EX:[attribute*value]

Customised Xpath syntax:
//tagname[@attribute=value]--Tagname optional 
reg Ex: [contains(@attribute, "Value")]

Generate CSS from ID:
tagname#ID -Tagname optional

Genwratting CSS from ClassName

'''
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value() only if the value is defined in html
driver.find_element_by_xpath("//input[@type='submit']").click()

driver.find_element_by_class_name("alert-success").text

message = (driver.find_element_by_css_selector("[class*='alert-success']").text)


assert "Success" in message
#driver.implicitly_wait(10)
driver.close()

