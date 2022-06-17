#!/bin/sh
registryurl="harbor.dds-sysu.tech/functions/"
arc="armhf"
functionname="sentiment"

imageurl=$registryurl$functionname":"$arc

docker buildx build --platform linux/arm/v7 . -t $imageurl
docker push $imageurl