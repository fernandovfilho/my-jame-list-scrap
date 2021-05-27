from flask import Flask, request, jsonify, render_template
from requests import get
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    query = request.args.get('query')

    if query is None:
        return "paramentro 'query' não especificado"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = get(f"https://www.giantbomb.com/api/search/?api_key=b6a60d7da93c2fc2cb3d5256ac814ff324be71eb&query={query}&format=json", headers=headers).json()

    games = []

    for i in r['results']:

        name = i['name']
        id = i['id']
        icon_url = i['image']['icon_url']
        thumb = i['image']['thumb_url']
        full_size = i['image']['original_url']



        platforms = []

        if 'platforms' in i:
            for p in i['platforms']:
                platforms.append(p['name'])

        data = {
            'id': id,
            'nome': name,
            'imagens': {
                'pequena': icon_url,
                'media': thumb,
                'original': full_size
            },
            'plataformas': ';'.join(platforms)
        }

        games.append(data)
    
    return jsonify(games)

@app.route('/game')
def seachById():
    game_id = request.args.get('id')
    if game_id is None:
        return "paramentro 'game_id' não especificado"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = get(f"https://www.giantbomb.com/api/game/{game_id}/?api_key=b6a60d7da93c2fc2cb3d5256ac814ff324be71eb&format=json", headers=headers).json()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

