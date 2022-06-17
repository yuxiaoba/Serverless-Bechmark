# functions/resizer

![](./gordon.png)  ![](./small_gordon.png)  

Use this FaaS function to resize an image with ImageMagick.

## Deploy the resizer function

### openfaas
```
$ bash ./openfaas/deploy.sh
$ faas-cli describe resizeimage
Name:                resizeimage
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    convert - -resize 50% fd:1
URL:                 http://127.0.0.1:8080/function/resizeimage
Async URL:           http://127.0.0.1:8080/async-function/resizeimage
```

### Knative
```
$ bash ./knative/deploy.sh
$ kubectl get ksvc
NAME            URL                                                   LATESTCREATED         LATESTREADY           READY   REASON
resizeimage     http://resizeimage.default.192.168.199.240.xip.io     resizeimage-00001     resizeimage-00001     True

```

## Invoke Function

Now pick an image such as the included picture of Gordon and use `curl` or a tool of your choice to send the data to the function. Pipe the result into a new file like this:

### Faasd

```
$ faas-cli describe resizeimage
Name:                resizeimage
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    convert - -resize 50% fd:1
URL:                 http://192.168.50.23:31112
/function/resizeimage
Async URL:           http://192.168.50.23:31112
/async-function/resizeimage

$ curl http://192.168.50.23:31112
/function/resizeimage --data-binary "@/root/faasbenchmark/ResizeImage/gordon.png" > small_gordon.png
```

### Knative
```
$ kubectl get ksvc
NAME            URL                                                   LATESTCREATED         LATESTREADY           READY   REASON
resizeimage     http://resizeimage.default.192.168.199.240.xip.io     resizeimage-00001     resizeimage-00001     True

$ curl http://resizeimage.default.192.168.199.240.xip.io --data-binary "@/root/faasbenchmark/ResizeImage/gordon.png" > small_gordon.png
```
