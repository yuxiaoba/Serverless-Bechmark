# functions/image inception

![](https://upload.wikimedia.org/wikipedia/commons/6/61/Humpback_Whale_underwater_shot.jpg) 

 You can call a HTTP endpoint with a URL to an image and get back categorizations through machine learning fast.

## Deploy the image inception function

### openfaas
```
$ bash ./openfaas/deploy.sh
```

### Knative
```
$ bash ./knative/deploy.sh
```

## Invoke Function

Now pick an image such as the included picture of Gordon and use `curl` or a tool of your choice to send the data to the function. Pipe the result into a new file like this:

### Faasd

```
$ faas-cli describe imageinception
Name:                imageinception
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    python index.py
URL:                 http://192.168.50.23:31112
/function/imageinception
Async URL:           http://192.168.50.23:31112
/async-function/imageinception

$ curl http://192.168.50.23:31112
/function/imageinception  -d 'https://clubimg.club.vmall.com/pic/2017/01/25/56fe4ab0aa41def434824d3302b44a26_IMG_20170125_153114.jpg'

[{"score": 0.6955435276031494, "name": "tabby"}, {"score": 0.1721213459968567, "name": "tiger cat"}, {"score": 0.06431407481431961, "name": "Egyptian cat"}, {"score": 0.0029729718808084726, "name": "lynx"}, {"score": 0.0020706052891910076, "name": "tiger"}, {"score": 0.0010852533159777522, "name": "doormat"}, {"score": 0.0009471490629948676, "name": "zebra"}, {"score": 0.00035808392567560077, "name": "window screen"}, {"score": 0.0003420915163587779, "name": "Persian cat"}, {"score": 0.0003204822714906186, "name": "French bulldog"}]
```

### Knative
```
$ kubectl get ksvc
NAME             URL                                                    LATESTCREATED          LATESTREADY            READY   REASON
imageinception   http://imageinception.default.192.168.199.240.xip.io   imageinception-00001   imageinception-00001   True

$ curl http://imageinception.default.192.168.199.240.xip.io -d 'https://clubimg.club.vmall.com/pic/2017/01/25/56fe4ab0aa41def434824d3302b44a26_IMG_20170125_153114.jpg'

[{"score": 0.6955435276031494, "name": "tabby"}, {"score": 0.1721213459968567, "name": "tiger cat"}, {"score": 0.06431407481431961, "name": "Egyptian cat"}, {"score": 0.0029729718808084726, "name": "lynx"}, {"score": 0.0020706052891910076, "name": "tiger"}, {"score": 0.0010852533159777522, "name": "doormat"}, {"score": 0.0009471490629948676, "name": "zebra"}, {"score": 0.00035808392567560077, "name": "window screen"}, {"score": 0.0003420915163587779, "name": "Persian cat"}, {"score": 0.0003204822714906186, "name": "French bulldog"}]

```
