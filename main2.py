import json

import requests

if __name__ == '__main__':
    url = "https://secure.cardcom.solutions/Interface/BillGoldService.asmx"
    # params = {
    #     # 'codepage': 65001,
    #     'Operation': 2,
    #     'TerminalNumber': 1000,
    #     'UserName': 'MyTestUser',
    #     'SumToBill': 100,
    #     'CoinID': 1,
    #     'Language': 'he',
    #     'ProductName': 'C101G',
    #     'APILevel': 10,
    #     'MaxNumOfPayments': 12,
    #     'MinNumOfPayments': 3,
    #     'SuccessRedirectUrl': 'http://lotto-matic.com/',
    #     'ErrorRedirectUrl': 'http://lotto-matic.com/',
    #     'IndicatorUrl': 'http://ec2-34-199-57-225.compute-1.amazonaws.com:6000/',
    # }
    # res = requests.post(url, json=params)
    # # res = requests.post("https://secure.cardcom.solutions/Interface/LowProfile.aspx", data=json.dumps(params))
    # print(res.text)
    body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CreateLowProfileDeal xmlns="BillGoldService">
      <terminalnumber>1000</terminalnumber>
      <username>barak9611</username>
      <lowprofileParams>
        <Operation>BillAndCreateToken</Operation>
        <ReturnValue>string</ReturnValue>
        <SumToBill>100.56</SumToBill>
        <CoinID>1</CoinID>
        <Languge>he</Languge>
        <ProductName>C101G</ProductName>
        <APILevel>10</APILevel>
        <SuccessRedirectUrl>http://lotto-matic.com/</SuccessRedirectUrl>
        <ErrorRedirectUrl>http://lotto-matic.com/</ErrorRedirectUrl>
        <IndicatorUrl>http://ec2-34-199-57-225.compute-1.amazonaws.com:6000/</IndicatorUrl>
      </lowprofileParams>
    </CreateLowProfileDeal>
  </soap:Body>
</soap:Envelope>"""
    response = requests.post(url, data=body, headers={'content-type': 'text/xml'})
    print(response.content.decode())