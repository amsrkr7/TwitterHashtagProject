from flask import Flask, redirect, url_for, flash, render_template, request
from flask_login import login_required, logout_user
from urllib.parse import quote
from .config import Config
from .models import db, login_manager, Trending, Tweet
from .oauth import blueprint
from .cli import create_db
import requests
import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
login_manager.init_app(app)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))


@app.route("/", methods=["POST","GET"])
def index():
    status = ''
    if request.method == "POST":
        status =  request.form['status']
        qstr = quote(status)
        resp = blueprint.session.post('statuses/update.json?status={}'.format(qstr))
        flash('Status Sent: {}'.format(status))

        return redirect(url_for("index"))
    return render_template("index.html", status=status)
    #return render_template("home.html")

@app.route("/check", methods=["POST","GET"])
def check():
    status = request.form['status']
    text_tokens = word_tokenize(status)

    lis = []
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    new_tokens = [word for word in tokens_without_sw if word.isalpha()]

    #print(new_tokens)
    sen = ""

    for tokens in new_tokens:
        sen = sen+ tokens+ " "
    sen = sen[:-1]
    new = "\""

    query = sen + " has:hashtags lang:en -is:retweet"
    tweet_fields = "tweet.fields=text"
    tweet_mode = "tweet_mode=extended"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    #print(url)
    bearer_token = Config.BEARER_TOKEN
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    json_response =  response.json()
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    #print(json_response["data"])
    hashtag_list = []
    for contents in json_response["data"]:
        for text in contents["text"].split():
            if text[0] == "#":
                hashtag_list.append(text)
    trending= hashtag_list
    return render_template("index.html", trends=trending, status=status)

@app.route("/suggestions", methods = ["POST","GET"])
def suggest():
    status = request.form['status']
    tokens = word_tokenize(status)
    stop_words = set(stopwords.words('english'))

    filtered_sentence = [w for w in tokens if not w in stop_words]
    filtered_sentence = []

    for w in tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    count = 0
    for token in filtered_sentence:
        hashtag="#"
        token = hashtag + token
        filtered_sentence[count] = token
        count = count +1

    return render_template("index.html", trends= filtered_sentence, status=status)



@app.route("/trending", methods = ["POST","GET"])
def trend():
    status = request.form['status']
    resp = blueprint.session.get("trends/place.json?id=23424977")
    info = resp.json()
    trending = []
    for trend in info[0]['trends']:
        trending.append(trend['name'])
        query_trend = db.session.query(Trending).filter_by(trend=trend['name']).first()
        if bool(query_trend):
            query_trend.tweet_volume = trend['tweet_volume']
        else:
            trend = Trending(
            trend=trend['name'] ,
            url=trend['url'] ,
            query=trend['query'] ,
            tweet_volume=trend["tweet_volume"]
            )
            db.session.add(trend)

    db.session.commit()
    return render_template("index.html", trends=trending[:15], status=status)
