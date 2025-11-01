Of course. Here are the notes taken directly from the PDF text, presented word-for-word in a structured format.

### **Page 1: SDLC - Deployment Types**

*   **Single Target**
    *   New app version is installed on target server
    *   Outage occurs during installation
    *   No secondary servers, testing is limited
    *   Rollback requires removing new version and installing previous version
*   **All-at-once**
    *   Deployment happens in one step
    *   Destination is multiple targets
    *   Requires orchestration tooling
    *   Shares negatives of Single Target
        *   No ability to test
        *   Outage
        *   Less than ideal rollback
*   **Minimum In-service**
    *   Happens in multiple stages
    *   Deployment happens to as many targets as possible while maintaining minimum in-service targets
    *   Allows automated testing
        *   Deployment targets are assessed and tested prior to continuing
    *   No downtime
*   **Rolling Deployment**
    *   Deployment happens in multiple stages, number of targets per stage is user-defined
    *   Moving parts, orchestration, health checks required
    *   Overall applicable health is not necessarily maintained
    *   Can be least efficient deployment type based on time-taken
    *   Allows automated testing
        *   Deployment targets are assessed and tested prior to continuing
    *   Generally no downtime, assuming number of targets will not impact application
    *   Can be paused, allowing limited multi-version testing
*   **Blue Green Deployment**
    *   Requires advanced orchestration tooling
    *   Costs more: maintain two environments at once
    *   Deployment is rapid, entire environment is deployed at once
    *   Cutover and migration is clean and controlled (DNS change)
    *   Rollback is equally clean (DNS regression)
    *   Health and performance of entire green environment can be tested prior to cutover
    *   Using advanced template systems (CloudFormation), entire process can be automated
*   **Canary Deployment**
    *   Similar to Blue Green, but blue stays incrementally active
    *   Can be done with Route53 - weighted Round Robin
    *   Easily allows for a/b testing

### **Page 2: CodeCommit**

*   Version control service to privately store and manage assets (such as documents, source code, and binary files) in the cloud
*   **Fully Managed** –AWS CodeCommit eliminates the need to host, maintain, backup, and scale your own source control servers.
*   **Secure** –AWS CodeCommit automatically encrypts your files in transit and at rest. AWS CodeCommit is integrated with AWS Identity and Access Management (IAM), allowing you to assign user-specific permissions to your repositories.
*   **Highly Available** – AWS CodeCommit is built on highly scalable, redundant, and durable AWS services such as Amazon S3 and Amazon DynamoDB.
*   **Scalable** - AWS CodeCommit allows you store any number of files and there are no repository size limits.
*   **Faster Development Lifecycle** - AWS CodeCommit keeps your repositories close to your build, staging, and production environments in the AWS cloud. This allows you to increase the speed and frequency of your development lifecycle.
*   **Creating Web Hooks with CodeCommit**
    *   In the Amazon Simple Notification Service (SNS) console, you can create a SNS topic with an HTTP endpoint and the desired URL for the webhook. From the AWS CodeCommit console, you can then configure that SNS topic to a repository event using triggers.

### **Page 3: CodeBuild**

*   Fully managed continuous integration service in the cloud. CodeBuild compiles source code, runs tests, and produces packages that are ready to deploy.
*   Eliminates the need to provision, manage, and scale your own build servers
*   Automatically scales up and down and processes multiple builds concurrently, so builds don’t have to wait in a queue.
*   Use prepackaged build environments or custom build environments to use your own build tools
*   Pay by the minute
*   **How it Works**
    *   As input, you must provide CodeBuild with a build project. A build project defines how CodeBuild runs a build. It includes information such as where to get the source code, the build environment to use, the build commands to run, and where to store the build output. A build environment represents a combination of operating system, programming language runtime, and tools that CodeBuild uses to run a build.
*   **Steps:**
    1.  CodeBuild uses the build project to create the build environment.
    2.  CodeBuild downloads the source code into the build environment and then uses the build specification (build spec), as defined in the build project or included directly in the source code. A build spec is a collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build.
    3.  If there is any build output, the build environment uploads its output to an Amazon S3 bucket. The build environment can also perform tasks that you specify in the build spec (for example, sending build notifications to an Amazon SNS topic).
    4.  While the build is running, the build environment sends information to CodeBuild and Amazon CloudWatch Logs.
    5.  While the build is running, you can use the CodeBuild console, AWS CLI, or AWS SDKs, to get summarized build information from CodeBuild and detailed build information from Amazon CloudWatch Logs. If you use AWS CodePipeline to run builds, you can get limited build information from CodePipeline.
*   **Sources**: CodeBuild can connect to AWS CodeCommit, S3, GitHub, and GitHub Enterprise and Bitbucket to pull source code
*   **Programming Frameworks**: Java, Ruby, Python, Go, Node.js, Android, .NET Core, PHP, and Docker. Customize an environment by creating a Docker image and uploading it to the Amazon EC2 Container Registry or the Docker Hub registry
*   **Jenkins Integration**: CodeBuild Plugin for Jenkins can be used to integrate CodeBuild into Jenkins jobs
*   **Security**:
    *   Specify a key stored in the AWS Key Management Service (AWS KMS) to encrypt your artifacts
    *   Runs build in fresh environments isolated from other users and discards each build environment upon completion. CodeBuild provides security and separation at the infrastructure and execution levels.

### **Pages 5-6: Buildspec.yml**

*   A build spec is a collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build. You can include a build spec as part of the source code or you can define a build spec when you create a build project.
*   By default, the build spec file must be named buildspec.yml and placed in the root of your source directory. You can override the default build spec file name and location
*   The build spec has the following syntax:
    *   version: 0.2
    *   run-as: Linux-user-name
    *   env:
        *   variables:
            *   key: "value"
            *   key: "value"
        *   parameter-store:
            *   key: "value"
            *   key: "value"
    *   phases:
        *   install:
            *   run-as: Linux-user-name
            *   commands:
                *   - command
                *   - command
            *   finally:
                *   - command
                *   - command
        *   pre_build:
            *   run-as: Linux-user-name
            *   commands:
                *   - command
                *   - command
            *   finally:
                *   - command
                *   - command
        *   build:
            *   run-as: Linux-user-name
            *   commands:
                *   - command
                *   - command
            *   finally:
                *   - command
                *   - command
        *   post_build:
            *   run-as: Linux-user-name
            *   commands:
                *   - command
                *   - command
            *   finally:
                *   - command
                *   - command
    *   artifacts:
        *   files:
            *   - location
            *   - location
        *   name: artifact-name
        *   discard-paths: yes
        *   base-directory: location
    *   secondary-artifacts:
        *   artifactIdentifier:
            *   files:
                *   - location
                *   - location
            *   name: secondary-artifact-name
            *   discard-paths: yes
            *   base-directory: location
        *   artifactIdentifier:
            *   files:
                *   - location
                *   - location
            *   discard-paths: yes
            *   base-directory: location
    *   cache:
        *   paths:
            *   - path
            *   - path

### **Pages 7-12: CodeDeploy**

*   Service that automates code deployments to any instance, including Amazon EC2 instances and instances running on-premises.
*   **Supported Platforms/Deployment Types:**
    *   **EC2/On-Premises: In-Place or Blue/Green Deployments**
        *   Describes instances of physical servers that can be Amazon EC2 cloud instances, on-premises servers, or both. Applications created using the EC2/On-Premises compute platform can be composed of executable files, configuration files, images, and more.
        *   Deployments that use the EC2/On-Premises compute platform manage the way in which traffic is directed to instances by using an in-place or blue/green deployment type.
    *   **AWS Lambda: Canary, Linear, All-At-Once Deployments**
        *   Applications created using the AWS Lambda compute platform can manage the way in which traffic is directed to the updated Lambda function versions during a deployment by choosing a canary, linear, or all-at-once configuration.
    *   **Amazon ECS: Blue/Green Deployment**
        *   Used to deploy an Amazon ECS containerized application as a task set.
        *   CodeDeploy performs a blue/green deployment by installing an updated version of the containerized application as a new replacement task set. CodeDeploy recovers production traffic from the original application, or task set, to the replacement task set. The original task set is terminated after a successful deployment.
*   **App Spec File**
    *   The application specification file (AppSpec file) is a YAML-formatted or JSON-formatted file used by CodeDeploy to manage a deployment.
    *   Note: the name of the AppSpec file for an EC2/On-Premises deployment must be appspec.yml. The name of the AppSpec file for an Amazon ECS or AWS Lambda deployment must be appspec.yaml.
*   **AppSpec Files on ECS** determine:
    *   Amazon ECS task definition file. This is specified with its ARN in the TaskDefinition instruction in the AppSpec file.
    *   The container and port in replacement task set where your Application Load Balancer or Network Load Balancer reroutes traffic during a deployment. This is specified with the LoadBalancerInfo instruction in the AppSpec file.
    *   Optional information about your Amazon ECS service, such the platform version on which it runs, its subnets, and its security groups.
    *   Optional Lambda functions to run during hooks that correspond with lifecycle events during an Amazon ECS deployment.
*   **AppSpec Files on Lambda** determine:
    *   Which Lambda function version to deploy.
    *   Which Lambda functions to use as validation tests.
*   **AppSpec Files on EC2/On-Premises** determine:
    *   What it should install onto your instances from your application revision in Amazon S3 or GitHub.
    *   Which lifecycle event hooks to run in response to deployment lifecycle events.
    *   Note: An AppSpec file must be a YAML-formatted file named appspec.yml and it must be placed in the root of the directory structure of an application's source code. Otherwise, deployments fail.
    *   **Steps:**
        *   Complete AppSpec file, bundle it, along with the content to deploy, into an archive file (zip, tar, or compressed tar)
        *   After you have a bundled archive file (known in CodeDeploy as a revision), you upload it to an Amazon S3 bucket or Git repository.
        *   Use CodeDeploy to deploy the revision.
        *   The appspec.yml for an EC2/On-Premises compute platform deployment is saved in the root directory of your revision.

### **Pages 13-25: CloudFormation**

*   **Key Terms**
    *   **Stack** - manage related resources as a single unit called a stack. Create, update, and delete a collection of resources by creating, updating, and deleting stacks. All the resources in a stack are defined by the stack's AWS CloudFormation template.
    *   **Template** - JSON or YAML formatted text file. AWS CloudFormation uses these templates as blueprints for building your AWS resources.
    *   **Stack Policy** - IAM style policy statement which governs what can be changed and who can change it.
*   **Anatomy of a Template**
    *   Format Version (optional)
    *   Description (optional)
    *   Metadata (optional)
    *   Parameters (optional)
    *   Mappings (optional)
    *   Conditions (optional)
    *   Transform (optional)
    *   Resources (required)
    *   Outputs (optional)
*   **Intrinsic Functions**: Fn::Base64, Fn::Cidr, Fn::FindInMap, Fn::GetAtt, Fn::GetAZs, Fn::ImportValue, Fn::Join, Fn::Select, Fn::Split, Fn::Sub, Fn::Transform, Ref.
*   **Condition Functions**: Fn::And, Fn::Equals, Fn::If, Fn::Not, Fn::Or.
*   **Wait Conditions/Creation Policy**
    *   **CreationPolicy** attribute prevents resource's status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded.
    *   Use the cfn-signal helper script or SignalResource API to send signal.
    *   In most conditions, CreationPolicy is preferable to WaitCondition.
*   **Nested Stack**: Stack is a resource which has following benefits: Overcome limits of CloudFormation, Split large number of resources over multiple templates, Reuse common template patterns.
*   **Resource Deletion Policies**: Three types of DeletionPolicy for each resource: Delete (default), Retain, Snapshot (only on a few services).
*   **Stack Updates**: Use Stack Policy to control actions.
    *   No stack policy = allow all updates
    *   Once a stack policy is applied, can't be deleted
    *   Once a policy is applied, all resources are protected by default. Update:* is denied.
*   **Custom Resources**: Create resources outside of the available AWS resources. Involves 3 parties: Template developer, custom resource provider, AWS CloudFormation.
*   **CloudFormation Best Practices**
    *   Organize Your Stacks By Lifecycle and Ownership (multi-layered architecture, service-oriented architecture (SOA)).
    *   Use Cross-Stack References to Export Shared Resources.
    *   Use IAM to Control Access.
    *   Verify Quotas for All Resource Types.
    *   Reuse Templates to Replicate Stacks in Multiple Environments.
    *   Use Nested Stacks to Reuse Common Template Patterns.
    *   Do Not Embed Credentials in Your Templates.
    *   Use AWS-Specific Parameter Types.
    *   Use Parameter Constraints.
    *   Use AWS::CloudFormation::Init to Deploy Software Applications on Amazon EC2 Instances.
    *   Use the Latest Helper Scripts (yum install -y aws-cfn-bootstrap).
    *   Validate Templates Before Using Them.
    *   Manage All Stack Resources Through AWS CloudFormation.
    *   Create Change Sets Before Updating Your Stacks.
    *   Use Stack Policies.
    *   Use Code Reviews and Revision Controls to Manage Your Templates.
    *   Update Your Amazon EC2 Linux Instances Regularly (yum update).

### **Pages 25-47: Other Key Services & Exam Tips**

*   **Elastic Beanstalk**: Upload an application and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring. **.ebextentions** allow advanced environment customization.
*   **AWS Config**: Enables you to assess, audit, and evaluate the configurations of your AWS resources. Allows for: Continuous monitoring, Continuous assessment, Troubleshooting, Compliance monitoring, Change management.
*   **ECS**: Highly scalable, high performance container management service that supports Docker containers.
*   **Lambda Step Functions**: Service that allows you to orchestrate your lambda functions. Reliable way to step through functions in a particular order.
*   **OpsWorks**: Three services: OpsWorks for Chef Automate, OpsWorks for Puppet Enterprise, OpsWorks Stacks (this is the service that will be in exam). Uses Chef (declarative state engine).
*   **Monitoring and Logging**
    *   **CloudWatch**:
        *   **Retention Period**: Data points < 60 seconds: 3 hours; 60 seconds: 15 days; 300 seconds: 63 days; 3600 seconds: 445 days.
        *   **Concepts**: Metrics, Namespace, Dimension.
    *   **CloudWatch Events**: Concepts: Events, Targets, Rules.
    *   **CloudWatch Logs**: Concepts: Log Events, Log Streams, Log Groups.
    *   **X-Ray**: Collects data about requests that your application serves.
*   **Policies and Standards Automation**
    *   **Service Catalog**: Allows IT administrators to create, manage, and distribute catalogs of approved products to end users.
    *   **Trusted Advisor**: Provides real time guidance. Categories: Cost optimization, Performance, Security, Fault tolerance, Service Limits.
    *   **Systems Manager**: Features: Run command, State manager, Inventory, Maintenance Window, Patch Manager, Automation, Parameter Store.
    *   **Organizations**: Policy-based management for multiple AWS accounts.
    *   **Secrets Manager**: Service to help protect secrets needed to access applications.
    *   **Macie**: Security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS (currently only S3).
    *   **Certificate Manager**: Easily provision, manage, and deploy SSL/TLS certificates.
*   **Incident and Event Response**
    *   **GuardDuty**: A threat detection service that continuously monitors for malicious or unauthorized behavior.
    *   **Amazon Inspector**: Automated service that assess your applications for vulnerabilities and produces a security findings report. Mainly based around protecting EC2 instances.
*   **Amazon Kinesis**: Collect, process, and analyze video and data streams in real time.
    *   **Kinesis Data Analytics**: Analyze streaming data using SQL.
    *   **Kinesis Data Firehose**: Deliver streaming data to S3, Redshift, etc.
    *   **Kinesis Data Streams**: Collect streaming data. Data stored for 7 days.
    *   **Kinesis Video Streams**: Collect streaming video.
*   **High Availability, Fault Tolerance, & Disaster Recovery**
    *   **Single Sign-On**: Centrally manage single sign on access.
    *   **CloudFront**: A fast content delivery network (CDN).
    *   **AutoScaling**:
        *   **Lifecycle**: Pending state -> In Service State -> Terminating State. Optional: Standby state, Detach Instance.
        *   **Lifecycle Hooks**: You can change heartbeat timeout. Use `complete-lifecycle-action` or `record-lifecycle-action-heartbeat`.
        *   **Cooldowns**: Ensure that autoscaling group does not launch or terminate more instances than needed.
    *   **Route 53 Routing Policies**: Failover, Geolocation, Geoproximity, Latency, Multivalue answer, Weighted (good for A/B Testing).
    *   **RDS**:
        *   **Benefits**: Fast, Cost efficient, Resizable, Secure, Highly Available, Minimal administration.
        *   **Scaling**: Vertical (Change instance type), Horizontal (Read replicas).
    *   **Aurora**:
        *   MySql and Postgres compatible DB built for the cloud.
        *   5x throughput of mysql on same hardware.
        *   Maintains 6 copies of data across 3 AZs.
        *   **Replicas**: Amazon Aurora replicas (up to 15, low impact) vs. MySQL read replicas (up to 5, high impact).
    *   **DynamoDB**:
        *   Fully managed NoSQL database.
        *   **Concepts**: WCUs (write capacity units), RCUs (read capacity units).
        *   **Streams**: Optional feature capturing data modification events. Can trigger lambda.
*   **Exam Strategy**
    *   Keep track of time.
    *   Read both the question and answer in full.
    *   Identify the key words in the question.
    *   Spot the distractor/silly answers.
    *   An answer that says "Don't do anything", is not the right answer.
    *   Avoid answers that have you doing manual commands/process.
    *   Focus on simplest, most technically correct answers.
