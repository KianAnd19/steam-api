import requests
import json
import logging
import time
import urllib.parse
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def get_user_profile(username):
    user = {}
    URL = f"https://steamcommunity.com/id/{username}/"
    page = getRequest(URL)
    if (page == None): return None
    soup = BeautifulSoup(page.content, 'html.parser')

    ## Get user's profile name
    results = soup.find("span", {"class": "actual_persona_name"})
    user["profile_block"] = results.text


    ## Get user's real name
    results = soup.find("img", {"class": "profile_flag"})
    if (results != None):
        user["location"] = results.text
    else:
        user["location"] = None


    ## Get user's avatar
    results = soup.find("div", {"class": "profile_avatar_frame"})
    temp = results.find("img")
    user["avatar"] = temp["src"]


    ## Description
    results = soup.find("div", {"class": "profile_summary"})
    user["description"] = results.text


    ## Get user's level
    results = soup.find("span", {"class": "friendPlayerLevelNum"})
    user["level"] = int(results.text)


    ## Gets the number of user friends
    results = soup.find("div", {"class": "profile_friend_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["friends"] = int(temp.text)


    ## Gets the number of user badges
    results = soup.find("div", {"class": "profile_badges"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["badges"] = int(temp.text)


    ## Gets the number of user games
    results = soup.find("div", {"class": "profile_item_links"})
    temp = results.findAll("span", {"class": "profile_count_link_total"})
    user["games"] = int(temp[0].text)


    ## Gets the amount of screenhots
    user["screenshots"] = int(temp[2].text)


    ## Gets the amount of artwork
    user["artwork"] = int(temp[3].text)


    ## Gets the users recent games
    user["comments"] = 0
    results = soup.find("span", {"id": "commentthread_Profile_76561198301205885_totalcount"})
    if (results != None):
        user["comments"] = int(results.text)
        

    ## Recent activity time
    results = soup.find("div", {"class": "recentgame_quicklinks recentgame_recentplaytime"})
    if results != None: user["recent_activity"] = results.text.strip()


    ## Gets the number of user games
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["games_owned"] = int(temp.text)

    ## Gets the number of user groups
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["groups"] = int(temp.text)

    ## Gets the top level friends
    results = soup.find("div", {"class": "profile_topfriends profile_count_link_preview"})
    temp = soup.findAll("div", {"class": "friendBlock persona online"}) + soup.findAll("div", {"class": "friendBlock persona offline"}) + soup.findAll("div", {"class": "friendBlock persona in-game"})
    top_friends = []
    for friend in temp:
        friend_info = {}
        text = friend.find("div", {"class": "friendBlockContent"}).text.strip()
        match = re.search(r'\n', text)

        if match:
            result = text[:match.start()]
            friend_info["name"] = result


        friend_info["img"] = friend.find("img")["src"]
        friend_info["link"] = friend.find("a")["href"]
        friend_info["level"] = int(friend.find("span", {"class": "friendPlayerLevelNum"}).text)
        top_friends.append(friend_info)
    user["top_friends"] = top_friends

    ## Gets the primary group
    results = soup.find("div", {"class": "profile_group profile_primary_group"})
    primary_group = {}
    temp = results.find("a", {"class": "whiteLink"})
    primary_group["name"] = temp.text.strip()
    primary_group["url"] = results.find("a")["href"]
    primary_group["image_url"] = results.find("img")["src"]
    text = results.find("div", {"class": "profile_group_membercount"}).text
    # text = friend.find("div", {"class": "friendBlockContent"}).text.strip()
    match = re.search(r'\s', text)
    if match:
        result = text[:match.start()]
        primary_group["member_count"] = numerical(result)
    user["primary_group"] = primary_group

    
    ## Recent activity game
    results = soup.find("div", {"class": "recent_games"})
    temp = results.findAll("div", {"class": "recent_game"})
    recent_games = []

    for game in temp:
        game_info = {}
        game_info["name"] = game.find("div", {"class": "game_name"}).text
        game_info["img"] = game.find("img")["src"]
        game_info["link"] = game.find("a")["href"]
        game_info["achievements"] = game.find("span", {"class": "ellipsis"})
        if game_info["achievements"] != None:
            game_info["achievements"] = game_info["achievements"].text.strip()
        text = game.find("div", {"class": "game_info"}).text.strip()
        first_space_index = text.find(" ")

        if first_space_index != -1:
            result = text[:first_space_index]
            game_info["hours"] = numerical(result)
        else:
            game_info["hours"] = 0
        recent_games.append(game_info)        

    user["recent_games"] = recent_games

    return user


def get_user_inventory_cs(username):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        if username.isnumeric():
            url = f'https://steamcommunity.com/profiles/{username}/inventory/#730'
        else:
            url = f'https://steamcommunity.com/id/{username}/inventory/#730'
        driver.get(url)

        # Wait for the inventory items to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_link"))
        )

        items = []

        ## Gets to the last page of the inventory
        while True:
            driver.execute_script("InventoryNextPage();")
            try:
                next_page_button = driver.find_element(By.ID, "pagebtn_next")
                if "disabled" in next_page_button.get_attribute("class"):
                    break  # Break the loop if the button is disabled
            except NoSuchElementException:
                # If the button is not found, continue to the next iteration
                continue
            
        time.sleep(1)
        # Now using Selenium to find elements
        results = driver.find_elements(By.CLASS_NAME, "itemHolder")
        for item in results:
            try:
                item_temp = {}
                temp = item.find_element(By.CSS_SELECTOR, ".item.app730.context2")
                item_id = temp.get_attribute("id")
                item_image = temp.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
                if item_id:
                    if item_image in items:
                        items[item_id]["count"] = items[item_id]["count"] + 1
                    else:
                        item_temp["id"] = item_id
                        item_temp["image"] = item_image
                        item_temp["count"] = 1
                        items.append(item_temp)
                else:
                    print("Found element does not have an ID attribute")
            except NoSuchElementException:
                print("Specific element not found in this itemHolder")

        return items

###730_2_33548259976
###730_2_33550092843
    
def get_user_inventory(username):
    user = {}
    URL = f"http://steamcommunity.com/inventory/{username}/730/2?l=english&count=5000"
    page = getRequest(URL)
    if (page == None): return None

    items = {}
    #convert to json
    json_data = json.loads(page.text)

    inventory = json_data["assets"]
    descriptions = json_data["descriptions"]

    for item in inventory:
        classid = item["classid"]
        if classid in items:
            # Increase the count for this classid
            items[classid]["count"] += 1
        else:
            # Add a new entry for this classid
            items[classid] = {
                "classid": item["classid"],
                "instanceid": item["instanceid"],
                "count": 1}

    for item in descriptions:
        classid = item["classid"]
        if classid in items:
            items[classid]["name"] = item["market_name"]
            items[classid]["type"] = item["type"]
            items[classid]["image"] = f"https://community.akamai.steamstatic.com/economy/image/{item['icon_url']}"
            
            url = f"https://steamcommunity.com/market/listings/730/{item['market_hash_name']}"
            encoded_url = urllib.parse.quote(url, safe=':/')
            items[classid]["link"] = encoded_url
    
    return items


def get_user_inventory_value(filename):
    # Open and read the JSON file
    with open(filename, 'r') as file:
        inventory = json.load(file)

    prices = []

    # Iterate through the JSON data
    for item_id, item_details in inventory.items():
        item = {}
        item["name"] = item_details["name"]
        item["count"] = item_details["count"]

        URL = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=28&market_hash_name={item['name']}"
        page = getRequest(URL)
        if (page == None): return None
        json_data = json.loads(page.text)
        item["price"] = json_data["median_price"]
        prices.append(item)
        # print(f"Item ID: {item_id}")
        # print(f"Class ID: {item_details['classid']}")
        # print(f"Instance ID: {item_details['instanceid']}")
        # print(f"Count: {item_details['count']}")
        # print(f"Name: {item_details['name']}")
        # print(f"Type: {item_details['type']}")
        # print(f"Image URL: {item_details['image']}")
        # print(f"Link: {item_details['link']}")
        # print("----------")
        return prices

## Exponential backoff in case of 429 error
def getRequest(url, params=None):
    time_wait = 1
    while (True):
        if (params != None):
            response = requests.get(url, params=params)
        else:
            response = requests.get(url)

        if (response.status_code == 200):
            break

        if(response.status_code == 404):
            print("404 ERROR")
            return None

        time_wait = time_wait * 2
        print(f"WAITING: {time_wait} seconds")
        time.sleep(time_wait)

    return response


## Convert scraped text to numerical value
def numerical(text):
    if re.search(r',', text):
        text = text.replace(',', '')
        return int(text)
    elif re.search(r'.', text):
        return float(text)
    else:
        return int(text)