# -*- coding: utf-8 -*-
#!/bin/python
#########
## QR code generator for in-store kiosk
#########

from flask import Flask, send_file
from flask import request
import qrcode
import json
import uuid
import requests
import os

DECODE_SERVICE = os.environ.get('DECODE_SERVICE', 'http://127.0.0.1:9080')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def encode():
    # request params to dict
    print(request.form)
    product = request.form.getlist('Product')
    product = list(map(int, product))
    amount = request.form.get('mount')
    dataFromURL = {
        'productIds': product,
        'amount': amount,
    }
    dataFromURL.update({'system': "SYSU DDS Serverless Benchmark"})
    dataFromURL.update({'orderNumber': str(uuid.uuid1())})
    print(dataFromURL)
    # transaction total
    try:
        img = qrcode.make(json.dumps(dataFromURL))
        img.save('./test.jpeg', 'JPEG', quality=70)
        file = open(r'./test.jpeg', mode='rb')
        data = {
            'file': file
        }
        requests.post(f'{DECODE_SERVICE}', files=data)
        return send_file('./test.jpeg', mimetype='image/jpeg')
    except Exception as e:
        return "Error generating QR code for this transaction."


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
