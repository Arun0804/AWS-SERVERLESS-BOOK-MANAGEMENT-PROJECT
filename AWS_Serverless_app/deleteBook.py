import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookData')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except Exception:
        return {"statusCode": 400, "body": json.dumps("Invalid request body")}

    book_id = body.get("bookid")

    if not book_id:
        return {
            "statusCode": 400,
            "body": json.dumps("bookid is required to delete a record")
        }

    try:
        table.delete_item(
            Key={"bookid": book_id}
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps("Delete failed: " + str(e))
        }

    return {
        "statusCode": 200,
        "body": json.dumps("Book deleted successfully")
    }
