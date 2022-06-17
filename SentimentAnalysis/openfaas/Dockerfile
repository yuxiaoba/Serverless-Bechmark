FROM openfaas/classic-watchdog:0.18.1-armhf as watchdog

FROM python:2.7-alpine@sha256:4d909d59d1d9b2cd8ac36e3c3cf6dd95b6cad9506c62bf5ed4f3505b6ae2c693

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk add --no-cache gcc g++ python-dev linux-headers libffi-dev openssl-dev

RUN pip install -i  https://mirrors.aliyun.com/pypi/simple/ pip -U
RUN pip config set global.index-url  https://mirrors.aliyun.com/pypi/simple/
RUN pip install textblob && pip install nltk==3.4.5

ENV NLTK_DATA /usr/share/nltk_data
COPY nltk_data /usr/share/nltk_data

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog 

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

WORKDIR /home/app

COPY handler.py .
ENV fprocess="python handler.py"

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]

