# AWS SAA-C03 - Ultra Quick Reference Card

**Print this for last-minute review or save on your phone**

---

## MUST MEMORIZE (15 Critical Rules)

1. **CloudFront + ACM cert** = us-east-1 ONLY ⚠️
2. **Memory metric** = Need CloudWatch agent (not default)
3. **S3 IA/Glacier** = 30-day minimum charge
4. **Multi-AZ** = HA (sync) | **Read Replica** = Scale (async)
5. **IAM evaluation** = DENY always wins (SCP beats IAM)
6. **ECS dynamic ports** = Requires ALB + awsvpc/bridge
7. **Instance store** = Lost on stop/terminate
8. **VPC peering DNS** = Enable in BOTH VPCs
9. **Glacier transitions** = Cannot go OUT without restore
10. **Bucket default class** = Only NEW objects (not existing)
11. **SCPs** = DON'T affect management account ⚠️
12. **File Gateway** = S3 objects (admins can access), Volume = blocks only
13. **RDS IAM Auth** = Token 15 min, MySQL/PostgreSQL/Aurora only
14. **SQS FIFO** = 300 msg/s (3000 batched), ends in `.fifo`
15. **Aurora Global** = <1s lag, <1 min failover (cross-region HA)

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

### Messaging & Integration
- **Queue (1-to-1, pull)**: SQS
- **Pub/Sub (1-to-many, push)**: SNS
- **Ordered + Exactly-once**: SQS FIFO
- **Real-time streaming**: Kinesis Data Streams
- **Load to S3/Redshift**: Kinesis Firehose
- **Event routing**: EventBridge
- **Workflow orchestration**: Step Functions
- **JMS/AMQP migration**: Amazon MQ

### Hybrid & Migration
- **Hybrid file storage**: Storage Gateway
- **File migration**: DataSync (10x faster)
- **DB migration**: DMS + SCT (if different engine)
- **Physical transfer < 10TB**: Snowcone
- **Physical transfer 10-80TB**: Snowball Edge
- **Physical transfer > 10PB**: Snowmobile
- **SFTP to S3**: Transfer Family

### Multi-Account Management
- **Centralized billing**: AWS Organizations
- **Enforce policies**: Service Control Policies (SCPs)
- **Automated setup**: Control Tower
- **Share resources**: Resource Access Manager (RAM)

### VPC Connectivity
- **VPC Endpoint Gateway**: S3/DynamoDB (FREE)
- **VPC Endpoint Interface**: Other services ($0.01/hr)
- **Transit Gateway**: >10 VPCs, hub-spoke
- **VPC Peering**: Simple 1-to-1

### VPC Advanced Features
- **Flow Logs**: Capture all traffic (accepted + rejected), VPC/Subnet/ENI level
- **DNS Settings**: enableDnsHostnames + enableDnsSupport (both needed for peering)
- **Private Link**: Expose service privately via NLB + VPC endpoint
- **NAT Gateway**: Managed NAT, HA per AZ, 45 Gbps
- **NAT Instance**: EC2-based, self-managed, cheaper but not HA
- **Internet Gateway**: 1 per VPC, scales automatically
- **Egress-Only IGW**: IPv6 outbound only
- **Direct Connect**: Dedicated network (1-10 Gbps), consistent latency
- **DX + VPN**: DX primary, VPN backup/failover, BGP routing
- **VPN**: Site-to-Site VPN over internet (up to 1.25 Gbps)

---

## COST OPTIMIZATION

- **Cost Explorer**: Visualize costs, forecasting, RI recommendations
- **Cost Allocation Tags**: Track costs by project/team/environment
- **Budgets**: Set custom budgets, alerts
- **Compute Optimizer**: Right-sizing recommendations
- **Trusted Advisor**: Cost optimization checks (Business/Enterprise support)
- **S3 Intelligent-Tiering**: Auto-move between access tiers, no retrieval fees
- **S3 Lifecycle Policies**: Auto-transition to cheaper storage classes
- **Reserved Instances**: Up to 72% discount (1-3 year commitment)
- **Savings Plans**: Up to 72% discount, more flexible than RIs
- **Spot Instances**: Up to 90% discount, can be interrupted
- **RDS Reserved Instances**: Up to 69% discount

---
- **Athena**: Query S3 with SQL
- **Glue Crawler**: Discover schemas
- **QuickSight**: BI dashboards

### Secrets
- **Secrets Manager**: Auto-rotation, RDS integration
- **Parameter Store**: Simple, free, no auto-rotation

### AWS Organizations & SCPs
- **Management Account**: Cannot be restricted by SCPs, pays all bills
- **Member Accounts**: Subject to SCPs, inherit from OUs
- **SCPs**: Maximum permissions (don't grant), preventive control
- **SCP Formula**: Effective = IAM policy AND SCP
- **Common SCP Uses**: Region restrict, require encryption, prevent org exit

### Storage Gateway (Hybrid Storage)
- **File Gateway**: NFS/SMB → S3 objects (admins can access via console)
- **Volume Gateway Cached**: Primary in S3, cache local
- **Volume Gateway Stored**: Primary local, async backup to S3
- **Tape Gateway**: Virtual tapes → S3 Glacier (backup software)

### Migration & Transfer
- **DataSync**: Automated file transfer (NFS/SMB → S3/EFS/FSx), 10x faster
- **DMS**: Database migration, minimal downtime, CDC
- **SCT**: Schema Conversion Tool (different DB engines)
- **Snowcone**: 8 TB, edge computing, portable
- **Snowball Edge**: 80 TB, large migrations
- **Snowmobile**: 100 PB, exabyte-scale (literal truck!)
- **Transfer Family**: SFTP/FTPS → S3/EFS

### Application Integration
- **SQS Standard**: Unlimited throughput, at-least-once, best-effort order
- **SQS FIFO**: 300 msg/s, exactly-once, ordered, name ends `.fifo`
- **SNS**: Pub/Sub, push to multiple targets, fan-out
- **EventBridge**: Event-driven, 20+ targets, scheduled/AWS events
- **Step Functions**: Orchestrate workflows, visual, error handling
- **Kinesis Data Streams**: Real-time, custom processing, replay
- **Kinesis Firehose**: Load to S3/Redshift, near real-time, managed

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
| Partition placement | 7 partitions per AZ |
| S3 multipart max parts | 10,000 |
| EBS io2 max IOPS | 64,000 |
| EBS io2 Block Express | 256,000 IOPS |
| gp3 base IOPS | 3,000 |
| gp3 base throughput | 125 MB/s |
| SQS FIFO throughput | 300 msg/s (3,000 batched) |
| Snowcone capacity | 8 TB (HDD) / 14 TB (SSD) |
| Snowball Edge | 80 TB storage optimized |
| Snowmobile | 100 PB per truck |
| S3 Transfer Acceleration | 50-500% faster |
| S3 performance | 3,500 PUT/s, 5,500 GET/s per prefix |

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

## EC2 ADVANCED FEATURES

- **Instance Metadata**: http://169.254.169.254/latest/meta-data/
- **Public IP**: Changes on stop/start (use Elastic IP for static)
- **ENA**: Elastic Network Adapter (up to 100 Gbps)
- **EFA**: Elastic Fabric Adapter (HPC, MPI, inter-node)
- **Enhanced Networking**: SR-IOV for high bandwidth, low latency
- **Instance Store**: Ephemeral storage, lost on stop/terminate
- **EBS-Optimized**: Dedicated bandwidth for EBS
- **T3 Unlimited**: Burst above baseline (pay extra)

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

### Route 53 Health Checks

- **Endpoint**: HTTP/HTTPS/TCP health check
- **Calculated**: Combine multiple health checks (AND/OR/NOT)
- **CloudWatch Alarm**: Based on CloudWatch metrics

---

## CLOUDWATCH MONITORING

- **Default EC2 Metrics**: CPU, Network, Disk ops (NO memory/disk space)
- **CloudWatch Agent**: Required for memory, disk space, custom metrics
- **Agent aggregation_dimensions**: Define metric dimensions
- **Cross-Account**: Share metrics for central monitoring
- **Logs Retention**: Indefinite by default (not 7 days)
- **Alarms**: Metric-based, composite, anomaly detection
- **Dashboards**: Custom metric visualization
- **EventBridge (CloudWatch Events)**: Event-driven automation

---

## CLOUDFRONT ADVANCED

- **Origin Access Identity (OAI)**: Access private S3 without public bucket
- **Origin Failover**: Primary + secondary origin, automatic failover
- **Cache Behaviors**: Path-based routing (/api/*, /images/*), priority order
- **Signed URLs**: Single file access, include expiration/IP
- **Signed Cookies**: Multiple files, don't change URLs
- **Custom Error Pages**: Custom HTML for 4xx/5xx errors
- **Cache Invalidation**: First 1000 paths free/month, then $0.005/path
- **Geo-Restriction**: Whitelist/blacklist countries
- **Lambda@Edge**: Run code at edge (30s timeout)
- **CloudFront Functions**: Lightweight (<1ms), viewer request/response

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

### ALB Advanced Features
- **Path-Based Routing**: Route by URL path, query strings, headers
- **Host-Based Routing**: Multiple domains on one ALB
- **Cognito Integration**: Offload authentication to ALB
- **Lambda Targets**: Invoke Lambda from ALB
- **IP as Targets**: Route to on-premises via IP
- **Slow Start Mode**: Gradual traffic increase to new targets
- **Sticky Sessions**: Route to same target (session affinity)
- **Connection Draining**: Complete in-flight requests before terminating

### NLB Features
- **Static IP**: One static IP per AZ
- **Preserve Source IP**: Client IP visible to targets
- **TLS Termination**: Decrypt at NLB
- **Ultra-Low Latency**: Millions of requests/sec
- **TCP/UDP/TLS**: Layer 4 protocols
- **PrivateLink**: Expose services privately

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

**Key Points:**
- **SSD (gp/io)**: Small random I/O, transactional workloads, databases
- **HDD (st/sc)**: Large sequential I/O, big data, cannot be boot volumes
- **gp3**: Most cost-effective for general workloads, tune IOPS/throughput independently
- **io2**: 99.999% durability, critical databases

---

## FSx FILE SYSTEMS

- **FSx for Windows**: SMB, Active Directory, Multi-AZ, DFS, shadow copies
- **FSx for Lustre**: HPC, ML, 100s GB/s, S3 integration, data repository tasks
- **FSx for NetApp ONTAP**: NFS, SMB, iSCSI, multi-protocol
- **FSx for OpenZFS**: Linux, snapshots, compression

### FSx for Lustre Deployment Types
- **Scratch**: Temporary, 6x faster, no replication
- **Persistent**: Long-term, HA, auto-replication

---

## ELASTICACHE

### Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Persistence | Yes | No |
| Replication | Yes (Multi-AZ) | No |
| Backup/Restore | Yes | No |
| Data Types | Advanced (sorted sets, lists) | Simple (strings) |
| Multi-threaded | No | Yes |
| Pub/Sub | Yes | No |
| Use Case | HA, persistence, complex | Simple, multi-core, distributed |

### DAX (DynamoDB Accelerator)
- **DynamoDB-only** cache
- **Microsecond** latency (vs milliseconds)
- **Drop-in compatible** with DynamoDB API
- **Write-through** caching

---

## DATABASE ADVANCED FEATURES

### RDS Features
- **Multi-AZ**: Sync replication, auto-failover (1-2 min), same region HA
- **Read Replicas**: Async, read scaling, can be cross-region, up to 15
- **IAM Auth**: Token-based (15 min), MySQL/PostgreSQL/Aurora only
- **Storage Auto Scaling**: Auto-increase when <10% free
- **Blue/Green Deployments**: Test on clone, 1-min switchover
- **Enhanced Monitoring**: OS-level metrics (1-60 second intervals)
- **Performance Insights**: Database performance monitoring

### Aurora Features
- **Aurora Global Database**: <1s replication lag, <1 min failover, 5 secondary regions
- **Aurora Serverless**: Auto-scales ACUs, pay per second, intermittent workloads
- **Aurora Multi-Master**: Multiple write nodes (all regions)
- **Backtrack**: Rewind to point in time (no restore needed)
- **Parallel Query**: Faster analytical queries
- **Cloning**: Fast DB clones (copy-on-write)

### DynamoDB
- **Auto Scaling**: Target 70% utilization
- **Global Tables**: Multi-region, multi-active, last-writer-wins
- **Streams**: Change data capture, 24-hour retention
- **On-Demand**: Pay per request (vs Provisioned)
- **Transactions**: ACID support
- **TTL**: Auto-delete expired items

---

## PLACEMENT GROUPS

- **Cluster**: Single AZ, low latency (10 Gbps), HPC
- **Spread**: Max 7/AZ, isolated, critical apps
- **Partition**: 7 partitions/AZ, Hadoop/Kafka

---

## ECS & CONTAINERS

- **Task Definition**: Blueprint (image, CPU, memory, ports, IAM roles)
- **Dynamic Port Mapping**: ALB + awsvpc/bridge network mode
- **ECS on Outposts**: On-premises AWS (vs Local Zones for low latency)
- **Fargate**: Serverless containers, no EC2 management
- **EC2 Launch Type**: More control, Reserved Instance savings

---

## AUTO SCALING

- **Target Tracking**: Maintain metric at target (e.g., 70% CPU)
- **Step Scaling**: Different actions for different thresholds
- **Scheduled Scaling**: Predictable load patterns
- **Cooldown**: 5 min default, prevents rapid scaling
- **Standby State**: Upgrade instance without traffic
- **Lifecycle Hooks**: Custom actions during launch/terminate

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

### Security Services

- **GuardDuty**: Threat detection (CloudTrail, VPC Flow, DNS logs)
- **AWS Config**: Compliance monitoring, auto-remediation
- **Security Hub**: Centralized security findings
- **WAF**: Web Application Firewall, rate-based rules, geo-blocking
- **Shield**: DDoS protection (Standard free, Advanced paid)
- **Inspector**: EC2/container vulnerability scanning
- **Macie**: S3 data classification, PII detection

---

## S3 ADVANCED FEATURES

- **Multipart Upload**: Use >100MB, required >5GB
- **Transfer Acceleration**: 50-500% faster, use s3-accelerate endpoint
- **Byte-Range Fetches**: Parallel downloads, resume on failure
- **Pre-Signed URLs**: Temporary access, configurable expiry
- **Object Lock**: Compliance (can't delete), Governance (can bypass)
- **Bucket Keys (SSE-KMS)**: Reduce KMS calls by 99%
- **Cross-Region Replication**: Versioning required, new objects only
- **Requester Pays**: Requester pays transfer, owner pays storage
- **Block Public Access**: 4 settings (account + bucket level)
- **Server Access Logging**: Must enable manually

---

## LAMBDA DEPLOYMENT

- **Version**: Immutable snapshot
- **$LATEST**: Mutable, current code
- **Alias**: Pointer to version(s)
- **Weighted alias**: Split traffic (10% v2, 90% v1)

### Lambda Advanced Features
- **Provisioned Concurrency**: Pre-warmed instances, no cold starts
- **Reserved Concurrency**: Limit max concurrent executions
- **Environment Variables**: Can be encrypted with KMS
- **Layers**: Share code/libraries across functions (up to 5 layers)
- **Extensions**: Integrate monitoring, security tools
- **Lambda@Edge**: Run at CloudFront edge locations (30s timeout)
- **CloudFront Functions**: Lightweight (<1ms), viewer request/response only

### Lambda Limits
- **Memory**: 128 MB - 10 GB (1 MB increments)
- **Timeout**: Max 15 minutes
- **Deployment Package**: 50 MB (zipped), 250 MB (unzipped)
- **Concurrent Executions**: 1000 per region (can request increase)
- **/tmp Storage**: 512 MB - 10 GB

---

## API GATEWAY

- **REST API**: HTTP/HTTPS APIs, full feature set
- **HTTP API**: Lower latency, lower cost (70% cheaper), simpler
- **WebSocket API**: Two-way communication, real-time
- **Edge-Optimized**: CloudFront distribution (default)
- **Regional**: Same region as API
- **Private**: VPC endpoint only
- **Throttling**: 10,000 RPS steady-state, 5,000 burst (returns 429)
- **Caching**: TTL 0-3600 seconds
- **Stage Variables**: Environment-specific configuration
- **Canary Deployments**: Test new versions with % traffic

---

## IAM & COGNITO

### IAM Key Concepts
- **IAM User**: Long-term credentials, specific person/service
- **IAM Role**: Temporary credentials, assumed by entities
- **IAM Policy**: JSON document defining permissions
- **IAM Group**: Collection of users with shared permissions
- **Permission Boundaries**: Maximum permissions a user can have
- **Policy Evaluation**: Explicit DENY → Explicit ALLOW → Implicit DENY

### Federation
- **SAML 2.0**: Enterprise identity (Active Directory, ADFS)
- **Web Identity**: Social logins (Google, Facebook, Amazon)
- **AWS SSO (IAM Identity Center)**: Multi-account centralized access
- **Custom Identity Broker**: Custom authentication + STS

### Cognito
- **User Pools**: User directory, authentication (sign-up/sign-in)
- **Identity Pools**: Authorization, temporary AWS credentials
- **Social Identity Providers**: Google, Facebook, Amazon, Apple
- **SAML Identity Providers**: Enterprise federation
- **Use Case**: User Pools (authenticate WHO), Identity Pools (authorize WHAT)

---

## WELL-ARCHITECTED FRAMEWORK (6 Pillars)

### 1. Operational Excellence
- **Design Principles**: IaC, annotate documentation, small reversible changes, refine procedures, anticipate failure, learn from failures
- **Key Services**: CloudFormation, Config, CloudWatch, CloudTrail, X-Ray

### 2. Security
- **Design Principles**: Strong identity foundation, traceability, security at all layers, automate security, protect data in transit/at rest, least privilege
- **Key Services**: IAM, Cognito, KMS, CloudTrail, GuardDuty, Security Hub, WAF, Shield

### 3. Reliability
- **Design Principles**: Test recovery, auto-recover, scale horizontally, stop guessing capacity, manage change through automation
- **Key Services**: Multi-AZ, Auto Scaling, Route 53, Backup, CloudFormation

### 4. Performance Efficiency
- **Design Principles**: Use advanced technologies, go global in minutes, use serverless, experiment, consider mechanical sympathy
- **Key Services**: CloudFront, Lambda, Auto Scaling, EBS types, ElastiCache

### 5. Cost Optimization
- **Design Principles**: Adopt consumption model, measure efficiency, stop spending on data center, analyze expenditure, use managed services
- **Key Services**: Cost Explorer, RIs, Savings Plans, S3 lifecycle, Auto Scaling

### 6. Sustainability
- **Design Principles**: Understand impact, establish goals, maximize utilization, adopt efficient hardware, use managed services, reduce downstream impact
- **Key Services**: EC2 Auto Scaling, Graviton processors, Lambda, S3 Intelligent-Tiering

---

## DISASTER RECOVERY (DR) STRATEGIES

**RTO** (Recovery Time Objective): How quickly to recover  
**RPO** (Recovery Point Objective): How much data loss acceptable

| Strategy | RTO | RPO | Cost | When to Use |
|----------|-----|-----|------|-------------|
| **Backup & Restore** | Hours-Days | Hours | 💰 | Non-critical, cost-sensitive |
| **Pilot Light** | 10min-Hours | Minutes | 💰💰 | Important, some downtime OK |
| **Warm Standby** | Minutes | Seconds | 💰💰💰 | Business-critical |
| **Multi-Site** | Real-time | Near-zero | 💰💰💰💰 | Mission-critical, zero downtime |

### Implementation Details
- **Backup & Restore**: Daily backups to S3, deploy from scratch during disaster
- **Pilot Light**: DB replica running, AMIs ready, scale up during disaster
- **Warm Standby**: Scaled-down full stack (30% capacity), scale to 100% on DR
- **Multi-Site**: Full capacity in multiple regions, Route 53 active-active

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
❌ **SCPs affect management account** → They DON'T  
❌ **File Gateway = blocks** → Files as S3 objects  
❌ **Volume Gateway = S3 console access** → Blocks only  
❌ **Tape Gateway for file access** → For backup/archive only  
❌ **DataSync = database migration** → Files only (use DMS for DBs)  
❌ **Snowball for <10TB** → Use DataSync or direct upload  
❌ **SQS FIFO unlimited throughput** → 300 msg/s (3000 batched)  
❌ **EventBridge = SNS** → EB for event routing, SNS for pub/sub  
❌ **Step Functions = Lambda** → Orchestration vs single function  

---

## QUICK DECISION TREES

### Need High Availability?
- **Database**: Multi-AZ RDS or Aurora Global
- **Compute**: Multi-AZ + Auto Scaling + ALB
- **Storage**: S3 (11 9's durability) or EFS (Multi-AZ)
- **DNS**: Route 53 with health checks + failover

### Need to Reduce Costs?
- **Compute**: Spot instances, RIs, Savings Plans, right-sizing
- **Storage**: S3 lifecycle policies, Intelligent-Tiering, delete unused
- **Database**: Aurora Serverless, RDS RIs, right-size instances
- **Network**: VPC endpoints (avoid NAT gateway charges)

### Need Better Performance?
- **Database**: ElastiCache (Redis/Memcached), DAX (DynamoDB)
- **Compute**: Larger instance, placement groups, ENA/EFA
- **Storage**: Provisioned IOPS (io2), instance store
- **Content**: CloudFront CDN, S3 Transfer Acceleration

### Need More Security?
- **Network**: Private subnets, NACLs, Security Groups, VPC endpoints
- **Data**: KMS encryption, S3 encryption, RDS encryption
- **Access**: MFA, least privilege IAM, SCPs
- **Monitoring**: CloudTrail, GuardDuty, Config, Security Hub

### Serverless Architecture?
- **Compute**: Lambda
- **API**: API Gateway
- **Database**: DynamoDB
- **Storage**: S3
- **Auth**: Cognito
- **Orchestration**: Step Functions

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
- **"Decoupled"** → SQS, SNS, EventBridge
- **"Disaster recovery"** → Pilot Light, Warm Standby, Multi-Site
- **"Cannot be overridden"** → SCPs (not IAM policies)
- **"Temporary credentials"** → IAM roles, STS, Cognito Identity Pools

---

## TEST-TAKING STRATEGIES

### Before the Exam
1. ✅ Review this card 2-3 times
2. ✅ Get good sleep (8 hours)
3. ✅ Eat a light meal before exam
4. ✅ Arrive 15 minutes early (or log in early for online)

### During the Exam
1. **Read Carefully**: Every word matters
2. **Eliminate Wrong Answers**: Remove obviously incorrect options first
3. **Look for Keywords**: "lowest cost", "highest performance", etc.
4. **Flag & Move On**: If stuck >2 minutes, flag and continue
5. **Watch for Traps**: Services that sound right but aren't optimal
6. **Consider All Requirements**: Cost AND performance AND security

### Common Traps
- ❌ Services that work but aren't optimal
- ❌ Missing required configurations (e.g., DNS for VPC peering)
- ❌ Wrong region requirements (CloudFront cert = us-east-1)
- ❌ Assuming default behaviors that don't exist
- ❌ Confusing similar services (EBS types, storage classes)

### If Unsure
1. What is the PRIMARY requirement? (cost, performance, security?)
2. What is EXPLICITLY stated vs assumed?
3. Which answer is MOST aligned with AWS best practices?
4. Which is the SIMPLEST solution that meets requirements?

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
- [ ] SCPs don't affect management account
- [ ] Storage Gateway: File (S3 objects), Volume (blocks), Tape (archive)
- [ ] DataSync (files), DMS (databases), Snow (physical)
- [ ] SQS FIFO: 300 msg/s, ends in .fifo
- [ ] EventBridge (event routing), SNS (pub/sub), SQS (queue)
- [ ] Step Functions (workflows), Lambda (single function)
- [ ] Aurora Global: <1s lag, <1min failover
- [ ] RDS IAM Auth: 15 min token
- [ ] ECS dynamic ports: ALB required
- [ ] Auto Scaling cooldown: 5 minutes

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

