from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe") #provide path of the chrome driver
url = "https://the-internet.herokuapp.com/hovers" #set the URL
driver.get(url) #Open the page
driver.maximize_window() #maximise the window
action = ActionChains(driver) #create


menu= driver.find_element_by_xpath("//div[1]/img[1]")
action.move_to_element(menu).perform()
child_menu = driver.find_element_by_link_text("View profile").click()
driver.back()
h3_tag = driver.find_element_by_tag_name("h3").text

assert "Hovers" == h3_tag


driver.close()