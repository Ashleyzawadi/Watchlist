from flask import render_template
from app import app
from .request import get_movies, get_movie

#Views
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome tothe Best movie Review Website online'
    return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie, now_showing=now_showing_movie)

# @app.route('/movie/<int:movie_id>')
# def movie(movie_id):
#     return render_template('movie.html', id = movie_id,)

@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html', title = title, movie=movie)

