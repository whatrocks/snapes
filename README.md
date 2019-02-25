# snapes

- [x] `/snippet` route with two params (url and max_age)
    - [x] returns extracted text
    - [x] checks cache first before scraping
    - [x] updates cache
- [x] cache needs to persist through restarts
- [ ] fix unit testing
- [ ] deployment / docker process
- [ ] add wsgi / gunicorn ... maybe nginx?
- [ ] logging
- [ ] backup the redis RDB file to s3 once a day / hour?
- [ ] load testing
- [ ] linting

### Notes

Add this to bash profile
`export PIPENV_VENV_IN_PROJECT=1`

## Local set up

Build images
`docker-compose build`

Start the containers
`docker-compose up -d`

Restart a container (e.g. redis)
`docker-compose restart redis`

Stop a container (without killing everything)
`docker-compose stop redis`

Kill a container and its memory
`docker-compose down redis`

Open redis-cli on redis container
`docker-compose exec redis redis-cli`