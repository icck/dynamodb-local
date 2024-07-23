import boto3

dynamodb = boto3.client("dynamodb", endpoint_url="http://localhost:8000")

if __name__ == "__main__":

    item = dynamodb.get_item(
        TableName="cli-table",
        Key={"id": {"S": "1"}},
    )
    print(item["Item"])