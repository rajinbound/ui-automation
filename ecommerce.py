import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions, wait

list = []
list1 = []
driver = webdriver.Chrome(executable_path="browserfile/chromedriver.exe") #provide path of the chrome driver
url = "https://rahulshettyacademy.com/seleniumPractise/#/" #set the URL
driver.get(url) #get the url, or launch the URL

driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys("ber") #find the seach box on the home page and seach for Ber
time.sleep(4) #wait for four second

count = len(driver.find_elements_by_xpath("//div[@class='product']")) #calculate how many product is displayed as output of the given search

assert count ==3 #verify that total number if displayed result is three

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button") #select add to cart button for displayed product

for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text) #list all the product details into the list variable
    button.click() #add ll the displayed product into the cart

print(list) #print the list
driver.find_element_by_css_selector("img[alt='Cart']").click() #Open cart window
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click() #select the checkout
driver.implicitly_wait(5)# wait untill the page is going to be load
veggies = driver.find_elements_by_xpath("//p[@class='product-name']") #check the listed veggies in the check out page
for veg in veggies: #iterate through the vegitable
    list1.append(veg.text) #and list them into the list1
print(list1)
#assert list == list1 #validate the add to car item with item in the cart #this can be vrify that listed vegitable are the one which were selected

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

amounts = driver.find_elements_by_xpath("//td/tr[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text) #48+160+180

print (sum)

assert int(total) == sum

driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
countries = driver.find_element_by_xpath("//div[1]/div[1]/div[1]/div[1]/div[1]/select[1]").click()
driver.find_element_by_xpath("//option[contains(text(),'India')]").click()
driver.find_element_by_xpath("//input[@class='chkAgree']").click()
driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()
#Success_page = driver.find_elements_by_link_text("//a[contains(text(),'Home')]").text

#print(Success_page)


driver.close()




