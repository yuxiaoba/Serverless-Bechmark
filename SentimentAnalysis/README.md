## SentimentAnalysis

Python function provides a rating on sentiment positive/negative (polarity -1.0-1.0) and subjectivity to provided to each of the sentences sent in via the [TextBlob project](http://textblob.readthedocs.io/en/dev/).


## Build function
We download the nltk packages beforehand in the repo ( The [nltk project](http://www.nltk.org/data.html#installing-via-a-proxy-web-server) tells how to download packages online ).

## Deploy function
### Openfaas
```
$ bash openfaas/deploy.sh
```

### Knative 
```
$ bash knative/deploy.sh
```

## Invoke function

### Openfaas
```
$ faas-cli describe sentiment
Name:                sentiment
Status:              Ready
Replicas:            1
Available replicas:  1
Invocations:         0
Image:
Function process:    python handler.py
URL:                 http://192.168.50.23:31112
/function/sentiment
Async URL:           http://192.168.50.23:31112
/async-function/sentiment

$ curl http://192.168.50.23:31112
/function/sentiment -d "The hotel was clean, but the area was terrible"
{"polarity": -0.31666666666666665, "sentence_count": 1, "subjectivity": 0.8500000000000001}

$ curl http://192.168.50.23:31112
function/sentiment -d "Personally I like functions to do one thing and only one thing well, it makes them more readable."
{"polarity": 0.16666666666666666, "sentence_count": 1, "subjectivity": 0.6}
```

### Knative
```
$ kubectl get ksvc
NAME             URL                                                    LATESTCREATED          LATESTREADY            READY   REASON
sentiment        http://sentiment.default.192.168.199.240.xip.io        sentiment-00001        sentiment-00001        True

$ curl http://sentiment.default.192.168.199.240.xip.io -d "The hotel was clean, but the are
a was terrible"
{"polarity": -0.31666666666666665, "sentence_count": 1, "subjectivity": 0.8500000000000001}

$ curl http://sentiment.default.192.168.199.240.xip.io -d "Personally I like functions to do one thing and only one thing well, it makes them more readable."
{"polarity": 0.16666666666666666, "sentence_count": 1, "subjectivity": 0.6}

$ curl http://sentiment.default.192.168.199.240.xip.io -d "Functions are great and proven to be awesome"
{"polarity": 0.9, "sentence_count": 1, "subjectivity": 0.875}
```
