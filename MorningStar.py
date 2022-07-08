import time
from os import path
from selenium import webdriver
from Drivers import Chrome_path


def fetch_morningstar():

   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--incognito")
   browser = webdriver.Chrome(executable_path=Chrome_path, options=chrome_options)
   print("Start Webpage Loading.................")
   browser.get("https://www.morningstar.ca/ca/report/etf/performance.aspx?t=0P0001HWR9&lang=en-CA")
   print("Webpage Loading Done.......")
   time.sleep(8)
   print("Fatching Details....")
   file_name = "ETF.csv"
   FileExist = 1
   if not path.exists(file_name):
      FileExist = 0
      print("File Not Exist.")
   f = open(file_name, "a", encoding="utf-8")
   if FileExist == 0:
      print("File Exist...")
      f.write("Date-Time,Price,Trend,Change $, Change %")

   prices = browser.find_elements_by_id("message-box-price")
   price = prices[0].text
   # print(price)
   PriceUp = browser.find_elements_by_xpath("""//*[@id="message-box-percentage"]/sup[1]""")

   priceTrend = "Down"
   if len(PriceUp) > 0:
      priceTrend = "Up"
   # print(priceTrend)
   changePriceNPercent = browser.find_elements_by_id("message-box-percentage")
   # print(changePriceNPercent)
   a = changePriceNPercent[0].text.replace("%", "")
   b = a.split("|")
   changePrice = b[0].strip()
   changePercent = b[1].strip()
   # print("changePrice,changePercent",changePrice,changePercent)
   ssDateTime = browser.find_elements_by_xpath("""//*[@id="sal-ii-report"]/div[1]/div[4]/sal-components/section/div/div/div[1]/sal-components-mip-quote/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/span[4]""")
   # print(ssDateTime)
   dts = ssDateTime[0].text
   dts = dts.replace("| Last Price updated as of ", "")
   dts = dts.replace(",", "")

   f.write("\n" + dts + "," + price + "," + priceTrend + "," + changePrice + "," + changePercent)

   print("price : " + price)
   print("priceTrend : " + priceTrend)
   print("changePrice : " + changePrice)
   print("changePercent : " + changePercent)
   print("dts : " + dts)
   f.close()


fetch_morningstar()
