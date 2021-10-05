from elasticsearch import Elasticsearch

index = "wasnd"
doc_type = "inventaire"
varoperation = "components"


def get_es_instance():
    es = Elasticsearch(["http://123:9200"])
    return(es)


def unique(list):
    list_unique = []
    list_set = set(list)
    unique_list = (list(list_set))
    for elem in unique_list:
        list_unique.append(elem)
    return(list_unique)


def msearch():
    es = get_es_instance()
    resp = es.search(
        index=varindex,
        doc_type=varoperation,
        body={"size":5000,
            "query": {"bool":{"must" : [
                {"match": {"status": "DONE"}},
                {"match": {"teams": teams}}
                ]
                }
            }
            }
    )
resp['hits']['hits'].sort(
    key=lambda content: (
    content['source']['code'],
    content['source']['code']))

for elem in resp['hits']['hits']:
    print(elem['_source']['tests'])
