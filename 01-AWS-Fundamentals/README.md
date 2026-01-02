# Module 01: AWS Fundamentals

## Overview
Understanding AWS fundamentals is crucial for building a strong foundation for the Solutions Architect certification. This module covers the core concepts of AWS cloud computing.

## Learning Objectives
- Understand AWS Global Infrastructure
- Navigate AWS Management Console and CLI
- Understand AWS account management
- Learn the AWS Well-Architected Framework
- Understand AWS shared responsibility model

---

## 1. What is Cloud Computing?

### Cloud Computing Models
- **IaaS (Infrastructure as a Service)**: EC2, VPC
- **PaaS (Platform as a Service)**: Elastic Beanstalk, RDS
- **SaaS (Software as a Service)**: AWS applications like WorkMail

### Cloud Deployment Models
- **Public Cloud**: AWS, Azure, GCP
- **Private Cloud**: On-premises cloud infrastructure
- **Hybrid Cloud**: Combination of public and private

### Benefits of Cloud Computing
1. **Trade capital expense for variable expense**
2. **Benefit from massive economies of scale**
3. **Stop guessing capacity**
4. **Increase speed and agility**
5. **Stop spending money on running data centers**
6. **Go global in minutes**

---

## 2. AWS Global Infrastructure

### Regions
- **Geographic area** with multiple Availability Zones
- **25+ Regions** worldwide
- Each region is isolated for fault tolerance
- Choose regions based on:
  - Compliance requirements
  - Proximity to users (latency)
  - Available services
  - Pricing

### Availability Zones (AZs)
- **One or more discrete data centers**
- Each AZ has redundant power, networking, connectivity
- **Isolated from failures** in other AZs
- Connected with **high-bandwidth, low-latency networking**
- Typical region has **3-6 AZs**
- Design for multi-AZ deployment for high availability

### Edge Locations
- **400+ Points of Presence** (Edge Locations + Regional Edge Caches)
- Used by **CloudFront** (CDN)
- Used by **Route 53** (DNS)
- Lower latency for end users

### Local Zones
- Extension of AWS region
- Places compute, storage closer to users
- Used for **low-latency applications**

### Wavelength Zones
- AWS infrastructure embedded in telecom providers' 5G networks
- **Ultra-low latency** for mobile and connected devices

---

## 3. AWS Management Tools

### AWS Management Console
- Web-based interface
- Mobile app available
- Good for learning and simple tasks
- Not ideal for automation

### AWS CLI (Command Line Interface)
- Command-line access to AWS services
- Available for Windows, Mac, Linux
- Uses access keys (Access Key ID + Secret Access Key)
- Supports automation and scripting

```bash
# Configure AWS CLI
aws configure

# Example: List S3 buckets
aws s3 ls

# Example: Launch EC2 instance
aws ec2 run-instances --image-id ami-xxxxx --instance-type t2.micro
```

### AWS SDKs
- Software Development Kits for various programming languages
- Languages: Java, Python, Node.js, .NET, PHP, Ruby, Go, C++
- Embedded in application code

### AWS CloudShell
- Browser-based shell environment
- Pre-configured with AWS CLI
- Free service
- 1GB of persistent storage per region

### Infrastructure as Code (IaC)
- **AWS CloudFormation**: Native IaC service (JSON/YAML templates)
- **AWS CDK**: Define infrastructure using programming languages
- **Terraform**: Third-party IaC tool

---

## 4. AWS Well-Architected Framework

The AWS Well-Architected Framework helps cloud architects build secure, high-performing, resilient, and efficient infrastructure.

### Six Pillars

#### 1. Operational Excellence
- **Focus**: Run and monitor systems to deliver business value
- **Key Practices**:
  - Perform operations as code
  - Make frequent, small, reversible changes
  - Refine operations procedures frequently
  - Anticipate failure
  - Learn from operational failures

#### 2. Security
- **Focus**: Protect data, systems, and assets
- **Key Practices**:
  - Implement strong identity foundation
  - Enable traceability
  - Apply security at all layers
  - Automate security best practices
  - Protect data in transit and at rest
  - Keep people away from data
  - Prepare for security events

#### 3. Reliability
- **Focus**: Ensure workload performs its intended function correctly and consistently
- **Key Practices**:
  - Automatically recover from failure
  - Test recovery procedures
  - Scale horizontally
  - Stop guessing capacity
  - Manage change through automation

#### 4. Performance Efficiency
- **Focus**: Use computing resources efficiently
- **Key Practices**:
  - Democratize advanced technologies
  - Go global in minutes
  - Use serverless architectures
  - Experiment more often
  - Consider mechanical sympathy

#### 5. Cost Optimization
- **Focus**: Avoid unnecessary costs
- **Key Practices**:
  - Implement cloud financial management
  - Adopt a consumption model
  - Measure overall efficiency
  - Stop spending on undifferentiated heavy lifting
  - Analyze and attribute expenditure

#### 6. Sustainability (NEW)
- **Focus**: Minimize environmental impact
- **Key Practices**:
  - Understand your impact
  - Establish sustainability goals
  - Maximize utilization
  - Anticipate and adopt new efficient offerings
  - Use managed services
  - Reduce downstream impact

---

## 5. AWS Shared Responsibility Model

### AWS Responsibility: "Security OF the Cloud"
- **Physical infrastructure**
- **Hardware and global infrastructure**
- **Managed services** (RDS, S3, DynamoDB)
- **Regions, Availability Zones, Edge Locations**

### Customer Responsibility: "Security IN the Cloud"
- **Customer data**
- **Identity and Access Management (IAM)**
- **Operating systems, network, firewall configuration**
- **Encryption** (at rest and in transit)
- **Application security**
- **Network traffic protection**

### Shared Controls
- **Patch Management**: AWS patches infrastructure; customer patches OS and applications
- **Configuration Management**: Both maintain configurations
- **Awareness & Training**: Both train their personnel

```
┌─────────────────────────────────────────────┐
│         Customer Responsibility             │
│  (Security IN the Cloud)                    │
├─────────────────────────────────────────────┤
│  Customer Data                              │
│  Platform, Applications, IAM                │
│  Operating System, Network & Firewall       │
│  Client-side Encryption & Authentication    │
│  Server-side Encryption                     │
│  Network Traffic Protection                 │
├─────────────────────────────────────────────┤
│         AWS Responsibility                  │
│  (Security OF the Cloud)                    │
├─────────────────────────────────────────────┤
│  Software: Compute, Storage, Database, Net  │
│  Hardware/AWS Global Infrastructure         │
│  Regions, AZs, Edge Locations               │
└─────────────────────────────────────────────┘
```

---

## 6. AWS Account Management

### AWS Organizations
- **Centrally manage multiple AWS accounts**
- **Consolidated billing** across accounts
- **Service Control Policies (SCPs)** for governance
- **Organizational Units (OUs)** for grouping accounts

### AWS Control Tower
- Set up and govern multi-account AWS environment
- Automates account setup
- Implements guardrails (preventive and detective)

### Root User
- **Complete access** to all AWS services
- Created when you first create AWS account
- **Best Practice**: Don't use for everyday tasks
- **Secure with MFA**
- Use for limited tasks only (billing, account closure)

### Service Quotas
- Default limits on AWS resources
- Can request quota increases
- Helps prevent unexpected bills

---

## 7. Key AWS Concepts

### ARN (Amazon Resource Name)
Uniquely identify AWS resources
```
arn:partition:service:region:account-id:resource-type/resource-id
arn:aws:s3:::my-bucket/*
arn:aws:ec2:us-east-1:123456789012:instance/i-0abcd1234
```

### Tags
- **Key-value pairs** attached to AWS resources
- Used for organization, cost allocation, automation
- Example: Environment=Production, Owner=TeamA, CostCenter=Engineering

### Resource Groups
- Group resources based on tags
- Manage and automate tasks across resources

---

## 8. AWS Support Plans

| Feature | Basic | Developer | Business | Enterprise |
|---------|-------|-----------|----------|------------|
| **Price** | Free | $29/month | $100/month+ | $15,000/month+ |
| **Use Case** | Testing | Development | Production | Mission-critical |
| **Technical Support** | None | Business hours email | 24/7 phone, email, chat | 24/7 phone, email, chat |
| **Response Time (General)** | N/A | 24 hours | 24 hours | 24 hours |
| **Response Time (System impaired)** | N/A | 12 hours | 12 hours | 12 hours |
| **Response Time (Production down)** | N/A | N/A | 4 hours | 4 hours |
| **Response Time (Business-critical down)** | N/A | N/A | 1 hour | 1 hour |
| **Response Time (Critical - Enterprise Only)** | N/A | N/A | N/A | 15 minutes |
| **Trusted Advisor Checks** | 7 Core | 7 Core | Full | Full |
| **Technical Account Manager (TAM)** | No | No | No | Yes |

---

## Practice Questions

1. **Which of the following is NOT a benefit of cloud computing?**
   - A. Trade capital expense for variable expense
   - B. Massive economies of scale
   - C. Complete control over physical hardware
   - D. Go global in minutes
   
   **Answer**: C

2. **How many Availability Zones are recommended for a highly available application?**
   - A. 1
   - B. 2 or more
   - C. At least 5
   - D. All AZs in a region
   
   **Answer**: B

3. **Under the Shared Responsibility Model, who is responsible for patching the operating system of an EC2 instance?**
   - A. AWS
   - B. Customer
   - C. Both AWS and Customer
   - D. Third-party vendor
   
   **Answer**: B

---

## Hands-On Labs

### Lab 1: Create an AWS Account
1. Sign up for AWS Free Tier account
2. Set up MFA for root user
3. Create an IAM user for daily use
4. Configure AWS CLI with IAM user credentials

### Lab 2: Explore AWS Regions and AZs
1. Log into AWS Console
2. Navigate to EC2 service
3. Switch between regions
4. Note available AZs in each region

### Lab 3: Create Resource Tags
1. Launch a sample EC2 instance
2. Add tags: Name, Environment, Project
3. Create a resource group based on tags

---

## Key Takeaways

✅ AWS has a global infrastructure with Regions, AZs, and Edge Locations  
✅ The Well-Architected Framework has 6 pillars (remember them!)  
✅ Shared Responsibility Model: AWS = Security OF the Cloud, Customer = Security IN the Cloud  
✅ Use IAM users instead of root user for day-to-day operations  
✅ Tags are essential for organization and cost management  
✅ Choose the right region based on compliance, latency, cost, and available services  

---

## Additional Resources

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)

---

**Next Module**: [Module 02: Identity and Access Management (IAM)](../02-IAM/README.md)

