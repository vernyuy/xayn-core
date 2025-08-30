import boto3
from botocore.exceptions import ClientError

class DynamoDBHelper:
    def __init__(self, table_name, region_name="us-east-1"):
        self.table_name = table_name
        self.dynamodb = boto3.resource("dynamodb", region_name=region_name)
        self.table = self.dynamodb.Table(table_name)

    def put_item(self, item: dict):
        try:
            self.table.put_item(Item=item)
            return {"status": "success", "item": item}
        except ClientError as e:
            return {"status": "error", "message": str(e)}

    def get_item(self, key: dict):
        try:
            response = self.table.get_item(Key=key)
            return response.get("Item")
        except ClientError as e:
            return {"status": "error", "message": str(e)}

    def delete_item(self, key: dict):
        try:
            self.table.delete_item(Key=key)
            return {"status": "success", "deleted_key": key}
        except ClientError as e:
            return {"status": "error", "message": str(e)}

    def scan_items(self, limit=10):
        try:
            response = self.table.scan(Limit=limit)
            return response.get("Items", [])
        except ClientError as e:
            return {"status": "error", "message": str(e)}
