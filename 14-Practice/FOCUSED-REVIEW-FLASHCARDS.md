# Focused Review Flashcards - Common Weak Areas

This flashcard set focuses on the most commonly missed topics in SAA-C03 practice exams.

---

## 🔐 Security & IAM (High Difficulty Topics)

### Card 1: IAM Policy Evaluation Logic
**Q:** What is the order of evaluation for IAM policies?  
**A:** 
1. **Explicit DENY** (highest priority - always wins)
2. **Explicit ALLOW** (only if no deny)
3. **Implicit DENY** (default if no allow exists)

**Key Point**: Any explicit DENY overrides all ALLOWs.

---

### Card 2: IAM Roles vs Resource Policies
**Q:** When should you use IAM roles vs resource-based policies for cross-account access?  
**A:**
- **IAM Role**: User assumes role, gives up original permissions temporarily
- **Resource Policy**: User retains original permissions while accessing resource
- **Use Resource Policy**: When you need to access resources in both accounts simultaneously (e.g., copy S3 bucket to bucket across accounts)

---

### Card 3: KMS Key Types
**Q:** What are the differences between KMS key types?  
**A:**
- **AWS Managed**: Free, automatic rotation yearly, managed by AWS
- **Customer Managed**: $1/month, manual/automatic rotation, full control
- **AWS Owned**: Free, no access/control, used by AWS services
- **CloudHSM**: Dedicated hardware, FIPS 140-2 Level 3, full control

**Exam Tip**: Compliance requirements = Customer Managed or CloudHSM

---

### Card 4: Secrets Manager vs Parameter Store
**Q:** When to use Secrets Manager vs Parameter Store?  
**A:**

| Feature | Secrets Manager | Parameter Store |
|---------|----------------|-----------------|
| **Auto Rotation** | ✅ Native (RDS, Redshift, DocumentDB) | ❌ Manual via Lambda |
| **Cost** | $0.40/secret/month + API calls | Free (Standard), $0.05/param (Advanced) |
| **Cross-account** | ✅ Yes | ❌ No (without additional setup) |
| **Use for** | DB passwords, API keys needing rotation | Config data, non-rotating secrets |

**Exam Tip**: Automatic rotation = Secrets Manager

---

### Card 5: GuardDuty vs Inspector vs Macie
**Q:** What is the difference between GuardDuty, Inspector, and Macie?  
**A:**
- **GuardDuty**: Threat detection (malicious activity, unauthorized behavior) - Uses ML
- **Inspector**: Vulnerability assessment (CVEs, network exposure, agent-based)
- **Macie**: Data security (PII discovery in S3, sensitive data classification)

**Memory Trick**: 
- **Guard**Duty = **Guard** against threats
- **Inspector** = **Inspect** for vulnerabilities
- **Macie** = **Maintain** data privacy

---

## 🗄️ Database (High Difficulty Topics)

### Card 6: RDS Multi-AZ vs Read Replicas
**Q:** What are the key differences between Multi-AZ and Read Replicas?  
**A:**

| Feature | Multi-AZ | Read Replicas |
|---------|----------|---------------|
| **Purpose** | High availability (HA) | Read scalability |
| **Replication** | Synchronous | Asynchronous |
| **Endpoint** | Same DNS (automatic failover) | Different DNS per replica |
| **Writes** | Primary only | Primary only |
| **Reads** | Primary only (standby not accessible) | Can read from replicas |
| **Backups** | From standby (no perf impact) | Can use for backups |
| **Cross-Region** | ❌ Same region only | ✅ Yes |

**Exam Tip**: HA/DR = Multi-AZ; Read scaling = Read Replicas

---

### Card 7: DynamoDB Capacity Modes
**Q:** On-Demand vs Provisioned capacity in DynamoDB?  
**A:**
- **On-Demand**: 
  - Pay per request
  - Auto-scales to workload
  - Good for: Unpredictable traffic, new apps, spiky workloads
  - Cost: 2.5x more expensive per request

- **Provisioned**:
  - Specify RCU/WCU
  - Auto-scaling available
  - Good for: Predictable traffic, steady workload
  - Cost: More economical at scale

**Exam Tip**: "Unpredictable" or "unknown traffic" = On-Demand

---

### Card 8: DynamoDB Indexes
**Q:** GSI vs LSI in DynamoDB?  
**A:**

| Feature | GSI (Global Secondary Index) | LSI (Local Secondary Index) |
|---------|------------------------------|----------------------------|
| **Partition Key** | Can be different | Must be same as base table |
| **Sort Key** | Can be different | Must be different |
| **Created** | Anytime | Only at table creation |
| **Projection** | All, Keys, Include | All, Keys, Include |
| **Capacity** | Separate RCU/WCU | Shares with base table |
| **Queries** | Eventually consistent | Strongly or eventually consistent |

**Exam Tip**: Need different partition key or create later = GSI

---

### Card 9: ElastiCache: Redis vs Memcached
**Q:** When to use Redis vs Memcached?  
**A:**

**Use Redis when you need:**
- Persistence/backup
- Multi-AZ with auto-failover
- Read replicas
- Complex data types (lists, sets, sorted sets)
- Pub/Sub messaging
- Transactions

**Use Memcached when you need:**
- Simple caching
- Multi-threaded performance
- Horizontal scaling (sharding)
- No persistence required

**Exam Tip**: HA, backup, complex data = Redis; Simple cache = Memcached

---

### Card 10: Aurora Key Features
**Q:** What makes Aurora special compared to RDS MySQL/PostgreSQL?  
**A:**
- **Performance**: 5x faster than MySQL, 3x faster than PostgreSQL
- **Storage**: Auto-scales 10GB → 128TB in 10GB increments
- **Replicas**: Up to 15 read replicas (RDS = 5)
- **Availability**: 6 copies across 3 AZs automatically
- **Endpoints**: Writer (R/W), Reader (load-balanced reads), Custom
- **Backtrack**: Rewind DB to previous point (without restore)
- **Global Database**: Cross-region replication (1 second lag)
- **Serverless**: Auto-scaling based on demand

**Exam Tip**: "Best performance" or "highest availability" = Aurora

---

## 🌐 Networking (High Difficulty Topics)

### Card 11: Security Groups vs NACLs
**Q:** What are the key differences between Security Groups and NACLs?  
**A:**

| Feature | Security Group | NACL |
|---------|----------------|------|
| **Level** | Instance | Subnet |
| **Rules** | Allow only | Allow and Deny |
| **Stateful** | Yes (return traffic auto-allowed) | No (must configure both inbound/outbound) |
| **Evaluation** | All rules (most permissive) | Rules in order (first match wins) |
| **Default** | Deny all inbound, allow all outbound | Allow all |

**Exam Tip**: Block specific IP = NACL (Security Groups can't deny)

---

### Card 12: VPC Endpoints
**Q:** Gateway Endpoints vs Interface Endpoints?  
**A:**

**Gateway Endpoints** (Free):
- Services: S3, DynamoDB only
- Uses: Route table entries
- No PrivateLink

**Interface Endpoints** (Paid - $0.01/hour):
- Services: Most AWS services (100+)
- Uses: ENI with private IP in subnet
- Powered by PrivateLink
- Can use Security Groups

**Exam Tip**: S3/DynamoDB = Gateway; Others = Interface

---

### Card 13: Route 53 Routing Policies
**Q:** What are the Route 53 routing policies and when to use each?  
**A:**

1. **Simple**: Single resource, no health checks
2. **Weighted**: A/B testing, gradual deployment (70/30 split)
3. **Latency**: Best performance for users (route to lowest latency)
4. **Failover**: Active-passive DR (primary/secondary)
5. **Geolocation**: Based on user's geographic location (GDPR compliance)
6. **Geoproximity**: Based on geography with bias (shift traffic)
7. **Multi-value**: Multiple resources with health checks (simple load balancing)

**Exam Tip**: "Best performance" = Latency; "DR" = Failover; "A/B test" = Weighted

---

### Card 14: Transit Gateway vs VPC Peering
**Q:** When to use Transit Gateway vs VPC Peering?  
**A:**

**VPC Peering**:
- Direct 1-to-1 connection
- No transitive routing
- Good for: Few VPCs (< 5)
- Cost: Data transfer only

**Transit Gateway**:
- Hub-and-spoke model
- Transitive routing (VPC A → TGW → VPC B → VPC C)
- Good for: Many VPCs, hybrid cloud, complex routing
- Cost: Attachment + data processing fees

**Exam Tip**: "Complex network" or "many VPCs" = Transit Gateway

---

### Card 15: Direct Connect vs VPN
**Q:** When to use Direct Connect vs VPN?  
**A:**

**VPN (Site-to-Site)**:
- Uses internet
- Quick setup (minutes)
- Encrypted by default
- Bandwidth: Up to 1.25 Gbps per tunnel
- Cost: Low ($0.05/hour)
- Good for: Immediate need, backup, temporary

**Direct Connect**:
- Dedicated private connection
- Setup: Weeks/months
- Must configure encryption (VPN over DX)
- Bandwidth: 1 Gbps → 100 Gbps
- Cost: Port hours + data transfer
- Good for: Large data transfer, consistent performance

**Best Practice**: DX with VPN backup

---

## 💾 Storage (High Difficulty Topics)

### Card 16: S3 Storage Classes Decision Tree
**Q:** How to choose the right S3 storage class?  
**A:**

1. **Frequently accessed** (>1/month) → **S3 Standard**
2. **Infrequent access** (>1/quarter) → **S3 Standard-IA** or **S3 One Zone-IA**
3. **Archive** (rarely accessed):
   - Minutes retrieval → **S3 Glacier Instant Retrieval**
   - 1-5 minutes → **S3 Glacier Flexible** (Expedited)
   - 3-5 hours → **S3 Glacier Flexible** (Standard)
   - 12 hours → **S3 Glacier Flexible** (Bulk)
   - 12-48 hours → **S3 Glacier Deep Archive**
4. **Unknown/changing** → **S3 Intelligent-Tiering**

**Minimum Storage Duration**:
- IA: 30 days
- Glacier Instant: 90 days
- Glacier Flexible: 90 days
- Glacier Deep: 180 days

---

### Card 17: S3 Replication
**Q:** CRR vs SRR in S3?  
**A:**

**Cross-Region Replication (CRR)**:
- Different regions
- Use cases: Compliance, lower latency, DR
- Can replicate to different storage class

**Same-Region Replication (SRR)**:
- Same region
- Use cases: Log aggregation, prod/dev sync, compliance

**Both Require**:
- Versioning enabled on source & destination
- Proper IAM permissions
- Only new objects replicated (unless using S3 Batch Replication)

**Exam Tip**: "Compliance" or "DR" across regions = CRR

---

### Card 18: EBS Volume Types
**Q:** Which EBS volume type for which use case?  
**A:**

**gp3/gp2 (General Purpose SSD)**:
- Boot volumes, dev/test, low-latency apps
- gp3: 3,000-16,000 IOPS (independent of size)
- gp2: IOPS tied to size (3 IOPS/GB)

**io2/io1 (Provisioned IOPS SSD)**:
- Critical business apps, databases (>16,000 IOPS)
- io2: 64,000 IOPS, 99.999% durability
- io1: 64,000 IOPS, 99.9% durability

**st1 (Throughput Optimized HDD)**:
- Big data, data warehouses, log processing
- Cannot be boot volume

**sc1 (Cold HDD)**:
- Infrequently accessed data
- Lowest cost
- Cannot be boot volume

**Exam Tip**: "High IOPS database" = io2; "Big data" = st1; "Lowest cost archive" = sc1

---

## ⚙️ Compute (High Difficulty Topics)

### Card 19: EC2 Purchasing Options
**Q:** When to use each EC2 purchasing option?  
**A:**

**On-Demand**: 
- Short-term, irregular workloads
- Pay by second
- No commitment

**Reserved Instances (1-3 years)**:
- Steady-state usage (databases, always-on)
- Up to 72% discount
- Standard (can't change instance type), Convertible (can change)

**Savings Plans (1-3 years)**:
- Flexible (instance family, size, OS, region)
- Up to 72% discount
- Commit to $ amount per hour

**Spot Instances**:
- Fault-tolerant, flexible workloads
- Up to 90% discount
- Can be interrupted with 2-min warning
- Good for: Batch jobs, data analysis, testing

**Dedicated Hosts**:
- Compliance, licensing (per-socket, per-core)
- Most expensive
- Full control over placement

**Exam Tip**: "Cost optimization" + "flexible" = Spot; "Steady-state" = Reserved

---

### Card 20: Load Balancer Types
**Q:** ALB vs NLB vs GWLB?  
**A:**

**Application Load Balancer (ALB)** - Layer 7:
- HTTP/HTTPS/gRPC
- Path-based, host-based routing
- WebSocket, HTTP/2
- Target: EC2, Lambda, IP, containers
- Use: Web applications, microservices

**Network Load Balancer (NLB)** - Layer 4:
- TCP/UDP/TLS
- Ultra-high performance (millions rps)
- Static IP, Elastic IP support
- Target: EC2, IP, ALB
- Use: Extreme performance, static IP needed

**Gateway Load Balancer (GWLB)** - Layer 3:
- Deploy/scale security appliances
- GENEVE protocol
- Transparent network gateway
- Use: Firewalls, IDS/IPS, DPI

**Exam Tip**: "Path routing" = ALB; "High performance" or "static IP" = NLB; "Security appliances" = GWLB

---

### Card 21: Auto Scaling Policies
**Q:** What are the Auto Scaling policy types?  
**A:**

1. **Target Tracking**: 
   - Maintain specific metric (e.g., CPU at 50%)
   - Simplest, recommended

2. **Step Scaling**:
   - Scale based on CloudWatch alarm thresholds
   - Different scaling adjustments for different alarm breaches

3. **Simple Scaling**:
   - Single scaling adjustment
   - Must wait for cooldown
   - Legacy (use Step instead)

4. **Scheduled**:
   - Scale at specific times
   - Known traffic patterns

5. **Predictive**:
   - ML-based forecasting
   - Proactive scaling

**Exam Tip**: "Maintain 70% CPU" = Target Tracking; "Traffic spike Mon 9am" = Scheduled

---

### Card 22: Lambda Limits & Best Practices
**Q:** What are critical Lambda limits and best practices?  
**A:**

**Key Limits**:
- **Timeout**: Max 15 minutes
- **Memory**: 128 MB to 10,240 MB (CPU scales with memory)
- **Deployment package**: 50 MB (zipped), 250 MB (unzipped)
- **Concurrent executions**: 1,000 (default, can increase)
- **Payload**: 6 MB (synchronous), 256 KB (asynchronous)

**Best Practices**:
- Keep functions small & focused
- Use environment variables for config
- Use layers for dependencies
- Set appropriate timeout (not max unless needed)
- Use reserved concurrency for critical functions
- Enable X-Ray for tracing
- Use VPC only when necessary (cold start impact)

**Exam Tip**: "Long-running task > 15 min" = NOT Lambda (use ECS/Batch)

---

## 🏗️ Architecture Patterns (High Difficulty Topics)

### Card 23: Disaster Recovery Strategies
**Q:** What are the DR strategies ranked by RTO/RPO?  
**A:**

1. **Backup & Restore** (Cheapest):
   - RTO: Hours, RPO: Hours
   - Regular backups to S3/Glacier
   - Restore when needed

2. **Pilot Light**:
   - RTO: 10s of minutes, RPO: Minutes
   - Core minimal version always running
   - Scale up when disaster occurs

3. **Warm Standby**:
   - RTO: Minutes, RPO: Seconds
   - Scaled-down fully functional version running
   - Scale up to production capacity

4. **Multi-Site/Hot Site** (Most expensive):
   - RTO: Real-time, RPO: Near-zero
   - Full production environment in multiple locations
   - Active-active

**Exam Tip**: Match RTO/RPO requirements to strategy cost

---

### Card 24: SQS Standard vs FIFO
**Q:** When to use SQS Standard vs FIFO?  
**A:**

**Standard**:
- Unlimited throughput
- At-least-once delivery (may duplicate)
- Best-effort ordering
- Use: High throughput, order doesn't matter

**FIFO**:
- 300 msg/s (3,000 with batching)
- Exactly-once processing
- Strict ordering (within message group)
- Name must end in .fifo
- Use: Order matters, no duplicates allowed

**Exam Tip**: "Order is critical" or "no duplicates" = FIFO; "Highest throughput" = Standard

---

### Card 25: EventBridge vs SNS vs SQS
**Q:** When to use EventBridge vs SNS vs SQS?  
**A:**

**EventBridge**:
- Event bus for AWS services, SaaS, custom apps
- Advanced filtering (content-based)
- Schema registry
- Multiple targets per rule
- Use: Event-driven architecture, AWS service integration

**SNS**:
- Pub/Sub messaging
- Fan-out to multiple subscribers
- Mobile push, SMS, email
- Use: Send notifications to multiple systems

**SQS**:
- Queue for decoupling
- Pull-based (consumers poll)
- Message persistence (up to 14 days)
- Use: Async processing, workload buffering

**Pattern**: SNS → SQS fan-out for durable delivery to multiple queues

---

### Card 26: CloudFront Use Cases
**Q:** When and why use CloudFront?  
**A:**

**Key Use Cases**:
1. **Static content delivery**: S3 + CloudFront (global distribution)
2. **Dynamic content acceleration**: API Gateway, ALB origin
3. **Video streaming**: On-demand, live streaming
4. **Security**: AWS Shield, WAF integration, DDoS protection
5. **HTTPS**: Free SSL/TLS with ACM
6. **Geo-restriction**: Allow/block countries
7. **Private content**: Signed URLs/Cookies

**Benefits**:
- Low latency (edge locations)
- DDoS protection (Shield Standard free)
- Cost reduction (less origin requests)
- HTTPS at edge

**Exam Tip**: "Global users" + "low latency" = CloudFront

---

### Card 27: API Gateway Endpoint Types
**Q:** What are API Gateway endpoint types?  
**A:**

**Edge-Optimized** (Default):
- CloudFront edge locations
- Best for: Global users
- Lower latency worldwide

**Regional**:
- Same region as API
- Best for: Users in same region, custom CDN
- Lower cost if users in one region

**Private**:
- Only accessible from VPC (via VPC endpoint)
- Best for: Internal APIs
- Most secure

**Exam Tip**: "Internal only" = Private; "Global users" = Edge-Optimized

---

## 💰 Cost Optimization (High Difficulty Topics)

### Card 28: S3 Cost Optimization
**Q:** How to optimize S3 costs?  
**A:**

1. **Lifecycle Policies**:
   - Transition to IA after 30 days
   - Transition to Glacier after 90 days
   - Delete after retention period

2. **Intelligent-Tiering**:
   - Auto-moves between tiers
   - Small monitoring fee

3. **S3 Select/Glacier Select**:
   - Retrieve subset of data
   - 80% cost reduction

4. **Compression**:
   - Reduce storage & transfer costs

5. **Delete incomplete multipart uploads**:
   - Lifecycle rule to clean up

6. **Requester Pays**:
   - Requester pays transfer costs

**Exam Tip**: "Unknown access patterns" = Intelligent-Tiering

---

### Card 29: EC2 Cost Optimization
**Q:** Best practices for EC2 cost optimization?  
**A:**

1. **Right-sizing**: Use CloudWatch to match instance to actual usage
2. **Reserved Instances**: For steady-state (up to 72% savings)
3. **Savings Plans**: Flexible commitment (up to 72% savings)
4. **Spot Instances**: Fault-tolerant workloads (up to 90% savings)
5. **Auto Scaling**: Scale down when not needed
6. **Stop instances**: Instead of keeping idle
7. **Use newer generations**: Better price/performance
8. **Use AWS Compute Optimizer**: ML recommendations

**Exam Tip**: Always match the pricing model to workload characteristics

---

### Card 30: Trusted Advisor Cost Checks
**Q:** What cost optimization checks does Trusted Advisor provide?  
**A:**

**Free Tier** (Basic/Developer Support):
- Service limits
- Basic security checks

**Business/Enterprise Support**:
- **Idle/underutilized resources**: ELB, EC2, RDS
- **Unassociated Elastic IPs**
- **Unused/underutilized EBS volumes**
- **RDS idle instances**
- **Reserved Instance optimization**
- **Low utilization EC2 instances**

**Exam Tip**: "Identify cost savings" = Trusted Advisor (Business+ support)

---

## 🔄 Integration & Migration (High Difficulty Topics)

### Card 31: Database Migration Service (DMS)
**Q:** What are DMS migration types and use cases?  
**A:**

**Migration Types**:
1. **Full Load**: One-time complete migration
2. **Full Load + CDC**: Migration + ongoing changes
3. **CDC Only**: Replicate ongoing changes only

**Common Patterns**:
- **Homogeneous**: Oracle → Oracle (same engine)
- **Heterogeneous**: Oracle → Aurora PostgreSQL (different engine - need SCT)

**Schema Conversion Tool (SCT)**:
- Required for heterogeneous migrations
- Converts schema, stored procedures, functions

**Exam Tip**: "Minimal downtime DB migration" = DMS with CDC

---

### Card 32: Storage Gateway Types
**Q:** What are Storage Gateway types and when to use each?  
**A:**

**File Gateway** (S3):
- NFS/SMB protocol
- Caches frequently accessed files
- Use: File shares, backups to S3

**Volume Gateway**:
- **Stored Volume**: All data on-premises, async backup to S3 (EBS snapshots)
- **Cached Volume**: Primary data in S3, cache frequently used locally
- Use: Block storage, DR

**Tape Gateway** (S3/Glacier):
- Virtual tape library (VTL)
- Use: Backup apps (Veeam, NetBackup)

**Exam Tip**: "NFS file share to S3" = File Gateway; "Virtual tapes" = Tape Gateway

---

### Card 33: DataSync vs Transfer Family
**Q:** When to use DataSync vs Transfer Family?  
**A:**

**DataSync**:
- **Purpose**: Large-scale data transfer/sync
- **Protocols**: NFS, SMB, HDFS, S3 API
- **Targets**: S3, EFS, FSx
- **Features**: Automatic encryption, validation, bandwidth throttling
- **Use**: One-time migrations, periodic sync, replication

**Transfer Family**:
- **Purpose**: SFTP/FTPS/FTP server as a service
- **Protocols**: SFTP, FTPS, FTP
- **Storage**: S3, EFS
- **Features**: Managed service, existing workflows
- **Use**: Replace existing FTP servers, B2B transfers

**Exam Tip**: "Migrate NFS server" = DataSync; "SFTP users uploading" = Transfer Family

---

### Card 34: Snow Family
**Q:** When to use each Snow device?  
**A:**

**Snowcone** (8-14 TB):
- Smallest, portable
- Edge computing (EC2, Lambda)
- Use: Edge locations, IoT, offline transfer < 14 TB

**Snowball Edge** (80 TB / 210 TB):
- Storage Optimized (80 TB) or Compute Optimized (42 TB)
- Local compute (EC2, Lambda)
- Use: Large migrations, edge computing

**Snowmobile** (100 PB):
- Shipping container on truck
- Exabyte-scale
- Use: Data center migration

**Rule of Thumb**: 
- < 1 week over network → Use network
- > 1 week → Use Snow device

**Exam Tip**: "PB+ data" or "< 10 Gbps network" = Snow Family

---

### Card 35: Application Migration Service vs Server Migration Service
**Q:** What's the difference between MGN and SMS?  
**A:**

**Application Migration Service (MGN)** - Current:
- Lift-and-shift (rehost) for physical, virtual, cloud servers
- Continuous block-level replication
- Automated conversion
- Minimal downtime
- **Recommended service**

**Server Migration Service (SMS)** - Legacy:
- Being replaced by MGN
- Agentless, VMware-focused
- Scheduled migrations

**Exam Tip**: For exam questions after 2022, assume MGN (AWS CloudEndure migration)

---

## Study Strategy
- Review 5-10 cards daily
- Focus on cards you get wrong
- Create your own cards for weak areas
- Practice with scenario-based questions
- Use these as quick reference before exam

---

*These flashcards cover the highest-difficulty topics that candidates commonly struggle with. Review regularly for best results.*

