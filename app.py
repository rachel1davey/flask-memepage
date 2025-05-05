from flask import Flask, render_template
import requests 
import json 

app = Flask(__name__)

# This function fetches a random meme from the meme-api
def get_meme(category=None):
    if category:
        url = f"https://meme-api.com/gimme/{category}"
    else:
        url = "https://meme-api.com/gimme/"

    response = requests.get(url).json()
    meme_large = response["url"]
    subreddit = response["subreddit"]
    return meme_large, subreddit


# This route fetches a random meme and displays it
@app.route("/randommeme/")
def random_meme(category=None):
    meme_pic, subreddit = get_meme(category=None)
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)

# Routes for specific categories
@app.route("/politicalmemes/")
def political_memes():
    meme_pic, subreddit = get_meme("politicalmemes")
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/cryptomemes/")
def crypto_memes():
    meme_pic, subreddit = get_meme("cryptomemes")
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/catmemes/")
def cat_memes():
    meme_pic, subreddit = get_meme("catmemes")
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/dogmemes/")
def dog_memes():
    meme_pic, subreddit = get_meme("dogmemes")
    return render_template("random_meme.html", meme_pic=meme_pic, subreddit=subreddit)




@app.route("/")
def index():
    return render_template("index.html")