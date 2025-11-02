# AWS DevOps Certification Notes: From CloudFormation StackSets to API Gateway Caching

These notes summarize the provided PPT content from Stephen's Udemy course. I've organized them into logical sections for easy revision. Key concepts, diagrams (described), and hands-on tips are highlighted. Use bullet points for clarity, and tables where comparisons or lists are effective.

## 1. CloudFormation StackSets
- **Overview**: Create, update, or delete stacks across multiple accounts and regions using a single operation/template.
  - Administrator account creates StackSets.
  - Target accounts manage stack instances.
  - Updates propagate to all associated stack instances.
  - Can apply to all accounts in AWS Organizations.
- **Diagram Description**: Administrator account → Template → StackSet → Stack Instances in Regions/Accounts (e.g., Region 1: Accounts A/B; Region 2: Accounts A/C).

### StackSets Permission Models
- **Self-Managed Permissions**: Create IAM roles in admin/target accounts with trust relationships. Deploy to any account with IAM role permissions.
- **Service-Managed Permissions**: For AWS Organizations-managed accounts. StackSets auto-creates IAM roles. Requires trusted access and "all features" enabled in Organizations. Supports automatic deployments to new accounts.
- **Diagram Description**: Admin account with AWSCloudFormationStackSetAdministrationRole trusts target accounts' AWSCloudFormationStackSetExecutionRole via AWS Organizations.

### StackSets with AWS Organizations
- Auto-deploy stack instances to new accounts.
- Delegate administration to member accounts.
- Enable trusted access first for delegated admins.
- **Diagram Description**: (Delegated) Admin Account → StackSet → OUs (Prod/Dev) → Member Accounts (A/B/C/New) with Stack Instances.

### Hands-On: StackSets
- Example: Enable AWS Config across regions with one click.
- **Diagram Description**: Admin/Target Account → Template → StackSet → Enable AWS Config in Regions 1/2/3.

### CloudFormation Troubleshooting
- **DELETE_FAILED**: Resources like S3 buckets must be emptied first. Use Custom Resources/Lambda for automation. Security Groups require all EC2 instances gone. Use DeletionPolicy=Retain.
- **UPDATE_ROLLBACK_FAILED**: Caused by external changes, permissions issues, or ASG signals. Fix manually, then use ContinueUpdateRollback.

### CloudFormation StackSet Troubleshooting
- **OUTDATED Status**: Insufficient permissions, global resource conflicts (e.g., unique S3 buckets), no trust relationship, or resource limits/quotas exceeded.

### CloudFormation ChangeSets
- Preview changes before updating stacks for confidence.
- Won't predict success/failure.
- For nested stacks, shows changes across all.
- **Diagram Description**: Original Stack → Create ChangeSet → View/Execute → Updated Stack. Additional ChangeSets optional.

### cfn-hup
- Polls for Metadata changes every 15 minutes on EC2 instances and reapplies configuration.
- Relies on configs: /etc/cfn/cfn-hup.conf and /etc/cfn/hooks.d/cfn-auto-reloader.conf.
- **Diagram Description**: EC2 Instance launches → Retrieves init data from CloudFormation → Checks Metadata changes every 15 mins → Re-runs config if detected.

### CloudFormation Drift
- Detects manual changes outside CloudFormation.
- Compares stack/resources to template.
- **Diagram Description**: Stack (e.g., Security Group) modified via EC2 Console → Compare to Template → Drifted!

### StackSet Drift Detection
- Detects drifts in stacks/instances/StackSet.
- Ignores changes made directly via CloudFormation (not at StackSet level).
- Drifts from unmanaged changes (e.g., EC2 Console).
- Can stop detection.
- **Diagram Description**: Admin Account → StackSet → Target Account Stack Instance → User modifies EC2 via Console → Drifted.

## 2. AWS Service Catalog
- Self-service portal for launching approved IT products (CloudFormation templates).
- Ensures compliance, consistency, governance.
- No deep AWS knowledge needed for users.
- Integrates with ServiceNow.
- **Products**: CloudFormation templates (e.g., VMs, DBs, storage).
- **Portfolios**: Collections of products assigned to teams.
- **Provisioned Products**: Launched, ready-to-use instances (configured/tagged).
- **Diagram Description**: Admin: Templates → Products → Portfolio (with IAM access). User: Launches → Provisioned Products.

### Service Catalog – Stack Set Constraints
- Configure deployments via StackSets: Accounts, Regions (with order), Permissions (IAM StackSet Admin Role).
- **Diagram Description**: Portfolio → Product → StackSets in Regions (e.g., eu-west-1, us-west-2) across Accounts.

### Service Catalog – Launch Constraints
- IAM Role for launching/updating/terminating products with minimal user permissions.
- Role needs: CloudFormation full access, AWS services in template, S3 read for template.

### Service Catalog – Continuous Delivery Pipeline (Syncing with CodeCommit)
- Sync products from CodeCommit repo.
- **Diagram Description**: Developer pushes to CodeCommit (e.g., product-a.yml) → Lambda (SyncServiceCatalogFunction) → Updates Service Catalog Products.

## 3. Elastic Beanstalk
### Overview
- Developer-centric: Deploys apps using EC2, ASG, ELB, RDS, etc.
- Managed: Handles provisioning, LB, scaling, health monitoring.
- Developer responsible for code only.
- Free (pay for resources).
- Solves developer problems: Infra management, deployments, config, scaling.

### Components
- **Application**: Collection of environments, versions, configs.
- **Application Version**: Code iteration.
- **Environment**: AWS resources running one version. Tiers: Web Server or Worker. Multiple envs (dev/test/prod).
- **Diagram Description**: Create App → Upload Version → Launch/Manage Env → Update/Deploy Versions.

### Supported Platforms
- Go, Java SE/Tomcat, .NET Core/Linux, .NET Windows, Node.js, PHP, Python, Ruby, Packer Builder, Single/Multi-Container Docker, Preconfigured Docker.

### Web Server Tier vs. Worker Tier
- **Web Server**: ELB + ASG (EC2 web servers).
- **Worker**: SQS Queue + ASG (EC2 workers). Scales on SQS messages. Push from Web Tier.
- **Diagram Description**: Web: ELB → ASG (EC2). Worker: SQS → ASG (EC2 pulling messages).

### Deployment Modes
- **Single Instance**: Dev (EC2 + Elastic IP + RDS).
- **High Availability**: Prod (ALB + ASG + Multi-AZ RDS).

### Deployment Options for Updates
- **All at Once**: Fastest, downtime. Good for dev.
- **Rolling**: Bucket-based, below capacity, both versions run. No extra cost, longer.
- **Rolling with Additional Batches**: At capacity, both versions, small extra cost, longer. Good for prod.
- **Immutable**: New ASG, zero downtime, double capacity, longest. Quick rollback. Good for prod.
- **Blue/Green**: New env, swap URLs. Zero downtime, validate independently.
- **Traffic Splitting**: Canary – % traffic to new ASG, monitor, auto-rollback. No downtime.
- Diagrams described in content (e.g., buckets for rolling, temp ASG for immutable).

### Notifications
- EventBridge rules for: Env operations (create/update/terminate), Resource status (ASG/ELB/EC2), Managed updates, Health status.
- **Diagram Description**: Elastic Beanstalk → EventBridge → SNS (email) or Lambda (message).

## 4. AWS SAM (Serverless Application Model)
- Framework for serverless apps.
- YAML config generates CloudFormation.
- Supports Outputs, Mappings, Parameters, Resources.
- Uses CodeDeploy for Lambda deploys.
- Local run: Lambda, API Gateway, DynamoDB.
- **Recipe**: Transform: 'AWS::Serverless-2016-10-31'. Resources: Function/Api/SimpleTable. Deploy: sam deploy/sync.
- **Deployment Diagram**: SAM YAML → Build/Package → S3 + CF Template → CF Stack (Lambda/API/DDB).
- **SAM Accelerate (sam sync)**: Fast sync code/infra. Options: --code (bypass CF), --resource, --watch.
- **SAM + CodeDeploy**: Traffic shifting, hooks, rollback via CW Alarms. AutoPublishAlias, DeploymentPreference (Canary/Linear/AllAtOnce).

## 5. AWS CDK (Cloud Development Kit)
- Define infra in JS/TS/Python/Java/.NET.
- High-level constructs compile to CF Template.
- Deploy infra + code (Lambda/Docker in ECS/EKS).
- **Diagram**: CDK App (Constructs) → cdk synth → CF Template → CloudFormation.
- **CDK vs SAM**: CDK (all AWS, programmatic). SAM (serverless, declarative).
- **CDK + SAM**: cdk synth → SAM CLI local invoke.
- **Hands-On Example**: S3 Upload → Lambda (Rekognition) → DynamoDB.

## 6. AWS Step Functions
- State machines for workflows (e.g., order fulfillment, data processing).
- JSON-based, visualized executions/history.
- Start via SDK/API Gateway/EventBridge.
- **Task States**: Invoke AWS services (Lambda/Batch/ECS/DDB/SNS/SQS/Step Functions) or Activities (poll-based).
- **States**: Choice (branch), Fail/Succeed, Pass (inject data), Wait (delay), Map (iterate), Parallel (branches).
- **Diagram**: Visual workflow in console.

## 7. AWS AppConfig
- Dynamic configs independent of code deploys.
- No restarts. For feature flags, tuning, allow/block.
- Works with EC2/Lambda/ECS/EKS.
- Gradual deploys, rollback via CW Alarms.
- Validate: JSON Schema (syntax) or Lambda (semantics).
- **Diagram**: Config Sources (SSM/S3) → Validate → Apps poll changes → CW Alarm triggers rollback.

## 8. AWS Systems Manager (SSM)
- Manage EC2/On-Prem at scale. Insights, patching, compliance.
- Integrated with CW/Config. Free.
- **Features Table**:

| Category | Features |
|----------|----------|
| Operations Management | Explorer, OpsCenter, CW Dashboard, PHD, Incident Manager |
| Shared Resources | Documents |
| Change Management | Change Manager, Automation, Change Calendar, Maintenance Windows |
| Application Management | App Manager, AppConfig, Parameter Store |
| Node Management | Fleet Manager, Compliance, Inventory, Hybrid Activations, Session Manager, Run Command, State Manager, Patch Manager, Distributor |

- **How it Works**: Install SSM Agent (default on Amazon Linux 2/Ubuntu). EC2 needs IAM role.
- **Diagram**: EC2/On-Prem (SSM Agent) → SSM with IAM.

### AWS Tags & Resource Groups
- Key-value pairs (e.g., Name, Env, Team).
- For grouping, automation, cost allocation.
- **Resource Groups**: Logical groups via tags (e.g., Env=Dev). Works with EC2/S3/DDB/Lambda.
- **Diagram**: Resources tagged Env=Dev → Group.

### SSM Documents
- JSON/YAML. Define params/actions.
- Used in Run Command/State Manager/Patch Manager/Automation/Parameter Store.

### SSM Run Command
- Execute scripts/commands on multiple instances (via groups).
- Rate/Error control, IAM/CloudTrail integrated. No SSH.
- Output to Console/S3/CW Logs. SNS notifications. EventBridge invoke.
- **Diagram**: EventBridge → Run Command → Output to S3/CW Logs/SNS.

### SSM Automation
- Maintenance/deploy tasks (e.g., restart EC2, AMI snapshot).
- Runbooks: SSM Automation docs (AWS/custom).
- Triggers: Console/CLI/SDK, EventBridge, Maintenance Windows, Config remediations.
- **Diagram**: Triggers → Runbooks → Execute on EC2/AWS Resources.

### SSM Parameter Store
- Secure config/secrets storage. KMS encryption. Versioning, IAM security, EventBridge notifications, CF integration.
- **Hierarchy**: e.g., /my-dept/my-app/dev/db-url. Get via API.
- **Tiers Table**:

| Feature | Standard | Advanced |
|---------|----------|----------|
| Total Params | 10,000 | 100,000 |
| Max Size | 4 KB | 8 KB |
| Policies | No | Yes |
| Cost | Free | $0.05/param/month |

- **Policies (Advanced)**: Expiration, ExpirationNotification, NoChangeNotification (via EventBridge).

### SSM Patch Manager
- Automate OS/app/security patching.
- On-demand or scheduled (Maintenance Windows).
- Scan/report compliance (to S3).
- **Patch Baseline**: Approved/rejected patches. Custom or pre-defined (e.g., AWS-RunPatchBaseline).
- **Patch Group**: Instances tagged (e.g., Patch Group=Dev) linked to baseline.
- **Diagram**: Instances (tagged) → Patch Manager → Baselines → Run AWS-RunPatchBaseline.

### SSM Maintenance Windows
- Schedule actions (e.g., patching, software install).
- Contains: Schedule, Duration, Targets, Tasks.

### SSM Session Manager
- Secure shell access (no SSH/bastions/keys).
- Supports Linux/macOS/Windows.
- Logs to S3/CW Logs. CloudTrail events.
- IAM: Control access/commands via tags/policies.
- **SSH vs SSM Table**:

| Aspect | SSH | SSM Session Manager |
|--------|-----|----------------------|
| Access | Port 22, IP-based | Console/CLI/SDK, IAM |
| Security | Keys/Bastions | No inbound ports, logs to S3/CW |
| Requirements | SG rules | SSM Agent, IAM profile |

- **Default Host Management Config (DHMC)**: Auto-config EC2 as managed (no instance profile). Uses Instance Identity Role. Enables Session/Patch/Inventory. Region-based, IMDSv2 required.
- **Hybrid Environments**: Manage on-prem/VMs/IoT. Prefix "mi-". Hybrid Activation (code/ID).
- **Automating Hybrid**: API GW + Lambda for activations.
- **IoT Greengrass**: SSM Agent as component. Token Exchange Role permissions.
- **VPC Endpoint for Private**: Interface Endpoints for ssm/ssmmessages/kms/logs/s3.

### SSM Automation Use Cases
- Start/Stop/Resize EC2/RDS via EventBridge (cost reduction).
- Weekly golden AMI build → Store in Parameter Store.
- Config remediation (e.g., enable S3 versioning).

### SSM Compliance
- Scan patches/associations. Sync to S3 for Athena/QuickSight. Multi-account/region. To Security Hub.

### SSM OpsCenter
- Central issue investigation/remediation (e.g., Security Hub, DynamoDB throttle).
- **OpsItems**: Issues from events/resources. Recommended runbooks.
- **Triggers**: CW/App Insights/EventBridge/Config/SSM/DevOps Guru/Sec Hub/SNS.
- **Use Case**: Delete orphaned EBS volumes (EventBridge + Lambda → OpsItems → Automation).

## 9. AWS Lambda (Resilient Aspects)
- **Versions**: $LATEST (mutable) → Publish immutable versions (V1, V2) with ARNs.
- **Aliases**: Mutable pointers (dev/test/prod) to versions. Enable canary (weights). Own ARNs.
- **Env Variables**: Key-value strings. Adjust behavior. Store KMS-encrypted secrets.
- **Concurrency/Throttling**: 1000 default limit. Reserved per function. Throttle: 429 sync, retry/DLQ async.
- **Concurrency Issue**: Unreserved can throttle high-traffic sources.
- **Async Invocations**: Throttles retry exponentially (1s to 5m, up to 6h).
- **Cold Starts**: Init latency. **Provisioned Concurrency**: Pre-allocate, no cold starts. Auto Scaling manages.
- **File Systems**: Mount EFS in VPC via Access Points. Watch limits.
- **Storage Options Table**:

| Option | Max Size | Persistence | Pricing | Sharing |
|--------|----------|-------------|---------|---------|
| /tmp | 10,240 MB | Ephemeral | Included | No |
| Layers | 250 MB total | Durable | Included | Yes |
| S3 | Elastic | Durable | Storage + Req | Yes |
| EFS | Elastic | Durable | Storage + TP | Yes |

- **Cross-Account EFS**: VPC Peering + Permissions (DescribeFileSystems, etc.) + EFS Policy.

## 10. AWS API Gateway
- Serverless API: Lambda integration, WebSocket, versioning, envs, security, throttling, Swagger, transforms, SDKs, caching.
- **Integrations**: Lambda (REST), HTTP (e.g., ALB), AWS Service (e.g., Step Functions/SQS).
- **AWS Service Example**: API GW → Kinesis Streams/Firehose → S3.
- **Endpoint Types**: Edge-Optimized (CloudFront), Regional (same region), Private (VPC Endpoint).
- **Security**: IAM/Cognito/Custom Authorizer. ACM for HTTPS (us-east-1 for Edge).
- **Deployment Stages**: Deploy changes to stages (dev/test/prod). Rollback history.
- **Stages v1/v2**: Separate URLs for breaking changes.
- **Stage Variables**: Like env vars. Use in Lambda ARN/HTTP/Mappings. e.g., ${stageVariables.varName}.
- **Stage Vars + Lambda Aliases**: Point aliases (dev/prod) to versions without API changes.
- **Canary Deployment**: % traffic to canary stage. Separate metrics/logs. Override vars.
- **OpenAPI Spec**: Define APIs as code (JSON/YAML). Import/Export. Generate SDKs.
- **Request Validation**: Basic checks (params/payload via JSON Schema). Fail fast (400 error). Setup via OpenAPI.
- **Caching**: Reduce backend calls. TTL 300s (0-3600). Per stage/method. Encrypt. Size 0.5-237 GB.
