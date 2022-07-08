from selenium import webdriver
from Drivers import Chrome_path
driver = webdriver.Chrome(executable_path = Chrome_path)
# url_link = "https://www.edmunds.com/mazda/cx-30/"
# url_link = "https://www.google.com/search?q={car}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"

url_link = "https://goocr.blogspot.com/?p=App&app=desktop&utm_source=OCRpro(github)-File&utm_medium=OcrproWeb&utm_campaign=redNewApp"
driver.get(url_link)
#Scroll to the end of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
xp = """//*[@id="home"]/div/div/div/div[1]/div[2]"""
imgResults = driver.find_elements_by_xpath(xp)
# imgResults = driver.find_elements_by_xpath("""//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img""")
totalResults=len(imgResults)
print(totalResults)
imgResults[0].click()

xp1 = """/html/body/div[3]/div[1]/a/span"""
idd = "goocrFileDragFile"
# s = driver.find_elements_by_id(idd)
s = driver.find_elements_by_xpath(xp1)
# s = driver.find_element_by_xpath(xp1)
#file path specified with send_keys
print(s)
s[0].send_keys(r"D:\PythonPC\WebAutomation\2.PNG")
# imgResults
