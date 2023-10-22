import requests
import json
import logging
import time
from bs4 import BeautifulSoup


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


    ## Gets the number of user games
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["games_owned"] = int(temp.text)

    ## Gets the number of user groups
    results = soup.find("div", {"class": "profile_group_links profile_count_link_preview_ctn responsive_groupfriends_element"})
    temp = results.find("span", {"class": "profile_count_link_total"})
    user["groups"] = int(temp.text)


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



print(get_user_profile("grandpasaurus"))