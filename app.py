from flask import Flask, render_template
import requests 
import json 

app = Flask(__name__)

# This function fetches a random meme from the meme-api
def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url).json()
    meme_large = response["url"]
    subreddit = response["subreddit"]
    return meme_large, subreddit


# This route fetches a random meme and displays it
@app.route("/randommeme/")
def random_meme():
    meme_pic, subreddit = get_meme()
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)


@app.route("/")
def index():
    return render_template("index.html")