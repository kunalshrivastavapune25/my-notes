# **AWS DevOps Pro - Final Notes Set**

## **Domain 3: Resilient Cloud Solutions (Continued)**

Sure! Here are your notes rewritten in **simple English**, with **real-world case studies/examples**, and **possible AWS DevOps exam-style questions**.

---

# ✅ **Application Auto Scaling – Integrated Services (Simple Notes + Case Studies)**

Application Auto Scaling lets AWS services automatically increase or decrease capacity based on demand.

| **Service**       | **What can be scaled automatically?** | **Simple Case Study Example**                                                                                 |
| ----------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| AppStream 2.0     | Virtual desktops (Fleets)             | A school uses AppStream 2.0 for online labs. During exams more students log in → fleet auto-scales.           |
| Aurora            | Read Replicas                         | An e-commerce site gets more read traffic during a sale → Aurora adds more read replicas.                     |
| Comprehend        | Document classifier endpoints         | A news agency uses Comprehend to analyze articles. During breaking news, requests increase → endpoints scale. |
| DynamoDB          | Tables & Global Secondary Indexes     | A game app sees a spike in player logins → DynamoDB auto-scales read/write capacity.                          |
| ECS               | Services                              | A food delivery app has more orders at dinner time → ECS adds more containers.                                |
| ElastiCache Redis | Replication Groups                    | A social media app uses Redis for caching. More users -> More Redis read replicas.                            |
| EMR               | Clusters                              | A data analytics company runs big jobs at night → EMR automatically adds more nodes.                          |
| Keyspaces         | Cassandra tables                      | IoT company collects data from 10,000 devices → Keyspaces scales automatically.                               |
| Lambda            | Provisioned Concurrency               | A ticket booking site prepares for sale → keeps 100 Lambda instances ready.                                   |
| MSK (Kafka)       | Broker Storage                        | Streaming platform needs to store more logs → MSK increases storage.                                          |
| Neptune           | Graph database clusters               | A social network grows fast → Neptune scales read replicas.                                                   |
| SageMaker         | Endpoint Variants                     | AI model predicts prices. New model is tested with 20% traffic → weighted endpoint.                           |
| Spot Fleet        | Spot instance requests                | Video rendering company uses Spot Fleet. When job load increases, Spot Fleet adds more spot instances.        |
| Custom resources  | Any AWS resource via Lambda           | A company wrote a Lambda to auto-scale SFTP EC2 servers.                                                      |

---

# ✅ **ALB (Application Load Balancer) Advanced Features**

### 🔹 1. **Listener Rules**

* ALB checks rules **from top to bottom**.
* If no rule matches → **default rule** is applied.

**Types of Conditions**:

* **host-header** → `api.company.com`
* **path-pattern** → `/images/*`, `/login`
* **source-ip** → Allow only office IPs.
* **http-header** → Check for specific browser/user-agent.
* **query-string** → `?version=beta`
* **http-method** → GET, POST, PUT, etc.

**Actions**:

* **forward** to target group (default)
* **redirect** to HTTPS
* **fixed-response** (like 403 Access Denied)

**Case Study**:

* `/api/*` Path → Send to ECS API backend
* `/images/*` → Send to S3-backed service
* Everything else → Default 404 page

---

### 🔹 2. **Target Group Weighting**

Used in:
✔ Blue/Green Deployment
✔ Canary Testing

**Example**:

| Environment | Traffic % |
| ----------- | --------- |
| Blue (old)  | 80%       |
| Green (new) | 20%       |

**Case Study**:

* New version of app is deployed but tested with only 20% users.
* If no error → slowly increase to 100%.

---

# ✅ **ELB Networking Concepts**

### 🔹 DualStack – IPv4 + IPv6

* ALB/NLB can support **both IPv4 and IPv6**.
* Useful when modern devices access from IPv6 internet.

### 🔹 NLB + AWS PrivateLink

* Share service across **different VPCs** without peering.
* Works even if **IP address ranges overlap**.
* Uses VPC **Interface Endpoints**.

**Case Study**:
A bank has a core service in VPC-A. Another team in VPC-B needs access without peering → use PrivateLink.

---

# ✅ **NAT Gateway (Simple Explanation)**

| Feature            | Detail                                                    |
| ------------------ | --------------------------------------------------------- |
| Purpose            | Allows private subnet EC2 to access the internet securely |
| Managed by         | AWS (fully managed)                                       |
| Placed in          | One AZ with Elastic IP                                    |
| Speed              | Starts at 5 Gbps → Scales to 100 Gbps                     |
| No Security Groups | It does not require inbound rules                         |
| Use Case           | EC2 in private subnet downloads patches/updates           |

---

### ✅ **NAT Gateway vs NAT Instance**

| Feature               | NAT Gateway        | NAT Instance                   |
| --------------------- | ------------------ | ------------------------------ |
| Availability          | Highly available   | Needs manual failover scripts  |
| Speed                 | Up to 100 Gbps     | Depends on EC2 type            |
| Managed by            | AWS                | You manage updates, patching   |
| Cost                  | Hourly + data cost | EC2 instance cost              |
| Bastion/SSH possible? | ❌ No               | ✅ Yes, can act as Bastion Host |

---

# 🎯 **AWS DevOps Exam Sample Questions**

**1. Which service can Application Auto Scaling NOT scale?**
A. DynamoDB
B. Lambda Provisioned Concurrency
C. S3 Bucket Size
D. ECS Services
✔ **Answer: C**

**2. For Blue/Green deployment using ALB, which feature is used?**
A. Host-based routing
B. Path-based routing
C. Target Group Weighting
D. SSL Offloading
✔ **Answer: C**

**3. What is the main difference between NAT Gateway and NAT Instance?**
✔ NAT Gateway is fully managed and auto-scales. NAT Instance requires manual setup.

**4. What does PrivateLink solve?**
✔ Sharing services across VPCs with overlapping IP addresses.

**5. Which ALB condition forwards traffic based on `/api/*`?**
✔ Path-pattern rule.

---

Would you like me to create **flashcards, tables, or mindmaps** for quick revision?

## **Multi-AZ & Multi-Region Architectures**

### **Multi-AZ Services**
- **Manual Setup**: EFS, ELB, ASG, Beanstalk, RDS, ElastiCache
- **Automatic**: S3, DynamoDB, Aurora (storage), proprietary AWS services
- **Blue-Green Deployments**:
  - **ALB**: Switch target groups
  - **Route 53**: DNS-based switching
  - **API Gateway**: Canary deployments

### **Multi-Region Services**
- **DynamoDB Global Tables**: Multi-way replication
- **AWS Config Aggregators**: Cross-region/account
- **RDS Cross-Region Read Replicas**: Read scaling & DR
- **Aurora Global Database**: <1s replication
- **S3 Cross-Region Replication**: Data redundancy
- **Route 53**: Global DNS with health checks

### **Route 53 Health Checks**
- **Endpoint Monitoring**: Application health checks
- **Calculated Health Checks**: Monitor other health checks
- **CloudWatch Alarms**: Full control over metrics
- **Integrated**: With CloudWatch metrics

---

## **Disaster Recovery Strategies**

### **RPO vs RTO**
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime

### **DR Strategies**
| Strategy | RTO | RPO | Cost | Complexity |
|----------|-----|-----|------|------------|
| **Backup & Restore** | Hours | Hours | Low | Low |
| **Pilot Light** | 10s of minutes | Minutes | Low | Medium |
| **Warm Standby** | Minutes | Minutes | Medium | High |
| **Hot Site/Multi-Site** | Seconds | Seconds | High | Very High |

### **DR Tips**
- **Backup**: EBS snapshots, RDS backups, S3 lifecycle policies
- **High Availability**: Route 53, Multi-AZ services
- **Replication**: Cross-region, database replication
- **Automation**: CloudFormation, Lambda, Elastic Beanstalk
- **Chaos Engineering**: Netflix Simian Army

---

## **Domain 4: Monitoring and Logging**

### **CloudWatch Metrics**
- **Namespaces**: Logical containers for metrics
- **Dimensions**: Attributes (up to 30 per metric)
- **Custom Metrics**: `PutMetricData` API
  - **Standard**: 1-minute resolution
  - **High Resolution**: 1/5/10/30 seconds
- **Metric Streams**: Real-time streaming to Kinesis Firehose

### **Advanced Monitoring**
- **Anomaly Detection**: ML-based baseline detection
- **Lookout for Metrics**: Automated anomaly detection with root cause analysis
- **Composite Alarms**: Combine multiple alarm states (AND/OR conditions)

### **CloudWatch Logs**
- **Log Groups**: Application-level grouping
- **Log Streams**: Instance/file/container level
- **Retention**: 1 day to 10 years or never
- **Sources**: SDK, agents, Elastic Beanstalk, ECS, Lambda, VPC Flow Logs

### **Log Processing**
- **Logs Insights**: Query engine for log analysis
- **Metric Filters**: Create metrics from log patterns
- **Subscriptions**: Real-time log streaming to Kinesis/Lambda
- **Export to S3**: Batch export (not real-time)

### **Log Types**
- **Application Logs**: Custom application code
- **OS Logs**: System events (/var/log/messages)
- **Access Logs**: Request logs (ALB, CloudFront, S3)
- **AWS Managed**: CloudTrail, VPC Flow, Route 53

### **CloudWatch Agents**
- **Logs Agent**: Legacy, logs only
- **Unified Agent**: Logs + system metrics (RAM, disk, processes)
- **Centralized Config**: SSM Parameter Store

### **CloudWatch Alarms**
- **States**: OK, INSUFFICIENT_DATA, ALARM
- **Periods**: Evaluation time windows
- **Targets**: EC2 actions, Auto Scaling, SNS
- **EC2 Recovery**: Automatic instance recovery

### **CloudWatch Synthetics**
- **Canary Monitoring**: Script-based availability testing
- **Blueprints**: Heartbeat, API, broken links, visual monitoring
- **Integration**: CloudWatch Alarms for automation

### **Athena**
- **Serverless SQL**: Query S3 data
- **Performance**: Use Parquet/ORC, partition data, compress
- **Federated Query**: Cross-data source queries via Lambda connectors

---

## **Domain 5: Incident and Event Response**

### **EventBridge**
- **Event Buses**: Default, partner, custom
- **Rules**: Schedule (cron) and event patterns
- **Schema Registry**: Automatic schema discovery and code generation
- **Resource Policies**: Cross-account event sharing

### **S3 Event Notifications**
- **Direct Integration**: S3 → SNS/SQS/Lambda
- **EventBridge**: Advanced filtering, multiple destinations
- **IAM Permissions**: Resource policies required

### **S3 Object Integrity**
- **Checksums**: MD5, SHA-1, SHA-256, CRC32
- **ETag**: Object version identifier
- **Validation**: Client and server-side checksum verification

### **AWS Health Dashboard**
- **Service Health**: General AWS service status
- **Personal Health**: Account-specific impacts
- **EventBridge Integration**: Automated response to health events

### **EC2 Status Checks**
- **System Checks**: Underlying hardware issues
- **Instance Checks**: OS/configuration issues
- **EBS Checks**: Volume connectivity
- **Recovery**: Stop/start for system issues, reboot for instance issues

### **CloudTrail**
- **Management Events**: Resource configuration changes
- **Data Events**: S3 object-level, Lambda invoke
- **Insights Events**: Anomaly detection
- **Retention**: 90 days in CloudTrail, indefinite in S3

### **Dead Letter Queues**
- **SQS DLQ**: Failed message processing after max receives
- **SNS DLQ**: Undeliverable messages after retries
- **Redrive**: Move messages back to source queue after fixes

### **X-Ray & Distributed Tracing**
- **Service Map**: Visualize microservices architecture
- **Integrations**: EC2, ECS, Lambda, API Gateway, Beanstalk
- **OpenTelemetry**: AWS-distributed open standard

---

## **Domain 6: Security and Compliance**

### **AWS Config**
- **Compliance Auditing**: Resource configuration tracking
- **Config Rules**: AWS-managed (75+) or custom (Lambda)
- **Remediation**: SSM Automation documents
- **Aggregators**: Cross-account/region view
- **Conformance Packs**: Packaged rules and remediations

### **AWS Organizations**
- **Service Control Policies (SCP)**: Allow/deny lists at OU/account level
- **Feature Modes**: Consolidated billing vs. All features
- **Moving Accounts**: Remove → Invite → Accept process
- **Reserved Instances**: Discount sharing across organization

### **AWS Control Tower**
- **Landing Zone**: Best-practice multi-account setup
- **Account Factory**: Standardized account provisioning
- **Guardrails**: Preventive (SCP) and detective (Config) controls
- **Levels**: Mandatory, strongly recommended, elective

### **IAM Identity Center (Successor to SSO)**
- **Single Sign-On**: AWS accounts, business apps, SAML 2.0
- **Permission Sets**: Collections of IAM policies
- **ABAC**: Attribute-based access control
- **External IdPs**: SAML 2.0 + SCIM for synchronization

### **WAF & Shield**
- **WAF**: Layer 7 protection (ALB, API Gateway, CloudFront)
- **Managed Rules**: 190+ pre-configured rules
- **Firewall Manager**: Cross-account WAF management
- **Shield Advanced**: DDoS protection with SRT support

### **GuardDuty**
- **Threat Detection**: ML-based anomaly detection
- **Data Sources**: CloudTrail, VPC Flow Logs, DNS logs
- **Multi-Account**: Centralized management
- **Findings**: Severity 0.1-8.0 with automated response

### **Other Security Services**
- **Detective**: Security investigation using graph analysis
- **Inspector**: Automated vulnerability assessment (EC2, ECR, Lambda)
- **Secrets Manager**: Secret rotation, multi-region replication

---

## **Other Important Services**

### **AMI Management**
- **Cross-Account Sharing**: Share unencrypted or customer-managed KMS encrypted AMIs
- **Cross-Account Copy**: Become owner of copied AMI
- **KMS Requirements**: Share keys for encrypted AMIs

### **Trusted Advisor**
- **Checks**: Cost, performance, security, fault tolerance, service limits
- **Support Levels**: Business/Enterprise for full access
- **Monitoring**: EventBridge integration for alerts

### **AWS Glue**
- **ETL Service**: Extract, transform, load
- **Data Catalog**: Central metadata repository
- **Streaming ETL**: Kinesis, Kafka, MSK integration

### **QuickSight**
- **BI Service**: Interactive dashboards and analytics
- **Serverless**: Auto-scaling, per-session pricing
- **Integration**: RDS, Aurora, Redshift, Athena, S3

---

## **Exam Preparation Tips**

### **Certification Paths**
- **Foundational**: Cloud Practitioner
- **Associate**: Solutions Architect, Developer, SysOps
- **Professional**: Solutions Architect, DevOps Engineer
- **Specialty**: Security, Advanced Networking, etc.

### **Study Strategy**
- **Hands-on Practice**: Essential for DevOps exam
- **AWS Documentation**: Deep dive into services
- **Practice Exams**: Identify knowledge gaps
- **AWS Blogs**: Stay updated on new features

### **Key Focus Areas for DevOps**
- **CI/CD**: CodePipeline, CodeBuild, CodeDeploy
- **Infrastructure as Code**: CloudFormation, CDK, SAM
- **Monitoring & Logging**: CloudWatch, X-Ray
- **Security & Compliance**: IAM, Config, Organizations
- **High Availability**: Multi-AZ, Multi-Region strategies

---

## **Congratulations!**

You've now covered the entire AWS DevOps Engineer Professional curriculum. Remember:

1. **Practice extensively** - hands-on experience is crucial
2. **Review these notes** regularly for quick revision
3. **Take practice exams** to identify weak areas
4. **Stay calm** during the exam - you've got this!

**Good luck with your certification journey! 🚀**

---

*These notes complete the entire AWS DevOps Engineer Professional course coverage. Use them for your final revision and exam preparation.*
