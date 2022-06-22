from flask import Flask, jsonify, redirect, render_template, request, url_for
import requests
app = Flask(__name__)

@app.route('/')
def home():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url) 
    r_json = response.json()
    personajes = r_json['results']
    return render_template('index.html', data = personajes)

if __name__ == "__main__":
    app.run(debug=True)