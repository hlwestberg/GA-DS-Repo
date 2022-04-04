import flask

# create a flask application using the Flask class
app = flask.Flask(__name__)

# creating our route- url
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/greet/<name>')
def greet(name):
    '''Say hello to your first parameter'''
    return "Hello, {}!".format(name)

# runs the application when script is executed. 
if __name__ == '__main__':
    app.run(debug=True)