FROM arm32v7/golang:1.10.4@sha256:7993cd5fcdcb0bf7f170ac269e9782102a386741b4e0079fa410054ffb28ac0e as BUILDER

ENV GOPROXY https://goproxy.cn

WORKDIR /go/src/github.com/faasbenchmark/qrcode
RUN mkdir -p /go/src/github.com/skip2/go-qrcode

COPY go-qrcode /go/src/github.com/skip2/go-qrcode
COPY *.go /go/src/github.com/faasbenchmark/qrcode

RUN go install .

FROM openfaas/classic-watchdog:0.18.1-armhf as watchdog
FROM alpine:3.9@sha256:cfd8b55d209956f63c8fcc931f5c6874984e5e0ffdcb8f45ba9085f190385d73

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
COPY --from=builder /go/bin/qrcode /usr/bin
RUN chmod +x /usr/bin/qrcode

ENV fprocess "/usr/bin/qrcode"

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD [ "/usr/bin/fwatchdog"]
