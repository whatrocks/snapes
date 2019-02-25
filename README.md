# snapes

Snapes is a RESTful snippets service that returns a short text snippet from a given website URL.

## Local development

Snapes uses `docker-compose` locally to build and run its microservices (currently Flask for API layer and Redis for caching). You need to have Docker running locally - you can [download Docker Desktop here](https://www.docker.com/products/docker-desktop).

To build and run the Snapes containers locally:

```bash
make build-and-run
```

Snapes will be available locally at port 5000. You can try out Snapes:

```bash
$ curl -G "http://localhost:5000/snippet" \
  --data-urlencode "url=https://en.wikipedia.org/wiki/Cheese" \
  --data-urlencode "max_age=3600"
```

As you can see, you need to provide a `url` and `max_age` as parameters. Snapes uses the `max_age` to determine the length of time a given snippet will persist in the Redis cache.

Alternatively to curl, you can use the provided utility script:

```bash
./scripts/curl.sh
```

### Testing

Run static analysis, linting, and unit tests:

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
make build-local
make check-all
```

### Debugging

Restart a container by name (e.g. redis).
```bash
docker-compose restart redis
```

Stop a container (without killing everything).
```bash
docker-compose stop redis
```

Kill a container and its memory
```bash
docker-compose down redis
```

Open redis-cli on redis container to explore the cache
```bash
docker-compose exec redis redis-cli
keys *
```

## To-do list

- [x] `/snippet` route with two params (url and max_age)
    - [x] returns extracted text
    - [x] checks redis cache first before scraping
    - [x] updates redis cache
- [x] cache needs to persist through service restarts
- [x] unit tests
- [x] add wsgi layer
- [x] linting
- [x] makefile
- [x] documenation
- [ ] improve logging
- [ ] add nginx
- [ ] deployment / docker process
- [ ] backup the redis RDB file to s3 once a day / hour?
- [ ] load testing