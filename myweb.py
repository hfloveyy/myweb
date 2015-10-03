from flask import Flask
import model
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello_world2():
    return 'Hello World2!'

if __name__ == '__main__':
    app.run(debug=True)