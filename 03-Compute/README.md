# Module 03: Compute Services

## Overview
AWS offers various compute services for different workloads. This module covers EC2, Lambda, ECS, EKS, and related services.

## Learning Objectives
- Understand EC2 instance types and purchasing options
- Configure Auto Scaling and Load Balancing
- Implement serverless computing with Lambda
- Work with container services (ECS, EKS, Fargate)
- Use Elastic Beanstalk for application deployment

---

## 1. Amazon EC2 (Elastic Compute Cloud)

### What is EC2?
- Virtual servers in the cloud
- Complete control over computing resources
- Pay only for what you use
- Launch instances in minutes

### EC2 Instance Components
1. **AMI (Amazon Machine Image)**: Operating system template
2. **Instance Type**: CPU, memory, storage, networking capacity
3. **EBS Volume**: Persistent block storage
4. **Security Groups**: Virtual firewall
5. **Key Pairs**: Secure login credentials
6. **Instance Metadata**: Data about your instance

---

## 2. EC2 Instance Types

### Instance Type Naming Convention
Example: **m5.2xlarge**
- **m**: Instance family
- **5**: Generation
- **2xlarge**: Size

### Instance Families

| Family | Type | Use Case | Example |
|--------|------|----------|---------|
| **General Purpose** | A, T, M | Balanced compute, memory, networking | Web servers, code repos |
| **Compute Optimized** | C | High-performance processors | HPC, gaming, ML inference |
| **Memory Optimized** | R, X, High Memory, z | Large datasets in memory | In-memory databases, SAP HANA |
| **Storage Optimized** | I, D, H | High sequential read/write | NoSQL databases, data warehousing |
| **Accelerated Computing** | P, G, F, Inf, VT | GPU, FPGA for ML, graphics | ML training, video encoding |

### Key Instance Types to Remember

**T-Series (T2, T3, T3a, T4g)**
- Burstable performance
- Baseline CPU performance with ability to burst
- CPU Credits system
- Cost-effective for variable workloads
- Use cases: Development, low-traffic websites

**M-Series (M5, M6i, M7g)**
- General purpose, balanced resources
- Use cases: Application servers, small-medium databases

**C-Series (C5, C6i, C7g)**
- Compute-optimized
- Use cases: Batch processing, gaming servers, scientific modeling

**R-Series (R5, R6i, R7g)**
- Memory-optimized
- Use cases: In-memory caches, real-time big data analytics

**Graviton Instances (ending in 'g')**
- AWS-designed ARM processors
- Up to 40% better price-performance
- Types: T4g, M7g, C7g, R7g

---

## 3. EC2 Purchasing Options

### 1. On-Demand Instances
- **Pay per second** (Linux) or per hour (Windows)
- No long-term commitments
- **Use case**: Short-term, unpredictable workloads
- **Cost**: Highest per-hour cost

### 2. Reserved Instances (RI)
- **1 or 3-year commitment**
- **Up to 72% discount** vs On-Demand
- Payment options:
  - All Upfront (highest discount)
  - Partial Upfront
  - No Upfront
- Types:
  - **Standard RI**: Cannot change instance attributes
  - **Convertible RI**: Can change instance family (up to 66% discount)
- **Use case**: Steady-state applications (databases, always-on servers)
- Can be sold in Reserved Instance Marketplace

### 3. Savings Plans
- **1 or 3-year commitment**
- Commit to a **dollar amount per hour** (e.g., $10/hour)
- **Up to 72% discount**
- Types:
  - **Compute Savings Plan**: Most flexible, apply to any instance family
  - **EC2 Instance Savings Plan**: Specific instance family in region
  - **SageMaker Savings Plan**: For SageMaker usage
- **Use case**: Flexible compute needs with commitment

### 4. Spot Instances
- **Up to 90% discount** vs On-Demand
- Can be terminated by AWS with 2-minute warning
- **Use case**: Fault-tolerant, flexible workloads
- Examples: Batch jobs, data analysis, CI/CD, big data
- **Spot Fleet**: Collection of Spot + On-Demand instances
- **Spot Blocks**: Spot instances for 1-6 hours without interruption

### 5. Dedicated Hosts
- **Physical server** dedicated to your use
- Most expensive option
- **Use case**: Regulatory requirements, server-bound software licenses
- Can use existing licenses (BYOL - Bring Your Own License)

### 6. Dedicated Instances
- Instances run on hardware dedicated to single customer
- May share hardware with other instances in same account
- Less expensive than Dedicated Hosts

### 7. Capacity Reservations
- Reserve capacity in specific AZ
- No billing discount (combine with RI or Savings Plan)
- **Use case**: Need guaranteed capacity for critical events

---

## 4. EC2 Instance Lifecycle

```
┌─────────┐
│ Pending │ (Billed)
└────┬────┘
     │
     ▼
┌─────────┐     ┌─────────┐     ┌────────────┐
│ Running │────▶│ Stopping│────▶│  Stopped   │
└────┬────┘     └─────────┘     └─────┬──────┘
     │           (Billed)              │ (Not billed for instance)
     │                                 │ (Still billed for EBS)
     ▼                                 │
┌──────────────┐                       │
│ Shutting Down│◀──────────────────────┘
└──────┬───────┘
       │
       ▼
┌────────────┐
│ Terminated │ (Not billed)
└────────────┘
```

**Important Notes**:
- Stopped instances: NOT billed for instance, STILL billed for EBS volumes
- Hibernate: Saves RAM contents to EBS, faster boot
- Terminate: Instance deleted (unless DeleteOnTermination is false)

---

## 5. EC2 Networking

### Elastic IP (EIP)
- **Static public IPv4** address
- Persists when instance is stopped
- **5 EIPs per account** (can request increase)
- **Charged when NOT attached** to running instance
- Best practice: Use DNS instead

### Enhanced Networking
- **SR-IOV** (Single Root I/O Virtualization)
- Higher bandwidth, lower latency
- **Elastic Network Adapter (ENA)**: Up to 100 Gbps
- **Intel 82599 VF**: Up to 10 Gbps (older)
- No additional charge

### Placement Groups

#### 1. Cluster Placement Group
- Instances in **single AZ, same rack**
- **Low latency**, 10 Gbps network
- Use case: HPC applications, tightly coupled workloads
- Risk: Single point of failure

#### 2. Spread Placement Group
- Instances on **different hardware**
- Max **7 instances per AZ** per group
- Use case: Critical applications requiring high availability
- Minimize correlated failures

#### 3. Partition Placement Group
- Instances in **logical partitions**
- Each partition on separate rack
- Up to **7 partitions per AZ**
- Use case: Hadoop, Cassandra, Kafka

---

## 6. Auto Scaling

### What is Auto Scaling?
- Automatically adjust number of EC2 instances
- Maintain application availability
- Optimize costs

### Auto Scaling Components

#### 1. Launch Template / Launch Configuration
- AMI, instance type, key pair, security groups
- **Launch Template** (newer, recommended)
  - Versioning support
  - Multiple instance types
  - Spot and On-Demand mix
- **Launch Configuration** (legacy)
  - Cannot be modified
  - Single instance type

#### 2. Auto Scaling Group (ASG)
- Minimum size
- Desired capacity
- Maximum size
- Target AZs

#### 3. Scaling Policies

**Dynamic Scaling**:
- **Target Tracking**: Maintain target metric (e.g., CPU 50%)
- **Step Scaling**: Scale based on CloudWatch alarms
- **Simple Scaling**: Single adjustment based on alarm

**Scheduled Scaling**:
- Scale based on schedule
- Example: Increase capacity weekdays 9am-5pm

**Predictive Scaling**:
- ML-powered predictions
- Automatically schedule scaling

### Auto Scaling Cooldown
- **Default 300 seconds**
- Prevents launching/terminating during previous scaling
- Use detailed monitoring for faster response

### Termination Policies
1. Select AZ with most instances
2. Select instance with oldest launch configuration/template
3. Or: Closest to next billing hour, random, newest/oldest instance

---

## 7. Elastic Load Balancing (ELB)

### Load Balancer Types

#### 1. Application Load Balancer (ALB)
- **Layer 7** (HTTP/HTTPS)
- Routes based on:
  - Path: `/api` vs `/images`
  - Hostname: `api.example.com` vs `www.example.com`
  - Query strings: `?id=123&order=asc`
  - Headers
- **Target Types**:
  - EC2 instances
  - IP addresses
  - Lambda functions
  - Containers
- **Features**:
  - Fixed hostname
  - Server Name Indication (SNI)
  - WebSocket support
  - HTTP/2 support
- **Use case**: Web applications, microservices, containers

#### 2. Network Load Balancer (NLB)
- **Layer 4** (TCP/UDP)
- **Ultra-high performance** (millions requests/sec)
- **Static IP** per AZ (Elastic IP support)
- **Low latency** (~100ms vs 400ms for ALB)
- **Target Types**:
  - EC2 instances
  - IP addresses
  - ALB (NLB in front of ALB)
- **Use case**: Extreme performance, TCP/UDP traffic, static IP

#### 3. Gateway Load Balancer (GWLB)
- **Layer 3** (Network layer)
- Deploy, scale, manage third-party appliances
- **GENEVE** protocol (port 6081)
- **Use case**: Firewalls, IDS/IPS, deep packet inspection

#### 4. Classic Load Balancer (CLB)
- **Legacy** (Layer 4 & 7)
- Not recommended for new applications
- Being retired

### Load Balancer Features

**Health Checks**
- Verify target health
- Protocol: HTTP, HTTPS, TCP
- Healthy threshold, unhealthy threshold
- Timeout, interval

**Cross-Zone Load Balancing**
- Distribute traffic evenly across all targets in all enabled AZs
- **ALB**: Always on, no charge
- **NLB**: Disabled by default, charge for inter-AZ data
- **CLB**: Disabled by default, no charge if enabled

**Connection Draining / Deregistration Delay**
- Time to complete in-flight requests before deregistering
- 1-3600 seconds (default 300)

**Sticky Sessions (Session Affinity)**
- Route same client to same target
- **Cookie types**:
  - Application-based cookie
  - Load balancer-generated cookie (AWSALB)
- **ALB, CLB**: Support sticky sessions
- **NLB**: Not applicable (Layer 4)

**SSL/TLS Termination**
- Load balancer handles SSL/TLS encryption/decryption
- Upload certificate to **ACM (AWS Certificate Manager)** or IAM
- **Server Name Indication (SNI)**:
  - Load multiple SSL certificates on one IP
  - Supported by ALB, NLB (not CLB)

---

## 8. AWS Lambda

### What is Lambda?
- **Serverless compute** service
- Run code without provisioning servers
- **Pay per request** and compute time
- Automatic scaling

### Lambda Key Features
- **Supported Languages**: Node.js, Python, Java, C#, Go, Ruby, Custom Runtime
- **Memory**: 128 MB to 10 GB (in 1 MB increments)
- **CPU**: Scales with memory
- **Timeout**: Up to **15 minutes**
- **Execution environment**: Temporary disk /tmp (up to 10 GB)
- **Concurrency**: 1000 concurrent executions (default, can increase)
- **Deployment package**: 50 MB (zipped), 250 MB (unzipped)

### Lambda Pricing
- **Requests**: $0.20 per 1 million requests
- **Duration**: Based on GB-seconds
- **Free tier**:
  - 1 million requests/month
  - 400,000 GB-seconds/month

### Lambda Invocation Types

#### 1. Synchronous
- Wait for response
- Examples: API Gateway, ALB, Cognito, Alexa
- Error handling: Retry on client side

#### 2. Asynchronous
- Lambda queues event and returns immediately
- Retries: 2 automatic retries
- Examples: S3, SNS, CloudWatch Events
- DLQ (Dead Letter Queue): Send failed events to SQS or SNS

#### 3. Event Source Mapping
- Lambda polls from stream/queue
- Examples: Kinesis, DynamoDB Streams, SQS
- Lambda responsible for polling

### Lambda with VPC
- By default, Lambda runs in AWS-owned VPC
- Can configure Lambda to access resources in your VPC
- Requires: VPC ID, subnets, security groups
- Use **VPC endpoints** for AWS services to avoid internet access

### Lambda@Edge
- Run Lambda at CloudFront edge locations
- Customize content delivery
- Use cases:
  - URL rewrite
  - Authentication at edge
  - A/B testing
  - Bot mitigation

### Lambda Layers
- Reusable components (libraries, dependencies)
- Reduce deployment package size
- Share code across functions
- Up to 5 layers per function

---

## 9. Container Services

### Amazon ECS (Elastic Container Service)

**What is ECS?**
- Container orchestration service
- Run Docker containers on AWS

**Launch Types**:

#### 1. EC2 Launch Type
- Run containers on EC2 instances you manage
- More control over infrastructure
- Responsible for managing EC2 instances

#### 2. Fargate Launch Type
- **Serverless** container platform
- AWS manages infrastructure
- Pay only for resources used
- No EC2 instances to manage

**ECS Components**:
- **Task Definition**: Blueprint for application (JSON)
  - Image, CPU, memory, ports, environment variables
- **Task**: Running instance of task definition
- **Service**: Maintain desired number of tasks
- **Cluster**: Logical grouping of tasks/services

**ECS Integration**:
- ALB/NLB for load balancing
- EBS/EFS for persistent storage
- CloudWatch for logging and monitoring
- IAM for security

### Amazon EKS (Elastic Kubernetes Service)

**What is EKS?**
- Managed Kubernetes service
- Run Kubernetes on AWS without managing control plane

**EKS Features**:
- **Managed control plane** (masters)
- Automatic updates and patching
- Integration with AWS services
- Multi-AZ for high availability

**EKS Node Types**:
- **Managed Node Groups**: AWS manages EC2 instances
- **Self-managed Nodes**: You manage EC2 instances
- **Fargate**: Serverless, AWS manages infrastructure

**EKS vs ECS**:
- **EKS**: Use if already using Kubernetes, need portability
- **ECS**: AWS-native, simpler, tighter AWS integration

### Amazon ECR (Elastic Container Registry)
- Fully managed Docker container registry
- Store, manage, deploy container images
- Integrated with ECS/EKS
- Encryption, vulnerability scanning
- Lifecycle policies

---

## 10. AWS Elastic Beanstalk

### What is Elastic Beanstalk?
- **Platform as a Service (PaaS)**
- Deploy applications without infrastructure management
- Automatically handles capacity provisioning, load balancing, scaling, monitoring

### Supported Platforms
- **Languages**: Java, .NET, PHP, Node.js, Python, Ruby, Go
- **Containers**: Docker (single/multi-container)
- **Custom platforms**: Using Packer

### Elastic Beanstalk Components
- **Application**: Collection of components
- **Application Version**: Specific iteration of code
- **Environment**: Resources running application version
  - Web Server Environment
  - Worker Environment (SQS-based)

### Deployment Options
1. **All at once**: Deploy to all instances simultaneously (downtime)
2. **Rolling**: Deploy in batches (reduced capacity)
3. **Rolling with additional batch**: Maintain full capacity
4. **Immutable**: Deploy to new instances, swap (safest)
5. **Traffic splitting**: Canary testing (portion of traffic to new version)
6. **Blue/Green**: Swap environment URLs

### Elastic Beanstalk Lifecycle
- **Lifecycle Policy**: Limit stored application versions
- Prevent hitting quota (1000 versions)

---

## 11. Other Compute Services

### AWS Batch
- Fully managed batch processing
- Dynamically provisions resources
- Schedule, execute, manage batch jobs
- Runs on ECS (EC2 or Fargate)

### AWS Lightsail
- Simple VPS (Virtual Private Server)
- Fixed monthly price
- Use case: Simple web apps, websites, dev/test environments
- Includes: Instance, storage, data transfer, DNS, static IP

### AWS Outposts
- AWS infrastructure on-premises
- Hybrid cloud solution
- Same AWS APIs, tools, hardware

### AWS Wavelength
- Deploy to 5G edge
- Ultra-low latency for mobile devices

### AWS Local Zones
- Extension of AWS Region
- Low-latency for specific geographic areas

---

## Practice Questions

1. **Which EC2 purchasing option provides up to 90% discount but can be terminated by AWS?**
   - A. Reserved Instances
   - B. Spot Instances
   - C. Dedicated Hosts
   - D. On-Demand
   
   **Answer**: B

2. **What is the maximum execution time for a Lambda function?**
   - A. 5 minutes
   - B. 15 minutes
   - C. 30 minutes
   - D. 1 hour
   
   **Answer**: B

3. **Which load balancer operates at Layer 7 and supports path-based routing?**
   - A. Classic Load Balancer
   - B. Network Load Balancer
   - C. Application Load Balancer
   - D. Gateway Load Balancer
   
   **Answer**: C

4. **Which ECS launch type is serverless?**
   - A. EC2
   - B. Fargate
   - C. Lambda
   - D. Lightsail
   
   **Answer**: B

---

## Hands-On Labs

### Lab 1: Launch EC2 Instance
1. Launch a t2.micro instance with Amazon Linux 2
2. Configure security group for SSH
3. Connect via SSH
4. Install and run a web server
5. Access via public IP

### Lab 2: Auto Scaling
1. Create launch template
2. Create Auto Scaling group (min: 2, max: 4)
3. Configure target tracking (CPU 50%)
4. Stress test to trigger scaling
5. Monitor scaling activities

### Lab 3: Application Load Balancer
1. Launch 2 EC2 instances in different AZs
2. Create target group
3. Create ALB
4. Configure health checks
5. Test load balancing

### Lab 4: Lambda Function
1. Create Lambda function (Python)
2. Configure trigger (API Gateway)
3. Test function
4. Monitor in CloudWatch Logs

### Lab 5: ECS with Fargate
1. Create ECS cluster
2. Define task definition
3. Create service with Fargate
4. Deploy container
5. Access application

---

## Key Takeaways

✅ Choose right instance type for workload (General, Compute, Memory, Storage)  
✅ Spot Instances for fault-tolerant workloads (up to 90% discount)  
✅ Reserved Instances/Savings Plans for steady-state workloads  
✅ ALB for Layer 7 (HTTP/HTTPS), NLB for Layer 4 (TCP/UDP) extreme performance  
✅ Lambda for serverless, event-driven, short-duration tasks (max 15 min)  
✅ ECS with Fargate for serverless containers  
✅ Auto Scaling maintains availability and optimizes costs  
✅ Elastic Beanstalk is PaaS - handles infrastructure automatically  
✅ Use IAM roles for EC2 instances, not access keys  
✅ Enable detailed monitoring for faster Auto Scaling response  

---

## Additional Resources

- [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/)
- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [Auto Scaling Best Practices](https://docs.aws.amazon.com/autoscaling/)

---

**Previous Module**: [Module 02: IAM](../02-IAM/README.md)  
**Next Module**: [Module 04: Storage Services](../04-Storage/README.md)

