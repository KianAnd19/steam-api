import steam_scraper
import json

data = steam_scraper.get_user_profile("grandpasaurus")
file_path = "test.json"
with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)


