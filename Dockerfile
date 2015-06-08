FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install -y build-essential python-dev libpqxx-4.0 libpqxx-dev libldap2-dev libsasl2-dev libssl-dev
RUN mkdir /code
WORKDIR /code
ADD ./config/requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
