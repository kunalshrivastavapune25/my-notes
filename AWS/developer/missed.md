Of course! Here is a consolidated and well-structured study guide created from your practice questions. The questions are presented with their options, the correct answer, and a clear, concise explanation.

### AWS Certified Developer - Associate Study Notes

---

#### 1. Debugging Lambda Functions
**Question:** As a developer, you have created a Lambda function that is not working as expected. How can you debug the issue in an easily understandable way?
- A. Use AWS CloudWatch metrics
- **B. Use AWS CloudWatch logs -- correct**
- C. Set the Lambda function debugging level to verbose
- D. Use AWS Cloudtrail logs

**Explanation:** Lambda automatically integrates with CloudWatch Logs. By adding logging statements (e.g., `console.log`) to your code, you can push all logs to a CloudWatch Logs group (`/aws/lambda/<function-name>`), making it easy to trace execution and errors.

---

#### 2. S3 Performance for High GET Requests
**Question:** Your company expects roughly 6000 GET requests per second on S3. Which two options ensure optimal performance?
- **A. Use a CloudFront distribution in front of the S3 bucket**
- **B. Use sequential date-based naming for your prefixes.**
- C. Enable versioning for the objects
- D. Enable Cross Region Replication for the bucket

**Explanation:**
- **A. CloudFront** caches content at edge locations, reducing direct load on S3 and improving latency.
- **B. Prefix Naming:** While AWS recommends *random* prefixes for maximum parallelism, using well-distributed prefixes (like date-based) can still help distribute requests across S3 partitions, preventing a "hot" partition.

---

#### 3. Serverless Deployment with SAM
**Question:** You have a SAM (Serverless Application Model) YAML template. Which two are required to ensure the deployment can take place?
- **A. Use the `cloudformation package` command to package the deployment**
- **C. Place the function code at the root level of the working directory along with the YAML file**
- B. Use the `cloudformation package` command to deploy the template
- D. Place the function code in the .eb extensions folder

**Explanation:**
- **A.** The `cloudformation package` command packages your code and uploads it to S3, creating a deployable CloudFormation template.
- **C.** The Lambda function code must be locally accessible for the packaging process. Placing it in the root alongside the template is a standard practice.

---

#### 4. KMS Encryption & Decryption Process
**Question:** For a Java application using AWS KMS for encryption, which two steps must be done?
- A. Use the Customer master key to encrypt the data
- **B. Use the Customer master key to generate a data key for the encryption process**
- C. Use the Customer master key to decrypt the data
- **D. Use the generated data key to decrypt the data**

**Explanation:** This describes **envelope encryption**.
- **B.** You call `GenerateDataKey` with the Customer Master Key (CMK) to get a unique data key.
- **D.** You use this plaintext data key to encrypt your data. For decryption, you use the same data key (after first decrypting its encrypted version with the CMK). Never use the CMK directly on your data.

---

#### 5. CORS Headers for Web Browsers
**Question:** Which two headers are required by web browsers for API methods with CORS enabled?
- **A. Access-Control-Allow-Headers**
- B. Access-Control-Allow-CORS
- C. Access-Control-Expose-Headers
- D. Access-Control-Expose-Origin
- **E. Access-Control-Allow-Origin**

**Explanation:** When a browser makes a preflight (OPTIONS) request for CORS, the API must respond with at least these headers to specify which origins and headers are allowed.
- **A.** Lists the headers the client is allowed to send.
- **E.** Specifies which origins (domains) are permitted to access the resource.

---

#### 6. Shifting Traffic Between Lambda Versions
**Question:** You need to shift traffic slowly from one Lambda function version to another. Which two steps would you carry out?
- **A. Create an ALIAS with the `--routing-config` parameter**
- **B. Update the ALIAS with the `--routing-config` parameter**
- C. Create a version with the `--routing-config` parameter
- D. Update the version with the `--routing-config` parameter
- E. Update the function with the `-config` parameter

**Explanation:** Lambda **aliases** (not versions) support traffic shifting. You first create an alias pointing to a version, and then you update that alias's `--routing-config` to split traffic between two versions (e.g., 90% to old, 10% to new).

---

#### 7. Handling "ServiceException" in a Lambda State Function
**Question:** What is the best practice to handle a "ServiceException" in a Step Functions state machine that invokes a Lambda function?
- A. Use Lambda Catch code with only “ErrorEquals” string.
- B. Use Lambda Retry code with only “BackoffRate” string
- **C. Use Lambda Retry code with only “ErrorEquals” string.**
- D. Use Lambda Catch code with only “ResultPath” string.

**Explanation:** Transient errors like `ServiceException` (often temporary throttling or service issues) should be retried. The `Retry` block in a Step Function state requires the `"ErrorEquals"` field to specify which errors to retry. `"BackoffRate"` is optional.

---

#### 8. Retrieving Data from a Large DynamoDB Table
**Question:** Which three preferred options should be used for retrieving data from a steadily growing DynamoDB table?
- **A. Use the query operation**
- B. Use the Scan operation
- **C. Use the GetItem API command**
- **D. Use the BatchGetItem API command**

**Explanation:**
- **A. Query:** Efficiently retrieves items from a specific partition key.
- **C. GetItem:** Efficiently retrieves a single item by its full primary key.
- **D. BatchGetItem:** Efficiently retrieves multiple items by their full primary keys in a single call.
- **B. Scan** is inefficient as it examines every item in the table, using up provisioned throughput.

---

#### 9. AWS Cognito & Compromised Credentials
**Question:** There is a security requirement to ensure that if a user’s credentials are compromised, they must use a new password. Which two need to be in place?
- **A. Ensure to create a user pool in AWS Cognito**
- **B. Ensure to “Block use” for compromised credentials in the Advanced Security section**
- C. Ensure to “Block use” for compromised credentials in the Basic Security section
- D. Verify sign-in operation on Cognito using Secure Remote Password

**Explanation:**
- **A.** User Pools are the Cognito feature that manages user sign-up/sign-in.
- **B.** The "Adaptive authentication with risk-based adaptation" feature in the **Advanced Security** section can be configured to "Block" sign-in attempts that use known compromised credentials.

---

#### 10. Custom TTL for CloudFront Cache
**Question:** You need to ensure a custom value for the time an object is stored in the CloudFront cache. Which two options fulfil this?
- **A. Configure the origin to add an Expires header field to the object**
- B. Configure the Cloudfront distribution to add an Expires header field to the object
- **C. Specify a value for Minimum TTL in CloudFront cache behaviors**
- D. Specify a value for Minimum TTL in the origin object

**Explanation:** You can control cache duration from two sides:
- **A. Origin:** Your S3 bucket or application server can set `Cache-Control` or `Expires` headers on the objects themselves.
- **C. CloudFront:** In a cache behavior, you can set a `Minimum TTL` that CloudFront will use, overriding a lower TTL from the origin.

---

#### 11. Tracking S3 Objects for a User Over Time
**Question:** After an S3 object creation event, how can a developer locate all objects for a particular user during a certain time period?
- A. Use DynamoDB with Customer ID as PK and Server ID as SK.
- B. Use Amazon Redshift with Customer ID as PK and TS-Server as SK.
- **C. Use DynamoDB with Customer ID as PK and TS-Server as SK.**
- D. Use Amazon Redshift with Customer ID as PK and Server ID as SK.

**Explanation:** Redshift is a data warehouse, not suitable for this transactional query. DynamoDB is ideal. To find all objects for a `CustomerID` within a time range, you need:
- **Partition Key:** `CustomerID` (to get all data for that user).
- **Sort Key:** `TS-Server` (a timestamp). This allows you to perform a `Query` on the `CustomerID` and filter/query based on the sort key for the time range.

---

#### 12. API Gateway 502 Error
**Question:** An API Gateway integrated with Lambda returns a 502 error. What should the developer do to resolve it?
- A. Change the HTTP endpoint of the API to an HTTPS endpoint
- B. Change the format of the payload sent to the API Gateway
- **C. Change the format of the Lambda function response to the API call**
- D. Change the authorization header in the API call to access the Lambda function

**Explanation:** A common cause for a 502 (Bad Gateway) from API Gateway is a malformed response from the Lambda function when using a Lambda Proxy integration. The response must be in a very specific JSON format including `statusCode`, `body`, and `headers`.

---

#### 13. Securing a Website Without Increasing EC2 CPU
**Question:** How can a website behind an ELB be secured without raising the CPU burden on the EC2 web servers? (Select two.)
- A. Configure an Elastic Load Balancer with SSL pass-through.
- B. Configure SSL certificates on an Elastic Load Balancer.
- C. Configure an Elastic Load Balancer with a Loadable Storage System.
- D. Install SSL certificates on the EC2 instances.
- **E. Configure an Elastic Load Balancer with SSL termination.**

**Explanation:** **SSL Termination** (also called SSL Offloading) is the process where the Load Balancer handles the SSL decryption. The traffic between the ELB and the EC2 instances can be in plain HTTP, removing the SSL encryption/decryption overhead from the web servers. To do this, you must **B.** configure the SSL certificate on the ELB itself.

---

#### 14. Enabling New API Keys for API Gateway Usage Plans
**Question:** New users get a 403 error when using a newly generated API key. Existing users are unaffected. What change is needed?
- A. Call the `createDeployment` method.
- B. Call the `updateAuthorizer` method.
- C. Call the `importApiKeys` method.
- **D. Call the `createUsagePlanKey` method to associate the newly created API key with the correct usage plan.**

**Explanation:** In API Gateway, simply creating an API key is not enough. The key must be **associated with a Usage Plan** that specifies throttling and quota limits and is linked to a specific API stage. The `createUsagePlanKey` API makes this association.

---

#### 15. Secure Static Website on S3
**Question:** A website hosted on S3 must support secure browser connections (HTTPS). Which two steps must be performed?
- A. Create an ELB and configure it to direct traffic to the S3 bucket.
- **B. Create an Amazon CloudFront distribution. Set the S3 bucket as an origin.**
- C. Configure the ELB with an SSL/TLS certificate.
- **D. Configure the Amazon CloudFront distribution with an SSL/TLS certificate.**
- E. Configure the S3 bucket with an SSL/TLS certificate.

**Explanation:** S3 website endpoints do not support HTTPS. The standard solution is to use **CloudFront** in front of S3.
- **B.** Create a CloudFront distribution with the S3 bucket as its origin.
- **D.** Configure CloudFront with an SSL/TLS certificate (provided by AWS ACM) to serve content over HTTPS.

---

#### 16. Cost-Effective Pre-merge Builds
**Question:** What is the most cost-effective solution to build code before developers push it to the main branch?
- A. Configure an Amazon EC2 instance with the CodeBuild agent.
- **B. Configure CodeBuild jobs on AWS for each branch build process.**
- C. Configure the CodeBuild agent to build the code in the local system.
- D. Configure a Jenkins plugin for CodeBuild.

**Explanation:** AWS CodeBuild is a fully managed service, meaning you pay only for the compute time used during the build. There are no servers to manage. Configuring a build project to trigger on branch updates (e.g., on push to a feature branch) is a cost-effective and scalable solution.

---

#### 17. Efficient Read from DynamoDB GSI
**Question:** To get a list of objects from a DynamoDB Global Secondary Index (GSI) using the fewest read capacity units, which API call should be used?
- A. Scan operation using eventually-consistent reads
- B. Query operation using strongly-consistent reads
- **C. Query operation using eventually-consistent reads**
- D. Scan operation using strongly-consistent reads

**Explanation:**
- **Query** is always more efficient than **Scan** as it accesses items directly based on key conditions.
- **Eventually-Consistent Reads** consume half the read capacity units (RCUs) compared to Strongly-Consistent Reads for the same data size.

---

#### 18. S3 Performance for High PUT Requests
**Question:** Which S3 best practice would enhance speed for thousands of PUT requests per second to a single bucket?
- A. Prefix folder names with user id.
- B. Prefix file names with timestamps.
- C. Prefix file names with random hex hashes.
- **D. Prefix folder names with random hex hashes.**

**Explanation:** S3 scales by partitioning data across prefixes (the folders in the path). Using **randomized prefixes** (like a hex hash at the start of the folder name) ensures that requests are distributed across many partitions, preventing a bottleneck and allowing for higher aggregate throughput.

---

#### 19. Tracing Microservices with X-Ray
**Question:** How can a developer collect trace information across ECS microservices to view the architecture?
- **A. Build the container from the `amazon/aws-xray-daemon` base image. Use the AWS X-Ray SDK to instrument the application.**
- B. Install the Amazon CloudWatch agent on the container image.
- C. Install the AWS X-Ray daemon on each of the ECS instances.
- D. Configure AWS CloudTrail data events.

**Explanation:** To use X-Ray, you need two components:
1. **The X-Ray SDK** integrated into your application code to generate segments and traces.
2. **The X-Ray Daemon**, which collects the trace data from the SDK and sends it to the AWS X-Ray service. Running it as a separate container in your ECS task definition is a common pattern.

---

#### 20. API Gateway Throttling with Usage Plans
**Question:** How can a developer implement tiered request limits for registered developers with the least management overhead?
- A. Enable throttling for the API Gateway stage.
- B. Set up Amazon CloudWatch API logging and a Lambda function.
- C. Enable Amazon CloudWatch metrics and set up alarms.
- **D. Set up a default usage plan, and if a user chooses a larger package, create a custom plan and associate it with the user.**

**Explanation:** **API Gateway Usage Plans** are the built-in, managed feature designed specifically for this purpose. You create plans with different rate and burst limits, associate them with API stages, and then link API keys to these plans. This requires no custom code or complex alarm configurations.

---

#### 21. S3 Encryption with an Audit Trail
**Question:** Which S3 encryption method provides an audit trail of when and by whom the master key was used?
- A. Server-side encryption with Amazon S3 managed keys (SSE-S3)
- **B. Server-side encryption with AWS KMS managed keys (SSE-KMS)**
- C. Server-side encryption with customer-provided keys (SSE-C)
- D. Server-side encryption with self-managed keys

**Explanation:** **SSE-KMS** uses AWS Key Management Service. A key benefit of KMS is that it integrates with AWS CloudTrail, providing a detailed log of every use of the CMK, including who used it, when, and from which API call.

---

#### 22. How Envelope Encryption Works
**Question:** How does AWS KMS's Envelope Encryption work?
- **A. The Customer Master Key is used to encrypt/decrypt a data key. The Plaintext Data Key is used to encrypt customer data.**
- B. Two encryption keys are used. The Customer Master Key encrypts customer data...
- C. Two encryption keys are used. The Data Key encrypts customer data...
- D. The Customer Master Key is used to encrypt/decrypt a data key. The Encrypted Data Key is used to encrypt customer data.

**Explanation:** Envelope encryption is a two-step process:
1. Your CMK is used to encrypt ("envelope") a randomly generated **data key**. This results in an **encrypted data key**.
2. The **plaintext version** of that same data key is used to encrypt your actual customer data. You then store the encrypted data alongside the encrypted data key. The plaintext data key is discarded from memory after use.

---

#### 23. Low-Latency Caching for DynamoDB
**Question:** A stock trading app needs data retrieval in less than one millisecond. The current DynamoDB read time is too high. What is the simplest solution?
- A. Add local secondary indexes (LSIs).
- B. Store trading data in Amazon S3 and use Transfer Acceleration.
- C. Add retries with exponential back-off.
- **D. Use DynamoDB Accelerator (DAX) to cache trading data.**

**Explanation:** **DynamoDB Accelerator (DAX)** is an in-memory cache designed specifically for DynamoDB. It can deliver response times in microseconds for eventually consistent reads, which is the simplest and most effective way to achieve the required performance with minimal code changes.

---

#### 24. All-or-Nothing Updates in DynamoDB
**Question:** A serverless app must perform synchronized, all-or-nothing updates to various products in a DynamoDB table. Which solution satisfies this?
- A. Enable transactions for the DynamoDB table. Use the `BatchWriteItem` operation.
- **B. Use the `TransactWriteItems` operation to group the changes.**
- C. Set up a FIFO queue using Amazon SQS.
- D. Create a transaction table in an Amazon Aurora DB cluster.

**Explanation:** The `TransactWriteItems` API is DynamoDB's native transactional operation. It ensures that either all the actions in the transaction succeed, or none of them do, providing the required all-or-nothing guarantee. `BatchWriteItem` does not offer this atomicity.

---

#### 25. Minimal IAM Rights for ECS Microservices
**Question:** How can bare minimal rights be provided to each of two microservices on ECS EC2, one needing RDS access and the other DynamoDB?
- A. Set `ECS_ENABLE_TASK_IAM_ROLE` to false... grant instance profile role access to both.
- B. Set `ECS_ENABLE_TASK_IAM_ROLE` to false... grant instance profile role access to both.
- **C. Set `ECS_ENABLE_TASK_IAM_ROLE` to true... Run the first microservice with an IAM role for ECS tasks with read-only access for RDS. Run the second with a different IAM role for ECS tasks with read-only access to DynamoDB.**
- D. Set `ECS_ENABLE_TASK_IAM_ROLE` to true... Grant the instance profile role access to both.

**Explanation:** The best practice is to use **IAM Roles for ECS Tasks**. By setting `ECS_ENABLE_TASK_IAM_ROLE=true`, you allow each task definition to specify its own IAM role. This allows you to grant the first service's task role access only to RDS and the second service's task role access only to DynamoDB, following the principle of least privilege.

---

#### 26. Managing Temporary Files in Lambda
**Question:** A Lambda function needs 100 MB of temporary storage for transient files. How can the developer manage these files most efficiently?
- A. Store the files in EBS and delete them.
- B. Copy the files to EFS and delete them.
- **C. Store the files in the `/tmp` directory and delete the files at the end of the Lambda function.**
- D. Copy the files to an S3 bucket with a lifecycle policy.

**Explanation:** Each Lambda function receives 512 MB of non-persistent disk space in its own `/tmp` directory. This is the perfect place for temporary files. While it's good practice to clean it up, the space is automatically cleared when the execution environment is frozen or recycled.

---

#### 27. Creating a Role for EC2
**Question:** A developer creates a role using the AWS CLI `create-role` command. Which policy should be implemented to enable Amazon EC2 to assume the role?
- A. Managed policy
- **B. Trust policy**
- C. Inline policy
- D. Service control policy (SCP)

**Explanation:** The **Trust Policy** (or Assume Role Policy) is a resource-based policy attached to the IAM role itself. It defines *which principals* (like the EC2 service: `ec2.amazonaws.com`) are allowed to assume this role.

---

#### 28. Prioritizing Messages in SQS
**Question:** How can you guarantee that videos from paying users are processed before those from non-paying users?
- **A. Create two SQS queues: one for paying members, and one for non-paying members. Poll the paying member queue first.**
- B. Use SQS to set priorities on individual items within a single queue...
- C. ...use Amazon SNS to encode the videos.
- D. Create two Amazon SNS topics...

**Explanation:** A single SQS queue does not support message prioritization. The standard solution is to use **multiple queues**. Your application can then poll the high-priority queue first and more frequently, and only poll the low-priority queue when the high-priority one is empty.

---

#### 29. Automating Deletion from DynamoDB
**Question:** What is the simplest method to automatically delete obsolete session entries from a DynamoDB table?
- A. Write a script and schedule it as a cron job on an EC2 instance.
- **B. Add an attribute with the expiration time; enable the Time To Live (TTL) feature based on that attribute.**
- C. Each day, create a new table and delete the previous day‘s table.
- D. Add an attribute with the expiration time; name the attribute ItemExpiration.

**Explanation:** **DynamoDB TTL** is a built-in, managed feature that automatically deletes items after a specified timestamp. You simply enable TTL on a table and specify which attribute holds the expiration time. This is far simpler and more cost-effective than running a custom cleanup script.

---

#### 30. Preventing Duplicate SQS Message Processing
**Question:** Processing an SQS message takes longer than planned. How can you ensure other application instances don't get the same message?
- A. Make a `ReceiveMessage` call again.
- B. Issue a `DeleteMessage` call.
- C. Use `SendMessage` to pass the message to the dead letter queue.
- **D. Send a `ChangeMessageVisibility` call to extend VisibilityTimeout.**

**Explanation:** The `VisibilityTimeout` is the time a message is hidden from other consumers after being received. If your processing is taking longer than this timeout, you should call `ChangeMessageVisibility` to extend it, preventing the message from being re-delivered to another worker and processed twice.

---

#### 31. DynamoDB Capacity Unit Calculation
**Question:** A table has 7KB items. Read rate: 3 highly consistent reads/sec. Write rate: 10 items/sec. What capacity is needed?
- A. Read: 3 RCU, Write: 70 WCU
- **B. Read: 6 RCU, Write: 70 WCU**
- C. Read: 6 RCU, Write: 10 WCU
- D. Read: 3 RCU, Write: 10 WCU

**Explanation:**
- **Read Capacity (RCU):** 1 strongly consistent read of a 7KB item requires 2 RCUs (since 4KB chunks are rounded up). For 3 reads/sec: 3 * 2 = **6 RCUs**.
- **Write Capacity (WCU):** 1 write of a 7KB item requires 7 WCUs (1 WCU per 1KB). For 10 writes/sec: 10 * 7 = **70 WCUs**.

---

#### 32. Granting EC2 Access to a KMS Key
**Question:** An EC2 application needs to decrypt objects in an S3 bucket secured with SSE-KMS. Which two actions provide access? (Select two.)
- A. Write an S3 bucket policy that grants the bucket access to the key.
- **B. Grant access to the key in the IAM EC2 role attached to the application‘s EC2 instances.**
- **C. Write a key policy that enables IAM policies to grant access to the key.**
- D. Grant access to the key in the S3 bucket‘s ACL
- E. Create a Systems Manager parameter.

**Explanation:** For an IAM principal (like an EC2 role) to use a KMS key, two conditions must be met:
1. **C. Key Policy:** The key's resource policy must allow the IAM principal to use it. This is often done by including a statement that allows `kms:Decrypt` for the IAM role's ARN, or by allowing the broader `"kms:ViaService": "s3.amazonaws.com"` or by enabling IAM policies (the typical default).
2. **B. IAM Policy:** The IAM role itself must have an identity-based policy granting it permissions for the required KMS actions (e.g., `kms:Decrypt`).

---

#### 33. Debugging Asynchronous Lambda Failures
**Question:** A Lambda function that runs asynchronously fails after two retries. How can the developer debug the error?
- A. Configure AWS CloudTrail logging.
- **B. Configure Dead Letter Queues (DLQ) by sending events to Amazon SQS for investigation.**
- C. Configure Amazon Simple Workflow Service.
- D. Configure AWS Config.

**Explanation:** For asynchronous invocations, Lambda will retry a failed function up to two times. If it exhausts its retries, the event is lost unless a **Dead Letter Queue (DLQ)** is configured. By sending failed events to an SQS queue or SNS topic, you can isolate and analyze the problematic messages.

---

#### 34. Updating Lambda Function Code
**Question:** A developer uploads a new .ZIP file to S3, but Lambda still runs the old code. What is the least obtrusive fix?
- A. Create another Lambda function.
- **B. Call the `update-function-code` API.**
- C. Remove the earlier .ZIP file first, then add the new one.
- D. Call the `create-alias` API.

**Explanation:** Simply uploading a new .ZIP to S3 does not update the Lambda function. You must explicitly tell Lambda to use the new code. The `update-function-code` API command is the direct and correct way to do this, pointing it to the new S3 object. This minimizes downtime and management overhead.

---

#### 35. S3 Encryption with Key Control (No In-House Management)
**Question:** A company needs documents encrypted at rest in S3. They don't want to manage infrastructure but need control over keys for compliance. Which method?
- A. Server-side encryption with Amazon S3 managed keys (SSE-S3)
- B. Server-side encryption with customer-provided keys (SSE-C)
- **C. Server-side encryption with AWS KMS managed keys (SSE-KMS)**
- D. Client-side encryption

**Explanation:**
- **A (SSE-S3):** AWS fully manages the keys (less control).
- **B (SSE-C):** You provide the keys (you manage them in-house).
- **C (SSE-KMS):** A perfect middle ground. AWS manages the KMS infrastructure, but you have control over the CMK (you can create, rotate, and manage its policy), meeting the compliance requirement without in-house key management.

---

#### 36. High Read Performance for S3
**Question:** An application needs 100,000 read requests per second from an unencrypted S3 bucket. Priority is cost-effectiveness. What is the simplest method?
- **A. Create 20 or more prefixes in Amazon S3. Place files by prefixes. Read in parallel by prefixes.**
- B. Create 20 or more AWS accounts.
- C. Deploy Memcached on Amazon EC2.
- D. Copy all files to Amazon DynamoDB.

**Explanation:** S3 can achieve very high request rates by spreading requests across prefixes. AWS documentation states that you can achieve 100,000+ RPS by using at least 20 prefixes and reading in parallel. This is the simplest and most cost-effective solution as it uses S3's native performance capabilities without additional services.

---

#### 37. Maximum EC2 Instances for Kinesis Data Streams
**Question:** A Kinesis data stream has 6 shards after resharding. Using the KCL, what is the maximum number of EC2 instances that can process data from all shards?
- A. 12
- **B. 6**
- C. 4
- D. 1

**Explanation:** The Kinesis Client Library (KCL) ensures that each shard is processed by exactly one KCL worker. A single EC2 instance can run one or more workers. Therefore, the **maximum** number of instances that can be usefully deployed is equal to the number of shards (6), as having more would leave some instances idle.

---

#### 38. Encrypting EBS Without Performance Loss
**Question:** What steps should be taken to guarantee data is encrypted on EBS disks without sacrificing performance?
- **A. Configure the Amazon EC2 instance fleet to use encrypted EBS volumes for storing data.**
- B. Add logic to write all data to an encrypted Amazon S3 bucket.
- C. Add a custom encryption algorithm to the application.
- D. Create a new AMI with an encrypted root volume and store data to ephemeral disks.

**Explanation:** Modern EBS encryption (which uses AWS KMS) has a negligible performance impact. The simplest and most effective solution is to simply configure your EC2 instances to use encrypted EBS volumes. The encryption/decryption is handled by the EBS service on the underlying infrastructure.

---

#### 39. Exposing a SOAP Service via API Gateway
**Question:** A legacy service has a SOAP interface. How can it be exposed via API Gateway for external customers?
- **A. Create a RESTful API with the API Gateway; transform the incoming JSON into a valid XML message for the SOAP interface using mapping templates.**
- B. Create a RESTful API... pass the incoming JSON to the SOAP interface through an ALB.
- C. Create a SOAP API with the API Gateway...
- D. Create a SOAP API... transform the incoming XML...

**Explanation:** API Gateway is primarily a REST/HTTP API service. To integrate with a backend SOAP service, you create a REST API and use API Gateway's **mapping templates** (Velocity Template Language - VTL) to transform the incoming JSON request into the required XML SOAP envelope.

---

#### 40. Instantiating AWS Clients Outside Lambda Handler
**Question:** What is the advantage of instantiating AWS clients outside the scope of the Lambda handler?
- A. Legibility and stylistic convention
- **B. Taking advantage of connection re-use**
- C. Better error handling
- D. Creating a new instance per invocation

**Explanation:** The Lambda execution environment can be reused for multiple invocations. By initializing SDK clients and database connections **outside** the handler function, you can reuse these established connections across invocations. This improves performance and reduces latency, as you avoid the overhead of creating a new connection every time.

---

Good luck with your certification preparation! Use these notes to review the key concepts and services.
