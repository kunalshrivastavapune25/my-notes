
Typical Enterprise workflows

<img width="1600" height="720" alt="image" src="https://github.com/user-attachments/assets/bc4f9bea-80ef-4b9a-802f-68bb824f57f8" />


CI/CD Orchestrators (choose ONE)
--------------------------------
Jenkins | GitHub Actions | CodePipeline

Infrastructure
--------------
Terraform / CloudFormation

Configuration
-------------
Ansible / Chef / Puppet

Deployment
----------
CodeDeploy / ECS / EKS / ArgoCD


GitHub Architecture

Developer
   |
   v
 GitHub Repo
   |
   v
+-----------------------------+
|    GitHub Actions Workflow  |
|     (CI/CD Orchestrator)    |
+-----------------------------+
            |
            | jobs & steps
            v
   ---------------------------------------
   |              |                      |
   v              v                      v
 Build/Test     Terraform             Ansible
 (Actions)      (IaC)             (Config & App)
     |              |                      |
     v              v                      v
 Artifacts     AWS Infrastructure      EC2 / EKS
 (ECR / S3)    - VPC                   Nodes
               - Subnets
               - EC2 / ASG
               - RDS

AWS CodePipeline Architecture

Developer
   |
   v
 GitHub / CodeCommit
   |
   v
+--------------------------+
|     AWS CodePipeline     |
|   (CI/CD Orchestrator)   |
+--------------------------+
            |
            | stages
            v
   -------------------------------------------------
   |              |                |               |
   v              v                v               v
 Source        Build           Provision          Deploy
               (CodeBuild)     (CodeBuild)        (CodeDeploy)
                  |               |                   |
                  v               v                   v
             Artifacts         Terraform           EC2 / ASG /
             (S3 / ECR)        (IaC)               ECS / Lambda
                                   |
                                   v
                          AWS Infrastructure
                          - VPC
                          - Subnets
                          - ALB
                          - EC2 / ASG
                          - RDS


Developer
   |
   v
 GitHub / GitLab
   |
   v
+------------------------+
|        Jenkins         |
|   (CI/CD Orchestrator) |
+------------------------+
            |
            | Jenkinsfile stages
            v
   ----------------------------
   |          |               |
   v          v               v
 Build/Test  Terraform       Ansible
 (Maven,    (Infra IaC)   (Config & App)
  npm)          |               |
                v               v
        AWS Infrastructure   EC2 / EKS Nodes
        - VPC                - Install packages
        - Subnets            - App deployment
        - EC2 / EKS          - Config management
        - RDS

| Feature     | CloudFormation | Terraform   | Ansible     | Chef        | Puppet      |
| ----------- | -------------- | ----------- | ----------- | ----------- | ----------- |
| Type        | IaC            | IaC         | Config Mgmt | Config Mgmt | Config Mgmt |
| Cloud       | AWS only       | Multi-cloud | Any         | Any         | Any         |
| Language    | YAML/JSON      | HCL         | YAML        | Ruby        | Puppet DSL  |
| Agent       | No             | No          | No          | Yes         | Yes         |
| State Mgmt  | AWS            | State file  | No          | Yes         | Yes         |
| Ease of Use | Medium         | Medium      | Easy        | Hard        | Medium      |
| Popularity  | High (AWS)     | Very High   | Very High   | Declining   | Declining   |




