#/bin/ksh

list_index="toolbox   "

for index in $list_index
    do

    curl - X POST -u_xxx "10x:9200/_reindex?pretty" -H 'Content-Type:application/json' -d'
    {
        "source":{
            "remote": {
                "host": "http://"
            },
        "index": "'"$index"'",
        "query": {
            "match_all" :{}

        }

        },
        "dest":{
            "index": "'"$index"'"
        }
    }
    '

done