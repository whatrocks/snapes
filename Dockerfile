FROM kennethreitz/pipenv
COPY . /app
WORKDIR /app
CMD ["python3", "snapes/app.py"]