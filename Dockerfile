FROM python:3.9.0b3-buster
WORKDIR app
COPY . .
RUN pip install -r requirements.txt
RUN python app/app.py
