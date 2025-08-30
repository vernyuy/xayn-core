import json
from aws_helper import DynamoDBHelper, S3Helper

# Initialize DynamoDB and S3 helpers
dynamodb = DynamoDBHelper(table_name="MyTable")
s3 = S3Helper(bucket_name="my-s3-bucket")

def lambda_handler(event, context):
    # Log the event for debugging
    print(f"Received event: {json.dumps(event)}")

    # Example: Retrieve item from DynamoDB (you can customize this)
    item_key = {"id": event.get("id", "default-id")}
    dynamo_response = dynamodb.get_item(item_key)
    
    if "Item" in dynamo_response:
        message = f"Item found: {dynamo_response['Item']}"
    else:
        message = f"Item not found. Adding new item."
        new_item = {"id": item_key["id"], "name": "New Item"}
        dynamo_response = dynamodb.put_item(new_item)

    # Example: Upload a file to S3 (can be triggered based on event)
    file_name = f"{item_key['id']}_file.txt"
    s3_response = s3.upload_file("/tmp/local-file.txt", file_name)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "s3_upload_status": s3_response,
            "dynamo_response": dynamo_response
        }),
    }
