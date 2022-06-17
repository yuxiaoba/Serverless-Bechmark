FROM golang:1.13-alpine3.12@sha256:959dc65113f6fdaa5e395a8a1b2f112d1bd1f5f4e6191bf7ecb7d7d5534bc626 as builder
ENV CGO_ENABLED=0

COPY ./vendor/github.com /go/src/github.com
COPY ./vendor/golang.org /go/src/golang.org
WORKDIR /go/src/github.com/openfaas/faas/sample-functions/MarkdownRender

COPY handler.go .

RUN go install

FROM openfaas/classic-watchdog:0.18.1-armhf as watchdog
FROM alpine:3.13.2@sha256:db5f021b29ec8fcf605f00d2aac06345756b0ffbdea0e7994044fe9172619a0a

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

COPY --from=builder /go/bin/MarkdownRender  /usr/bin/MarkdownRender
ENV fprocess "/usr/bin/MarkdownRender"

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["/usr/bin/fwatchdog"]
