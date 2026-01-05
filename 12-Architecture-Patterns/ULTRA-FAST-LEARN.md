# 12: Architecture Patterns - Ultra Fast Learning 🚀

## Well-Architected Framework (6 Pillars)

### 1. Operational Excellence
- **Run and monitor** systems
- **IaC**: CloudFormation, CDK
- **Automate**: CI/CD pipelines
- **Frequent, small changes**: Reduce risk
- **Learn from failures**: Post-mortems
- **Runbooks and playbooks**: Document procedures

### 2. Security
- **Identity**: IAM, least privilege
- **Detection**: CloudTrail, GuardDuty, Config
- **Protection**: Encryption (at-rest, in-transit)
- **Infrastructure protection**: VPC, Security Groups, NACLs
- **Data protection**: Versioning, MFA Delete, backup

### 3. Reliability
- **Recover from failures**: Auto Scaling, Multi-AZ
- **Test recovery**: Simulate failures
- **Auto-scale**: Handle demand changes
- **Manage capacity**: Right-size resources
- **Design principles**: Distributed systems, graceful degradation

### 4. Performance Efficiency
- **Use right resources**: Instance types, storage
- **Monitor performance**: CloudWatch
- **Experiment**: Test different configurations
- **Go global**: Multi-region deployment
- **Serverless**: Lambda, Fargate (no server management)

### 5. Cost Optimization
- **Pay for what you use**: Stop unused resources
- **Reserved/Savings Plans**: Commit for discounts
- **Right-size**: Match resources to workload
- **Monitor costs**: Cost Explorer, Budgets
- **Measure efficiency**: Cost per transaction

### 6. Sustainability
- **Minimize environmental impact**
- **Use managed services**: Higher utilization
- **Reduce idle resources**: Auto Scaling
- **Optimize regions**: Lower carbon footprint

## Multi-Tier Architecture

### 3-Tier Web Application
```
Users → CloudFront → Route 53
  ↓
ALB (Public Subnet)
  ↓
EC2 Auto Scaling Group (Private Subnet)
  ↓
RDS Multi-AZ (Private Subnet)
```

**Components**:
- **Presentation**: CloudFront, Route 53, ALB
- **Application**: EC2 Auto Scaling (private subnets)
- **Data**: RDS Multi-AZ (private subnets)

**Features**:
- ✅ High availability (Multi-AZ)
- ✅ Scalability (Auto Scaling)
- ✅ Security (Private subnets, SGs)
- ✅ Performance (CloudFront CDN)

## Serverless Architecture

### Serverless Web App
```
Users → CloudFront + S3 (static)
  ↓
API Gateway
  ↓
Lambda
  ↓
DynamoDB
```

**Benefits**:
- ✅ No server management
- ✅ Auto-scaling
- ✅ Pay per use
- ✅ High availability (built-in)

**Use cases**: Web apps, mobile backends, APIs

## Event-Driven Architecture

### Pattern 1: S3 → Lambda
```
S3 (file upload) → Lambda (process) → DynamoDB/S3
```
**Use case**: Image processing, ETL

### Pattern 2: SNS Fan-out
```
Application → SNS Topic → [SQS 1, SQS 2, Lambda]
```
**Use case**: Parallel processing, multiple consumers

### Pattern 3: EventBridge
```
AWS Service → EventBridge → [Lambda, Step Functions, SQS]
```
**Use case**: Event-driven automation

## High Availability Patterns

### Multi-AZ Deployment
- **RDS Multi-AZ**: Automatic failover
- **ELB**: Distribute across AZs
- **Auto Scaling**: Launch in multiple AZs
- **S3**: 11 nines durability, auto-replicated

### Multi-Region Deployment
- **Route 53**: Failover routing policy
- **Global Accelerator**: Anycast IPs
- **DynamoDB Global Tables**: Multi-region replication
- **Aurora Global Database**: <1 sec replication lag
- **CloudFront**: Edge locations worldwide

## Disaster Recovery Patterns

### 1. Backup & Restore (Cheapest, Slowest)
- Backup to S3/Glacier
- **RTO/RPO**: Hours to days
- **Cost**: Low

### 2. Pilot Light (Core services always on)
- Minimal setup always running
- **RTO**: 10s of minutes
- **Cost**: Low-Medium

### 3. Warm Standby (Scaled-down version)
- Running but minimal capacity
- **RTO**: Minutes
- **Cost**: Medium

### 4. Multi-Site (Full active-active)
- Full capacity in multiple regions
- **RTO**: Real-time
- **Cost**: High

## Decoupling Patterns

### SQS Queue Pattern
```
Producer → SQS Queue → Consumer (Auto Scaling)
```
**Benefits**: Asynchronous, decouple, scale independently

### Load Balancer Pattern
```
Users → ALB → Target Groups (EC2, Lambda, IP)
```
**Benefits**: Distribute load, health checks

## Caching Patterns

### Layer 1: CloudFront (Edge)
- Cache static content at edge locations
- **TTL**: 24 hours default
- **Use case**: Global users, static assets

### Layer 2: ElastiCache (Application)
- Cache database queries
- **Sub-millisecond** latency
- **Use case**: Frequent DB reads

### Layer 3: DAX (DynamoDB)
- In-memory cache for DynamoDB
- **Microsecond** latency
- **Use case**: DynamoDB read-heavy workloads

## Microservices Patterns

### Container-Based
```
ALB → ECS Fargate (Service Discovery)
  ↓
DynamoDB / RDS
```

### Serverless
```
API Gateway → Lambda Functions → DynamoDB
```

**Benefits**: Independent scaling, deployment, development

## Security Patterns

### Defense in Depth
```
CloudFront (WAF) → ALB (SG) → Private Subnet (NACL) → EC2 (SG) → Data (Encryption)
```

**Layers**:
1. **Edge**: CloudFront, WAF, Shield
2. **Network**: VPC, NACLs, Security Groups
3. **Application**: IAM, encryption
4. **Data**: Encryption at rest/transit

## Real-World Scenarios

### Scenario 1: E-Commerce Site
- **Front**: CloudFront + S3 (static)
- **API**: API Gateway + Lambda
- **Database**: DynamoDB (products), RDS (orders)
- **Search**: OpenSearch
- **Cache**: ElastiCache

### Scenario 2: Video Streaming
- **Storage**: S3
- **CDN**: CloudFront
- **Transcoding**: MediaConvert or Lambda
- **Auth**: Cognito
- **Signed URLs**: Restrict access

### Scenario 3: Big Data Pipeline
- **Ingest**: Kinesis Data Streams
- **Process**: Lambda or Kinesis Analytics
- **Store**: S3 (Data Lake)
- **Query**: Athena
- **Visualize**: QuickSight

## Quick Exam Tips
- **3-Tier**: Presentation, Application, Data layers
- **Serverless**: Lambda + API Gateway + DynamoDB
- **HA**: Multi-AZ + Auto Scaling + ELB
- **DR**: Backup (cheapest) → Multi-Site (fastest)
- **Decoupling**: Use SQS, SNS, EventBridge
- **Caching**: CloudFront (edge) → ElastiCache (app) → DAX (DynamoDB)
- **Security**: Defense in depth, multiple layers
- **Microservices**: ECS/EKS or Lambda
- **Cost**: Reserved/Savings Plans, right-size, monitor
- **Performance**: Right resources, CDN, caching
- **Read scenario carefully**: Match pattern to requirements!

