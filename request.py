import urllib.request, json
from .models import Sources, Article

# Sources = news.Sources
Articles = Article

# Getting the api key
api_key = None

# Base URL
base_url = None

# Article URL
article_url = None


def configure_request(app):
    global api_key, base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    # print(api_key)
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['BASE_URL']