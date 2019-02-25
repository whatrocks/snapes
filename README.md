# snapes

- [ ] `/snippet` route with two params (url and max_age)
    - [ ] returns extracted text
    - [ ] checks cache first before scraping
    - [ ] updates cache
- [ ] cache needs to persist through restarts
- [ ] testing / linting / load testing
- [ ] deployment / docker process
- [ ] logging


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