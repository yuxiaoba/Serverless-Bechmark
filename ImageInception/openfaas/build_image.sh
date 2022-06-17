#!/bin/sh
registryurl="harbor.dds-sysu.tech/functions/"
arc="armhf"
functionname="imageinception"

imageurl=$registryurl$functionname":"$arc

docker buildx build --platform linux/arm/v7 . \
    --build-arg ADDITIONAL_PACKAGE="libatlas-base-dev gfortran libhdf5-dev libc-ares-dev libeigen3-dev libopenblas-dev libblas-dev liblapack-dev build-essential" \
    -t $imageurl
    
docker push $imageurl