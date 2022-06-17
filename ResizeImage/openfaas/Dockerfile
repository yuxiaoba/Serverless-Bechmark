FROM openfaas/classic-watchdog:0.18.1-armhf as watchdog

FROM functions/alpine:latest-armhf

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN apk --no-cache add imagemagick

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

ENV fprocess "convert - -resize 50% fd:1"

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD [ "/usr/bin/fwatchdog"]
