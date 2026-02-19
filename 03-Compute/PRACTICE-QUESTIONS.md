# Compute Services - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company needs to run a batch processing job that can tolerate interruptions and must minimize costs. Which EC2 pricing model should be used?

A. On-Demand Instances  
B. Reserved Instances  
C. Spot Instances  
D. Dedicated Hosts  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Spot Instances offer up to 90% discount compared to On-Demand
- Can be interrupted with 2-minute warning when AWS needs capacity
- Perfect for fault-tolerant, flexible workloads
- **Ideal Use Cases**: Batch jobs, data analysis, image processing, CI/CD
- Option A: On-Demand is most expensive
- Option B: Reserved requires 1-3 year commitment
- Option D: Dedicated Hosts are most expensive, for compliance

**Key Points**:
- Spot = Cheapest, can be interrupted
- Best for: Stateless, fault-tolerant, flexible workloads

**References:** EC2 Pricing Models, Spot Instances
</details>

---

### Question 2
An application experiences predictable traffic spikes every Monday at 9 AM. What is the MOST cost-effective Auto Scaling approach?

A. Target Tracking Scaling  
B. Simple Scaling  
C. Step Scaling  
D. Scheduled Scaling  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- Scheduled Scaling scales based on predefined schedule
- Perfect for predictable traffic patterns
- Scales before traffic spike occurs (proactive)
- Most cost-effective for known patterns

**Schedule Example**:
```bash
aws autoscaling put-scheduled-update-group-action \
  --auto-scaling-group-name my-asg \
  --scheduled-action-name monday-morning-scale \
  --recurrence "0 8 * * MON" \
  --desired-capacity 10
```

- Option A: Target Tracking is reactive, scales after metric changes
- Option B/C: Step/Simple scaling are reactive
- **Scheduled = Proactive, Target/Step/Simple = Reactive**

**References:** Auto Scaling Policies, Scheduled Scaling
</details>

---

### Question 3
A web application requires high availability across multiple Availability Zones with automatic distribution of traffic. Which load balancer should be used for HTTP/HTTPS traffic with advanced routing?

A. Classic Load Balancer  
B. Application Load Balancer  
C. Network Load Balancer  
D. Gateway Load Balancer  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Application Load Balancer (ALB)** operates at Layer 7 (HTTP/HTTPS)
- Advanced routing: path-based, host-based, header-based
- WebSocket and HTTP/2 support
- Perfect for modern web applications

**ALB Features**:
- Path-based routing: `/api/*` → API servers, `/images/*` → image servers
- Host-based routing: `api.example.com` vs `www.example.com`
- Query string/header routing
- Fixed response, redirects
- AWS WAF integration
- Authentication (OIDC, Cognito)

**Load Balancer Comparison**:
- **CLB**: Legacy, Layer 4/7, basic
- **ALB**: Layer 7, HTTP/HTTPS, advanced routing
- **NLB**: Layer 4, TCP/UDP, ultra-high performance, static IP
- **GLB**: Layer 3, third-party virtual appliances

**References:** Application Load Balancer, ELB Types
</details>

---

### Question 4
A microservices application needs a load balancer that can handle millions of requests per second with ultra-low latency and static IP addresses. Which load balancer should be used?

A. Application Load Balancer  
B. Network Load Balancer  
C. Classic Load Balancer  
D. CloudFront  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Network Load Balancer (NLB)** operates at Layer 4 (TCP/UDP/TLS)
- Handles millions of requests per second
- Ultra-low latency (microseconds)
- Static IP addresses (one per AZ)
- Preserves source IP address

**NLB Use Cases**:
- Extreme performance requirements
- Static/Elastic IP needed (whitelist in firewalls)
- TCP/UDP traffic
- PrivateLink endpoints
- Game servers, IoT, real-time applications

**NLB vs ALB**:
- **NLB**: Layer 4, faster, static IP, TCP/UDP
- **ALB**: Layer 7, advanced routing, HTTP/HTTPS

**References:** Network Load Balancer, Layer 4 vs Layer 7
</details>

---

### Question 5
A company wants to run code in response to events without managing servers. The code should execute only when triggered and scale automatically. Which service should be used?

A. Amazon EC2 with Auto Scaling  
B. AWS Lambda  
C. Amazon ECS  
D. AWS Elastic Beanstalk  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Lambda** is serverless compute service
- Event-driven execution
- Automatic scaling (1 to 1000s of concurrent executions)
- Pay only for compute time (per millisecond)
- No server management

**Lambda Characteristics**:
- **Max execution time**: 15 minutes
- **Memory**: 128 MB to 10,240 MB
- **Deployment package**: 50 MB (zipped), 250 MB (unzipped)
- **Concurrent executions**: 1000 (default, can increase)
- **Billing**: Per request + compute time (GB-seconds)

**Lambda Triggers**:
- API Gateway (REST APIs)
- S3 events
- DynamoDB Streams
- EventBridge (scheduled/event-based)
- SNS, SQS
- Kinesis

**References:** AWS Lambda, Serverless Computing
</details>

---

### Question 6
An application running on EC2 instances experiences variable traffic and needs to maintain 50% average CPU utilization. What Auto Scaling policy should be configured?

A. Simple Scaling  
B. Step Scaling  
C. Target Tracking Scaling  
D. Predictive Scaling  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Target Tracking Scaling** automatically adjusts capacity to maintain target metric
- Specify target value (e.g., 50% CPU), Auto Scaling does the rest
- Easiest to configure and manage
- Creates and manages CloudWatch alarms automatically

**Configuration Example**:
```json
{
  "TargetValue": 50.0,
  "PredefinedMetricSpecification": {
    "PredefinedMetricType": "ASGAverageCPUUtilization"
  }
}
```

**Predefined Metrics**:
- `ASGAverageCPUUtilization`
- `ASGAverageNetworkIn`
- `ASGAverageNetworkOut`
- `ALBRequestCountPerTarget`

**Scaling Policy Types**:
- **Target Tracking**: Maintain specific metric value (EASIEST)
- **Step**: Add/remove capacity based on CloudWatch alarm thresholds
- **Simple**: Single scaling adjustment (legacy)
- **Predictive**: ML-based forecasting

**References:** Target Tracking Scaling, Auto Scaling Policies
</details>

---

### Question 7
A company needs to run Docker containers without managing EC2 instances. Which service should be used?

A. Amazon ECS with EC2 launch type  
B. Amazon ECS with Fargate launch type  
C. Amazon EKS  
D. AWS Elastic Beanstalk  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Fargate** is serverless container platform
- No EC2 instance management required
- Pay for vCPU and memory resources used
- Works with both ECS and EKS

**Container Service Options**:

| Service | Description | Management |
|---------|-------------|------------|
| **ECS + EC2** | Container orchestration on EC2 | Manage instances |
| **ECS + Fargate** | Serverless containers | No instance management |
| **EKS + EC2** | Kubernetes on EC2 | Manage instances + K8s |
| **EKS + Fargate** | Serverless Kubernetes | No instance management |

**Fargate Benefits**:
- No instance provisioning/scaling
- No patching/securing instances
- Pay per task
- Simpler operations

**When to use Fargate vs EC2**:
- **Fargate**: Simplicity, less operational overhead
- **EC2**: Need specific instance types, GPU, cost optimization for sustained workloads

**References:** AWS Fargate, Amazon ECS
</details>

---

### Question 8
An EC2 instance needs low-latency, high-throughput connectivity to other instances in the same cluster. Which placement group should be used?

A. Cluster Placement Group  
B. Spread Placement Group  
C. Partition Placement Group  
D. No placement group needed  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **Cluster Placement Group** places instances close together in single AZ
- Low-latency network (10 Gbps between instances)
- High throughput, enhanced networking
- All instances in same rack/physical proximity

**Placement Group Types**:

| Type | Purpose | AZ | Max Instances |
|------|---------|----|----|
| **Cluster** | Low latency, high throughput | Single AZ | Limited by instance type |
| **Spread** | Reduce correlated failures | Multi-AZ | 7 per AZ |
| **Partition** | Large distributed workloads | Multi-AZ | 7 partitions per AZ |

**Use Cases**:
- **Cluster**: HPC, big data, low-latency apps
- **Spread**: Critical applications (each instance separate rack)
- **Partition**: Hadoop, Cassandra, Kafka (partition = rack)

**Limitations**:
- Cluster: Single AZ only
- Spread: Max 7 instances per AZ
- Not all instance types supported

**References:** EC2 Placement Groups
</details>

---

### Question 9
A company wants to deploy a web application with automatic scaling, load balancing, and health monitoring without managing infrastructure. Which service should be used?

A. AWS Lambda  
B. Amazon EC2 with Auto Scaling  
C. AWS Elastic Beanstalk  
D. Amazon Lightsail  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Elastic Beanstalk** is PaaS (Platform as a Service)
- Upload code, Beanstalk handles deployment
- Automatic provisioning: EC2, ALB, Auto Scaling, RDS, monitoring
- Multiple platforms: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker

**Elastic Beanstalk Features**:
- Automatic capacity provisioning
- Load balancing
- Auto Scaling
- Health monitoring
- Platform updates
- Still have full control over resources (not completely abstracted)

**Deployment Options**:
- **All at once**: Fastest, downtime
- **Rolling**: Partial batches, reduced capacity
- **Rolling with additional batch**: Maintains full capacity
- **Immutable**: New instances, safest
- **Blue/Green**: Manual via swap URLs

**Beanstalk vs Others**:
- **Lambda**: Functions, not full applications
- **EC2 + Auto Scaling**: More manual configuration
- **Lightsail**: Simpler, less scalable

**References:** AWS Elastic Beanstalk, PaaS
</details>

---

### Question 10
An application requires guaranteed capacity reservation for EC2 instances in a specific Availability Zone without long-term commitment. Which option should be used?

A. Reserved Instances  
B. Savings Plans  
C. On-Demand Capacity Reservations  
D. Spot Instances  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **On-Demand Capacity Reservations** reserve capacity in specific AZ
- No long-term commitment (can cancel anytime)
- Charged at On-Demand rates whether used or not
- Ensures capacity availability when needed

**Capacity Options Comparison**:

| Option | Commitment | Discount | Capacity Guarantee |
|--------|------------|----------|-------------------|
| **On-Demand** | None | None | No guarantee |
| **Reserved** | 1-3 years | Up to 72% | Yes (regional or zonal) |
| **Savings Plans** | 1-3 years | Up to 66% | No |
| **Capacity Reservations** | None | None | Yes (zonal) |
| **Spot** | None | Up to 90% | No (can be interrupted) |

**Use Case**:
- Disaster recovery (reserve capacity but don't always run)
- Business-critical events (Black Friday)
- Regulatory/compliance requirements

**Cost Optimization**: Combine Capacity Reservation with Savings Plan

**References:** On-Demand Capacity Reservations
</details>

---

### Question 11
A Lambda function is timing out after 3 seconds when processing large files. What should be changed?

A. Increase Lambda memory allocation  
B. Increase Lambda timeout setting  
C. Use Lambda layers  
D. Switch to EC2  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Lambda default timeout is 3 seconds
- Can be increased up to 15 minutes (900 seconds)
- Timeout configuration is separate from memory

**Lambda Configuration**:
- **Memory**: 128 MB to 10,240 MB (10 GB)
- **Timeout**: 1 second to 900 seconds (15 minutes)
- **CPU scales with memory** (1,792 MB = 1 vCPU)
- **Ephemeral storage (/tmp)**: 512 MB to 10,240 MB

**Performance Tuning**:
1. Increase timeout for long-running tasks
2. Increase memory if CPU-bound (CPU scales with memory)
3. Optimize code
4. Use async patterns for very long tasks

**When Lambda is NOT suitable**:
- Tasks > 15 minutes
- Need GPU
- Stateful applications
- Real-time latency requirements (cold starts)

**References:** Lambda Configuration, Lambda Limits
</details>

---

### Question 12
A company wants to run EC2 instances with dedicated physical servers for compliance requirements. Which option should be used?

A. Dedicated Instances  
B. Dedicated Hosts  
C. Reserved Instances  
D. Spot Instances  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Dedicated Hosts**: Physical server dedicated to your use
- Visibility into sockets, cores, host ID
- Support for BYOL (Bring Your Own License) - Windows Server, SQL Server
- Meet compliance requirements
- Most expensive option

**Dedicated Instances vs Dedicated Hosts**:

| Feature | Dedicated Instances | Dedicated Hosts |
|---------|-------------------|----------------|
| **Isolation** | Instance-level | Physical server |
| **Visibility** | No hardware visibility | Socket/core visibility |
| **BYOL** | Not supported | Supported |
| **Placement** | Automatic | Control placement |
| **Billing** | Per instance | Per host |
| **Use Case** | Compliance (soft requirement) | BYOL, compliance (strict) |

**Use Cases for Dedicated Hosts**:
- Server-bound software licenses
- Regulatory compliance
- Track physical host usage

**References:** Dedicated Hosts, Dedicated Instances, BYOL
</details>

---

### Question 13
An Auto Scaling group has 10 instances. An administrator manually terminates 3 instances. What happens next?

A. Auto Scaling terminates 3 more instances  
B. Auto Scaling launches 3 new instances  
C. Auto Scaling does nothing  
D. Auto Scaling sends an alert  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Auto Scaling maintains desired capacity
- If instances are terminated (manually or automatically), ASG replaces them
- Ensures desired count is maintained

**Auto Scaling Group Configuration**:
- **Minimum**: Minimum number of instances
- **Desired**: Target number of instances
- **Maximum**: Maximum number of instances

**Scaling Activities**:
- Scale out: Launch instances (desired < current)
- Scale in: Terminate instances (desired > current)
- Replace unhealthy: Terminate and replace
- Rebalance across AZs

**Instance Protection**:
- Can enable scale-in protection on specific instances
- Prevents Auto Scaling from terminating protected instances
- Manual termination still works

**References:** Auto Scaling Groups, Desired Capacity
</details>

---

### Question 14
A batch processing application uses Lambda functions but needs to coordinate multiple steps with error handling and retries. Which service should be used?

A. Amazon SQS  
B. Amazon SNS  
C. AWS Step Functions  
D. Amazon EventBridge  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Step Functions** orchestrates serverless workflows
- Coordinate multiple Lambda functions
- Built-in error handling, retries, parallel execution
- Visual workflow designer

**Step Functions Features**:
- **State machine**: Define workflow as states
- **Error handling**: Catch errors, retry logic
- **Parallel execution**: Run steps concurrently
- **Wait states**: Delays between steps
- **Choice states**: Conditional logic
- **Map states**: Iterate over arrays

**Workflow Types**:
- **Standard**: Long-running (up to 1 year), exactly-once execution
- **Express**: Short-lived (5 min), at-least-once, high-rate

**Use Cases**:
- ETL pipelines
- Order processing
- Video processing
- Machine learning workflows

**Step Functions vs Alternatives**:
- **SQS**: Message queue, no orchestration
- **SNS**: Pub/sub messaging, no orchestration
- **EventBridge**: Event routing, simpler workflows

**References:** AWS Step Functions, Serverless Orchestration
</details>

---

### Question 15
An application needs consistent performance with baseline CPU and ability to burst above baseline when needed. Which EC2 instance type should be used?

A. M5 (General Purpose)  
B. C5 (Compute Optimized)  
C. T3 (Burstable Performance)  
D. R5 (Memory Optimized)  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **T3/T4g instances** are burstable performance instances
- Baseline CPU performance with credit system
- Accumulate CPU credits when below baseline
- Burst above baseline using credits
- Cost-effective for variable workloads

**T3 CPU Credits**:
- Baseline performance depends on instance size
- Earn credits when CPU < baseline
- Spend credits when CPU > baseline
- **Unlimited mode**: Can burst beyond credits (additional charges)

**T3 Instance Types**:
- t3.nano: 5% baseline
- t3.micro: 10% baseline
- t3.small: 20% baseline
- t3.medium: 20% baseline
- t3.large: 30% baseline

**Use Cases**:
- Web servers, dev/test
- Small databases
- Code repositories
- Microservices

**When NOT to use T3**:
- Sustained high CPU usage
- Predictable high performance needs
- Use C5/M5 for sustained performance

**References:** T3 Instances, Burstable Performance, CPU Credits
</details>

---

### Question 16
A company wants to deploy containerized applications using Kubernetes without managing the control plane. Which service should be used?

A. Amazon ECS  
B. Amazon EKS  
C. AWS Fargate  
D. AWS Elastic Beanstalk  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon EKS** (Elastic Kubernetes Service) is managed Kubernetes
- AWS manages Kubernetes control plane
- Compatible with standard Kubernetes tools (kubectl, Helm)
- Multi-AZ control plane for high availability

**EKS Features**:
- Managed K8s control plane (etcd, API server)
- Automatic upgrades and patches
- Integrate with AWS services (IAM, VPC, ALB, CloudWatch)
- CNCF certified (standard Kubernetes)

**EKS Worker Nodes Options**:
- **Self-managed nodes**: You manage EC2 instances
- **Managed node groups**: AWS manages EC2 lifecycle
- **Fargate**: Serverless, no node management

**ECS vs EKS**:
- **ECS**: AWS-proprietary, simpler, tight AWS integration
- **EKS**: Standard Kubernetes, portable, more complex, existing K8s expertise

**When to use EKS**:
- Existing Kubernetes workloads
- Kubernetes expertise in team
- Multi-cloud/hybrid requirements
- Standard Kubernetes tools needed

**References:** Amazon EKS, Kubernetes on AWS
</details>

---

### Question 17
An Auto Scaling group needs to ensure that newly launched instances are ready to serve traffic before receiving requests. What should be configured?

A. EC2 Status Checks  
B. ELB Health Checks  
C. Auto Scaling Health Check Grace Period  
D. CloudWatch Alarms  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Health Check Grace Period** gives instances time to boot and pass checks
- Prevents premature termination during initialization
- Default: 300 seconds (5 minutes)
- Should be longer than application startup time

**Auto Scaling Health Checks**:
- **EC2 health check**: Instance running (default)
- **ELB health check**: Instance passes load balancer health checks
- Grace period applies to both types

**Recommended Configuration**:
1. Set grace period > application startup time
2. Enable ELB health checks
3. Configure ELB health check with appropriate interval/threshold

**Example**:
```bash
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --health-check-type ELB \
  --health-check-grace-period 600  # 10 minutes
```

**References:** Auto Scaling Health Checks, Grace Period
</details>

---

### Question 18
A company wants to migrate lift-and-shift Windows applications to AWS without refactoring. Which compute option is MOST appropriate?

A. AWS Lambda  
B. Amazon ECS  
C. Amazon EC2  
D. AWS Fargate  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon EC2** for lift-and-shift migrations
- Run Windows Server, install applications as-is
- Minimal refactoring required
- Full control over OS and configuration

**Migration Strategies (6 R's)**:
1. **Rehost (Lift-and-Shift)**: Move as-is to EC2
2. **Replatform (Lift-Tinker-Shift)**: Minor optimizations
3. **Repurchase**: Move to SaaS
4. **Refactor/Re-architect**: Redesign for cloud-native
5. **Retire**: Decommission
6. **Retain**: Keep on-premises

**Lift-and-Shift Approach**:
- Quick migration
- Minimal risk
- Can optimize later
- Use AWS Application Migration Service (MGN)

**Other Options Not Suitable**:
- Lambda: Requires code changes, event-driven
- ECS/Fargate: Requires containerization
- EC2 is best for "as-is" Windows applications

**References:** Migration Strategies, EC2 for Windows
</details>

---

### Question 19
An application running on Lambda is invoked by S3 events. During peak times, thousands of files are uploaded simultaneously. How should Lambda handle this?

A. Increase Lambda memory  
B. Enable Lambda reserved concurrency  
C. Lambda automatically scales concurrently  
D. Use Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Lambda automatically scales to handle concurrent invocations
- Each S3 event triggers separate Lambda invocation
- Default account concurrency: 1000 (can request increase)
- No configuration needed for basic scaling

**Lambda Concurrency Types**:
- **Account concurrency**: Total concurrent executions across all functions (1000 default)
- **Reserved concurrency**: Dedicated concurrency for specific function
- **Provisioned concurrency**: Pre-initialized instances (reduce cold starts)

**When to use Reserved Concurrency**:
- Limit function concurrency (prevent overwhelming downstream)
- Guarantee concurrency for critical functions
- Prevent one function from consuming all account concurrency

**Example Scenario**:
- 1000 files uploaded to S3
- Lambda invoked 1000 times concurrently (within account limits)
- If account limit is 1000, all execute immediately
- If limit exceeded, some invocations throttled (429 error)

**References:** Lambda Concurrency, Automatic Scaling
</details>

---

### Question 20
A web application needs to maintain session state. The application runs on multiple EC2 instances behind an Application Load Balancer. How should session state be managed?

A. Store session data on EC2 instance local storage  
B. Enable sticky sessions on ALB  
C. Store session data in Amazon ElastiCache or DynamoDB  
D. Use NLB instead of ALB  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **External session storage** (ElastiCache/DynamoDB) is best practice
- Sessions accessible from any instance
- Survives instance failures
- True stateless architecture

**Session Management Options**:

| Option | Pros | Cons |
|--------|------|------|
| **ElastiCache/DynamoDB** | Stateless, scalable, resilient | Additional service |
| **Sticky Sessions** | Simple | Uneven load, not resilient |
| **Local Storage** | Fast | Lost on instance failure |

**Why ElastiCache/DynamoDB is Better**:
- ✅ Any instance can serve any request
- ✅ Auto Scaling works properly
- ✅ Instance failure doesn't lose sessions
- ✅ Better load distribution

**Sticky Sessions Issues**:
- Uneven instance utilization
- New instances get no traffic initially
- Instance failure = lost sessions
- Use only if refactoring is not possible

**References:** Stateless Architecture, Session Management, ElastiCache
</details>

---

### Question 21
A company needs to run AWS services in its own data center to meet strict data residency requirements, while maintaining a consistent hybrid cloud experience. Which AWS service should they use?

A. AWS Outposts  
B. Amazon EC2 Dedicated Hosts  
C. AWS Snowball Edge  
D. AWS Direct Connect  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS Outposts brings native AWS services, infrastructure, and operating models to on-premises data centers
- Provides a consistent hybrid experience
- Supports EC2, EBS, RDS, ECS, EKS, S3, and more
- Dedicated Hosts are for compliance, not hybrid cloud
- Snowball Edge is for edge computing and data transfer, not full AWS services
- Direct Connect is for network connectivity, not running AWS services on-premises

**References:** AWS Outposts, Hybrid Cloud
</details>

---

### Question 22
A research organization needs to run large-scale, high-throughput batch jobs on AWS with automatic job scheduling and resource provisioning. Which service should they use?

A. AWS Batch  
B. Amazon EC2 Auto Scaling  
C. AWS Lambda  
D. Amazon EMR  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS Batch is a fully managed batch computing service
- Automatically provisions compute resources and schedules jobs
- Supports Docker containers and EC2/Spot/Fargate
- EC2 Auto Scaling is for scaling instances, not job scheduling
- Lambda is for short-lived, event-driven compute
- EMR is for big data processing, not general batch jobs

**References:** AWS Batch, Batch Computing
</details>

---

### Question 23
A development team wants to share and deploy serverless applications published by AWS and third parties. Which AWS service should they use?

A. AWS Serverless Application Repository  
B. AWS Marketplace  
C. AWS Lambda Layers  
D. AWS CloudFormation StackSets  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS Serverless Application Repository is a managed repository for serverless apps
- Allows sharing and deployment of Lambda-based applications
- Marketplace is for commercial software, not serverless apps
- Lambda Layers are for code sharing, not full applications
- CloudFormation StackSets is for multi-account deployments

**References:** AWS Serverless Application Repository, Serverless Deployment
</details>

---

### Question 24
A company wants to run VMware workloads on AWS with seamless integration and management using familiar VMware tools. Which solution should they use?

A. VMware Cloud on AWS  
B. AWS Outposts  
C. Amazon EC2 Dedicated Hosts  
D. AWS Snowball Edge  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- VMware Cloud on AWS integrates VMware vSphere, NSX, and vSAN with AWS infrastructure
- Enables seamless migration and hybrid operations
- Managed by both AWS and VMware
- Outposts is for running AWS services on-premises
- Dedicated Hosts are for compliance
- Snowball Edge is for edge computing

**References:** VMware Cloud on AWS, Hybrid VMware
</details>

---

### Question 25
A global enterprise needs to deploy AWS compute and storage services at the edge of mobile networks to deliver ultra-low latency applications. Which AWS service should they use?

A. AWS Wavelength  
B. AWS Outposts  
C. Amazon CloudFront  
D. AWS Direct Connect  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS Wavelength brings AWS services to the edge of 5G networks
- Enables ultra-low latency applications for mobile and edge devices
- Outposts is for on-premises data centers
- CloudFront is a CDN, not edge compute
- Direct Connect is for network connectivity

**References:** AWS Wavelength, Edge Computing
</details>

---

### Question 26
A company wants to run Amazon ECS and EKS workloads on its own infrastructure outside AWS, managed from the AWS Console. Which services should they use?

A. Amazon ECS Anywhere and Amazon EKS Anywhere  
B. AWS Outposts  
C. AWS Fargate  
D. Amazon EC2 Dedicated Hosts  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- ECS Anywhere and EKS Anywhere extend container orchestration to on-premises infrastructure
- Managed from AWS Console
- Outposts is for running AWS infrastructure on-premises
- Fargate is for serverless containers in AWS
- Dedicated Hosts are for compliance

**References:** ECS Anywhere, EKS Anywhere, Hybrid Containers
</details>

---

### Question 27
A team needs a managed, scalable Apache Cassandra-compatible database for their application. Which AWS service should they use?

A. Amazon Keyspaces  
B. Amazon DynamoDB  
C. Amazon RDS for PostgreSQL  
D. Amazon Aurora  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon Keyspaces is a managed Cassandra-compatible database
- Supports Cassandra Query Language (CQL)
- DynamoDB is NoSQL but not Cassandra-compatible
- RDS and Aurora are relational databases

**References:** Amazon Keyspaces, Managed Cassandra
</details>

---

### Question 28
A financial institution needs a fully managed, immutable, cryptographically verifiable ledger database. Which AWS service should they use?

A. Amazon QLDB  
B. Amazon Aurora  
C. Amazon RDS  
D. Amazon DynamoDB  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon QLDB (Quantum Ledger Database) is a fully managed ledger database
- Provides immutable, cryptographically verifiable transaction log
- Aurora, RDS, and DynamoDB are not ledger databases

**References:** Amazon QLDB, Ledger Database
</details>

---

## Summary

**Total Questions**: 28  
**Topics Covered**:
- EC2 Instance Types and Pricing (On-Demand, Reserved, Spot, Dedicated)
- Auto Scaling (Policies, Health Checks, Lifecycle)
- Elastic Load Balancing (ALB, NLB, CLB, GLB)
- AWS Lambda (Configuration, Limits, Concurrency)
- Container Services (ECS, EKS, Fargate)
- Elastic Beanstalk (PaaS)
- Placement Groups
- Session Management
- AWS Outposts
- AWS Batch
- AWS Serverless Application Repository
- VMware Cloud on AWS
- AWS Wavelength
- ECS Anywhere
- EKS Anywhere
- Amazon Keyspaces
- Amazon QLDB

**Exam Tips**:

**EC2 Pricing**:
- **Spot**: Cheapest (90% discount), can be interrupted
- **Reserved**: 1-3 year commitment, up to 72% discount
- **Savings Plans**: Flexible commitment, up to 66% discount
- **On-Demand**: No commitment, highest price
- **Dedicated Hosts**: BYOL, compliance, most expensive

**Auto Scaling Policies**:
- **Target Tracking**: Easiest, maintain metric at target
- **Scheduled**: Predictable patterns
- **Step**: Multiple thresholds
- **Predictive**: ML-based forecasting

**Load Balancers**:
- **ALB**: Layer 7, HTTP/HTTPS, advanced routing
- **NLB**: Layer 4, extreme performance, static IP
- **CLB**: Legacy, basic
- **GLB**: Layer 3, virtual appliances

**Lambda**:
- Max timeout: 15 minutes
- Memory: 128 MB - 10 GB
- CPU scales with memory
- Automatic concurrent scaling

**Containers**:
- **ECS + EC2**: Manage instances
- **ECS + Fargate**: Serverless containers
- **EKS**: Managed Kubernetes

**Placement Groups**:
- **Cluster**: Low latency, single AZ
- **Spread**: Max availability, 7/AZ
- **Partition**: Large distributed apps

**Best Practices**:
1. Use IAM roles for EC2 (not access keys)
2. External session storage (ElastiCache/DynamoDB)
3. Multi-AZ for high availability
4. Right-size instances (use CloudWatch metrics)
5. Use Spot for fault-tolerant workloads
6. Target Tracking for most Auto Scaling scenarios

**Next Steps**:
- Practice identifying correct pricing model for scenarios
- Understand when to use each load balancer type
- Know Lambda limitations and when to use alternatives
- Compare ECS vs EKS, Fargate vs EC2 launch types
