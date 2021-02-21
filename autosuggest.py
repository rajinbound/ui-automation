from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries: #iterate through all the posisble matching
    if country.text == "India": # if matches India from the drop down
        country.click()
        break

#print(driver.find_element_by_id("autosuggest").get_attribute('value'))

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

driver.close()