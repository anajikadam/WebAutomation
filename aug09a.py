
from selenium import webdriver
from Drivers import Chrome_path
driver = webdriver.Chrome(executable_path = Chrome_path)

# driver = webdriver.Chrome()
def upload():

	url_link = "https://goocr.blogspot.com/?p=App&app=desktop&utm_source=OCRpro(github)-File&utm_medium=OcrproWeb&utm_campaign=redNewApp"
	driver.get(url_link)
	xp = """//*[@id="home"]/div/div/div/div[1]/div[2]"""
	imgResults = driver.find_elements_by_xpath(xp)
	imgResults[0].click()
	xp1 = """//*[@id="upload-photo"]"""
	driver.switch_to.frame(xp1)
	driver.find_element_by_name('image').send_keys("2.PNG")

if __name__ == '__main__':
    upload()
    driver.quit()