import steam_scraper
import json

data = steam_scraper.get_user_inventory_value("test/test.json")
file_path = "test/test2.json"
with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

#To get the price of an item
# Wait 3 seconds after each request to avoid ratelimits
#https://steamcommunity.com/market/priceoverview/?appid=730&currency=28&market_hash_name=StatTrak™%20M4A1-S%20|%20Hyper%20Beast%20(Minimal%20Wear)