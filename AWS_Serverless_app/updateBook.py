import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookData')

def lambda_handler(event, context):
    # Parse body for API Gateway Proxy
    try:
        body = json.loads(event.get("body", "{}"))
    except Exception:
        return {"statusCode": 400, "body": json.dumps("Invalid request body")}

    book_id = body.get("bookid")
    title = body.get("title")
    author = body.get("author")
    year = body.get("year")

    if not book_id:
        return {
            "statusCode": 400,
            "body": json.dumps("bookid is required to update a record")
        }

    # Build update expression dynamically
    update_expr = []
    expr_attr_vals = {}

    if title:
        update_expr.append("title = :t")
        expr_attr_vals[":t"] = title

    if author:
        update_expr.append("author = :a")
        expr_attr_vals[":a"] = author

    if year:
        update_expr.append("year = :y")
        expr_attr_vals[":y"] = year

    if not update_expr:
        return {
            "statusCode": 400,
            "body": json.dumps("No attributes provided for update")
        }

    update_expression = "SET " + ", ".join(update_expr)

    try:
        table.update_item(
            Key={"bookid": book_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expr_attr_vals
        )
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps("Update failed: " + str(e))
        }

    return {
        "statusCode": 200,
        "body": json.dumps("Book updated successfully")
    }
