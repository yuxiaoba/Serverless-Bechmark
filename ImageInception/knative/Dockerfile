FROM openfaas/classic-watchdog:0.18.1 as watchdog
FROM python:3.7-slim-buster

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

ARG ADDITIONAL_PACKAGE
# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apt-get -qy update && apt-get install -qy apt-transport-https ca-certificates 
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY sources.list /etc/apt/
RUN apt-get -qy update &&  apt-get -qy install htop gcc make ${ADDITIONAL_PACKAGE}

WORKDIR /root/

COPY requirements.txt ./
COPY *.py ./

RUN pip install -i  https://mirrors.aliyun.com/pypi/simple/ pip -U
RUN pip config set global.index-url  https://mirrors.aliyun.com/pypi/simple/
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

ENV TF_CPP_MIN_LOG_LEVEL=3
RUN python ./pre_download.py

ENV write_debug="true"
ENV fprocess="python index.py"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1
CMD ["/usr/bin/fwatchdog"]
