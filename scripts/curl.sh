#!/bin/bash

URL=https://www.holloway.com
MAX_AGE=3600

curl -G "http://localhost:4000/snippet"   --data-urlencode "url=$URL"   --data-urlencode "max_age=$MAX_AGE"