from app import app
import urllib.request, json # urllib.request helps us create a connection to our API URL and send a request. json modules format json responses to python dictionary
from .models import movie

Movie = movie.Movie

#Getting api key
api_key = app.config['MOVIE_API_KEY']

#Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results)
    
    return movie_results 