curl -X PUT "localhost:9200/dbpedia_abstracts?pretty" -H 'Content-Type: application/json' -d'
{ "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "term_vector": "with_positions_offsets_payloads",
        "store" : true,
        "analyzer" : "fulltext_analyzer"
       }
    }
  },
  "settings" : {
    "index" : {
      "number_of_shards" : 2,
      "number_of_replicas" : 0
    },
    "analysis": {
      "analyzer": {
        "fulltext_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": [
            "lowercase",
            "type_as_payload"
          ]
        }
      }
    }
  }
}'
