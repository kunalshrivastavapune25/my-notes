$Bucket = "kunal-cfn-templates"
$StackName = "my-nested-stack"

# Upload child templates
aws s3 cp network.yml s3://$Bucket/network.yml
aws s3 cp lambda.yml  s3://$Bucket/lambda.yml

# Deploy parent stack
aws cloudformation deploy `
  --template-file parent.yml `
  --stack-name $StackName `
  --capabilities CAPABILITY_NAMED_IAM `
  --no-fail-on-empty-changeset
