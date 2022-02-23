FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

WORKDIR /usr/src/app

RUN apt-get -y update &&\
    apt-get -y install git \    
    curl\
    nano
    
COPY requirements.txt ./
COPY . /usr/src/app

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 

EXPOSE 8888