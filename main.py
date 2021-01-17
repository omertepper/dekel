import urllib3
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = request.data
    print(data)
    return 'Hello, World!'


@app.route('/download_result', methods=['GET'])
def download_result():
    LOTTO_URL = 'https://www.pais.co.il/Lotto/lotto_resultsDownload.aspx'
    http = urllib3.PoolManager()
    r = http.request('GET', LOTTO_URL)
    print(r.status)
    return 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
