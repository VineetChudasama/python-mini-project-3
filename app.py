from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_songs():
    with open('data/songs.json', 'r') as file:
        return json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    mood = None
    songs = []
    if request.method == 'POST':
        mood = request.form.get('mood')
        all_songs = load_songs()
        songs = all_songs.get(mood, [])
    return render_template('index.html', mood=mood, songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
