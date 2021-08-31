
import requests
import os
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='AAAAAAAAAAAAAAAAAAAAAE0zIwEAAAAAQ8CxLojtkW6Hfq%2F13yocU87VMfA%3DBab0vO44egfy8ANQzjau070tB0UNEI189uhzpQdJRjvwiEcbQM'


def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url():


   
    text = input("Enter your tweet:")

    text_tokens = word_tokenize(text)

    lis = []
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    new_tokens = [word for word in tokens_without_sw if word.isalpha()]

    print(new_tokens)

    sen = ""

    for tokens in new_tokens:
        sen = sen+ tokens+ " "
    sen = sen[:-1]
    new = "\""
    query = sen + " has:hashtags lang:en" 


    print(query)
    
    tweet_fields = "tweet.fields=text"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    print(url)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    //print(json_response["data"])
    

if __name__ == "__main__":
    main()

  