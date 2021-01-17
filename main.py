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


@app.route('/download_lottery_result', methods=['GET'])
def download_lottery_result():
    LOTTO_URL = 'https://www.pais.co.il/Lotto/lotto_resultsDownload.aspx'
    proxy = {
        "http": 'http://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
        "https": 'https://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
    }
    res = requests.get(LOTTO_URL, proxies=proxy)
    data = res.text.split('\r\n')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('results')
    data.pop(0)
    for row in data:
        row_data = row.split(',')
        table.put_item(
            Item={
                'id': int(row_data[0]),
                'date': row_data[1],
                'numbers': [row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7]],
                'strong_number': row_data[8],
                'form_kind': 'lotto',
            }
        )
    return 200


@app.route('/download_chance_result', methods=['GET'])
def download_chance_result():
    LOTTO_URL = 'https://www.pais.co.il/chance/chance_resultsDownload.aspx'
    proxy = {
        "http": 'http://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
        "https": 'https://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
    }
    res = requests.get(LOTTO_URL, proxies=proxy)
    data = res.text.split('\r\n')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Chance_Results')
    data.pop(0)
    for row in data:
        row_data = row.split(',')
        table.put_item(
            Item={
                'id': int(row_data[1]),
                'date': row_data[0],
                'numbers': [row_data[2], row_data[3], row_data[4], row_data[5]],
                'form_kind': 'chance',
            }
        )
    return 200


@app.route('/download_777_result', methods=['GET'])
def download_777_result():
    LOTTO_URL = 'https://www.pais.co.il/777/777_resultsDownload.aspx'
    proxy = {
        "http": 'http://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
        "https": 'https://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
    }
    res = requests.get(LOTTO_URL, proxies=proxy)
    data = res.text.split('\r\n')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('777_Results')
    data.pop(0)
    for row in data:
        row_data = row.split(',')
        table.put_item(
            Item={
                'id': int(row_data[1]),
                'date': row_data[0],
                'numbers': [row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7],
                            row_data[8], row_data[9], row_data[10], row_data[11], row_data[12], row_data[13],
                            row_data[14], row_data[15], row_data[16], row_data[17], row_data[18]
                            ],
                'form_kind': '777',
            }
        )
    return 200

@app.route('/download_123_result', methods=['GET'])
def download_123_result():
    LOTTO_URL = 'https://www.pais.co.il/123/123_resultsDownload.aspx'
    proxy = {
        "http": 'http://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
        "https": 'https://user-dekelev-sessionduration-30:dekel123@il.smartproxy.com:30001',
    }
    res = requests.get(LOTTO_URL, proxies=proxy)
    data = res.text.split('\r\n')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('123_Results')
    data.pop(0)
    for row in data:
        row_data = row.split(',')
        table.put_item(
            Item={
                'id': int(row_data[1]),
                'date': row_data[0],
                'numbers': [row_data[2], row_data[3], row_data[4]],
                'form_kind': '123',
            }
        )
    return 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
