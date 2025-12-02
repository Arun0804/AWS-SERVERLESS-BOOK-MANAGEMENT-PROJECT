import json
import boto3

def lambda_handler(event, context):
    """
    Fetch all books from the bookData table.
    Returns a JSON array of book objects.
    """

    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

    # Select the DynamoDB table named 'bookData'
    table = dynamodb.Table('bookData')

    # Scan the table to retrieve all items
    response = table.scan()
    data = response.get('Items', [])

    # Handle pagination if there are more items
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response.get('Items', []))

    # For non-proxy integration, you can just 'return data'
    # But to be consistent with HTTP-style responses:
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
