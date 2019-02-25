FROM python:3.7-alpine

COPY . /app
WORKDIR /app

# TODO: remove this step after install
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install --no-cache-dir -e .; \
	apk del .build-deps;

# RUN pip install --no-cache-dir -e .

# Run flask dev server
# CMD ["flask", "run", "-h" ,"0.0.0.0"]

# Run WSGI app
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "snapes.wsgi:app", "--processes", "2", "--threads", "1", "--py-autoreload", "1", "--reload-mercy", "1", "--worker-reload-mercy", "1"]