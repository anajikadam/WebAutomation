from selenium import webdriver
from Drivers import Chrome_path

driver = webdriver.Chrome(executable_path = Chrome_path)
driver.get("https://www.google.co.in/")
searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys("ariyana garand")
searchbuttom = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
searchbuttom.click()
driver.save_screenshot('screenshot.png')

