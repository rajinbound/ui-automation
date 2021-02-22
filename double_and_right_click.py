
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe") #provide path of the chrome driver

##perfoirming double click
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver) #create

double_click_element = driver.find_element_by_id("double-click")

#action.context_click(double_click_element).perform() #right click
action.double_click(double_click_element).perform()

##jave alert

alert = driver.switch_to.alert
print(alert.text)
assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()

driver.close()

