# _*_ coding:utf-8 _*_
from flask import Flask

app = Flask(__name__)


import urls



if __name__ == '__main__':
    app.run(debug=True)