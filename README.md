# snapes

- [x] `/snippet` route with two params (url and max_age)
    - [x] returns extracted text
    - [x] checks cache first before scraping
    - [x] updates cache
- [x] cache needs to persist through restarts
- [x] unit tests
- [x] add wsgi
- [x] linting
- [x] makefile
- [ ] documenation
- [ ] add nginx?
- [ ] deployment / docker process
- [ ] logging
- [ ] backup the redis RDB file to s3 once a day / hour?
- [ ] load testing

## Local set up

Build and run the containers
```bash
make build-and-run
```

Restart a container (e.g. redis)
```bash
docker-compose restart redis
```

Stop a container (without killing everything)
```bash
docker-compose stop redis
```

Kill a container and its memory
```bash
docker-compose down redis
```

Open redis-cli on redis container
```bash
docker-compose exec redis redis-cli
keys *
```

## Run tests

```bash
virtualenv -p python3 /.venv
source /.venv/bin/activate
make build-local
make check-all
```