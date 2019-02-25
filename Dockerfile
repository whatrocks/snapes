FROM kennethreitz/pipenv
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]