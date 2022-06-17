FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM yuxiaoba/archlinux-armv7:base

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN mkdir /data
COPY ./generated/* /data/

COPY omp /usr/bin
RUN chmod +x /usr/bin/omp 

ENV fprocess="omp --dataset /data/1m_10k"

ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["/usr/bin/fwatchdog"]
