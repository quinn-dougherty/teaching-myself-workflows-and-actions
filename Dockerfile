FROM python:3.9.0b3-alpine3.12
WORKDIR app
COPY . .
RUN pip install -r requirements.txt
RUN python app/app.py
