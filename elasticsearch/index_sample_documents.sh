#!/bin/sh

curl -XPUT localhost:9200/fruit_basket/_create/1 -H "Content-Type: application/json" -d '{
     "fruit": "orange"
}';

curl -XPUT localhost:9200/fruit_basket/_create/2 -H "Content-Type: application/json" -d '{
     "fruit": "apple"
}';

curl -XPUT localhost:9200/fruit_basket/_create/3 -H "Content-Type: application/json" -d '{
     "fruit": "banana"
}';
