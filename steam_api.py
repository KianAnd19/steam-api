import steam_scraper
from flask import Flask, request, jsonify
import os

GITHUB_API_PORT = os.environ.get("STEAM_API_PORT", 5000)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Active'

@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    temp = (steam_scraper.get_user_profile(name))
    if temp == None:
        return None, 404
    return temp, 200

@app.route('/user/inventory_cs/<name>', methods=['GET'])
def get_user(name):
    temp = (steam_scraper.get_user_inventory_cs(name))
    if temp == None:
        return None, 404
    return temp, 200

if __name__ == '__main__':
    app.run(debug=True, port = GITHUB_API_PORT)
