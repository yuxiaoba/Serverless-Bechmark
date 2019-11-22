FROM harbor.test.com/knative/python3.7-alpine:v1 as builder

RUN apk add --no-cache \
    linux-headers \
    tcpdump \
    build-base \
    ebtables

WORKDIR /kube-hunter
COPY ./requirements.txt /kube-hunter/.
RUN pip install -r /kube-hunter/requirements.txt -t /kube-hunter

COPY . /kube-hunter

FROM harbor.test.com/knative/python3.7-alpine:v1

COPY --from=builder /kube-hunter /kube-hunter

WORKDIR /kube-hunter

ENTRYPOINT python kube-hunter.py --pod
