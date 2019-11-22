#!flask/bin/python
from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def payment():
    dataFromURL = request.form
    if dataFromURL['payment_response']:
        print("Your Order:" + dataFromURL['orderNumber'] + ", Mount:" + dataFromURL['amount'] + ", has paid successful")
        return "Your Order:" + dataFromURL['orderNumber'] + ", Mount:" + dataFromURL['amount'] + ", has paid successful"
    else:
        print("Sorry, Your Order:" + dataFromURL['orderNumber'] + " , Mount:" + dataFromURL['amount'] + " , failed")
        return "Sorry, Your Order:" + dataFromURL['orderNumber'] + " , Mount:" + dataFromURL['amount'] + " , failed"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
