FROM python:3.8-slim-buster

ENV URL="http://nav-deckofcards.herokuapp.com/shuffle"

COPY . .

RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt

ENTRYPOINT python main.py --url ${URL}


