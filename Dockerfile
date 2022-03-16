FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD [ "python3", "app.py"]
HEALTHCHECK CMD curl --fail http://localhost:3000 || exit 1
