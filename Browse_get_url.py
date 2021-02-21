from selenium import webdriver


driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe")
#driver = webdriver.Firefox(executable_path="browserfile/geckodriver.exe")
driver.maximize_window()
#driver.get("https://www.google.com")
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
#driver.get("http://172.18.246.86/labs/#/")
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.back() #go back to previous page
driver.refresh()#refresh the page
#Locator: ID,Name, Class, XPATH, CSS, ClassName,linkText

driver.find_element_by_name("name")

driver.close()

