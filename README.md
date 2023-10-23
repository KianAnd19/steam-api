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

`git clone https://github.com/yourusername/steam-profile-scraper.git`

2. Switch to the project directory

`cd steam-profile-scraper`

3. Run the Flash web application:

`python3 steam_api.py`