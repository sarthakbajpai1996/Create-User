aws cloudformation package --s3-bucket {bucket-name} --s3-prefix iam --template-file ./Create_User/create_api_role.yaml --output-template-file api-iam-role-packaged.yaml && ^
aws cloudformation deploy --s3-bucket {bucket-name} --s3-prefix iam --stack-name API-IAM-Stack --capabilities CAPABILITY_NAMED_IAM --template-file api-iam-role-packaged.yaml

aws cloudformation package --s3-bucket {bucket-name} --s3-prefix iam --template-file ./Create_User/create_lambda_role.yaml --output-template-file api-iam-role-packaged.yaml && ^
aws cloudformation deploy --s3-bucket {bucket-name} --s3-prefix iam --stack-name Lambda-IAM-Stack --capabilities CAPABILITY_NAMED_IAM --template-file api-iam-role-packaged.yaml