import json
import boto3

# Create a DynamoDB resource using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Select the DynamoDB table
table = dynamodb.Table('bookData')

# Lambda handler
def lambda_handler(event, context):
    """
    Handles inserting a book record into the bookData table.
    Supports both:
    - direct mapping (event is already a dict with fields)
    - API Gateway proxy integration (event['body'] is JSON string)
    """

    # Handle API Gateway proxy format
    if "body" in event:
        try:
            body = json.loads(event["body"])
        except Exception:
            return {
                "statusCode": 400,
                "body": json.dumps("Invalid JSON body")
            }
    else:
        # Direct mapping (like in the original tutorial)
        body = event

    # Extract values
    book_id = body.get("bookid")
    title = body.get("title")
    author = body.get("author")
    year = body.get("year")

    # Basic validation
    if not title or not author:
        return {
            "statusCode": 400,
            "body": json.dumps("Both 'title' and 'author' are required.")
        }

    # Write book data to DynamoDB
    response = table.put_item(
        Item={
            "bookid": book_id if book_id else f"book-{title}-{author}",
            "title": title,
            "author": author,
            "year": str(year) if year is not None else ""
        }
    )

    # Return a properly formatted JSON object
    return {
        "statusCode": 200,
        "body": json.dumps("Book data saved successfully!")
    }
