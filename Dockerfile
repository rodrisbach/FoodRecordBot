FROM python:3.9.2-alpine

WORKDIR /app

COPY src/ ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "telegramBot.py" ]


