from selenium import webdriver
from Drivers import Chrome_path
driver = webdriver.Chrome(executable_path = Chrome_path)
# url_link = "https://www.edmunds.com/mazda/cx-30/"
url_link = "https://www.google.com/search?q={car}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
driver.get(url_link)
#Scroll to the end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
imgResults = driver.find_elements_by_xpath("""//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img""")
totalResults=len(imgResults)
print(totalResults)
imgResults[0].click()
actual_image = driver.find_elements_by_css_selector('img.n3VNCb')
alt = actual_image[0].get_attribute('alt')
print(alt)
src = actual_image[0].get_attribute('src')
print(src)
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

