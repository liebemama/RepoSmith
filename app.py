from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") which returns "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# This block allows you to run the app directly from the command line
if __name__ == '__main__':
    # debug=True will reload the server automatically when you make changes
    app.run(debug=True)
