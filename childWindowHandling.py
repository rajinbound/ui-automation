from selenium import webdriver

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe") #provide path of the chrome driver
url = "https://the-internet.herokuapp.com/" #set the URL
driver.get(url) #get the url and open the url in browser
driver.maximize_window() #maximise the window

#click the link by text "Multiple window"
driver.find_element_by_link_text("Multiple Windows").click()
#click the link by text "Click Here", new tab will be open
driver.find_element_by_link_text("Click Here").click()
#all new tab windows are store into list so [1] is the very next tab
#in this case only one tab is open so [0] will present the parent window and [1] will present childwindow
childWindow = driver.window_handles[1]
#selenium webdriver is switch to child window
driver.switch_to.window(childWindow)

#grab and print the h3 tag from child window
child_text = (driver.find_element_by_tag_name("h3").text)

assert "New Window" == child_text
driver.close() #close child

#coming back to parent window
driver.switch_to.window(driver.window_handles[0])
#grab and print the h3 tag of the parent window
final_page = (driver.find_element_by_tag_name("h3").text)

#validation of the tag
assert "Opening a new window" == final_page

driver.close()

