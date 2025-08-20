from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

@app.route('/')
def index():
    response = requests.get(API_URL)
    data = response.json()
    return render_template('index.html', crypto=data)

if __name__ == "__main__":
    app.run(debug=True)
