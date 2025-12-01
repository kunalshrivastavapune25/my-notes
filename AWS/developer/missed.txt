
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

1. As a developer, you have created a Lambda function that is used to work with a bucket in Amazon S3. The Lambda function is not working as expected. You need to debug the issue and understand what’s the underlying issue. How can you accomplish this in an easily understandable way?
 Use AWS Cloudwatch metrics
 Use AWS CloudWatch logs 
 Set the Lambda function debugging level to verbose
 Use AWS Cloudtrail logs
 
Answer – B
You can insert logging statements into your code to help you validate that your code is working as expected. Lambda automatically integrates with Amazon CloudWatch Logs and pushes all logs from your code to a CloudWatch Logs group associated with a Lambda function (/aws/lambda/).

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

2. Question
Your company is planning on using the Simple Storage service to host objects that will be accessed by users. There is a speculation that there would be roughly 6000 GET requests per second. Which of the following could be used to ensure optimal performance? Choose 2 answers from the options given below?
 Use a Cloudfront distribution in front of the S3 bucket
 Use sequential date-based naming for your prefixes.
 Enable versioning for the objects
 Enable Cross Region Replication for the bucket

Answer – A,B 
 ✅ A. Use a CloudFront distribution in front of the S3 bucket
CloudFront helps cache frequently accessed objects at edge locations, reducing the number of direct requests to the S3 bucket and improving performance by serving content closer to users. This significantly reduces latency and enhances scalability.
CloudFront reduces the load on S3 by serving cached content, improving scalability and performance.
✅ B. Use sequential date-based naming for your prefixes
AWS S3 performance best practices recommend using random prefixes instead of sequential date-based naming to avoid performance bottlenecks. However, if prefixes are distributed evenly (e.g., using hashed or partitioned keys), this can improve request distribution across partitions in S3, ensuring optimal performance for high request rates.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

3. Question
You have the following YAML file given to you which is required to deploy a Lambda function using serverless deployment.

AWSTemplateFormatVersion: ‘2010-09-09’
Transform: AWS::Serverless-2016-10-31
Resources:
TestFunction:
Type: AWS::Serverless::Function
Properties:
Handler: index.handler
Runtime: nodejs6.10
Environment:
Variables:
S3_BUCKET: demobucket

Which of the following is required to ensure the deployment can take place? Please select 2 correct answers.

 Use the cloudformation package command to package the deployment
 Use the cloudformation package command to deploy the template
 Place the function code at the root level of the working directory along with the YAML file
 Place the function code in the .eb extensions folder

Answer – A and C
The above snippet is used to create a serverless application that is deployed using the serverless deployment language. You need to ensure that the Lambda function is present as part of the deployment package
Option B is incorrect since these are not CloudFormation specific templates
Option D is incorrect since this is normally used for Elastic Beanstalk deployments

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

4. Question
You are developing a Java based application that needs to make use of the AWS KMS service for encryption. Which of the following must be done for the encryption and decryption process? Choose 2 answers from the options given below.

 Use the Customer master key to encrypt the data
 Use the Customer master key to generate a data key for the encryption process
 Use the Customer master key to decrypt the data
 Use the generated data key to decrypt the data

Answer – B and D
The AWS Documentation mentions the following
The AWS Encryption SDK is a client-side encryption library that makes it easier for you to implement cryptography best practices in your application. It includes secure default behaviour for developers who are not encryption experts, while being flexible enough to work for the most experienced users.
Options A and C are incorrect because you should never use the Customer master keys directly for the encryption of decryption process.
In the AWS Encryption SDK, by default, you generate a new data key for each encryption operation
For more information on the Encryption SDK , please refer to the below URL
https://docs.aws.amazon.com/kms/latest/developerguide/programming-top.html

Note:
AWS Docs Says
“When you encrypt your data, your data is protected, but you have to protect your encryption key. One strategy is to encrypt it. Envelope encryption is the practice of encrypting plaintext data with a data key, and then encrypting the data key under another key.
You can even encrypt the data encryption key under another encryption key, and encrypt that encryption key another encryption key. But, eventually, one key must remain in plaintext so you can decrypt the keys and your data. This top-level plaintext key encryption key is known as the master key.”
For more information on the enveloping, please refer to the below URL
https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

5. Question
You have developed a Web based application which makes calls to backend API. Which of the following headers are required by Web browsers to be set up in each API m
thod which has CORS enabled.(Select TWO.)

 Access-Control-Allow-Headers
 Access-Control-Allow-CORS
 Access-Control-Expose-Headers
 Access-Control-Expose-Origin
 Access-Control-Allow-Origin

Correct Answer – A, E
To support CORS, API resource needs to implement an OPTIONS method that can respond to the OPTIONS preflight request with following headers,
Access-Control-Allow-Headers
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Option B, C & D are incorrect as both these headers are not required to included as a part of OPTIONS method.
For more information on enabling CORS on resource using API Gateway, refer to the following URL,
https://docs.aws.amazon.com/apigateway/latest/developerguide/enable-cors-for-resource-using-swagger-importer-tool.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

6. Question
Your application currently points to several Lambda functions in AWS. A change is being made to one of the Lambda functions. You need to ensure that application traffic is shifted slowly from one Lambda function to the other. Which two of the following steps would you carry out?

 Create an ALIAS with the –routing-config parameter
 Update the ALIAS with the –routing-config parameter
 Create a version with the –routing-config parameter
 Update the version with the –routing-config parameter
 Update the function with the - config parameter
Incorrect
Answer – A and B
This is mentioned in the AWS Documentation
By default, an alias points to a single Lambda function version. When the alias is updated to point to a different function version, incoming request traffic in turn instantly points to the updated version. This exposes that alias to any potential instabilities introduced by the new version. To minimize this impact, you can implement the routing-config parameter of the Lambda alias that allows you to point to two different versions of the Lambda function and dictate what percentage of incoming traffic is sent to each version.
Options C and D are incorrect since you need to use ALIAS for this purpose.
Option E is incorrect. Because A & B are the correct ways to achieve the requirement.
For more information on shifting traffic using ALIAS , please refer to the below URL
https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

7. Question
You have created a Lambda State Function which is generating error “ServiceException”, Which of the following is a best practice to handle this exception with a Lambda State Function?

 Use Lambda Catch code with only “ErrorEquals” string.
 Use Lambda Retry code with only “BackoffRate” string
 Use Lambda Retry code with only “ErrorEquals” string.
 Use Lambda Catch code with only “ResultPath” string.
Incorrect
Correct Answer – C
For errors such as “ServiceException”, best practice is to Retry invoking Lambda function. Within a Retry Code “ErrorEquals” field is required string which matches error names & all other fields are optional.
Option A is incorrect as Lambda Catch code is only used after a number of retries are performed by State function.
Option B is incorrect as BackoffRate field is optional in Lambda Retry code & if not specified Default value of 2.0 is considered.
Option D is incorrect as Lambda Catch code is only used after a number of retries are performed by State function. ResultPath is an optional field in a Catch Code, ErrorEquals & Next are required strings.
For more information on troubleshooting Lambda State Function errors, refer to the following URL,
https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-errors.html#amazon-states-language-retrying-after-error

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

8. Question
Your development team is currently working with an application that interacts with the DynamoDB table. Due to the proposed extensive use of the application, the underlying DynamoDB table would undergo a steady growth in size.
Which of the following preferred options should be used for retrieving the data? (Choose 3)

 Use the query operation
 Use the Scan operation
 Use the GetItem API command
 Use the BatchGetItem API command
Incorrect
Answer – A ,C and D
The AWS Documentation mentions the following
If possible, you should avoid using a Scan operation on a large table or index with a filter that removes many results. Also, as a table or index grows, the Scan operation slows. The Scan operation examines every item for the requested values and can use up the provisioned throughput for a large table or index in a single operation. For faster response times, design your tables and indexes so that your applications can use Query instead of Scan. (For tables, you can also consider using the GetItem and BatchGetItem APIs.)
Option B is incorrect since this would cause performance issues as the amount of items starts to increase.
For more information on best practises for the query and scan operation, please refer to the below URL
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

9. Question
You are developing an application that is going to make use of AWS Cognito. The default sign-in and sign-up features of the AWS Cognito service will be used. There is a security requirement to ensure that if the user’s credentials are compromised, then they would need to use a new password.
Which of the following needs to be in place for this? (Choose 2)

 Ensure to create a user pool in AWS Cognito
 Ensure to “Block use” for compromised credentials in the Advanced Security section
 Ensure to “Block use” for compromised credentials in the Basic Security section
 Verify sign-in operation on Cognito using Secure Remote Password
Incorrect
Answer – A and B
This is given in the AWS Documentation

Option C is incorrect since this configuration needs to be done in the Advanced Security section

Option D is incorrect as Currently, Amazon Cognito doesn’t check for compromised credentials for sign-in operations with Secure Remote Password (SRP) flow, which doesn’t send the password during sign-in.
For more information on Cognito User pools, please refer to the below URL
https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-compromised-credentials.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

10. Question
Your team is planning on delivering content to users by using the CloudFront service and an S3 bucket as the source. You need to ensure that a custom value is placed for the amount of time the object is stored in the CloudFront cache.
Which 2 of the following options can be used to fulfil this requirement?

 Configure the origin to add an Expires header field to the object
 Configure the Cloudfront distribution to add an Expires header field to the object
 Specify a value for Minimum TTL in CloudFront cache behaviors
 Specify a value for Minimum TTL in the origin object
Incorrect
Answer – A and C
This is also mentioned in the AWS Documentation
For web distributions, to control how long your objects stay in a CloudFront cache before CloudFront forwards another request to your origin, you can:
Configure your origin to add a Cache-Control or an Expires header field to each object.
Specify a value for Minimum TTL in CloudFront cache behaviors.
Use the default value of 24 hours.

Since this is clearly mentioned in the AWS Documentation , the other options are invalid
For more information on request and response behaviour for Cloudfront with S3, please refer to the below URL
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

11. Question
Through an API, a company‘s fleet of Amazon EC2 instances collects data from millions of consumers. To guarantee high access rates, the servers batch the data, create an object for each user, and upload the objects to an S3 bucket. Customer ID, Server ID, TS-Server (TimeStamp and Server ID), the object‘s size, and a timestamp are the object‘s properties. A developer wishes to locate all items gathered for a particular user during a certain time period.How can the developer accomplish this need after establishing an S3 object created event?

 A. Run an AWS Lambda function in response to the S3 object creation events that creates an Amazon DynamoDB record for every object with the Customer ID as the partition key and the Server ID as the sort key. Retrieve all the records using the Customer ID and Server ID attributes.
 B. Run an AWS Lambda function in response to the S3 object creation events that creates an Amazon Redshift record for every object with the Customer ID as the partition key and TS-Server as the sort key. Retrieve all the records using the Customer ID and TS-Server attributes.
 C. Run an AWS Lambda function in response to the S3 object creation events that creates an Amazon DynamoDB record for every object with the Customer ID as the partition key and TS-Server as the sort key. Retrieve all the records using the Customer ID and TS-Server attributes.
 D. Run an AWS Lambda function in response to the S3 object creation events that creates an Amazon Redshift record for every object with the Customer ID as the partition key and the Server ID as the sort key. Retrieve all the records using the Customer ID and Server ID attributes.
Incorrect
Redshift can‘t be used for storing the object creation and customer details, it is mainly used for Datawarehouse requirements. So any option with Redshift is ruled out. For DynamoDb, User wants to retrieve all records for given customer in a specified time range, so Customer ID has to be a Partition Key and TS Server as sort key to specify the time range. Hence Option C is correct

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

12. Question
A developer is combining an Amazon API Gateway with an AWS Lambda function in order to create an application. When the developer attempts to use the API, he or she gets the following error:Wed Nov 08 01:13:00 UTC 2017 : Method completed with status: 502What is the developer‘s responsibility in resolving the error?

 A. Change the HTTP endpoint of the API to an HTTPS endpoint
 B. Change the format of the payload sent to the API Gateway
 C. Change the format of the Lambda function response to the API call
 D. Change the authorization header in the API call to access the Lambda function
Incorrect
https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/ “The format of the Lambda function‘s response is often the source of these errors. If the format is the problem, then you see a message that looks like this in the logs: Thu Dec 08 01:13:00 UTC 2016 : Execution failed due to configuration error: Malformed Lambda proxy response Thu Dec 08 01:13:00 UTC 2016 : Method completed with status: 502“
Option C is correct

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

13. Question
A business requires security for its current website, which is hosted behind an Elastic Load Balancer. Amazon EC2 instances hosting the website are CPU restricted.How can the website be secured without raising the CPU burden on the Amazon EC2 web servers? (Select two.)

 A. Configure an Elastic Load Balancer with SSL pass-through.
 B. Configure SSL certificates on an Elastic Load Balancer.
 C. Configure an Elastic Load Balancer with a Loadable Storage System.
 D. Install SSL certificates on the EC2 instances.
 E. Configure an Elastic Load Balancer with SSL termination.
Incorrect
https://aws.amazon.com/blogs/aws/elastic-load-balancer-support-for-ssl-termination/ You can now create a highly scalable, load-balanced web site using multiple Amazon EC2 instances, and you can easily arrange for the entire HTTPS encryption and decryption process (generally known as SSL termination) to be handled by an Elastic Load Balancer. Your users can benefit from encrypted communication with very little operational overhead or administrative complexity. Until now, you had to handle the termination process within each EC2 instance. This added to the load on the instance and also required you to install an X.509 certificate on each instance. With this new release, you can simply upload the certificates to your AWS account and well take care of getting them distributed to the load balancers.
Correct Answer is C and E

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

14. Question
A corporation uses Amazon API Gateway and the API Gateway native API key validation to maintain a REST service. Users can now join up for the service through a new registration website that was recently developed by the corporation. The registration page uses CreateApiKey to generate a new API key and sends it to the user. The user receives a 403 Forbidden error when attempting to call the API with this key. Existing API users are unaffected and can continue to utilize it.What changes to the code will allow these additional users to access the API?

 A. The createDeployment method must be called so the API can be redeployed to include the newly created API key.
 B. The updateAuthorizer method must be called to update the API‘s authorizer to include the newly created API key.
 C. The importApiKeys method must be called to import all newly created API keys into the current stage of the API.
 D. The createUsagePlanKey method must be called to associate the newly created API key with the correct usage plan.
Incorrect
Do you have a Usage Plan? if not need to create one. Link you API with Usage Plan. For that add a stage, it will link your API. Do you have API Key? if not you need to create an API Key and enable it. Add the Usage Plan which is linked with your API to this API Key. For that add Usage Plan. + https://stackoverflow.com/questions/39061041/using-an-api-key-in-amazon-api-gateway

Correct Option is D

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

15. Question
A developer is developing a website that will be hosted on Amazon‘s S3 service. Secure browser connections must be supported by the website.Which steps must the developer perform in combination to satisfy this requirement? (Select two.)

 A. Create an Elastic Load Balancer (ELB). Configure the ELB to direct traffic to the S3 bucket.
 B. Create an Amazon CloudFront distribution. Set the S3 bucket as an origin.
 C. Configure the Elastic Load Balancer with an SSL/TLS certificate.
 D. Configure the Amazon CloudFront distribution with an SSL/TLS certificate.
 E. Configure the S3 bucket with an SSL/TLS certificate.
Incorrect
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.html
Option B and D

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

16. Question
A business utilizes AWS CodeBuild and AWS CodeCommit to implement a continuous build process. Developers routinely submit code throughout the development period, resulting in large build failures. The firm is looking for a solution that would generate code prior to developers pushing it to the main branch.Which option best fits these criteria in terms of cost-effectiveness?

 A. Configure am Amazon EC2 instance with the CodeBuild agent to build the code.
 B. Configure CodeBuild jobs on AWS for each branch build process.
 C. Configure the CodeBuild agent to build the code in the local system.
 D. Configure a Jenkins plugin for CodeBuild to run the code build process
Incorrect
Cost-effective: CodeBuild is a fully managed service that handles the build infrastructure, so you don’t need to maintain your own build servers or agents. This can significantly reduce costs.
Scalability: CodeBuild can automatically scale up or down based on demand, ensuring that your builds are processed efficiently without excessive costs.
Integration with CodeCommit: CodeBuild is tightly integrated with CodeCommit, making it easy to configure build jobs for each branch.
Early detection of build failures: By running builds on branches before code is pushed to the main branch, you can detect and address build failures earlier in the development process, saving time and effort.
The other options are less cost-effective or not as suitable for this scenario:

A. Configure am Amazon EC2 instance with the CodeBuild agent to build the code: This option would require you to maintain an EC2 instance, which can be costly, especially if the build process is resource-intensive.
C. Configure the CodeBuild agent to build the code in the local system: This option would require developers to have the CodeBuild agent installed on their local machines, which might not be feasible or desirable for all team members.
D. Configure a Jenkins plugin for CodeBuild to run the code build process: While Jenkins can be used for CI/CD, it would add additional complexity and might not be as cost-effective as using CodeBuild directly.
Therefore, configuring CodeBuild jobs on AWS for each branch build process is the most cost-effective and efficient solution for this scenario.

https://docs.aws.amazon.com/codebuild/latest/userguide/use-codebuild-agent.html
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

17. Question
A developer wishes to get a list of objects from an Amazon DynamoDB table‘s global secondary index.Which DynamoDB API call should the developer use to utilize the fewest read capacity units possible?

 A. Scan operation using eventually-consistent reads
 B. Query operation using strongly-consistent reads
 C. Query operation using eventually-consistent reads
 D. Scan operation using strongly-consistent reads
Incorrect
C. Query operation using eventually-consistent reads

Explanation:

To minimize read capacity units, we should aim for the most efficient operation possible. Here’s a breakdown of why “Query operation using eventually-consistent reads” is the best choice:

Query Operation: This operation is more efficient than a Scan operation because it allows you to specify a specific query condition based on a partition key and sort key. This reduces the amount of data that DynamoDB needs to process.
Eventually-Consistent Reads: This read consistency model offers lower latency and higher throughput compared to strongly consistent reads. While it might not guarantee the absolute latest data, it’s often sufficient for many applications.
By using a Query operation with eventually-consistent reads, we can significantly reduce the number of read capacity units consumed, making it the most cost-effective approach.

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

18. Question
Amazon S3 is structured as follows: S3:/BUCKET/FOLDERNAME/FILENAME.zipWhich S3 best practice would enhance speed when a single bucket receives thousands of PUT requests per second?

 A. Prefix folder names with user id; for example, s3://BUCKET/2013-FOLDERNAME/FILENAME.zip
 B. Prefix file names with timestamps; for example, s3://BUCKET/FOLDERNAME/2013-26-05-15-00-00-FILENAME.zip
 C. Prefix file names with random hex hashes; for example, s3://BUCKET/FOLDERNAME/23a6-FILENAME.zip
 D. Prefix folder names with random hex hashes; for example, s3://BUCKET/23a6-FOLDERNAME/FILENAME.zip
Incorrect
The best S3 practice to enhance speed when a single bucket receives thousands of PUT requests per second is:

D. Prefix folder names with random hex hashes; for example, s3://BUCKET/23a6-FOLDERNAME/FILENAME.zip

Here’s why:

Parallelization: Amazon S3 can achieve higher throughput by parallelizing PUT requests across multiple S3 prefixes within a bucket.
Random Hex Hashes: By using random hex hashes for folder names, you distribute uploads across different prefixes, maximizing the potential for parallelization. This improves overall upload performance.
User IDs and Timestamps: While these options (A & B) might seem reasonable for organization, they don’t necessarily distribute uploads evenly across prefixes. If many users upload around the same time, their uploads might end up in the same prefix, limiting parallelization benefits.
Additional Considerations:

Number of Prefixes: While using many prefixes can improve performance, creating an excessive number can have diminishing returns.
Impact on Data Management: Using random hex prefixes might make it harder to locate specific files later. Consider implementing a separate metadata store to track file locations by name alongside their random prefix locations.
By implementing folder names with random hex hashes, you leverage S3’s parallelization capabilities to accelerate PUT requests for high-volume uploads.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

19. Question
Amazon Elastic Container Service is used to deploy a microservices application across several containers (Amazon ECS). A developer want to collect trace information across microservices and view the microservices architecture in order to optimize performance.Which solution will satisfy these criteria?

 A. Build the container from the amazon/aws-xray-daemon base image. Use the AWS X-Ray SDK to instrument the application.
 B. Install the Amazon CloudWatch agent on the container image. Use the CloudWatch SDK to publish custom metrics from each of the microservices.
 C. Install the AWS X-Ray daemon on each of the ECS instances.
 D. Configure AWS CloudTrail data events to capture the traffic between the microservices.
Incorrect
https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-ecs.html#xray-daemon-ecs-build . You build the xray container along side the other ecs images deployed via the task definition. you then have to configure/ instrument the app to utilize the sdk for the rest
Option A

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

20. Question
A developer is configuring the Amazon API Gateway to support their business‘s goods. Registered developers may use the API to query and change their environments. For financial and security concerns, the organization want to restrict the number of requests that end users may submit. Management want to provide registered developers with the option of purchasing bigger packages that support a greater number of requests.How can the developer do this with the LEAST amount of management overhead?

 A. Enable throttling for the API Gateway stage. Set a value for both the rate and burst capacity. If a registered user chooses a larger package, create a stage for them, adjust the values, and share the new URL with them.
 B. Set up Amazon CloudWatch API logging in API Gateway. Create a filter based on the user and requestTime fields and create an alarm on this filter. Write an AWS Lambda function to analyze the values and requester information, and respond accordingly. Set up the function as the target for the alarm. If a registered user chooses a larger package, update the Lambda code with the values.
 C. Enable Amazon CloudWatch metrics for the API Gateway stage. Set up CloudWatch alarms based off the Count metric and the ApiName, Method, Resource, and Stage dimensions to alerts when request rates pass the threshold. Set the alarm action to Deny. If a registered user chooses a larger package, create a user-specific alarm and adjust the values.
 D. Set up a default usage plan, specify values for the rate and burst capacity, and associate it with a stage. If a registered user chooses a larger package, create a custom plan with the appropriate values and associate the plan with the user.
Incorrect
After you create, test, and deploy your APIs, you can use API Gateway usage plans to make them available as product offerings for your customers. You can configure usage plans and API keys to allow customers to access selected APIs at agreed-upon request rates and quotas that meet their business requirements and budget constraints. If desired, you can set default method-level throttling limits for an API or set throttling limits for individual API methods.
Option D

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

21. Question
A developer is using Amazon S3 to store sensitive data created by an application. The developer want to encrypt the data while it is in transit. A corporate policy demands an audit trail detailing when and by whom the master key was used.Which encryption method will satisfy these criteria?

 A. Server-side encryption with Amazon S3 managed keys (SSE-S3)
 B. Server-side encryption with AWS KMS managed keys (SSE-KMS)
 C. Server-side encryption with customer-provided keys (SSE-C)
 D. Server-side encryption with self-managed keys
Incorrect
https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html Similar to SSE-S3, but with some additional benefits along with some additional charges for using this service. provides you with an audit trail of when your key was used and by whom. Additionally, you have the option to create and manage encryption keys yourself, or use a default key that is unique to you.
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

22. Question
How does AWS KMS‘s Envelope Encryption work?

 A. The Customer Master Key is used to encrypt/decrypt a data key. The Plaintext Data Key is used to encrypt customer data.
 B. Two encryption keys are used. The Customer Master Key encrypts customer data. The Data Key is used to re-encrypt the encrypted data.
 C. Two encryption keys are used. The Data Key encrypts customer data. The ?¡ustomer Master Key is used to re-encrypt the encrypted data.
 D. The Customer Master Key is used to encrypt/decrypt a data key. The Encrypted Data Key is used to encrypt customer data.
Incorrect
https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping “Envelope encryption When you encrypt your data, your data is protected, but you have to protect your encryption key. One strategy is to encrypt it. Envelope encryption is the practice of encrypting plaintext data with a data key, and then encrypting the data key under another key. “
Option A

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

23. Question
A business is developing a stock trading application. The program requires a latency of less than one millisecond to handle trading requests. The firm stores all trade data in Amazon DynamoDB, which is utilized to perform each trading request.A development team conducts load testing on the application and discovers that the time required to get data is longer than intended. The development team need a solution that significantly improves data retrieval time with the least amount of work feasible.Which solution satisfies these criteria?

 A. Add local secondary indexes (LSIs) for trading data.
 B. Store trading data in Amazon S3 and use Transfer Acceleration.
 C. Add retries with exponential back-off for DynamoDB queries
 D. Use DynamoDB Accelerator to cache trading data.
Incorrect
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html Amazon DynamoDB is designed for scale and performance. In most cases, the DynamoDB response times can be measured in single-digit milliseconds. However, there are certain use cases that require response times in microseconds. For these use cases, DynamoDB Accelerator (DAX) delivers fast response times for accessing eventually consistent data. keywords are “time required to get data“, “significantly improves data retrieval time“ and “least amount of work“
Option D

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

24. Question
A business is in the process of building a serverless ecommerce web application. The application must perform synchronized, all-or-nothing updates to various products in the company‘s Amazon DynamoDB inventory database.Which solution will satisfy these criteria?

 A. Enable transactions for the DynamoDB table. Use the BatchWriteItem operation to update the items.
 B. Use the TransactWriteItems operation to group the changes. Update the items in the table.
 C. Set up a FIFO queue using Amazon SQS. Group the changes in the queue. Update the table based on the grouped changes.
 D. Create a transaction table in an Amazon Aurora DB cluster to manage the transactions. Write a backend process to sync the Aurora DB table and the DynamoDB table.
Incorrect
TransactWriteItems operation differs from a BatchWriteItem operation in that all the actions it contains must be completed successfully, or no changes are made at all. With a BatchWriteItem operation, it is possible that only some of the actions in the batch succeed while the others do not.
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

25. Question
On Amazon EC2 ECS, two containerized microservices are hosted. The first microservice reads a database instance from Amazon RDS Aurora, while the second microservice reads a table from Amazon DynamoDB.How can the bare minimal rights be provided to each microservice?

 A. Set ECS_ENABLE_TASK_IAM_ROLE to false on EC2 instance boot in ECS agent configuration file. Run the first microservice with an IAM role for ECS tasks with read-only access for the Aurora database. Run the second microservice with an IAM role for ECS tasks with read-only access to DynamoDB.
 B. Set ECS_ENABLE_TASK_IAM_ROLE to false on EC2 instance boot in the ECS agent configuration file. Grant the instance profile role read-only access to the Aurora database and DynamoDB.
 C. Set ECS_ENABLE_TASK_IAM_ROLE to true on EC2 instance boot in the ECS agent configuration file. Run the first microservice with an IAM role for ECS tasks with read-only access for the Aurora database. Run the second microservice with an IAM role for ECS tasks with read-only access to DynamoDB.
 D. Set ECS_ENABLE_TASK_IAM_ROLE to true on EC2 instance boot in the ECS agent configuration file. Grant the instance profile role read-only access to the Aurora database and DynamoDB.
Incorrect
ECS_ENABLE_TASK_IAM_ROLE should be set to TRUE in EC2 that has the ECS Agent config file. Then IAM ready only DB roles will be assumed for ECS Tasks
Option C

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

26. Question
A developer is developing a Lambda function to create and export a file. While the program is running, it needs 100 MB of temporary storage for transient files. These files are no longer required after the function has been completed.How can the developer manage temporary files most efficiently?

 A. Store the files in EBS and delete the files at the end of the Lambda function.
 B. Copy the files to EFS and delete the files at the end of the Lambda function.
 C. Store the files in the /tmp directory and delete the files at the end of the Lambda function.
 D. Copy the files to an S3 bucket with a lifecycle policy to delete the files.
Incorrect
#> https://aws.amazon.com/lambda/faqs/ #> Each Lambda function receives 512MB of non-persistent disk space in its own /tmp directory.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

27. Question
A developer is establishing a position that will provide access to Amazon S3 buckets. The developer creates the role using the AWS CLI create-role command.Which policy should be implemented to enable Amazon EC2 to take over the role?

 A. Managed policy
 B. Trust policy
 C. Inline policy
 D. Service control policy (SCP)
Incorrect
A JSON policy document in which you define the principals that you trust to assume the role. A role trust policy is a required resource-based policy that is attached to a role in IAM. The principals that you can specify in the trust policy include users, roles, accounts, and services. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

28. Question
There are two categories of members on a video-hosting website: those who pay a charge and those who do not. Each video upload creates a message in Amazon Simple Queue Service (SQS). Each video is processed by a fleet of Amazon EC2 instances that poll Amazon SQS.The developer must guarantee that the developer processes the films submitted by paying users first.How is the developer to achieve this criterion?

 A. Create two SQS queues: one for paying members, and one for non-paying members. Poll the paying member queue first and then poll the non-paying member queue.
 B. Use SQS to set priorities on individual items within a single queue; give the paying members‘ videos the highest priority.
 C. Use SQS to set priorities on individual items within a single queue and use Amazon SNS to encode the videos.
 D. Create two Amazon SNS topics: one for paying members and one for non-paying members. Use SNS topic subscription priorities to differentiate between the two types of members.
Incorrect
Create two SQS queues https://aws.amazon.com/sqs/features/ Priority: Use separate queues to provide prioritization of work. (priority in the same queue is not possible.) https://forums.aws.amazon.com/thread.jspa?threadID=48134
Option A

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

29. Question

In an Amazon DynamoDB database, a business caches session information for a web application. The organization want to automate the process of deleting obsolete entries from the table.What is the easiest method for doing this?

 A. Write a script that deletes old records; schedule the scripts as a cron job on an Amazon EC2 instance.
 B. Add an attribute with the expiration time; enable the Time To Live feature based on that attribute.
 C. Each day, create a new table to hold session data; delete the previous day‘s table.
 D. Add an attribute with the expiration time; name the attribute ItemExpiration.
Incorrect
B https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

30. Question
The processing of an Amazon SQS message by an application takes longer than planned.What should the developer do to ensure that other instances of the program do not get the same message?

 A. Make a ReceiveMessage call to get the same message again from the queue
 B. Issue a DeleteMessage call to delete the message from the queue
 C. Use SendMessage to pass the message to the dead letter queue
 D. Send a ChangeMessageVisibility call to extend VisibilityTimeout
Incorrect
Visibility Timeout is used to hide messages from other consumers when one of the consumers is processing the message. In the above case, when one of the Amazon EC2 instance is processing messages from the Amazon SQS queue, due to load on instance it is taking time to process messages. Within that time period visibility timeout is expired & another EC2 instance is processing the same message & sending updates to users. To avoid multiple processing of the same message, Visibility timeout can be increased so that Amazon EC2 processes the message before visibility timeout expires.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

31. Question
A developer is required to create an application that makes advantage of Amazon DynamoDB. The criteria include that the DynamoDB table‘s contents must be 7KB in size and that reads must be highly consistent. The read pace is limited to three items per second, whereas the write rate is limited to ten things per second.What size DynamoDB table should the developer create to satisfy these requirements?

 A. Read: 3 read capacity units Write: 70 write capacity units
 B. Read: 6 read capacity units Write: 70 write capacity units
 C. Read: 6 read capacity units Write: 10 write capacity units
 D. Read: 3 read capacity units Write: 10 write capacity units
Incorrect
We are talking about 3 strong reads of 7KB. 7KB requires 2 RCUs, so 3 x 2 = 6. Regarding the writes, we are talking about 10 itens per second. 7KB requires 7 WCUs. So 10 x 7 = 70.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

32. Question
A server-side application running on Amazon EC2 instances needs access assets contained in an Amazon S3 bucket that have been secured using AWS KMS encryption keys (SSE-KMS). To decrypt the items, the program must have access to the customer master key (CMK).Which sequence of actions will provide access to the application? (Select two.)

 A. Write an S3 bucket policy that grants the bucket access to the key.
 B. Grant access to the key in the IAM EC2 role attached to the application‘s EC2 instances.
 C. Write a key policy that enables IAM policies to grant access to the key.
 D. Grant access to the key in the S3 bucket‘s ACL
 E. Create a Systems Manager parameter that exposes the KMS key to the EC2 instances.
Incorrect
1. Open the AWS KMS console, and then view the key‘s policy document using the policy view. Modify the key‘s policy to grant the IAM user permissions for the kms:GenerateDataKey and kms:Decrypt actions at minimum. 2. Open the IAM console. Add a policy to the IAM user that grants the permissions to upload and download from the bucket. https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-access-default-encryption/

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

33. Question
A developer is testing an application that asynchronously executes an AWS Lambda function. The Lambda function fails to process after two retries during the testing phase.How can the developer debug the error?

 A. Configure AWS CloudTrail logging to investigate the invocation failures
 B. Configure Dead Letter Queues by sending events to Amazon SQS for investigation
 C. Configure Amazon Simple Workflow Service to process any direct unprocessed events
 D. Configure AWS Config to process any direct unprocessed events
Incorrect
“Dead-letter queues are useful for debugging your application or messaging system because they let you isolate problematic messages to determine why their processing doesn‘t succeed“ https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

34. Question
A developer creates an AWS Lambda function and uploads it to Amazon S3 in the form of a.ZIP file. The developer modifies the code and sends an updated.ZIP file to Amazon S3. Lambda, on the other hand, runs the preceding code.How can the Developer resolve this in the LEAST obtrusive manner possible?

 A. Create another Lambda function and specify the new .ZIP file.
 B. Call the update-function-code API.
 C. Remove the earlier .ZIP file first, then add the new .ZIP file.
 D. Call the create-alias API.
Incorrect
A. Create another Lambda Function: This creates a completely new function, which is unnecessary and creates additional management overhead.
C. Remove the earlier .ZIP file first, then add the new .ZIP file: This approach works technically, but it introduces downtime for the function while the old code is removed and the new code is uploaded. Not ideal!
D. Call the create-alias API: This API allows you to create an alias for an existing function version, but it doesn’t update the actual code.
The update-function-code API is specifically designed to update the code of an existing Lambda function. It allows you to upload a new .ZIP file containing the updated code, effectively replacing the old code with the new one. This approach minimizes downtime and doesn’t require any significant changes to the function configuration.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

35. Question
A software business must ensure that documents provided by users are maintained securely in Amazon S3. At rest, the documents must be encrypted in Amazon S3.The firm does not want to operate its security infrastructure in-house, but it need additional protection to maintain control over its encryption keys in order to comply with industry laws.Which encryption technique should a developer use in order to satisfy these requirements?

 A. Server-side encryption with Amazon S3 managed keys (SSE-S3)
 B. Server-side encryption with customer-provided encryption keys (SSE-C)
 C. Server-side encryption with AWS KMS managed keys (SSE-KMS)
 D. Client-side encryption
Incorrect
The highlight in the question is “The company does not want to manage the security infrastructure in-house, but the company still needs extra protection to ensure it has control over its encryption keys due to industry regulations“. SSE-C could be the answer if the company is ok to manage the keys in-house. So the answer is SSE-KMS

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

36. Question
A developer wishes to improve the performance of reads from an unencrypted Amazon S3 bucket. Each second, the program needs 100,000 read requests. Priority is given to cost-effectiveness.What is the MOST SIMPLE method for implementing these requirements?

 A. Create 20 or more prefixes in Amazon S3. Place files by prefixes. Read in parallel by prefixes.
 B. Create 20 or more AWS accounts. Create a bucket in each account. Read in parallel by bucket.
 C. Deploy Memcached on Amazon EC2. Cache the files in memory. Retrieve from the Memcached cache.
 D. Copy all files to Amazon DynamoDB. Index the files with S3 metadata. Retrieve from DynamoDB.
Incorrect
“if you create 10 prefixes in an Amazon S3 bucket to parallelize reads, you could scale your read performance to 55,000 read requests per second. “ https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

37. Question
Amazon Kinesis Data Streams enables an application to ingest and handle huge streams of data records in real time. Utilizing the Amazon Kinesis Client Library, Amazon EC2 instances ingest and process data from the shards of the Kinesis data stream (KCL). The program manages failure situations and eliminates the need for backup personnel. The program indicates that a particular shard is getting much more data than anticipated. The hot shard is resharded to react to variations in the pace of data flow.If the initial number of shards in the Kinesis data stream is four, and the number of shards increases to six after resharding, what is the maximum number of EC2 instances that can be deployed to process data from all the shards?

 A. 12
 B. 6
 C. 4
 D. 1
Incorrect
Typically, when you use the KCL, you should ensure that the number of instances does not exceed the number of shards (except for failure standby purposes). Each shard is processed by exactly one KCL worker and has exactly one corresponding record processor, so you never need multiple instances to process one shard. However, one worker can process any number of shards, so it‘s fine if the number of shards exceeds the number of instances. https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

38. Question
A business is developing a compute-intensive application that will operate on an Amazon EC2 fleet. The program stores data on associated Amazon EBS drives. Because the program will be processing sensitive data, all data must be encrypted.What steps should a developer take to guarantee data is encrypted on disk without sacrificing performance?

 A. Configure the Amazon EC2 instance fleet to use encrypted EBS volumes for storing data.
 B. Add logic to write all data to an encrypted Amazon S3 bucket.
 C. Add a custom encryption algorithm to the application that will encrypt and decrypt all data.
 D. Create a new Amazon Machine Image (AMI) with an encrypted root volume and store the data to ephemeral disks.
Incorrect
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html
Option A

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

39. Question
A legacy service has a SOAP interface that is XML-based. The developer want to use the Amazon API Gateway to expose the service‘s capabilities to external customers. Which approach is necessary to do this?

 A. Create a RESTful API with the API Gateway; transform the incoming JSON into a valid XML message for the SOAP interface using mapping templates.
 B. Create a RESTful API with the API Gateway; pass the incoming JSON to the SOAP interface through an Application Load Balancer.
 C. Create a SOAP API with the API Gateway; pass the incoming XML to the SOAP interface through an Application Load Balancer.
 D. Create a SOAP API with the API Gateway; transform the incoming XML into a valid message for the SOAP interface using mapping templates.
Incorrect
A, good explanation here and about halfway down the page it‘s talking about mapping templates to convert json to xml and xml to json https://blog.codecentric.de/en/2016/12/serverless-soap-legacy-api-integration-java-aws-lambda-aws-api-gateway/
Option A

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

40. Question
What is the advantage of instantiating AWS clients outside the scope of the handler when constructing a Lambda function?

 A. Legibility and stylistic convention
 B. Taking advantage of connection re-use
 C. Better error handling
 D. Creating a new instance per invocation
Incorrect
Take advantage of execution environment reuse to improve the performance of your function. Initialize SDK clients and database connections outside of the function handler, and cache static assets locally in the /tmp directory. Subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time. https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#:~:text=Take%20advantage%20of,function%20run%20time.
Option B

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

41. Question
Three microservice projects are created by a developer and are stored in distinct folders under the same AWS CodeCommit repository. Each project is served by a distinct AWS CodePipeline pipeline. When a developer pushes modifications to a single microservice, all three pipelines begin to execute.The developer must ensure that only necessary pipelines are executed. The developer is not permitted to alter the organization of the repository.Which solution will satisfy these criteria?

 A. For each of the three microservice projects, create a separate CodeCommit repository.
 B. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that invokes an AWS Lambda function to evaluate changes to the repository and run the appropriate pipeline.
 C. Create an Amazon API Gateway API that is backed by an AWS Lambda function to determine the appropriate pipeline to run. Add the API endpoint to a webhook in CodeCommit.
 D. Migrate all three pipelines to a single pipeline. Add conditional stages to build a certain microservice project.
Incorrect
“To introduce custom logic and control the events that kickoff the pipeline, this example configures the default CloudWatch Events rule to detect changes in the source and trigger a Lambda function rather than invoke the pipeline directly.“ Ref: https://aws.amazon.com/blogs/devops/adding-custom-logic-to-aws-codepipeline-with-aws-lambda-and-amazon-cloudwatch-events/

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

42. Question
A developer transferred a web application to Amazon Web Services (AWS). As part of the move, the developer used a blue/green deployment to automate the continuous integration/continuous improvement (CI/CD) process. The deployment creates new Amazon EC2 instances in an Auto Scaling group, which is configured to run behind a new Application Load Balancer. Following the move, the Developer started receiving complaints from users who had been booted off the system. Additionally, the system needs users to log in upon each new deployment.How are these problems to be resolved?

 A. Use rolling updates instead of a blue/green deployment
 B. Externalize the user sessions to Amazon ElastiCache
 C. Turn on sticky sessions in the Application Load Balancer
 D. Use multicast to replicate session information
Incorrect
The deployment uses a new Application Load Balancer. So enabling session stickiness in ALB (old) wont help here. So there should be some mechanism to store sessions outside of ALB. Which is elasticache or dynamodb. Here the option is ElastiCache

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

43. Question
Two Amazon DynamoDB tables are accessed using an AWS Lambda function. A developer wishes to optimize the Lambda function‘s performance by finding bottlenecks inside the function.How can a developer determine the duration of DynamoDB API calls?

 A. Add DynamoDB as an event source to the Lambda function. View the performance with Amazon CloudWatch metrics.
 B. Place an Application Load Balancer (ALB) in front of the two DynamoDB tables. Inspect the ALB logs.
 C. Limit Lambda to no more than five concurrent invocations. Monitor from the Lambda console.
 D. Enable AWS X-Ray tracing for the function. View the traces from the X-Ray service.
Incorrect
Enable X-ray for Serverless application to view the map and find the traces for each segments

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

44. Question
All data in transit between an EC2 instance and an Amazon EBS volume must be secured for a physician‘s office management application.Which one of the following strategies satisfies this criterion? (Select two.)

 A. Create encrypted snapshots into Amazon S3.
 B. Use Amazon RDS with encryption.
 C. Use IAM roles to limit access to the Amazon EBS volume.
 D. Enable EBS encryption.
 E. Leverage OS-level encryption.
Incorrect
IAM role is for access, RDS has no relevance here, A talks about encryption at rest and not trnasit, so only D and E makes perfect sense here . The other 3 does not make sense. B is talking about RDS. This question does not talk about RDS . C – Is about access to EBS . A – Why save in a S3 ?

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

45. Question
Page load times on a website steadily increase as more people visit the system concurrently. According to the analysis, a user profile is being loaded from a database on each web page viewed by a user, which increases database load and page load delay. The developer chooses to cache the user profile data in order to remedy this problem.Which caching approach would most effectively solve this situation?

 A. Create a new Amazon EC2 Instance and run a NoSQL database on it. Cache the profile data within this database using the write-through caching strategy.
 B. Create an Amazon ElastiCache cluster to cache the user profile data. Use a cache-aside caching strategy.
 C. Use a dedicated Amazon RDS instance for caching profile data. Use a write-through caching strategy.
 D. Create an ElastiCache cluster to cache the user profile data. Use a write-through caching strategy.
Incorrect
Lazy caching, also called lazy population or cache-aside, is the most prevalent form of caching. Laziness should serve as the foundation of any good caching strategy. The basic idea is to populate the cache only when an object is actually requested by the application. Cache-aside = lazy loading

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

46. Question
A development team is tasked with the task of creating a mobile application that will need multi-factor authentication.Which measures should be made in order to accomplish this? (Select two.)

 A. Use Amazon Cognito to create a user pool and create users in the user pool.
 B. Send multi-factor authentication text codes to users with the Amazon SNS Publish API call in the app code.
 C. Enable multi-factor authentication for the Amazon Cognito user pool.
 D. Use AWS IAM to create IAM users.
 E. Enable multi-factor authentication for the users created in AWS IAM.
Incorrect
Create the user pool with cognito (A) and then enable MFA for those users (C)

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

47. Question
A developer is using Amazon API Gateway to create a WebSocket API. The payload submitted to this API is JSON with an action key included. This key may take on one of three values: create, update, or delete. The developer must interact with several routes dependent on the value of the incoming JSON payload‘s action key.How can the developer execute this operation using the LESS settings possible?

 A. Deploy the WebSocket API to three stages for the respective routes: create, update, and remove
 B. Create a new route key and set the name as action
 C. Set the value of the route selection expression to action
 D. Set the value of the route selection expression to $request.body.action
Incorrect
The correct answer is: D. Set the value of the route selection expression to $request.body.action.

Here’s why:

WebSocket API: The scenario involves a WebSocket API using JSON payloads with an “action” key.
Multiple routes: The developer needs to interact with different routes based on the value of the “action” key.
LESS settings: The question emphasizes using the least settings possible.
By setting the route selection expression to $request.body.action, the developer achieves the desired functionality with minimal configuration:

$request.body.action accesses the value of the “action” key within the JSON body of the incoming request.
API Gateway evaluates the expression and matches it against the defined route keys.
Based on the matching value (create, update, or delete), the request is routed to the appropriate backend integration.
This approach achieves the routing logic without needing to deploy separate stages for each action or managing multiple route keys.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

48. Question
A programmer is developing an application that will handle a stream of data given by the user. The data stream must be received concurrently and in real time by various Amazon EC2-based processing apps. Each processor must be capable of restarting without losing data if service is interrupted. The Application Architect intends to expand the number of processors in the near future and wants to reduce data duplication.Which solution will meet these criteria?

 A. Publish the data to Amazon SQS.
 B. Publish the data to Amazon Kinesis Data Firehose.
 C. Publish the data to Amazon CloudWatch Events.
 D. Publish the data to Amazon Kinesis Data Streams.
Incorrect
D. Publish the data to Amazon Kinesis Data Streams.

Kinesis Data Streams is the most suitable solution for this scenario due to its ability to handle real-time, high-throughput data streams and its support for multiple consumers.

Here’s how it meets the criteria:

Real-time, concurrent processing: Kinesis Data Streams allows multiple consumers to read data concurrently from the same stream, ensuring real-time processing.
Fault tolerance and data durability: Kinesis Data Streams provides strong durability guarantees, ensuring that data is not lost even in the event of failures.
Scalability: Kinesis Data Streams can automatically scale to handle increasing data loads.
Reduced data duplication: Kinesis Data Streams allows multiple consumers to read the same data without duplicating it.
Other options:

Amazon SQS: While SQS can handle concurrent processing, it’s more suited for asynchronous processing and message queues, not real-time data streams.
Amazon Kinesis Data Firehose: Primarily used for loading data into data lakes and analytics services. It’s not ideal for real-time, low-latency processing.
Amazon CloudWatch Events: Used for event-driven architectures, not real-time data streams.
Therefore, Kinesis Data Streams is the most suitable solution for this use case.

Reference: https://aws.amazon.com/kinesis/data-streams/faqs/

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

49. Question

A business uses Amazon EC2 instances to execute a bespoke web application behind an Application Load Balancer. The instances are managed as part of an Auto Scaling group. The company‘s development team deploys all services through AWS CloudFormation. When the development team runs a new instance of the program, it takes time to install and setup.Which sequence of actions should a developer follow to improve efficiency while launching a new instance? (Select two.)

 A. Use an AWS Marketplace Amazon Machine Image (AMI) with a prebuilt application.
 B. Create a prebuilt Amazon Machine Image (AMI) with the application installed and configured.
 C. Update the launch template resource in the CloudFormation template.
 D. Use AWS Systems Manager Run Command to install and configure the application.
 E. Use CloudFormation helper scripts to install and configure the application.
Incorrect
The two actions that a developer should follow to improve efficiency while launching a new instance are:

B. Create a prebuilt Amazon Machine Image (AMI) with the application installed and configured.

This is the most efficient approach. By creating an AMI with the application already installed and configured, you eliminate the time-consuming installation and setup process each time you launch a new instance.
This significantly reduces launch times and improves overall deployment speed.
C. Update the launch template resource in the CloudFormation template.

Launch templates are used to define the configuration of your EC2 instances, including the AMI.
By updating the Launch Template resource within your CloudFormation template to reference the pre-built AMI, you can easily deploy new instances with the application pre-installed. This ensures consistency and simplifies the deployment process.
Explanation of other options:

A. Use an AWS Marketplace Amazon Machine Image (AMI) with a prebuilt application. While this might be an option in some cases, it might not be suitable if the application is highly customized or has specific dependencies. Using a custom AMI provides more control and flexibility.
D. Use AWS Systems Manager Run Command to install and configure the application. This approach can be used to automate post-launch tasks, but it still requires the instance to be launched first, which adds to the overall launch time.
E. Use CloudFormation helper scripts to install and configure the application. While CloudFormation helper scripts can automate some tasks, they still require execution after the instance is launched, which can add to the overall launch time.
By combining the creation of a pre-built AMI with the use of Launch Templates within your CloudFormation template, you can significantly improve the efficiency of launching new instances of your web application.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

50. Question
When deploying new application versions on AWS Elastic Beanstalk, an application‘s error rate increases, resulting in service deterioration for customers. This, the Development team thinks, is due to the capacity loss throughout the deployment processes. The team want to update the environment‘s deployment policy configuration to one that maintains full capacity during deployment while using current instances.Which deployment strategy will satisfy these criteria while using current instances?

 A. All at once
 B. Rolling
 C. Rolling with additional batch
 D. Immutable
Incorrect
All at once
Updates all instances simultaneously.
Problem: Service is disrupted; no capacity maintained.
Rolling ✅
Updates a subset (batch) of instances at a time.
Remaining instances continue serving traffic → full capacity maintained during deployment.
Uses current instances (no new instances created).
Rolling with additional batch
Adds extra instances to maintain capacity.
Not using only current instances → more costly.
Immutable
Deploys new instances alongside old ones.
Old instances replaced only after health checks pass.
Maintains full capacity but creates new instances, not just using current ones.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

51. Question
A developer used a CLI command to register an AWS Lambda function as a target for an Application Load Balancer (ALB). However, when the client submits requests via the ALB, the Lambda function is not called.Why isn‘t the Lambda function called?

 A. A Lambda function cannot be registered as a target for an ALB.
 B. A Lambda function can be registered with an ALB using AWS Management Console only.
 C. The permissions to invoke the Lambda function are missing.
 D. Cross-zone is not enabled on the ALB.
Incorrect
You can register your Lambda functions as targets and configure a listener rule to forward requests to the target group for your Lambda function. When the load balancer forwards the request to a target group with a Lambda function as a target, it invokes your Lambda function and passes the content of the request to the Lambda function, in JSON format.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

52. Question
A real-time application processes millions of events that are received over an API.Which service might be utilized to enable concurrent processing of data by several users in the most cost-effective manner possible?

 A. Amazon SNS with fanout to an SQS queue for each application
 B. Amazon SNS with fanout to an SQS FIFO (first-in, first-out) queue for each application
 C. Amazon Kinesis Firehose
 D. Amazon Kinesis Streams
Incorrect
Q: When should I use Amazon Kinesis Data Streams, and when should I use Amazon SQS? We recommend Amazon Kinesis Data Streams for use cases with requirements that are similar to the following: Ability for multiple applications to consume the same stream concurrently. For example, you have one application that updates a real-time dashboard and another that archives data to Amazon Redshift. You want both applications to consume data from the same stream concurrently and independently. Reference: https://aws.amazon.com/kinesis/data-streams/faqs/ . C: This will also work but because it is a managed service, its more expensive. There are a couple major differences I‘m aware of. One, Firehose is fully managed (i.e. scales automatically) whereas Streams is manually managed. Second, Firehose only goes to S3 or RedShift, whereas Streams can go to other services. … Kinesis Streams on the other hand can store the data for up to 7 days.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

53. Question
Numerous apps make use of an Amazon RDS database instance to seek for previous data. The pace of queries is quite steady. When historical data is updated daily, the associated write traffic degrades the speed of read queries, affecting all application users.What can be done to minimize the effect on application users‘ performance?

 A. Make sure Amazon RDS is Multi-AZ so it can better absorb increased traffic.
 B. Create an RDS Read Replica and direct all read traffic to the replica.
 C. Implement Amazon ElastiCache in front of Amazon RDS to buffer the write traffic.
 D. Use Amazon DynamoDB instead of Amazon RDS to buffer the read traffic.
Incorrect
Pick AWS Elasticache If the same read query is performed over and over again. AWS RDS Read Replica if the read query changes dynamically.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

54. Question
An application is composed of two components: one for handling HTTP requests and another for doing background processing operations. Each component must be self-scaling. The developer want to use AWS Elastic Beanstalk to deploy this application.How, in light of these criteria, should this application be deployed?

 A. Deploy the application in a single Elastic Beanstalk environment.
 B. Deploy each component in a separate Elastic Beanstalk environment.
 C. Use multiple Elastic Beanstalk environments for the HTTP component, but one environment for the background task component.
 D. Use multiple Elastic Beanstalk environments for the background task component, but one environment for the HTTP component.
Incorrect
When you launch an Elastic Beanstalk environment, you first choose an environment tier. The environment tier designates the type of application that the environment runs, and determines what resources Elastic Beanstalk provisions to support it. An application that serves HTTP requests runs in a web server environment tier. A backend environment that pulls tasks from an Amazon Simple Queue Service (SQS) queue runs in a worker environment tier.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

55. Question
Amazon API Gateway is being used by a media business to handle microservices configured as AWS Lambda functions. The development team of the corporation intends to release a new version of its API. To prevent impacting current customers when the new API is launched, the firm intends to provide all users a three-month grace period during which they may migrate from the old API to the new API.Which implementation technique should the business utilize to accomplish this objective?

 A. Update the Lambda functions. Configure the API to use Lambda proxy integration.
 B. Update the Lambda functions. Provide the API client with the new Lambda endpoints.
 C. Use API Gateway to deploy a new stage that uses updated Lambda functions and provides users with a new URL.
 D. Use API Gateway to redirect requests based on a request header to updated Lambda functions. Configure a 90-day expiration on the old API.
Incorrect
A stage is a named reference to a deployment, which is a snapshot of the API. You use a Stage to manage and optimize a particular deployment. For example, you can configure stage settings to enable caching, customize request throttling, configure logging, define stage variables, or attach a canary release for testing.
Option c
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

56. Question
A developer is now working on an application that manages papers that are ten megabytes in size and include very sensitive data. The application will encrypt data on the client side using AWS KMS.Which procedures must be followed?

 A. Invoke the Encrypt API passing the plaintext data that must be encrypted, then reference the customer managed key ARN in the KeyId parameter
 B. Invoke the GenerateRandom API to get a data encryption key, then use the data encryption key to encrypt the data
 C. Invoke the GenerateDataKey API to retrieve the encrypted version of the data encryption key to encrypt the data
 D. Invoke the GenerateDataKey API to retrieve the plaintext version of the data encryption key to encrypt the data
Incorrect
nvoke the GenerateDataKey API to retrieve the plaintext version of the data encryption key to encrypt the data #> https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html #> When uploading an objectUsing the customer master key (CMK) ID, the client first sends a request to AWS KMS for a CMK that it can use to encrypt your object data. AWS KMS returns two versions of a randomly generated data key: #> 1. A plaintext version of the data key that the client uses to encrypt the object data #> 2. A cipher blob of the same data key that the client uploads to Amazon S3 as object metadata #> Note: The client obtains a unique data key for each object that it uploads.

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

57. Question
A developer must adapt the architecture of an application to accommodate new functional requirements. Amazon DynamoDB is used to store application data, which is processed for analysis in a nightly batch. System analysts do not like to wait until the next day to examine processed data and have requested that it be made accessible in near-real time.Which application architectural pattern would allow real-time data processing?

 A. Event driven
 B. Client-server driven
 C. Fan-out driven
 D. Schedule driven
Incorrect
https://tanzu.vmware.com/content/blog/introduction-to-event-driven-architecture-and-apache-kafka

---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------

58. Question
A developer has created a market application that utilizes Amazon DynamoDB and Amazon ElastiCache to store price data. The market‘s prices fluctuate often. Sellers have began to complain that when they alter the price of an item, the price in the product listing does not really change.What may be causing this problem?

 A. The cache is not being invalidated when the price of the item is changed
 B. The price of the item is being retrieved using a write-through ElastiCache cluster
 C. The DynamoDB table was provisioned with insufficient read capacity
 D. The DynamoDB table was provisioned with insufficient write capacity
Incorrect
Cache is not being invalidated after table write and this causes inconsistency
























