This work is a forked version of the work by [Magnus Erik Hvass Pedersen](https://github.com/Hvass-Labs/TensorFlow-Tutorials) 'Inception Model.
We re-packaged it as an [Knative](https://knative.dev) serverless function.

## Deploy and test example
```
$ kubectl apply -f deploy.yaml

$ kubectl get ksvc
NAME                URL                                        LATESTCREATED             LATESTREADY               READY   REASON  
image-recognition   http://image-recognition.default.dds.com   image-recognition-bf8zf   image-recognition-bf8zf   True  

$ curl http://image-recognition.default.dds.com?imageUrl=https://upload.wikimedia.org/wikipedia/commons/6/61/Humpback_Whale_underwater_shot.jpg
[{"score": 0.5343282222747803, "name": "great white shark"}, {"score": 0.09276451915502548, "name": "tiger shark"}, {"score": 0.058990731835365295, "name": "grey whale"}, {"score": 0.05105867236852646, "name": "sea lion"}, {"score": 0.01991075649857521, "name": "hammerhead"}]
```
