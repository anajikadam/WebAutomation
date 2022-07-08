# https://betterprogramming.pub/introducing-autoscraper-a-smart-fast-and-lightweight-web-scraper-for-python-20987f52c749


from autoscraper import AutoScraper
url = 'https://finance.yahoo.com/quote/AAPL/'
wanted_list = ["121.42"]
scraper = AutoScraper()
# Here we can also pass html content via the html parameter instead of the url (html=html_content)
result = scraper.build(url, wanted_list)
print(result)

result = scraper.build(url, wanted_list)

print(result)
op = scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/')
print(op)
