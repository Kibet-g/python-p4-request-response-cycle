import os
from flask import Flask, request, current_app, g, make_response, redirect, abort

# Create Flask application instance
app = Flask(__name__)

# Before request hook to store application path in global object 'g'
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# Route to handle the index page
@app.route('/')
def index():
    # Accessing request and application context
    host = request.headers.get('Host')
    appname = current_app.name

    # Creating the response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    # Setting HTTP status code and headers
    status_code = 200
    headers = {}

    # Returning the response with status and headers
    return make_response(response_body, status_code, headers)

# Route to demonstrate redirect
@app.route('/redirect')
def redirect_example():
    return redirect('/')

# Route to demonstrate abort with a 404 error
@app.route('/error')
def error_example():
    abort(404)

# Running the Flask application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
