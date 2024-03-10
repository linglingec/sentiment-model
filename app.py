import tkinter as tk
from tkinter import ttk
import requests

# Function to get sentiment score
def get_sentiment():
    text = text_input.get("1.0", "end-1c")
    if text:
        response = requests.post("http://localhost:5000/sentiment", json={"text": text})
        if response.status_code == 200:
            result = response.json()
            score.set(f"Score: {result['score']}")
            sentiment.set(f"Sentiment: {result['label']}")
        else:
            score.set("Error in sentiment analysis")
            sentiment.set("")

# UI setup
root = tk.Tk()
root.title("Sentiment Analysis")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_button = ttk.Button(root, text="Analyze Sentiment", command=get_sentiment)
analyze_button.pack()

score = tk.StringVar()
sentiment = tk.StringVar()

score_label = ttk.Label(root, textvariable=score)
score_label.pack()

sentiment_label = ttk.Label(root, textvariable=sentiment)
sentiment_label.pack()

root.mainloop()