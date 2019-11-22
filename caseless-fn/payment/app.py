#!flask/bin/python
from flask import Flask, request
import json
import requests
import os
import time
import random

PHONE_SERVICE = os.environ.get('PHONE_SERVICE', 'http://127.0.0.1:9098')


def stripePayment(orderNumber='0000', inputAmount=0,  email="user@example.com",
                   responseCode= False, method='Alipay', currency="CNY"):
    data = {
        'orderNumber': orderNumber,
        'amount': inputAmount,
        'currency': currency,
        'payment_method_types': method,
        'receipt_email': email,
        'payment_response': responseCode,
    }
    requests.post(f'{PHONE_SERVICE}', data=data)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def payment():
    # Simulate the commodity payment process
    time.sleep(random.randint(5, 10))
    dataFromURL = request.data
    data = json.loads(bytes.decode(dataFromURL))
    orderNumber = data['orderNumber']
    amount = data['amount']
    email = "serverless-demo@sysu.dds.com"

    if _validateRequest(data):
        stripePayment(orderNumber, amount, email, True)
        return "Pay Successful"

    else:
        stripePayment(orderNumber, amount, email, False)
        return "{'errorMessage': 'Invalid payload for payment request. %s'}" % data


def _validateRequest(req_data):
    if 'orderNumber' in req_data and 'amount' in req_data:
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

