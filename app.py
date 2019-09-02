from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    #return u'Welcome to My Watchlist!'
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/home')
def home():
    return 'Welcome to My Watchlist!'

@app.route('/user/<name>')
def user_page(name):
    #return 'User page'
    return 'User :%s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='grepyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
