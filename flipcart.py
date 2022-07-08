from selenium import webdriver
from Drivers import Chrome_path

driver = webdriver.Chrome(executable_path = Chrome_path)
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
searchbox = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchbox.send_keys("samsung m21")
searchbuttom = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
searchbuttom.click()
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[1]/div/a[1]/img').click()
# nm = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
# print(type(nm))
# nm.click()
# for i in nm:
#     print(i.text)

