FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -e .

CMD ["flask", "run", "-h" ,"0.0.0.0"]