FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update && \
      apt-get -y install sudo
RUN wget -qO- https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN apt-get install npm
RUN npm install
RUN pip install --no-cache-dir -r requirements.txt

