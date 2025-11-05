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

Sure! Here’s a **simple, clean, and exam-focused summary** of **Amazon ECS, ECR, and EKS**—along with **DevOps certification-style questions and answers** to help you revise and prepare confidently.

---

# ✅ **Amazon ECS – Elastic Container Service**

### **What is ECS?**

A fully managed service to run containers (like Docker) on AWS. You don’t need to set up your own Kubernetes cluster.

---

### **Launch Types**

| Feature              | **EC2 Launch Type**   | **Fargate Launch Type**         |
| -------------------- | --------------------- | ------------------------------- |
| Who manages servers? | You (EC2 instances)   | AWS (serverless)                |
| Scaling              | Auto Scaling Groups   | Auto scales tasks automatically |
| Payment              | Pay for EC2 instances | Pay per CPU & RAM used by tasks |
| Maintenance          | OS patching required  | No maintenance (AWS handles)    |

---

### **IAM Roles in ECS**

| Role                  | Purpose                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------- |
| **EC2 Instance Role** | Used when using EC2 instances → allows ECS Agent to send logs, pull images from ECR, access SSM/Secrets Manager |
| **Task Role**         | Specific permissions for each task (per application) → secure access to only required AWS services              |

---

### **Load Balancers with ECS**

* **ALB (Application Load Balancer)** → Best & most common.
* **NLB (Network Load Balancer)** → High performance, TCP traffic, PrivateLink.
* **Classic Load Balancer** → Old & not recommended (no Fargate support).

---

### **Storage in ECS**

* **Uses Amazon EFS (Elastic File System)** for shared storage.
* Works with **EC2 and Fargate**.
* **Serverless Storage** = Fargate + EFS.

---

### **Auto Scaling**

| Level                    | What scales?                                                                     |
| ------------------------ | -------------------------------------------------------------------------------- |
| **Service Auto Scaling** | Increases/decreases **tasks** in a service based on CPU, memory, or ALB requests |
| **EC2 Auto Scaling**     | Adds/removes **EC2 instances** in the ECS cluster                                |

---

### **Event-Driven ECS**

Events (like S3 upload or Schedule) → trigger ECS task → process → store in S3/DynamoDB.

---

### **Logging**

| Method            | Where?                                        |
| ----------------- | --------------------------------------------- |
| `awslogs` driver  | Sends logs to CloudWatch                      |
| Sidecar container | Sends logs to a separate container/log system |
| Fargate           | Needs **Task Execution Role**                 |

---

---

# ✅ **Amazon ECR – Elastic Container Registry**

### **What is ECR?**

Private Docker image storage like Docker Hub but secure and AWS-managed.

### **Key Features**

✔ Stores Docker/container images
✔ Image **versioning and tagging**
✔ **Vulnerability scanning**
✔ Integrated with **ECS, EKS, Lambda**

---

### **Lifecycle Policies**

* Automatically delete **old or unused images**
* Based on **age or number of images**
* Cleanup happens **within 24 hours**

---

### **CI/CD Example**

**CodePipeline Workflow:**
`CodeCommit → CodeBuild → Push image to ECR → Deploy to ECS/EKS/Fargate`

---

---

# ✅ **Amazon EKS – Elastic Kubernetes Service**

### **What is EKS?**

AWS-managed Kubernetes service. You use Kubernetes, but AWS manages control plane (API server, etcd).

---

### **Node Types**

| Type                    | Who Manages Nodes?                                    |
| ----------------------- | ----------------------------------------------------- |
| **Managed Node Groups** | AWS manages EC2 nodes, scaling, patching              |
| **Self-Managed Nodes**  | You create & manage your own EC2 nodes (more control) |
| **Fargate**             | Fully serverless pod execution — no EC2 nodes         |

---

### **Storage in EKS**

| Storage Type | Use Case                                                                     |
| ------------ | ---------------------------------------------------------------------------- |
| **EBS**      | Block storage for individual pods                                            |
| **EFS**      | Shared storage (multi-pod, multi-AZ)                                         |
| **FSx**      | High-performance storage (e.g., Lustre for ML, ONTAP for Windows/Linux apps) |

---

### **Logging in EKS**

✔ Control Plane Logs (API, Audit, Auth, Scheduler) → CloudWatch
✔ Worker Node logs (pod/container logs) → via **Fluent Bit/Fluentd**
✔ **Container Insights** for metrics and dashboards

---

---

# 🎯 **DevOps Certification – Expected Questions & Sample Answers**

### ✅ ECS Sample Questions

**Q1. What’s the difference between ECS EC2 and Fargate launch type?**
**Ans:** In EC2, you manage servers (EC2 instances). In Fargate, AWS manages infrastructure and you pay only for CPU and RAM used by tasks.

**Q2. Why use ECS Task Role?**
**Ans:** To give specific AWS permissions only to that particular task — secure and least privilege.

---

### ✅ ECR Sample Questions

**Q1. What is the purpose of ECR Lifecycle Policy?**
**Ans:** To delete old/unused images automatically based on age or image count.

**Q2. How does ECR integrate with Jenkins or CodePipeline?**
**Ans:** Build in CodeBuild/Jenkins → Push Docker image to ECR → Deploy using ECS/EKS.

---

### ✅ EKS Sample Questions

**Q1. How is EKS different from ECS?**
**Ans:** EKS uses Kubernetes; ECS is AWS-native and doesn’t use Kubernetes.

**Q2. Which storage types are used in EKS for persistent volumes?**
**Ans:** EBS, EFS, FSx. StorageClass is used to define which one to use.

---

---
Sure! I’ll add a clear and exam-friendly section on **AWS Fargate** and also connect it to ECS and EKS for full understanding.

---

# ✅ **AWS Fargate – Simplified Explanation & Certification Notes**

### **🔹 What is Fargate?**

AWS Fargate is a **serverless compute engine for containers**.
You don’t need to create or manage EC2 servers — just define:
✔ **Container image**
✔ **CPU & RAM required**
✔ **Task/Pod definition**
…and Fargate runs it for you automatically.

---

### **🔹 Where is Fargate Used?**

| Service        | Does Fargate Work? | Description                                                |
| -------------- | ------------------ | ---------------------------------------------------------- |
| **Amazon ECS** | ✅ Yes              | You can run ECS tasks using Fargate without EC2 cluster    |
| **Amazon EKS** | ✅ Yes              | Kubernetes pods can run on Fargate instead of worker nodes |
| **Standalone** | ❌ No               | Must work under ECS or EKS                                 |

---

### **🔹 Fargate vs EC2 (Simple Comparison)**

| Feature           | **EC2 Launch Type**                        | **Fargate Launch Type**                       |
| ----------------- | ------------------------------------------ | --------------------------------------------- |
| Server Management | You manage EC2 VMs                         | No servers to manage (serverless)             |
| Scaling           | Manual or Auto Scaling Group               | Auto scales per task/pod                      |
| OS Patching       | Required                                   | Not required                                  |
| Cost              | Pay for full EC2 instance (even when idle) | Pay only for vCPU + RAM your container uses   |
| Security          | Bigger surface area (VM)                   | Smaller attack surface (no SSH, no VM access) |

---

### **🔹 Benefits of AWS Fargate**

✅ No need to launch or patch EC2 instances
✅ You only pay when your tasks/pods are running
✅ Built-in isolation for each task (more secure)
✅ Works with **EFS** for persistent shared storage
✅ Integrated with IAM roles and CloudWatch logging
✅ Excellent for **microservices, event-based apps, batch jobs**

---

### **🔹 Limitations of Fargate (Good to know for Exam)**

| Limitation                        | Explanation                                          |
| --------------------------------- | ---------------------------------------------------- |
| No SSH access                     | You cannot log in to the underlying server           |
| Limited control                   | Cannot customize OS or install system-level packages |
| No GPU support (earlier)          | Now partially supported but limited                  |
| Higher cost for long-running apps | For continuous high usage, EC2 may be cheaper        |
| Requires Task Execution IAM Role  | Needed for pulling images, sending logs, etc.        |

---

### **🔹 Fargate in ECS – How It Works**

1. Create **Task Definition** (Docker image + CPU/RAM + task role).
2. Select **Fargate Launch Type**.
3. Attach Load Balancer (optional).
4. ECS runs the container serverlessly.

---

### **🔹 Fargate in EKS – How It Works**

1. You define a **Pod + Namespace + Fargate Profile** in Kubernetes.
2. When pods in that namespace are created → automatically scheduled on Fargate.
3. No worker node provisioning required.

---

### **🔹 DevOps Exam Questions on Fargate (with Answers)**

**Q1: What is the key difference between ECS EC2 and ECS Fargate?**
**Answer:** In EC2, you manage servers and infrastructure. In Fargate, AWS manages everything — you just run tasks or containers.

---

**Q2: Does Fargate support persistent storage? If yes, how?**
**Answer:** Yes. Fargate supports **EFS (Elastic File System)**, allowing containers across multiple AZs to share the same data.

---

**Q3: Why is a Task Execution Role required in Fargate?**
**Answer:** It allows Fargate to pull container images from ECR, send logs to CloudWatch, and access Secrets Manager/SSM.

---

**Q4: Can Fargate be used in Kubernetes (EKS)?**
**Answer:** Yes. In EKS, Fargate allows pods to run without EC2 worker nodes using Fargate Profiles.

---




Sure! Here are **simple, clear, exam-friendly notes on Amazon Kinesis**, just like the ECS/EKS format you liked — plus extra info, comparisons, and certification-style Q&A.

---

# ✅ **Amazon Kinesis – Real-Time Data Streaming on AWS**

Amazon Kinesis is used to **collect, process, and analyze real-time streaming data** like logs, clickstreams, IoT data, stock market, gaming, etc.

It has 3 main services:

| Service                                           | Purpose                                                            |
| ------------------------------------------------- | ------------------------------------------------------------------ |
| **Kinesis Data Streams (KDS)**                    | Collect and stream real-time data                                  |
| **Kinesis Data Firehose**                         | Load streaming data into S3, Redshift, etc. (no servers to manage) |
| **Kinesis Data Analytics (Managed Apache Flink)** | Real-time analytics and processing using SQL, Java, Scala          |

---

## 🚀 **1. Kinesis Data Streams (KDS)**

### 🔹 Overview

* Collects **real-time data** in small batches (milliseconds).
* Stores data temporarily so consumers can process it.
* Data producers → Stream → Shards → Consumers.

### 🔹 Key Features

| Feature            | Details                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| **Retention**      | Default 24 hours, can increase to **365 days**                                         |
| **Replay data**    | Yes — can reprocess data from history                                                  |
| **Ordering**       | Maintains order within **same partition key/shard**                                    |
| **Scaling**        | Add more **shards** to increase throughput                                             |
| **Capacity Modes** | **Provisioned:** You choose shard count<br>**On-Demand:** Auto scales based on traffic |

### 🔹 Shard Capacity

| Per Shard | Limit                         |
| --------- | ----------------------------- |
| Writes    | 1 MB/sec or 1,000 records/sec |
| Reads     | 2 MB/sec                      |

### 🔹 Consumers

* **Enhanced Fan-Out** (low latency ~70ms)
* **Standard Consumer** (shared throughput)

---

## 🔥 **2. Kinesis Data Firehose**

### 🔹 What It Does:

Fully managed service to **deliver streaming data to destinations** like:

* **S3**
* **Redshift**
* **OpenSearch (Elasticsearch)**
* **HTTP / 3rd party services**

### 🔹 Key Features

| Feature             | Explanation                                         |
| ------------------- | --------------------------------------------------- |
| **No servers**      | AWS manages everything                              |
| **Transforms data** | Can use **AWS Lambda** to convert/clean data        |
| **Buffering**       | Delivers data in batches, based on **time or size** |
| **Near Real-Time**  | Delay of 1–60 seconds                               |
| **Auto-scaling**    | No need to manage shards                            |

### 🔹 Comparison with Data Streams

| Feature       | Data Streams                | Firehose                       |
| ------------- | --------------------------- | ------------------------------ |
| Management    | Manual (you manage scaling) | Fully managed                  |
| Data Storage  | Temporary only              | Delivers and stores            |
| Replay Events | ✅ Yes                       | ❌ No (no reprocess)            |
| Latency       | Milliseconds                | Seconds                        |
| Use Case      | Build custom streaming apps | Simple delivery to S3/Redshift |

---

## ⚙️ **3. Kinesis Data Analytics (Managed Apache Flink)**

### 🔹 What It Is:

A managed service to **analyze and process streaming data** from Kinesis or Kafka using:

* **SQL**
* **Java / Scala with Apache Flink**

### 🔹 Key Features

| Feature                        | Explanation                                  |
| ------------------------------ | -------------------------------------------- |
| **Real-time analytics**        | Filter, aggregate, window functions          |
| **Languages**                  | SQL, Java, Scala                             |
| **Fully managed**              | AWS handles infrastructure, scaling          |
| **Auto-scaling & checkpoints** | Saves state automatically                    |
| **Outputs to**                 | S3, Kinesis, Firehose, Lambda, Elasticsearch |

### 📌 Use Cases

✔ Fraud detection
✔ Real-time dashboards
✔ IoT sensor analytics
✔ Live leaderboards (gaming/stock data)

---

## 🎯 **✅ DevOps Certification – Practice Questions & Answers**

---

**Q1. What is the difference between Kinesis Data Streams and Firehose?**
**Answer:**

* Data Streams → Real-time, manual scaling, supports replay, developers process data.
* Firehose → Fully managed, auto-scales, delivers to S3/Redshift, no data replay.

---

**Q2. How do you increase throughput in Kinesis Data Streams?**
**Answer:**
Increase the number of **shards** (shard splitting), or use **on-demand mode**.

---

**Q3. Can Kinesis reprocess historical data?**
**Answer:**
Yes, **Kinesis Data Streams** can replay data for up to 365 days.
Firehose cannot replay.

---

**Q4. What is Enhanced Fan-Out?**
**Answer:**
A feature in Data Streams that lets multiple consumers get data in parallel with **70ms latency**, without sharing read throughput.

---

**Q5. Can Kinesis Firehose transform data before delivery?**
**Answer:**
Yes, using **AWS Lambda** functions for real-time transformations.

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

Sure! Here are your **exam-ready, simplified, and complete notes** for **RDS, Aurora, ElastiCache, DynamoDB, and AWS DMS**—in the same clean format as before.

---

# ✅ **Amazon RDS & Amazon Aurora**

### 🎯 **What is RDS?**

Managed relational database service (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server).

### 🎯 **What is Aurora?**

AWS-built, MySQL/PostgreSQL-compatible database. Faster, more scalable, fault-tolerant.

---

### 🔹 **Read Replicas (RDS & Aurora)**

| Feature      | Details                                       |
| ------------ | --------------------------------------------- |
| Purpose      | Scale **read workloads** (reports, analytics) |
| Replicas     | Up to **5** in RDS, **15** in Aurora          |
| Replication  | **Asynchronous** → Eventually Consistent      |
| Cross-Region | Supported but extra network cost              |
| Failover?    | ❌ No automatic failover (only for reads)      |

---

### 🔹 **Multi-AZ Deployment (High Availability)**

| Feature     | Details                                       |
| ----------- | --------------------------------------------- |
| Replication | **Synchronous** to standby in another AZ      |
| Purpose     | **Disaster Recovery / Failover**, not scaling |
| Failover    | Auto-detect & auto-promote standby            |
| Endpoint    | Same database **DNS name** (no app change)    |
| Data Loss   | Zero (sync replication)                       |

---

### 🔹 **Aurora Global Database**

| Feature      | Details                               |
| ------------ | ------------------------------------- |
| Regions      | 1 Primary + up to 5 Secondary regions |
| Lag          | Less than **1 second**                |
| DR (RTO)     | < **1 minute failover**               |
| Read Scaling | **16 replicas per region**            |
| Use Case     | Global apps, low-latency reads, DR    |

---

# ✅ **Amazon ElastiCache**

### 🎯 **What is it?**

In-memory cache for fast data access → improves performance for apps, databases.

---

### 🔹 **Redis vs Memcached**

| Feature         | **Redis**                         | **Memcached**    |
| --------------- | --------------------------------- | ---------------- |
| Replication     | ✅ Multi-AZ, replicas              | ❌ No replication |
| Persistence     | ✅ Snapshot/AOF                    | ❌ No persistence |
| Data Types      | Strings, Sets, Lists, Sorted Sets | Only strings     |
| Architecture    | Single-threaded                   | Multi-threaded   |
| Pub/Sub Support | ✅ Yes                             | ❌ No             |

---

### 🔹 **Cluster Modes (Redis)**

| Mode                        | Structure                         | Nodes                 |
| --------------------------- | --------------------------------- | --------------------- |
| **Disabled (Single Shard)** | 1 Primary + up to 5 Read Replicas | Max 6 per shard       |
| **Enabled (Cluster Mode)**  | Multiple Shards                   | Up to 500 nodes total |
| **Auto Scaling**            | ✅ Only in Cluster Mode Enabled    |                       |

---

### 🔹 **Endpoints**

| Type                       | Purpose                                 |
| -------------------------- | --------------------------------------- |
| **Primary Endpoint**       | Write operations                        |
| **Reader Endpoint**        | Load-balanced read requests             |
| **Configuration Endpoint** | Used for Cluster Mode to discover nodes |

---

# ✅ **Amazon DynamoDB**

### 🎯 **What is DynamoDB?**

Fully managed NoSQL database, key-value & document-based, serverless, ultra-fast.

---

### 🔹 **Capacity Modes**

| Mode            | Use Case                                                      |
| --------------- | ------------------------------------------------------------- |
| **Provisioned** | Predictable traffic, pre-set RCU/WCU                          |
| **On-demand**   | Unpredictable traffic, pay-per-request (scales automatically) |

---

### 🔹 **DAX (DynamoDB Accelerator)**

| Feature        | Details                       |
| -------------- | ----------------------------- |
| Purpose        | In-memory cache for DynamoDB  |
| Latency        | Microseconds                  |
| API Compatible | Yes (no code change required) |
| TTL            | Default 5 minutes             |

---

### 🔹 **Streams & Global Tables**

| Feature           | Purpose                                    |
| ----------------- | ------------------------------------------ |
| **Streams**       | Captures real-time data change events      |
| **Uses**          | Triggers Lambda, Replication, Auditing     |
| **Global Tables** | Multi-region, active-active database       |
| **Use Case**      | Low-latency global apps, disaster recovery |

---

### 🔹 **TTL – Time to Live**

| Feature   | Details                                        |
| --------- | ---------------------------------------------- |
| Purpose   | Auto-delete expired items (based on timestamp) |
| Use Cases | Session data, caching, GDPR compliance         |
| Process   | Background task – removes expired data         |

---

### 🔹 **Backup & Restore**

| Type                              | Details                                 |
| --------------------------------- | --------------------------------------- |
| **PITR (Point-in-Time Recovery)** | Continuous backups for last **35 days** |
| **On-demand Backup**              | Full backup anytime                     |
| **Export to S3**                  | For analytics / ETL                     |

---

# ✅ **AWS DMS (Database Migration Service)**

### 🎯 **Purpose** – Migrate databases to AWS with minimal downtime.

---

### 🔹 **Migration Types**

| Type                          | Example                                            |
| ----------------------------- | -------------------------------------------------- |
| **Homogeneous**               | Oracle → Oracle / MySQL → MySQL                    |
| **Heterogeneous**             | SQL Server → Aurora, Oracle → PostgreSQL           |
| **CDC (Change Data Capture)** | Continues to replicate new changes after full load |

---

### 🔹 **Schema Conversion Tool (SCT)**

| Feature         | Purpose                                                      |
| --------------- | ------------------------------------------------------------ |
| Converts schema | When migrating to a different engine (e.g., Oracle → Aurora) |
| Not needed      | For same engine migrations                                   |
| Limitation      | Compute-intensive, needs strong instance                     |

---

### 🔹 **Monitoring DMS**

| Method                 | Details                               |
| ---------------------- | ------------------------------------- |
| **Task Status**        | Creating, Running, Stopped            |
| **Table State**        | Shows migration progress per table    |
| **CloudWatch Metrics** | CPU, Memory, Latency, Replication Lag |


Absolutely! Here are simplified, exam-focused, and revision-friendly notes for:

✅ **Amazon S3 Replication**
✅ **AWS Storage Gateway**
✅ **Auto Scaling Groups – Advanced**
✅ **ELB (Elastic Load Balancer) – Advanced Features**
✅ **AWS Application Auto Scaling**

---

# ✅ **Amazon S3 Replication**

### 🔹 Types of Replication

| Type                               | Description                              |
| ---------------------------------- | ---------------------------------------- |
| **CRR (Cross-Region Replication)** | Replicates objects to another AWS Region |
| **SRR (Same-Region Replication)**  | Replicates within the same region        |

---

### 🔹 Key Requirements & Behaviors

| Feature              | Explanation                                                                        |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Versioning**       | Must be enabled on **both source and destination buckets**                         |
| **New Objects Only** | Existing files are **not replicated automatically** – use **S3 Batch Replication** |
| **Deletes Handling** | You can choose to **replicate delete markers or not**                              |
| **No Chaining**      | If A → B is enabled and B → C is enabled, A **won’t replicate to C**               |
| **IAM Role Needed**  | For S3 to perform replication on your behalf                                       |

---

# ✅ **AWS Storage Gateway – File Gateway**

### 🔹 Cache Refresh (Common Exam Question)

| Situation                                       | Behavior                                                       |
| ----------------------------------------------- | -------------------------------------------------------------- |
| Files uploaded directly to S3 (outside Gateway) | Not visible to on-prem system immediately                      |
| **Manual Fix**                                  | Call `RefreshCache` API                                        |
| **Automatic Fix**                               | Enable **Auto-Refresh** in File Gateway settings (recommended) |

---

# ✅ **Auto Scaling Groups (Advanced Topics)**

### 🔹 Types of Scaling Policies

| Policy Type            | Works For                            | Example                          |
| ---------------------- | ------------------------------------ | -------------------------------- |
| **Target Tracking**    | Maintain a target metric             | Keep CPU at 40%                  |
| **Step Scaling**       | Based on CloudWatch alarm thresholds | Add 2 instances if CPU > 70%     |
| **Scheduled Scaling**  | Predictable traffic                  | Increase to 10 instances at 5 PM |
| **Predictive Scaling** | Machine Learning forecast            | Scale before traffic spikes      |

---

### 🔹 Good Metrics for Scaling

✔ `CPUUtilization`
✔ `RequestCountPerTarget` (from ALB)
✔ `NetworkIn` / `NetworkOut`
✔ **Custom metrics** (via CloudWatch)

---

### 🔹 Lifecycle Hooks (Interview-Favorite)

| Lifecycle Stage              | Purpose                                                               |
| ---------------------------- | --------------------------------------------------------------------- |
| **Pending → InService**      | Hold before launching fully (e.g., install software, run scripts)     |
| **Terminating → Terminated** | Hold before termination (e.g., extract logs, deregister from systems) |
| **Integration**              | Works with **SNS, SQS, EventBridge, Lambda**                          |

---

### 🔹 Warm Pools

| Feature        | Details                                                        |
| -------------- | -------------------------------------------------------------- |
| **Purpose**    | Reduce time to launch new instances (pre-warmed EC2 instances) |
| **States**     | Running, Stopped (only EBS charged), Hibernated                |
| **Efficiency** | Instances reused when scaling in                               |

---

### 🔹 Termination Policies (Which Instance to Delete First?)

| Policy                              | Explanation                              |
| ----------------------------------- | ---------------------------------------- |
| **Default**                         | Oldest instance, closest to billing hour |
| **OldestInstance / NewestInstance** | Based on launch time                     |
| **ClosestToNextBillingHour**        | Saves cost                               |
| **Custom**                          | Use **Lambda-backed policy**             |

---

# ✅ **ELB (Elastic Load Balancer) – Advanced Features**

### 🔹 Listener Rules (Processed Top → Bottom)

| Condition Type   | Examples                     |
| ---------------- | ---------------------------- |
| **host-header**  | `api.example.com`            |
| **path-pattern** | `/images/*`, `/admin/*`      |
| **source-ip**    | Only allow company IP ranges |
| **http-header**  | Check user-agent, language   |
| **query-string** | `/search?category=books`     |

**Actions:**
✔ `forward to target group`
✔ `redirect (HTTP → HTTPS)`
✔ `fixed-response (403, 404, custom page)`

---

### 🔹 Target Group Weighting

| Use Case                  | Example                                                 |
| ------------------------- | ------------------------------------------------------- |
| **Blue/Green Deployment** | Send 90% traffic to old version, 10% to new             |
| **Canary Testing**        | Gradually shift users                                   |
| **How?**                  | Assign weight to each target group (e.g., 80/20, 50/50) |

---

### 🔹 DualStack Networking

| Feature                       | Details                                          |
| ----------------------------- | ------------------------------------------------ |
| **Supports both IPv4 & IPv6** | Load balancer has dual DNS                       |
| **Auto convert**              | Converts IPv6 requests to IPv4 backend if needed |
| **Requirement**               | AZ & subnet must support IPv6                    |

---

# ✅ **AWS Application Auto Scaling**

### 🔹 What It Does?

Scales resources **other than EC2**, such as:
✔ DynamoDB
✔ ECS Tasks
✔ Lambda provisioned concurrency
✔ Aurora replicas
✔ SQS queue length
✔ EMR clusters, etc.

---

### 🔹 Features

| Feature                         | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| **Unified Scaling Console/API** | Manage scaling for multiple services in one place      |
| **Resource Discovery**          | Can detect resources using tags or CloudFormation      |
| **Scaling Plans**               | Automatically handle provisioning + predictive scaling |
| **Integration**                 | Works with CloudWatch metrics + IAM                    |

