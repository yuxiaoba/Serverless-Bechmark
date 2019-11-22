#!flask/bin/python
from flask import Flask
import requests
import os
import random
import time

ENCODE_SERVICE = os.environ.get('ENCODE_SERVICE', 'http://127.0.0.1:8080')


app = Flask(__name__)


@app.route('/')
def product_select():
    # Simulate the commodity selection process
    time.sleep(random.randint(10, 20))
    productNum = random.randint(1, 10)
    product = []
    mount = 0
    for i in range(productNum):
        product.append(random.randint(1, 100))
        mount += random.randint(1, 1000)
    data = {
        'Product': product,
        'mount': mount,
    }
    print(data)
    requests.post(f'{ENCODE_SERVICE}', data=data)

    return "Select Products amd Pay for them  Successfully"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

