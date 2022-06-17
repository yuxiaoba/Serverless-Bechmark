FROM golang:1.10.4 as BUILDER

ENV GOPROXY https://goproxy.cn

WORKDIR /go/src/github.com/faasbenchmark/qrcode
RUN mkdir -p /go/src/github.com/skip2/go-qrcode

COPY go-qrcode /go/src/github.com/skip2/go-qrcode
COPY *.go /go/src/github.com/faasbenchmark/qrcode

RUN go install .

FROM openfaas/classic-watchdog:0.18.1 as watchdog
FROM alpine:3.9

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog
COPY --from=builder /go/bin/qrcode /usr/bin
RUN chmod +x /usr/bin/qrcode

ENV fprocess "/usr/bin/qrcode"

CMD [ "/usr/bin/fwatchdog"]
