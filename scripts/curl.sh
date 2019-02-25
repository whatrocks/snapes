#!/bin/bash

URL=https://en.wikipedia.org/wiki/Beer  
MAX_AGE=60

curl -G "http://localhost:5000/snippet" --data-urlencode "url=$URL" --data-urlencode "max_age=$MAX_AGE"