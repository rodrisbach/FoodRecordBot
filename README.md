# FoodRecordBot

Telegram bot to record all foods over a period of time (a day, a week, a month...)

## Requirements
* Docker
### Without using Docker
* Python3
* Virtualenv, Pipenv, or any tool to create isolated Python environment

## How to use it?
You will need to load an environment variable called TOKEN with the Telegram Bot's Token
``export TOKEN="YOUR_TOKEN"``

### Using docker
1. Build the Docker image
``docker build -t foodrecordbot .``
2. Run the Docker container
``docker run -d --rm --env TOKEN=$TOKEN foodrecordbot``
