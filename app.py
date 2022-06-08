from flask import Flask, request
app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """Return 'welcome'"""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def welcome_home():
    """Return 'welcome home'"""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.get('/welcome/back')
def welcome_back():
    """Return 'welcome back'"""

    html = "<html><body><h1>Welcome Back</h1></body></html>"
    return html
