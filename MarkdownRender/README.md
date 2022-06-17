# functions/MarkdownRender

This function renders the markdown statement to html statement

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
$ faas-cli describe markdown
Name:                markdown
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    /usr/bin/MarkdownRender
URL:                 http://192.168.50.23:31112
/function/markdown
Async URL:           http://192.168.50.23:31112
/async-function/markdown

$ curl http://192.168.50.23:31112
/function/markdown -d "### yuxiaoba"
<h3>yuxiaoba</h3>
```

### Knative
```
$ kubectl get ksvc
NAME             URL                                                    LATESTCREATED          LATESTREADY            READY   REASON
markdown         http://markdown.default.192.168.199.240.xip.io         markdown-00001         markdown-00001         True

$ curl http://markdown.default.192.168.199.240.xip.io -d "### yuxiaoba"
<h3>yuxiaoba</h3>
```
