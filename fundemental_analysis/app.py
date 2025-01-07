from flask import Flask, render_template
from data_scraper import scrape_data


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)