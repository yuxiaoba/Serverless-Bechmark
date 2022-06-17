FROM openfaas/classic-watchdog:0.18.1-armhf as watchdog
FROM python:3.7-slim-buster@sha256:84cdade544de0e76c963c8d073348019c936bafd91fc496615cc62dad5e89e21

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

ARG ADDITIONAL_PACKAGE
# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apt-get -qy update && apt-get install -qy apt-transport-https ca-certificates
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY sources.list /etc/apt/
RUN apt-get -qy update &&  apt-get -qy install gcc make ${ADDITIONAL_PACKAGE}

WORKDIR /root/

COPY requirements.txt ./
COPY *.py ./
COPY tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl ./

RUN pip install -i  https://mirrors.aliyun.com/pypi/simple/ pip -U
RUN pip config set global.index-url  https://mirrors.aliyun.com/pypi/simple/
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
RUN rm tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl

ENV TF_CPP_MIN_LOG_LEVEL=3
RUN python ./pre_download.py

ENV write_debug="true"
ENV fprocess="python index.py"

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1
CMD ["/usr/bin/fwatchdog"]
