from selenium import webdriver

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

'''
for checkbox in checkboxes: #click on all the check box on the screen.
    checkbox.click()
'''

for checkbox in checkboxes: #click the option2
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_xpath("//input[@class='radioButton']")


'''
radiobuttons[2].click() #select option 3
radiobuttons[0].click() #select option 1
radiobuttons[1].click() #select option 2

'''
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()

#
#
#Handling Java Alerts
#
#
#
validatetext = "Raj"
driver.find_element_by_css_selector("#name").send_keys(validatetext)

driver.find_element_by_xpath("//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert validatetext in alerttext
alert.accept()

'''
driver.find_element_by_css_selector("#name").send_keys(validatetext)
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
alarT = alert.text
assert validatetext in alarT
alert.dismiss()
'''
