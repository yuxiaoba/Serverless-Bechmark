# functions/image inception

![](./qrcode.png)

This function uses the skip2/go-qrcode Go library to generate a QR Code for a string.

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


### Faasd

```
$ faas-cli describe qrcode
Name:                qrcode
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    /usr/bin/qrcode
URL:                 http://192.168.50.23:31112
/function/qrcode
Async URL:           http://192.168.50.23:31112
/async-function/qrcode

$ curl http://http://192.168.50.23:31112
/function/qrcode -d "yuxiaoba" > qrcode.png
```

### Knative
```
$ kubectl get ksvc
NAME             URL                                                    LATESTCREATED          LATESTREADY            READY   REASON
qrcode           http://qrcode.default.192.168.199.240.xip.io           qrcode-00001           qrcode-00001           True

$ curl http://qrcode.default.192.168.199.240.xip.io -d "yuxiaoba" > qrcode.png
```
