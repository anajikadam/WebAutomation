from selenium import webdriver
from Drivers import Chrome_path
driver = webdriver.Chrome(executable_path = Chrome_path)

url_link = "https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B089MQ622N/?_encoding=UTF8&pd_rd_w=v8v5Z&pf_rd_p=ebccae33-c8cf-48ef-bb6c-881f21a02fcb&pf_rd_r=XG81Y4VWXXZP6FKJM8CF&pd_rd_r=8f96a59e-cf91-46db-8c9b-a421ec43ec15&pd_rd_wg=KP3ZC&ref_=pd_gw_trq_rep_sims_gw"
driver.get(url_link)
# driver.save_screenshot('screenshot.png')
review_list = driver.find_elements_by_xpath("""//*[@id="R92X3ALK65GQG"]""")
# data = driver.find_elements_by_xpath("""/html/body/div[1]/div/main/div[4]/div/div[3]/div/div/section/div[2]/div/div[2]/div/div[1]/div/div[2]""")
# data = driver.find_elements_by_css_selector('div.user-title ml-0_5 ml-md-0_5 size-16 font-weight-medium d-inline')
print(review_list)
print(len(review_list))
details = []
# a = review_list[1:2]
# print(len(a))
for review in review_list:
    # print(review)
    review_title = review.find_elements_by_xpath("""//*[@id="customer_review-R29J5P8WG0JR84"]/div[2]/a[2]/span""")[0]
    title = review_title.text
    review_date = review.find_elements_by_xpath("""// *[ @ id = "customer_review-R29J5P8WG0JR84"] / span""")[0]
    date = review_date.text
    review_cust = review.find_elements_by_xpath("""//*[@id="customer_review-R31W27Y31QR1R1"]/div[4]""")[0]
    review = review_cust.text
    print(title)
    print(date)
    print(review)
driver.quit()
  # details.append(review_cust.text)
# print(details)
# searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
# searchbox.send_keys("ariyana garand")
# searchbuttom = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
# searchbuttom.click()
