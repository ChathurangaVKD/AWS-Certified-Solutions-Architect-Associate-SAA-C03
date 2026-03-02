# AWS SAA-C03 - Ultra Quick Reference Card

**Print this for last-minute review or save on your phone**

---

## MUST MEMORIZE (10 Critical Rules)

1. **CloudFront + ACM cert** = us-east-1 ONLY ⚠️
2. **Memory metric** = Need CloudWatch agent (not default)
3. **S3 IA/Glacier** = 30-day minimum charge
4. **Multi-AZ** = HA (sync) | **Read Replica** = Scale (async)
5. **IAM evaluation** = DENY always wins
6. **ECS dynamic ports** = Requires ALB + awsvpc/bridge
7. **Instance store** = Lost on stop/terminate
8. **VPC peering DNS** = Enable in BOTH VPCs
9. **Glacier transitions** = Cannot go OUT without restore
10. **Bucket default class** = Only NEW objects (not existing)

---

## SERVICE SELECTION (Quick Decision)

### Caching
- **Redis**: Persistence, HA, Multi-AZ, complex data
- **Memcached**: Simple, multi-threaded, no persistence
- **DAX**: DynamoDB only, microsecond latency

### Storage
- **FSx Lustre**: HPC, ML (100s GB/s)
- **FSx Windows**: SMB, Active Directory
- **EFS**: Linux shared filesystem
- **S3**: Object storage

### Global Services
- **CloudFront**: HTTP/HTTPS, caching, CDN
- **Global Accelerator**: Static IP, TCP/UDP, non-HTTP

### Database HA
- **RDS Multi-AZ**: Same region, auto-failover (1-2 min)
- **Aurora Global**: Cross-region, <1s lag, <1 min failover
- **DynamoDB Global**: Multi-region, multi-write

### VPC Connectivity
- **VPC Endpoint Gateway**: S3/DynamoDB (FREE)
- **VPC Endpoint Interface**: Other services ($0.01/hr)
- **Transit Gateway**: >10 VPCs, hub-spoke
- **VPC Peering**: Simple 1-to-1

### Analytics
- **Athena**: Query S3 with SQL
- **Glue Crawler**: Discover schemas
- **QuickSight**: BI dashboards

### Secrets
- **Secrets Manager**: Auto-rotation, RDS integration
- **Parameter Store**: Simple, free, no auto-rotation

---

## KEY NUMBERS

| What | Value |
|------|-------|
| S3 IA minimum | 30 days |
| Auto Scaling cooldown | 5 min (300s) |
| Glacier Expedited | 1-5 min |
| Glacier Standard | 3-5 hours |
| Glacier Bulk | 5-12 hours |
| Deep Archive Standard | 12 hours |
| Deep Archive Bulk | 48 hours |
| Aurora Global lag | <1 second |
| RDS Multi-AZ failover | 1-2 minutes |
| IAM token validity | 15 minutes |
| Lambda@Edge timeout | 30 seconds |
| CloudFront Functions | <1 millisecond |
| Kinesis retention default | 1 day (max 365) |
| API Gateway RPS | 10,000 steady, 5,000 burst |
| VPC Peering limit | 125 per VPC |
| Spread placement | 7 instances per AZ |
| S3 multipart max parts | 10,000 |
| EBS io2 max IOPS | 64,000 |
| gp3 base IOPS | 3,000 |
| gp3 base throughput | 125 MB/s |

---

## STORAGE CLASSES (Cheapest → Most Expensive)

1. S3 Glacier Deep Archive ($0.00099/GB) ⭐ CHEAPEST
2. S3 Glacier Flexible ($0.004/GB)
3. S3 Intelligent-Tiering ($0.0025-0.023/GB)
4. S3 One Zone-IA ($0.01/GB)
5. S3 Standard-IA ($0.0125/GB)
6. S3 Standard ($0.023/GB)

---

## EC2 INSTANCE TYPES (Quick Guide)

- **C5/C6** = Compute-optimized (CPU heavy)
- **M5/M6** = General purpose (balanced)
- **R5/R6** = Memory-optimized (RAM heavy)
- **T3/T4** = Burstable (variable, cheap)
- **I3/I4** = Storage-optimized (IOPS)
- **G4/P3** = GPU (ML, graphics)

---

## EC2 PRICING MODELS

| Model | Discount | Flexibility | Use Case |
|-------|----------|-------------|----------|
| On-Demand | 0% | Full | Variable workloads |
| Standard RI | 72% | None | Steady state |
| Convertible RI | 54% | Change type | Some flexibility |
| Savings Plans | 66-72% | High | Flexible commitment |
| Spot | 90% | Can interrupt | Fault-tolerant |

---

## ROUTING POLICIES (Route 53)

- **Simple**: One resource
- **Weighted**: % traffic split (A/B testing)
- **Latency**: Lowest latency region
- **Failover**: Primary/secondary + health checks
- **Geolocation**: User's country/continent
- **Geoproximity**: Distance + bias (-99 to +99)
- **Multi-value**: Multiple IPs + health checks

---

## LOAD BALANCERS

| Feature | ALB | NLB | CLB |
|---------|-----|-----|-----|
| Layer | 7 (HTTP) | 4 (TCP) | 4 & 7 |
| Static IP | No | Yes | No |
| Path routing | Yes | No | No |
| ECS dynamic ports | Yes | No | No |
| WebSockets | Yes | Yes | No |
| Performance | Good | Extreme | Legacy |

---

## EBS VOLUME TYPES

| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| gp3 | 3K-16K | 125-1000 MB/s | General |
| gp2 | 3 IOPS/GB | Up to 250 MB/s | Legacy |
| io2 | Up to 64K | Up to 1000 MB/s | High perf |
| io1 | Up to 64K | Up to 1000 MB/s | Older |
| st1 | 500 | 500 MB/s | Throughput |
| sc1 | 250 | 250 MB/s | Cold data |

---

## PLACEMENT GROUPS

- **Cluster**: Single AZ, low latency (10 Gbps), HPC
- **Spread**: Max 7/AZ, isolated, critical apps
- **Partition**: 7 partitions/AZ, Hadoop/Kafka

---

## SECURITY COMPARISON

### Security Group vs NACL

| Feature | Security Group | NACL |
|---------|---------------|------|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Evaluation | All rules | Numbered order |

### Encryption Options

| Type | Who Manages | Key Location |
|------|-------------|--------------|
| SSE-S3 | AWS | AWS |
| SSE-KMS | AWS KMS | KMS |
| SSE-C | You | Your systems |
| Client-side | You | You encrypt |

---

## LAMBDA DEPLOYMENT

- **Version**: Immutable snapshot
- **$LATEST**: Mutable, current code
- **Alias**: Pointer to version(s)
- **Weighted alias**: Split traffic (10% v2, 90% v1)

---

## ELASTIC BEANSTALK DEPLOYMENT

| Strategy | Downtime | Cost | Risk | Rollback |
|----------|----------|------|------|----------|
| All at once | Yes | Low | High | Manual |
| Rolling | No | Low | Medium | Manual |
| Rolling + batch | No | Medium | Medium | Manual |
| Immutable | No | High | Low | Quick |
| Blue/Green | No | High | Lowest | Instant |

---

## COMMON TRAPS TO AVOID

❌ **Memory is default metric** → Need CloudWatch agent  
❌ **CloudFront cert in any region** → Must be us-east-1  
❌ **Bucket default affects existing** → Only new objects  
❌ **Can transition from Glacier** → Must restore first  
❌ **VPC peering auto DNS** → Must enable both sides  
❌ **Read replica for HA** → Multi-AZ for HA  
❌ **Instance store persists** → Lost on stop  
❌ **SSE-C = AWS manages** → You manage keys  
❌ **IAM allow > deny** → Deny ALWAYS wins  
❌ **CloudWatch logs auto-expire** → Indefinite default  

---

## EXAM KEYWORDS (What They Mean)

- **"Lowest cost"** → Cheapest storage class, Spot, RIs
- **"Highest performance"** → Provisioned IOPS, cluster placement, caching
- **"Most secure"** → Encryption, private subnets, least privilege
- **"Minimum operational overhead"** → Managed services, serverless
- **"Highly available"** → Multi-AZ, multiple regions
- **"Scalable"** → Auto Scaling, serverless, elastic
- **"Real-time"** → Kinesis, DynamoDB Streams, Lambda
- **"Near real-time"** → Firehose, CloudWatch

---

## TIME MANAGEMENT (Exam)

- **130 minutes** / 65 questions = **2 min/question**
- Spend <1 min on easy questions (bank extra time)
- Flag and skip if >2 minutes
- Reserve 30 minutes for review at end
- Review flagged questions with fresh eyes

---

## FINAL CHECKLIST (Before Exam)

- [ ] CloudFront certs = us-east-1
- [ ] Memory = CloudWatch agent
- [ ] Multi-AZ = HA, Read Replica = scale
- [ ] IAM deny wins always
- [ ] S3 IA = 30-day minimum
- [ ] Glacier retrieval times memorized
- [ ] Instance types (C/M/R/T) purposes
- [ ] VPC Endpoint: Gateway (S3/DDB), Interface (others)
- [ ] Caching: Redis vs Memcached vs DAX
- [ ] FSx: Lustre (HPC), Windows (SMB)

---

## STAY CALM & CONFIDENT

✅ You've studied hard  
✅ You know the material  
✅ Read questions carefully  
✅ Eliminate wrong answers first  
✅ Trust your preparation  

**You've got this! 🚀**

---

*Ultra Quick Reference Card v1.0*  
*AWS Certified Solutions Architect Associate (SAA-C03)*  
*Print or save for last-minute review*

