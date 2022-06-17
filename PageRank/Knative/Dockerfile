FROM openfaas/classic-watchdog:0.18.1 as watchdog

FROM lionell/pagerank:latest

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN mkdir /data
COPY ./generated/* /data/

ENV fprocess="omp --dataset /data/1m_10k"

CMD ["/usr/bin/fwatchdog"]
