from selenium import webdriver
from Drivers import Chrome_path
import time
import pandas as pd
driver = webdriver.Chrome(executable_path = Chrome_path)
url_link = "https://www.indeed.com/q-data-scientist-jobs.html"
driver.get(url_link)
time.sleep(5)
job_details = []
job_list = driver.find_elements_by_xpath("//div[@data-tn-component='organicJob']")
# data = driver.find_elements_by_xpath("""/html/body/div[1]/div/main/div[4]/div/div[3]/div/div/section/div[2]/div/div[2]/div/div[1]/div/div[2]""")
# data = driver.find_elements_by_css_selector('div.user-title ml-0_5 ml-md-0_5 size-16 font-weight-medium d-inline')

totalResults=len(job_list)
print(totalResults)
for each_job in job_list:
    # Getting job info //*[@id="jl_3dde0133818987f0"]
    job_title = each_job.find_elements_by_xpath(".//h2[@class='title']/a")[0]
    job_company = each_job.find_elements_by_xpath(".//span[@class='company']")[0]
    job_location = each_job.find_elements_by_xpath(".//span[@class='location accessible-contrast-color-location']")[0]
    job_summary = each_job.find_elements_by_xpath(".//div[@class='summary']")[0]
    job_publish_date = each_job.find_elements_by_xpath(".//span[@class='date ']")[0]
    # Saving job info
    job_info = [job_title.text, job_company.text, job_location.text, job_summary.text, job_publish_date.text]
    # Saving into job_details
    job_details.append(job_info)
driver.quit()
job_details_df = pd.DataFrame(job_details)
job_details_df.columns = ['title', 'company', 'location', 'summary', 'publish_date']
job_details_df.to_csv('job_details.csv', index=False)
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

