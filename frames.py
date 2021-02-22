import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe") #provide path of the chrome driver
url = "https://the-internet.herokuapp.com/iframe" #set the URL
enter_text = "I am Raj and This is automation in iframe"
driver.get(url)

driver.maximize_window()
#frame id or frame name or index value can be use to switch
driver.switch_to.frame("mce_0_ifr")
#time.sleep(4) #global sleep

#clear the text in ifram which ever is present
driver.find_element_by_css_selector("#tinymce").clear()
#send the string to enter in iframe
driver.find_element_by_css_selector("#tinymce").send_keys(enter_text)
#get the entred text and validate
get_text = driver.find_element_by_css_selector("#tinymce").text

assert get_text == enter_text

driver.switch_to.default_content() #go back to parent as main html or exit the iframe

#get the text on the page to validate
h3tag_on_page = driver.find_element_by_tag_name("h3").text

#print(h3tag_on_page)

assert "An iFrame containing the TinyMCE WYSIWYG Editor" == h3tag_on_page

driver.close() #close the webdriver