import os
from elasticsearch import Elasticsearch
from flask import Flask, render_template, request, jsonify
from search import multi_index_search


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/healthcheck')
def healthcheck():
    return render_template('healthcheck.html')


@app.route('/toolbox', methods=['POST', 'GET'])
def toolbox():
    if request.method == "POST":
        keyword = request.form['searchtoolbox']
        es = Elasticsearch(['http://'])
        body = {
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["alias", "host"]
                }
            }
        }

        res = es.search(index="toolbox", body=body)
        for elem in res['hits']['hits']:
            alias = elem['_source']['alias']
            version = elem['_source']['version']
            env = elem['_source']['env']

        infos = {'alias': alias, 'version': version, 'env': env}

        return render_template('detail.html', **infos)
    else:
        return render_template('toolbox.html')


@app.route('/search', methods=['POST','GET'])
    def search():
        infos = multi_index_search()
        return render_template('search_index.html', **infos)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
