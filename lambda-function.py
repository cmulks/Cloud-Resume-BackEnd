import json
import boto3

def lambda_handler(event, context):
    # connect to DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    
    # create a DynamoDB client to visitor_count table
    table = dynamodb.Table('visitor_count')
    
    # increment visitor_count attribute for index.html key
    table.update_item(
        Key={
            'path': 'index.html'
        },
        UpdateExpression='SET visitor_count = visitor_count + :inc',
        ExpressionAttributeValues={
            ':inc': 1
        }
    )
    
    # get updated visitor_count based on index.html key
    response = table.get_item(
        Key={
            'path': 'index.html'
        }
    )
    visitor_count = response['Item']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers' : {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
