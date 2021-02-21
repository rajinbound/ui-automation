import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions, wait

list = []
list1 = []
driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe")
url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver.get(url)

driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='product']"))

assert count ==3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button") #select add to card locator

for button in buttons:
    #//div[@class='product-action']/button/parent::div/parent::div/h4 path of the item name
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click() #select all the add to card button
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.implicitly_wait(5)
veggies = driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in veggies:
    list1.append(veg.text)
print(list1)
#assert list == list1 #validate the add to car item with item in the cart

total = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click() #click on apply button
time.sleep(5) #explicit wait can be also used
#wait.until(expected_conditions.presence_of_element_located((by.CSS_SELECTOR, "span.promoInfo")))
#driver.find_element_by_xpath()

Discounted_total = driver.find_element_by_css_selector(".discountAmt").text
print(total, Discounted_total)
assert float(Discounted_total) < int(total)


#print(driver.find_element_by_xpath("//span[@class='promoInfo']").get_attribute())

driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
countries = driver.find_element_by_xpath("//div[1]/div[1]/div[1]/div[1]/div[1]/select[1]").click()
driver.find_element_by_xpath("//option[contains(text(),'India')]").click()
driver.find_element_by_xpath("//input[@class='chkAgree']").click()
driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()
#Success_page = driver.find_elements_by_link_text("//a[contains(text(),'Home')]").text

#print(Success_page)


driver.close()




