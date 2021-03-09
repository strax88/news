FROM python:3.8.5
RUN apt-get update
RUN apt-get install apt-utils nano mc python3-pip libpq-dev systemd git -y
ADD . /home/task
WORKDIR /home/task
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt