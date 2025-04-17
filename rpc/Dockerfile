FROM python:3-alpine

WORKDIR /rpc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY common /rpc/common
COPY rpc.py ./
COPY boot.sh ./
RUN chmod +x boot.sh

ENTRYPOINT ["./boot.sh"]