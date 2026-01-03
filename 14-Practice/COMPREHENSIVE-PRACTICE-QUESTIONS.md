# Comprehensive Practice Questions - Remaining Modules

## Security (Module 07)

### Question 1
A company wants to encrypt data at rest in S3 with full control over encryption keys including key rotation policy. Which encryption method should be used?

A. SSE-S3  
B. SSE-KMS with AWS managed keys  
C. SSE-KMS with customer managed keys (CMK)  
D. Client-side encryption  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **SSE-KMS with Customer Managed Keys (CMK)** provides full control
- Can create, rotate, disable keys
- Audit key usage with CloudTrail
- Granular access control

**Encryption Options Comparison**:
- **SSE-S3**: AWS manages, simple, no control
- **SSE-KMS (AWS managed)**: AWS rotates, audit trail
- **SSE-KMS (CMK)**: Full control, custom rotation
- **Client-side**: Encrypt before upload

**References:** AWS KMS, S3 Encryption
</details>

---

### Question 2
An application needs to securely store database credentials that can be automatically rotated. Which service should be used?

A. AWS Systems Manager Parameter Store  
B. AWS Secrets Manager  
C. AWS KMS  
D. S3 with encryption  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Secrets Manager** designed for secrets with automatic rotation
- Built-in rotation for RDS, DocumentDB, Redshift
- Versioning and audit trail

**Secrets Manager vs Parameter Store**:
| Feature | Secrets Manager | Parameter Store |
|---------|----------------|-----------------|
| **Rotation** | Automatic | Manual |
| **Cost** | Per secret + API calls | Free (Standard), charges (Advanced) |
| **Use Case** | DB credentials, API keys | Configuration, non-rotating |
| **Encryption** | KMS (required) | KMS (optional) |

**References:** AWS Secrets Manager, Secrets Management
</details>

---

## Application Integration (Module 08)

### Question 3
A microservices architecture needs asynchronous communication where multiple services can process the same message. Which service should be used?

A. Amazon SQS  
B. Amazon SNS  
C. Amazon EventBridge  
D. AWS Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon SNS** (Simple Notification Service) provides pub/sub messaging
- One message → multiple subscribers
- Push-based delivery
- Supports multiple protocols (SQS, Lambda, HTTP, Email, SMS)

**SNS vs SQS**:
| Feature | SNS | SQS |
|---------|-----|-----|
| **Pattern** | Pub/Sub (1-to-many) | Queue (1-to-1) |
| **Delivery** | Push | Pull |
| **Subscribers** | Multiple | Single consumer per message |

**Common Pattern**: SNS → Multiple SQS queues (fan-out)

**References:** Amazon SNS, Pub/Sub Messaging
</details>

---

### Question 4
An application needs to decouple components and handle message processing failures with retry logic. Messages should be processed exactly once. Which service and feature should be used?

A. Amazon SQS Standard Queue  
B. Amazon SQS FIFO Queue  
C. Amazon SNS  
D. Amazon Kinesis  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **SQS FIFO Queue** provides exactly-once processing
- Ordered message delivery
- Deduplication based on deduplication ID
- 300 messages/second (3000 with batching)

**SQS Standard vs FIFO**:
| Feature | Standard | FIFO |
|---------|----------|------|
| **Ordering** | Best-effort | Guaranteed |
| **Delivery** | At-least-once | Exactly-once |
| **Throughput** | Unlimited | 300/s (3000 batched) |
| **Deduplication** | No | Yes |

**FIFO Queue Features**:
- Message groups for parallel processing
- Content-based deduplication
- High throughput mode available

**References:** Amazon SQS FIFO, Message Queuing
</details>

---

### Question 5
A serverless application needs to process streaming data in real-time from thousands of IoT devices. Which service should be used?

A. Amazon SQS  
B. Amazon SNS  
C. Amazon Kinesis Data Streams  
D. AWS Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon Kinesis Data Streams** for real-time streaming data
- Handle massive data ingestion
- Multiple consumers can read same data
- Data retention (24 hours to 365 days)

**Kinesis Family**:
- **Data Streams**: Real-time streaming, custom processing
- **Data Firehose**: Load to S3, Redshift, Elasticsearch (easier)
- **Data Analytics**: SQL queries on streaming data
- **Video Streams**: Video streaming

**Kinesis vs SQS**:
- **Kinesis**: Real-time, multiple consumers, ordered
- **SQS**: Decoupling, single consumer per message

**References:** Amazon Kinesis, Stream Processing
</details>

---

## Monitoring and Logging (Module 09)

### Question 6
A company wants to monitor CPU utilization of EC2 instances and trigger Auto Scaling when CPU exceeds 70%. Which service provides this capability?

A. AWS CloudTrail  
B. Amazon CloudWatch  
C. AWS Config  
D. AWS X-Ray  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon CloudWatch** monitors AWS resources and applications
- Metrics, alarms, dashboards, logs
- Triggers Auto Scaling policies
- Default and custom metrics

**CloudWatch Components**:
- **Metrics**: CPU, network, disk, custom
- **Alarms**: Trigger actions based on thresholds
- **Logs**: Centralized log management
- **Events/EventBridge**: Event-driven automation
- **Dashboards**: Visualization

**Monitoring Services**:
- **CloudWatch**: Performance metrics, logs
- **CloudTrail**: API call auditing
- **Config**: Resource configuration changes
- **X-Ray**: Application tracing

**References:** Amazon CloudWatch, Monitoring
</details>

---

### Question 7
A company needs to track all API calls made in their AWS account for security auditing. Which service should be enabled?

A. Amazon CloudWatch Logs  
B. AWS CloudTrail  
C. AWS Config  
D. VPC Flow Logs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS CloudTrail** records API calls and events
- Who, what, when, where
- Enables governance, compliance, auditing
- Stores in S3, integrates with CloudWatch Logs

**CloudTrail Features**:
- Management events (control plane operations)
- Data events (S3 object operations, Lambda invocations)
- Insights events (unusual activity detection)
- Multi-region, multi-account support
- Log file integrity validation

**Use Cases**:
- Security analysis
- Troubleshooting
- Compliance auditing
- Operational troubleshooting

**References:** AWS CloudTrail, API Auditing
</details>

---

### Question 8
A company wants to ensure all EC2 instances have required tags and are using approved AMIs. Which service can continuously check compliance?

A. AWS CloudTrail  
B. Amazon CloudWatch  
C. AWS Config  
D. AWS Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Config** tracks resource configurations and compliance
- Continuously evaluates against rules
- Configuration history and change tracking
- Automated compliance checking

**AWS Config Features**:
- **Config Rules**: Managed or custom compliance rules
- **Remediation**: Automatic or manual fixes (SSM Automation)
- **Conformance Packs**: Grouped compliance rules
- **Multi-account/region aggregation**

**Common Config Rules**:
- Required tags
- Approved AMIs
- Encrypted volumes
- Security group rules
- Resource relationships

**References:** AWS Config, Compliance Monitoring
</details>

---

## Architecture Patterns (Module 12)

### Question 9
A company wants to implement a disaster recovery strategy with minimal cost. They can tolerate hours of downtime and some data loss. Which strategy should they use?

A. Backup and Restore  
B. Pilot Light  
C. Warm Standby  
D. Multi-Site Active-Active  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
**DR Strategies (Cost → Capability)**:

| Strategy | RTO | RPO | Cost | Readiness |
|----------|-----|-----|------|-----------|
| **Backup & Restore** | Hours/Days | Hours | Lowest | Backups only |
| **Pilot Light** | 10s mins | Minutes | Low | Minimal infrastructure |
| **Warm Standby** | Minutes | Seconds | Medium | Scaled-down environment |
| **Multi-Site** | Real-time | None/Minimal | Highest | Full environment |

**Backup and Restore**:
- Regular backups to S3/Glacier
- Restore when disaster occurs
- Lowest cost, highest RTO/RPO

**References:** Disaster Recovery Strategies, Business Continuity
</details>

---

### Question 10
An application should serve traffic from multiple AWS regions with automatic failover if a region becomes unavailable. What should be implemented?

A. Route 53 Geolocation Routing  
B. Route 53 Failover Routing with Health Checks  
C. CloudFront with multiple origins  
D. Global Accelerator  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Route 53 Failover Routing** provides active-passive failover
- Health checks monitor primary
- Automatically routes to secondary if primary fails

**Failover Configuration**:
- **Primary**: Active region
- **Secondary**: Standby region (or multiple secondaries)
- **Health Checks**: Monitor endpoint availability

**Multi-Region HA Patterns**:
1. Route 53 Failover (active-passive)
2. Route 53 Geoproximity/Latency (active-active)
3. Global Accelerator (anycast IPs)
4. CloudFront with origin failover

**References:** Route 53 Failover, Multi-Region Architecture
</details>

---

## Cost Optimization (Module 13)

### Question 11
A company has steady-state workloads running 24/7. What is the MOST cost-effective EC2 pricing option?

A. On-Demand Instances  
B. Reserved Instances (1 or 3 year)  
C. Savings Plans  
D. Spot Instances  

<details>
<summary>Show Answer</summary>

**Answer: B or C**

**Explanation:**
For steady-state, both are cost-effective:

**Reserved Instances**:
- Up to 72% discount
- 1 or 3 year commitment
- Specific instance type/region

**Compute Savings Plans**:
- Up to 66% discount
- Flexible (instance family, size, OS, tenancy)
- 1 or 3 year commitment

**Recommendation**: 
- **Savings Plans**: More flexibility
- **Reserved**: Slightly higher discount, less flexibility

**Cost Optimization Strategies**:
1. Reserved/Savings Plans for baseline
2. Spot for flexible workloads
3. On-Demand for peak/unpredictable

**References:** EC2 Pricing, Reserved Instances, Savings Plans
</details>

---

### Question 12
A company wants visibility into their AWS spending and cost allocation by project and department. What should be implemented?

A. AWS Budgets  
B. Cost Allocation Tags  
C. AWS Cost Explorer  
D. AWS Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Cost Allocation Tags** enable cost tracking by category
- Tag resources with Project, Department, Environment
- View costs grouped by tags in Cost Explorer

**Cost Management Tools**:

| Tool | Purpose |
|------|---------|
| **Cost Allocation Tags** | Categorize costs |
| **Cost Explorer** | Visualize and analyze costs |
| **AWS Budgets** | Set budget alerts |
| **Trusted Advisor** | Cost optimization recommendations |
| **Compute Optimizer** | Right-sizing recommendations |

**Best Practices**:
1. Define tagging strategy
2. Enforce tags (Tag Policies, SCPs)
3. Activate tags in billing
4. Regular cost reviews

**References:** Cost Allocation Tags, Cost Management
</details>

---

### Question 13
An application has variable workloads. The company wants AWS to recommend instance types to reduce costs. Which service provides these recommendations?

A. AWS Cost Explorer  
B. AWS Trusted Advisor  
C. AWS Compute Optimizer  
D. AWS Budgets  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Compute Optimizer** provides ML-based recommendations
- Right-sizing for EC2, Lambda, EBS, Auto Scaling
- Analyzes utilization patterns
- Recommends optimal instance types

**Compute Optimizer Benefits**:
- Up to 25% cost savings
- Performance improvements
- Historical utilization analysis (14 days default)
- EC2, Lambda function, EBS, ASG recommendations

**Optimization Tools**:
- **Compute Optimizer**: Resource right-sizing
- **Trusted Advisor**: Best practices, including cost
- **Cost Explorer**: Analyze spending, rightsizing recommendations

**References:** AWS Compute Optimizer, Right-Sizing
</details>

---

### Question 14
A company wants to reduce S3 costs for infrequently accessed data that doesn't have predictable access patterns. Which storage class should be used?

A. S3 Standard-IA  
B. S3 One Zone-IA  
C. S3 Intelligent-Tiering  
D. S3 Glacier  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **S3 Intelligent-Tiering** automatically optimizes costs
- Moves data between access tiers based on patterns
- No retrieval fees (unlike IA classes)
- Small monthly monitoring fee

**When to Use**:
- Unknown or changing access patterns
- Want automatic optimization
- Avoid manual lifecycle management

**Cost Optimization**:
- **Predictable patterns**: Use Lifecycle policies
- **Unpredictable patterns**: Use Intelligent-Tiering

**References:** S3 Intelligent-Tiering, S3 Cost Optimization
</details>

---

### Question 15
A company wants to receive alerts when monthly AWS costs are forecasted to exceed $10,000. Which service should be configured?

A. CloudWatch Alarms  
B. AWS Budgets  
C. Cost Explorer  
D. Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Budgets** sets custom cost and usage budgets
- Alerts via SNS when exceeded or forecasted to exceed
- Supports cost, usage, reservation, Savings Plans budgets

**Budget Types**:
- **Cost Budget**: Track spending
- **Usage Budget**: Track resource usage
- **RI/Savings Plans Utilization**: Track commitment utilization
- **RI/Savings Plans Coverage**: Track coverage percentage

**Budget Features**:
- Forecasted costs
- Multiple alert thresholds
- SNS notifications
- Budget actions (automated responses)

**References:** AWS Budgets, Cost Alerts
</details>

---

## Additional Cross-Domain Questions

### Question 16
A company stores sensitive data in S3 and needs to ensure objects cannot be deleted for 7 years for regulatory compliance. What should be configured?

A. S3 Versioning  
B. S3 Object Lock in Compliance Mode  
C. MFA Delete  
D. S3 Glacier Vault Lock  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Object Lock (Compliance Mode)** enforces WORM
- Cannot be overridden by anyone, including root
- Retention period enforced
- Perfect for regulatory compliance

**Object Lock Modes**:
- **Compliance**: Immutable, even root can't delete
- **Governance**: Special permissions can override

**Related Features**:
- **Versioning**: Must be enabled
- **Legal Hold**: Indefinite protection
- **Glacier Vault Lock**: Similar for Glacier

**References:** S3 Object Lock, Compliance
</details>

---

### Question 17
An application needs to send emails to customers. Which AWS service should be used?

A. Amazon SNS  
B. Amazon SES  
C. Amazon SQS  
D. Amazon Pinpoint  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon SES** (Simple Email Service) for sending emails
- Bulk and transactional emails
- High deliverability
- Cost-effective

**Email Services**:
- **SES**: Send emails (marketing, transactional)
- **SNS**: Notifications (SMS, email, push)
- **Pinpoint**: Multi-channel marketing campaigns

**SES Features**:
- Send/receive emails
- Template support
- Analytics and insights
- Reputation dashboard

**References:** Amazon SES, Email Services
</details>

---

### Question 18
A Lambda function needs to process records from a DynamoDB table whenever items are modified. How should this be implemented?

A. Lambda polls DynamoDB table  
B. DynamoDB Streams + Lambda Event Source Mapping  
C. CloudWatch Events triggers Lambda  
D. SNS topic triggers Lambda  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **DynamoDB Streams** captures item-level changes
- **Lambda Event Source Mapping** polls stream and invokes Lambda
- Near real-time processing
- Exactly-once processing per shard

**Event Source Mapping**:
- Lambda polls stream
- Batches records
- Invokes Lambda function
- Handles retries

**Use Cases**:
- Update search indexes
- Send notifications
- Audit logging
- Cross-region replication

**References:** DynamoDB Streams, Lambda Event Sources
</details>

---

### Question 19
A company wants to analyze application logs to identify security threats. Which service should be used?

A. Amazon CloudWatch Logs  
B. AWS CloudTrail  
C. Amazon GuardDuty  
D. AWS Security Hub  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon GuardDuty** provides intelligent threat detection
- Analyzes CloudTrail, VPC Flow Logs, DNS logs
- Machine learning for anomaly detection
- No agents or infrastructure required

**GuardDuty Features**:
- Automated threat detection
- Cryptocurrency mining detection
- Compromised instance detection
- Reconnaissance detection
- Integration with Security Hub, EventBridge

**Security Services**:
- **GuardDuty**: Threat detection
- **Security Hub**: Centralized security findings
- **Inspector**: Vulnerability scanning
- **Macie**: Data privacy/protection (PII detection)

**References:** Amazon GuardDuty, Threat Detection
</details>

---

### Question 20
A web application experiences slow database queries. The company wants to identify which queries are causing the issue. Which AWS service can help?

A. Amazon CloudWatch  
B. AWS X-Ray  
C. AWS CloudTrail  
D. VPC Flow Logs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS X-Ray** provides distributed tracing
- Analyze and debug applications
- Identify performance bottlenecks
- Service map visualization

**X-Ray Features**:
- Request tracing end-to-end
- Service map (dependencies)
- Latency analysis
- Error and exception tracking
- Annotations and metadata

**X-Ray Integration**:
- Lambda, ECS, Elastic Beanstalk, API Gateway
- Application code instrumentation
- SQL query tracing

**Debugging Tools**:
- **X-Ray**: Application performance, tracing
- **CloudWatch**: Metrics and logs
- **RDS Performance Insights**: Database queries

**References:** AWS X-Ray, Application Tracing
</details>

---

## Summary

**Modules Covered**: Security, Application Integration, Monitoring, Architecture Patterns, Cost Optimization, and Cross-Domain Scenarios

**Key Takeaways**:

**Security**:
- **Secrets Manager**: Auto-rotation
- **KMS CMK**: Full key control
- **CloudTrail**: API auditing
- **GuardDuty**: Threat detection

**Application Integration**:
- **SNS**: Pub/Sub (1-to-many)
- **SQS**: Queue, decoupling
- **SQS FIFO**: Exactly-once, ordered
- **Kinesis**: Real-time streaming
- **EventBridge**: Event routing

**Monitoring**:
- **CloudWatch**: Metrics, logs, alarms
- **CloudTrail**: API calls
- **Config**: Compliance, configuration
- **X-Ray**: Application tracing

**Cost Optimization**:
- **Reserved/Savings Plans**: Steady workloads
- **Spot**: Flexible workloads
- **Budgets**: Cost alerts
- **Compute Optimizer**: Right-sizing

**Architecture**:
- **DR Strategies**: Backup, Pilot Light, Warm Standby, Multi-Site
- **Multi-Region**: Route 53 Failover, Global Accelerator

**Exam Tips**:
1. Know when to use each messaging service
2. Understand DR strategy trade-offs
3. Remember cost optimization tools and their purposes
4. Know monitoring services and what they track
5. Understand security services and their use cases

---

## Complete Module Coverage Checklist

✅ **Module 01**: AWS Fundamentals (20 questions)  
✅ **Module 02**: IAM (20 questions)  
✅ **Module 03**: Compute (20 questions)  
✅ **Module 04**: Storage (20 questions)  
✅ **Module 05**: Database (20 questions)  
✅ **Module 06**: Networking (20 questions)  
✅ **Module 07**: Security (included above)  
✅ **Module 08**: Application Integration (included above)  
✅ **Module 09**: Monitoring (included above)  
✅ **Module 12**: Architecture Patterns (included above)  
✅ **Module 13**: Cost Optimization (included above)  

**Total Practice Questions Created**: 140+ Questions

**Next Steps**:
1. Review all module questions
2. Take full-length mock exams
3. Focus on weak areas
4. Practice scenario-based questions
5. Review AWS whitepapers and FAQs

