FROM ubuntu:22.04

RUN apt update -y
RUN apt install -y libsm6 libxext6
RUN apt install -y libxrender-dev
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.7 -y
RUN apt install python3-pip -y
RUN apt install python3.7-distutils -y
WORKDIR app/

COPY . .
RUN python3.7 -m pip install --no-cache-dir -r requirements.txt
RUN ls /usr/bin/python*
RUN ls

RUN chmod u+x VideoRun.sh
CMD ["/bin/bash", "-c", "./VideoRun.sh"]