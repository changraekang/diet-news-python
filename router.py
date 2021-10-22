from flask import Flask
from flask.templating import render_template
import diet_news_api as dn

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html", dietNews = dn.DietNews)

if __name__ == "__main__":
    app.run(debug=True)