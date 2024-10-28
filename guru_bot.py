
import json
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return "positive"
    elif scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"


def load_quotes():
    with open("quotes.json", "r") as file:
        return json.load(file)


def get_quote(category):
    quotes = load_quotes()
    if category in quotes:
        return random.choice(quotes[category])
    return "Sometimes silence itself is the best answer."


def guru_response(user_input):
    category = analyze_sentiment_vader(user_input)
    quote = get_quote(category)
    return quote


if __name__ == '__main__':
    print("Hello! I’m your personal guru bot, here to offer wisdom and support. How are you feeling today?")
    print("type 'quit' to exit.")
    while True:
        user_input = input("Message Guru Bot: ")
        if user_input.lower() == 'quit':
            break
        response = guru_response(user_input)
        print("Guru Bot:", response)
