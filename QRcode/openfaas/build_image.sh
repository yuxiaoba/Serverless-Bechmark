#!/bin/sh
registryurl="harbor.dds-sysu.tech/functions/"
arc="armhf"
functionname="qrcode"

imageurl=$registryurl$functionname":"$arc

docker buildx build --platform linux/arm/v7 . -t $imageurl
docker push $imageurl
