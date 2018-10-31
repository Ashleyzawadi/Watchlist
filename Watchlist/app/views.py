from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    message = 'Hello World'
    title = 'Home - Welcome tothe Best movie Review Website online'
    return render_template('index.html', message = message, title = title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html', id = movie_id)