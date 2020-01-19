import re
import hashlib
import requests

with open('/home/mdaquin/data/dbpedia/long_abstracts_wkd_uris_en.ttl', 'r') as reader:     
     line = reader.readline()
     object ={'uri': '', 'text':''}
     while line != '': 
          usearch = re.search('^<([^ ]*)> ',line)
          if usearch:
              object['uri'] = usearch.group(1)
          tsearch = re.search('"(.*)"',line)
          if tsearch:
               object['text'] = tsearch.group(1)
          id = hashlib.md5(object['uri']).hexdigest()
          print (id+' '+object['uri'])
          r=requests.put('http://localhost:9200/dbpedia_abstracts/_doc/'+id,json=object)
          print(r.status_code)
          # print(r.text)
          line = reader.readline()
          object ={'uri': '', 'text':''}
