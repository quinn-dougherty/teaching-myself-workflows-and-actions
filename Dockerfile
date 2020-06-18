FROM python:3.8.3-slim-buster
COPY . .
CMD python app/request.py
