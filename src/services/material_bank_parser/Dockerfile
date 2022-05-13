FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5100 --workers=1 --threads=1 --chdir=. --log-level 'debug'"
EXPOSE 5100

CMD ["gunicorn", "app:app"]