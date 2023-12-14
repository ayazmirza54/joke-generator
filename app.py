from flask import Flask, render_template
import requests

app = Flask(__name__)

def generate_joke():
    api_url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            if data["type"] == "single":
                return f"Joke: {data['joke']}"
            elif data["type"] == "twopart":
                return f"Setup: {data['setup']}\nPunchline: {data['delivery']}"
            else:
                return "Oops! Unable to fetch a joke at the moment."
        else:
            return "Oops! Unable to fetch a joke at the moment."

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while fetching the joke."

@app.route('/')
def index():
    joke = generate_joke()
    return render_template('index.html', joke=joke)
