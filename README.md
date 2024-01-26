# Steam User Profile Scraper

A Python script and Flask web application for scraping and displaying Steam user profiles.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
<!-- - [Usage](#usage)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license) -->

## Introduction

The Steam User Profile Scraper is a Python project that allows you to retrieve and display information from Steam user profiles. It uses web scraping techniques to extract data from the Steam Community website.

## Features

- Retrieve various details from a Steam user profile:
  - Profile name
  - Real name
  - Location
  - Avatar
  - Description
  - User level
  - Friends count
  - Badges count
  - Games owned count
  - Screenshots count
  - Artwork count
  - Comments count
  - Recent activity
  - Games owned
  - Groups count
  - Top friends
  - Primary group
  - Recent games

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Flask
- BeautifulSoup (bs4)
- requests

You can install the required Python packages using pip:

`pip install Flask beautifulsoup4 requests`

or

`pip install -r requirements.txt`


### Installation

1. Clone the repository to your local machine:

`git clone git@github.com:KianAnd19/steam-api.git`

2. Switch to the project directory

`cd steam-profile-scraper`

3. Run the Flash web application:

`python3 steam_api.py`

## Routes

1. Get a users profile

`http://127.0.0.1:5000/user/<id>`


## Example Output
The following is the output given when my own steam profile is requested
```
{
    "profile_block": "Grandpasaurus",
    "location": "",
    "avatar": "https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/items/1098340/71f42ec23a7f80c365f0c3900a6e61bdc78733d7.png",
    "description": "\r\n\t\t\t\t\t\t\t\tVery important Grandpasaurus Lore: https://kianand19.github.io/Grandpasaurus/ Was Silver Elite until started playing with SneakyMaens XD\u279c Silver 1 : \u2714 \u279c Silver 2 : \u2714 (Current rank)\u279c Silver 3 : \u2714 \u279c Silver 4 : \u2714 \u279c Silver Elite : \u2714 \u279c Silver Elite Master : \u2716\u279c Gold Nova 1 :  \u2716\u279c Gold Nova 2 : \u2716\u279c Gold Nova 3 :  \u2716\u279c Gold Nova Master :  \u2716\u279c Master Guardian 1 :  \u2716\u279c Master Guardian 2 : \u2716\u279c Master Guardian Elite :  \u2716\u279c Distinguished Master Guardian :  \u2716\u279c Legendary Eagle : \u2716\u279c Legendary Eagle Master : \u2716\u279c Supreme Master First Class : \u2716 \u279c The Global Elite : \u2716\t\t\t\t\t\t\t",
    "level": 39,
    "friends": 86,
    "badges": 15,
    "games": 27,
    "screenshots": 3,
    "artwork": 7,
    "comments": 12,
    "games_owned": 2,
    "groups": 2,
    "top_friends": [
        {
            "name": "Noncelores Cumbridge",
            "img": "https://avatars.cloudflare.steamstatic.com/b1fd6d2a128e673b21e453c4baa528c863650394_medium.jpg",
            "link": "https://steamcommunity.com/profiles/76561198279721485",
            "level": 92
        },
        {
            "name": "Sol",
            "img": "https://avatars.cloudflare.steamstatic.com/1b40dc2a0a904f1f032edffa90595f5115e2dc1b_medium.jpg",
            "link": "https://steamcommunity.com/id/_NN_",
            "level": 92
        },
        {
            "name": "fire",
            "img": "https://avatars.cloudflare.steamstatic.com/2c0cd25a7a49b05c1b35aedd25d2e663489634a3_medium.jpg",
            "link": "https://steamcommunity.com/id/fir3_haz4rd",
            "level": 64
        },
        {
            "name": "gigabyte210",
            "img": "https://avatars.cloudflare.steamstatic.com/c03a3d421ce3e8cd051b204f3ec05de695781bfd_medium.jpg",
            "link": "https://steamcommunity.com/profiles/76561198101330139",
            "level": 57
        },
        {
            "name": "MrDivine",
            "img": "https://avatars.cloudflare.steamstatic.com/fe032f5b97f8de627c9d83d1a3a0572d601917d9_medium.jpg",
            "link": "https://steamcommunity.com/id/OfficialMrDivine",
            "level": 56
        },
        {
            "name": "\ud83d\udc7f\ud835\udd44\ud835\udd55\ud835\udd44\ud83d\udc7f",
            "img": "https://avatars.cloudflare.steamstatic.com/faeef81a0980d32d0a89a2bd434a0ea6bade3c3a_medium.jpg",
            "link": "https://steamcommunity.com/profiles/76561198051414229",
            "level": 75
        }
    ],
    "primary_group": {
        "name": "Strid\u025b",
        "url": "https://steamcommunity.com/groups/Team-Stride",
        "image_url": "https://avatars.cloudflare.steamstatic.com/5703dedbb3300bc6e498839ab338fba58df43d90_medium.jpg",
        "member_count": 26.0
    },
    "recent_games": [
        {
            "name": "Counter-Strike 2",
            "img": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_184x69.jpg?t=1698860631",
            "link": "https://steamcommunity.com/app/730",
            "achievements": "1 of 1",
            "hours": 2009
        },
        {
            "name": "Cyberpunk 2077",
            "img": "https://cdn.cloudflare.steamstatic.com/steam/apps/1091500/capsule_184x69.jpg?t=1702306332",
            "link": "https://steamcommunity.com/app/1091500",
            "achievements": "11 of 57",
            "hours": 27.0
        },
        {
            "name": "Lethal Company",
            "img": "https://cdn.cloudflare.steamstatic.com/steam/apps/1966720/capsule_184x69.jpg?t=1700231592",
            "link": "https://steamcommunity.com/app/1966720",
            "achievements": null,
            "hours": 5.8
        }
    ]
}
```