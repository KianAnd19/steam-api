import steam_scraper
import json

data = steam_scraper.get_user_inventory("76561198279721485")
file_path = "test.json"
with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

#To get the price of an item
# Wait 3 seconds after each request to avoid ratelimits
#http://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=StatTrak%E2%84%A2 M4A1-S | Hyper Beast (Minimal Wear)