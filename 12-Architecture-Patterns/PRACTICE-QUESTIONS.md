# Architecture Patterns - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company needs to deploy a web application that can handle unpredictable traffic spikes and minimize operational overhead. The application should scale automatically and use a pay-per-use pricing model. Which architecture is MOST appropriate?

A. EC2 instances with Auto Scaling behind an ALB  
B. Serverless architecture with S3, CloudFront, API Gateway, Lambda, and DynamoDB  
C. ECS containers on EC2 instances  
D. EC2 instances with manual scaling  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Serverless architecture automatically scales and is pay-per-use
- S3/CloudFront for static content
- API Gateway/Lambda for compute (scales automatically)
- DynamoDB for database (on-demand capacity)
- Zero operational overhead for infrastructure
- Option A requires some management and continuous costs
- Option C requires container orchestration
- Option D requires manual intervention

**References:** Serverless Architecture, Auto Scaling
</details>

---

### Question 2
A solutions architect is designing a highly available application that must survive the failure of an entire Availability Zone. The RTO requirement is less than 5 minutes. Which pattern should be implemented?

A. Single AZ deployment with automated backups  
B. Multi-AZ deployment with Auto Scaling and Application Load Balancer  
C. Cross-region replication with manual failover  
D. Single region with daily snapshots  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Multi-AZ deployment provides automatic failover
- ALB distributes traffic across AZs and health checks instances
- Auto Scaling replaces failed instances automatically
- Meets < 5 minute RTO requirement
- Option A doesn't protect against AZ failure
- Option C has longer RTO (manual failover)
- Option D doesn't provide HA

**References:** Multi-AZ Architecture, High Availability
</details>

---

### Question 3
A company wants to implement a disaster recovery solution for their production database. They can tolerate a 1-hour data loss (RPO) and 4-hour recovery time (RTO). Which DR strategy is MOST cost-effective?

A. Multi-site active-active  
B. Warm standby  
C. Pilot light  
D. Backup and restore  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Pilot light maintains core services (like database replication)
- RPO: Minutes (database replication lag)
- RTO: Hours (time to scale up remaining services)
- More cost-effective than warm standby
- Meets the 1-hour RPO and 4-hour RTO requirements
- Multi-site is expensive and over-engineered
- Warm standby costs more than necessary
- Backup and restore may not meet RPO/RTO

**References:** Disaster Recovery Strategies, Pilot Light
</details>

---

### Question 4
An application experiences high database read load. The data is read frequently but rarely updated. Which caching strategy should be implemented to reduce database load?

A. Write-through caching  
B. Cache-aside (Lazy Loading) with ElastiCache  
C. Database connection pooling only  
D. Increase database instance size  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Cache-aside pattern is ideal for read-heavy workloads
- Application checks cache first, loads from DB if cache miss
- ElastiCache (Redis/Memcached) reduces database load
- Cost-effective solution
- Write-through is better for write-heavy workloads
- Connection pooling helps but doesn't cache data
- Scaling database is more expensive

**References:** Caching Strategies, ElastiCache
</details>

---

### Question 5
A company is building a microservices architecture and needs to decouple services to handle traffic spikes without losing messages. Which AWS service pattern should be used?

A. Direct API calls between services  
B. SQS queues between services  
C. Shared database between services  
D. File-based communication via S3  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- SQS provides loose coupling and buffering between services
- Messages are persisted, not lost during traffic spikes
- Services process at their own pace
- Standard microservices pattern
- Direct API calls create tight coupling
- Shared database violates microservices principles
- S3 file-based communication is inefficient for real-time

**References:** Microservices Architecture, SQS Decoupling
</details>

---

### Question 6
A solutions architect needs to design a system that processes events from multiple sources (S3, DynamoDB, custom applications) and routes them to different targets based on event content. Which service is MOST appropriate?

A. Amazon SQS  
B. Amazon SNS  
C. Amazon EventBridge  
D. AWS Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- EventBridge is an event bus for routing events
- Supports multiple sources including AWS services and custom apps
- Content-based filtering and routing
- Built-in integration with 90+ AWS services
- SQS is for point-to-point messaging
- SNS is for pub/sub but limited filtering
- Step Functions is for workflow orchestration

**References:** Event-Driven Architecture, EventBridge
</details>

---

### Question 7
A company wants to minimize costs for a batch processing workload that runs nightly and can tolerate interruptions. Which compute option should be used?

A. On-Demand EC2 instances  
B. Reserved Instances  
C. Spot Instances  
D. Dedicated Hosts  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Spot Instances can save up to 90% compared to On-Demand
- Batch processing is fault-tolerant (can handle interruptions)
- Can checkpoint progress and resume
- Most cost-effective for this use case
- On-Demand is more expensive
- Reserved requires 1-3 year commitment
- Dedicated Hosts are most expensive

**References:** Cost Optimization, Spot Instances
</details>

---

### Question 8
An application requires sub-millisecond latency for database queries. The data is accessed in a key-value pattern. Which database solution should be used?

A. Amazon RDS with read replicas  
B. DynamoDB with DAX (DynamoDB Accelerator)  
C. Amazon Aurora  
D. Amazon Redshift  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DAX provides microsecond latency for DynamoDB
- In-memory cache specifically for DynamoDB
- Key-value access pattern is perfect for DynamoDB
- Meets sub-millisecond requirement
- RDS/Aurora have millisecond latency
- Redshift is for analytics, not operational workloads

**References:** DynamoDB DAX, Low Latency
</details>

---

### Question 9
A global application needs to serve static content with the lowest possible latency worldwide. Which architecture should be implemented?

A. EC2 instances in multiple regions  
B. S3 with CloudFront distribution  
C. S3 with Cross-Region Replication  
D. ALB in multiple regions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudFront is a CDN with 400+ edge locations globally
- Caches content close to users worldwide
- S3 origin for static content
- Lowest latency for global distribution
- EC2 requires management and doesn't cache at edge
- CRR helps availability but doesn't reduce latency
- ALB doesn't provide edge caching

**References:** CloudFront, Global Architecture
</details>

---

### Question 10
A three-tier web application has presentation, application, and database tiers. The database contains sensitive customer data. How should the tiers be deployed for security?

A. All tiers in public subnets  
B. All tiers in private subnets  
C. Presentation in public, application and database in private subnets  
D. Presentation and application in public, database in private subnet  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Presentation tier (web servers) needs internet access - public subnet
- Application tier doesn't need direct internet access - private subnet
- Database tier must be isolated - private subnet
- Follows defense-in-depth security principle
- Application tier accesses internet via NAT Gateway
- Database has no internet access
- Minimizes attack surface

**References:** Three-Tier Architecture, Security Best Practices
</details>

---

### Question 11
A company needs to orchestrate a complex workflow with multiple Lambda functions, error handling, and retry logic. Which service should be used?

A. EventBridge  
B. SNS with Lambda subscriptions  
C. AWS Step Functions  
D. SQS with Lambda triggers  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Step Functions orchestrates workflows with state machines
- Built-in error handling and retry logic
- Visual workflow designer
- Integrates with Lambda and other AWS services
- Best for complex, multi-step workflows
- EventBridge routes events but doesn't orchestrate
- SNS/SQS don't provide workflow orchestration

**References:** Step Functions, Serverless Orchestration
</details>

---

### Question 12
An application deployed across multiple regions needs a database that supports multi-region writes with automatic conflict resolution. Which database should be used?

A. RDS with cross-region read replicas  
B. Aurora Global Database  
C. DynamoDB Global Tables  
D. Redshift with cross-region snapshots  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- DynamoDB Global Tables support multi-region active-active writes
- Automatic conflict resolution (last-writer-wins)
- Multi-master replication
- RDS replicas are read-only
- Aurora Global Database has one primary region for writes
- Redshift is for analytics, not multi-region writes

**References:** DynamoDB Global Tables, Multi-Region Architecture
</details>

---

### Question 13
A company wants to implement a pub/sub messaging pattern where multiple consumers receive the same message. Which service should be used?

A. Amazon SQS Standard Queue  
B. Amazon SQS FIFO Queue  
C. Amazon SNS  
D. Amazon Kinesis Data Streams  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- SNS is publish-subscribe messaging service
- One message published to topic, multiple subscribers receive it
- Fan-out pattern
- Classic pub/sub use case
- SQS is point-to-point (one consumer per message)
- Kinesis allows multiple consumers but is for streaming data

**References:** SNS, Pub/Sub Pattern
</details>

---

### Question 14
An application needs to process uploaded images: resize, apply filters, and update database. The processing can take several minutes. Which architecture ensures reliable processing?

A. API Gateway → Lambda (process synchronously)  
B. API Gateway → Lambda → S3 → Lambda (triggered by S3) → DynamoDB  
C. EC2 instances polling S3  
D. Upload directly to EC2 for processing  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Upload triggers first Lambda to save to S3
- S3 event triggers second Lambda for processing (asynchronous)
- Decoupled, reliable processing
- Lambda can run up to 15 minutes
- Option A: API Gateway has 29-second timeout
- Option C: Inefficient polling
- Option D: No auto-scaling, not serverless

**References:** Event-Driven Architecture, Asynchronous Processing
</details>

---

### Question 15
A financial application requires ACID transactions across multiple tables. The database must scale for read traffic. Which database solution should be used?

A. DynamoDB  
B. Amazon Aurora with Read Replicas  
C. Amazon Redshift  
D. ElastiCache  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Aurora supports ACID transactions (relational database)
- Read Replicas scale read traffic (up to 15 replicas)
- Better performance than standard RDS
- DynamoDB doesn't support traditional ACID across multiple items
- Redshift is for analytics, not transactional workloads
- ElastiCache is for caching, not primary database

**References:** Aurora, ACID Transactions
</details>

---

### Question 16
A company needs to ensure their web application can handle a sudden 10x traffic increase during product launches. Which architectural pattern should be implemented?

A. Static capacity with manual scaling  
B. Auto Scaling with target tracking based on CPU utilization  
C. Pre-warming with scheduled scaling  
D. Serverless architecture with Lambda and DynamoDB on-demand  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- Serverless scales automatically without pre-warming
- Lambda scales to thousands of concurrent executions
- DynamoDB on-demand scales with traffic
- No capacity planning required
- Option A doesn't scale
- Option B has lag time for scaling
- Option C requires predicting launch time
- Serverless handles unpredictable spikes best

**References:** Serverless Architecture, Elastic Scaling
</details>

---

### Question 17
An application uses CloudFront, ALB, EC2, and RDS. Users in a specific region experience slow performance. What is the MOST likely cause and solution?

A. Increase EC2 instance size  
B. Deploy application stack in the user's region with Route 53 latency-based routing  
C. Enable CloudFront compression  
D. Upgrade to Provisioned IOPS for RDS  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Regional deployment reduces latency for local users
- Route 53 latency-based routing directs to nearest region
- CloudFront caches static content but dynamic content goes to origin
- Multi-region deployment needed for dynamic content
- Increasing instance size doesn't reduce network latency
- Compression helps but doesn't solve regional latency
- IOPS doesn't affect network latency

**References:** Multi-Region Architecture, Latency Optimization
</details>

---

### Question 18
A company wants to implement defense-in-depth security for their web application. Which combination of services should be used?

A. Security Groups only  
B. WAF + Shield + Security Groups + NACLs + KMS encryption  
C. IAM policies and Security Groups  
D. CloudFront with HTTPS only  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Defense-in-depth requires multiple security layers
- WAF: Application layer protection (OWASP Top 10)
- Shield: DDoS protection
- Security Groups: Instance-level firewall
- NACLs: Subnet-level firewall
- KMS: Data encryption
- Layered approach provides comprehensive security
- Single layer security is insufficient

**References:** Defense in Depth, Security Patterns
</details>

---

### Question 19
A batch processing application needs to read messages from a queue, process them, and only delete messages after successful processing. Which service and pattern should be used?

A. SNS with immediate deletion  
B. SQS with visibility timeout and explicit deletion  
C. Kinesis with checkpointing  
D. EventBridge with Lambda  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- SQS supports visibility timeout (hides message during processing)
- Message only deleted after explicit DeleteMessage call
- Ensures message not lost if processing fails
- If processing fails, message becomes visible again
- SNS doesn't persist messages
- Kinesis is for streaming, not queue pattern
- EventBridge doesn't provide message persistence

**References:** SQS, Message Processing Patterns
</details>

---

### Question 20
A company wants to optimize costs for a development environment that runs Monday-Friday, 9 AM-6 PM. The environment uses EC2, RDS, and NAT Gateway. What should be done?

A. Use Reserved Instances  
B. Use Instance Scheduler to start/stop resources outside business hours  
C. Migrate to Serverless  
D. Use Spot Instances  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Instance Scheduler automatically starts/stops resources on schedule
- Saves costs during nights and weekends (65% of week)
- Works with EC2 and RDS
- Reserved Instances require 1-3 year commitment, doesn't stop resources
- Serverless may not support all workloads
- Spot Instances can be interrupted during work hours
- Scheduled stop/start is most cost-effective for dev environments

**References:** Cost Optimization, Instance Scheduler
</details>

---

## Summary

### Key Concepts Tested:
1. **Serverless Architecture**: S3, CloudFront, API Gateway, Lambda, DynamoDB
2. **High Availability**: Multi-AZ, Auto Scaling, Load Balancing
3. **Disaster Recovery**: Backup & Restore, Pilot Light, Warm Standby, Multi-Site
4. **Microservices**: Service decoupling, SQS, SNS, EventBridge
5. **Caching**: CloudFront, API Gateway, ElastiCache, DAX
6. **Event-Driven**: EventBridge, SNS, SQS, Lambda triggers
7. **Cost Optimization**: Right-sizing, Spot, Reserved, Scheduling
8. **Security**: Defense-in-depth, multiple layers
9. **Three-Tier Architecture**: Public/private subnet placement
10. **Global Architecture**: Multi-region, CloudFront, Route 53

### Exam Tips:
- ✅ Multi-AZ for high availability within a region
- ✅ Multi-Region for disaster recovery and global performance
- ✅ Serverless minimizes operational overhead and costs
- ✅ Use SQS to decouple components and handle traffic spikes
- ✅ Caching at multiple layers reduces load and latency
- ✅ Spot Instances save up to 90% for fault-tolerant workloads
- ✅ Defense-in-depth requires multiple security layers
- ✅ Pilot Light for medium RPO/RTO at reasonable cost
- ✅ EventBridge for event routing, Step Functions for orchestration
- ✅ Private subnets for application and database tiers

