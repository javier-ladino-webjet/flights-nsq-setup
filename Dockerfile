FROM python:3.9


RUN apt-get update -y; apt-get upgrade -y
RUN python -m pip install --upgrade pip
RUN python -m pip install requests


WORKDIR /usr/app
COPY . /usr/app/

CMD [ "python3", "src/app.py" ]