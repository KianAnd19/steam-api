import requests
import json
import logging
import time
from bs4 import BeautifulSoup
import re


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


    ## Gets the number of user games
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["games_owned"] = int(temp.text)

    ## Gets the number of user groups
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["groups"] = int(temp.text)

    results = soup.find("div", {"class": "profile_group profile_primary_group"})
    primary_group = {}
    temp = results.find("a", {"class": "whiteLink"})
    primary_group["name"] = temp.text.strip()
    primary_group["url"] = results.find("a")["href"]
    primary_group["image_url"] = results.find("img")["src"]
    primary_group["member_count"] = results.find("div", {"class": "profile_group_membercount"}).text
    user["primary_group"] = primary_group

    


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
    user["recent_activity"] = results.text.strip()


    ## Recent activity game
    results = soup.find("div", {"class": "recent_games"})
    temp = results.findAll("div", {"class": "recent_game"})
    recent_games = []

    for game in temp:
        game_info = {}
        game_info["name"] = game.find("div", {"class": "game_name"}).text
        game_info["img"] = game.find("img")["src"]
        game_info["link"] = game.find("a")["href"]
        game_info["achievements"] = game.find("span", {"class": "ellipsis"}).text.strip()
        text = game.find("div", {"class": "game_info"}).text.strip()
        first_space_index = text.find(" ")

        if first_space_index != -1:
            result = text[:first_space_index]
            game_info["hours"] = (result)
        else:
            game_info["hours"] = 0
        recent_games.append(game_info)        

    user["recent_games"] = recent_games



    

    return user




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



# print(get_user_profile("grandpasaurus"))