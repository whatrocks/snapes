#!/bin/bash

URL=https://www.nintendo.com
MAX_AGE=10

curl -G "http://localhost:5000/snippet" --data-urlencode "url=$URL" --data-urlencode "max_age=$MAX_AGE"