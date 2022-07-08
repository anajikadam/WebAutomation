from selenium import webdriver
from Drivers import Chrome_path

driver = webdriver.Chrome(executable_path = Chrome_path)

youtube = "https://www.youtube.com/"
driver.get(youtube)
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys("ariyana garand")
searchbuttom = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbuttom.click()

