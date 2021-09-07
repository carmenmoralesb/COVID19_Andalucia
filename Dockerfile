# pull official base image
FROM ubuntu:latest

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

# install psycopg2 dependencies
RUN apt-get update
RUN apt-get install -y \
    python3 dh-python python3-dev gcc python3-pip \
    postgresql cron
RUN apt-get install -y dos2unix
# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /home/app

# create the appropriate directories

# create the app user
RUN addgroup --system app 
RUN adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# copy project
COPY . $APP_HOME

RUN usermod -a -G app app

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Setup cron job
ADD cron_job /etc/cron.d/cron_job
RUN chmod 0744 /etc/cron.d/cron_job &&\
    crontab /etc/cron.d/cron_job
RUN dos2unix /etc/cron.d/cron_job

RUN service cron start

CMD ["cron", "-f"]