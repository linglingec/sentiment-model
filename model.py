from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the sentiment analysis model
sentiment_analysis = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

app = Flask(__name__)

# Define a function to apply sentiment analysis
def analyze_sentiment(text):
    try:
        sentiment = sentiment_analysis(text)
        return sentiment[0]['label'], sentiment[0]['score']
    except:
        return None, None

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    label, score = analyze_sentiment(text)
    if label is not None:
        return jsonify({"label": label, "score": score})
    else:
        return jsonify({"error": "Error in processing sentiment analysis"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)