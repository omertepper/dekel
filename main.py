import boto3
import urllib3
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = request.data
    print(data)
    return 'Hello, World!'


@app.route('/download_result', methods=['GET'])
def download_result():
    print('in')
    LOTTO_URL = 'https://www.pais.co.il/Lotto/lotto_resultsDownload.aspx'
    res = requests.get(LOTTO_URL)
    data = res.text.split('\r\n')
    print(data)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('results')
    for row in data:
        table.put_item(
            Item={
                'id': row[0],
                'date': row[1],
                'numbers': [row[2], row[3], row[4], row[5], row[6], row[7]],
                'strong_number': row[8],
                'form_kind': 'lotto',
            }
        )
    return 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
