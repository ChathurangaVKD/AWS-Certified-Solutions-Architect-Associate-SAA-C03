# Module 14: Practice Questions & Mock Exams

## Overview
This module provides comprehensive practice questions organized by domain, real-world scenarios, and full mock exams to prepare for the AWS Solutions Architect Associate exam.

## Exam Format Reminder
- **65 questions** (multiple choice and multiple response)
- **130 minutes** (2 hours 10 minutes)
- **Passing score**: 720/1000
- **Scenario-based questions**
- **No penalty for wrong answers** (guess if unsure)

---

## Domain 1: Design Secure Architectures (30%)

### Questions

**Q1.** A company needs to store sensitive customer data in S3. The data must be encrypted at rest, and the company wants full control over the encryption keys, including key rotation. Which solution meets these requirements?

A. Use S3-managed encryption (SSE-S3)  
B. Use AWS KMS-managed encryption (SSE-KMS) with customer managed keys  
C. Use customer-provided encryption (SSE-C)  
D. Use client-side encryption  

<details>
<summary>Answer</summary>
**B.** SSE-KMS with customer managed keys allows full control including key rotation via KMS.
</details>

---

**Q2.** An application running on EC2 needs to access S3 buckets. What is the MOST secure way to grant this access?

A. Create an IAM user with access keys and store them on the EC2 instance  
B. Attach an IAM role to the EC2 instance  
C. Use S3 bucket policy to allow access from the EC2 instance's IP address  
D. Make the S3 bucket public  

<details>
<summary>Answer</summary>
**B.** IAM roles provide temporary credentials and are the most secure method for EC2 to access AWS services.
</details>

---

**Q3.** A company wants to ensure that only encrypted connections are used to access their S3 bucket. What should they do?

A. Enable S3 default encryption  
B. Use S3 bucket policy to deny requests without ssl:SecureTransport  
C. Enable S3 versioning  
D. Configure S3 CORS  

<details>
<summary>Answer</summary>
**B.** Bucket policy with condition `"Condition": {"Bool": {"aws:SecureTransport": "false"}}` and Effect Deny.
</details>

---

**Q4.** A solutions architect needs to design a solution where multiple AWS accounts can access a centralized logging S3 bucket. What is the MOST operationally efficient solution?

A. Create IAM users in the logging account for each account  
B. Use S3 bucket policy to grant access to specific AWS account IDs  
C. Enable S3 Cross-Region Replication  
D. Make the bucket public  

<details>
<summary>Answer</summary>
**B.** S3 bucket policy can grant cross-account access using Principal with account IDs.
</details>

---

**Q5.** Which IAM policy element can be used to restrict access to AWS resources based on the source IP address?

A. Principal  
B. Action  
C. Resource  
D. Condition  

<details>
<summary>Answer</summary>
**D.** Condition with `aws:SourceIp` key.
</details>

---

**Q6.** A company needs to implement MFA for all users accessing sensitive S3 data. How can this be enforced?

A. Enable MFA Delete on the S3 bucket  
B. Use IAM policy condition requiring `aws:MultiFactorAuthPresent`  
C. Configure S3 bucket policy with IP restrictions  
D. Use AWS Organizations SCPs  

<details>
<summary>Answer</summary>
**B.** IAM policy with condition `"Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}`.
</details>

---

**Q7.** A security audit requires that all API calls made in an AWS account be logged and stored for 7 years. What should be configured?

A. Enable CloudWatch Logs with 7-year retention  
B. Enable CloudTrail and configure S3 bucket with lifecycle policy to Glacier  
C. Enable VPC Flow Logs  
D. Enable AWS Config  

<details>
<summary>Answer</summary>
**B.** CloudTrail logs API calls. Store in S3 and use lifecycle policy to move to Glacier for long-term retention.
</details>

---

**Q8.** An application needs to access AWS Secrets Manager to retrieve database credentials. What is the BEST way to grant access?

A. Store Secrets Manager API credentials in application code  
B. Use IAM role attached to EC2/Lambda with GetSecretValue permission  
C. Use root account credentials  
D. Store database credentials in environment variables  

<details>
<summary>Answer</summary>
**B.** IAM role with least privilege permission to access specific secrets.
</details>

---

## Domain 2: Design Resilient Architectures (26%)

**Q9.** A company runs a web application that must be highly available across multiple Availability Zones. The application uses a relational database. What is the MOST cost-effective solution?

A. Deploy EC2 instances in multiple AZs with Auto Scaling, and RDS Multi-AZ  
B. Deploy EC2 instances in multiple regions with Aurora Global Database  
C. Use Lambda with DynamoDB  
D. Deploy in single AZ with regular snapshots  

<details>
<summary>Answer</summary>
**A.** Multi-AZ deployment with Auto Scaling and RDS Multi-AZ provides high availability at reasonable cost.
</details>

---

**Q10.** An application requires a file system that can be mounted on multiple EC2 instances simultaneously across different AZs. Which storage service should be used?

A. EBS  
B. Instance Store  
C. EFS  
D. S3  

<details>
<summary>Answer</summary>
**C.** EFS is a managed NFS that can be mounted on multiple instances across AZs.
</details>

---

**Q11.** A company wants to implement disaster recovery with an RTO of 1 hour and RPO of 15 minutes for their critical application. Which DR strategy should they use?

A. Backup and Restore  
B. Pilot Light  
C. Warm Standby  
D. Multi-Site Active-Active  

<details>
<summary>Answer</summary>
**C.** Warm Standby provides RTO in minutes to hours and RPO in seconds to minutes with continuous replication.
</details>

---

**Q12.** An Auto Scaling group is not launching new instances despite high CPU utilization. What could be the issue? (Choose TWO)

A. Security group is blocking traffic  
B. Maximum capacity reached  
C. Launch template is invalid  
D. Insufficient IAM permissions for Auto Scaling  
E. ELB health checks are failing  

<details>
<summary>Answer</summary>
**B, D.** Maximum capacity limit or IAM permissions issue would prevent new instances from launching.
</details>

---

**Q13.** A company needs to ensure that deleted objects in an S3 bucket can be recovered for up to 30 days. What should be enabled?

A. S3 Cross-Region Replication  
B. S3 Versioning  
C. S3 Object Lock  
D. S3 Lifecycle Policy  

<details>
<summary>Answer</summary>
**B.** S3 Versioning preserves deleted objects as delete markers, allowing recovery.
</details>

---

**Q14.** A solutions architect is designing a decoupled architecture. Which AWS service should be used to decouple the components?

A. Elastic Load Balancing  
B. Amazon SQS  
C. Amazon CloudFront  
D. AWS Direct Connect  

<details>
<summary>Answer</summary>
**B.** SQS provides message queuing to decouple components.
</details>

---

**Q15.** An application experiences variable traffic with sudden spikes. What is the MOST cost-effective compute solution?

A. Reserved Instances  
B. On-Demand Instances with Auto Scaling  
C. Dedicated Hosts  
D. Spot Instances  

<details>
<summary>Answer</summary>
**B.** On-Demand with Auto Scaling handles variable traffic and you only pay when instances run.
</details>

---

## Domain 3: Design High-Performing Architectures (24%)

**Q16.** A web application serves static content to users globally. Which combination provides the LOWEST latency? (Choose TWO)

A. Amazon CloudFront  
B. Amazon S3  
C. Amazon EC2 in multiple regions  
D. Route 53 latency-based routing  
E. Elastic Load Balancing  

<details>
<summary>Answer</summary>
**A, B.** CloudFront CDN with S3 origin provides global edge locations for lowest latency.
</details>

---

**Q17.** An application needs to process millions of requests per second with single-digit millisecond latency for a NoSQL database. Which service should be used?

A. RDS MySQL  
B. Aurora  
C. DynamoDB with DAX  
D. Redshift  

<details>
<summary>Answer</summary>
**C.** DynamoDB provides high throughput, and DAX adds microsecond latency caching.
</details>

---

**Q18.** A company needs to improve RDS database read performance without modifying application code. What should they do?

A. Increase RDS instance size  
B. Enable RDS Multi-AZ  
C. Create RDS Read Replicas  
D. Enable automated backups  

<details>
<summary>Answer</summary>
**C.** Read Replicas offload read traffic from primary database.
</details>

---

**Q19.** An application performs complex analytical queries on large datasets. Which database is MOST appropriate?

A. DynamoDB  
B. RDS MySQL  
C. Amazon Redshift  
D. ElastiCache  

<details>
<summary>Answer</summary>
**C.** Redshift is a data warehouse optimized for OLAP queries on large datasets.
</details>

---

**Q20.** A gaming application requires ultra-low latency and needs to process millions of requests per second at Layer 4. Which load balancer should be used?

A. Application Load Balancer  
B. Network Load Balancer  
C. Classic Load Balancer  
D. Gateway Load Balancer  

<details>
<summary>Answer</summary>
**B.** NLB operates at Layer 4, provides ultra-low latency and handles millions of requests/second.
</details>

---

**Q21.** A company wants to migrate their MongoDB database to AWS with minimal changes. Which service should they use?

A. RDS MySQL  
B. DynamoDB  
C. Amazon DocumentDB  
D. Amazon Neptune  

<details>
<summary>Answer</summary>
**C.** DocumentDB is MongoDB-compatible.
</details>

---

**Q22.** An EC2 instance requires maximum I/O performance for a database workload. Which EBS volume type should be used?

A. gp3  
B. gp2  
C. io2 Block Express  
D. sc1  

<details>
<summary>Answer</summary>
**C.** io2 Block Express provides highest IOPS (256,000) and lowest latency.
</details>

---

## Domain 4: Design Cost-Optimized Architectures (20%)

**Q23.** A company runs batch processing jobs that can be interrupted. Which EC2 pricing option provides the MOST cost savings?

A. On-Demand  
B. Reserved Instances  
C. Spot Instances  
D. Dedicated Hosts  

<details>
<summary>Answer</summary>
**C.** Spot Instances provide up to 90% discount and are suitable for interruptible workloads.
</details>

---

**Q24.** A database runs 24/7 for the next 3 years. What is the MOST cost-effective option?

A. On-Demand Instances  
B. Spot Instances  
C. Reserved Instances with 3-year All Upfront  
D. Savings Plans  

<details>
<summary>Answer</summary>
**C.** 3-year All Upfront RIs provide highest discount for steady-state workloads.
</details>

---

**Q25.** A company stores log files in S3 that are accessed frequently for 30 days, then rarely accessed. What is the MOST cost-effective solution?

A. Store in S3 Standard for 30 days, then manually move to Glacier  
B. Use S3 Intelligent-Tiering  
C. Use S3 lifecycle policy to transition to S3 IA after 30 days, then Glacier after 90 days  
D. Store everything in S3 Glacier  

<details>
<summary>Answer</summary>
**C.** Lifecycle policies automate transitions to optimize cost based on access patterns.
</details>

---

**Q26.** A company needs to reduce data transfer costs between EC2 instances and S3 in the same region. What should they use?

A. CloudFront  
B. VPC Endpoint for S3  
C. NAT Gateway  
D. Internet Gateway  

<details>
<summary>Answer</summary>
**B.** VPC Gateway Endpoint for S3 keeps traffic within AWS network (no data transfer charges) and is free.
</details>

---

**Q27.** An application uses Lambda functions that run for 10 minutes several times per day. How can costs be optimized?

A. Use Provisioned Concurrency  
B. Increase memory allocation  
C. Optimize code to reduce execution time  
D. Switch to EC2  

<details>
<summary>Answer</summary>
**C.** Lambda charges based on execution time and memory, so reducing execution time reduces cost.
</details>

---

**Q28.** A company has multiple AWS accounts and wants to receive one consolidated bill. What should they use?

A. AWS Cost Explorer  
B. AWS Budgets  
C. AWS Organizations with consolidated billing  
D. AWS Trusted Advisor  

<details>
<summary>Answer</summary>
**C.** AWS Organizations provides consolidated billing across multiple accounts and volume discounts.
</details>

---

## Scenario-Based Questions

**Scenario 1: High Availability Web Application**

A company is deploying a web application that must:
- Serve users globally with low latency
- Be highly available across multiple AZs
- Handle traffic spikes automatically
- Use a MySQL database
- Store user-uploaded images

**Q29.** Which architecture components should be used? (Choose THREE)

A. CloudFront for content delivery  
B. Application Load Balancer across multiple AZs  
C. EC2 Auto Scaling Group  
D. Single EC2 instance  
E. RDS MySQL in single AZ  
F. RDS MySQL Multi-AZ  

<details>
<summary>Answer</summary>
**A, B, C, F.** CloudFront for global delivery, ALB for HA load balancing, Auto Scaling for handling spikes, RDS Multi-AZ for database HA. (Choose 3: A, C, F most critical)
</details>

---

**Q30.** Where should user-uploaded images be stored?

A. EBS volumes attached to EC2  
B. Instance Store  
C. Amazon S3  
D. RDS database  

<details>
<summary>Answer</summary>
**C.** S3 provides durable object storage for images, accessible from multiple instances.
</details>

---

**Scenario 2: Serverless Application**

A startup wants to build a serverless REST API that:
- Handles unpredictable traffic
- Stores user data
- Sends email notifications
- Requires user authentication

**Q31.** Which services should be used for the API layer?

A. EC2 with Elastic Load Balancing  
B. API Gateway with Lambda  
C. ECS with Fargate  
D. Elastic Beanstalk  

<details>
<summary>Answer</summary>
**B.** API Gateway + Lambda is fully serverless, auto-scales, and pay per use.
</details>

---

**Q32.** Which service should be used for user authentication?

A. IAM  
B. Amazon Cognito  
C. AWS Directory Service  
D. AWS SSO  

<details>
<summary>Answer</summary>
**B.** Cognito provides user authentication for web and mobile apps.
</details>

---

**Q33.** Which database service is MOST appropriate?

A. RDS MySQL  
B. Aurora Serverless  
C. DynamoDB  
D. Redshift  

<details>
<summary>Answer</summary>
**C.** DynamoDB is serverless NoSQL, auto-scales, and pay per request (On-Demand mode).
</details>

---

**Q34.** How should email notifications be sent?

A. Lambda directly calls email API  
B. SNS topic with email subscription  
C. SQS queue with Lambda consumer  
D. SES with Lambda  

<details>
<summary>Answer</summary>
**D.** Amazon SES (Simple Email Service) is designed for sending emails, triggered by Lambda.
</details>

---

**Scenario 3: Data Analytics Platform**

A company needs to:
- Ingest clickstream data from millions of devices in real-time
- Process and analyze data
- Store historical data cost-effectively
- Query data using SQL

**Q35.** Which service should be used for real-time data ingestion?

A. Amazon SQS  
B. Amazon Kinesis Data Streams  
C. Amazon S3  
D. AWS Database Migration Service  

<details>
<summary>Answer</summary>
**B.** Kinesis Data Streams handles real-time streaming data at scale.
</details>

---

**Q36.** How should data be processed in real-time?

A. EC2 instances  
B. Lambda or Kinesis Data Analytics  
C. Redshift  
D. RDS  

<details>
<summary>Answer</summary>
**B.** Lambda (for event processing) or Kinesis Data Analytics (for streaming SQL).
</details>

---

**Q37.** Where should historical data be stored for cost optimization?

A. DynamoDB  
B. RDS  
C. S3 with lifecycle policy to Glacier  
D. EBS volumes  

<details>
<summary>Answer</summary>
**C.** S3 for durability and low cost, lifecycle to Glacier for archival.
</details>

---

**Q38.** Which service should be used to query data in S3 using SQL?

A. Amazon RDS  
B. Amazon Athena  
C. Amazon EMR  
D. Amazon Redshift Spectrum  

<details>
<summary>Answer</summary>
**B.** Athena allows SQL queries directly on S3 data, serverless and pay per query.
</details>

---

## Mock Exam 1 (30 Questions)

**Q39.** What is the maximum size of an S3 object?

A. 5 GB  
B. 5 TB  
C. 500 GB  
D. Unlimited  

<details>
<summary>Answer</summary>
**B.** Maximum object size is 5 TB.
</details>

---

**Q40.** Which routing policy in Route 53 is used for active-passive failover?

A. Simple  
B. Weighted  
C. Failover  
D. Geolocation  

<details>
<summary>Answer</summary>
**C.** Failover routing policy with primary and secondary records.
</details>

---

**Q41.** An EC2 instance needs temporary credentials to access S3. What should be used?

A. IAM User with access keys  
B. IAM Role  
C. Root account  
D. S3 bucket policy  

<details>
<summary>Answer</summary>
**B.** IAM Role provides temporary credentials automatically.
</details>

---

**Q42.** Which service provides DDoS protection at no additional cost?

A. AWS WAF  
B. AWS Shield Standard  
C. AWS Shield Advanced  
D. Amazon GuardDuty  

<details>
<summary>Answer</summary>
**B.** Shield Standard is free for all AWS customers.
</details>

---

**Q43.** What is the minimum and maximum size of a VPC CIDR block?

A. /8 to /32  
B. /16 to /28  
C. /24 to /32  
D. /16 to /24  

<details>
<summary>Answer</summary>
**B.** VPC CIDR can be /16 to /28.
</details>

---

**Q44.** Which service automatically discovers and protects sensitive data in S3?

A. Amazon Inspector  
B. Amazon GuardDuty  
C. Amazon Macie  
D. AWS Config  

<details>
<summary>Answer</summary>
**C.** Macie uses ML to discover and protect sensitive data (PII) in S3.
</details>

---

**Q45.** What is the default behavior of a custom NACL?

A. Allow all inbound and outbound  
B. Deny all inbound and outbound  
C. Allow inbound, deny outbound  
D. Deny inbound, allow outbound  

<details>
<summary>Answer</summary>
**B.** Custom NACLs deny all traffic by default until rules are added.
</details>

---

**Q46.** Which EBS volume type can be used as a boot volume?

A. st1  
B. sc1  
C. gp3  
D. All of the above  

<details>
<summary>Answer</summary>
**C.** Only SSD volumes (gp2, gp3, io1, io2) can be boot volumes.
</details>

---

**Q47.** How many Read Replicas can an Aurora database have?

A. 5  
B. 10  
C. 15  
D. 20  

<details>
<summary>Answer</summary>
**C.** Aurora supports up to 15 Read Replicas.
</details>

---

**Q48.** What is the maximum execution time for a Lambda function?

A. 5 minutes  
B. 10 minutes  
C. 15 minutes  
D. 30 minutes  

<details>
<summary>Answer</summary>
**C.** Lambda timeout is maximum 15 minutes (900 seconds).
</details>

---

**Q49.** Which service provides a managed GraphQL API?

A. API Gateway  
B. AWS AppSync  
C. Amazon Kinesis  
D. AWS Step Functions  

<details>
<summary>Answer</summary>
**B.** AppSync provides managed GraphQL APIs.
</details>

---

**Q50.** A company needs to migrate 100 TB of data to AWS within one week. Which service should they use?

A. AWS DataSync over internet  
B. AWS Snowball  
C. Direct Connect  
D. S3 Transfer Acceleration  

<details>
<summary>Answer</summary>
**B.** Snowball is designed for offline data transfer of large amounts in days.
</details>

---

## Exam Tips

### Time Management
- **2 minutes per question** on average
- Flag difficult questions and come back
- Answer all questions (no penalty for wrong answers)

### Reading Questions
- Read question carefully (look for keywords: MOST, LEAST, BEST)
- Identify what's being asked (cost, performance, security, availability)
- Eliminate obviously wrong answers

### Common Patterns
- **High Availability** → Multi-AZ, Auto Scaling, ELB
- **Disaster Recovery** → Cross-region replication, backups
- **Cost Optimization** → Spot, Reserved, lifecycle policies, right-sizing
- **Performance** → Caching (CloudFront, ElastiCache, DAX), Read Replicas
- **Security** → Least privilege, encryption, IAM roles, private subnets
- **Scalability** → Auto Scaling, serverless, managed services

### Keywords to Watch
- **MOST secure** → IAM roles, encryption, private subnets, least privilege
- **MOST cost-effective** → Spot, Reserved, S3 lifecycle, serverless
- **LEAST operational overhead** → Managed services, serverless
- **Highly available** → Multi-AZ, multiple regions
- **Lowest latency** → CloudFront, edge locations, caching

---

## Study Checklist

- [ ] Reviewed all 14 modules
- [ ] Completed hands-on labs for each service
- [ ] Practiced with sample questions (200+)
- [ ] Taken at least 2 full-length mock exams
- [ ] Reviewed AWS Well-Architected Framework
- [ ] Familiar with all major service limits/quotas
- [ ] Understand common architecture patterns
- [ ] Can differentiate between similar services (RDS vs DynamoDB, ALB vs NLB, etc.)
- [ ] Reviewed AWS whitepapers (at least key ones)
- [ ] Confident with IAM policies and permissions

---

## Additional Practice Resources

1. **AWS Skill Builder**: Free official practice exams
2. **AWS Whitepapers**: Focus on Well-Architected Framework
3. **AWS FAQs**: Read FAQs for major services (EC2, S3, RDS, VPC)
4. **AWS Documentation**: Service features and use cases
5. **AWS re:Invent Videos**: Architecture sessions

---

**Good luck on your AWS Solutions Architect Associate exam!** 🎉

---

**Previous Module**: [Module 13: Cost Optimization](../13-Cost-Optimization/README.md)  
**Main README**: [Back to Main](../README.md)

