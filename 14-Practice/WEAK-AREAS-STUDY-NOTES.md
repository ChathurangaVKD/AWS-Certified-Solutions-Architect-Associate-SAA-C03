# Weak Areas Study Notes - Deep Dive

These notes provide in-depth coverage of the most commonly misunderstood topics in SAA-C03.

---

## Table of Contents
1. [IAM Deep Dive](#iam-deep-dive)
2. [Database Selection Matrix](#database-selection-matrix)
3. [Networking Mastery](#networking-mastery)
4. [Storage Decision Trees](#storage-decision-trees)
5. [Security Services Comparison](#security-services-comparison)
6. [Architecture Patterns Quick Reference](#architecture-patterns-quick-reference)
7. [Cost Optimization Strategies](#cost-optimization-strategies)

---

## IAM Deep Dive

### Policy Evaluation Logic (Most Tested!)

```
Decision Flow:
1. Start with IMPLICIT DENY (default)
2. Evaluate ALL applicable policies
3. EXPLICIT DENY? → DENY (end)
4. EXPLICIT ALLOW? → ALLOW
5. No EXPLICIT ALLOW? → DENY
```

**Key Rule**: DENY ALWAYS WINS

### Cross-Account Access Patterns

#### Pattern 1: IAM Role (Most Common)
```
Account A User → Assumes Role in Account B → Access Resources
```
- User temporarily gives up Account A permissions
- Use when: Simple cross-account access

#### Pattern 2: Resource-Based Policy
```
Account A User → Access via Resource Policy → Account B Resource
```
- User retains Account A permissions
- Use when: Need simultaneous access to both accounts
- Works with: S3, SNS, SQS, Lambda, etc.

#### Pattern 3: Cross-Account Role with ExternalId
```
Account A → Role with ExternalId → Account B
```
- Prevents "confused deputy" problem
- Use when: Third-party access (SaaS providers)

### Permission Boundaries

**What they do**: Set MAXIMUM permissions (ceiling)
**Use case**: Delegated admin creation of roles/users

```
User's Effective Permissions = 
  User Policy 
  ∩ Permission Boundary 
  ∩ SCP (if in Organization)
  − Explicit Denies
```

**Example Scenario**:
- Permission Boundary: Can't delete S3 buckets
- User Policy: Full S3 Admin
- **Result**: User can do everything EXCEPT delete buckets

### Service Control Policies (SCPs)

**Key Points**:
- Apply to OUs or accounts in AWS Organizations
- Do NOT grant permissions (only restrict)
- Affect ALL users including root (big deal!)
- Do NOT affect service-linked roles

**Common Exam Scenario**:
```
SCP denies region eu-west-1
+ User has full admin
= User cannot access eu-west-1
```

### Identity Federation Best Practices

**SAML 2.0** (Traditional Enterprise):
- Corporate AD/LDAP → SAML IdP → AWS
- Console access via federation endpoint
- Use: Large enterprises with existing IdP

**AWS IAM Identity Center (SSO)** (Modern):
- Centralized access to multiple AWS accounts
- SAML 2.0 compatible
- Built-in IdP or external (AD, Okta, Azure AD)
- Use: Multi-account organizations

**Web Identity Federation**:
- Login with Amazon, Facebook, Google
- Use Cognito (preferred) or direct federation
- Use: Mobile/web apps

**Cognito**:
- User Pools: User directory, authentication
- Identity Pools: AWS credentials for users
- Use together for complete solution

---

## Database Selection Matrix

### Decision Tree

```
Need to query with SQL?
├─ YES → Relational Database
│   ├─ Need highest performance?
│   │   └─ Aurora (5x MySQL, 3x PostgreSQL)
│   ├─ Need specific engine?
│   │   └─ RDS (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server)
│   └─ Data warehouse?
│       └─ Redshift
└─ NO → NoSQL
    ├─ Key-value, high throughput?
    │   └─ DynamoDB
    ├─ In-memory, sub-ms latency?
    │   ├─ Need persistence? → Redis (ElastiCache)
    │   └─ Simple cache? → Memcached (ElastiCache)
    ├─ Document database (MongoDB)?
    │   └─ DocumentDB
    ├─ Graph database?
    │   └─ Neptune
    └─ Time-series?
        └─ Timestream
```

### RDS Multi-AZ vs Read Replicas - Deep Dive

**Multi-AZ Deployment**:

```
Primary DB (AZ-A) ⟷[Synchronous Replication]⟷ Standby (AZ-B)
       ↓
Application uses SAME endpoint
       ↓
Automatic failover (60-120 seconds)
```

**When it fails over**:
- Primary DB failure
- AZ failure
- DB instance type change
- OS patching
- Manual failover (for testing)

**Important**: 
- Standby is NOT accessible for reads
- Backup from standby (no performance impact)
- No additional read capacity

**Read Replicas**:

```
Primary DB → [Asynchronous Replication] → Read Replica 1
                                        → Read Replica 2
                                        → Read Replica 3 (different region)
```

**Key Features**:
- Up to 5 read replicas (15 for Aurora)
- Each has its own endpoint
- Can be in different regions (async lag increases)
- Can be promoted to standalone DB
- No automatic failover (manual promotion)

**Exam Trick Question**:
"Need high availability AND read scaling"
**Answer**: Multi-AZ + Read Replicas (can combine both!)

### DynamoDB Deep Dive

**Capacity Planning**:

**Read Capacity Unit (RCU)**:
- 1 RCU = 1 strongly consistent read/sec OR 2 eventually consistent reads/sec
- Item size up to 4 KB
- Formula: (Item size in KB / 4) × Reads per second ÷ 2 (if eventually consistent)

**Write Capacity Unit (WCU)**:
- 1 WCU = 1 write/sec
- Item size up to 1 KB
- Formula: (Item size in KB) × Writes per second

**Example**:
- Read 10 items/sec, 8 KB each, eventually consistent
- RCU needed: (8/4) × 10 ÷ 2 = 10 RCUs

**When to use On-Demand vs Provisioned**:

| Scenario | Choose |
|----------|--------|
| New application, unknown traffic | On-Demand |
| Unpredictable spikes | On-Demand |
| Mobile app (varied usage) | On-Demand |
| Traffic doubles during business hours, steady otherwise | Provisioned with auto-scaling |
| Consistent 24/7 traffic | Provisioned |
| Need absolute lowest cost with predictable traffic | Provisioned |

**DynamoDB Transactions**:
- All-or-nothing operations
- Up to 25 items or 4 MB
- 2x WCU/RCU cost
- Use: Financial transactions, inventory systems

**DynamoDB Streams**:
- Ordered record of item-level changes
- 24-hour retention
- Trigger Lambda functions
- Use: Audit logs, replicate to ElasticSearch, analytics

### ElastiCache Detailed Comparison

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data Persistence** | ✅ RDB + AOF | ❌ None |
| **Backup/Restore** | ✅ Yes | ❌ No |
| **Replication** | ✅ Multi-AZ, read replicas | ❌ Multi-node for partitioning only |
| **Auto-Failover** | ✅ Yes | ❌ No |
| **Data Types** | Strings, Lists, Sets, Sorted Sets, Hashes, Bitmaps, HyperLogLogs | Strings only |
| **Transactions** | ✅ Yes | ❌ No |
| **Pub/Sub** | ✅ Yes | ❌ No |
| **Lua Scripting** | ✅ Yes | ❌ No |
| **Multi-threading** | ❌ Single-threaded | ✅ Multi-threaded |
| **Horizontal Scaling** | ✅ Cluster mode | ✅ Yes (simple) |
| **Encryption** | ✅ At-rest & in-transit | ❌ In-transit only |
| **Auth** | ✅ AUTH token | ✅ SASL |

**Exam Scenarios**:
- "Session store with backup" → Redis
- "Leaderboard/gaming scores" → Redis (Sorted Sets)
- "Real-time analytics" → Redis
- "Simplest caching layer, no persistence" → Memcached
- "Need multi-threaded performance" → Memcached

---

## Networking Mastery

### VPC Complete Architecture

```
VPC (10.0.0.0/16)
├─ Public Subnet (10.0.1.0/24) - AZ-A
│   ├─ Route: 0.0.0.0/0 → Internet Gateway
│   ├─ NAT Gateway
│   └─ Instances with public IP/EIP
├─ Private Subnet (10.0.2.0/24) - AZ-A
│   ├─ Route: 0.0.0.0/0 → NAT Gateway
│   └─ Instances (no public IP)
├─ Public Subnet (10.0.3.0/24) - AZ-B
└─ Private Subnet (10.0.4.0/24) - AZ-B
```

### Security Groups vs NACLs - Detailed

**Security Group Rules**:
```
Inbound:
Type: HTTP, Protocol: TCP, Port: 80, Source: 0.0.0.0/0
Type: SSH, Protocol: TCP, Port: 22, Source: 10.0.0.0/16

Outbound:
(Default: All traffic allowed)
```

**NACL Rules** (Evaluated in order!):
```
Inbound:
Rule# 100: HTTP (80) from 0.0.0.0/0 - ALLOW
Rule# 200: SSH (22) from 10.0.0.0/16 - ALLOW
Rule# 300: All from 203.0.113.0/24 - DENY
Rule# *: All - DENY

Outbound:
Rule# 100: HTTP (80) to 0.0.0.0/0 - ALLOW
Rule# 110: Ephemeral (1024-65535) to 0.0.0.0/0 - ALLOW (important!)
Rule# *: All - DENY
```

**Critical NACL Concept**: Must allow ephemeral ports for return traffic!

### VPC Peering Rules (Exam Favorites!)

**What's Allowed**:
- Private IP communication
- Cross-region peering
- Cross-account peering
- Multiple peering connections

**What's NOT Allowed** (Most tested!):
- ❌ Transitive routing: VPC-A ↔ VPC-B ↔ VPC-C (A cannot talk to C)
- ❌ Overlapping CIDR blocks
- ❌ Edge-to-edge routing (VPN, Direct Connect, Internet Gateway)

**Exam Trick**:
"VPC-A peers with VPC-B, VPC-B peers with VPC-C. Can A reach C?"
**Answer**: NO! Need direct peering A ↔ C OR use Transit Gateway

### Transit Gateway - When & Why

**Use Cases**:
1. **Hub-Spoke Network**: 1 TGW + multiple VPCs (transitive routing works!)
2. **Multi-Region**: TGW peering across regions
3. **Hybrid Cloud**: VPN/Direct Connect → TGW → Multiple VPCs
4. **Network Segmentation**: Route tables for isolation

**Cost Comparison** (10 VPCs full mesh):
- VPC Peering: 45 connections (n×(n-1)/2)
- Transit Gateway: 10 attachments

**Exam Scenario**:
"Company has 20 VPCs, on-premises DC with VPN, needs central routing"
**Answer**: Transit Gateway (not VPC Peering - too complex)

### Direct Connect Deep Dive

**Connection Types**:

**Dedicated Connection**:
- 1 Gbps, 10 Gbps, 100 Gbps
- Physical fiber from AWS
- Your router at AWS DX location
- Single-tenant

**Hosted Connection**:
- 50 Mbps → 10 Gbps
- Through AWS Partner
- Multi-tenant
- Faster provisioning

**Virtual Interfaces (VIF)**:

1. **Private VIF**: 
   - Access VPC private resources
   - Connect to Virtual Private Gateway (VGW)

2. **Public VIF**:
   - Access AWS public services (S3, DynamoDB) without internet
   - Still uses private connection

3. **Transit VIF**:
   - Connect to Transit Gateway
   - Access multiple VPCs

**High Availability Pattern**:
```
On-Premises
├─ DX Connection 1 → AWS (Primary)
└─ VPN Connection → AWS (Backup)
```

**Or for mission-critical**:
```
On-Premises
├─ DX Connection 1 → DX Location A → AWS
└─ DX Connection 2 → DX Location B → AWS
```

### Route 53 Routing Policies - Detailed Examples

**Weighted Routing** (A/B Testing):
```
Record: api.example.com
├─ Weight 70 → ALB-Production (70% traffic)
└─ Weight 30 → ALB-New-Version (30% traffic)
```

**Latency Routing**:
```
Record: app.example.com
├─ us-east-1 → ALB-East (NA users routed here)
├─ eu-west-1 → ALB-West (EU users routed here)
└─ ap-south-1 → ALB-Asia (Asia users routed here)
```
Route 53 automatically routes to lowest latency endpoint.

**Failover Routing** (Active-Passive DR):
```
Record: db.example.com
├─ Primary → RDS-us-east-1 (with health check)
└─ Secondary → RDS-us-west-2 (failover if primary unhealthy)
```

**Geolocation** (Compliance, Localization):
```
Record: www.example.com
├─ Europe → ALB-EU (GDPR compliance, EU data)
├─ North America → ALB-US
└─ Default → ALB-US (all other locations)
```

**Geoproximity** (Traffic Bias):
```
Record: api.example.com
├─ us-east-1, bias: +50 → Pull more traffic
└─ eu-west-1, bias: -30 → Push traffic away
```

**Multi-value Answer**:
- Returns up to 8 healthy IPs
- Client-side load balancing
- Simple alternative to ELB for basic use cases

---

## Storage Decision Trees

### S3 vs EBS vs EFS vs FSx

**Decision Flow**:

```
Need file system interface?
├─ NO → S3 (object storage)
│   └─ Access pattern?
│       ├─ Frequent → S3 Standard
│       ├─ Infrequent → S3 IA
│       ├─ Archive → Glacier
│       └─ Unknown → Intelligent-Tiering
└─ YES → Block or File?
    ├─ Block → EBS
    │   ├─ Boot volume? → gp3/gp2
    │   ├─ High IOPS DB? → io2
    │   └─ Big data? → st1
    └─ File System
        ├─ Linux/POSIX? → EFS
        ├─ Windows? → FSx for Windows File Server
        ├─ High performance computing? → FSx for Lustre
        └─ NetApp ONTAP? → FSx for NetApp ONTAP
```

### S3 Lifecycle Policy Examples

**Example 1: Log Archival**
```json
{
  "Rules": [{
    "Id": "LogArchival",
    "Status": "Enabled",
    "Filter": {"Prefix": "logs/"},
    "Transitions": [
      {
        "Days": 30,
        "StorageClass": "STANDARD_IA"
      },
      {
        "Days": 90,
        "StorageClass": "GLACIER_IR"
      },
      {
        "Days": 365,
        "StorageClass": "DEEP_ARCHIVE"
      }
    ],
    "Expiration": {"Days": 2555}
  }]
}
```

**Example 2: Incomplete Multipart Upload Cleanup**
```json
{
  "Rules": [{
    "Id": "CleanupMultipart",
    "Status": "Enabled",
    "AbortIncompleteMultipartUpload": {
      "DaysAfterInitiation": 7
    }
  }]
}
```

### S3 Security Layers

**Layer 1: Bucket Policies** (Resource-based)
```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::123456789012:root"},
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::mybucket/*",
  "Condition": {
    "IpAddress": {"aws:SourceIp": "203.0.113.0/24"}
  }
}
```

**Layer 2: IAM Policies** (Identity-based)
**Layer 3: ACLs** (Legacy, avoid)
**Layer 4: Block Public Access** (Override everything)

**Exam Pattern**:
"User has full S3 access, but bucket policy denies their account"
**Answer**: Access DENIED (explicit deny wins)

### EBS Snapshots & Encryption

**Key Facts**:
- Snapshots are incremental (only changed blocks)
- Stored in S3 (managed by AWS, you don't see)
- Can copy across regions
- Can share with other accounts (if unencrypted)

**Encryption Rules**:
- Encrypted volume → Encrypted snapshot (automatically)
- Unencrypted volume → Can create encrypted copy of snapshot
- Cannot remove encryption once added
- Uses KMS keys

**Lifecycle Manager**:
- Automate snapshot creation/deletion
- Schedule: Every 12/24 hours
- Retention: Count or age-based
- Cross-region copy

### EFS Performance Modes

**Performance Mode** (Set at creation):
- **General Purpose**: Default, low latency (most use cases)
- **Max I/O**: Higher latency, higher throughput, higher parallelism (big data)

**Throughput Mode** (Can change):
- **Bursting**: Throughput scales with storage size
- **Provisioned**: Set specific throughput regardless of size
- **Elastic**: Auto-scales throughput (recommended)

**Storage Classes**:
- **Standard**: Frequent access, multi-AZ
- **Infrequent Access (IA)**: Lower cost, retrieval fee
- **One Zone**: 47% cheaper, single AZ

**Lifecycle Management**:
- Auto-move files to IA after N days of no access
- Saves up to 92% cost

---

## Security Services Comparison

### Encryption Services Matrix

| Service | Use Case | Key Type | FIPS 140-2 Level |
|---------|----------|----------|------------------|
| **KMS** | Most encryption needs | Managed, Customer managed | Level 2 (some 3) |
| **CloudHSM** | Regulatory compliance | You manage in HSM | Level 3 |
| **ACM** | SSL/TLS certificates | AWS managed | - |
| **Secrets Manager** | Auto-rotate secrets | KMS | - |
| **Parameter Store** | Config, non-rotating | KMS (optional) | - |

### Threat Detection Services

**GuardDuty**:
```
Data Sources:
├─ VPC Flow Logs (network traffic)
├─ CloudTrail Events (API calls)
├─ DNS Logs (DNS queries)
└─ EKS Audit Logs

Detects:
├─ Compromised instances (crypto mining, C&C)
├─ Reconnaissance (port scanning)
├─ Compromised credentials (unusual API calls)
└─ Suspicious network traffic
```

**Automated Response Pattern**:
```
GuardDuty Finding
  ↓
EventBridge Rule
  ↓
Lambda Function
  ↓
Actions:
├─ Disable IAM credentials
├─ Isolate EC2 instance (apply SG)
├─ Create snapshot (forensics)
└─ Send SNS notification
```

**Macie**:
- Discovers PII/sensitive data in S3
- Uses ML to identify data types
- Automated discovery jobs
- Sensitive Data Identifier (SDI)

**Inspector**:
- **EC2**: Agent-based, network reachability, CVEs
- **ECR**: Image scanning for vulnerabilities
- **Lambda**: Code and dependencies scanning
- Risk score (0-10)

### WAF vs Shield vs Firewall Manager

**AWS Shield Standard** (Free):
- DDoS protection Layer 3/4
- All AWS customers
- CloudFront, Route 53, ELB

**AWS Shield Advanced** ($3,000/month):
- Enhanced DDoS protection
- 24/7 DDoS Response Team (DRT)
- Cost protection (scale costs during attack)
- Real-time attack notifications

**AWS WAF**:
- Layer 7 protection (HTTP/HTTPS)
- Web ACLs with rules:
  - IP address
  - HTTP headers, body, URL
  - Geographic location
  - Rate-based (rate limiting)
  - Managed rule groups (OWASP Top 10)
- Deploy on: CloudFront, ALB, API Gateway, AppSync

**AWS Firewall Manager**:
- Centrally manage WAF, Shield Advanced, Security Groups
- Apply across AWS Organizations
- Compliance dashboard

---

## Architecture Patterns Quick Reference

### High Availability Patterns

**Multi-AZ Application**:
```
Route 53
  ↓
CloudFront (optional)
  ↓
ALB (multi-AZ)
  ├─ AZ-A: ASG (EC2 instances)
  ├─ AZ-B: ASG (EC2 instances)
  └─ AZ-C: ASG (EC2 instances)
  ↓
RDS Multi-AZ
  ├─ Primary (AZ-A)
  └─ Standby (AZ-B)
```

**Multi-Region Application**:
```
Route 53 (Latency or Failover routing)
  ├─ Region 1
  │   ├─ ALB
  │   ├─ EC2 Auto Scaling
  │   └─ RDS (with read replica in Region 2)
  └─ Region 2
      ├─ ALB
      ├─ EC2 Auto Scaling
      └─ RDS (promoted from replica if Region 1 fails)

S3: Cross-Region Replication
DynamoDB: Global Tables
```

### Event-Driven Architecture

**Pattern 1: Fan-Out**
```
API Gateway → Lambda → SNS
                        ├─ SQS Queue 1 → Lambda
                        ├─ SQS Queue 2 → Lambda
                        └─ Email subscription
```

**Pattern 2: Queue Chain**
```
Upload to S3
  → S3 Event → SQS
  → Lambda (process)
  → SQS (results)
  → Lambda (notifications)
```

**Pattern 3: Event Bus**
```
AWS Services → EventBridge
Custom Apps → EventBridge
SaaS Apps → EventBridge
              ↓
         Event Rules (filtering)
              ↓
         Targets: Lambda, Step Functions, SQS, SNS, etc.
```

### Microservices Patterns

**Container-Based**:
```
Route 53 → ALB
            ├─ Target Group 1: ECS Service (Auth)
            ├─ Target Group 2: ECS Service (Orders)
            └─ Target Group 3: ECS Service (Inventory)

Path-based routing:
/auth/* → Auth service
/orders/* → Orders service
/inventory/* → Inventory service
```

**Serverless**:
```
API Gateway
  ├─ /users → Lambda → DynamoDB
  ├─ /orders → Lambda → DynamoDB
  └─ /products → Lambda → DynamoDB

API Gateway can:
- Throttling
- Caching
- Auth (Cognito, IAM, Lambda authorizer)
- Request/response transformation
```

### Disaster Recovery Strategies - Detailed

**Backup & Restore**:
```
Production (Region 1)          Backup (Region 2)
├─ EC2                        ├─ AMIs (periodic)
├─ EBS                        ├─ Snapshots (S3)
├─ RDS                        ├─ Snapshots
└─ S3                         └─ Replicated

RTO: Hours, RPO: Hours
Cost: $, Complexity: Low
```

**Pilot Light**:
```
Production (Region 1)          Pilot (Region 2)
├─ Full application           ├─ Core: RDS (running, small)
├─ Auto Scaling               ├─ AMIs ready
├─ Full RDS                   └─ Data: Continuously replicated

RTO: 10s of mins, RPO: Minutes  
Cost: $$, Complexity: Medium
```

**Warm Standby**:
```
Production (Region 1)          Warm Standby (Region 2)
├─ Full capacity              ├─ Reduced capacity (20-30%)
├─ Auto Scaling               ├─ Auto Scaling (can scale up)
└─ RDS (large)                └─ RDS (small, replicated)

RTO: Minutes, RPO: Seconds
Cost: $$$, Complexity: High
```

**Multi-Site (Hot-Hot)**:
```
Region 1 (Active)              Region 2 (Active)
├─ 50% capacity               ├─ 50% capacity
├─ Receives traffic           ├─ Receives traffic
└─ DynamoDB Global Table      └─ Same table

Route 53: Latency or Weighted routing

RTO: Real-time, RPO: Near-zero
Cost: $$$$, Complexity: Very High
```

---

## Cost Optimization Strategies

### EC2 Cost Optimization Checklist

1. **Right-sizing** (Use CloudWatch metrics):
   - Check CPU, memory, network usage over 2-4 weeks
   - Downsize underutilized instances (30-40% utilization)
   - Use AWS Compute Optimizer recommendations

2. **Pricing Models**:
   ```
   Workload Type              → Pricing Model
   ───────────────────────────────────────────
   24/7 production DB         → Reserved Instance (3-year)
   Batch processing (nightly) → Spot Instances
   Web servers (steady)       → Savings Plan (1-year)
   Dev/Test (9am-5pm)         → Scheduled Reserved or On-Demand
   Unpredictable spikes       → Auto Scaling with On-Demand
   ```

3. **Scheduling**:
   - Stop dev/test instances outside business hours
   - Use Instance Scheduler (Lambda + CloudWatch Events)
   - Savings: ~65% for 9-5, Monday-Friday usage

4. **Auto Scaling**:
   - Scale down during low traffic
   - Use predictive scaling for known patterns

### S3 Cost Optimization Strategies

**Storage Cost Reduction**:
1. Lifecycle policies (auto-transition)
2. Delete old versions (if versioning enabled)
3. Clean up incomplete multipart uploads
4. Use S3 Intelligent-Tiering for unknown patterns

**Transfer Cost Reduction**:
1. S3 Transfer Acceleration (faster uploads, no cost if not faster)
2. CloudFront (reduce origin requests)
3. S3 Select/Glacier Select (retrieve only needed data)
4. Compression before upload

**Request Cost Reduction**:
1. CloudFront caching (fewer S3 requests)
2. Batch operations instead of individual API calls
3. Use ListObjectsV2 (more efficient than V1)

### Database Cost Optimization

**RDS**:
- Right-size based on CloudWatch metrics
- Reserved Instances for production (up to 69% savings)
- Multi-AZ only for production (not dev/test)
- Delete old snapshots (lifecycle policy)
- Use Aurora Serverless v2 for variable workloads

**DynamoDB**:
- On-Demand → Provisioned for steady traffic (2.5x cost difference)
- Enable auto-scaling for provisioned
- Delete unused tables/indexes
- Use TTL to auto-delete expired items
- Reserved Capacity for predictable workloads

**Redshift**:
- Reserved Instances (up to 75% savings)
- Pause/Resume clusters (dev/test)
- Use DC2 for less than 500GB
- Use RA3 for larger datasets (separate compute/storage)

### Data Transfer Costs (Often Overlooked!)

**Most Expensive**:
- ❌ Internet out ($0.09/GB first 10TB)
- ❌ Cross-region replication

**Moderate**:
- Between AZs ($0.01/GB in/out)
- Between regions

**Free**:
- ✅ Internet IN (always free)
- ✅ Same AZ (if using private IP)
- ✅ S3 → CloudFront
- ✅ Between S3 and EC2 in same region
- ✅ CloudFront → Internet

**Optimization**:
- Use CloudFront for static content delivery (free S3→CF, cheaper CF→Internet)
- Keep resources in same AZ when possible
- Use VPC endpoints for S3/DynamoDB (no data transfer charges)

### Trusted Advisor Cost Optimization Checks

**Business/Enterprise Support includes**:
- Low utilization EC2 instances
- Idle RDS instances
- Underutilized EBS volumes
- Unassociated Elastic IPs
- Idle load balancers
- Reserved Instance optimization recommendations

**Cost Explorer + Right Sizing**:
- Historical cost analysis
- Forecast future costs
- Right-sizing recommendations
- Reserved Instance recommendations

---

## Quick Exam Tips

### Time Management
- 130 minutes ÷ 65 questions = 2 minutes per question
- Flag difficult questions, come back later
- No penalty for wrong answers (always guess!)

### Question Patterns
1. **"Most cost-effective"** → Look for Reserved Instances, Spot, Lifecycle policies
2. **"Minimum operational overhead"** → Managed services, serverless
3. **"High availability"** → Multi-AZ, Auto Scaling, multiple regions
4. **"Best performance"** → Aurora, ElastiCache, CloudFront, instance types
5. **"Least privilege"** → Most restrictive IAM policy
6. **"Compliance"** → Encryption, CloudHSM, audit logs (CloudTrail, Config)

### Elimination Strategy
- Eliminate obviously wrong answers first
- Usually 2 completely wrong, 1 plausible distractor, 1 correct
- Watch for answers that solve wrong problem

### Red Flags (Usually Wrong)
- Manually doing something AWS can automate
- Complex custom solutions when AWS has native service
- Over-provisioning for HA (e.g., "deploy in all regions")
- Solutions that violate security best practices

---

*Review these notes regularly, especially 2-3 days before your exam. Focus on areas where you miss practice questions.*

