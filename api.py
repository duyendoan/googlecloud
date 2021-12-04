import flask
from flask import request, jsonify
from test import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>THIS IS A TEST</h1>
<p>Test API</p>'''


@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    results = get_movies_by_id()
    return jsonify(results)


@app.route('/api/v1/resources/movies', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'movieId' in request.args:
        movieId = int(request.args['movieId'])
    else:
        return "Error: No movieId field provided. Please specify an movieId."
        
    if 'imdbId' in request.args:
        imdbId = int(request.args['imdbId'])
    else:
        return "Error: No imdbId field provided. Please specify an imdbId."

    results = get_movies_by_movieId_userId(movieId, imdbId)

    return jsonify(results)

app.run()