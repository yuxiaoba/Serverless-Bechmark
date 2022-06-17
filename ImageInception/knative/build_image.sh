#!/bin/sh
registryurl="harbor.dds-sysu.tech/functions/"
arc="amd"
functionname="imageinception"

dockerhuburl="yuxiaoba/"$functionname":"$arc

imageurl=$registryurl$functionname":"$arc

docker build . -t $imageurl

docker push $imageurl

docker tag $imageurl $dockerhuburl

docker push $dockerhuburl
