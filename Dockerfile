FROM python:3.8.5

WORKDIR /usr/src/goatbot

RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . .

CMD ["python", "src/bot.py"]