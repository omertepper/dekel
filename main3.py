import json
import csv
import urllib3
import boto3


def lambda_handler(event, context):
    LOTTO_URL = 'https://www.pais.co.il/Lotto/lotto_resultsDownload.aspx'
    http = urllib3.PoolManager()
    r = http.request('GET', LOTTO_URL)
    r = r.data
    r = r.decode('ISO-8859-1')
    csv_data = r.splitlines()
    csv_data.pop(0)
    print(csv_data)
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('results')
    # for row in csv_data:
    #     table.put_item(
    #         Item={
    #             'id':row[0],
    #             'date': csv[1] ,
    #             'numbers': [csv[2],csv[3],csv[4],csv[5],csv[6],csv[7]],
    #             'strong_number': csv[8],
    #             'form_kind':'lotto' ,
    #         }
    #     )

if __name__ == '__main__':
    lambda_handler(None,None)