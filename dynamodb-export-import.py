#!/usr/bin/python3

import boto3
clientDynamoDB = boto3.client('dynamodb')
allItems = clientDynamoDB.scan(
    TableName='backend1',
    Limit=5000
)
for eachItem in allItems['Items']:
    clientDynamoDB.put_item(
        TableName='backend2',
        Item = eachItem
    )
