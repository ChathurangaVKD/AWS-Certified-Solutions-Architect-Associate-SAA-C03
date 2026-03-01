# AWS SAA-C03 Flashcards - Smart Learning Guide

> **Learning Strategy**: Start from Section 1 (Fundamentals) and progress sequentially. Review Section 7 (Quick Reference) daily.

---

## 🎯 **NEW: Focused Review Resources for Weak Areas**

Having trouble with practice tests? Check out these targeted resources:

### 📊 **Track Your Progress**
- **[Test Results Tracker](14-Practice/TEST-RESULTS-TRACKER.md)** - Log practice test scores and identify weak areas

### 🎴 **Focused Flashcards**
- **[Focused Review Flashcards](14-Practice/FOCUSED-REVIEW-FLASHCARDS.md)** - 35 cards covering the most commonly missed topics

### 📚 **Deep Dive Study Notes**
- **[Weak Areas Study Notes](14-Practice/WEAK-AREAS-STUDY-NOTES.md)** - Comprehensive explanations of difficult concepts

### 📝 **Targeted Practice**
- **[Targeted Weak Area Questions](14-Practice/TARGETED-WEAK-AREA-QUESTIONS.md)** - 30+ practice questions on commonly missed topics

**Use these resources when you:**
- Score below 70% on practice tests
- Consistently miss questions on specific topics
- Need deeper understanding of complex concepts
- Want focused review before exam day

---

## 📋 Table of Contents
1. [AWS Fundamentals](#1-aws-fundamentals)
2. [Core Services Overview](#2-core-services-overview)
3. [Compute Services](#3-compute-services)
4. [Storage Services](#4-storage-services)
5. [Database Services](#5-database-services)
6. [Networking & Content Delivery](#6-networking--content-delivery)
7. [Security & Identity](#7-security--identity)
8. [Application Integration](#8-application-integration)
9. [Monitoring & Management](#9-monitoring--management)
10. [Analytics](#10-analytics)
11. [Migration & Transfer](#11-migration--transfer)
12. [Architecture Patterns](#12-architecture-patterns)
13. [Cost Optimization](#13-cost-optimization)
14. [Quick Reference & Exam Tips](#14-quick-reference--exam-tips)

---

## 1. AWS Fundamentals

### 1.1 AWS Global Infrastructure

```
┌──────────────────┬────────────────┬──────────────────┬─────────────────┐
│    Component     │    Scope       │     Count        │   Purpose       │
├──────────────────┼────────────────┼──────────────────┼─────────────────┤
│ Region           │ Geographic     │ 30+ globally     │ Data residency  │
│ Availability Zone│ Within Region  │ 3-6 per region   │ High availability│
│ Edge Location    │ Global         │ 400+ worldwide   │ Low latency CDN │
│ Local Zone       │ Metro areas    │ 15+ cities       │ Ultra-low latency│
└──────────────────┴────────────────┴──────────────────┴─────────────────┘
```

**💡 Memory Tip**: "**R**egions for **R**esidency, **A**Zs for **A**vailability, **E**dges for **E**xperience"

### 1.2 Well-Architected Framework (6 Pillars)

```
1. 🎯 OPERATIONAL EXCELLENCE  → Automate, improve, monitor
2. 🔒 SECURITY               → Protect data, systems, assets
3. 🔄 RELIABILITY            → Recover from failures, meet demand
4. ⚡ PERFORMANCE EFFICIENCY  → Use resources efficiently  
5. 💰 COST OPTIMIZATION      → Eliminate unnecessary costs
6. 🌱 SUSTAINABILITY         → Minimize environmental impact
```

**💡 Acronym**: "**O**wl **S**its **R**eally **P**eacefully **C**atching **S**almon" (OSRPCS)

### 1.3 Shared Responsibility Model

```
┌─────────────────────────────────────────────────────┐
│          CUSTOMER: "Security IN the Cloud"          │
├─────────────────────────────────────────────────────┤
│ ✓ Customer Data & Content                           │
│ ✓ Platform, Applications, IAM, Access Management    │
│ ✓ Operating System, Network & Firewall Config       │
│ ✓ Client-side & Server-side Encryption              │
│ ✓ Network Traffic Protection                        │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│           AWS: "Security OF the Cloud"              │
├─────────────────────────────────────────────────────┤
│ ✓ Hardware & AWS Global Infrastructure              │
│ ✓ Compute, Storage, Database, Networking Services   │
│ ✓ Regions, Availability Zones, Edge Locations       │
│ ✓ Physical security of data centers                 │
└─────────────────────────────────────────────────────┘
```

**💡 Memory Tip**: "AWS protects **OF** (infrastructure), You protect **IN** (configuration & data)"

### 📚 Learn More
- [AWS Fundamentals - Chapter Guide](./01-AWS-Fundamentals/README.md)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

---

## 2. Core Services Overview

### 2.1 Service Categories Map

#### Compute
```
┌─────────────────────────────────────────┐
│ EC2         → Virtual Servers           │
│ Lambda      → Serverless Functions      │
│ ECS/EKS     → Container Orchestration   │
│ Fargate     → Serverless Containers     │
│ Beanstalk   → PaaS (Just Upload Code)   │
│ Lightsail   → Simple VPS                │
└─────────────────────────────────────────┘
```

#### Storage
```
┌─────────────────────────────────────────┐
│ S3          → Object Storage            │
│ EBS         → Block Storage (EC2 disk)  │
│ EFS         → Network File System       │
│ FSx         → Managed File Systems      │
│ Glacier     → Archive Storage           │
│ Snow Family → Physical Data Transfer    │
└─────────────────────────────────────────┘
```

#### Database
```
┌─────────────────────────────────────────┐
│ RDS         → Managed Relational DB     │
│ Aurora      → AWS High-Perf Relational  │
│ DynamoDB    → Serverless NoSQL          │
│ Redshift    → Data Warehouse            │
│ ElastiCache → In-Memory Cache           │
│ Neptune     → Graph Database            │
└─────────────────────────────────────────┘
```

#### Networking
```
┌─────────────────────────────────────────┐
│ VPC         → Virtual Private Cloud     │
│ Route 53    → DNS & Traffic Management  │
│ CloudFront  → CDN (Content Delivery)    │
│ ALB/NLB     → Load Balancers            │
│ API Gateway → API Management            │
│ Direct Conn → Dedicated Network Link    │
└─────────────────────────────────────────┘
```

#### Security & Identity
```
┌─────────────────────────────────────────┐
│ IAM         → Users, Groups, Roles      │
│ Cognito     → User Authentication       │
│ Secrets Mgr → Credentials Management    │
│ KMS         → Encryption Key Management │
│ WAF         → Web Application Firewall  │
│ Shield      → DDoS Protection           │
│ GuardDuty   → Threat Detection          │
│ Macie       → Data Privacy (PII)        │
└─────────────────────────────────────────┘
```

#### Application Integration
```
┌─────────────────────────────────────────┐
│ SQS         → Message Queue             │
│ SNS         → Pub/Sub Messaging         │
│ EventBridge → Event Bus                 │
│ Step Func   → Workflow Orchestration    │
│ AppSync     → GraphQL API               │
│ MQ          → Managed Message Broker    │
└─────────────────────────────────────────┘
```

#### Monitoring & Management
```
┌─────────────────────────────────────────┐
│ CloudWatch  → Metrics & Logs            │
│ CloudTrail  → API Activity Audit        │
│ Config      → Resource Configuration    │
│ Systems Mgr → Operational Insights      │
│ Trusted Adv → Best Practice Checks      │
│ Health Dash → Service Health Status     │
└─────────────────────────────────────────┘
```

#### Analytics
```
┌─────────────────────────────────────────┐
│ Athena      → Query S3 with SQL         │
│ EMR         → Big Data (Hadoop/Spark)   │
│ Kinesis     → Real-time Streaming       │
│ Glue        → ETL Service               │
│ QuickSight  → Business Intelligence     │
│ Data Pipeline → Data Workflow          │
└─────────────────────────────────────────┘
```

#### Migration & Transfer
```
┌─────────────────────────────────────────┐
│ DMS         → Database Migration        │
│ SMS         → Server Migration          │
│ Snow Family → Physical Data Transfer    │
│ DataSync    → Online Data Transfer      │
│ Transfer    → SFTP/FTPS File Transfer   │
│ Migration Hub → Migration Tracking      │
└─────────────────────────────────────────┘
```

### 2.2 Quick Service Selection Guide

**When you need to...**

| Requirement | Choose This |
|------------|-------------|
| Store files (images, videos, backups) | **S3** |
| Run a virtual machine | **EC2** |
| Run code without managing servers | **Lambda** |
| Host a relational database | **RDS** or **Aurora** |
| Host a NoSQL database | **DynamoDB** |
| Create a private network | **VPC** |
| Distribute content globally | **CloudFront** |
| Send notifications | **SNS** |
| Queue messages | **SQS** |
| Monitor resources | **CloudWatch** |
| Manage user permissions | **IAM** |
| Encrypt data at rest | **KMS** |
| Protect against DDoS attacks | **Shield** |
| Detect threats and anomalies | **GuardDuty** |
| Audit API calls | **CloudTrail** |
| Orchestrate workflows | **Step Functions** |
| Stream real-time data | **Kinesis** |
| Query data in S3 with SQL | **Athena** |
| Migrate databases | **DMS** |
| Transfer large datasets | **Snow Family** or **DataSync** |
| Run big data analytics | **EMR** |
| Create business dashboards | **QuickSight** |
| Manage secrets and credentials | **Secrets Manager** |
| Web application firewall | **WAF** |
| Event-driven architecture | **EventBridge** |

### 📚 Learn More
- [AWS Services Overview](https://aws.amazon.com/products/)
- [AWS Service Categories](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
- [AWS Free Tier](https://aws.amazon.com/free/)

---

## 3. Compute Services

### 3.1 EC2 (Elastic Compute Cloud)

**What**: Virtual servers in the cloud

**Instance Types - Remember "FIGHT DR MCPXZ"**
```
F - FPGA              → Genomics, financial analysis
I - I/O Optimized     → NoSQL databases, data warehousing
G - GPU Graphics      → Machine learning, gaming
H - High Disk         → MapReduce, distributed file systems
T - Burstable (T2/T3) → Web servers, dev environments
D - Dense Storage     → Data warehouses, Hadoop
R - RAM Optimized     → In-memory databases, caches
M - General Purpose   → Application servers (balanced)
C - Compute Optimized → Batch processing, HPC
P - GPU (Pictures)    → Deep learning, rendering
X - Xtreme Memory     → SAP HANA, big data
Z - High Frequency    → Gaming, high-performance computing
```

**💡 Exam Focus**: T3 (burstable), M5 (general), C5 (compute), R5 (memory)

**Purchasing Options**
```
┌────────────────┬──────────┬────────────────────────┐
│     Option     │ Discount │      Best For          │
├────────────────┼──────────┼────────────────────────┤
│ On-Demand      │   0%     │ Short, unpredictable   │
│ Reserved 1yr   │ Up to 40%│ Steady-state workloads │
│ Reserved 3yr   │ Up to 72%│ Long-term predictable  │
│ Savings Plans  │ Up to 72%│ Flexible usage         │
│ Spot           │ Up to 90%│ Fault-tolerant batch   │
│ Dedicated Host │   0%     │ Licensing compliance   │
└────────────────┴──────────┴────────────────────────┘
```

**Placement Groups**
- **Cluster**: Low latency (same rack) - HPC
- **Spread**: High availability (different racks) - critical apps, max 7 per AZ
- **Partition**: Distributed apps (Hadoop, Cassandra)

### 3.2 Lambda

**What**: Run code without managing servers (serverless)

**Key Limits to Memorize**
```
⏱️  Max Execution Time: 15 minutes (900 seconds)
💾 Memory: 128 MB - 10 GB
📦 Deployment Package: 50 MB zipped, 250 MB unzipped
💿 /tmp Storage: 512 MB - 10 GB
🔢 Concurrent Executions: 1,000 (default)
📊 Environment Variables: 4 KB total
```

**Pricing**: Based on requests + duration (GB-seconds)
**Free Tier**: 1M requests/month + 400,000 GB-seconds

**💡 Use Cases**: Event-driven processing, APIs, data transformation, automation

### 3.3 Container Services

```
┌──────────┬─────────────────────────────────────┐
│  ECS     │ AWS native container orchestration  │
│          │ Launch: EC2 (you manage) or Fargate │
├──────────┼─────────────────────────────────────┤
│  EKS     │ Managed Kubernetes                  │
│          │ Use existing K8s skills             │
├──────────┼─────────────────────────────────────┤
│  Fargate │ Serverless containers               │
│          │ No EC2 management needed            │
├──────────┼─────────────────────────────────────┤
│  ECR     │ Container image registry            │
│          │ Like Docker Hub but private         │
└──────────┴─────────────────────────────────────┘
```

### 3.4 Elastic Beanstalk

**What**: Platform as a Service (PaaS) - just upload your code

**Supported Platforms**: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker

**AWS Manages**: Capacity, load balancing, auto-scaling, health monitoring
**You Control**: Application code

**💡 Use When**: You want to focus on code, not infrastructure

### 3.5 Auto Scaling

**Scaling Policies**
```
1. Target Tracking   → "Keep CPU at 50%"
2. Step Scaling      → "Add 1 at 70%, add 2 at 90%"
3. Scheduled Scaling → "Scale up at 8 AM weekdays"
4. Predictive        → ML-based forecasting
```

**Key Concepts**
- **Cooldown Period**: 300 seconds (5 min) default between activities
- **Launch Template**: Defines what to launch (AMI, instance type, etc.)
- **Desired Capacity**: Target number of instances
- **Min/Max**: Capacity boundaries

### 📚 Learn More
- [Compute Services - Chapter Guide](./03-Compute/README.md)
- [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [Amazon EKS Documentation](https://docs.aws.amazon.com/eks/)

---

## 4. Storage Services

### 4.1 S3 (Simple Storage Service)

**What**: Infinitely scalable object storage

**Key Concepts**
```
📦 Object Size: 0 bytes to 5 TB
🏷️  Bucket Names: 3-63 characters, globally unique
📤 Single PUT: Max 5 GB (use multi-part for larger)
💎 Durability: 99.999999999% (11 nines)
✅ Availability: 99.99% (Standard)
🔄 Requests/sec per prefix: 3,500 PUT/COPY/POST/DELETE, 5,500 GET/HEAD
```

**Storage Classes Comparison**
```
┌────────────────────┬──────┬─────┬─────────┬───────────┬─────────┐
│   Storage Class    │Avail │ AZs │ Min Days│ Retrieval │Use Case │
├────────────────────┼──────┼─────┼─────────┼───────────┼─────────┤
│ Standard           │99.99%│ ≥3  │  None   │ Instant   │Frequent │
│ Intelligent-Tier   │99.9% │ ≥3  │  None   │ Instant   │ Unknown │
│ Standard-IA        │99.9% │ ≥3  │   30    │ Instant   │Infreq   │
│ One Zone-IA        │99.5% │  1  │   30    │ Instant   │Infreq+OK│
│ Glacier Instant    │99.9% │ ≥3  │   90    │Millisec   │ Archive │
│ Glacier Flexible   │99.99%│ ≥3  │   90    │ 1-5 min   │ Archive │
│ Glacier Deep       │99.99%│ ≥3  │  180    │ 12 hours  │LongArch │
└────────────────────┴──────┴─────┴─────────┴───────────┴─────────┘

💰 COST: Standard > IA > Glacier Instant > Flexible > Deep Archive
```

**💡 Memory Tip**: "**S**tandard for **S**peed, **IA** for **I**nfrequent **A**ccess, **G**lacier for **G**oing to storage"

**Important S3 Features**

**1. Versioning**
- Keeps multiple versions of objects
- Protects from accidental deletion
- Once enabled, can only **suspend** (not disable)
- Deleting adds a **delete marker** (can be removed)

**2. Lifecycle Policies**
- Automate transitions between storage classes
- Expire objects after X days
- Example: Standard → IA (30d) → Glacier (90d) → Delete (365d)

**3. Replication**
- **CRR** (Cross-Region): DR, compliance, lower latency
- **SRR** (Same-Region): Log aggregation, live replication
- Requires **versioning enabled** on both buckets
- Can replicate to different storage class
- Replicate delete markers optionally

**4. Encryption**
```
SSE-S3  → AWS manages keys (AES-256) - default
SSE-KMS → AWS KMS keys (audit trail, control)
SSE-C   → Customer provides keys (you manage)
Client  → Encrypt before upload (client-side)
```

**5. S3 Transfer Acceleration**
- Upload to nearest edge location → faster to S3
- Use CloudFront edge network
- Good for global uploads

### 4.2 EBS (Elastic Block Store)

**What**: Block storage volumes for EC2 (like a hard drive)

**Volume Types**
```
┌────────────┬─────────┬────────┬─────────────────────┐
│    Type    │  IOPS   │  Size  │     Use Case        │
├────────────┼─────────┼────────┼─────────────────────┤
│ gp3 (SSD)  │3K-16K   │1GB-16TB│ General purpose     │
│            │         │        │ Cost-effective      │
├────────────┼─────────┼────────┼─────────────────────┤
│ gp2 (SSD)  │3K-16K   │1GB-16TB│ Boot volumes        │
│            │         │        │ Baseline performance│
├────────────┼─────────┼────────┼─────────────────────┤
│ io2 (SSD)  │Up to 64K│4GB-16TB│ Mission-critical DB │
│            │         │        │ Sustained IOPS      │
├────────────┼─────────┼────────┼─────────────────────┤
│ st1 (HDD)  │  500    │125GB-  │ Big data, logs      │
│            │         │ 16TB   │ Throughput optimized│
├────────────┼─────────┼────────┼─────────────────────┤
│ sc1 (HDD)  │  250    │125GB-  │ Cold data           │
│            │         │ 16TB   │ Lowest cost         │
└────────────┴─────────┴────────┴─────────────────────┘
```

**💡 Choose**: **SSD** for random I/O (databases), **HDD** for sequential (big data, logs)

**Key Features**
- **Scope**: AZ-specific (not regional)
- **Snapshots**: Stored in S3, incremental, can copy cross-region
- **Encryption**: KMS encryption at rest
- **Multi-Attach**: Only io1/io2, max 16 instances, same AZ

### 4.3 EFS (Elastic File System)

**What**: Managed NFS file system for Linux

**Key Features**
```
✅ Regional service (Multi-AZ)
✅ Shared across multiple EC2 instances
✅ Elastic - grows/shrinks automatically
✅ Pay for what you use
✅ POSIX-compliant file system
✅ Performance modes: General Purpose, Max I/O
✅ Throughput modes: Bursting, Provisioned
```

**Storage Classes**
- **Standard**: Frequent access
- **Infrequent Access (IA)**: Cost-optimized, automatic lifecycle

**💡 Use Case**: Shared file storage, content management, web serving, data analytics

### 4.4 FSx Family

```
┌──────────────┬────────────────────────────────────┐
│ FSx Windows  │ Windows SMB file system            │
│              │ Active Directory integration       │
│              │ Microsoft apps (SQL Server, etc.)  │
├──────────────┼────────────────────────────────────┤
│ FSx Lustre   │ High-performance computing (HPC)   │
│              │ ML, video processing, financial    │
│              │ Can link to S3 bucket              │
├──────────────┼────────────────────────────────────┤
│ FSx NetApp   │ NetApp ONTAP compatibility         │
│              │ Enterprise features                │
├──────────────┼────────────────────────────────────┤
│ FSx OpenZFS  │ Linux ZFS compatibility            │
│              │ High performance NAS               │
└──────────────┴────────────────────────────────────┘
```

### 4.5 Snow Family

**What**: Physical devices to migrate large amounts of data

```
┌───────────────┬──────────┬────────────────────────┐
│    Device     │ Capacity │      Use Case          │
├───────────────┼──────────┼────────────────────────┤
│ Snowcone      │ 8-14 TB  │ Edge computing, IoT    │
│               │          │ Smallest, portable     │
├───────────────┼──────────┼────────────────────────┤
│ Snowball Edge │ 80-210TB │ Large data migrations  │
│               │          │ Edge compute           │
├───────────────┼──────────┼────────────────────────┤
│ Snowmobile    │ 100 PB   │ Datacenter migration   │
│               │          │ Exabyte-scale (truck!) │
└───────────────┴──────────┴────────────────────────┘
```

**💡 Rule**: If transfer > 1 week over network → Use Snow Family

**OpsHub**: GUI software to manage Snow devices

### 4.6 Storage Comparison Summary

**S3 vs EBS vs EFS - Know the Difference!**
```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │      S3      │     EBS      │     EFS      │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Type        │ Object       │ Block        │ File (NFS)   │
│ Access      │ HTTP/API     │ Mount to EC2 │ Mount to EC2 │
│ Scope       │ Regional     │ AZ-specific  │ Regional     │
│ Sharing     │ Internet/URL │ Single EC2*  │ Multi-EC2    │
│ Max Size    │ Unlimited    │ 64 TB/vol    │ Unlimited    │
│ Use Case    │ Static files │ Instance disk│ Shared files │
│ Durability  │ 11 nines     │ 99.999%      │ 11 nines     │
│ Price Model │ Per GB stored│ Provisioned  │ Pay per use  │
└─────────────┴──────────────┴──────────────┴──────────────┘
* EBS Multi-Attach available for io1/io2 only
```

**💡 Decision Tree**:
- Object storage (images, backups) → **S3**
- Boot disk for EC2 → **EBS**
- Shared file system (Linux) → **EFS**
- Shared file system (Windows) → **FSx for Windows**
- HPC/ML workloads → **FSx for Lustre**

### 📚 Learn More
- [Storage Services - Chapter Guide](./04-Storage/README.md)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Amazon EBS Documentation](https://docs.aws.amazon.com/ebs/)
- [Amazon EFS Documentation](https://docs.aws.amazon.com/efs/)
- [Amazon FSx Documentation](https://docs.aws.amazon.com/fsx/)

---

## 5. Database Services

### 5.1 RDS (Relational Database Service)

**What**: Managed relational databases

**Supported Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora (AWS)

**Key Features**
```
✅ Automated backups (1-35 days retention, default 7)
✅ Automated patching
✅ Multi-AZ for high availability
✅ Read Replicas for scalability
✅ Storage auto-scaling
✅ Encryption at rest (KMS)
✅ Encryption in transit (SSL/TLS)
```

**Multi-AZ vs Read Replicas**
```
┌─────────────────┬──────────────┬───────────────────┐
│    Feature      │  Multi-AZ    │  Read Replicas    │
├─────────────────┼──────────────┼───────────────────┤
│ Purpose         │ HA/DR        │ Scalability       │
│ Replication     │ Synchronous  │ Asynchronous      │
│ Failover        │ Automatic    │ Manual promotion  │
│ Endpoint        │ One DNS name │ Each has own DNS  │
│ Backups From    │ Standby      │ Can use replica   │
│ Max Count       │ 1 standby    │ Up to 15 (Aurora) │
│ Cross-Region    │ No           │ Yes               │
│ Read Traffic    │ Standby=No   │ Yes               │
│ Use For         │ Availability │ Performance       │
└─────────────────┴──────────────┴───────────────────┘
```

**💡 Memory Tip**: "Multi-AZ = **A**vailability, Read Replicas = **R**eads"

### 5.2 Aurora

**What**: AWS high-performance relational database

**Key Facts**
```
🚀 5x faster than MySQL, 3x faster than PostgreSQL
💾 6 copies across 3 AZs (2 copies per AZ)
🔄 Self-healing with peer-to-peer replication
📖 Up to 15 Read Replicas (10ms lag)
⚡ Automated failover (< 30 seconds)
📈 Auto-scaling storage (10GB → 128TB)
⏪ Backtrack: Restore to any point without backup
🌐 Aurora Global: Cross-region (< 1 sec lag)
```

**Aurora Serverless**
- Auto-scaling based on demand
- Pay per second for capacity used
- Good for infrequent, intermittent, or unpredictable workloads

**💡 When to use Aurora**: Need highest performance for relational DB

### 5.3 DynamoDB

**What**: Fully managed serverless NoSQL database

**Key Concepts**
```
📄 Item Size: Max 400 KB
🔑 Partition Key: Required (hash key)
📊 Sort Key: Optional (range key)
🔍 GSI (Global Secondary Index): Max 20, create anytime
📌 LSI (Local Secondary Index): Max 5, only at table creation
⚡ Single-digit millisecond latency
🌐 Global Tables: Multi-region, multi-active
```

**Capacity Modes**
```
┌──────────────┬────────────────────────────────────┐
│ Provisioned  │ • Predictable traffic              │
│              │ • Specify RCU/WCU                  │
│              │ • Lower cost if usage predictable  │
├──────────────┼────────────────────────────────────┤
│ On-Demand    │ • Unpredictable traffic            │
│              │ • Pay per request                  │
│              │ • No capacity planning             │
└──────────────┴────────────────────────────────────┘
```

**DynamoDB Features**
- **Streams**: 24-hour change log (trigger Lambda)
- **DAX**: In-memory cache (microsecond latency)
- **Point-in-Time Recovery**: Restore to any time (last 35 days)
- **Global Tables**: Multi-region replication

**💡 Use DynamoDB**: Web apps, gaming, IoT, mobile apps (key-value access)

### 5.4 ElastiCache

**What**: Managed in-memory cache

```
┌────────────┬─────────────────────────────────────┐
│  Redis     │ • In-memory data structures         │
│            │ • Persistence, backup/restore       │
│            │ • Multi-AZ with auto-failover       │
│            │ • Read replicas for read scaling    │
│            │ • Pub/Sub, sorted sets, leaderboards│
│            │ • Geospatial data                   │
├────────────┼─────────────────────────────────────┤
│ Memcached  │ • Simple caching (no persistence)   │
│            │ • Multi-threaded architecture       │
│            │ • Horizontal partitioning (sharding)│
│            │ • No replication, no backup         │
│            │ • Simpler, faster for simple cache  │
└────────────┴─────────────────────────────────────┘
```

**💡 Choose**: **Redis** for HA/persistence/features, **Memcached** for simple distributed cache

### 5.5 Redshift

**What**: Petabyte-scale data warehouse for analytics

**Key Features**
```
📊 Columnar storage
🚀 MPP (Massively Parallel Processing)
💰 10x better performance than other warehouses
🔄 Automated snapshots to S3
🌐 Cross-region snapshot copy
📈 Concurrency Scaling (handle bursts)
📁 Redshift Spectrum: Query S3 directly
```

**Use Cases**: OLAP, Business Intelligence, reporting, analytics

**💡 Not for**: OLTP (use RDS/Aurora instead)

### 5.6 Database Selection Guide

```
Need a database?
├─ Relational (SQL)?
│  ├─ AWS-optimized, highest performance? → Aurora
│  ├─ Specific engine (Oracle, SQL Server)? → RDS
│  └─ Self-managed on EC2? → EC2 + database software
│
├─ NoSQL?
│  ├─ Key-value, serverless? → DynamoDB
│  ├─ Document (MongoDB compatible)? → DocumentDB
│  └─ Graph (relationships)? → Neptune
│
├─ Analytics/Data Warehouse?
│  └─ Petabyte-scale analytics? → Redshift
│
├─ In-memory cache?
│  ├─ Complex data structures, HA? → ElastiCache Redis
│  └─ Simple distributed cache? → ElastiCache Memcached
│
├─ Time-series data?
│  └─ IoT, DevOps metrics? → Timestream
│
└─ Immutable ledger?
   └─ Cryptographically verifiable? → QLDB
```

### 5.7 Database Comparison

**RDS vs DynamoDB vs Redshift**
```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │     RDS      │   DynamoDB   │   Redshift   │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Type        │ Relational   │ NoSQL        │ Data Warehouse│
│ Schema      │ Fixed        │ Flexible     │ Fixed        │
│ Scaling     │ Vertical     │ Horizontal   │ Horizontal   │
│ Query       │ SQL          │ Key-Value    │ SQL (OLAP)   │
│ Use Case    │ OLTP         │ Web/Mobile   │ Analytics    │
│ Latency     │ Milliseconds │ Single-digit │ Seconds      │
│ Best For    │ Transactions │ High traffic │ Reports      │
│ Max Size    │ 64 TB        │ Unlimited    │ Petabytes    │
└─────────────┴──────────────┴──────────────┴──────────────┘
```

**💡 Memory Tip**: "**R**DS = **R**elations, **D**ynamo = **D**ynamic, **R**edshift = **R**eports"

### 📚 Learn More
- [Database Services - Chapter Guide](./05-Database/README.md)
- [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/)
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Amazon Aurora Documentation](https://docs.aws.amazon.com/aurora/)
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/)
- [Amazon ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/)

---

## 6. Networking & Content Delivery

### 6.1 VPC (Virtual Private Cloud)

**What**: Your own isolated network in AWS

**CIDR Blocks**
```
Private IP Ranges (RFC 1918):
  10.0.0.0/8       → 10.0.0.0 - 10.255.255.255 (16M IPs)
  172.16.0.0/12    → 172.16.0.0 - 172.31.255.255 (1M IPs)
  192.168.0.0/16   → 192.168.0.0 - 192.168.255.255 (65K IPs)

VPC CIDR: Min /28 (16 IPs) → Max /16 (65,536 IPs)

AWS Reserves 5 IPs per Subnet:
  x.x.x.0   → Network address
  x.x.x.1   → VPC router
  x.x.x.2   → DNS server
  x.x.x.3   → Reserved for future use
  x.x.x.255 → Broadcast (not used but reserved)
```

**💡 Available IPs** = Total - 5 (e.g., /24 = 256 - 5 = 251 usable)

### 6.2 VPC Components

**Internet Gateway (IGW)**
- One per VPC
- HA, scalable, redundant
- Provides NAT for public IPv4
- Must add route to route table (0.0.0.0/0 → IGW)

**NAT Gateway vs NAT Instance**
```
┌─────────────┬──────────────┬──────────────┐
│   Feature   │ NAT Gateway  │ NAT Instance │
├─────────────┼──────────────┼──────────────┤
│ Managed by  │ AWS          │ You          │
│ Bandwidth   │ 5-45 Gbps    │ Instance type│
│ HA          │ HA in AZ     │ Manual script│
│ Cost        │ $/hr + $/GB  │ EC2 cost     │
│ Bastion use │ No           │ Yes          │
│ Security SG │ No (only NACL│ Yes          │
│ Maintenance │ AWS handles  │ You patch    │
└─────────────┴──────────────┴──────────────┘
```

**💡 Exam Tip**: NAT Gateway is preferred (managed, HA, scalable)

**VPC Peering**
- Connect two VPCs privately
- **Not transitive**: A↔B, B↔C does NOT mean A↔C
- Can peer across regions and accounts
- CIDR blocks must NOT overlap

**VPC Endpoints**
```
┌──────────────────┬────────────────────────────────┐
│ Gateway Endpoint │ • S3 and DynamoDB only         │
│                  │ • Route table entry            │
│                  │ • No cost                      │
├──────────────────┼────────────────────────────────┤
│ Interface        │ • Most AWS services            │
│ Endpoint         │ • ENI with private IP          │
│ (PrivateLink)    │ • Costs apply                  │
│                  │ • Powered by AWS PrivateLink   │
└──────────────────┴────────────────────────────────┘
```

**💡 Use**: Access AWS services without internet gateway

**Transit Gateway**
- Central hub connecting VPCs, on-premises
- Simplifies complex network topologies
- Transitive routing (solves peering limitation)
- Cross-region support
- Works with VPN and Direct Connect

### 6.3 Security Groups vs NACLs

```
┌──────────────┬───────────────┬──────────────┐
│   Feature    │ Security Group│    NACL      │
├──────────────┼───────────────┼──────────────┤
│ Level        │ Instance (ENI)│ Subnet       │
│ State        │ Stateful      │ Stateless    │
│ Rules        │ Allow only    │ Allow + Deny │
│ Processing   │ All rules     │ Order matters│
│ Return       │ Auto allowed  │ Must allow   │
│ Default      │ Deny all in   │ Allow all    │
│ Apply to     │ Specific ENI  │ All in subnet│
└──────────────┴───────────────┴──────────────┘
```

**💡 Key Difference**: 
- **Security Group** = Stateful (return traffic auto-allowed)
- **NACL** = Stateless (must explicitly allow return traffic)

**💡 Memory Tip**: "**SG** = **S**tateful at **G**ateway (instance), **NACL** = **N**eed **A**ll rules, **C**heck **L**ayer (subnet)"

### 6.4 Route 53

**What**: AWS DNS service with advanced routing

**Routing Policies**
```
┌───────────────────┬────────────────────────────────┐
│  Simple           │ Single resource, no health check│
├───────────────────┼────────────────────────────────┤
│  Weighted         │ Distribute by % (A/B testing)  │
├───────────────────┼────────────────────────────────┤
│  Latency          │ Route to lowest latency region │
├───────────────────┼────────────────────────────────┤
│  Failover         │ Active-passive DR setup        │
├───────────────────┼────────────────────────────────┤
│  Geolocation      │ Based on user's location       │
├───────────────────┼────────────────────────────────┤
│  Geoproximity     │ Based on proximity + bias      │
├───────────────────┼────────────────────────────────┤
│  Multi-value      │ Return multiple IPs w/health   │
└───────────────────┴────────────────────────────────┘
```

**Health Checks**
- Monitor endpoint health
- Interval: 30 seconds (standard) or 10 seconds (fast)
- Can trigger CloudWatch alarms
- Can monitor other health checks (calculated health checks)

**💡 Use Cases**:
- **Latency**: Best performance for global users
- **Failover**: Disaster recovery
- **Geolocation**: Content localization, compliance
- **Weighted**: Gradual migration, A/B testing

### 6.5 CloudFront

**What**: Global Content Delivery Network (CDN)

**Key Features**
```
🌐 400+ Edge Locations worldwide
⚡ Caches content close to users
🔒 DDoS protection (AWS Shield Standard included)
🛡️  Integrates with AWS WAF
🔐 HTTPS support, custom SSL certificates
📍 Geo-restriction capability
```

**Origins**: S3, ALB, EC2, HTTP server, MediaStore

**TTL**: Default 24 hours (customizable)

**Signed URLs/Cookies**: Control access to private content

**💡 Use CloudFront**: Global user base, static/dynamic content, video streaming

### 6.6 Load Balancers

```
┌─────────┬─────┬─────────────┬────────────────────────┐
│  Type   │Layer│  Protocol   │      Features          │
├─────────┼─────┼─────────────┼────────────────────────┤
│  ALB    │  7  │ HTTP/HTTPS  │ • Path/host routing    │
│         │     │ WebSocket   │ • Lambda targets       │
│         │     │ gRPC        │ • Container support    │
│         │     │             │ • Fixed hostname       │
├─────────┼─────┼─────────────┼────────────────────────┤
│  NLB    │  4  │ TCP/UDP/TLS │ • Extreme performance  │
│         │     │             │ • Static IP,Elastic IP │
│         │     │             │ • PrivateLink support  │
│         │     │             │ • Millions req/sec     │
├─────────┼─────┼─────────────┼────────────────────────┤
│  GWLB   │  3  │ IP Protocol │ • 3rd party appliances │
│         │     │             │ • Firewalls, IDS/IPS   │
│         │     │             │ • Transparent proxy    │
├─────────┼─────┼─────────────┼────────────────────────┤
│  CLB    │ 4&7 │ Legacy      │ • Classic (deprecated) │
│         │     │             │ • Don't use for new    │
└─────────┴─────┴─────────────┴────────────────────────┘
```

**💡 Choose**:
- **ALB**: HTTP/HTTPS, microservices, containers, Lambda
- **NLB**: TCP/UDP, extreme performance, static IP needed
- **GWLB**: Third-party virtual appliances

### 6.7 VPN vs Direct Connect

```
┌────────────────┬──────────────┬─────────────────┐
│   Feature      │     VPN      │ Direct Connect  │
├────────────────┼──────────────┼─────────────────┤
│ Connection     │ Over internet│ Private fiber   │
│ Setup Time     │ Minutes      │ Weeks to months │
│ Bandwidth      │ Up to 1.25Gb │ 1-100 Gbps      │
│ Cost           │ Low          │ High            │
│ Encryption     │ Built-in     │ Need VPN/MACsec │
│ Latency        │ Variable     │ Low, consistent │
│ Use Case       │ Quick, backup│ Dedicated, heavy│
└────────────────┴──────────────┴─────────────────┘
```

**💡 Exam Tip**: VPN for quick/cheap, Direct Connect for consistent/high-bandwidth

**Global Accelerator**
- Uses AWS global network
- 2 static Anycast IPs
- Improves global application performance
- Health checks, failover
- Good for non-HTTP (gaming, IoT, VoIP)

### 📚 Learn More
- [Networking Services - Chapter Guide](./06-Networking/README.md)
- [Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [Amazon CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [Elastic Load Balancing Documentation](https://docs.aws.amazon.com/elasticloadbalancing/)
- [Amazon Route 53 Documentation](https://docs.aws.amazon.com/route53/)
- [AWS Direct Connect Documentation](https://docs.aws.amazon.com/directconnect/)

---

## 7. Security & Identity

### 7.1 IAM (Identity and Access Management)

**Components**
```
┌──────────────────────────────────────────────────┐
│  Users    → Long-term credentials (people/apps)  │
│  Groups   → Collection of users                  │
│  Roles    → Temporary credentials (AWS services) │
│  Policies → JSON documents (permissions)         │
└──────────────────────────────────────────────────┘
```

**IAM Policy Structure**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",                    // Allow or Deny
    "Action": "s3:GetObject",             // What can be done
    "Resource": "arn:aws:s3:::bucket/*",  // Which resources
    "Condition": {}                       // Optional conditions
  }]
}
```

**Policy Evaluation Logic**
```
1. Explicit DENY → Always wins (highest priority)
2. Explicit ALLOW → Allowed if no deny exists
3. Default → Implicit deny (no statement = denied)
```

**💡 Memory Tip**: "**D**eny **A**lways **W**ins" (DAW)

**IAM Best Practices**
```
✅ Enable MFA for root and privileged users
✅ Create individual IAM users (never share)
✅ Use groups to assign permissions
✅ Grant least privilege
✅ Use roles for EC2 (not access keys)
✅ Rotate credentials regularly
✅ Enable CloudTrail for audit logging
✅ Use strong password policies
✅ Remove unused credentials

❌ NEVER use root for daily tasks
❌ NEVER share credentials
❌ NEVER embed access keys in code
```

**Identity Federation**
```
┌────────────────────┬──────────────────────────────┐
│ SAML 2.0           │ Enterprise (Active Directory)│
│ AWS SSO            │ Centralized multi-account    │
│ Cognito            │ Mobile/Web app users         │
│ OIDC               │ Google, Facebook, etc.       │
└────────────────────┴──────────────────────────────┘
```

**💡 Use Case**: SAML for enterprise, Cognito for customer apps

### 7.2 KMS (Key Management Service)

**What**: Manage encryption keys

**Key Types**
```
Symmetric (AES-256)  → Single key, most common
Asymmetric (RSA/ECC) → Public/private key pair
```

**Key Categories**
```
AWS Managed    → Free, auto-rotate yearly, AWS controls
Customer Managed → $1/month, you control rotation/policies
AWS Owned      → Free, AWS controls, you don't see
```

**Key Limits**
- **API Requests**: 5,500/sec (shared), can request increase to 30K
- **Encrypt/Decrypt**: Max 4 KB per call
- **Envelope Encryption**: For > 4 KB data

**💡 Important**: You never get the actual key, always call KMS API

### 7.3 AWS Security Services

```
┌───────────────┬────────────────────────────────────┐
│ CloudTrail    │ • Logs ALL API calls (audit)       │
│               │ • 90 days free, longer with trail  │
│               │ • Store in S3 for compliance       │
├───────────────┼────────────────────────────────────┤
│ GuardDuty     │ • Intelligent threat detection     │
│               │ • ML-based, analyzes CloudTrail,   │
│               │   VPC Flow Logs, DNS logs          │
├───────────────┼────────────────────────────────────┤
│ WAF           │ • Web Application Firewall (L7)    │
│               │ • Protect vs SQL injection, XSS    │
│               │ • Deploy on ALB, API GW, CloudFront│
├───────────────┼────────────────────────────────────┤
│ Shield        │ • DDoS protection                  │
│               │ • Standard: Free for all           │
│               │ • Advanced: $3K/month + features   │
├───────────────┼────────────────────────────────────┤
│ Inspector     │ • Automated security assessment    │
│               │ • Scans EC2, containers, Lambda    │
│               │ • Vulnerability management         │
├───────────────┼────────────────────────────────────┤
│ Macie         │ • Discover sensitive data (PII)    │
│               │ • ML-powered S3 data classification│
├───────────────┼────────────────────────────────────┤
│ Secrets Mgr   │ • Store & rotate secrets           │
│               │ • Auto-rotation for RDS            │
│               │ • $0.40/secret/month               │
├───────────────┼────────────────────────────────────┤
│ Parameter     │ • Store config & secrets           │
│ Store (SSM)   │ • Free tier available              │
│               │ • No auto-rotation (vs Secrets Mgr)│
├───────────────┼────────────────────────────────────┤
│ Certificate   │ • Free SSL/TLS certificates        │
│ Manager (ACM) │ • Auto-renewal                     │
│               │ • For ALB, CloudFront, API Gateway │
├───────────────┼────────────────────────────────────┤
│ Cognito       │ • User authentication for apps     │
│               │ • User pools + identity pools      │
│               │ • Social & enterprise federation   │
└───────────────┴────────────────────────────────────┘
```

**Secrets Manager vs Parameter Store**
```
┌──────────────────┬────────────────┬──────────────────┐
│    Feature       │ Secrets Manager│ Parameter Store  │
├──────────────────┼──────────────────┼──────────────────┤
│ Auto-rotation    │ Yes (RDS, etc.)│ No               │
│ Cost             │ $0.40/secret   │ Free tier available│
│ Integration      │ RDS, Redshift  │ All AWS services │
│ Max value size   │ 64 KB          │ 8 KB (advanced)  │
│ Force rotation   │ Built-in       │ Manual           │
│ Use for          │ DB passwords   │ Config parameters│
└──────────────────┴────────────────┴──────────────────┘
```

**💡 Choose**: Secrets Manager for database credentials, Parameter Store for app configuration

### 7.4 Encryption Summary

**At Rest**
- S3: SSE-S3 (default), SSE-KMS, SSE-C, client-side
- EBS: KMS encryption (checkbox at launch)
- RDS: KMS encryption (must enable at creation)
- DynamoDB: KMS encryption

**In Transit**
- All AWS services support TLS/SSL
- Enforce HTTPS on S3, CloudFront, API Gateway
- VPN for site-to-site encryption

### 📚 Learn More
- [Security Services - Chapter Guide](./07-Security/README.md)
- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
- [AWS KMS Documentation](https://docs.aws.amazon.com/kms/)
- [AWS Secrets Manager Documentation](https://docs.aws.amazon.com/secretsmanager/)
- [AWS WAF Documentation](https://docs.aws.amazon.com/waf/)
- [AWS Shield Documentation](https://docs.aws.amazon.com/shield/)
- [AWS Security Best Practices](https://docs.aws.amazon.com/security/)

---

## 8. Application Integration

### 8.1 SQS (Simple Queue Service)

**What**: Fully managed message queue service

**Queue Types**
```
┌──────────────┬────────────────────────────────────┐
│ Standard     │ • Unlimited throughput             │
│              │ • At-least-once delivery (possible │
│              │   duplicates)                      │
│              │ • Best-effort ordering             │
├──────────────┼────────────────────────────────────┤
│ FIFO         │ • 300 msg/sec (3,000 with batching)│
│              │ • Exactly-once processing          │
│              │ • Strict ordering (FIFO)           │
│              │ • Name must end with .fifo         │
└──────────────┴────────────────────────────────────┘
```

**Key Parameters**
```
📦 Max Message Size: 256 KB
⏱️  Message Retention: 1 minute to 14 days (default 4 days)
👁️  Visibility Timeout: 0-12 hours (default 30 seconds)
🔁 Long Polling: 1-20 seconds (reduces empty responses)
⏲️  Delay Queue: 0-15 minutes (delay all messages)
💀 Dead Letter Queue: Store failed messages
```

**💡 Use Case**: Decouple application components, async processing

### 8.2 SNS (Simple Notification Service)

**What**: Pub/Sub messaging service

**Model**: Publisher → Topic → Subscribers

**Subscribers**
- Email / Email-JSON
- HTTP/HTTPS endpoints
- SMS text messages
- SQS queues (fan-out pattern)
- Lambda functions
- Mobile push notifications
- Kinesis Data Firehose

**Features**
- Message filtering
- FIFO topics (with SQS FIFO)
- Message attributes
- Delivery retries

**💡 Use Case**: Send notifications to multiple subscribers, fan-out to SQS

### 8.3 EventBridge (CloudWatch Events)

**What**: Serverless event bus

**Components**
```
Event Bus → Rules → Targets
```

**Event Sources**
- AWS services (S3, EC2, RDS, etc.)
- Custom applications (PutEvents API)
- SaaS partners (Zendesk, Datadog, Shopify)

**Targets** (20+ options)
- Lambda, Step Functions
- SQS, SNS, Kinesis
- EC2, ECS, Batch
- Systems Manager

**💡 Use Case**: Event-driven architectures, scheduled tasks (cron), SaaS integration

### 8.4 Step Functions

**What**: Visual workflow orchestration

**Workflow Types**
```
┌──────────────┬────────────────────────────────────┐
│ Standard     │ • Max 1 year execution             │
│              │ • Exactly-once execution           │
│              │ • Full execution history           │
├──────────────┼────────────────────────────────────┤
│ Express      │ • Max 5 minutes execution          │
│              │ • At-least-once execution          │
│              │ • High-volume event processing     │
└──────────────┴────────────────────────────────────┘
```

**Features**
- Error handling & retries
- Human approval steps
- Parallel processing
- Wait states
- Integration with 200+ AWS services

**💡 Use Case**: Order processing, ETL jobs, multi-step workflows

### 8.5 API Gateway

**What**: Create, publish, and manage APIs

**API Types**
- **REST API**: RESTful APIs
- **HTTP API**: Lower latency, lower cost (simpler)
- **WebSocket API**: Real-time two-way communication

**Features**
- Request/response transformation
- API versioning & stages
- Caching
- Request throttling
- API keys & usage plans
- CORS support
- Custom authorizers (Lambda)

**Limits**
- Timeout: 29 seconds
- Payload size: 10 MB

**💡 Integrations**: Lambda, HTTP endpoints, AWS services

### 8.6 Integration Patterns Comparison

**SQS vs SNS vs EventBridge**
```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Feature   │     SQS      │     SNS      │ EventBridge  │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Pattern     │ Queue (pull) │ Pub/Sub(push)│ Event routing│
│ Consumers   │ 1 consumer   │ Many         │ Many (rules) │
│ Retention   │ Up to 14 days│ No storage   │ No storage   │
│ Order       │ FIFO option  │ No guarantee │ No guarantee │
│ Filtering   │ No           │ Yes          │ Yes (advanced│
│ Best For    │ Work queues  │ Fan-out      │ Event-driven │
└─────────────┴──────────────┴──────────────┴──────────────┘
```

**💡 Memory Tip**: "**SQS** = **Q**ueue, **SNS** = **N**otify **S**ubscribers, **EventBridge** = **E**vents **B**us"

### 📚 Learn More
- [Application Integration - Chapter Guide](./08-Application-Integration/README.md)
- [Amazon SQS Documentation](https://docs.aws.amazon.com/sqs/)
- [Amazon SNS Documentation](https://docs.aws.amazon.com/sns/)
- [Amazon EventBridge Documentation](https://docs.aws.amazon.com/eventbridge/)
- [AWS Step Functions Documentation](https://docs.aws.amazon.com/step-functions/)

---

## 9. Monitoring & Management

### 9.1 CloudWatch

**What**: Monitoring and observability service

**CloudWatch Metrics**
```
Default EC2 Metrics (5 min, 1 min with detailed):
  ✅ CPU Utilization
  ✅ Network In/Out
  ✅ Disk Read/Write
  ✅ Status Checks
  
Need CloudWatch Agent for:
  ❌ Memory utilization
  ❌ Disk space usage
  ❌ Process-level metrics
```

**Custom Metrics**
- Standard resolution: 1 minute
- High resolution: 1 second
- Use PutMetricData API

**CloudWatch Alarms**
- States: OK, ALARM, INSUFFICIENT_DATA
- Actions: Auto Scaling, EC2 actions, SNS
- Based on metric thresholds or anomaly detection

**CloudWatch Logs**
```
Hierarchy: Log Groups → Log Streams → Log Events

Sources:
  • CloudWatch Agent (EC2, on-prem)
  • Lambda functions
  • VPC Flow Logs
  • CloudTrail
  • Route 53 DNS queries
  • ECS/EKS containers
```

**Features**
- **Metric Filters**: Create metrics from logs
- **Log Insights**: Query language for analysis
- **Subscriptions**: Stream to Kinesis, Lambda, OpenSearch
- **Retention**: Never expire to 10 years
- **Export to S3**: Batch export (up to 12 hours)

### 9.2 CloudTrail

**What**: AWS API call logging (audit trail)

**Key Facts**
```
📝 Logs ALL API calls in AWS account
🕐 90 days event history (free, no trail needed)
💾 Create trail to store in S3 indefinitely
🔍 Integrate with CloudWatch Logs for alarms
🌐 Multi-region trail option
✅ Log file integrity validation
```

**Use Cases**
- Compliance and auditing
- Security analysis
- Troubleshooting
- Track resource changes

**💡 Answers**: "WHO did WHAT, WHEN, and WHERE"

### 9.3 AWS Config

**What**: Track resource configuration changes

**Key Features**
```
📸 Continuous recording of configurations
📊 Configuration history and snapshots
✅ Compliance checking with Config Rules
🔔 Notifications on configuration changes
📈 Configuration timeline
```

**Config Rules**
- Managed rules (AWS-provided)
- Custom rules (Lambda-based)
- Evaluate compliance automatically
- Trigger remediation actions

**💡 Answers**: "What did my resources look like at time X?"

### 9.4 Monitoring Services Comparison

```
┌─────────────┬───────────────────────────────────┐
│ CloudTrail  │ WHO did WHAT, WHEN, WHERE         │
│             │ API call history (audit log)      │
│             │ Governance, compliance, audit     │
├─────────────┼───────────────────────────────────┤
│ CloudWatch  │ Performance monitoring            │
│             │ Metrics, logs, alarms, dashboards │
│             │ Operational health                │
├─────────────┼───────────────────────────────────┤
│ Config      │ Resource configuration changes    │
│             │ Compliance, inventory, history    │
│             │ "What did it look like before?"   │
├─────────────┼───────────────────────────────────┤
│ X-Ray       │ APPLICATION tracing               │
│             │ Distributed request tracing       │
│             │ Performance bottlenecks           │
└─────────────┴───────────────────────────────────┘
```

**💡 Memory Tip**: "**Watch** performance, **Trail** actions, **Config** compliance, **X-Ray** traces"

### 9.5 Trusted Advisor

**What**: Best practice recommendations

**Check Categories (5)**
```
1. Cost Optimization     → Reduce costs
2. Performance          → Improve performance
3. Security             → Close security gaps
4. Fault Tolerance      → Increase resilience
5. Service Limits       → Avoid hitting limits
```

**Support Plan Differences**
- **Basic/Developer**: 7 core checks
- **Business/Enterprise**: All checks + API access

### 9.6 Systems Manager

**What**: Manage and configure AWS and on-premises resources

**Key Features**
```
📋 Session Manager    → SSH without opening ports
🔧 Run Command        → Execute commands at scale
📦 Patch Manager      → Automate OS patching
📊 Inventory          → Collect software inventory
💾 Parameter Store    → Store config & secrets
🔧 State Manager      → Maintain desired state
📄 Documents          → Define actions to perform
```

**💡 Session Manager**: Access EC2 without SSH keys or bastions (IAM-based)

### 📚 Learn More
- [Monitoring & Management - Chapter Guide](./09-Monitoring/README.md)
- [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [AWS Config Documentation](https://docs.aws.amazon.com/config/)
- [AWS Systems Manager Documentation](https://docs.aws.amazon.com/systems-manager/)
- [AWS Trusted Advisor Documentation](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

---

## 10. Analytics

### 10.1 Athena

**What**: Serverless SQL queries on S3 data

**Key Facts**
```
💰 Pricing: $5 per TB scanned
📊 Query formats: CSV, JSON, Parquet, ORC, Avro
🚀 Serverless (no infrastructure)
📁 Uses AWS Glue Data Catalog for schemas
```

**Performance Optimization**
- Use columnar formats (Parquet, ORC) - less scan
- Compress data
- Partition data (reduce scan)
- Use larger files (> 128 MB)

**💡 Use Case**: Ad-hoc queries, log analysis, one-time reports

### 10.2 Kinesis Services

```
┌────────────────────┬─────────────────────────────┐
│ Kinesis Data       │ Real-time data streaming    │
│ Streams            │ Producers → Shards →        │
│                    │ Consumers                   │
│                    │ Retention: 1-365 days       │
├────────────────────┼─────────────────────────────┤
│ Kinesis Data       │ Load streaming data to      │
│ Firehose           │ S3, Redshift, ElasticSearch │
│                    │ Near real-time (60s buffer) │
│                    │ Serverless, auto-scaling    │
├────────────────────┼─────────────────────────────┤
│ Kinesis Data       │ Real-time analytics with    │
│ Analytics          │ SQL or Apache Flink         │
│                    │ Serverless                  │
└────────────────────┴─────────────────────────────┘
```

**💡 Choose**: Streams for custom processing, Firehose for AWS destinations

### EMR (Elastic MapReduce)

```
Purpose: Big data processing frameworks
Frameworks: Hadoop, Spark, HBase, Presto, Flink
Use Cases:
  • Log analysis
  • Machine learning
  • ETL at scale
  • Financial analysis

Cluster Types:
  • Master: Coordinate (always on)
  • Core: Run tasks, store data (HDFS)
  • Task: Run tasks only (spot instances)
```

### Glue

```
Components:
  • Glue Crawler: Discover schema, populate catalog
  • Glue Data Catalog: Central metadata repository
  • Glue ETL Jobs: Transform data (Spark)
  • Glue DataBrew: Visual data preparation

Use Cases:
  • ETL pipelines (serverless)
  • Schema discovery
  • Data catalog for Athena, EMR, Redshift
```

### Redshift

```
What: Petabyte-scale data warehouse
Based on: PostgreSQL (but not for OLTP)
Architecture: Columnar storage, MPP
Performance: 10x faster than other warehouses

Features:
  • Redshift Spectrum: Query S3 directly
  • Enhanced VPC routing
  • Snapshots to S3 (manual or automated)
  • Cross-region snapshot copy
  • Concurrency Scaling

Use Case: OLAP, BI, analytics, reporting
```

### QuickSight

```
What: Serverless BI (Business Intelligence) service
Features:
  • Interactive dashboards
  • ML-powered insights
  • Embedded analytics
  • Pay-per-session pricing

Data Sources:
  • RDS, Aurora, Redshift, Athena
  • S3, OpenSearch
  • SaaS (Salesforce, Jira)
  • On-premises databases
```

### 📚 Learn More
- [Analytics Services - Chapter Guide](./11-Analytics/README.md)
- [Amazon Kinesis Documentation](https://docs.aws.amazon.com/kinesis/)
- [Amazon Athena Documentation](https://docs.aws.amazon.com/athena/)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [Amazon EMR Documentation](https://docs.aws.amazon.com/emr/)
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/)
- [Amazon QuickSight Documentation](https://docs.aws.amazon.com/quicksight/)

---

## 11. Migration & Transfer

### 11.1 Database Migration Service (DMS)

**What**: Migrate databases to AWS

**Migration Types**
```
Homogeneous:   Oracle → Oracle (same engine)
Heterogeneous: Oracle → Aurora (different, use SCT)

Modes:
  • Full load
  • Full load + CDC (Change Data Capture)
  • CDC only
```

**Key Advantage**: Source database stays online during migration

**SCT (Schema Conversion Tool)**: Convert schemas for heterogeneous migrations

### 11.2 DataSync

**What**: Automated data transfer service

```
From: On-premises (NFS/SMB) → AWS
To: S3, EFS, FSx

Features:
  • 10x faster than open-source tools
  • Bandwidth throttling
  • Data validation & verification
  • Incremental transfers
  • Scheduling
```

**💡 Use Case**: One-time migration, ongoing replication to AWS

### 11.3 Migration Strategies (6 R's)

```
1. REHOST      → "Lift & Shift" - Move as-is (fastest)
2. REPLATFORM  → "Lift & Optimize" - Minor cloud optimizations
3. REPURCHASE  → "Drop & Shop" - Move to SaaS
4. REFACTOR    → "Re-architect" - Cloud-native rebuild
5. RETIRE      → Turn off what you don't need
6. RETAIN      → Keep on-premises (for now)
```

**💡 Most Common**: Rehost (70%) for quick wins, then optimize

### 11.4 Transfer Family

**What**: SFTP/FTPS/FTP to S3 or EFS

**Use Case**: Third parties upload files to S3 using FTP clients

### 📚 Learn More
- [Migration Services - Chapter Guide](./10-Migration/README.md)
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/)
- [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/)
- [AWS DataSync Documentation](https://docs.aws.amazon.com/datasync/)
- [AWS Snow Family Documentation](https://docs.aws.amazon.com/snowball/)
- [AWS Transfer Family Documentation](https://docs.aws.amazon.com/transfer/)

---

## 12. Architecture Patterns

### 12.1 High Availability Web Application

```
┌─────────────────────────────────────────────┐
│  Users → Route 53 (health checks)           │
│           ↓                                  │
│        CloudFront (CDN)                      │
│           ↓                                  │
│        ALB (Multi-AZ)                        │
│           ↓                                  │
│     Auto Scaling Group (Multi-AZ)           │
│           ↓                                  │
│     RDS Multi-AZ or Aurora                  │
│           ↓                                  │
│     S3 (static assets)
  • Error handling and retry logic
  • Human approval steps
  • Parallel processing
```

---

## 📊 Monitoring & Management (Module 09)

### CloudWatch Metrics & Alarms

```
Default EC2 Metrics (every 5 min, or 1 min detailed):
  ✅ CPU Utilization
  ✅ Network In/Out
  ✅ Disk Read/Write
  ✅ Status Checks
  ❌ Memory (need CloudWatch Agent)
  ❌ Disk Space (need CloudWatch Agent)

Custom Metrics:
  • PutMetricData API
  • Standard: 1-minute resolution
  • High-resolution: 1-second resolution

Alarm States:
  • OK - Within threshold
  • ALARM - Breached threshold
  • INSUFFICIENT_DATA - Not enough data

Alarm Actions:
  • Auto Scaling (scale in/out)
  • EC2 actions (stop, terminate, reboot, recover)
  • SNS notifications
```

### CloudWatch Logs

```
Hierarchy:
  Log Groups → Log Streams → Log Events

Log Sources:
  • SDK/CloudWatch Agent
  • Elastic Beanstalk
  • ECS containers
  • Lambda functions
  • VPC Flow Logs
  • API Gateway
  • CloudTrail (with filter)
  • Route 53 DNS queries

Features:
  • Metric Filters: Create metrics from logs
  • Log Insights: Query language for analysis
  • Subscriptions: Real-time to Kinesis, Lambda
  • Retention: Never expire to 10 years
  • Export to S3 (batch)
```

### CloudTrail vs CloudWatch vs Config

```
┌─────────────┬───────────────────────────────────┐
│ CloudTrail  │ WHO did WHAT, WHEN, WHERE         │
│             │ API call history (audit log)      │
│             │ Governance, compliance, audit     │
├─────────────┼───────────────────────────────────┤
│ CloudWatch  │ Performance monitoring            │
│             │ Metrics, logs, alarms, dashboards │
│             │ Operational health                │
├─────────────┼───────────────────────────────────┤
│ Config      │ Resource configuration changes    │
│             │ Compliance, inventory, history    │
│             │ "What did it look like before?"   │
└─────────────┴───────────────────────────────────┘

REMEMBER: Trail=Audit, Watch=Monitor, Config=Compliance
```

---

## 🚚 Migration & Transfer (Module 10)

### 6 R's Migration Strategy

```
1. Rehost        → Lift & Shift (fast, no changes)
2. Replatform    → Lift & Optimize (minor changes)
3. Repurchase    → Drop & Shop (move to SaaS)
4. Refactor      → Re-architect (cloud-native)
5. Retire        → Turn off unused apps
6. Retain        → Keep on-premises (for now)

EXAM TIP: Most migrations use Rehost (quick wins)
```

### AWS DataSync

```
Purpose: Automated data transfer
From: On-premises NFS/SMB → AWS storage
To: S3, EFS, FSx
Features:
  • 10x faster than open-source tools
  • Bandwidth throttling
  • Data validation
  • Encryption in-transit (TLS)
  • Incremental transfers
  • Schedule tasks

Use Case: Migrate large datasets, ongoing replication
```

### Database Migration Service (DMS)

```
Migration Types:
  • Homogeneous: Oracle → Oracle
  • Heterogeneous: Oracle → Aurora (use SCT)

Replication:
  • Full load
  • Full load + CDC (Change Data Capture)
  • CDC only

Sources: Oracle, SQL Server, MySQL, PostgreSQL, MongoDB
Targets: RDS, Aurora, Redshift, DynamoDB, S3

EXAM TIP: DMS keeps source DB online during migration
```

### Snow Family

```
┌───────────────┬──────────┬────────────────────┐
│    Device     │ Capacity │   Use When         │
├───────────────┼──────────┼────────────────────┤
│ Snowcone      │ 8-14 TB  │ Edge computing,IoT │
│ Snowball Edge │ 80-210TB │ Data migration,    │
│               │          │ edge compute       │
│ Snowmobile    │ 100 PB   │ Datacenter exit    │
└───────────────┴──────────┴────────────────────┘

Rule: If > 1 week over network → Use Snow
OpsHub: GUI to manage Snow devices
```

---

## 📈 Analytics Deep Dive (Module 11)

### Athena

```
What: Serverless SQL queries on S3
Pricing: $5 per TB scanned
Format: CSV, JSON, Parquet, ORC, Avro
Use Case: Ad-hoc queries, log analysis

Performance Tips:
  • Use columnar formats (Parquet, ORC)
  • Compress data
  • Partition data
  • Use larger files (avoid small files)

Integration: AWS Glue Data Catalog for schema
```

### Kinesis Services

```
┌────────────────────┬─────────────────────────────┐
│ Kinesis Data       │ Real-time data streaming    │
│ Streams            │ Producers → Shards →        │
│                    │ Consumers                   │
│                    │ Retention: 1-365 days       │
├────────────────────┼─────────────────────────────┤
│ Kinesis Data       │ Load streaming data to      │
│ Firehose           │ S3, Redshift, ElasticSearch │
│                    │ Near real-time (60s buffer) │
│                    │ Serverless, auto-scaling    │
├────────────────────┼─────────────────────────────┤
│ Kinesis Data       │ Real-time analytics with    │
│ Analytics          │ SQL or Apache Flink         │
│                    │ Serverless                  │
└────────────────────┴─────────────────────────────┘
```

CHOOSE: Streams for custom processing, Firehose for AWS destinations

### EMR (Elastic MapReduce)

```
Purpose: Big data processing frameworks
Frameworks: Hadoop, Spark, HBase, Presto, Flink
Use Cases:
  • Log analysis
  • Machine learning
  • ETL at scale
  • Financial analysis

Cluster Types:
  • Master: Coordinate (always on)
  • Core: Run tasks, store data (HDFS)
  • Task: Run tasks only (spot instances)
```

### Glue

```
Components:
  • Glue Crawler: Discover schema, populate catalog
  • Glue Data Catalog: Central metadata repository
  • Glue ETL Jobs: Transform data (Spark)
  • Glue DataBrew: Visual data preparation

Use Cases:
  • ETL pipelines (serverless)
  • Schema discovery
  • Data catalog for Athena, EMR, Redshift
```

### Redshift

```
What: Petabyte-scale data warehouse
Based on: PostgreSQL (but not for OLTP)
Architecture: Columnar storage, MPP
Performance: 10x faster than other warehouses

Features:
  • Redshift Spectrum: Query S3 directly
  • Enhanced VPC routing
  • Snapshots to S3 (manual or automated)
  • Cross-region snapshot copy
  • Concurrency Scaling

Use Case: OLAP, BI, analytics, reporting
```

### QuickSight

```
What: Serverless BI (Business Intelligence) service
Features:
  • Interactive dashboards
  • ML-powered insights
  • Embedded analytics
  • Pay-per-session pricing

Data Sources:
  • RDS, Aurora, Redshift, Athena
  • S3, OpenSearch
  • SaaS (Salesforce, Jira)
  • On-premises databases
```

---

## 🏛️ Architecture Patterns (Module 12)

### Serverless Architecture

```
Architecture:
  Users → API Gateway → Lambda → DynamoDB
                        ↓
                       S3 (for files)

Benefits:
  ✅ No server management
  ✅ Auto-scaling
  ✅ Pay per use
  ✅ High availability built-in

Use Case: Web apps, APIs, real-time processing
```

### Event-Driven Architecture

```
Pattern:
  S3 Upload → EventBridge → Lambda → Process
  DynamoDB Change → Stream → Lambda → Alert
  
Components:
  • Event Source: S3, DynamoDB, API Gateway
  • Event Router: EventBridge, SNS
  • Event Consumer: Lambda, Step Functions
  
Benefits:
  ✅ Loose coupling
  ✅ Scalability
  ✅ Flexibility
```

### Multi-Tier HA Architecture

```
Layers:
  1. CDN: CloudFront
  2. DNS: Route 53 (health checks)
  3. Load Balancer: ALB/NLB (Multi-AZ)
  4. Compute: EC2 Auto Scaling (Multi-AZ)
  5. Database: RDS Multi-AZ or Aurora
  6. Cache: ElastiCache (Multi-AZ)
  7. Storage: S3 (cross-region replication)

Key Principles:
  • Eliminate single points of failure
  • Multi-AZ deployment
  • Auto Scaling
  • Self-healing (health checks)
```

### Disaster Recovery Strategies

```
┌─────────────────┬──────┬──────┬────────────────┐
│   Strategy      │ RTO  │ RPO  │  Cost          │
├─────────────────┼──────┼──────┼────────────────┤
│ Backup&Restore  │Hours │Hours │ $              │
│ Pilot Light     │10min │Minutes│ $$            │
│ Warm Standby    │Minutes│Seconds│ $$$          │
│ Multi-Site      │Real-time│0   │ $$$$          │
└─────────────────┴──────┴──────┴────────────────┘

RTO: Recovery Time Objective
RPO: Recovery Point Objective
```

---

## 🔢 Critical Numbers & Limits (Must Memorize!)

### Lambda Limits
```
• Max execution time: 15 minutes (900 seconds)
• Memory: 128 MB - 10 GB
• /tmp storage: 512 MB - 10 GB
• Deployment package: 50 MB (zipped), 250 MB (unzipped)
• Concurrent executions: 1,000 (default, can increase)
• Environment variables: 4 KB total
```

### S3 Numbers
```
• Max object size: 5 TB
• Multipart upload: Required for > 5 GB, recommended for > 100 MB
• Bucket name: 3-63 characters, globally unique
• PUT/COPY/POST/DELETE: 3,500 requests/sec per prefix
• GET/HEAD: 5,500 requests/sec per prefix
• Durability: 99.999999999% (11 nines)
• S3 Standard availability: 99.99%
• Lifecycle min days: Standard-IA (30), Glacier (90), Deep Archive (180)
```

### EC2 & Auto Scaling
```
• Placement group spread: Max 7 instances per AZ
• Default cooldown period: 300 seconds (5 minutes)
• EBS volume: 1 GB - 64 TB (depending on type)
• EBS Multi-Attach: Max 16 instances (io1/io2 only, same AZ)
• Instance metadata: http://169.254.169.254/latest/meta-data/
```

### RDS & Database
```
• RDS backup retention: 1-35 days (default 7)
• RDS Multi-AZ failover: 60-120 seconds
• Aurora Read Replicas: Up to 15
• Aurora failover: < 30 seconds
• DynamoDB item size: Max 400 KB
• DynamoDB GSI: Max 20 per table
• DynamoDB LSI: Max 5 per table (only at creation)
• ElastiCache Redis: Max 500 nodes per cluster
• Redshift: Max 128 compute nodes
```

### VPC & Networking
```
• VPCs per region: 5 (soft limit)
• Subnets per VPC: 200
• VPC CIDR block: /16 to /28
• AWS reserved IPs per subnet: 5 (first 4 + last 1)
• Internet Gateways per VPC: 1
• NAT Gateway bandwidth: 5 Gbps - 45 Gbps
• VPC Peering: Not transitive
• Route 53 health check interval: 30 sec (standard), 10 sec (fast)
• CloudFront cache TTL: Default 24 hours
```

### SQS & Messaging
```
• SQS message size: Max 256 KB
• SQS retention: 1 minute - 14 days (default 4 days)
• SQS visibility timeout: 0 - 12 hours (default 30 seconds)
• SQS long polling: 1-20 seconds
• SQS delay queue: 0-15 minutes
• SQS FIFO throughput: 300 msg/sec (3,000 with batching)
• SNS message size: Max 256 KB
```

### CloudWatch & Monitoring
```
• Default EC2 monitoring: 5 minutes
• Detailed EC2 monitoring: 1 minute
• Custom metrics standard resolution: 1 minute
• Custom metrics high resolution: 1 second
• CloudWatch Logs retention: Never expire - 10 years
• CloudTrail trail: 90 days in event history (free)
```

### KMS & Security
```
• KMS API requests: 5,500/sec (shared, can increase to 10K-30K)
• KMS encrypt/decrypt: Max 4 KB per call
• Customer managed keys: $1/month
• Secrets Manager: $0.40/secret/month
• WAF web ACL: Max 1,500 rules
```

### Kinesis
```
• Kinesis Data Streams shard: 1 MB/sec write, 2 MB/sec read
• Kinesis Data Streams retention: 1-365 days (default 24 hours)
• Kinesis Data Firehose buffer: 1-128 MB or 60-900 seconds
• Kinesis max record size: 1 MB
```

### Storage Transfer
```
• Data transfer > 1 week over network → Use Snow Family
• Snowcone: 8-14 TB
• Snowball Edge: 80-210 TB
• Snowmobile: Up to 100 PB
```

### Important Ports
```
• SSH: 22
• HTTP: 80
• HTTPS: 443
• RDP: 3389
• PostgreSQL: 5432
• MySQL/Aurora: 3306
• MSSQL: 1433
• Oracle: 1521
• Redis: 6379
• Memcached: 11211
```

### Percentages to Remember
```
• Reserved Instance discount: Up to 72% (3-year)
• Spot Instance discount: Up to 90%
• Savings Plans discount: Up to 66%
• S3 durability: 99.999999999% (11 nines)
• S3 Standard availability: 99.99%
• DynamoDB availability: 99.99%
```

### Time Periods
```
• Lambda max execution: 15 minutes
• Step Functions Standard: Up to 1 year
• Step Functions Express: Up to 5 minutes
• API Gateway timeout: 29 seconds
• CloudFront max timeout: 60 seconds
• ELB connection idle timeout: 60 seconds (default)
• Auto Scaling cooldown: 300 seconds (default)
```

---

## 🔄 Service Comparisons (Know the Difference!)

### Compute
- **EC2**: Virtual servers you manage
- **Lambda**: Code that runs on events (max 15 min)
- **Fargate**: Containers without servers

### Storage
- **S3**: Infinite object storage, globally unique bucket names
- **EBS**: Hard drive for EC2 instances
- **EFS**: Network file system for multiple EC2s
- **Glacier**: Cheap archival (hours to retrieve)

### Database
- **RDS**: Managed MySQL/PostgreSQL/SQL Server/Oracle/MariaDB
- **Aurora**: AWS's fast RDS (5x MySQL, 3x PostgreSQL)
- **DynamoDB**: NoSQL for web apps (single-digit ms)
- **Redshift**: Analyze petabytes of data (data warehouse)

### Networking
- **VPC**: Your own network in AWS
- **Internet Gateway**: Connect VPC to internet
- **NAT Gateway**: Private subnet → internet (outbound only)
- **Route 53**: DNS + health checks + routing

### Security
- **IAM**: Users, groups, roles, policies
- **KMS**: Encryption key management
- **CloudTrail**: Log all API calls (audit trail)
- **GuardDuty**: Detect threats using ML

### Monitoring
- **CloudWatch**: Metrics and logs
- **CloudTrail**: API call history (who did what)
- **Config**: Track resource configuration changes

### Integration
- **SQS**: Message queue
- **SNS**: Notifications (email, SMS, push)
- **Step Functions**: Orchestrate workflows

### Analytics
- **Athena**: SQL queries on S3 (serverless)
- **Kinesis**: Real-time data streaming
- **EMR**: Hadoop/Spark clusters
- **Glue**: ETL jobs and data catalog
- **QuickSight**: BI dashboards

### Migration
- **DMS**: Migrate databases
- **DataSync**: Sync on-prem files to AWS
- **Snow**: Physical devices for massive data transfer

---

## 🧩 Pattern Recognition

### Pattern 1: "Serverless Architecture"
```
User → API Gateway → Lambda → DynamoDB
                        ↓
                       S3 (for files)
```
**Keywords**: Scalable, no servers, pay per use

### Pattern 2: "High Availability Web App"
```
Route 53 (DNS)
    ↓
CloudFront (CDN)
    ↓
ALB (Multi-AZ)
    ↓
EC2 Auto Scaling (Multi-AZ)
    ↓
RDS Multi-AZ
    ↓
S3 (static content)
```
**Keywords**: Fault-tolerant, Multi-AZ, auto-scaling

### Pattern 3: "Hybrid Cloud"
```
On-Premises ←→ Direct Connect/VPN ←→ AWS VPC
                                        ↓
                                  Storage Gateway
                                        ↓
                                       S3
```
**Keywords**: Hybrid, on-premises integration

### Pattern 4: "Data Analytics Pipeline"
```
Data Sources → Kinesis → Lambda/Analytics → S3
                                              ↓
                                           Athena
                                              ↓
                                         QuickSight
```
**Keywords**: Real-time, streaming, analytics

### Pattern 5: "Disaster Recovery"
```
Production (Region A)     Backup (Region B)
      ↓                          ↓
  RDS Multi-AZ    →→→   Read Replica (Cross-Region)
      ↓                          ↓
   S3 Bucket     →→→   S3 Cross-Region Replication
```
**Keywords**: DR, failover, cross-region

---

## 📊 Decision Trees

### Storage Decision Tree
```
Need storage?
    ├─ Object storage? → S3
    ├─ Block storage for EC2? → EBS
    ├─ Shared file system?
    │   ├─ Linux? → EFS
    │   └─ Windows? → FSx for Windows
    ├─ Archive? → Glacier
    └─ Hybrid? → Storage Gateway
```

### Database Decision Tree
```
Need database?
    ├─ Relational (SQL)?
    │   ├─ Managed? → RDS or Aurora
    │   └─ Self-managed? → EC2 + database
    ├─ NoSQL?
    │   ├─ Key-value? → DynamoDB
    │   ├─ Document? → DocumentDB
    │   └─ Graph? → Neptune
    ├─ Analytics/Warehouse? → Redshift
    └─ Cache? → ElastiCache
```

### Compute Decision Tree
```
Need compute?
    ├─ Full control? → EC2
    ├─ Event-driven? → Lambda
    ├─ Containers?
    │   ├─ Managed cluster? → ECS/EKS
    │   └─ Serverless? → Fargate
    └─ Just deploy code? → Elastic Beanstalk
```

### 📚 Learn More
- [Architecture Patterns - Chapter Guide](./12-Architecture-Patterns/README.md)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS Reference Architectures](https://aws.amazon.com/architecture/reference-architecture-diagrams/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)

---

## 🔢 Numbers to Remember

### S3
- **Bucket names**: 3-63 characters, globally unique
- **Object size**: 0 bytes to 5 TB
- **Single PUT**: Max 5 GB (use multi-part for larger)
- **Durability**: 99.999999999% (11 nines)
- **Availability**: 99.99% (Standard)

### EC2 & EBS
- **Instance store**: Ephemeral (lost on stop/terminate)
- **EBS volume**: Max 64 TB
- **Placement groups**: 
  - Cluster = low latency
  - Spread = high availability (max 7 instances per AZ)
  - Partition = distributed apps

### Lambda
- **Max execution**: 15 minutes
- **Memory**: 128 MB to 10 GB
- **Concurrent executions**: 1,000 (default, can increase)
- **Deployment package**: 50 MB (zipped), 250 MB (unzipped)

### RDS & Aurora
- **Automated backups**: 1-35 days retention
- **Max storage**: 64 TB (most engines)
- **Read replicas**: Up to 15 (Aurora), 5 (others)
- **Multi-AZ**: Automatic failover (1-2 minutes)

### DynamoDB
- **Item size**: Max 400 KB
- **Partition key**: Required (hash)
- **Sort key**: Optional (range)
- **GSI**: Max 20 per table
- **LSI**: Max 5 per table (must create with table)

### VPC & Networking
- **CIDR block**: /16 to /28
- **Subnets**: Max 200 per VPC
- **Security groups**: Max 5 per instance (default)
- **Rules per SG**: 60 inbound, 60 outbound

### CloudFront
- **Edge locations**: 400+ globally
- **TTL**: Default 24 hours (customizable)
- **Max file size**: 20 GB

---

## 🎨 Color-Coded Priority

### 🔴 MUST KNOW (High Priority)
- S3 storage classes
- EC2 instance types and purchasing options
- Security Groups vs NACLs
- IAM (users, groups, roles, policies)
- VPC basics (subnets, IGW, NAT, route tables)
- RDS Multi-AZ vs Read Replicas
- Load balancer types (ALB, NLB)
- Well-Architected Framework pillars

### 🟡 SHOULD KNOW (Medium Priority)
- Lambda limitations
- DynamoDB (tables, indexes, streams)
- Route 53 routing policies
- CloudWatch, CloudTrail, Config differences
- Auto Scaling policies
- Kinesis (Streams, Firehose, Analytics)
- EBS volume types
- S3 encryption methods

### 🟢 GOOD TO KNOW (Lower Priority)
- AWS Batch
- Step Functions
- AppSync
- Cognito
- X-Ray
- Systems Manager
- Secrets Manager
- Parameter Store

---

## 💰 Cost Optimization (Module 13)

### AWS Pricing Models

```
┌────────────────────┬──────────┬────────────────────────┐
│   Pricing Model    │ Discount │      When to Use       │
├────────────────────┼──────────┼────────────────────────┤
│ On-Demand          │   0%     │ Unpredictable workload │
│ Reserved (1 year)  │  Up to   │ Steady-state usage     │
│                    │  40%     │ Known requirements     │
│ Reserved (3 year)  │  Up to   │ Long-term commitment   │
│                    │  72%     │ Predictable workloads  │
│ Savings Plans      │  Up to   │ Flexible instance types│
│                    │  72%     │ Compute commitment     │
│ Spot Instances     │  Up to   │ Fault-tolerant apps    │
│                    │  90%     │ Batch processing       │
│ Dedicated Hosts    │  Varies  │ Licensing requirements │
└────────────────────┴──────────┴────────────────────────┘

REMEMBER: "On-Demand = No commitment, Reserved = Long commitment"
```

### Cost Optimization Strategies

```
✅ Right-Sizing
   → Use the smallest instance type that meets requirements
   → Use Compute Optimizer for recommendations

✅ Increase Elasticity
   → Auto Scaling to match demand
   → Turn off non-production environments

✅ Choose Right Pricing Model
   → Reserved for baseline, On-Demand for peaks
   → Spot for fault-tolerant workloads

✅ Optimize Storage
   → S3 Lifecycle policies (move to cheaper classes)
   → Delete unused EBS volumes and snapshots
   → Use S3 Intelligent-Tiering

✅ Monitor and Analyze
   → AWS Cost Explorer for trends
   → AWS Budgets for alerts
   → Cost Allocation Tags

✅ Use Managed Services
   → Reduce operational overhead
   → Lambda instead of EC2 for sporadic tasks
```

### AWS Free Tier

```
Always Free:
  • Lambda: 1M requests/month
  • DynamoDB: 25 GB storage, 25 WCU, 25 RCU
  • SNS: 1M publishes
  • CloudWatch: 10 custom metrics

12 Months Free:
  • EC2: 750 hours/month t2.micro/t3.micro
  • S3: 5 GB standard storage
  • RDS: 750 hours/month db.t2.micro
  • CloudFront: 50 GB data transfer out
```

### Data Transfer Cost Rules

```
✅ FREE: Data IN to AWS (ingress)
✅ FREE: Data between services in same region
✅ FREE: Data to CloudFront

💰 PAID: Data OUT from AWS (egress)
💰 PAID: Data between regions
💰 PAID: Data to internet

Cost Reduction Tips:
  → Use CloudFront CDN
  → Use VPC Endpoints
  → Keep data in same region
```

### AWS Cost Management Tools

```
• Cost Explorer     → Visualize and forecast costs
• AWS Budgets       → Set alerts for spending thresholds
• Cost & Usage Report → Detailed cost data to S3
• Compute Optimizer → ML-based rightsizing recommendations
• Trusted Advisor   → Cost optimization best practices
• Cost Allocation Tags → Track costs by project/team
```

### 📚 Learn More
- [Cost Optimization - Chapter Guide](./13-Cost-Optimization/README.md)
- [AWS Pricing](https://aws.amazon.com/pricing/)
- [AWS Cost Management](https://aws.amazon.com/aws-cost-management/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
- [AWS Pricing Calculator](https://calculator.aws/)

---

## 💭 Think Like AWS

### When AWS Says... They Mean...
- **"Highly available"** → Multi-AZ
- **"Fault-tolerant"** → Continue working even with failures
- **"Scalable"** → Can grow/shrink automatically
- **"Durable"** → Data won't be lost
- **"Cost-effective"** → Cheapest option that works
- **"Secure"** → Encryption, IAM, VPC
- **"Managed"** → AWS handles maintenance
- **"Serverless"** → No server management, pay per use

### AWS Prefers...
- ✅ Managed services over self-managed
- ✅ Serverless over EC2 (when possible)
- ✅ Multi-AZ over single AZ
- ✅ IAM roles over access keys
- ✅ Encryption enabled
- ✅ Least privilege access
- ✅ Auto Scaling over fixed capacity
- ✅ CloudFormation for infrastructure as code

---

## 🎬 Scenario-Based Quick Answers

### "I need to..."

**...store millions of images uploaded by users**
→ **S3** (unlimited storage, HTTP access)

**...run a MySQL database with automatic backups**
→ **RDS MySQL** with Multi-AZ

**...process data in real-time from IoT sensors**
→ **Kinesis Data Streams** → Lambda

**...send email notifications to users**
→ **SNS** (or SES for email specifically)

**...ensure my app survives AZ failure**
→ **Multi-AZ** deployment + **ALB** + **Auto Scaling**

**...analyze logs with SQL**
→ **Athena** (query S3 logs directly)

**...migrate on-prem Oracle DB to AWS**
→ **DMS** + **SCT** (Schema Conversion Tool)

**...cache database queries**
→ **ElastiCache** (Redis or Memcached)

**...store session state for web app**
→ **DynamoDB** or **ElastiCache**

**...host a static website**
→ **S3** + **CloudFront**

**...run code when file uploaded to S3**
→ **S3 Event** → **Lambda**

**...connect on-prem network to AWS securely**
→ **VPN** (quick) or **Direct Connect** (dedicated)

**...ensure compliance with data residency**
→ Choose specific **AWS Region**

**...reduce data transfer costs**
→ **CloudFront** CDN

**...implement disaster recovery**
→ **Automated backups** + **Cross-region replication**

---

## 🧪 Quick Self-Test

### Question Format: "What service should you use when..."

1. **Q**: You need to run code in response to HTTP requests without managing servers?
   **A**: API Gateway + Lambda

2. **Q**: You need a managed NoSQL database with single-digit millisecond latency?
   **A**: DynamoDB

3. **Q**: You need to distribute traffic across EC2 instances based on URL path?
   **A**: Application Load Balancer (ALB)

4. **Q**: You need to store objects up to 5 TB in size?
   **A**: S3 (use multi-part upload)

5. **Q**: You need to encrypt data at rest in S3 with your own keys?
   **A**: SSE-C (Server-Side Encryption with Customer-Provided Keys) or SSE-KMS

6. **Q**: You need to automatically scale EC2 instances based on CPU usage?
   **A**: Auto Scaling Group with target tracking policy

7. **Q**: You need to query S3 data with SQL without loading it into a database?
   **A**: Athena

8. **Q**: You need to monitor API calls made in your AWS account?
   **A**: CloudTrail

9. **Q**: You need to create a private network in AWS?
   **A**: VPC

10. **Q**: You need to transfer 100 TB of data to AWS with limited bandwidth?
    **A**: AWS Snowball

---

## 🏆 Exam Day Shortcuts

### Time-Saving Elimination Techniques

**Eliminate if the answer suggests:**
- ❌ Storing credentials in code
- ❌ Single point of failure (no redundancy)
- ❌ Opening port 22 (SSH) to 0.0.0.0/0
- ❌ Using root user for applications
- ❌ Not using encryption when security is mentioned
- ❌ Complex custom solution when AWS service exists

**Choose the answer that:**
- ✅ Uses managed AWS services
- ✅ Implements least privilege
- ✅ Has Multi-AZ/redundancy
- ✅ Uses encryption
- ✅ Is cost-effective (serverless, right-sized)
- ✅ Scales automatically

### Keywords = Services Mapping

| Keyword | Think This Service |
|---------|-------------------|
| "Real-time" | Kinesis, DynamoDB Streams |
| "Archive" | S3 Glacier |
| "Serverless" | Lambda, DynamoDB, Aurora Serverless |
| "Cache" | ElastiCache, CloudFront, DAX |
| "Queue" | SQS |
| "Notification" | SNS |
| "Workflow" | Step Functions |
| "Big Data" | EMR, Athena, Redshift |
| "Migration" | DMS, DataSync, Snow |
| "Container" | ECS, EKS, Fargate |
| "CDN" | CloudFront |
| "DNS" | Route 53 |
| "DDoS protection" | Shield, WAF |

### 📚 Learn More - Additional Study Resources
- [Practice Questions](./14-Practice/COMPREHENSIVE-PRACTICE-QUESTIONS.md)
- [AWS Certified Solutions Architect Official Study Guide](https://aws.amazon.com/certification/certified-solutions-architect-associate/)
- [AWS Whitepapers](https://aws.amazon.com/whitepapers/)
- [AWS FAQs](https://aws.amazon.com/faqs/)
- [AWS Training and Certification](https://aws.amazon.com/training/)
- [AWS Skill Builder](https://skillbuilder.aws/)

---

## 📚 Final Memorization Tips

### The 3 P's of AWS Exam Success

1. **Patterns**: Recognize common architecture patterns
2. **Principles**: Apply Well-Architected Framework
3. **Practice**: Do practice exams

### Study Schedule Recommendation

**Week 1-2**: Core Services (EC2, S3, VPC, IAM)
**Week 3-4**: Databases & Storage (RDS, DynamoDB, EBS, EFS)
**Week 5**: Networking & Content Delivery
**Week 6**: Security & Monitoring
**Week 7**: Serverless & Application Integration
**Week 8**: Analytics, Migration, Cost Optimization
**Week 9-10**: Practice exams & review weak areas

### Memory Retention Techniques

1. **Spaced Repetition**: Review flashcards daily
2. **Active Recall**: Test yourself without looking
3. **Teach Others**: Explain concepts to someone
4. **Visual Aids**: Draw architecture diagrams
5. **Acronyms**: Use mnemonics (CROPS, SIGGIZ, etc.)
6. **Real Practice**: Use AWS Free Tier

---

**Remember**: The exam tests your ability to choose the **right** service for the **right** scenario. Focus on understanding **when** and **why** to use each service, not just **what** they do.

**You've got this! 🚀**

