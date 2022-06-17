#!/bin/sh
registryurl="harbor.dds-sysu.tech/functions/"
arc="amd"
functionname="resizeimage"

imageurl=$registryurl$functionname":"$arc

docker build . -t $imageurl

docker push $imageurl