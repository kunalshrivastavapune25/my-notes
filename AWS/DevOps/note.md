Absolutely! Here's a **simple, structured and easy-to-understand version of Domain 1 & Domain 2 notes for SDLC Automation and CloudFormation/IaC** — perfect for revision or interview prep.

---

# ✅ **Domain 1: SDLC Automation (CI/CD & DevOps Tools)**

### 🎯 **Goal of CI/CD**

Automate the process of **writing → building → testing → deploying** code so that deployments are:
✔ Faster
✔ Less error-prone
✔ Consistent across Dev, Test, Staging, Production

---

### 🚀 **AWS DevOps Tools Overview**

| Service          | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **CodeCommit**   | Private Git repository (similar to GitHub).   |
| **CodeBuild**    | Compiles & tests code (build server).         |
| **CodeDeploy**   | Deploys apps to EC2, Lambda, ECS, or on-prem. |
| **CodePipeline** | Connects everything – automated pipeline.     |
| **CodeStar**     | Pre-configured DevOps project setup.          |
| **CodeArtifact** | Private package repository (npm, Maven, pip). |
| **CodeGuru**     | AI-based code reviews + performance profiler. |

---

### 🔁 **CI vs CD (Simple Explanation)**

| Concept                         | Meaning                                                              | Example                          |
| ------------------------------- | -------------------------------------------------------------------- | -------------------------------- |
| **CI (Continuous Integration)** | Developers frequently push code → code automatically builds & tests. | Code push to Git triggers build. |
| **CD (Continuous Delivery)**    | CI + code is automatically deployed to test/staging environments.    | After tests → deploy to staging. |
| **Continuous Deployment**       | Even production deployment is automated (no human approval).         | Code → Prod without approval.    |

---

### 💻 **AWS CodeCommit**

✅ Fully managed Git repository service by AWS.
✅ Encrypted, IAM-secured, version-controlled.
⚠️ **Important:** AWS announced deprecation for new users after July 2024 (but still in exam).

**Features:**

* Cross-region replication
* Branch security (allow only Leads to push to `master`)
* Pull request approvals

---

### 🔗 **AWS CodePipeline (CI/CD Workflow Automator)**

Visual pipeline for automating code flow:

```
Source (CodeCommit/GitHub) → Build (CodeBuild) → Test → Deploy → Prod
```

✅ Can include **manual approval steps** (via SNS email)
✅ Artifacts stored in **S3** between stages
✅ Can trigger **Lambda, Step Functions, CloudFormation**

**Start triggers:**

| Method      | When to Use                        |
| ----------- | ---------------------------------- |
| EventBridge | Real-time triggering on commit     |
| Webhook     | External Git providers like GitHub |
| Polling     | When no event system is available  |

---

### 🏗️ **AWS CodeBuild**

* Fully managed build/test service.
* Uses `buildspec.yml` file to define build commands.

**buildspec.yml sample:**

```yaml
version: 0.2
phases:
  install:
    commands:
      - npm install
  build:
    commands:
      - npm run test
artifacts:
  files:
    - '**/*'
```

---

### 🚚 **AWS CodeDeploy**

| Deployment Type | Used For                | Works On         | Example                           |
| --------------- | ----------------------- | ---------------- | --------------------------------- |
| In-Place        | Update existing servers | EC2/On-Prem      | Replace code on same instance     |
| Blue-Green      | Swap new environment    | EC2, ECS, Lambda | Deploy new version, shift traffic |

**Hooks in appspec.yml (EC2 example):**

```
BeforeInstall → Install scripts → ApplicationStart → ValidateService
```

---

### 📦 **AWS CodeArtifact**

* Like **npm/maven private repo** inside AWS
* Stores and shares packages across teams
* Can pull from public repositories like npmjs/Maven Central

---

### 🤖 **AWS CodeGuru**

* **Reviewer:** AI reviews Java/Python pull requests
* **Profiler:** Detects performance bottlenecks in live apps
* Detects **hardcoded secrets**, too!

---

# ✅ **Domain 2: Configuration Management & IaC**

## 🏗️ **AWS CloudFormation (IaC – Infrastructure as Code)**

### 💡 **Why?**

Instead of manually creating AWS resources → Write code (YAML/JSON) → CloudFormation builds everything.

✔ Consistent
✔ Version-controlled
✔ Automates infrastructure

---

### 📄 **CloudFormation Template Components**

| Section        | Purpose                                      |
| -------------- | -------------------------------------------- |
| **Parameters** | Inputs → like username, VPC ID               |
| **Mappings**   | Fixed values per region (e.g., AMI ID)       |
| **Resources**  | ✅ Required – actual AWS components (EC2, S3) |
| **Outputs**    | Export values (DB Endpoint, ARN)             |
| **Conditions** | Create resources based on logic              |
| **Metadata**   | Extra config for tools like cfn-init         |

---

### 🛠️ **Basic Template Example**

```yaml
Resources:
  MyBucket:
    Type: AWS::S3::Bucket

Outputs:
  BucketName:
    Value: !Ref MyBucket
```

---

### 🔁 **CloudFormation Advanced Features**

| Feature                   | Use Case                                       |
| ------------------------- | ---------------------------------------------- |
| **Change Sets**           | Preview changes before applying                |
| **Stack Policies**        | Protect critical resources from updates        |
| **Deletion Policy**       | Keep or snapshot resources when deleting stack |
| **Nested Stacks**         | Reuse templates inside templates               |
| **StackSets**             | Deploy same stack to multiple accounts/regions |
| **Dynamic References**    | Pull secrets from SSM/Secrets Manager          |
| **cfn-init & cfn-signal** | Configure EC2 internally before “complete”     |

---

### 🛑 **DeletionPolicy Types**

| Policy     | What Happens?                           |
| ---------- | --------------------------------------- |
| `Delete`   | Resource is removed (default)           |
| `Retain`   | Resource is not deleted                 |
| `Snapshot` | EBS/RDS create snapshot before deletion |

---

### 💬 **Need More Help?**

I can also provide:
✔ Diagram images
✔ Sample CloudFormation / CodePipeline / CodeBuild YAML
✔ Practice exam questions
✔ Flowcharts for CI/CD pipelines

---

Would you like me to continue with **Elastic Beanstalk vs CloudFormation vs CDK vs SAM comparison?** or **Next Domain (Handling artifacts, logging, monitoring)?**
