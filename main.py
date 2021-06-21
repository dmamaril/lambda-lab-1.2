import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')

aws lambda create-function --function-name student1002-lab2 \
--zip-file fileb://function.zip --handler main.lambda_handler --runtime python3.7 \
--role arn:aws:iam::994185329081:role/student1002-lambda-cli-role

wyNFJpk5BdV1QhJVpzFU9d0O6rR3241QtdobX7bz

{
    "FunctionName": "student1002-lab2",
    "FunctionArn": "arn:aws:lambda:us-east-2:994185329081:function:student1002-lab2",
    "Runtime": "python3.7",
    "Role": "arn:aws:iam::994185329081:role/student1002-lambda-cli-role",
    "Handler": "main.lambda_handler",
    "CodeSize": 373,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2021-06-21T16:58:54.501+0000",
    "CodeSha256": "juZXyDT+p+2JUHOjbRty7xp5VaFpOqBckmiperOt+lo=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "0b9c1f8c-a7bd-44aa-927b-a5fe07262159",
    "State": "Active",
    "LastUpdateStatus": "Successful",
    "PackageType": "Zip"
}

aws lambda invoke --function-name student1002-lab2 --log-type Tail \
--cli-binary-format raw-in-base64-out \
--payload '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
outputfile.txt