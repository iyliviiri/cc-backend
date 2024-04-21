from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

app = Flask(__name__)

# Initialize NLTK's sentiment analyzer
nltk.download('vader_lexicon')  # Download dictionary for sentiment analysis
sia = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        sentiment_scores = sia.polarity_scores(user_input)
        sentiment = "Positive" if sentiment_scores["compound"] > 0 else "Negative"
        return render_template("results.html", user_input=user_input, sentiment=sentiment)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)