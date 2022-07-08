from selenium import webdriver
from Drivers import Chrome_path
driver = webdriver.Chrome(executable_path = Chrome_path)
url_link = "https://www.edmunds.com/mazda/cx-30/"
driver.get(url_link)

# data = driver.find_elements_by_xpath("""/html/body/div[1]/div/main/div[4]/div/div[3]/div/div/section/div[2]/div/div[2]/div/div[1]/div/div[2]""")
data = driver.find_elements_by_css_selector('div.user-title ml-0_5 ml-md-0_5 size-16 font-weight-medium d-inline')
totalResults=len(data)
print(totalResults)
# data[0].click()
# actual_image = driver.find_elements_by_css_selector('img.n3VNCb')
# alt = actual_image[0].get_attribute('alt')
# print(alt)
# src = actual_image[0].get_attribute('src')
# print(src)
# userid_element = driver.find_elements_by_xpath('/html/body/div[1]/div/main/div[4]/div/div[3]/div/div/section/div[2]/div/div[1]/div/div[1]/div/div[2]')
# print(userid_element)
# print(type(userid_element))
# userid = userid_element.text
#
# userid
# driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
# searchbox = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
# searchbox.send_keys("samsung m21")
# searchbuttom = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
# searchbuttom.click()
# driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[1]/div/a[1]/img').click()
# nm = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
# print(type(nm))
# nm.click()
# for i in nm:
#     print(i.text)

