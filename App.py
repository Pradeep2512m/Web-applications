from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my website"

@app.route('/contact')
def contact_page():
    return "contact page"

@app.route('/gallery')
def gallery_page():
    return "gallery page"

@app.route('/home')
def home_page():
    return "home page"

if __name__ == "__main__":
    app.run()