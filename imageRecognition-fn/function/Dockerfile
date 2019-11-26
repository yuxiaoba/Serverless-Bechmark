#FROM tensorflow/tensorflow:latest
FROM gigi1982/inception-function-start
RUN apt-get update -qy \
 && apt-get install -qy \
       python3-pip

WORKDIR /app/

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

ENV TF_CPP_MIN_LOG_LEVEL=3
COPY *.py ./

RUN python3 ./pre_download.py

COPY *.txt ./

CMD ["python3", "index.py"]
