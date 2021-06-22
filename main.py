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

test

aws lambda update-function-code --function-name student1002-github-webhook2 \
--zip-file fileb://function.zip

{
    "FunctionName": "student1002-github-webhook2",
    "FunctionArn": "arn:aws:lambda:us-east-2:994185329081:function:student1002-github-webhook2",
    "Runtime": "python3.7",
    "Role": "arn:aws:iam::994185329081:role/student1002-lambda-cli-role",
    "Handler": "webhook.post",
    "CodeSize": 5635243,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2021-06-21T19:59:03.448+0000",
    "CodeSha256": "aKVdMZwLqYWSgroeRNpcyfFDHWKpWQmjz5f2Z40dEJc=",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "19eb4d9c-0f29-4ff8-bab1-b9038177fbec",
    "State": "Active",
    "LastUpdateStatus": "Successful",
    "PackageType": "Zip"
}

aws lambda update-function-configuration --function-name student1002-github-webhook2 \
--timeout 300

aws lambda update-function-configuration --function-name student1002-github-webhook2 \
--memory 512

echo '{
    "Version": "2012-10-17",
    "Statement": [{
        "Action": [
            "s3:GetObject",
            "s3:ListBucket",
            "s3:GetBucketLocation",
            "s3:PutObject",
            "s3:DeleteObject"
        ],
        "Resource": [
            "arn:aws:s3:::student1002-aws-hugo-1",
            "arn:aws:s3:::student1002-aws-hugo-1/*"
        ],
        "Effect": "Allow"
    }]
}' > /tmp/role-policy.json

aws iam put-role-policy --role-name student1002-lambda-cli-role --policy-name AllowLambdaS3 --policy-document file:///tmp/role-policy.json

aws lambda update-function-configuration --function-name student1002-github-webhook2 --environment "Variables={output_bucket=student1002-aws-hugo-1,github_secrets=secretsecret}"

aws lambda create-function --function-name student1002-comments-post \
--zip-file fileb://function.zip --handler comments.post --runtime python3.7 \
--role arn:aws:iam::994185329081:role/student1002-lambda-cli-role

aws lambda create-function --function-name student1002-comments-get \
--zip-file fileb://function.zip --handler comments.get --runtime python3.7 \
--role arn:aws:iam::994185329081:role/student1002-lambda-cli-role

aws lambda create-function --function-name student1002-dynamo-stream \
--zip-file fileb://function.zip --handler dynamo_stream.fake_webhook --runtime python3.7 \
--role arn:aws:iam::994185329081:role/student1002-lambda-cli-role


aws lambda update-function-code --function-name student1002-comments-post \
--zip-file fileb://function.zip

aws lambda update-function-code --function-name student1002-comments-get \
--zip-file fileb://function.zip

aws lambda update-function-code --function-name student1002-dynamo-stream \
--zip-file fileb://function.zip


aws dynamodb create-table --table-name student1002-comments --attribute-definitions AttributeName=uuid,AttributeType=S --key-schema AttributeName=uuid,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "uuid",
                "AttributeType": "S"
            }
        ],
        "TableName": "student1002-comments",
        "KeySchema": [
            {
                "AttributeName": "uuid",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "CREATING",
        "CreationDateTime": "2021-06-21T15:22:39.825000-07:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:us-east-2:994185329081:table/student1002-comments",
        "TableId": "47195592-6685-45ca-bdd1-e5a923a0d45e"
    }
}

aws lambda update-function-configuration --function-name student1002-comments-get --environment "Variables={table_name=student1002-comments}" 
aws lambda update-function-configuration --function-name student1002-comments-get --environment "Variables={table_name=student1002-comments}" 
aws lambda update-function-configuration --function-name student1002-comments-post --environment "Variables={table_name=student1002-comments}" 

aws lambda update-function-configuration --function-name student1002-dynamo-stream --environment "Variables={webhook_function=student1002-github-webhook2,full_name=dmamaril/lambda-lab-1.2,clone_url=https://github.com/dmamaril/lambda-lab-1.2.git}"
aws lambda update-function-configuration --function-name student1002-github-webhook2 --environment "Variables={comment_function=student1002-comments-get}"

aws lambda update-function-code --function-name student1002-github-webhook2 \
--zip-file fileb://function.zip

aws iam put-role-policy --role-name student1002-lambda-cli-role --policy-name FullAccess --policy-document file:///tmp/new-policy.json

aws lambda update-function-code --function-name student1002-comments-get \
--zip-file fileb://function.zip


## LAB 2.1
sam init --runtime python3.7
aws s3 mb s3://student1002-sam-deploy
sam package --output-template-file packaged.yaml --s3-bucket student1002-sam-deploy
sam deploy --template-file packaged.yaml --stack-name student1002-sam-app --capabilities CAPABILITY_IAM

---------------------------------------------------------------------------------------
|                                   DescribeStacks                                    |
+-------------+-----------------------------------------------------------------------+
|  Description|  API Gateway endpoint URL for Prod stage for Hello World function     |
|  OutputKey  |  HelloWorldApi                                                        |
|  OutputValue|  https://30q5fnqwj7.execute-api.us-east-2.amazonaws.com/Prod/hello/   |
+-------------+-----------------------------------------------------------------------+

## LAB 2.2
sam build --use-container 
 sam package --output-template-file packaged.yaml --s3-bucket student1002-sam-deploy
 sam deploy --template-file packaged.yaml --stack-name student1002-blog-stack --capabilities CAPABILITY_IAM


## OUTPUT
CloudFormation outputs from deployed stack
------------------------------------------------------------------------------------------------------------------------------
Outputs
------------------------------------------------------------------------------------------------------------------------------
Key                 Student00CommentsPostSAM
Description         CommentsPost Lambda Function ARN
Value               arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00CommentsPostSAM-
oKbAdUYrQ8Yl

Key                 Student00GithubWebhookSAM
Description         GithubWebhook Lambda Function ARN
Value               arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00GithubWebhookSAM-
Xh4sywmohSXF

Key                 Student00CommentsGetSAM
Description         CommentsGet Lambda Function ARN
Value               arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00CommentsGetSAM-
sh5BjpN8x5pk

Key                 HugoBlogWebhook
Description         API Gateway endpoint URL for Prod stage for Hugo static site github webhook
Value               https://qbd70vt420.execute-api.us-east-2.amazonaws.com/Prod/webhook/

Key                 WebsiteURL
Description         URL for website hosted on S3
Value               http://student1002-blog-stack-student00hugositebucket-1sbbmjryzvcmj.s3-website.us-east-2.amazonaws.com

Key                 HugoBlogComments
Description         API Gateway endpoint URL for Prod stage for Hugo static site github webhook
Value               https://qbd70vt420.execute-api.us-east-2.amazonaws.com/Prod/comments/
------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                                                                       DescribeStacks                                                                                                       |
+------------------------------------------------------------------------------+----------------------------+----------------------------------------------------------------------------------------------------------------+
|                                  Description                                 |         OutputKey          |                                                  OutputValue                                                   |
+------------------------------------------------------------------------------+----------------------------+----------------------------------------------------------------------------------------------------------------+
|  CommentsPost Lambda Function ARN                                            |  Student00CommentsPostSAM  |  arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00CommentsPostSAM-oKbAdUYrQ8Yl   |
|  GithubWebhook Lambda Function ARN                                           |  Student00GithubWebhookSAM |  arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00GithubWebhookSAM-Xh4sywmohSXF  |
|  CommentsGet Lambda Function ARN                                             |  Student00CommentsGetSAM   |  arn:aws:lambda:us-east-2:994185329081:function:student1002-blog-stack-Student00CommentsGetSAM-sh5BjpN8x5pk    |
|  API Gateway endpoint URL for Prod stage for Hugo static site github webhook |  HugoBlogWebhook           |  https://qbd70vt420.execute-api.us-east-2.amazonaws.com/Prod/webhook/                                          |
|  URL for website hosted on S3                                                |  WebsiteURL                |  http://student1002-blog-stack-student00hugositebucket-1sbbmjryzvcmj.s3-website.us-east-2.amazonaws.com        |
|  API Gateway endpoint URL for Prod stage for Hugo static site github webhook |  HugoBlogComments          |  https://qbd70vt420.execute-api.us-east-2.amazonaws.com/Prod/comments/                                         |
+------------------------------------------------------------------------------+----------------------------+----------------------------------------------------------------------------------------------------------------+

test