# **AWS DevOps Pro - Continuation Notes (Part 2)**

## **API Gateway - Advanced Features**

### **Cache Invalidation**
- **Manual Invalidation**: Flush entire cache immediately via console/API
- **Programmatic Invalidation**: Clients can invalidate cache with header:
  ```http
  Cache-Control: max-age=0
  ```
- **Security**: Requires IAM authorization (`InvalidateCache` policy)
- **Default**: Without authorization policy, any client can invalidate cache

### **Logging & Tracing**
- **CloudWatch Logs**:
  - Enable at Stage level
  - Log Levels: ERROR, DEBUG, INFO
  - Contains request/response body information
- **X-Ray Tracing**:
  - Provides end-to-end request tracing
  - Combine with Lambda for full picture
  - Helps debug performance issues

### **CloudWatch Metrics**
| Metric | Description | Use Case |
|--------|-------------|----------|
| `CacheHitCount` & `CacheMissCount` | Cache efficiency | Cache performance |
| `Count` | Total API requests | Traffic volume |
| `IntegrationLatency` | Backend processing time | Backend performance |
| `Latency` | Total client response time | End-to-end performance |
| `4XXError` | Client-side errors | Client issues |
| `5XXError` | Server-side errors | Backend issues |

### **Throttling & Limits**
- **Account Limit**: 10,000 RPS across all APIs (soft limit)
- **Throttling Response**: 429 Too Many Requests
- **Granular Controls**:
  - Stage-level limits
  - Method-level limits  
  - Usage Plans (per customer)
- **Risk**: One overloaded API can throttle others if not limited

### **Common Errors**
- **4xx Client Errors**:
  - 400: Bad Request
  - 403: Access Denied / WAF filtered
  - 429: Throttle / Quota exceeded
- **5xx Server Errors**:
  - 502: Bad Gateway (Lambda proxy issues)
  - 503: Service Unavailable
  - 504: Integration Timeout (29-second max)

---

## **Amazon ECS (Elastic Container Service)**

### **Launch Types**
| Feature | EC2 Launch Type | Fargate Launch Type |
|---------|----------------|---------------------|
| **Infrastructure** | You manage EC2 instances | Serverless (AWS manages) |
| **Scaling** | Auto Scaling Groups | Automatic task scaling |
| **Pricing** | Pay for EC2 instances | Pay per vCPU/RAM |
| **Maintenance** | OS patching required | Fully managed |

### **IAM Roles**
- **EC2 Instance Profile** (EC2 Launch Type only):
  - ECS Agent API calls
  - CloudWatch Logs, ECR access
  - Secrets Manager/Parameter Store
- **ECS Task Role**:
  - Per-task specific permissions
  - Defined in task definition
  - Different roles per service

### **Load Balancer Integration**
- **ALB**: Most common use cases
- **NLB**: High throughput/performance, AWS Private Link
- **Classic ELB**: Not recommended (no Fargate support)

### **Data Volumes - EFS Integration**
- **Both Launch Types**: EC2 and Fargate
- **Multi-AZ Shared Storage**: Tasks in any AZ access same data
- **Fargate + EFS = Serverless** persistent storage

### **Auto Scaling**
- **Service Auto Scaling** (Task Level):
  - CPU/Memory utilization
  - ALB Request Count Per Target
  - Target Tracking, Step Scaling, Scheduled
- **EC2 Auto Scaling** (Instance Level - EC2 Launch Type):
  - Scale underlying EC2 instances
  - Capacity Providers for automatic provisioning

### **Event-Driven ECS**
```yaml
EventBridge → ECS Task → DynamoDB/S3
```
- **Use Cases**: File processing, batch jobs, scheduled tasks
- **Event Sources**: S3 events, scheduled events, custom events

### **Logging**
- **awslogs Driver**: Direct to CloudWatch Logs
- **Sidecar Container**: Centralized log collection
- **Fargate**: Task Execution Role permissions required
- **EC2**: Configure `ECS_AVAILABLE_LOGGING_DRIVERS`

---

## **Amazon ECR (Elastic Container Registry)**

### **Lifecycle Policies**
- **Automate Image Cleanup**: Remove old/unused images
- **Rule Types**: Age-based or count-based
- **Evaluation**: All rules evaluated simultaneously
- **Expiration**: Within 24 hours after meeting criteria

### **CI/CD Pipeline**
```yaml
CodeCommit → CodeBuild → ECR → ECS/Fargate
```
- **Secure**: IAM-controlled access
- **Integrated**: With ECS, EKS, Lambda
- **Features**: Vulnerability scanning, versioning, lifecycle

---

## **Amazon EKS (Elastic Kubernetes Service)**

### **Node Types**
- **Managed Node Groups**: AWS manages nodes (ASG)
- **Self-Managed Nodes**: You manage nodes (your ASG)
- **Fargate**: Serverless, no node management

### **Storage**
- **StorageClass Manifest**: Required for persistent volumes
- **Supported**:
  - EBS (block storage)
  - EFS (file storage - works with Fargate)
  - FSx for Lustre/NetApp ONTAP

### **Logging**
- **Control Plane Logs**: API, Audit, Authenticator, etc.
- **Node/Container Logs**: Fluent Bit/Fluentd to CloudWatch
- **Container Insights**: Monitoring dashboard

---

## **Amazon Kinesis**

### **Kinesis Data Streams**
- **Real-time** streaming data collection
- **Retention**: Up to 365 days
- **Replay Capability**: Reprocess data
- **Ordering Guarantee**: Same partition key
- **Capacity Modes**:
  - **Provisioned**: Choose shard count
  - **On-demand**: Automatic scaling

### **Data Firehose**
- **Fully Managed**: No administration
- **Destinations**: S3, Redshift, OpenSearch, HTTP endpoints
- **Transformations**: Lambda functions
- **Near Real-time**: Buffering based on size/time

### **Managed Service for Apache Flink**
- **Stream Processing**: Java, Scala, SQL
- **Managed Cluster**: Automatic scaling, backups
- **Use Cases**: Complex event processing, real-time analytics

---

## **Amazon Route 53**

### **Record Types**
- **A**: IPv4 address
- **AAAA**: IPv6 address  
- **CNAME**: Canonical name (subdomains only)
- **NS**: Name Servers for hosted zone

### **Hosted Zones**
- **Public**: Internet-facing domains
- **Private**: VPC-only domains
- **Cost**: $0.50 per month per hosted zone

### **Routing Policies**
| Policy | Use Case | Key Feature |
|--------|----------|-------------|
| **Weighted** | Load balancing, testing | Traffic percentage |
| **Latency-based** | Performance | Lowest latency region |
| **Failover** | Disaster recovery | Active-passive |
| **Geolocation** | Content localization | User location |
| **Multi-value** | Simple load balancing | Multiple healthy records |

---

## **RDS & Aurora**

### **Read Replicas**
- **Scalability**: Up to 15 replicas
- **Use Cases**: Reporting, analytics, read scaling
- **Replication**: Async (eventually consistent)
- **Cross-Region**: Additional network cost

### **Multi-AZ Deployment**
- **High Availability**: Sync replication to standby
- **Automatic Failover**: Single DNS name
- **Zero Downtime**: Seamless promotion

### **Aurora Global Database**
- **Cross-Region**: <1 second replication lag
- **Disaster Recovery**: <1 minute RTO
- **Read Scaling**: Up to 16 replicas per region

---

## **Amazon ElastiCache**

### **Redis vs Memcached**
| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Replication** | Multi-AZ, Read Replicas | Sharding only |
| **Persistence** | AOF persistence | Non-persistent |
| **Data Types** | Strings, Sets, Sorted Sets | Strings only |
| **Architecture** | Single-threaded | Multi-threaded |

### **Cluster Modes**
- **Disabled**: Single shard, 1 primary + 5 replicas
- **Enabled**: Multiple shards, up to 500 nodes
- **Auto Scaling**: Shard and replica scaling (Cluster Mode Enabled only)

### **Connection Endpoints**
- **Primary Endpoint**: Write operations
- **Reader Endpoint**: Read load balancing
- **Configuration Endpoint**: Cluster Mode Enabled

---

## **Amazon DynamoDB**

### **Capacity Modes**
- **Provisioned**: Predictable workloads, capacity planning
- **On-demand**: Unpredictable workloads, pay per request

### **DAX (DynamoDB Accelerator)**
- **In-memory Cache**: Microsecond latency
- **Compatibility**: Existing API compatible
- **TTL**: 5 minutes default

### **Streams & Global Tables**
- **Stream Processing**: Real-time change capture
- **Global Tables**: Multi-region, active-active
- **Use Cases**: Aggregations, cross-region replication

### **TTL (Time to Live)**
- **Automatic Expiration**: Based on timestamp
- **Use Cases**: Session data, regulatory compliance
- **Process**: Scan and delete expired items

### **Backups & Export**
- **PITR**: 35-day continuous backups
- **On-demand**: Full backups for retention
- **S3 Export**: Analytics, ETL processing

---

## **AWS DMS (Database Migration Service)**

### **Migration Types**
- **Homogeneous**: Same engine (Oracle → Oracle)
- **Heterogeneous**: Different engines (SQL Server → Aurora)
- **CDC**: Continuous Data Replication

### **Schema Conversion Tool (SCT)**
- **Engine Conversion**: Different database engines
- **Not Required**: Same engine migrations
- **Compute Intensive**: Requires powerful instances

### **Monitoring**
- **Task Status**: Creating, Running, Stopped
- **Table State**: Progress of individual tables
- **CloudWatch Metrics**: CPU, memory, replication metrics

---

## **Amazon S3 Replication**

### **Types**
- **CRR**: Cross-Region Replication
- **SRR**: Same-Region Replication

### **Requirements & Behavior**
- **Versioning**: Required on source and destination
- **Existing Objects**: Use S3 Batch Replication
- **DELETE Operations**: Optional marker replication
- **No Chaining**: Bucket 1 → Bucket 2 → Bucket 3 (Bucket 1 not → Bucket 3)

---

## **AWS Storage Gateway**

### **File Gateway - Cache Refresh**
- **Problem**: Direct S3 uploads not immediately visible
- **Manual**: `RefreshCache` API call
- **Automated**: Auto-refresh feature (recommended)

---

## **Auto Scaling Groups - Advanced**

### **Scaling Policies**
| Policy Type | Use Case | Configuration |
|-------------|----------|---------------|
| **Target Tracking** | Maintain metric at target | CPU at 40% |
| **Step Scaling** | CloudWatch alarm-based | Add 2 if CPU > 70% |
| **Scheduled** | Predictable patterns | Min=10 at 5pm Fridays |
| **Predictive** | ML-based forecasting | Forecasted load |

### **Good Scaling Metrics**
- `CPUUtilization`
- `RequestCountPerTarget` (ALB)
- Network In/Out
- Custom metrics

### **Lifecycle Hooks**
- **Pending State**: Before instance in service
- **Terminating State**: Before instance termination
- **Use Cases**: Log extraction, cleanup, health checks
- **Integration**: EventBridge, SNS, SQS

### **Warm Pools**
- **Purpose**: Reduce scale-out latency
- **States**: Running, Stopped, Hibernated
- **Cost Optimization**: Only pay for EBS in stopped state
- **Instance Reuse**: Return instances to pool on scale-in

### **Termination Policies**
- **Default**: Oldest Launch Template, closest to billing hour
- **Custom**: Lambda-backed policies
- **Strategies**: OldestInstance, NewestInstance, ClosestToNextInstanceHour

---

## **ELB Advanced Features**

### **Listener Rules**
- **Processing Order**: Sequential with default rule
- **Conditions**: host-header, path-pattern, source-ip, http-header, query-string
- **Actions**: forward, redirect, fixed-response

### **Target Group Weighting**
- **Traffic Distribution**: Control percentages
- **Use Cases**: Blue/green deployments, canary testing
- **Configuration**: Weight values per target group

### **DualStack Networking**
- **IPv4 & IPv6**: Client compatibility
- **Automatic Conversion**: IPv6 to IPv4 if needed
- **Requirements**: AZ must support both protocols

---

## **AWS Application Auto Scaling**
- **Unified Scaling**: Multiple services from single interface
- **Resource Discovery**: CloudFormation stacks, tags, ASGs
- **Scaling Plans**: Automated capacity management
- **Supported Services**: DynamoDB, ECS, Lambda, Aurora, and many more

---

**These notes complete the coverage up to API Gateway Caching and beyond. Good luck with your exam preparation! 🚀**
