from autoscraper import AutoScraper


url = 'https://www.ebay.com/sch/i.html?_nkw=iphone'
wanted_list = ['Apple iPhone 8 64GB Factory Unlocked AT&T T-Mobile Gray Smartphone', '$41.99', 'https://www.ebay.com/itm/Apple-iPhone-8-64GB-Factory-Unlocked-AT-T-T-Mobile-Gray-Smartphone/265080584595?hash=item3db808b993:g:iyAAAOSwrAFgRY38']

scraper = AutoScraper()
result = scraper.build(url=url, wanted_list=wanted_list)
scraper.get_result_similar(url, grouped=True)
scraper.set_rule_aliases({'rule_0aok': 'title', 'rule_vn5z': 'price', 'rule_buz1': 'url'})

scraper.keep_rules(['rule_0aok', 'rule_vn5z', 'rule_buz1'])

scraper.save('ebay-search')

