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

def get_sources(category):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        # print(get_sources_response)
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    """
    Function that processes the sources result and tranforms them to a list of objects
    """
