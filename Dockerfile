FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt install git python3 tzdata python3-pip ffmpeg -y 
RUN pip3 install -U pip

RUN mkdir /app/
WORKDIR /app/
RUN chmod 777 /app/
COPY requirements.txt /app/
RUN pip3 install -U -r requirements.txt
COPY . /app/
EXPOSE 8000

CMD ["python3", "-m", "Ayane"]