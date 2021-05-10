FROM python:3.8-slim-buster
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN python3 -m venv /opt/venv
COPY requirements.txt requirements.txt
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]