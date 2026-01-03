# AWS Fundamentals - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company is deploying a new application on AWS and needs to ensure the highest level of availability and fault tolerance. The application must continue to operate even if an entire data center fails. Which AWS infrastructure component should be used?

A. Deploy across multiple Edge Locations  
B. Deploy across multiple Availability Zones within a single Region  
C. Deploy across multiple Regions  
D. Deploy using AWS Local Zones  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Availability Zones (AZs) are separate data centers within a Region
- Deploying across multiple AZs protects against data center failure
- This is the standard approach for high availability within a Region
- Option C (multiple Regions) is for disaster recovery, not just data center failure
- Edge Locations are for content delivery, not application hosting
- Local Zones are for ultra-low latency but don't provide the same fault tolerance

**References:** AWS Global Infrastructure, Well-Architected Framework - Reliability Pillar
</details>

---

### Question 2
A solutions architect needs to design a solution that minimizes latency for users accessing static content globally. Which combination of AWS services should be used?

A. Amazon S3 with Cross-Region Replication  
B. Amazon CloudFront with S3 as the origin  
C. Amazon S3 with Transfer Acceleration  
D. Multiple EC2 instances in different Regions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudFront is AWS's Content Delivery Network (CDN) with 400+ edge locations globally
- It caches content close to users, minimizing latency
- S3 serves as the origin for static content
- Option A provides redundancy but doesn't optimize latency
- Option C accelerates uploads, not downloads
- Option D is cost-ineffective and complex to manage

**References:** CloudFront, Edge Locations, Global Infrastructure
</details>

---

### Question 3
According to the AWS Shared Responsibility Model, which of the following is AWS's responsibility?

A. Encryption of data at rest in S3  
B. Patch management of guest operating systems on EC2  
C. Physical security of data centers  
D. Configuration of security groups  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS is responsible for "Security OF the Cloud" - physical infrastructure
- This includes data centers, hardware, and facilities
- Customers are responsible for "Security IN the Cloud"
- Options A, B, and D are all customer responsibilities
- Customers choose whether to encrypt, patch OS, and configure security

**References:** AWS Shared Responsibility Model
</details>

---

### Question 4
A startup company wants to deploy an application without managing servers, operating systems, or runtime environments. Which AWS service category best fits this requirement?

A. Infrastructure as a Service (IaaS)  
B. Platform as a Service (PaaS)  
C. Software as a Service (SaaS)  
D. Function as a Service (FaaS)  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- PaaS services (like Elastic Beanstalk) abstract infrastructure management
- Users deploy code without managing servers or OS
- IaaS (like EC2) requires managing virtual machines
- SaaS is fully managed applications (like Amazon Chime)
- FaaS (like Lambda) is event-driven, not for full applications typically
- PaaS is the best fit for deploying applications without infrastructure management

**References:** AWS Service Categories, Cloud Computing Models
</details>

---

### Question 5
A company has regulatory requirements to ensure that data stored in AWS does not leave a specific geographic location. How can this be achieved?

A. Enable AWS GuardDuty  
B. Choose the appropriate AWS Region and do not enable cross-region features  
C. Use AWS Organizations with Service Control Policies  
D. Enable AWS CloudTrail  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Data in an AWS Region stays in that Region unless you explicitly configure otherwise
- No cross-region replication, backups, or data transfer ensures data residency
- GuardDuty is for threat detection, not data residency
- SCPs can enforce policies but the key is choosing the right Region
- CloudTrail is for logging, not data residency
- Primary control: select Region and don't configure cross-region services

**References:** AWS Regions, Data Sovereignty, Compliance
</details>

---

### Question 6
Which pillar of the AWS Well-Architected Framework focuses on the ability to recover from failures and dynamically acquire computing resources to meet demand?

A. Operational Excellence  
B. Security  
C. Reliability  
D. Performance Efficiency  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Reliability pillar focuses on recovery from failures and maintaining workload functionality
- Key aspects: fault tolerance, disaster recovery, self-healing
- Operational Excellence focuses on operations and monitoring
- Security focuses on protecting information and systems
- Performance Efficiency focuses on using resources efficiently

**References:** AWS Well-Architected Framework - Reliability Pillar
</details>

---

### Question 7
A company wants to estimate the cost of running their planned AWS infrastructure before deployment. Which AWS tool should they use?

A. AWS Cost Explorer  
B. AWS Budgets  
C. AWS Pricing Calculator  
D. AWS Cost and Usage Report  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS Pricing Calculator estimates costs for planned architectures
- Cost Explorer analyzes existing/historical costs
- AWS Budgets sets budget alerts
- Cost and Usage Report provides detailed billing data
- For estimation BEFORE deployment, Pricing Calculator is correct

**References:** AWS Pricing Tools, Cost Management
</details>

---

### Question 8
An application requires 15 milliseconds or less of latency for users in a specific metropolitan area. Which AWS infrastructure component should be used?

A. AWS Region  
B. Availability Zone  
C. AWS Local Zone  
D. AWS Wavelength Zone  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS Local Zones bring compute, storage, and database closer to end-users
- Designed for single-digit millisecond latency requirements
- Placed in metropolitan areas for ultra-low latency applications
- Wavelength Zones are for 5G edge computing
- Regular Regions/AZs may not meet ultra-low latency requirements

**References:** AWS Local Zones, Global Infrastructure
</details>

---

### Question 9
Which AWS service provides a unified interface to manage multiple AWS accounts within an organization?

A. AWS IAM  
B. AWS Organizations  
C. AWS Control Tower  
D. AWS Systems Manager  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Organizations centrally manages multiple AWS accounts
- Provides consolidated billing, account creation, and policy management
- IAM manages permissions within an account
- Control Tower sets up multi-account environments (uses Organizations underneath)
- Systems Manager manages AWS resources, not accounts
- Direct answer for multi-account management: Organizations

**References:** AWS Organizations, Account Management
</details>

---

### Question 10
According to the AWS Well-Architected Framework, which design principle is recommended for the Security pillar?

A. Implement a strong identity foundation  
B. Go global in minutes  
C. Stop spending money on data center operations  
D. Implement feedback loops  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- "Implement a strong identity foundation" is a Security pillar principle
- Includes: least privilege, separation of duties, centralized identity management
- Option B relates to global deployment (general AWS benefit)
- Option C is a cloud advantage, not security principle
- Option D relates to Operational Excellence pillar

**References:** AWS Well-Architected Framework - Security Pillar Design Principles
</details>

---

### Question 11
A company wants to use AWS CLI to manage resources but wants to avoid embedding long-term credentials in their scripts. What is the BEST practice?

A. Use root account credentials  
B. Create an IAM user and store credentials in the script  
C. Use IAM roles with temporary security credentials  
D. Use access keys without secret keys  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- IAM roles provide temporary security credentials via AWS STS
- Credentials rotate automatically, enhancing security
- Never use root account credentials for daily tasks
- Never hardcode credentials in scripts
- Access keys always require secret keys
- Best practice: IAM roles with temporary credentials

**References:** IAM Best Practices, AWS CLI Security
</details>

---

### Question 12
Which of the following is a benefit of using AWS Regions? (Choose TWO)

A. Reduced latency for users in specific geographic areas  
B. Automatic data replication across all Regions  
C. Compliance with data sovereignty requirements  
D. Lower costs compared to using a single Region  
E. Automatic failover between Regions  

<details>
<summary>Show Answer</summary>

**Answer: A, C**

**Explanation:**
- **A is correct**: Deploying in Regions closer to users reduces latency
- **C is correct**: Regions enable meeting data residency/sovereignty requirements
- B is incorrect: Replication is NOT automatic, must be configured
- D is incorrect: Multiple Regions typically increase costs
- E is incorrect: Failover is NOT automatic, requires architecture design

**References:** AWS Regions, Global Infrastructure Benefits
</details>

---

### Question 13
A solutions architect needs to design a system that follows the "Design for Failure" principle of the Well-Architected Framework. Which approach should be taken?

A. Use only the largest EC2 instance types to prevent failures  
B. Design the application to handle component failures gracefully  
C. Deploy all resources in a single Availability Zone for simplicity  
D. Rely on AWS Support to handle all failures  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- "Design for Failure" means assuming components will fail and planning accordingly
- Applications should handle failures gracefully with retry logic, health checks, etc.
- Larger instances don't prevent failures
- Single AZ deployment increases failure risk
- You must design for failure, not rely solely on support
- Proper approach: graceful degradation, automatic recovery

**References:** AWS Well-Architected Framework - Reliability Pillar
</details>

---

### Question 14
Which statement about AWS Edge Locations is correct?

A. Edge Locations are only used for CloudFront content delivery  
B. There are fewer Edge Locations than Regions  
C. Edge Locations can be used for both content delivery and edge computing  
D. Edge Locations are the same as Availability Zones  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Edge Locations support CloudFront (CDN), Lambda@Edge, and other edge services
- There are 400+ edge locations vs 30+ Regions
- Edge Locations ≠ Availability Zones (different purposes)
- Used for content delivery AND edge computing (Lambda@Edge, CloudFront Functions)

**References:** AWS Global Infrastructure - Edge Locations
</details>

---

### Question 15
A company wants to receive alerts when their monthly AWS costs exceed a threshold. Which service should they use?

A. AWS Cost Explorer  
B. AWS Budgets  
C. AWS Pricing Calculator  
D. AWS Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Budgets allows setting custom cost/usage budgets with alerts
- Can send notifications via SNS when thresholds are exceeded
- Cost Explorer visualizes historical costs but doesn't send alerts
- Pricing Calculator estimates future costs
- Trusted Advisor provides best practice recommendations
- For threshold alerts: AWS Budgets

**References:** AWS Budgets, Cost Management
</details>

---

### Question 16
According to the AWS Shared Responsibility Model, who is responsible for patching the underlying hypervisor for EC2 instances?

A. Customer  
B. AWS  
C. Both AWS and Customer  
D. Third-party vendors  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS manages the hypervisor layer (security OF the cloud)
- Customers manage guest OS patches (security IN the cloud)
- Hypervisor is infrastructure, AWS's responsibility
- Customer patches OS, applications, data encryption

**References:** AWS Shared Responsibility Model - EC2
</details>

---

### Question 17
A company wants to deploy applications closer to 5G mobile users for ultra-low latency. Which AWS service should be used?

A. AWS Local Zones  
B. AWS Wavelength  
C. AWS Outposts  
D. AWS Direct Connect  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Wavelength embeds compute at 5G network edge
- Provides single-digit millisecond latency to mobile devices
- Local Zones are for metro areas but not 5G-specific
- Outposts is for on-premises AWS infrastructure
- Direct Connect is for dedicated network connection
- For 5G mobile: Wavelength

**References:** AWS Wavelength, Edge Computing
</details>

---

### Question 18
Which pillar of the AWS Well-Architected Framework includes the principle "Stop guessing your capacity needs"?

A. Cost Optimization  
B. Performance Efficiency  
C. Reliability  
D. Operational Excellence  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Performance Efficiency pillar includes capacity planning principles
- "Stop guessing capacity" - use Auto Scaling and elastic services
- Enables right-sizing and dynamic capacity adjustment
- Cost Optimization focuses on eliminating waste
- Reliability focuses on recovery and testing
- Operational Excellence focuses on running/monitoring

**References:** AWS Well-Architected Framework - Performance Efficiency Pillar
</details>

---

### Question 19
A company has multiple development teams that need separate AWS accounts for isolation. They want consolidated billing. What should they implement?

A. AWS Control Tower  
B. AWS Organizations with consolidated billing  
C. Multiple IAM users in one account  
D. AWS Resource Groups  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Organizations provides consolidated billing across multiple accounts
- Each team gets isolated account with separate resources
- Single bill for entire organization
- Control Tower helps set up Organizations but Organizations is the direct answer
- IAM users don't provide account-level isolation
- Resource Groups organize resources, not billing

**References:** AWS Organizations, Consolidated Billing
</details>

---

### Question 20
What is the primary purpose of Availability Zones within an AWS Region?

A. To provide different pricing tiers  
B. To enable fault tolerance and high availability  
C. To support different AWS services  
D. To reduce data transfer costs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Availability Zones are isolated locations within a Region
- Primary purpose: fault tolerance and high availability
- Each AZ has independent power, cooling, networking
- Deploying across AZs protects against single point of failure
- Not for pricing, service availability, or cost reduction
- Core purpose: resilience and availability

**References:** AWS Availability Zones, High Availability Architecture
</details>

---

## Summary

**Total Questions**: 20  
**Topics Covered**:
- AWS Global Infrastructure (Regions, AZs, Edge Locations, Local Zones, Wavelength)
- AWS Well-Architected Framework (All 6 pillars)
- Shared Responsibility Model
- AWS Account Management (Organizations, Consolidated Billing)
- Cost Management Tools (Pricing Calculator, Budgets, Cost Explorer)
- Service Categories and Cloud Models

**Exam Tips**:
1. Understand the difference between Regions, AZs, Edge Locations, Local Zones, and Wavelength
2. Memorize the 6 pillars of Well-Architected Framework
3. Know what AWS vs Customer manages in Shared Responsibility Model
4. Understand when to use each cost management tool
5. Know AWS Organizations for multi-account management

**Next Steps**:
- Review incorrect answers
- Study referenced topics in main README
- Practice scenario-based questions
- Take module quiz to reinforce learning

