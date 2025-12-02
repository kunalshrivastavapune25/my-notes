1. Question
A company has a development team that’s heavily relying on AWS CodeBuild, and CodeDeploy. The management would like to further automate its CI/CD process. They requested a system that monitors the status of each code change, from the moment it’s committed through to its deployment.

Which of the following AWS services will help you achieve this?

Amazon CodeGuru
AWS Elastic Beanstalk
AWS CodePipeline
AWS Fault Injection Simulator
Correct
AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This makes it a good choice for automating your CI/CD process and centrally monitoring application activity.

Moreover, AWS CodePipeline integrates with AWS CloudWatch, which provides a reliable, scalable, and flexible monitoring solution. You can create dashboards in CloudWatch to centrally monitor application activity and manage day-to-day development tasks.



The option that says: AWS Fault Injection Simulator is incorrect because this is just a managed service that is commonly used in chaos engineering, and not for application development. It enables you to perform fault injection experiments on your AWS workloads to improve the performance and resiliency of your applications.

The option that says: Elastic Beanstalk is incorrect because it is an orchestration service to quickly deploy and manage applications in AWS.

The option that says: Amazon CodeGuru is incorrect because this is simply a developer tool that provides intelligent recommendations to improve the quality of your codebase and for identifying an application’s most “expensive” lines of code in terms of resource intensiveness, CPU performance, and code efficiency.

 

References:

https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html

https://aws.amazon.com/codepipeline/

 

Check out this AWS CodePipeline Cheat Sheet:

https://tutorialsdojo.com/aws-codepipeline/


2. Question
An EBS-backed EC2 instance has been recently reported to contain a malware that could spread to your other instances. To fix this security vulnerability, you will need to attach its root EBS volume to a new EC2 instance which hosts a security program that can scan viruses, worms, Trojan horses, or spyware.

What steps would you take to detach the root volume from the compromised EC2 instance?

Detach the volume from the AWS Console. AWS takes care of unmounting the volume for you.
Unmount the volume from the OS and then detach.
Unmount the volume, stop the instance, and then detach.
Stop the instance then detach the volume.
Correct
You can detach an Amazon EBS volume from an instance explicitly or by terminating the instance. However, if the instance is running, you must first unmount the volume from the instance.

If an EBS volume is the root device of an instance, you must stop the instance before you can detach the volume.

The options that say unmount the volume from the OS and then detach and unmount the volume, stop the instance, and then detach are both incorrect because you can’t unmount the root volume on a running instance.

The option that says: Detach the volume from the AWS Console. AWS takes care of unmounting the volume for you is incorrect because unmounting the volume is not managed by AWS.

 

Reference:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html

 

Check out this Amazon EC2 Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/


4. Question
A developer is building a photo-sharing application that automatically enhances images uploaded by users to Amazon S3. When a user uploads an image, its S3 path is sent to an image-processing application hosted on AWS Lambda. The Lambda function applies the selected filter to the image and stores it back to S3.

If the upload is successful, the application will return a prompt telling the user that the request has been accepted. The entire processing typically takes an average of 5 minutes to complete, which causes the application to become unresponsive.

Which of the following is the MOST suitable and cost-effective option which will prevent the application from being unresponsive?

Configure the application to asynchronously process the requests and use the default invocation type of the Lambda function.
Use a combination of Lambda and Step Functions to orchestrate service components and asynchronously process the requests.
Use AWS Serverless Application Model (AWS SAM) to allow asynchronous requests to your Lambda function.

Configure the application to asynchronously process the requests and change the invocation type of the Lambda function to Event.
Correct
AWS Lambda supports synchronous and asynchronous invocation of a Lambda function. You can control the invocation type only when you invoke a Lambda function (referred to as on-demand invocation). The following examples illustrate on-demand invocations:

– Your custom application invokes a Lambda function.

– You manually invoke a Lambda function (for example, using the AWS CLI) for testing purposes.

In both cases, you invoke your Lambda function using the Invoke operation, and you can specify the invocation type as synchronous or asynchronous.

When you use AWS services as a trigger, the invocation type is predetermined for each service. You have no control over the invocation type that these event sources use when they invoke your Lambda function.

In the Invoke API, you have 3 options to choose from for the InvocationType:

RequestResponse (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.

Event – Invoke the function asynchronously. Send events that fail multiple times to the function’s dead-letter queue (if it’s configured). The API response only includes a status code.

DryRun – Validate parameter values and verify that the user or role has permission to invoke the function.

By configuring the application to asynchronously process requests by changing the invocation type of the Lambda function to “Event,” the function can run in the background without blocking the main application. When the processing is complete, Lambda can store it back to S3 and trigger another event, such as a notification to the user that the image is ready.



Hence, the correct answer is to configure the application to asynchronously process the requests and change the invocation type of the Lambda function to Event.

Configuring the application to asynchronously process the requests and use the default invocation type of the Lambda function is incorrect because this will invoke your Lambda function synchronously. The default invocation type is RequestResponse which invokes the function synchronously and keeps the connection open until the function returns a response or times out.

Using AWS Serverless Application Model (AWS SAM) to allow asynchronous requests to your Lambda function is incorrect because AWS SAM just is an open-source framework that you can use to build serverless applications on AWS.

Using a combination of Lambda and Step Functions to orchestrate service components and asynchronously process the requests is incorrect because the AWS Step Functions service just lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Although this can be a valid solution, it is not cost-effective since the application does not have a lot of components to orchestrate. Lambda functions can effectively meet the requirements in this scenario without using Step Functions by processing the requests asynchronously.

 

References:

https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html

https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html

 

Check out this AWS Lambda Cheat Sheet:

https://tutorialsdojo.com/aws-lambda/


7. Question
An application is sending thousands of log files to an S3 bucket everyday. The request to retrieve the list of objects using the AWS CLI aws s3api list-objects command is timing out due to the high volume of data being fetched. In order to rectify this issue, you have to use pagination to control the number of results returned on your request.

Which of the following parameters should you include in CLI command for this scenario? (Select TWO.)


--summarize

--page-size

--size-only

--exclude

--max-items
Correct
For commands that can return a large list of items, the AWS Command Line Interface (AWS CLI) adds three options that you can use to control the number of items included in the output when the AWS CLI calls a service’s API to populate the list. By default, the AWS CLI uses a page size of 1000 and retrieves all available items.

If you see issues when running list commands on a large number of resources, the default page size of 1000 might be too high. This can cause calls to AWS services to exceed the maximum allowed time and generate a “timed out” error. You can use the --page-size option to specify that the AWS CLI request a smaller number of items from each call to the AWS service. The CLI still retrieves the full list, but performs a larger number of service API calls in the background and retrieves a smaller number of items with each call. This gives the individual calls a better chance of succeeding without a timeout.

To include fewer items at a time in the AWS CLI output, use the --max-items option. The AWS CLI still handles pagination with the service as described above, but prints out only the number of items at a time that you specify. If the number of items output is fewer than the total number of items returned by the underlying API calls, the output includes a NextToken that you can pass to a subsequent command to retrieve the next set of items.

Hence, the correct ones that you should include in the AWS CLI command are the --page-size and --max-items parameters.

The –size-only parameter is incorrect because this just accepts a boolean value and is typically used along with “s3 sync” command. It makes the size of each key the only criteria to use to decide whether to sync from source to destination.

The –exclude parameter is incorrect because it simply makes Amazon S3 exclude all files or objects that match a specified pattern from the result of the command.

The –summary parameter is incorrect because this only displays the summary information (number of objects, total size) of objects returned from an “s3 ls” command.

 

References:

https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html

https://docs.aws.amazon.com/cli/latest/reference/s3/index.html#cli-aws-s3


9. Question
A company has a global multi-player game with a multi-master DynamoDB database topology which stores data in multiple AWS regions. You were assigned to develop a real-time data analytics application which will track and store the recent changes on all the tables from various regions. Only the new data of the recently updated item is needed to be tracked by your application.

Which of the following is the MOST suitable way to configure the data analytics application to detect and retrieve the updated database entries automatically?


Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application.

Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application.

Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB.

Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB.
Correct
DynamoDB Streams provides a time-ordered sequence of item-level changes in any DynamoDB table. The changes are de-duplicated and stored for 24 hours. Applications can access this log and view the data items as they appeared before and after they were modified, in near real time.

The Kinesis Adapter is the recommended way to consume streams from DynamoDB for real-time processing. The DynamoDB Streams API is intentionally similar to that of Kinesis Streams, a service for real-time processing of streaming data at a massive scale. You can write applications for Kinesis Streams using the Kinesis Client Library (KCL). The KCL simplifies coding by providing useful abstractions above the low-level Kinesis Streams API. As a DynamoDB Streams user, you can leverage the design patterns found within the KCL to process DynamoDB Streams shards and stream records. To do this, you use the DynamoDB Streams Kinesis Adapter. The Kinesis Adapter implements the Kinesis Streams interface, so that the KCL can be used for consuming and processing records from DynamoDB Streams.



When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:

KEYS_ONLY – Only the key attributes of the modified item are written to the stream.

NEW_IMAGE – The entire item, as it appears after it was modified, is written to the stream.

OLD_IMAGE – The entire item, as it appeared before it was modified, is written to the stream.

NEW_AND_OLD_IMAGES – Both the new and the old item images of the item are written to the stream.

Hence, the correct answer is: Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE then use Kinesis Adapter in the application to consume streams from DynamoDB.

The option that says: Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application is incorrect. Using Lambda for real-time data analytics is not a suitable solution for this scenario since it reads records in batches. A more appropriate service to use is the Kinesis service. In addition, using the StreamViewType of NEW_AND_OLD_IMAGE is wrong since this will send both the old and the new values of the item. Remember that it is specifically mentioned in the scenario that only the new values should be tracked.

The option that says: Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application is incorrect because just like what is mentioned above, it is better to use Kinesis instead of Lambda for the real-time data analytics application.

The option that says: Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB is incorrect because this will send both the old and the new values of the item to the data analytics application. The correct StreamViewType to use here should be NEW_IMAGE.

 

References:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.KCLAdapter.html

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html

 

Check out this Amazon DynamoDB Cheat Sheet:

https://tutorialsdojo.com/amazon-dynamodb/

 

AWS Lambda Integration with Amazon DynamoDB Streams:

https://tutorialsdojo.com/aws-lambda-integration-with-amazon-dynamodb-streams/


10. Question
A developer is creating an analytics REST API service that is powered by API Gateway. Analysts from a separate AWS account must interact with the service through an IAM role. The IAM role already has a policy that grants permission to invoke the API.

What else should the developer do to meet the requirement without too much overhead?


Create an API Key for the API. Attach a resource policy to the API that grants permission to the specified IAM role to invoke the GetAPIKeys action.

Create a Lambda function authorizer for the API. In the Lambda function, write a logic that verifies the requester’s identity by extracting the information from the context object.
Create a Cognito User Pool authorizer. Add the IAM role to the user pool. Authenticate the requester’s identity using Cognito. Ask the analysts to pass the token returned by Cognito in their request headers.

Set AWS_IAM as the method authorization type for the API. Attach a resource policy to the API that grants permission to the specified IAM role to invoke the execute-api:Invoke action.
Correct
By using AWS_IAM as the method authorization type, it ensures that the API can only be accessed by IAM identities such as IAM users or IAM roles. Attaching a resource policy to the API that grants permission to the specified IAM role to invoke the execute-api:Invoke action allows the specified IAM role to make authorized requests to the API while denying access to any other unauthorized users or roles.

{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"AWS": [
"arn:aws:iam::account-id:role/Analyst"
]
},
"Action": "execute-api:Invoke",
"Resource": [
"execute-api:/stage/GET/reports"
]
}
]
}

This combination of method authorization and resource policy provides an additional layer of security for the API.

Hence, the correct answer in this scenario is to Set AWS_IAM as the method authorization type for the API. Attach a resource policy to the API that grants permission to the specified IAM role to invoke the execute-api:Invoke action.

The option that says: Create an API Key for the API. Attach a resource policy to the API that grants permission to the specified IAM role to invoke the GetAPIKeys action is incorrect API Keys are just a way of identifying the calling parties that you trust, but they are not intended to be used to grant permissions to an IAM role.

The option that says: Create a Lambda function authorizer for the API. In the Lambda function, write a logic that verifies the requester’s identity by extracting the information from the context object is incorrect. While this may be possible, Lambda function authorizer is more suitable for custom authorization scheme that uses a bearer token authentication strategy such as OAuth or SAML. Additionally, this approach requires you to write, test, and maintain custom authentication and authorization code, which can be complex and time-consuming.

The option that says: Create a Cognito User Pool authorizer. Add the IAM role to the user pool. Authenticate the requester’s identity using Cognito. Ask the analysts to pass the token returned by Cognito in their request headers is incorrect. Adding a Cognito User Pool authorizer is unnecessary since the API will be accessed through an IAM role.

 

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-examples.html#apigateway-resource-policies-cross-account-example

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-authorization-flow.html

 

Check out this AWS API Gateway Sheet:

https://tutorialsdojo.com/amazon-api-gateway/


11. Question
A startup wants an application that triggers processes in response to customer orders and inventory updates using AWS Lambda and Amazon EventBridge. The application requires a Lambda function to send the specific events to an Amazon EventBridge event bus. The developer uses the AWS SDK to call the PutEvents action on EventBridge. Upon deployment, the developer notices AccessDeniedException errors in the event logs, which is the reason why the function is not functioning as intended.

Which solution will help the developer in resolving the issue?


Adjust the AWS Lambda function’s execution role to grant it permissions for the PutEvents action on EventBridge.

Update the developer’s IAM role by including permission to explicitly allow the PutEvents operation on EventBridge.

Implement a resource-based policy on the Lambda function that grants necessary permissions to perform the PutEvents action on EventBridge.
Establish a Virtual Private Cloud (VPC) peering connection to facilitate communication between AWS Lambda and EventBridge.
Correct
AWS Lambda is a service that allows you to run your code without managing any servers. It only runs your code when it is needed and can scale from a few requests per day to thousands per second automatically. Moreover, AWS Lambda functions can be triggered by various AWS services, such as Amazon EventBridge. Amazon EventBridge is a serverless event bus that can connect application data from your apps, SaaS, and AWS services. Using EventBridge, you can build event-driven architectures that are highly scalable and decoupled from each other. This approach can make your applications more resilient and flexible.



Lambda functions often need to interact with other AWS services, such as sending events to an EventBridge bus. However, to access and perform actions on these services, the function requires the necessary permissions. This is where the concept of an execution role comes into play. An execution role is an IAM role that grants the Lambda function permissions to access AWS services and resources. By adjusting the execution role of a Lambda function to include permissions for the PutEvents action on EventBridge, the function can safely interact with EventBridge. This method follows the AWS best practice of granting the least privilege, ensuring that the function only has the permissions needed to perform its designated tasks. As a result, the security posture of the application is enhanced.

In the provided scenario, where a developer’s AWS Lambda function encounter AccessDeniedException errors when attempting to publish events to an EventBridge event bus, adjusting the Lambda function’s execution role is the correct approach to resolving the issue. By granting the execution role permission for the PutEvents action on EventBridge, the Lambda function is authorized to execute the PutEvents call successfully. This solution emphasizes the importance of IAM roles in managing permissions within AWS environments, ensuring secure and efficient access management for serverless applications.

Hence, the correct answer is: Adjust the AWS Lambda function’s execution role to grant it permissions for the PutEvents action on EventBridge.

The option that says: Establish a Virtual Private Cloud (VPC) peering connection to facilitate communication between AWS Lambda and EventBridge is incorrect. VPC peering is a networking feature that allows traffic to be routed between two VPCs using private IP addresses. However, this option does not address the underlying issue, which is related to IAM permissions and not network connectivity. Amazon EventBridge is a serverless event bus service that doesn’t require VPC peering with AWS Lambda for connectivity. The AccessDeniedException error indicates a permissions issue that needs IAM configuration adjustments rather than network infrastructure changes.

The option that says: Update the developer’s IAM role by including permission to explicitly allow the PutEvents operation on EventBridge is incorrect because the permissions required to execute AWS service operations from within an AWS Lambda function are determined by the execution role attached to the Lambda function itself, not the IAM role of the developer. The execution role provides the Lambda function with the necessary AWS credentials to interact with other AWS services under the permissions defined in that role. Modifying the programmer’s IAM role would not grant the Lambda function the permissions it needs to interact with EventBridge.

The option that says: Implement a resource-based policy on the Lambda function that grants necessary permissions to perform the PutEvents action on EventBridge is incorrect. Lambda functions do not use resource-based policies to grant permissions to access other AWS services. Instead, permissions are primarily managed through the execution role.

References:

https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html

https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html

Check out these AWS Lambda and Amazon EventBridge Cheat Sheets:

https://tutorialsdojo.com/aws-lambda/

https://tutorialsdojo.com/amazon-eventbridge/


14. Question
You are working as an IT Consultant for a top investment bank in Europe which uses several serverless applications in their AWS account. They just launched a new API Gateway service with a Lambda proxy integration and you were instructed to test out the new API. However, you are getting a Connection refused error whenever you use this Invoke URL http://779protaw8.execute-api.us-east-1.amazonaws.com/tutorialsdojo/ of the API Gateway.

Which of the following is the MOST likely cause of this issue?

You are not using WebSocket in invoking the API.
You are not using FTP in invoking the API.
You are not using HTTPS in invoking the API.
You are not using HTTP/2 in invoking the API.
Correct
All of the APIs created with Amazon API Gateway expose HTTPS endpoints only. Amazon API Gateway does not support unencrypted (HTTP) endpoints. By default, Amazon API Gateway assigns an internal domain to the API that automatically uses the Amazon API Gateway certificate. When configuring your APIs to run under a custom domain name, you can provide your own certificate for the domain.



Calling a deployed API involves submitting requests to the URL for the API Gateway component service for API execution, known as execute-api. The base URL for REST APIs is in the following format:

 https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/
where {restapi_id} is the API identifier, {region} is the region, and {stage_name} is the stage name of the API deployment.

Hence, the most likely cause of the issue in the scenario is that you are not using HTTPS in invoking the API.

The option that says: you are not using HTTP/2 in invoking the API is incorrect because API Gateway only supports HTTPS.

The option that says: you are not using FTP in invoking the API is incorrect because API Gateway is using HTTPS to expose the APIs. FTP is primarily used for accessing file servers and not Web APIs.

The option that says: you are not using WebSocket in invoking the API is incorrect because all of the APIs created with Amazon API Gateway expose HTTPS endpoints only.

 

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html

https://aws.amazon.com/api-gateway/faqs/

 

Check out this Amazon API Gateway Cheat Sheet:

https://tutorialsdojo.com/amazon-api-gateway/


16. Question
A company has an application hosted in an On-Demand EC2 instance in your VPC. The developer has been instructed to create a shell script that fetches the instance’s associated public and private IP addresses.

What should the developer do to complete this task?

Get the public and private IP addresses from AWS CloudTrail.

Get the public and private IP addresses from the instance metadata service using the http://169.254.169.254/latest/meta-data/ endpoint.

Get the public and private IP addresses from the instance user data service using the http://169.254.169.254/latest/userdata/ endpoint.
Get the public and private IP addresses from Amazon CloudWatch.
Correct
Instance metadata is data about your EC2 instance that you can use to configure or manage the running instance. Because your instance metadata is available from your running instance, you do not need to use the Amazon EC2 console or the AWS CLI. This can be helpful when you’re writing scripts to run from your instance. For example, you can access the local IP address of your instance from instance metadata to manage a connection to an external application.



To view the private IPv4 address, public IPv4 address, and all other categories of instance metadata from within a running instance, use the following URL: http://169.254.169.254/latest/meta-data/.

Hence, the correct answer is: Get the public and private IP addresses from the instance metadata service using the http://169.254.169.254/latest/meta-data/ endpoint.

The option that says: Get the public and private IP addresses from Amazon CloudWatch is incorrect because there is no direct way to fetch the public and private IP addresses of the EC2 instance using CloudWatch.

The option that says: Get the public and private IP addresses from AWS CloudTrail is incorrect because CloudTrail is primarily used to track the API activity of each AWS service. Just like CloudWatch, there is no easy way to get the associated IP addresses of the EC2 instance using CloudTrail.

The option that says: Get the public and private IP addresses from the instance user data service using the http://169.254.169.254/latest/userdata/ endpoint is incorrect because a user data is mainly used to perform common automated configuration tasks and run scripts after the instance starts. You will not find the associated IP addresses of the EC2 instance from its user data. You have to use the metadata service instead.

 

References:

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html

 

Check out this Amazon EC2 Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/


17. Question
A developer is managing a serverless application orchestrated by AWS Step Functions. One of the Lambda functions sends an API call to a third-party payment service, which takes some time to complete. The Step Functions workflow needs to pause while the service validates the payment. It should only resume after the service sends a notification to a webhook endpoint.

Which combination of actions will fulfill the requirements in the most cost-effective manner? (Select Two)


Configure the Lambda function task state to use the waitForTaskToken option. Retrieve the task token from the context object of the state machine and include it as part of the Lambda function’s payload body.

Configure the webhook handler to call the SendTaskSuccess method after a successful notification.

Configure the webhook handler to call the SendTaskHeartbeat method after a successful notification.
Use a Wait State to pause the execution of the workflow. Configure the webhook handler to invoke the Lambda function synchronously.
Set the invocation method of the Lambda function task state to asynchronous. Create an AWS SQS queue and configure the webhook handler to send the payment service’s response to the queue. Use a combination of Wait State and Choice State to poll the queue.
Correct
In AWS Step Functions, the waitForTaskToken option allows a task to be paused until an external system signals its completion. When a task is configured with this option, Step Functions generates a unique token, which can be retrieved from the context object of the state machine. This token, for instance, can be stored in a data store for reference.

The diagram below depicts how waitForTaskToken is used for an SQS task state.



An external system, such as a webhook handler can then reference the token and call the SendTaskSuccess or SendTaskFailure method to signal Step Functions to resume the workflow. When the workflow is in a paused state, you’re not billed for the time the workflow is paused, making it a cost-effective method for awaiting external processes or events.

Hence, the correct answers are:

Configure the Lambda function task state to use the waitForTaskToken option. Retrieve the task token from the context object of the state machine and include it as part of the Lambda function’s payload body.
Configure the webhook handler to call the SendTaskSuccess method after a successful notification.
The option that says: Set the invocation method of the Lambda function task state to asynchronous. Create an AWS SQS queue and configure the webhook handler to send the payment service’s response to the queue. Use a combination of Wait State and Choice State to poll the queue is incorrect. While this solution may work, every iteration involving the Wait State and Choice State incurs a cost as a state transition. If the third-party service takes an unpredictable amount of time, the state machine could go through multiple cycles of waiting and checking the SQS queue, resulting in a higher cost.

The option that says: Use a Wait State to pause the execution of the workflow. Configure the webhook handler to invoke the Lambda function synchronously is incorrect. A fixed Wait State is less cost-effective in scenarios where the waiting duration is unpredictable. If the third-party service finishes earlier than the wait duration, you’re paying for unused time. If it takes longer, the workflow might proceed before the task is complete.

The option that says: Configure the webhook handler to call the SendTaskHeartbeat method after a successful notification is incorrect because this method is simply used for keeping tasks alive and preventing them from timing out. It also does not signal completion.

 

References:

https://aws.amazon.com/blogs/compute/building-cost-effective-aws-step-functions-workflows/

https://docs.aws.amazon.com/step-functions/latest/dg/callback-task-sample-sqs.html

https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html

 

Check out this AWS Step Functions Cheat Sheet:

https://tutorialsdojo.com/aws-step-functions/


19. Question
A developer is building a prototype microservices that are running as tasks in an Amazon ECS Cluster. His manager instructed him to define a task placement strategy which needs to be both cost and resource efficient. The task placement should minimize the number of instances in use which will keep the cost down since high availability is not much of a concern for this prototype.

What should the developer implement to meet the above requirements?


Distribute tasks among all registered EC2 instances based on the least available amount of CPU or memory using the binpack task placement strategy.

Distribute tasks evenly across all available EC2 instances using the spread task placement strategy.

Place tasks randomly using the random task placement strategy.
Distribute tasks evenly across Availability Zones, and then re-distribute the tasks among EC2 instances based on the least available amount of CPU/memory within each Availability Zone.
Correct
The binpack strategy tries to fit your workloads in as few instances as possible. It gets its name from the bin packing problem where the goal is to fit objects of various sizes in the smallest number of bins. It is well suited to scenarios for minimizing the number of instances in your cluster, perhaps for cost savings, and lends itself well to automatic scaling for elastic workloads, to shut down instances that are not in use.

A task placement strategy is an algorithm for selecting instances for task placement or tasks for termination. Task placement strategies can be specified when either running a task or creating a new service.

Amazon ECS supports the following task placement strategies:

binpack – Place tasks based on the least available amount of CPU or memory. This minimizes the number of instances in use.

random – Place tasks randomly.

spread – Place tasks evenly based on the specified value. Accepted values are attribute key-value pairs, instanceId, or host.



When you use the binpack strategy, you must also indicate if you are trying to make optimal use of your instances’ CPU or memory. This is done by passing an extra field parameter, which tells the task placement engine which parameter to use to evaluate how “full” your “bins” are. It then chooses the instance with the least available CPU or memory (depending on which you pick). If there are multiple instances with this CPU or memory remaining, it chooses randomly.

By spreading tasks among your EC2 instances using the binpack strategy, you can minimize costs and resource consumption since this strategy maximizes available CPU/memory of your already running instances.

Hence, the correct answer is: Distribute tasks among all registered EC2 instances based on the least available amount of CPU or memory using the binpack task placement strategy. 

The option that says: Distribute tasks evenly across all available EC2 instances using the spread task placement strategy is incorrect because this strategy is typically used to achieve high availability by making sure that multiple copies of a task are scheduled across multiple instances based on attributes such as Availability Zones. Since the scenario is focused on cost rather than availability, this option is clearly not suitable for this scenario.

The option that says: Place tasks randomly using the random task placement strategy is incorrect. Random task placement just ensures tasks are run on instances with sufficient resources to complete them. Binpack has better cost-savings since it strategically places tasks in as few instances as possible.

The option that says: Distribute tasks evenly across Availability Zones, and then re-distributing the tasks among EC2 instances based on the least available amount of CPU/memory within each Availability Zone is incorrect. Although it will meet the required task placement, this method will use more unnecessary EC2 instances. Take note that the scenario requires you to minimize the number of instances in use, which will keep the cost down.

 

References:

https://aws.amazon.com/blogs/compute/amazon-ecs-task-placement/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html

 

Check out this Amazon ECS Cheat Sheet:

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/


22. Question
Your serverless AWS Lambda functions are integrated with Amazon API gateway using Lambda proxy integration. The API caching feature is enabled in the API Gateway with a TTL value of 300 seconds. A client would like to fetch the latest data from your endpoints every time a request is sent and invalidate the existing cache.

What should the client do in order to get the latest data?

Modify cache TTL value to a shorter period.

Have the client send a request with the Cached: false header.
Override API caching by allowing the client to send requests to the endpoint directly.

Have the client send a request with the Cache-Control: max-age=0 header.
Correct
A client of your API can invalidate an existing cache entry and reload it from the integration endpoint for individual requests. The client must send a request that contains the Cache-Control: max-age=0 header.

 



 

The client receives the response directly from the integration endpoint instead of the cache, provided that the client is authorized to do so. This replaces the existing cache entry with the new response, which is fetched from the integration endpoint.

Modifying the TTL value for the cached data to a lower value is incorrect because there is still no guarantee that the client will submit a request after the cache has expired. Also, you will not be fully utilizing the purpose of API caching since new data will be fetched from the endpoint more often. The best solution for this scenario is to use the Cache-Control header instead.

Allowing the client to access the endpoint directly is incorrect because the purpose of placing API Gateway in-front of your endpoints is to not expose your endpoints to the public and risk security issues. It also provides you the additional benefits of not burdening your endpoints with a massive number of requests and allowing developer-friendly data exchanges through APIs.

Having the client send a request with the Cached: false header is incorrect because this is a custom header. The correct way is to configure the Cache-Control: max-age=0 header instead.

 

Reference:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#override-api-gateway-stage-cache-for-method-cache

 

Check out this Amazon API Gateway Cheat Sheet:

https://tutorialsdojo.com/amazon-api-gateway/


23. Question
An application experiences a sluggish response whenever there is a surge in requests involving read queries. The developer has already attempted to improve performance by optimizing the queries. However, the problem still persists even after applying the change. The application is hosted in an Amazon ECS Cluster and uses a MySQL database backed by Amazon RDS.

Which of the following could the developer do to resolve the performance issue? (Select TWO.)

Replace the database with Amazon MemoryDB for Redis
Set up read replicas for the RDS database instance and route read queries to these replicas.
Cache the database response using Amazon CloudFront.
Implement a Multi-AZ deployment configuration for the RDS DB instance.
Implement database caching using Amazon ElastiCache.
Correct
Amazon RDS Read Replicas provide enhanced performance and durability for the database (DB) instances. This feature makes it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. You can create one or more replicas of a given source DB Instance and serve high-volume application read traffic from multiple copies of your data, thereby increasing aggregate read throughput.

You can reduce the load on your source DB instance by routing read queries from your applications to the read replica. Read replicas allow you to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads.



Because read replicas can be promoted to master status, they are useful as part of a sharding implementation. To shard your database, add a read replica and promote it to master status, then, from each of the resulting DB Instances, delete the data that belongs to the other shard.

In-memory data caching can be one of the most effective strategies to improve your overall application performance and reduce your database costs. Caching can be applied to any type of database, including relational databases such as Amazon RDS or NoSQL databases such as Amazon DynamoDB, MongoDB, and Apache Cassandra. The best part of caching is that it’s minimally invasive to implement, and by doing so, your application performance regarding both scale and speed is dramatically improved.

Amazon ElastiCache offers fully managed Redis and Memcached. Seamlessly deploy, run, and scale popular open-source compatible in-memory data stores. Build data-intensive apps or improve the performance of your existing apps by retrieving data from high throughput and low latency in-memory data stores.

Hence, the correct answers in this scenario are:

 – Set up read replicas for the RDS database instance and route read queries to these replicas.

 – Implement database caching using Amazon ElastiCache.

The option that says: Replace the database with Amazon MemoryDB for Redis is incorrect because Redshift is primarily used for online analytics processing applications (OLAP) and as a data warehouse. Hence, this will not improve the read performance of your application.

The option that says: Cache the database response using Amazon CloudFront is incorrect. Although CloudFront can provide caching and for CDN, it is not suitable to be used for database caching. Using Read Replicas and ElastiCache are more appropriate features to be used in this scenario.

The option that says: Implement a Multi-AZ deployment configuration for the RDS DB instance is incorrect because configuring a Multi-AZ RDS just improves the availability of the database but does not drastically improve the read performance, which Read Replicas can provide.

 

References:

https://aws.amazon.com/caching/database-caching/

https://aws.amazon.com/rds/details/read-replicas/

https://aws.amazon.com/elasticache/

 

Check out these Amazon RDS and Elasticache Cheat Sheets:

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

https://tutorialsdojo.com/amazon-elasticache/

 

Tutorials Dojo’s AWS Certified Developer Associate Exam Study Guide:

https://tutorialsdojo.com/aws-certified-developer-associate/


24. Question
A developer is instructed to collect data on the number of times that web visitors click the advertisement link of a popular news website. A database entry containing the count will be incremented for every click. Given that the website has millions of readers worldwide, your database should be configured to provide optimal performance to capture all the click events.

What is the BEST service that the developer should implement in this scenario?

Use Amazon RDS for the database and setup SQL AUTO_INCREMENT on your tables.

Set up Amazon DynamoDB for the database and implement atomic counters for UpdateItem operation of the website counter.
Take advantage of Amazon Aurora's performance speed and AUTO_INCREMENT feature for item updates.
Launch an Amazon Redshift for the database and apply a step count of 1 for the IDENTITY column.
Correct
Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. Since fast performance is one of the requirements asked in the scenario, DynamoDB should be an option to consider.

In DynamoDB, an item is a collection of attributes. Each attribute has a name and a value. An attribute value can be a scalar, a set, or a document type. DynamoDB provides four operations for basic create/read/update/delete (CRUD) functionality:

PutItem      – create an item.

GetItem      – read an item.

UpdateItem – update an item.

DeleteItem – delete an item.

You can use the UpdateItem operation to implement an atomic counter—a numeric attribute that is incremented, unconditionally, without interfering with other write requests. With an atomic counter, the numeric value will increment each time you call UpdateItem.



For example, you might use an atomic counter to keep track of the number of visitors to a website. In this case, your application would increment a numeric value, regardless of its current value. If an UpdateItem operation should fail, the application could simply retry the operation. This would risk updating the counter twice, but you could probably tolerate a slight overcounting or undercounting of website visitors.

Hence, the correct answer is to setup Amazon DynamoDB for the database and implement atomic counters for the UpdateItem operation of the website counter.

Using Amazon RDS for the database and setting up SQL AUTO_INCREMENT on your tables is incorrect because RDS is not scalable enough to handle millions of data being submitted by readers worldwide. Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table. This is often the primary key field that we would like to be created automatically every time a new record is inserted. Since you would not want to add a new database entry for every link click and immediately consume all your storage space, it would be better to use DynamoDB’s atomic counter instead.

Launching an Amazon Redshift for the database and applying a step count of 1 for the IDENTITY column is incorrect because Redshift is more suited for data warehousing demands that need parallel execution capabilities and columnar storage types.

Taking advantage of Amazon Aurora’s performance speed and AUTO_INCREMENT feature for item updates is incorrect. Although Aurora is a scalable database service, using the AUTO_INCREMENT feature of SQL does not suit the scenario’s requirement. Auto-increment simply allows a unique number to be generated automatically when a new record is inserted into a table.

 

References:

https://aws.amazon.com/dynamodb/

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.AtomicCounters

https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html

 

Check out this Amazon DynamoDB Cheat Sheet:

https://tutorialsdojo.com/amazon-dynamodb/


27. Question
A developer has just finished writing a serverless application using AWS SAM (Serverless Application Model) on a local machine. There is a SAM template ready and the corresponding Lambda function code in a directory. The developer now wants to deploy this application to AWS.

Which combination of steps should the developer follow to successfully deploy the SAM application? (Select THREE)

Build the SAM template in an Amazon EC2 instance.
Build the SAM template in the local environment
Deploy the SAM template from AWS CodePipeline.
Deploy the SAM template from an Amazon S3 bucket.
Build the SAM template using the AWS SDK for AWS CodeDeploy.
Package the SAM application for deployment.
Correct
AWS SAM uses AWS CloudFormation as the underlying deployment mechanism. You can deploy your application by using AWS SAM command line interface (CLI) commands. You can also use other AWS services that integrate with AWS SAM to automate your deployments.



The typical AWS SAM deployment workflow starts with the sam build command, which compiles source code and readies deployment artifacts. Once built for deployment, the SAM template and the associated artifacts need to be stored in an S3 bucket. The sam deploy command takes care of this by first uploading the CloudFormation template to the S3 bucket. Though historically, the sam package command was used for this purpose, it’s become somewhat legacy, as sam deploy , now implicitly handles the packaging. Once the template is in the S3 bucket, AWS CloudFormation references it to create or update the defined resources.

Hence, the correct answers are:

– Build the SAM template in the local environment

– Package the SAM application for deployment.

– Deploy the SAM template from an Amazon S3 bucket.

The option that says: Deploy the SAM template from AWS CodePipeline is incorrect. AWS CodePipeline is primarily a continuous integration and continuous delivery (CI/CD) service that automates the build, test, and deploy phases of your release process. While CodePipeline can deploy SAM applications, it is not a required step for a local SAM deployment workflow.

The option that says: Build the SAM template using the AWS SDK for AWS CodeDeploy is incorrect. The AWS SDK for CodeDeploy is typically used for management operations of the CodeDeploy service, not for building SAM templates. Building the SAM application is a separate process, typically done using the SAM CLI.

The option that says: Build the SAM template in an Amazon EC2 instance is incorrect. This option is unnecessary. While you can technically build on an EC2 instance, it’s not a requirement for SAM deployment. In the scenario, there’s no condition that warrants the use of an EC2 instance.

 

References:

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html

https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html

 

Check out this AWS SAM Cheat Sheet:

https://tutorialsdojo.com/aws-serverless-application-model-sam/


29. Question
A developer is building an image processing utility using an AWS Lambda function. The function processes images in parallel using multiple threads to optimize performance. The images are stored in an Amazon S3 bucket and retrieved for processing. However, the function is not performing as efficiently as expected, with the processing time taking longer than anticipated, even when handling relatively small images.

Which action should the developer modify to achieve better performance in the AWS Lambda function?

Optimize memory allocation for the Lambda function.
Use AWS Step Functions to split tasks into smaller workflows.
Utilize Amazon S3 Transfer Acceleration for image uploads.
Increase the timeout setting of the Lambda function.
Correct
AWS Lambda is a serverless compute service that allows developers to run code without provisioning or managing servers. It automatically scales based on the workload and charges only for the compute time consumed. Developers can use Lambda to execute code in response to events such as changes in data, HTTP requests, or system state changes, making it ideal for event-driven architectures. Lambda supports multiple programming languages and integrates seamlessly with other AWS services, enabling flexible and scalable application development.

AWS Lambda functions operate within a highly available infrastructure and manage resources automatically, ensuring reliability and performance. Lambda can execute specific business logic by using triggers like S3 events, DynamoDB streams, or API Gateway, making it a key component for building modern, agile applications.

AWS Lambda Memory Allocation

AWS Lambda allows developers to configure memory allocation for 128 MB to 10,240 MB functions. This memory setting directly influences the CPU resources available to the function, as Lambda allocates CPU power proportionally to the configured memory. For instance, at 1,769 MB, a function has the equivalent of one vCPU. Increasing the memory allocation provides more RAM and enhances CPU capacity, which can lead to significant performance improvements for compute-intensive tasks.

Hence, the correct answer is: Optimize memory allocation for the Lambda function.

The option that says: Use AWS Step Functions to split tasks into smaller workflows is incorrect. AWS Step Functions are primarily used for orchestrating workflows and breaking down complex processes into smaller, manageable steps. However, this approach does not directly improve the execution performance of the Lambda function itself. The issue lies in the Lambda function’s CPU resources, which Step Functions simply cannot address. While they can enhance task coordination, they typically do not optimize the speed of underlying tasks within a single function.

The option that says: Increase the timeout setting of the Lambda function is incorrect. This option primarily focuses on extending the maximum runtime for the Lambda function. Increasing the timeout setting would allow the function to run longer but not address the underlying inefficiencies caused by insufficient memory or CPU resources. Timeout adjustments are typically useful for handling long-running tasks, not optimizing compute-intensive workloads.

The option that says: Utilize Amazon S3 Transfer Acceleration for image uploads is incorrect. Amazon S3 Transfer Acceleration is designed to improve the upload and download speed of objects to and from S3 by using Amazon’s global edge network. However, this feature is only relevant when data transfer speed between the client and S3 is a bottleneck. In this case, the issue lies with the processing of images within the Lambda function. Transfer Acceleration simply cannot influence the performance of compute tasks, as it is unrelated to the Lambda execution environment.

 

References:

https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html

https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html

https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html

 

Check out this AWS Lambda Cheat Sheet:

https://tutorialsdojo.com/aws-lambda/


30. Question
A web application running in Amazon Elastic Beanstalk reads and writes a large number of related items in DynamoDB and processes each item one at a time. The network overhead of these transactions causes degradation in the application’s performance. You were instructed by your manager to quickly refactor the application but without introducing major code changes such as implementing concurrency management or multithreading.

Which of the following solutions is the EASIEST method to implement that will improve the application performance in a cost-effective manner?

Refactor the application to use DynamoDB transactional read and write APIs .
Use DynamoDB Batch Operations API for GET, PUT, and DELETE operations.
Enable DynamoDB Streams.
Upgrade the EC2 instances to a higher instance type.
Correct
For applications that need to read or write multiple items, DynamoDB provides the BatchGetItem and BatchWriteItem operations. Using these operations can reduce the number of network round trips from your application to DynamoDB. In addition, DynamoDB performs the individual read or write operations in parallel. Your applications benefit from this parallelism without having to manage concurrency or threading.



The batch operations are essentially wrappers around multiple read or write requests. For example, if a BatchGetItem request contains five items, DynamoDB performs five GetItem operations on your behalf. Similarly, if a BatchWriteItem request contains two put requests and four delete requests, DynamoDB performs two PutItem and four DeleteItem requests.

In general, a batch operation does not fail unless all of the requests in the batch fail. For example, suppose you perform a BatchGetItemoperation but one of the individual GetItem requests in the batch fails. In this case, BatchGetItem returns the keys and data from the GetItemrequest that failed. The other GetItem requests in the batch are not affected.

Hence, the correct answer is to use DynamoDB Batch Operations API for GET, PUT, and DELETE operations in this scenario.

Upgrading the EC2 instances to a higher instance type is incorrect because the network overhead is the one that affects application performance and not the compute capacity. This is due to multiple read and write requests performed as single operations on DynamoDB, instead of a Batch operation.

Enabling DynamoDB Streams is incorrect because a DynamoDB stream is just an ordered flow of information about changes to items in an Amazon DynamoDB table. When you enable a stream on a table, DynamoDB captures information about every modification to data items in the table. Apparently, this feature does not solve the application issue where there is a large volume of data being processed one by one, and not by batch.

Refactoring the application to use DynamoDB transactional read and write APIs is incorrect because the Amazon DynamoDB transactions feature just simplifies the developer experience of making coordinated, all-or-nothing changes to multiple items both within and across tables. Transactions provide atomicity, consistency, isolation, and durability (ACID) in DynamoDB, enabling you to maintain data correctness in your applications easily. Take note that every transactional read and write API call consumes high RCU and WCUs, unlike eventual or strong consistency requests. Hence, this entails a significant increase in costs which contradicts the requirements of the scenario.

 

References:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.ConditionalUpdate

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html

 

Check out this Amazon DynamoDB Cheat Sheet:

https://tutorialsdojo.com/amazon-dynamodb/


39. Question
A clickstream application uses Amazon Kinesis Data Stream for real-time processing. PutRecord API calls are being used by the producer to send data to the stream. However, there are cases where the producer intermittently restarted while doing the processing, which resulted in sending the same data twice to the stream. This inadvertently causes duplication of entries in the data stream, which affects the processing of the consumers.

Which of the following should you implement to resolve this issue?

Add more shards.
Split shards of the data stream.
Merge shards of the data stream.
Embed a primary key within the record.
Correct
There are two primary reasons why records may be delivered more than one time to your Amazon Kinesis Data Streams application: producer retries and consumer retries. Your application must anticipate and appropriately handle processing individual records multiple times.



Consider a producer that experiences a network-related timeout after it makes a call to PutRecord, but before it can receive an acknowledgment from Amazon Kinesis Data Streams. The producer cannot be sure if the record was delivered to Kinesis Data Streams. Assuming that every record is important to the application, the producer would have written to retry the call with the same data. If both PutRecord calls on that same data were successfully committed to Kinesis Data Streams, then there will be two Kinesis Data Streams records. Although the two records have identical data, they also have unique sequence numbers. Applications that need strict guarantees should embed a primary key within the record to remove duplicates later when processing. Note that the number of duplicates due to producer retries is usually low compared to the number of duplicates due to consumer retries.

Hence, the correct answer in this scenario is to embed a primary key within the record to remove duplicates later when processing.

Adding more shards is incorrect because this is not a suitable solution for handling duplicate records in the Kinesis data stream. This is primarily used to increase the rate of data flowing through the stream.

Splitting shards of the data stream is incorrect because this is used to increase the capacity of the stream and not to avoid any duplicate data.

Merging shards of the data stream is incorrect because this is primarily used to make better use of the unused capacity in the stream and to save on costs.

 

References:

https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-duplicates.html

https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html

 

Check out this Amazon Kinesis Cheat Sheet:

https://tutorialsdojo.com/amazon-kinesis/


40. Question
A company has a suite of web applications that is heavily using RDS database in Multi-AZ Deployments configuration with several Read Replicas. For improved security, you were instructed to ensure that all of their database credentials, API keys, and other secrets are encrypted and rotated on a regular basis. You should also configure your applications to use the latest version of the encrypted credentials when connecting to the RDS database.

Which of the following is the MOST appropriate solution to secure the credentials?

Use AWS Secrets Manager to store and encrypt the credentials and enable automatic rotation.
Store the credentials in AWS KMS.

Store the credentials to Systems Manager Parameter Store with a SecureString data type.
Store the credentials to AWS ACM.
Correct
AWS Secrets Manager is an AWS service that makes it easier for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text. You can store and control access to these secrets centrally by using the Secrets Manager console, the Secrets Manager command line interface (CLI), or the Secrets Manager API and SDKs.

In the past, when you created a custom application that retrieves information from a database, you typically had to embed the credentials (the secret) for accessing the database directly in the application. When it came time to rotate the credentials, you had to do much more than just create new credentials. You had to invest time to update the application to use the new credentials. Then you had to distribute the updated application. If you had multiple applications that shared credentials and you missed updating one of them, the application would break. Because of this risk, many customers have chosen not to regularly rotate their credentials, which effectively substitutes one risk for another.



Secrets Manager enables you to replace hardcoded credentials in your code (including passwords), with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure that the secret can’t be compromised by someone examining your code, because the secret simply isn’t there. Also, you can configure Secrets Manager to automatically rotate the secret for you according to a schedule that you specify. This enables you to replace long-term secrets with short-term ones, which helps to significantly reduce the risk of compromise.

Hence, using AWS Secrets Manager to store and encrypt the credentials and enabling automatic rotation is the most appropriate solution for this scenario.

Storing the credentials to Systems Manager Parameter Store with a SecureString data type is incorrect because, by default, Systems Manager Parameter Store doesn’t rotate its parameters which is one of the requirements in the above scenario.

Storing the credentials to AWS ACM is incorrect because it is just a managed private CA service that helps you easily and securely manage the lifecycle of your private certificates to allow SSL communication to your application. This is not a suitable service to store database or any other confidential credentials.

Storing the credentials in AWS KMS is incorrect because this only makes it easy for you to create and manage encryption keys and control the use of encryption across a wide range of AWS services. This is primarily used for encryption and not for hosting your credentials.

 

References:

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html

https://aws.amazon.com/blogs/compute/sharing-secrets-with-aws-lambda-using-aws-systems-manager-parameter-store/

 

Check out these AWS Systems Manager and Secrets Manager Cheat Sheets:

https://tutorialsdojo.com/aws-systems-manager/

https://tutorialsdojo.com/aws-secrets-manager/


41. Question
A developer is creating a new global secondary index on a provisioned mode DynamoDB table. Since the application will store large quantities of data, the write capacity units must be specified for the expected workload on both the base table and its secondary index.

Which of the following should the developer do to avoid any potential request throttling?

Ensure that the global secondary index's provisioned RCU is equal or less than the RCU of the base table.
Ensure that the global secondary index's provisioned WCU is equal or less than the WCU of the base table.
Ensure that the global secondary index's provisioned RCU is equal or greater than the RCU of the base table.
Ensure that the global secondary index's provisioned WCU is equal or greater than the WCU of the base table.
Correct
A global secondary index (GSI) is an index with a partition key and a sort key that can be different from those on the base table. It is considered “global” because queries on the index can span all of the data in the base table, across all partitions.

Every global secondary index has its own provisioned throughput settings for read and write activity. Queries or scans on a global secondary index consume capacity units from the index, not from the base table. The same holds true for global secondary index updates due to table writes.

When you create a global secondary index on a provisioned mode table, you must specify read and write capacity units for the expected workload on that index. The provisioned throughput settings of a global secondary index are separate from those of its base table. A Query operation on a global secondary index consumes read capacity units from the index, not the base table. When you put, update, or delete items in a table, the global secondary indexes on that table are also updated; these index updates consume write capacity units from the index, not from the base table.



For example, if you Query a global secondary index and exceed its provisioned read capacity, your request will be throttled. If you perform heavy write activity on the table but a global secondary index on that table has insufficient write capacity, then the write activity on the table will be throttled.

To avoid potential throttling, the provisioned write capacity for a global secondary index should be equal or greater than the write capacity of the base table since new updates will write to both the base table and global secondary index.

Hence, the correct answer in this scenario is to ensure that the global secondary index’s provisioned WCU is equal to or greater than the WCU of the base table.

Ensuring that the global secondary index’s provisioned WCU is equal or less than the WCU of the base table is incorrect because it should be the other way around, just as what is mentioned above. The provisioned write capacity for a global secondary index should be equal to or greater than the write capacity of the base table.

Ensuring that the global secondary index’s provisioned RCU is equal to or greater than the RCU of the base table is incorrect because you have to set the WCU and not the RCU.

Ensuring that the global secondary index’s provisioned RCU is equal or less than the RCU of the base table is incorrect because this should be WCU and in addition, the global secondary index’s provisioned WCU should be set to a value that is equal or greater than the WCU of the base table to prevent request throttling.

 

References:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.ThroughputConsiderations

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes

 

Check out this Amazon DynamoDB Cheat Sheet:

https://tutorialsdojo.com/amazon-dynamodb/


42. Question
A leading financial company has recently deployed its application to AWS using Lambda and API Gateway. However, they noticed that all metrics are being populated in their CloudWatch dashboard except for CacheHitCount and CacheMissCount.

What could be the MOST likely cause of this issue?

API Caching is not enabled in API Gateway.
API Gateway Private Integrations has not been configured yet.
They have not provided an IAM role to their API Gateway yet.
The provided IAM role to their API Gateway only has read access but no write privileges to CloudWatch.
Correct
You can monitor API execution using CloudWatch, which collects and processes raw data from API Gateway into readable, near-real-time metrics. These statistics are recorded for a period of two weeks so that you can access historical information and gain a better perspective on how your web application or service is performing. By default, API Gateway metric data is automatically sent to CloudWatch in one-minute periods.



The metrics reported by API Gateway provide information that you can analyze in different ways. The list below shows some common uses for the metrics. These are suggestions to get you started, not a comprehensive list.

 – Monitor the IntegrationLatency metrics to measure the responsiveness of the backend.

 – Monitor the Latency metrics to measure the overall responsiveness of your API calls.

 – Monitor the CacheHitCount and CacheMissCount metrics to optimize cache capacities to achieve a desired performance. CacheMissCount tracks the number of requests served from the backend in a given period, when API caching is enabled. On the other hand, CacheHitCount track the number of requests served from the API cache in a given period.

Hence, the root cause of this issue is that the API Caching is not enabled in API Gateway which is why the CacheHitCount and CacheMissCount metrics are not populated.

The option that says: they have not provided an IAM role to their API Gateway yet is incorrect because, in the first place, the scenario already mentioned that all metrics are being populated in their CloudWatch dashboard except for two metrics. This implies that some of the metrics are populated which means that the API Gateway already has an IAM Role associated with it.

The option that says: the provided IAM role to their API Gateway only has read access but no write privileges to CloudWatch is incorrect because just as what is mentioned above, there is no issue with the IAM Role since all metrics are being populated except only for CacheHitCount and CacheMissCount. This means that the associated IAM Role already has write privileges to write logs to CloudWatch to begin with. The only reason why those two metrics are not being populated is that the API Caching is not enabled.

The option that says: API Gateway Private Integrations has not been configured yet is incorrect because this feature only makes it easier to expose your HTTP/HTTPS resources behind an Amazon VPC for access by clients outside of the VPC.

 

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring-cloudwatch.html

 

Check out this Amazon API Gateway Cheat Sheet:

https://tutorialsdojo.com/amazon-api-gateway


43. Question
A developer needs to configure the environment name, solution stack, and environment links of his application environment which will be hosted in Elastic Beanstalk. Which configuration file should the developer add in the source bundle to meet the above requirement?


Dockerrun.aws.json

cron.yaml

env.config

env.yaml
Correct
In Elastic Beanstalk, you can include a YAML formatted environment manifest in the root of your application source bundle to configure the environment name, solution stack and environment links to use when creating your environment. An environment manifest uses the same format as Saved Configurations.

This file format includes support for environment groups. To use groups, specify the environment name in the manifest with a + symbol at the end. When you create or update the environment, specify the group name with --group-name (AWS CLI) or --env-group-suffix (EB CLI).

The following example manifest defines a web server environment for the tutorialsdojo frontend application, with a link to a worker environment component that it is dependent upon. The manifest uses groups to allow creating multiple environments with the same source bundle:

 ~/tutorialsdojo/frontend/env.yaml

AWSConfigurationTemplateVersion: 1.1.0.0
SolutionStack: 64bit Amazon Linux 2015.09 v2.0.6 running Multi-container Docker 1.7.1 (Generic)
OptionSettings:
  aws:elasticbeanstalk:command:
    BatchSize: '30'
    BatchSizeType: Percentage
  aws:elasticbeanstalk:sns:topics:
    Notification Endpoint: me@tutorialsdojo.com
  aws:elb:policies:
    ConnectionDrainingEnabled: true
    ConnectionDrainingTimeout: '20'
  aws:elb:loadbalancer:
    CrossZone: true
  aws:elasticbeanstalk:environment:
    ServiceRole: aws-elasticbeanstalk-service-role
  aws:elasticbeanstalk:application:
    Application Healthcheck URL: /
  aws:elasticbeanstalk:healthreporting:system:
    SystemType: enhanced
  aws:autoscaling:launchconfiguration:
    IamInstanceProfile: aws-elasticbeanstalk-ec2-role
    InstanceType: t2.micro
    EC2KeyName: workstation-uswest2
  aws:autoscaling:updatepolicy:rollingupdate:
    RollingUpdateType: Health
    RollingUpdateEnabled: true
Tags:
  Cost Center: Tutorials Dojo Dev
CName: front-A08G28LG+
EnvironmentName: front+
EnvironmentLinks:
  "WORKERQUEUE" : "worker+"

Hence, using the env.yaml is the correct configuration file to be used in this scenario.

Dockerrun.aws.json is incorrect because this configuration file is primarily used in multicontainer Docker environments that are hosted in Elastic Beanstalk. This can be used alone or combined with source code and content in a source bundle to create an environment on a Docker platform.

env.config is incorrect because this is just a custom configuration file which is not readily available in Elastic Beanstalk. Configuration files are YAML- or JSON-formatted documents with a .config file extension that you place in a folder named .ebextensions and deploy in your application source bundle. The more appropriate configuration file to use here is the env.yaml which can help you configure the environment name, solution stack, and environment links to use when creating your environment.

cron.yaml is incorrect because this configuration file is primarily used to define periodic tasks that add jobs to your worker environment’s queue automatically at a regular interval.


 

References:

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html


 

Check out this AWS Elastic Beanstalk Cheat Sheet:

https://tutorialsdojo.com/aws-elastic-beanstalk/


47. Question
A developer needs to encrypt all objects being uploaded by their application to the S3 bucket to comply with the company’s security policy. The bucket will use server-side encryption with Amazon S3-Managed encryption keys (SSE-S3) to encrypt the data using 256-bit Advanced Encryption Standard (AES-256) block cipher.

Which of the following request headers should the developer use?


x-amz-server-side-encryption-customer-algorithm

x-amz-server-side-encryption

x-amz-server-side-encryption-customer-key

x-amz-server-side-encryption-customer-key-MD5
Correct
Server-side encryption protects data at rest. If you use Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3), Amazon S3 will encrypt each object with a unique key and as an additional safeguard, it encrypts the key itself with a master key that it rotates regularly. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.



If you need server-side encryption for all of the objects that are stored in a bucket, use a bucket policy. For example, the following bucket policy denies permissions to upload an object unless the request includes the x-amz-server-side-encryption header to request server-side encryption:



However, if you chose to use server-side encryption with customer-provided encryption keys (SSE-C), you must provide encryption key information using the following request headers:

x-amz-server-side​-encryption​-customer-algorithm

x-amz-server-side​-encryption​-customer-key

x-amz-server-side​-encryption​-customer-key-MD5

Hence, using the x-amz-server-side-encryption header is correct as this is the one being used for Amazon S3-Managed Encryption Keys (SSE-S3). All other options are incorrect since they are used for SSE-C.

 

References:

https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html

 

Check out this Amazon S3 Cheat Sheet:

https://tutorialsdojo.com/amazon-s3/


48. Question
A company is using OpenAPI, which is also known as Swagger, for the API specifications of their REST web services that are hosted on their on-premises data center. They want to migrate their system to AWS using Lambda and API Gateway. In line with this, you are instructed to create a new API and populate it with the resources and methods from their Swagger definition.

Which of the following is the EASIEST way to accomplish this task?

Create models and templates for request and response mappings based on the company's API definitions.
Use AWS SAM to migrate and deploy the company's web services to API Gateway.
Import their Swagger or OpenAPI definitions to API Gateway using the AWS Console.
Use CodeDeploy to migrate and deploy the company's web services to API Gateway.
Correct
You can use the API Gateway Import API feature to import a REST API from an external definition file into API Gateway. Currently, the Import API feature supports OpenAPI v2.0 and OpenAPI v3.0 definition files. You can update an API by overwriting it with a new definition or merge a definition with an existing API. You specify the options using a mode query parameter in the request URL.

You can paste a Swagger API definition in the AWS Console to create a new API and populate it with the resources and methods from your Swagger or OpenAPI definition, just as shown below:



You can also import your Swagger definition through the AWS CLI and SDKs.

Hence, the correct answer in this scenario is to import their Swagger or OpenAPI definitions to API Gateway using the AWS Console.

Using CodeDeploy to migrate and deploy the company’s web services to API Gateway is incorrect because using CodeDeploy alone is not enough to deploy new custom APIs. This is mainly used in conjunction with AWS SAM where you can add deployment preferences to manage the way traffic is shifted during an AWS Lambda application deployment.

Using AWS SAM to migrate and deploy the company’s web services to API Gateway is incorrect. Although using AWS SAM is the preferred way to deploy your serverless application, it is not the easiest way to import the Swagger API definitions file. As mentioned above, you can simply import Swagger or OpenAPI files directly to AWS.

Creating models and templates for request and response mappings based on the company’s API definitions is incorrect because this is primarily done for API Gateway integration to other services and not for importing API definitions file.

 

References:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-from-example.html

 

Check out this Amazon API Gateway Cheat Sheet:

https://tutorialsdojo.com/amazon-api-gateway/


49. Question
A website hosted in AWS has a custom CloudWatch metric to track all HTTP server errors in the site every minute, which occurs intermittently. An existing CloudWatch Alarm has already been configured for this metric but you would like to re-configure this to properly monitor the application. The alarm should only be triggered when all three data points in the most recent three consecutive periods are above the threshold.

Which of the following options is the MOST appropriate way to monitor the website based on the given threshold?

Use metric math in CloudWatch to properly compute the threshold.
Use high-resolution metrics.

Set both the Period and Datapoints to Alarm to 3.

Set both the Evaluation Period and Datapoints to Alarm to 3.
Correct
When you create an alarm, you specify three settings to enable CloudWatch to evaluate when to change the alarm state:

 – Period is the length of time to evaluate the metric or expression to create each individual data point for an alarm. It is expressed in seconds. If you choose one minute as the period, there is one datapoint every minute.

 – Evaluation Period is the number of the most recent periods, or data points, to evaluate when determining alarm state.

 – Datapoints to Alarm is the number of data points within the evaluation period that must be breaching to cause the alarm to go to the ALARM state. The breaching data points do not have to be consecutive, they just must all be within the last number of data points equal to Evaluation Period.

In the following figure, the alarm threshold is set to three units. The alarm is configured to go to the ALARM state and both Evaluation Period and Datapoints to Alarm are 3. That is, when all three datapoints in the most recent three consecutive periods are above the threshold, the alarm goes to the ALARM state. In the figure, this happens in the third through fifth time periods. At period six, the value dips below the threshold, so one of the periods being evaluated is not breaching, and the alarm state changes to OK. During the ninth time period, the threshold is breached again, but for only one period. Consequently, the alarm state remains OK.



Hence, the option that says: Set both the Evaluation Period and Datapoints to Alarm to 3 is the correct answer.

The option that says: Use high-resolution metrics is incorrect because the scenario says that it only needs to monitor the HTTP server errors every minute, and not its sub-minute activity. If you set an alarm on a high-resolution metric, you can specify a high-resolution alarm with a period of 10 seconds or 30 seconds. Hence, this option is irrelevant in this scenario.

The option that says: Set both the Period and Datapoints to Alarm to 3 is incorrect because you should set the Evaluation Period and not the Period setting.

The option that says: Use metric math in CloudWatch to properly compute the threshold is incorrect because the Metric Math feature is only applicable for scenarios where you need to query multiple CloudWatch metrics or if you want to use math expressions to create new time series based on selected metrics.

 

References:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html

 

Check out this Amazon CloudWatch Cheat Sheet:

https://tutorialsdojo.com/amazon-cloudwatch/


51. Question
A financial mobile application has a serverless backend API which consists of DynamoDB, Lambda, and Cognito. Due to the confidential financial transactions handled by the mobile application, there is a new requirement provided by the company to add a second authentication method that doesn’t rely solely on user name and password.

Which of the following is the MOST suitable solution that the developer should implement?

Use a new IAM policy to a user pool in Cognito.
Use Cognito with SNS to allow additional authentication via SMS.
Integrate multi-factor authentication (MFA) to a user pool in Cognito to protect the identity of your users.
Create a custom application that integrates with Amazon Cognito which implements the second layer of authentication.
Correct
You can add multi-factor authentication (MFA) to a user pool to protect the identity of your users. MFA adds a second authentication method that doesn’t rely solely on usernames and passwords. You can choose to use SMS text messages, or time-based one-time (TOTP) passwords as second factors in signing in your users. You can also use adaptive authentication with its risk-based model to predict when you might need another authentication factor. It’s part of the user pool’s advanced security features, which also include protections against compromised credentials.



Multi-factor authentication (MFA) increases security for your app by adding another authentication method, and not relying solely on user name and password. You can choose to use SMS text messages, or time-based one-time (TOTP) passwords as second factors in signing in your users.

With adaptive authentication, you can configure your user pool to require second-factor authentication in response to an increased risk level.

Hence, the correct answer in this scenario is to integrate multi-factor authentication (MFA) to a user pool in Cognito to protect the identity of your users.

Creating a custom application that integrates with Amazon Cognito which implements the second layer of authentication is incorrect. Although this option is viable, it is not the most suitable solution in this scenario since you can simply use MFA as a second-factor authentication for the mobile app.

Using a new IAM policy to a user pool in Cognito is incorrect because an IAM Policy alone cannot implement a second-factor authentication. You have to configure Cognito to use MFA instead.

Using Cognito with SNS to allow additional authentication via SMS is incorrect. Although this is part of the MFA setup, using this solution alone is not enough if you didn’t enable MFA in the first place.

 

References:

https://docs.aws.amazon.com/cognito/latest/developerguide/managing-security.html

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

 

Tutorials Dojo’s AWS Certified Developer Associate Exam Study Guide:

https://tutorialsdojo.com/aws-certified-developer-associate/
