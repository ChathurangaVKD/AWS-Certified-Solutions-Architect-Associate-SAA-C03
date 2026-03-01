# AWS SAA-C03 Practice Questions

> Focused practice questions for weak areas and common exam scenarios

> **⚠️ DISCLAIMER:** These are **original practice questions** created for educational purposes. They are **NOT actual exam questions** and do not represent questions from the AWS certification exam. All content is based on publicly available AWS documentation.

## 📋 Categories
- [Auto Scaling & High Availability](#auto-scaling--high-availability)
- [Storage & Data Management](#storage--data-management)
- [Networking](#networking)
- [Databases](#databases)
- [Serverless & Containers](#serverless--containers)
- [Security](#security)
- [Cost Optimization](#cost-optimization)

---

## Auto Scaling & High Availability

### Question 1
An Auto Scaling group isn't responding to CloudWatch alarms despite the alarm firing. What's the most likely cause?

**Options:**
A. Wrong CloudWatch metric configured
B. The Auto Scaling group is in cooldown period ✓
C. Minimum size of ASG is 0
D. Desired size of ASG is 0

**Explanation:** Cooldown periods suppress scaling actions to let metrics stabilize after a scaling event.

---

### Question 2
You need to upgrade one EC2 instance in an ASG without receiving traffic. What should you do?

**Options:**
A. Hibernate the instance
B. Use cooldown timers
C. Put instance in Standby, upgrade, return to InService ✓
D. Use lifecycle hooks

**Explanation:** Standby detaches from load balancing while retaining in ASG, preventing replacement.

---

## Storage & Data Management

### Question 3
How do you achieve WORM (Write Once Read Many) in S3?

**Options:**
A. Enable versioning
B. Enable Object Lock at bucket creation ✓
C. Use S3 Glacier
D. Configure bucket policy

**Explanation:** Object Lock enforces WORM with retention periods; must be enabled at bucket creation.

---

### Question 4
After deleting an S3 object (no versioning), what do you see immediately in a list-objects call?

**Options:**
A. Object still appears
B. Object is deleted ✓
C. May appear or not depending on consistency
D. Object has a delete marker

**Explanation:** S3 provides strong consistency; object disappears immediately after successful delete.

---

## Networking

### Question 5
What VPC feature provides private connectivity to S3 and DynamoDB without cost?

**Options:**
A. NAT Gateway
B. VPC Peering
C. Gateway Endpoints ✓
D. Interface Endpoints

**Explanation:** Gateway endpoints for S3/DynamoDB are free and route-table based.

---

### Question 6
Internet-facing ALB requests fail despite healthy targets. What's likely wrong?

**Options:**
A. ALB subnet route table lacks IGW route ✓
B. Targets in public subnet
C. ALB has no Elastic IP
D. Cross-zone LB disabled

**Explanation:** ALB must be in public subnets with 0.0.0.0/0 → IGW route.

---

## Databases

### Question 7
Your read-heavy app hits 100% CPU on RDS. What helps scale reads? (Choose 3)

**Options:**
A. Add Read Replicas ✓
B. Enable Storage Auto Scaling
C. Use SQS to throttle
D. Use ElastiCache ✓
E. Shard across multiple RDS instances ✓
F. Enable Multi-AZ

**Explanation:** Read replicas, caching, and sharding all reduce read load on primary.

---

### Question 8
Multi-AZ RDS deployment provides:

**Options:**
A. Read scaling
B. Automatic failover for high availability ✓
C. Cross-region disaster recovery
D. Cost optimization

**Explanation:** Multi-AZ maintains synchronous standby for automatic failover, not for reads.

---

## Serverless & Containers

### Question 9
Lambda needs to write CloudWatch Logs. Which permissions required? (Choose 3)

**Options:**
A. logs:CreateLogGroup ✓
B. logs:GetLogEvents
C. logs:CreateLogStream ✓
D. logs:DescribeLogStreams
E. logs:PutLogEvents ✓

**Explanation:** Lambda runtime needs all three to create log groups, streams, and write events.

---

### Question 10
Which ECS networking mode provides task-level security groups?

**Options:**
A. Host
B. Bridge
C. awsvpc ✓
D. Default

**Explanation:** awsvpc gives each task its own ENI, enabling task-level security groups.

---

## Security

### Question 11
How do you restrict S3 bucket access to specific IAM roles only?

**Options:**
A. Bucket policy with explicit deny for all except listed roles
B. Bucket policy with explicit deny for all users except listed
C. Bucket policy allowing only specific role; users assume role ✓
D. Bucket policy with NotPrincipal

**Explanation:** Grant bucket access to a role; users authenticate then assume that role.

---

### Question 12
CloudFront serves private content from S3. How do you grant access to multiple files?

**Options:**
A. S3 pre-signed URLs
B. CloudFront signed URLs
C. CloudFront signed cookies ✓
D. CloudFront geo restrictions

**Explanation:** Signed cookies grant access to multiple objects without changing URLs.

---

## Cost Optimization

### Question 13
Which services identify underutilized EC2 instances? (Choose 2)

**Options:**
A. CloudWatch ✓
B. SNS
C. Trusted Advisor ✓
D. CloudTrail
E. Config

**Explanation:** CloudWatch metrics and Trusted Advisor checks identify low-utilization instances.

---

### Question 14
Most cost-effective connectivity for small vendor team to VPC databases?

**Options:**
A. AWS Client VPN ✓
B. Direct Connect
C. Site-to-Site VPN to VGW
D. Site-to-Site VPN to Transit Gateway

**Explanation:** Client VPN provides user-level auth, pay-as-you-go pricing, minimal setup.

---

## Architecture Patterns

### Question 15
Serverless media processing pipeline with visual workflow and priority queues?

**Options:**
A. S3 → Lambda → SQS → DynamoDB
B. S3 → Lambda → SWF → DynamoDB
C. S3 → Lambda → process → DynamoDB
D. S3 → Lambda → Step Functions → DynamoDB ✓

**Explanation:** Step Functions orchestrates with visual console, priority via separate entry points.

---

*Practice these scenarios until you can explain each answer confidently!*

