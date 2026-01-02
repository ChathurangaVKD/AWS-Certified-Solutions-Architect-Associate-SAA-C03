# AWS Solutions Architect - Quick Reference Guide

## 🚀 Service Quick Reference

### Compute

| Service | Type | Use Case | Key Features |
|---------|------|----------|--------------|
| **EC2** | Virtual Servers | General compute | Instance types, purchasing options |
| **Lambda** | Serverless | Event-driven, short tasks | 15 min max, pay per invocation |
| **ECS** | Containers | Docker orchestration | EC2 or Fargate launch types |
| **EKS** | Kubernetes | K8s workloads | Managed control plane |
| **Fargate** | Serverless Containers | No server management | Pay per use |
| **Elastic Beanstalk** | PaaS | Web apps | Handles infrastructure |
| **Batch** | Batch Processing | Large-scale jobs | Managed scheduling |

### Storage

| Service | Type | Use Case | Key Specs |
|---------|------|----------|-----------|
| **S3** | Object | Files, backups | 11 9's durability, unlimited |
| **EBS** | Block | EC2 boot/data volumes | AZ-specific, up to 64,000 IOPS |
| **EFS** | File (NFS) | Shared Linux storage | Multi-AZ, petabyte-scale |
| **FSx Windows** | File (SMB) | Windows workloads | Active Directory integration |
| **FSx Lustre** | File | HPC, ML | High throughput, S3 integration |
| **Storage Gateway** | Hybrid | On-prem to cloud | File, Volume, Tape gateways |
| **Snow Family** | Physical | Offline data transfer | TB to EB scale |

### Database

| Service | Type | Use Case | Key Features |
|---------|------|----------|--------------|
| **RDS** | Relational | OLTP | MySQL, PostgreSQL, SQL Server, Oracle |
| **Aurora** | Relational | Cloud-native SQL | 5x MySQL, 3x PostgreSQL performance |
| **DynamoDB** | NoSQL (Key-Value) | High-scale apps | Serverless, millisecond latency |
| **ElastiCache** | In-Memory | Caching | Redis or Memcached |
| **Redshift** | Data Warehouse | OLAP, analytics | Columnar, petabyte-scale |
| **DocumentDB** | NoSQL (Document) | MongoDB workloads | MongoDB-compatible |
| **Neptune** | Graph | Social networks | Billions of relationships |
| **QLDB** | Ledger | Immutable records | Cryptographically verifiable |

### Networking

| Service | Purpose | Key Features |
|---------|---------|--------------|
| **VPC** | Virtual Network | Isolated network, subnets, routing |
| **Route 53** | DNS | Domain registration, health checks, routing policies |
| **CloudFront** | CDN | 400+ edge locations, DDoS protection |
| **API Gateway** | API Management | REST/WebSocket APIs, throttling |
| **Direct Connect** | Dedicated Connection | 1-100 Gbps, private connectivity |
| **Transit Gateway** | Network Hub | Connect thousands of VPCs |
| **Global Accelerator** | Performance | Static IPs, AWS backbone network |
| **VPN** | Encrypted Connection | Site-to-Site, Client VPN |

### Security

| Service | Purpose | Key Features |
|---------|---------|--------------|
| **IAM** | Identity & Access | Users, groups, roles, policies |
| **KMS** | Key Management | Encryption keys, FIPS 140-2 Level 2 |
| **CloudHSM** | Hardware Security | FIPS 140-2 Level 3, single-tenant |
| **Secrets Manager** | Secret Rotation | Auto-rotate DB credentials |
| **WAF** | Web Firewall | SQL injection, XSS protection |
| **Shield** | DDoS Protection | Standard (free), Advanced ($3k/month) |
| **GuardDuty** | Threat Detection | ML-based anomaly detection |
| **Inspector** | Vulnerability Assessment | EC2, containers, Lambda |
| **Macie** | Data Discovery | PII detection in S3 |
| **Security Hub** | Security Center | Aggregates findings |

---

## 🎯 Common Exam Patterns

### High Availability
**Pattern**: Multi-AZ + Auto Scaling + Load Balancer
```
Route 53 → CloudFront → ALB (Multi-AZ) → Auto Scaling Group → RDS Multi-AZ
```

### Cost Optimization
- **Steady State**: Reserved Instances / Savings Plans
- **Variable**: On-Demand + Auto Scaling
- **Interruptible**: Spot Instances (up to 90% off)
- **Storage**: S3 Lifecycle → IA → Glacier

### Disaster Recovery (RPO/RTO)
1. **Backup & Restore**: Hours (cheapest)
2. **Pilot Light**: Hours to minutes
3. **Warm Standby**: Minutes
4. **Multi-Site**: Near zero (most expensive)

### Serverless Stack
```
CloudFront + S3 → API Gateway → Lambda → DynamoDB
+ Cognito (Auth) + SES (Email) + SNS (Notifications)
```

---

## 📊 Service Limits (Important)

| Service | Limit | Notes |
|---------|-------|-------|
| **S3 Object Size** | 5 TB max | Use multipart for >100 MB |
| **Lambda Timeout** | 15 min max | 900 seconds |
| **Lambda Package** | 50 MB zipped, 250 MB unzipped | Use layers |
| **VPC CIDR** | /16 to /28 | 5 VPCs per region (soft) |
| **Security Groups per Instance** | 5 | Can be increased |
| **Rules per Security Group** | 60 inbound, 60 outbound | Soft limit |
| **Read Replicas** | RDS: 5, Aurora: 15 | Per database |
| **EBS IOPS** | io2: 64,000, io2 BE: 256,000 | Per volume |
| **DynamoDB Item Size** | 400 KB | Max item size |
| **CloudFront** | 25 distributions | Soft limit |

---

## 🔄 Service Comparisons

### Storage

**S3 vs EBS vs EFS**
- **S3**: Object storage, HTTP access, unlimited
- **EBS**: Block storage, single EC2 (except Multi-Attach io2), AZ-specific
- **EFS**: File storage (NFS), multiple EC2s, multi-AZ

### Database

**RDS vs DynamoDB**
- **RDS**: Relational (SQL), ACID, complex queries
- **DynamoDB**: NoSQL (Key-Value), millisecond latency, serverless

**Aurora vs RDS**
- **Aurora**: 5x faster, auto-scaling storage, 15 Read Replicas
- **RDS**: Standard MySQL/PostgreSQL, 5 Read Replicas

### Load Balancers

**ALB vs NLB vs GWLB**
- **ALB**: Layer 7 (HTTP/HTTPS), path/host routing, Lambda targets
- **NLB**: Layer 4 (TCP/UDP), ultra-low latency, static IPs
- **GWLB**: Layer 3, third-party appliances (firewalls, IDS/IPS)

### Caching

**CloudFront vs ElastiCache vs DAX**
- **CloudFront**: Edge caching for static/dynamic content
- **ElastiCache**: Database caching (Redis/Memcached)
- **DAX**: DynamoDB caching only, microsecond latency

---

## 🛡️ Security Best Practices

### Data Protection
✅ **At Rest**: KMS encryption for S3, EBS, RDS  
✅ **In Transit**: HTTPS/TLS, VPN, Direct Connect  
✅ **Backup**: Automated backups, Cross-Region Replication  

### Access Control
✅ **IAM**: Least privilege, roles over users  
✅ **MFA**: Root and privileged users  
✅ **Network**: Private subnets, Security Groups, NACLs  

### Monitoring
✅ **CloudTrail**: All API calls, all regions  
✅ **Config**: Resource configuration tracking  
✅ **GuardDuty**: Threat detection  
✅ **CloudWatch**: Metrics, logs, alarms  

---

## 💰 Cost Optimization Strategies

### Compute
- **Reserved** for steady workloads (up to 72% off)
- **Spot** for fault-tolerant (up to 90% off)
- **Auto Scaling** to match demand
- **Lambda** for intermittent workloads

### Storage
- **S3 Lifecycle**: Standard → IA → Glacier
- **S3 Intelligent-Tiering**: Automatic transitions
- **Delete** unused snapshots and volumes
- **Right-size** EBS volumes

### Database
- **Reserved Instances** for RDS
- **Aurora Serverless** for variable workloads
- **DynamoDB On-Demand** for unpredictable
- **Read Replicas** instead of larger instance

### Networking
- **VPC Endpoints**: Avoid data transfer charges
- **CloudFront**: Reduce origin requests
- **Direct Connect**: For high-volume transfers

---

## 🎓 Exam Day Checklist

### Before the Exam
- [ ] Schedule exam at optimal time (morning, alert)
- [ ] Test equipment (for online proctored)
- [ ] Quiet room with good internet (online)
- [ ] Government-issued ID ready
- [ ] Arrive 15-30 minutes early (in-person)

### During the Exam
- [ ] Read questions carefully (keywords: MOST, LEAST, BEST)
- [ ] Eliminate obviously wrong answers
- [ ] Flag difficult questions, return later
- [ ] Answer ALL questions (no penalty)
- [ ] Manage time: ~2 minutes per question
- [ ] Review flagged questions if time permits

### Common Traps
- ❌ Don't overthink - choose simplest solution
- ❌ Watch for "MOST cost-effective" vs "BEST performance"
- ❌ "Least operational overhead" = managed services
- ❌ Read all options before selecting

---

## 📝 Mental Cheat Sheet

### When You See...

**"High Availability"**
→ Multi-AZ, Auto Scaling, Load Balancer

**"Cost-Effective"**
→ Spot, Reserved, Serverless, Lifecycle policies

**"Low Latency"**
→ CloudFront, ElastiCache, DAX, Local/Regional services

**"Secure"**
→ IAM roles, KMS encryption, private subnets, least privilege

**"Disaster Recovery"**
→ Cross-region replication, backups, Multi-AZ, failover

**"Decouple"**
→ SQS, SNS, EventBridge, Step Functions

**"Serverless"**
→ Lambda, API Gateway, DynamoDB, S3, Fargate

**"Real-time"**
→ Kinesis, Lambda, DynamoDB Streams, EventBridge

**"Analytics"**
→ Redshift (warehouse), Athena (S3 queries), EMR (big data)

**"Migration"**
→ DMS (databases), DataSync (files), Snow Family (offline)

---

## 🔑 Key Acronyms

- **AZ**: Availability Zone
- **ALB**: Application Load Balancer
- **NLB**: Network Load Balancer
- **ASG**: Auto Scaling Group
- **EBS**: Elastic Block Store
- **EFS**: Elastic File System
- **RDS**: Relational Database Service
- **S3**: Simple Storage Service
- **VPC**: Virtual Private Cloud
- **IAM**: Identity and Access Management
- **KMS**: Key Management Service
- **NACL**: Network Access Control List
- **SG**: Security Group
- **IGW**: Internet Gateway
- **NAT**: Network Address Translation
- **CDN**: Content Delivery Network
- **TTL**: Time To Live
- **IOPS**: Input/Output Operations Per Second
- **RPO**: Recovery Point Objective
- **RTO**: Recovery Time Objective
- **HA**: High Availability
- **DR**: Disaster Recovery

---

## 🎯 Final Tips

1. **Trust your preparation** - you've studied hard!
2. **Stay calm** - take deep breaths if stressed
3. **Read carefully** - don't rush
4. **Eliminate wrong answers** - narrows choices
5. **Use process of elimination** - often 2 answers are clearly wrong
6. **Answer everything** - no penalty for guessing
7. **Flag and return** - don't get stuck on one question
8. **Think AWS-native** - prefer AWS managed services
9. **Well-Architected** - think of the 6 pillars
10. **You got this!** 💪

---

**Good luck with your AWS Solutions Architect Associate certification!** 🚀

---

[Back to Main README](../README.md)

