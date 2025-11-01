# **AWS DevOps Pro - One-Page Cheat Sheet**

## **Domain 1: SDLC Automation**

### **CI/CD Core Services**
- **CodeCommit**: Private Git repos → *Deprecated July 2024, use GitHub*
- **CodePipeline**: Orchestrates pipeline stages (Source→Build→Test→Deploy)
- **CodeBuild**: Managed CI service → uses `buildspec.yml`
- **CodeDeploy**: Deploys to EC2, Lambda, ECS, on-premises

### **CodePipeline Key Points**
- **Artifacts**: Stored in S3, passed between stages
- **Manual Approval**: SNS integration for email approvals
- **Multi-Region**: Actions can span regions, requires S3 artifact stores in each region
- **CloudFormation Actions**: `CREATE_UPDATE`, `DELETE_ONLY` modes
- **Invoke Actions**: Lambda & Step Functions

### **CodeBuild Essentials**
- **buildspec.yml**:
  - `phases`: install, pre_build, build, post_build
  - `artifacts`: Output to S3
  - `cache`: Dependencies to S3 for speed
- **VPC Access**: Configure for internal resources (RDS, ELB)
- **Service Role**: Grants access to AWS resources
- **PR Validation**: Trigger builds on PR events

### **CodeDeploy Deployment Types**
| Platform | Supported Deployments | Key Requirements |
|----------|---------------------|------------------|
| **EC2/On-prem** | In-place, Blue/Green | CodeDeploy Agent |
| **Lambda** | Blue/Green only | Lambda alias, traffic shifting |
| **ECS** | Blue/Green only | Load Balancer required |

**AppSpec File**: `appspec.yml` defines deployment hooks
**Deployment Configs**: AllAtOnce, HalfAtATime, OneAtATime, Custom

### **Other Services**
- **CodeArtifact**: Package repository (npm, Maven, pip)
  - **Domains**: Container for repos, shared KMS key
  - **External Connection**: One per repo to public repos
- **CodeGuru**: 
  - **Reviewer**: Code analysis (Java/Python)
  - **Profiler**: Performance optimization
- **EC2 Image Builder**: Automated AMI creation pipeline
- **Amplify**: Full-stack web/mobile apps with CI/CD

---

## **Domain 2: Configuration Management & IaC**

### **CloudFormation Core**
- **Declarative** infrastructure provisioning
- **Template Components**: Resources (mandatory), Parameters, Mappings, Outputs, Conditions
- **Intrinsic Functions**: `!Ref`, `!GetAtt`, `!FindInMap`, `!ImportValue`

### **Advanced CF Features**
- **DeletionPolicy**: 
  - `Delete` (default), `Retain`, `Snapshot` (RDS, EBS)
- **Stack Policies**: JSON to protect resources during updates
- **Termination Protection**: Prevent accidental stack deletion
- **Custom Resources**: For unsupported resources → Lambda/SNS backed
- **Dynamic References**: `{{resolve:ssm:parameter}}`, `{{resolve:secretsmanager:secret}}`

### **EC2 Configuration**
- **cfn-init**: Processes `AWS::CloudFormation::Init` metadata (packages, files, commands)
- **cfn-signal**: Signals successful configuration → used with `CreationPolicy`/`WaitCondition`
- **User Data**: `Fn::Base64` for scripts

### **Stack Strategies**
- **Cross-Stack**: Export/Import values between independent stacks
- **Nested Stacks**: Reusable components within a parent stack
- **StackSets**: Deploy stacks across **multiple accounts & regions**

---

## **Key Security Patterns**
- **CodeCommit**: IAM policies for branch security
- **CodeBuild**: Service Role for AWS resource access
- **CodePipeline**: Service Role for deployment permissions
- **CodeArtifact**: Resource policies for cross-account sharing
- **CloudFormation**: Capabilities (`CAPABILITY_NAMED_IAM`) for IAM resources

---

## **Troubleshooting Tips**
- **CodeDeploy Agent**: Check if running, correct time sync, IAM permissions
- **CloudFormation Rollbacks**: Check logs, disable rollback for debugging
- **WaitCondition Timeouts**: Verify cfn-init & cfn-signal execution, internet access
- **Pipeline Failures**: Check IAM Service Role permissions, CloudWatch Events for state changes

---

**Good Luck! Remember: Hands-on experience trumps everything. You've got this! 🚀**