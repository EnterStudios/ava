FROM python:3.4
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install -y build-essential python3-dev libpqxx-4.0 libpqxx-dev libldap2-dev libsasl2-dev libssl-dev
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --use-wheel -r /code/requirements/common.txt
