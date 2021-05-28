from flask import Flask, request, jsonify, render_template
from requests import get
from datetime import datetime
app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('query')
    page = request.args.get('page')

    if query is None:
        return "paramentro 'query' não especificado"
    if page is None:
        page = 1

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = get(f"https://www.giantbomb.com/api/search/?api_key=b6a60d7da93c2fc2cb3d5256ac814ff324be71eb&query={query}&page={page}&resources=game&format=json", headers=headers).json()

    games = []

    for i in r['results']:

        name = i['name']
        id = i['id']
        icon_url = i['image']['icon_url']
        thumb = i['image']['thumb_url']
        full_size = i['image']['original_url']

        try:
            release = datetime.strptime(i['original_release_date'],'%Y-%m-%d').strftime('%d/%m/%Y')
        except:
            release = "N/A"



        platforms = []

        if 'platforms' in i:
            try:
                for p in i['platforms']:
                    platforms.append(p['name'])
            except:
                platforms.append('N/A')


        data = {
            'id': id,
            'nome': name,
            'release': release,
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
        return "paramentro 'id' não especificado"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = get(f"https://www.giantbomb.com/api/game/{game_id}/?api_key=b6a60d7da93c2fc2cb3d5256ac814ff324be71eb&format=json", headers=headers).json()

    for i in r['results']:

        name = i['name']
        id = i['id']
        icon_url = i['image']['icon_url']
        thumb = i['image']['thumb_url']
        full_size = i['image']['original_url']

        try:
            release = datetime.strptime(i['original_release_date'],'%Y-%m-%d').strftime('%d/%m/%Y')
        except:
            release = "N/A"


@app.route('/test')
def test():
    query = request.args.get('query')
    page = request.args.get('page')

    if query is None:
        return "paramentro 'query' não especificado"
    if page is None:
        page = 1

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = get(f"https://www.giantbomb.com/api/search/?api_key=b6a60d7da93c2fc2cb3d5256ac814ff324be71eb&query={query}&page={page}&resources=game&format=json", headers=headers).json()

    games = []

    for i in r['results']:

        name = i['name']
        id = i['id']
        icon_url = i['image']['icon_url']
        thumb = i['image']['thumb_url']
        full_size = i['image']['original_url']

        try:
            release = datetime.strptime(i['original_release_date'],'%Y-%m-%d').strftime('%d/%m/%Y')
        except:
            release = "N/A"



        platforms = []

        if 'platforms' in i:
            try:
                for p in i['platforms']:
                    platforms.append(p['name'])
            except:
                platforms.append('N/A')


        data = {
            'id': id,
            'nome': name,
            'release': release,
            'imagens': {
                'pequena': icon_url,
                'media': thumb,
                'original': full_size
            },
            'plataformas': ';'.join(platforms)
        }

        games.append(data)
    
    return jsonify(games)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

