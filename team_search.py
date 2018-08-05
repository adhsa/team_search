from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

# Stuff for flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

# Connect to elasticsearch
client = Elasticsearch(
    'https://username:password@363516e916bf46eea1aaa035058f02d7.eu-west-1.aws.found.io:9243')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form['team_query']

        query = {
            'size': 20,
            'query': {
                'match': {
                    'text': keyword
                }
            }
        }
        res = client.search(index='team_search', body=query)
        data = [{'link': r['_id'], 'score': r['_score'], 'team': r['_id'].split('igem.org/Team:')[-1]} for r in res['hits']['hits']]
        output = {'data': data}
        return jsonify(output)

    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)
