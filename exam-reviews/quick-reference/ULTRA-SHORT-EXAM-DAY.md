# ⚡ EDGE CASES & EXAM TRAPS - ULTRA-SHORT

**Last-Minute Review • Focus on Tricky Scenarios • 20 mins**  
**Updated:** March 6, 2026 • **All 7 Practice Tests Covered**

---

## 🔥 CRITICAL EDGE CASES (Top 25)

### CloudFront & CDN Gotchas
1. **CloudFront ACM Certificate = MUST be us-east-1** (even for EU/APAC origins!)
   - ❌ TRAP: "Use closest region to users" 
   - ❌ TRAP: "Same region as origin"

2. **CloudFront Signed URLs vs Signed Cookies**
   - Signed URLs = Single file access
   - Signed Cookies = Multiple files (premium content areas)
   - ❌ TRAP: "Always use signed URLs for protected content"
   
3. **CloudFront vs Global Accelerator**
   - CloudFront = HTTP/HTTPS ONLY, caches content
   - Global Accelerator = TCP/UDP/HTTP, NO caching, 2 static IPs
   - ❌ TRAP: Using CloudFront for UDP gaming traffic

### VPC & Networking Edge Cases
4. **Gateway Endpoints = S3 + DynamoDB ONLY, Interface = Everything else**
   - ❌ TRAP: "Use Gateway endpoint for ECR" (needs Interface!)
   - Gateway = FREE, route table entry, no IP
   - Interface = $0.01/hr + data, ENI with private IP

5. **Gateway Endpoints NOT Transitive** ⚠️ NEW (Test 6)
   - VPC-A has S3 endpoint, VPC-B peered to VPC-A
   - VPC-B CANNOT use VPC-A's endpoint
   - ❌ TRAP: "Peer VPCs to share S3 endpoint"
   - ✅ Solution: Create S3 endpoint in EACH VPC (it's FREE!)

6. **Subnet CIDR Calculations** ⚠️ NEW (Test 6)
   - Formula: Usable IPs = 2^(32-n) - 5 (AWS reserves 5 IPs)
   - /28 = 16 total - 5 = 11 usable (NOT 16!)
   - /27 = 32 total - 5 = 27 usable
   - ❌ TRAP: "Forgetting the 5 reserved IPs"

7. **Transit Gateway ECMP vs VPG**
   - VPG = 1.25 Gbps MAX (only 1 tunnel active, others standby)
   - TGW = 50+ Gbps (multiple tunnels active via ECMP)
   - ❌ TRAP: "Scale VPG with multiple tunnels" (doesn't work!)

8. **Direct Connect BGP Community Tags** ⚠️ NEW (Test 7)
   - Public VIF routing scope:
     - 7224:9100 = Local region only
     - 7224:9200 = All regions in continent
     - 7224:9300 = Global (all regions)
   - ❌ TRAP: "Use Local Preference on Public VIF" (NOT supported!)
   - ✅ Use BGP community tags instead

9. **NAT Gateway Cost Optimization** ⚠️ NEW (Test 7)
   - Public NAT = Internet access (needs EIP)
   - Private NAT = VPC/on-premises connectivity (no EIP)
   - ❌ TRAP: "Single NAT Gateway for multi-AZ" (cross-AZ charges!)
   - ✅ Deploy one NAT Gateway per AZ to avoid cross-AZ data transfer

10. **VPC Flow Logs = Accept + Reject traffic** (NOT just rejected)
    - ❌ TRAP: "Flow logs only show denied traffic"
    - Captures: Source, destination, ports, protocol, bytes
    - Does NOT capture: Packet contents, DNS queries to Route 53

11. **VPC Peering = NO transitive routing**
    - VPC A ↔ VPC B ↔ VPC C: A cannot reach C
    - ❌ TRAP: "Chain VPC peerings" (doesn't work!)
    - Solution: Transit Gateway for hub-and-spoke

### Multi-AZ & HA Edge Cases
12. **RDS Multi-AZ Standby = NOT readable** (synchronous, standby only)
    - Read Replica = Readable (asynchronous)
    - ❌ TRAP: "Use Multi-AZ standby for read scaling"
    - Multi-AZ = HA/DR, Read Replica = Performance

13. **Aurora Global Database = 1 master region** (other regions read-only)
    - DynamoDB Global Tables = Multi-master (all regions writable)
    - ❌ TRAP: Confusing which DB supports multi-master writes

14. **ALB Cross-Zone = ON by default** | NLB Cross-Zone = OFF by default
    - ❌ TRAP: Assuming same behavior for all LBs
    - NLB cross-zone = Additional data transfer charges

### Storage Edge Cases
15. **S3 Versioning = Can SUSPEND, CANNOT disable after enabling**
    - Delete with versioning = Delete marker (can recover)
    - ❌ TRAP: "Disable versioning to save costs"
    - Solution: Lifecycle policy to expire old versions

16. **S3 Glacier Restore ≠ Change storage class directly**
    - Must: Restore → Temp copy → Copy to target class → Delete original
    - ❌ TRAP: "Change bucket default class to migrate objects"
    - Default class only affects NEW uploads!

17. **S3 LIST operations = Expensive at scale**
    - ❌ TRAP: Using LIST for metadata queries on millions of objects
    - ✅ Solution: S3 Inventory + Athena queries

18. **EBS Multi-Attach = io1/io2 ONLY, same AZ only**
    - ❌ TRAP: "Multi-attach gp3 volumes" (not supported)
    - ❌ TRAP: "Multi-attach across AZs" (impossible)
    - Max 16 EC2 instances, cluster-aware filesystem required

### Compute Edge Cases
19. **ECS Fargate = NOT on Outposts** (EC2 launch type only)
    - ❌ TRAP: "Use Fargate for on-premises low latency"
    - Outposts = On-premises AWS, requires EC2 management

20. **ECS Dynamic Port Mapping = ALB ONLY** (NOT NLB/CLB)
    - hostPort: 0 = Dynamic allocation (ephemeral ports 32768-65535)
    - ❌ TRAP: "Use NLB with dynamic ports"
    - NLB/CLB = Static port mapping only

21. **Lambda Timeout = MAX 15 minutes** (900 seconds)
    - ❌ TRAP: "Use Lambda for 30-minute batch job"
    - Solution: Step Functions + multiple Lambdas, or use Fargate/Batch

22. **EC2 User Data vs Task Definition** ⚠️ NEW (Test 6)
    - User Data = EC2 instance bootstrap (runs at first boot)
    - Task Definition = ECS container configuration
    - ❌ TRAP: "Configure host OS via Task Definition"
    - ✅ Reality: User Data for host, Task Definition for containers

23. **Security Group Changes = Instant** ⚠️ NEW (Test 6)
    - Changes apply immediately (no reboot required)
    - Stateful (return traffic auto-allowed)
    - ❌ TRAP: "SG changes take 2-5 minutes to propagate"
    - ✅ Reality: Instant, no propagation delay

24. **EC2 Reserved Instance Scope**
    - Regional RI = Flexible AZ, NO capacity reservation
    - Zonal RI = Fixed AZ, capacity reservation included
    - Standard RI = Up to 72% off, cannot change instance type
    - Convertible RI = Up to 54% off, can change family/OS
    - ❌ TRAP: "Regional RI reserves capacity"
    - ✅ Reality: Only Zonal RI reserves capacity

### Database Edge Cases
22. **RDS Default Parameter Groups = Cannot Modify** ⚠️ NEW (Test 6)
    - Default parameter groups are read-only (AWS-managed)
    - ❌ TRAP: "Edit default parameter group settings"
    - ✅ Solution: Create custom parameter group (fully editable)

23. **DynamoDB Streams for Change Data Capture** ⚠️ NEW (Test 6)
    - 24-hour retention, ordered by key, Lambda trigger
    - ❌ TRAP: "Duplicate table to track changes"
    - ✅ Solution: Enable DynamoDB Streams (CDC built-in)

### Security Edge Cases
24. **KMS Multi-Region Keys** ⚠️ NEW (Test 7)
    - Default KMS keys = Regional (cannot decrypt in other regions)
    - Multi-Region Keys = Same key ID across regions
    - ❌ TRAP: "KMS keys are global"
    - ✅ Reality: Keys regional by default, must explicitly create multi-region

25. **AWS Directory Service Types** ⚠️ NEW (Test 7)
    - Simple AD = Max 500-5000 users, standalone, ~$36/month
    - AD Connector = Proxy to on-prem AD (requires VPN/DX), ~$36/month
    - Managed Microsoft AD = Enterprise features, 30K+ users, ~$146/month
    - ❌ TRAP: "Use Simple AD for 10,000 users"
    - ✅ Solution: Use AWS Managed Microsoft AD

---

## 📦 STORAGE EDGE CASES & TRAPS

### S3 Critical Edge Cases
**1. Glacier Restore Process (4-step, cannot skip!)**
- Step 1: Initiate restore (creates temporary accessible copy)
- Step 2: Wait 12-48hrs (Deep Archive) or 1-12hrs (Flexible)
- Step 3: Copy from temporary to target storage class
- Step 4: Delete Glacier version (optional)
- ❌ TRAP: "Change default class to migrate existing objects"
- Reality: Default class ONLY affects NEW uploads

**2. S3 Storage Class Minimum Charges**
- Standard-IA: Min 30 days storage, min 128KB per object
- ❌ TRAP: "Store 10KB files in Standard-IA to save money"
- Reality: Charged for 128KB × 30 days minimum

**3. S3 Object Lock Modes**
- Compliance = Root CANNOT delete (WORM)
- Governance = Can delete with s3:BypassGovernanceRetention permission
- Legal Hold = Indefinite, no expiration, toggle on/off
- ❌ TRAP: "Use Compliance if need emergency delete access"
- ⚠️ Versioning MUST be enabled for Object Lock

**4. S3 Encryption Key Management**
- SSE-S3 = AWS manages keys automatically, FREE
- SSE-KMS = AWS KMS keys, audit trail, can disable
- SSE-C = YOU provide key with EVERY request (HTTPS required)
- ❌ TRAP: "SSE-C = Provide key once" (WRONG, every request!)

**5. S3 Cross-Region Replication**
- Requires: Versioning ON in both buckets
- Does NOT replicate: Existing objects (only new), delete markers
- ❌ TRAP: "Enable CRR to replicate existing data"
- Solution: Use S3 Batch Replication for existing objects

**6. S3 Performance Optimization**
- LIST = Slow/expensive for millions of objects
- ✅ Use: S3 Inventory (daily/weekly) + Athena queries
- Multipart Upload: Required >100MB, recommended >5GB
- ❌ TRAP: Using DynamoDB index for S3 metadata "real-time queries"
- Reality: S3 Inventory sufficient for most use cases

### EBS Edge Cases
**7. EBS Volume Types - IOPS Limits**
- gp3: 16,000 IOPS max (3,000 baseline), 1,000 MB/s throughput
- io2: 64,000 IOPS (256,000 with Block Express)
- ❌ TRAP: "Need 100,000 IOPS = Use io2" (Block Express required!)

**8. EBS Snapshots - Incremental Behavior**
- First snapshot = Full copy
- Subsequent = Only changed blocks (delta)
- Delete middle snapshot: Only unique data deleted
- ❌ TRAP: "Delete all snapshots to save cost" (last one = full!)
- Reality: Can safely delete old snapshots, only delta removed

**9. EBS Multi-Attach Restrictions**
- io1/io2 ONLY (not gp2/gp3/st1/sc1)
- Same AZ only (cannot span AZs)
- Max 16 EC2 instances
- Requires cluster-aware filesystem (GFS2, OCFS2)
- ❌ TRAP: "Multi-attach for general file sharing"
- Reality: For specialized cluster applications only

### EFS Edge Cases
**10. EFS Performance Modes (Cannot change after creation!)**
- General Purpose (default): Max 7,000 ops/sec per filesystem
- Max I/O: >7,000 ops/sec, higher latency
- ❌ TRAP: "Start with General, upgrade to Max I/O later"
- Reality: Must choose at creation, cannot change

**11. EFS Throughput Modes**
- Bursting: Scales with storage size (50 MB/s per TB)
- Provisioned: Fixed throughput regardless of size
- Elastic: Auto-scales up to 3 GB/s read, 1 GB/s write
- ❌ TRAP: "Need high throughput on small filesystem = Bursting"
- Reality: Use Provisioned or Elastic

**12. EFS vs FSx Decision Matrix**
- EFS = Linux, NFS, POSIX, Multi-AZ by default
- FSx Windows = SMB, AD integration, DFS, Windows apps
- FSx Lustre = HPC, ML, POSIX, single AZ, S3 integration
- ❌ TRAP: "Use EFS for Windows file sharing"
- Reality: FSx for Windows File Server required

### Redshift Edge Cases
**13. Snapshot Cost Trap**
- Automated snapshots = 1-35 days retention, FREE (up to 1x cluster size)
- Manual snapshots = FOREVER until deleted (cost accumulates!)
- ❌ TRAP: "All snapshots auto-delete"
- Reality: Manual snapshots must be deleted manually (⚠️ cost trap!)

**14. Redshift Query Monitoring**
- Query performance = Redshift Console + System Tables (STL_QUERY)
- ❌ TRAP: "Use CloudTrail for slow query analysis"
- Reality: CloudTrail = API calls only, NOT query execution details
- CloudWatch = Cluster metrics (CPU, disk), NOT query performance

**15. Glacier Retrieval Tiers**
- Glacier Flexible: Expedited (1-5min, $0.03/GB), Standard (3-5hrs, $0.01/GB), Bulk (5-12hrs, $0.0025/GB)
- Glacier Deep: Standard (12hrs), Bulk (48hrs)
- ❌ TRAP: "Cannot restore Glacier objects"
- ✅ Reality: Must restore first, creates temporary copy, THEN access/copy

---

## 💾 DATABASE EDGE CASES & TRAPS

### RDS Critical Edge Cases
**15. Multi-AZ vs Read Replica Confusion**
- Multi-AZ Standby = NOT readable, synchronous, same region, auto-failover <60s
- Read Replica = Readable, asynchronous, can be cross-region, manual promotion
- ❌ TRAP: "Use Multi-AZ standby for read scaling"
- Reality: Multi-AZ = HA/DR ONLY, Read Replica = Performance/scaling

**16. RDS Encryption Limitations**
- Cannot encrypt existing unencrypted DB
- ❌ TRAP: "Enable encryption on running DB instance"
- Solution: Snapshot → Copy with encryption → Restore → Redirect app

**17. RDS Backup Window Behavior**
- Automated backup during window = Brief I/O suspension (Single-AZ)
- Multi-AZ = Backup from standby (no performance impact)
- ❌ TRAP: "Automated backups don't affect Multi-AZ performance"
- Reality: Single-AZ affected, Multi-AZ not affected

**18. RDS Read Replica Lag**
- Asynchronous replication = Replica lag possible
- Lag visible in CloudWatch: ReplicaLag metric
- ❌ TRAP: "Read replica = Real-time data" (not always!)
- Use case matters: Analytics (lag OK), critical reads (lag not OK)

### Aurora Edge Cases
**19. Aurora Global Database Architecture**
- 1 primary region (read-write)
- Up to 10 secondary regions (read-only) *(2025: was 5)*
- <1 second replication lag
- ❌ TRAP: "Aurora Global = Multi-master writes"
- Reality: DynamoDB Global Tables = Multi-master, Aurora = Single master

**20. Aurora Serverless v2 Scaling**
- Instant scaling (fraction of second)
- Scales in increments of 0.5 ACU
- Min: 0.5 ACU, Max: 128 ACU
- ❌ TRAP: "Serverless v1 = Same as v2"
- Reality: v1 = Cold starts, v2 = Instant scaling

**21. Aurora Backtrack vs Point-in-Time Recovery**
- Backtrack = Rewind in-place (no new cluster), seconds
- PITR = Restore to new cluster, minutes
- ❌ TRAP: "Backtrack = Free time travel"
- Reality: Limited to 72 hours, charges per backtrack change record

### DynamoDB Edge Cases
**22. GSI vs LSI Critical Differences**
- GSI = Different partition key, eventual consistency, can add anytime
- LSI = Same partition key, strong consistency option, must create with table
- Max: 20 GSIs, 5 LSIs per table
- ❌ TRAP: "Add LSI after table creation"
- Reality: LSI must be defined at table creation, cannot add later

**23. DynamoDB Capacity Modes**
- On-Demand = Pay per request, no planning, unpredictable traffic
- Provisioned = WCU/RCU, cheaper at scale, predictable traffic
- ❌ TRAP: "Always use On-Demand for cost savings"
- Reality: Provisioned cheaper if traffic predictable/high volume

**24. DynamoDB Streams + Lambda**
- Stream retention = 24 hours (not configurable)
- Batch size: 1-10,000 records
- ❌ TRAP: "Streams = Long-term audit log"
- Reality: Streams = Short-term trigger only (use DynamoDB + Kinesis for long-term)

**25. DynamoDB Global Tables Requirements**
- Streams must be enabled (NEW_AND_OLD_IMAGES)
- Tables must have same partition/sort key
- ❌ TRAP: "Enable Global Tables on existing table with different schema"
- Reality: All tables must have identical schema

**26. DynamoDB Item Size Limit**
- Max item size = 400KB (including attribute names)
- ❌ TRAP: "Store 1MB document in single item"
- Reality: Use S3 for large objects, store S3 key in DynamoDB

### ElastiCache Edge Cases
**27. Redis vs Memcached Decision**
- Redis = Persistence, Pub/Sub, sorted sets, complex data, Multi-AZ with failover
- Memcached = Simple cache, multi-threaded, horizontal scaling, no persistence
- ❌ TRAP: "Use Memcached for session store with failover"
- Reality: Redis required for persistence and HA

**28. ElastiCache Cluster Mode (Redis)**
- Cluster Mode Disabled = Single shard, up to 5 read replicas
- Cluster Mode Enabled = Multiple shards (partitions), 90 nodes max
- ❌ TRAP: "Cannot change cluster mode after creation"
- Reality: Must create new cluster and migrate data

---

## 🖥️ COMPUTE EDGE CASES & TRAPS

### EC2 & Auto Scaling Edge Cases
**29. CloudWatch Agent for Custom Metrics**
- Default EC2 metrics = CPU, Network, Disk I/O, Status checks
- Does NOT include: Memory, Disk space %, Swap usage
- ❌ TRAP: "Detailed monitoring adds memory metrics"
- Reality: Detailed monitoring only changes frequency (5min → 1min)
- Solution: Install CloudWatch Agent + aggregation_dimensions

**30. Auto Scaling aggregation_dimensions**
- Config: aggregation_dimensions: ["AutoScalingGroupName"]
- Effect: Aggregates metrics across all instances in ASG
- Without: 10 instances = 10 separate metrics
- ❌ TRAP: "Can scale on memory without aggregation"
- Reality: Aggregation simplifies ASG-level metric creation

**31. Auto Scaling Cooldown Period**
- Default: 300 seconds (5 minutes)
- Prevents: Rapid scaling (thrashing)
- ❌ TRAP: "Scale every minute based on spikes"
- Reality: Cooldown prevents premature scaling actions

**32. EC2 Instance Metadata Service (IMDS)**
- IMDSv1 = Open request/response (security risk)
- IMDSv2 = Session-oriented, token-based (recommended)
- ❌ TRAP: "IMDS v1 = Same security as v2"
- Reality: IMDSv2 prevents SSRF attacks, more secure

### Lambda Edge Cases
**33. Lambda Timeout = 15 minutes MAX**
- Max execution time = 900 seconds
- ❌ TRAP: "Use Lambda for 30-min batch processing"
- Solutions: Step Functions (orchestrate multiple), Fargate, Batch

**34. Lambda VPC Cold Start**
- Lambda in VPC = Requires ENI creation
- Old behavior = 10+ seconds cold start
- New (Hyperplane) = Sub-second ENI attachment
- ❌ TRAP: "Avoid VPC Lambda due to cold start"
- Reality: Hyperplane significantly reduced cold start delay

**35. Lambda Provisioned Concurrency**
- Pre-warmed instances = No cold start
- Cost = $0.000015 per GB-second (in addition to invocations)
- ❌ TRAP: "Always use provisioned concurrency"
- Reality: Only for latency-sensitive, high-traffic functions

**36. Lambda Layers**
- Max 5 layers per function
- Total unzipped size = 250MB (function + layers)
- ❌ TRAP: "Layers = Unlimited shared code"
- Reality: Size limits apply

### ECS Edge Cases
**37. ECS Task-Level Security Groups (awsvpc mode)**
- awsvpc = Each task gets own ENI + security group
- Bridge = Host security group applies to all tasks
- ❌ TRAP: "Bridge mode for task-specific security groups"
- Reality: awsvpc mode REQUIRED for task-level SGs

**38. ECS Dynamic Port Mapping**
- Requirements: ALB + (awsvpc OR bridge mode)
- Task definition: hostPort: 0 (dynamic)
- Ephemeral port range: 32768-65535
- ❌ TRAP: "NLB supports dynamic port mapping"
- Reality: ALB ONLY (NLB/CLB need static ports)

**39. ECS on AWS Outposts**
- Outposts = On-premises AWS hardware (<5ms latency requirement)
- Supported: ECS EC2 launch type ONLY
- NOT supported: ECS Fargate
- ❌ TRAP: "Use Fargate on Outposts for serverless"
- Reality: Must manage EC2 instances

**40. ECS Service Auto Scaling**
- Target Tracking = Based on metric (CPU, memory, ALB requests)
- Step Scaling = Based on CloudWatch alarm
- ❌ TRAP: "ECS service scaling = EC2 instance scaling"
- Reality: ECS service = Task scaling, separate from EC2 capacity

**41. ECS Task IAM Roles**
- Task Role = Permissions for application (S3, DynamoDB, etc.)
- Task Execution Role = Permissions for ECS agent (pull images, logs)
- ❌ TRAP: "One role for everything"
- Reality: Separate roles for security/least privilege

---

## 🌐 NETWORKING EDGE CASES & TRAPS

### VPC Edge Cases
**42. VPC Flow Logs Capture Behavior**
- Captures: Accepted AND rejected traffic (both!)
- Does NOT capture: Packet contents, DNS to Route 53, metadata service
- ❌ TRAP: "Flow logs only show denied traffic"
- Levels: VPC, Subnet, or ENI (choose appropriate granularity)

**43. Transit Gateway vs VPN Virtual Gateway**
- VPG throughput = 1.25 Gbps MAX (single active tunnel)
- TGW throughput = 50+ Gbps (ECMP across multiple tunnels)
- ❌ TRAP: "Add VPN connections to VPG for more bandwidth"
- Reality: Only 1 tunnel active at a time, others standby

**44. VPC Endpoints - Gateway vs Interface**
- Gateway Endpoints = S3 + DynamoDB ONLY, route table, FREE
- Interface Endpoints = All other services, ENI + IP, $0.01/hr/AZ + data
- ❌ TRAP: "Use Gateway endpoint for ECR" (needs Interface!)
- ❌ TRAP: "Interface endpoint for S3 to save cost" (Gateway is FREE!)

**45. NAT Gateway High Availability**
- NAT Gateway = Per AZ (not multi-AZ automatically)
- ❌ TRAP: "Deploy one NAT Gateway for multi-AZ HA"
- Reality: Need 1 NAT Gateway per AZ + route tables per AZ

**46. VPC Peering Limitations**
- No transitive routing: A↔B, B↔C ≠ A↔C
- No overlapping CIDR blocks
- ❌ TRAP: "Chain peerings to connect multiple VPCs"
- Solution: Transit Gateway for hub-and-spoke

**47. Security Groups vs NACLs**
- Security Groups = Stateful (return traffic auto-allowed)
- NACLs = Stateless (must explicitly allow return traffic)
- ❌ TRAP: "NACL allows outbound, return traffic works"
- Reality: Must allow inbound ephemeral ports (1024-65535)

### Load Balancer Edge Cases
**48. ALB vs NLB Cross-Zone Load Balancing**
- ALB = Cross-zone enabled by default, FREE
- NLB = Cross-zone disabled by default, data transfer charges
- ❌ TRAP: "All LBs behave the same for cross-zone"
- Reality: Different defaults and costs

**49. ALB Path-Based Routing Evaluation Order**
- More specific paths evaluated first
- Example: /api/users before /api/* before /*
- ❌ TRAP: "First rule matches always wins"
- Reality: Specificity matters

**50. NLB Target Health Checks**
- TCP health checks = Connection-based (open port = healthy)
- ❌ TRAP: "NLB health check = Application health"
- Reality: Port open doesn't mean app is working (use ALB for HTTP/HTTPS)

**51. Classic Load Balancer Limitations**
- No WebSocket support
- No dynamic port mapping (ECS)
- No path-based or host-based routing
- ❌ TRAP: "Use CLB for modern microservices"
- Reality: Use ALB or NLB (CLB is legacy)

### CloudFront Edge Cases
**52. CloudFront Origin Access Identity (OAI) vs Origin Access Control (OAC)**
- OAI = Legacy, S3 buckets only
- OAC = New, supports SSE-KMS, more secure
- ❌ TRAP: "OAI = Same as OAC"
- Reality: Migrate to OAC for SSE-KMS support

**53. CloudFront Signed URLs vs Signed Cookies**
- Signed URL = Single file access
- Signed Cookies = Multiple files access
- ❌ TRAP: "Always use signed URLs"
- Reality: Signed cookies better for multiple files

**54. CloudFront Field-Level Encryption**
- Encrypts specific POST fields at edge
- Separate from HTTPS (additional layer)
- ❌ TRAP: "HTTPS = End-to-end encryption for all fields"
- Reality: Field-level adds encryption beyond HTTPS for sensitive data

### Global Accelerator Edge Cases
**55. Global Accelerator vs CloudFront Use Cases**
- CloudFront = HTTP/HTTPS, caching, content delivery
- Global Accelerator = TCP/UDP/HTTP, no caching, static IPs
- ❌ TRAP: "Use CloudFront for UDP gaming traffic"
- Reality: Global Accelerator for non-HTTP protocols

**56. Global Accelerator Static IPs**
- Provides 2 static anycast IPs
- Benefits: No DNS changes, instant failover
- ❌ TRAP: "Need DNS for Global Accelerator"
- Reality: Static IPs eliminate DNS propagation delay

### Route 53 Edge Cases
**57. Route 53 Health Check for AWS Resources**
- ALB/CloudFront/API Gateway = Use "Evaluate Target Health" (FREE)
- ❌ TRAP: "Create health check for ALB" ($0.50/month unnecessary)
- Reality: "Evaluate Target Health" uses built-in checks

**58. Route 53 Alias Record Limitations**
- Can alias: CloudFront, ALB, NLB, S3 website, Elastic Beanstalk
- Cannot alias: EC2 instance, RDS endpoint
- ❌ TRAP: "Alias record to EC2 public IP"
- Reality: Use A record (not alias) for EC2

**59. Route 53 Private Hosted Zone**
- DNS for VPC (not internet-accessible)
- Requires: enableDnsHostnames + enableDnsSupport on VPC
- ❌ TRAP: "Private hosted zone works without VPC settings"
- Reality: Both VPC DNS settings must be enabled

**60. Route 53 Routing Policy - Geolocation vs Geoproximity**
- Geolocation = Route based on user's location (continent/country/state)
- Geoproximity = Route based on resource + user location with bias
- ❌ TRAP: "Geolocation = Closest resource"
- Reality: Geolocation = Fixed mapping, Geoproximity = Distance + bias

---

## 🔐 SECURITY EDGE CASES & TRAPS

### IAM Edge Cases
**61. Cross-Account Access - Role vs Resource Policy**
- Resource Policy = Simple, single resource (SQS, S3, Lambda)
- IAM Role = Complex, multiple services, detailed audit
- ❌ TRAP: "Always use IAM roles for cross-account"
- Reality: Resource policy simpler for single-service access

**62. IAM Permission Boundaries**
- Sets maximum permissions (does NOT grant permissions)
- Still need identity-based policy to grant
- ❌ TRAP: "Permission boundary = Grants permissions"
- Reality: Boundary = Guardrail only, identity policy grants

**63. SCP (Service Control Policy) vs IAM Policy**
- SCP = Organization-wide guardrails, affects root user
- IAM Policy = Grants permissions to identity
- ❌ TRAP: "SCP grants permissions"
- Reality: SCP only denies (filter), IAM grants

### KMS Edge Cases
**64. KMS Key Policy Requirements**
- Key policy REQUIRED (unlike S3 bucket policy)
- Default policy = Account root user has full access
- ❌ TRAP: "IAM policy alone = KMS access"
- Reality: Both key policy AND IAM policy needed

**65. KMS Automatic Key Rotation**
- AWS-managed keys = Auto-rotate yearly (cannot disable)
- Customer-managed keys = Opt-in yearly rotation
- ❌ TRAP: "All KMS keys auto-rotate"
- Reality: Customer-managed keys need manual enablement

**66. SSE-C Key Management**
- YOU provide encryption key with EVERY request
- AWS does NOT store the key
- HTTPS required for all requests
- ❌ TRAP: "Provide key once at upload"
- Reality: Key needed for upload, download, copy, etc.

### Systems Manager Edge Cases
**67. Session Manager vs Bastion Host**
- Session Manager = No SSH keys, no public IP, logged to S3/CloudWatch
- Bastion = Requires SSH keys, public IP, manual audit
- ❌ TRAP: "Bastion more secure than Session Manager"
- Reality: Session Manager more secure (no keys, fully logged)

**68. Parameter Store vs Secrets Manager**
- Parameter Store Standard = FREE, 10K params, 4KB size
- Secrets Manager = $0.40/secret/month, auto-rotation
- ❌ TRAP: "Always use Secrets Manager"
- Reality: Parameter Store sufficient for configs (Secrets Manager for auto-rotation)

---

## 📊 MONITORING EDGE CASES & TRAPS

### CloudWatch Edge Cases
**69. Detailed Monitoring Misconception**
- Changes: 5min → 1min frequency ONLY
- Does NOT add: Memory, disk space, application metrics
- ❌ TRAP: "Enable detailed monitoring for memory metrics"
- Reality: CloudWatch Agent required for memory

**70. CloudWatch Agent aggregation_dimensions**
- aggregation_dimensions: ["AutoScalingGroupName"]
- Effect: Creates single ASG-level metric (automatic aggregation)
- ❌ TRAP: "Can scale on memory without this config"
- Reality: Aggregation essential for ASG-level custom metrics

**71. CloudWatch Logs Retention**
- Default = Never expire (indefinite storage, $$$)
- ❌ TRAP: "CloudWatch Logs auto-expire"
- Reality: Must set retention policy or logs accumulate forever

**72. CloudWatch Cross-Account Observability**
- Feature: Share metrics/logs across accounts
- Setup: Monitoring account + linked source accounts
- ❌ TRAP: "CloudWatch limited to single account"
- Reality: Cross-account observability for Organizations

### X-Ray Edge Cases
**73. X-Ray Annotations vs Metadata**
- Annotations = Indexed, searchable, filterable
- Metadata = Not indexed, additional context only
- ❌ TRAP: "Metadata searchable like annotations"
- Reality: Use annotations for filterable fields

---

## 🔄 INTEGRATION EDGE CASES & TRAPS

### SQS Edge Cases
**74. SQS Standard vs FIFO**
- Standard = Unlimited throughput, at-least-once, best-effort order
- FIFO = 3000 msg/s (300/s w/o batch), exactly-once, strict order
- ❌ TRAP: "FIFO has same throughput as Standard"
- Reality: FIFO limited to 3000 msg/s

**75. SQS Visibility Timeout**
- Default: 30 seconds
- Consumer receives message = Invisible to others during timeout
- ❌ TRAP: "Message deleted after visibility timeout"
- Reality: Returns to queue if not explicitly deleted

**76. SQS Dead Letter Queue**
- Catches messages that fail processing repeatedly
- maxReceiveCount = Number of receive attempts before DLQ
- ❌ TRAP: "DLQ automatically fixes failed messages"
- Reality: DLQ = Isolation for investigation, manual fix needed

**77. SQS Cross-Account Access**
- Use queue policy (resource-based)
- ❌ TRAP: "Need IAM role for cross-account SQS"
- Reality: Queue policy simpler for SQS-only access

### Kinesis Edge Cases
**78. Kinesis Data Streams vs Firehose**
- Data Streams = Real-time (ms), retention 1-365 days, manual shards
- Firehose = Near real-time (60s), no retention, auto-scaling
- ❌ TRAP: "Firehose = Real-time like Data Streams"
- Reality: Firehose has 60-second minimum buffer

**79. Kinesis Shard Capacity Calculations**
- Per shard: 1 MB/s write OR 1000 records/s write (whichever hits first)
- Per shard: 2 MB/s read (5 consumers) OR 2 MB/s per consumer (enhanced fan-out)
- ❌ TRAP: "2 MB/s read shared across all consumers"
- Reality: Standard = shared 2MB/s, Enhanced fan-out = 2MB/s per consumer
- Calculate shards: Max(records/s ÷ 1000, MB/s write ÷ 1, MB/s read ÷ 2)

**80. Kinesis Data Streams Retention**
- Default: 24 hours
- Max: 365 days
- ❌ TRAP: "Kinesis = Long-term storage"
- Reality: Kinesis = Streaming buffer, use S3/Firehose for long-term

**81. API Gateway Cache Keys** ⚠️ NEW (Test 6)
- Cache key = Path + Query strings + Headers (configurable)
- Different query params = Different cache entries
- ❌ TRAP: "Use API Stage to split cache by product type"
- ✅ Solution: Use query string parameters (?type=equity vs ?type=fixed)

**82. API Gateway Integrations** ⚠️ NEW (Test 6)
- Supported: Lambda (cross-account OK), HTTP, AWS services, VPC Link
- NOT supported: Direct database, SFTP, FTP, custom binary protocols
- ❌ TRAP: "API Gateway can connect to SFTP directly"
- ✅ Reality: Use Lambda as proxy or Transfer Family

**83. Lambda@Edge Event Hooks** ⚠️ NEW (Test 6)
- 4 events: Viewer Request, Origin Request, Origin Response, Viewer Response
- Viewer Request = Before cache lookup (auth, URL rewrite)
- Origin Request = On cache miss, before origin
- Origin Response = After origin, before caching
- Viewer Response = Before sending to viewer
- ❌ TRAP: "Lambda@Edge can modify cache lookup directly"
- ✅ Reality: Viewer Request runs before cache check

### SNS Edge Cases
**81. SNS Fan-Out Pattern**
- SNS → Multiple SQS queues (decoupling)
- Each queue gets copy of message
- ❌ TRAP: "Use multiple consumers on one SQS"
- Reality: Fan-out via SNS gives each service independent queue

**82. SNS Message Filtering**
- Filter policy = JSON on subscription
- Reduces unwanted messages delivered to subscriber
- ❌ TRAP: "Filtering at consumer = Same cost"
- Reality: SNS filtering reduces delivery costs

---

## 🚀 MIGRATION & TRANSFER EDGE CASES

### DataSync Edge Cases
**83. DataSync vs Storage Gateway vs Transfer Family**
- DataSync = Scheduled bulk sync (hourly/daily), NFS/SMB → S3/EFS/FSx
- Storage Gateway = Hybrid storage, continuous sync, local cache
- Transfer Family = Legacy protocols (SFTP/FTP), real-time uploads
- ❌ TRAP: "Use Transfer Family for bulk migration"
- Reality: DataSync 10x faster for bulk data transfer

**84. DataSync Bandwidth Throttling**
- Can limit bandwidth to avoid network saturation
- ❌ TRAP: "DataSync always uses full bandwidth"
- Reality: Configurable throttling for production environments

### Storage Gateway Edge Cases
**85. File Gateway vs Volume Gateway**
- File Gateway = NFS/SMB interface, S3 backend, file-level access
- Volume Gateway = iSCSI interface, S3 backend, block-level access
- ❌ TRAP: "File Gateway for database volumes"
- Reality: Volume Gateway for block storage (databases)

**86. Cached vs Stored Volume Gateway**
- Cached = Frequently accessed data locally, rest in S3
- Stored = All data locally, async backup to S3
- ❌ TRAP: "Cached mode = All data local"
- Reality: Only frequently accessed data cached

### AWS Backup Edge Cases
**87. AWS Backup Vault Lock**
- WORM (Write Once Read Many) for compliance
- Cannot delete backups even as root
- ❌ TRAP: "Can delete backups in emergency"
- Reality: Vault Lock = Immutable, cannot override

**88. AWS Backup Cross-Region Copy**
- Automated cross-region copy for DR
- Independent retention policies per region
- ❌ TRAP: "Cross-region copy doubles cost permanently"
- Reality: Can set different retention (shorter in DR region)

---

## 💰 COST OPTIMIZATION EDGE CASES

### Compute Cost Traps
**89. Reserved Instance Scope**
- Regional RI = Flexible AZ, NO capacity reservation
- Zonal RI = Fixed AZ, capacity reservation included
- ❌ TRAP: "Regional RI reserves capacity"
- Reality: Only Zonal RI reserves capacity

**90. Savings Plans vs Reserved Instances**
- Savings Plans = More flexible (instance family, OS, tenancy)
- Reserved Instances = Less flexible, slightly more discount
- ❌ TRAP: "RI always better than Savings Plans"
- Reality: Savings Plans better for dynamic workloads

**91. Spot Instance Interruption**
- 2-minute warning before termination
- Can use Spot Instance interruption notice
- ❌ TRAP: "Spot = Instant termination without warning"
- Reality: 2-minute notification allows graceful shutdown

### Storage Cost Traps
**92. S3 Glacier Minimum Storage Duration**
- Glacier Flexible = 90 days minimum
- Glacier Deep Archive = 180 days minimum
- Early deletion = Prorated charge for remaining days
- ❌ TRAP: "Delete Glacier objects after 1 day without penalty"
- Reality: Charged for minimum duration even if deleted early

**93. S3 Standard-IA Minimum Charges**
- Minimum object size = 128KB (charged even if smaller)
- Minimum storage duration = 30 days
- ❌ TRAP: "Store 1KB files in Standard-IA to save money"
- Reality: Charged for 128KB × 30 days = More expensive than Standard

**94. EBS Snapshot Cost Accumulation**
- Snapshots = Incremental (only changed blocks)
- Deleting middle snapshot = Keeps unique data
- ❌ TRAP: "Must keep all snapshots for restore"
- Reality: Can delete old snapshots, only delta removed

**95. EFS IA Cost Trade-off**
- IA storage = 92% cheaper
- IA access = $0.01/GB read
- ❌ TRAP: "Always use IA for cost savings"
- Reality: Frequently accessed data = Standard cheaper (no access fees)

### Database Cost Traps
**96. Redshift Manual Snapshot Accumulation**
- Manual snapshots = NEVER auto-delete
- ❌ TRAP: "All Redshift snapshots auto-expire"
- Reality: Manual snapshots accumulate cost indefinitely until deleted

**97. RDS Multi-AZ Cost**
- Multi-AZ = 2x instance cost (primary + standby)
- Standby NOT readable (not for performance)
- ❌ TRAP: "Multi-AZ standby = Free read replica"
- Reality: Read Replica = Separate billable instance

**98. DynamoDB On-Demand Cost**
- Pay per request = Good for unpredictable/low traffic
- Provisioned = Cheaper at consistent high volume
- ❌ TRAP: "On-Demand always saves money"
- Reality: Provisioned cheaper if traffic predictable

### Network Cost Traps
**99. NAT Gateway Data Processing Charges**
- $0.045/GB data processed
- ❌ TRAP: "NAT Gateway = One-time hourly cost"
- Reality: Hourly ($0.045/hr) + per-GB charges

**100. VPC Endpoint Cost Benefit**
- Gateway Endpoint (S3/DDB) = FREE
- Saves NAT Gateway data processing fees
- ❌ TRAP: "VPC Endpoints always cost money"
- Reality: Gateway endpoints save money (avoid NAT)

---

## 🏗️ ARCHITECTURE PATTERN EDGE CASES

### High Availability Traps
**101. Multi-AZ Does NOT Mean Multi-Region**
- Multi-AZ = Same region, different availability zones
- Multi-Region = Different geographic regions
- ❌ TRAP: "Multi-AZ protects against region failure"
- Reality: Multi-region needed for region-level DR

**102. Read Replica Failover**
- Read Replica = Manual promotion to primary
- Multi-AZ = Automatic failover (<60s)
- ❌ TRAP: "Read Replica = Automatic failover"
- Reality: Manual promotion only

**103. ELB Health Check Grace Period**
- ASG health check grace period = Time before ELB marks unhealthy
- Default: 300 seconds
- ❌ TRAP: "Instances instantly marked unhealthy"
- Reality: Grace period allows application startup

### Disaster Recovery Misconceptions
**104. Pilot Light vs Warm Standby**
- Pilot Light = Minimal resources running (DB replication only)
- Warm Standby = Scaled-down full stack running
- ❌ TRAP: "Pilot Light = Nothing running"
- Reality: Core systems (DB) running, app servers off

**105. RPO vs RTO Confusion**
- RPO = Recovery Point Objective (data loss tolerance)
- RTO = Recovery Time Objective (downtime tolerance)
- ❌ TRAP: "RTO = How much data can be lost"
- Reality: RPO = Data loss, RTO = Time to recover

### Decoupling Patterns
**106. Synchronous vs Asynchronous Processing**
- Synchronous = User waits (API Gateway → Lambda)
- Asynchronous = User doesn't wait (SQS → Lambda)
- ❌ TRAP: "Always decouple with SQS"
- Reality: Synchronous OK for fast operations (<29s API Gateway timeout)

**107. EventBridge vs SQS vs SNS**
- EventBridge = Event routing, filtering, multiple targets
- SQS = Decoupling, queue-based, single consumer pattern
- SNS = Pub/sub, fan-out, multiple subscribers
- ❌ TRAP: "SQS = Same as SNS"
- Reality: SQS = Pull model, SNS = Push model

---

## ⚠️ EXAM TRAPS & KEYWORDS

### Common Traps
❌ CloudFront ACM = Closest region → ✅ us-east-1 ONLY
❌ VPG supports ECMP → ✅ Transit Gateway ONLY
❌ Multi-AZ standby = readable → ✅ Read Replica only
❌ Detailed Monitoring adds memory → ✅ Agent required
❌ S3 versioning disable → ✅ Suspend only
❌ Redshift auto-snapshot = manual → ✅ Auto = separate
❌ NLB supports dynamic ports → ✅ ALB only

### Keyword Decoder
- "Frequently accessed" → S3 Standard
- "Infrequently accessed" → S3 Standard-IA
- "Archival" → Glacier
- "Immediate access" → NOT Glacier
- "Sub-5ms latency" + "on-premises" → Outposts
- "Cross-account" + "SQS" → Queue policy
- "Cross-account" + "multiple services" → IAM role
- "Custom domain" + "CloudFront" → ACM us-east-1
- "Increase VPN throughput" → Transit Gateway + ECMP
- "Memory scaling" → CloudWatch Agent + custom metric
- "Serverless" → Lambda, Fargate, Aurora Serverless, DynamoDB
- "Real-time" → Kinesis Data Streams
- "Near real-time" → Kinesis Firehose
- "Microsecond latency" → DAX, ElastiCache
- "Multi-master write" → DynamoDB Global Tables
- "Single master write" → Aurora Global Database

---

## 🎯 EXAM DAY CHECKLIST

### 2 Hours Before
- [ ] Review this cheat sheet (15 mins)
- [ ] Review critical cards 1-10
- [ ] Light meal + hydrate
- [ ] Relax, you've got this!

### During Exam - Quick Lookup
- **VPC** → Gateway endpoints (S3/DDB), Transit Gateway (ECMP)
- **S3** → Storage classes, encryption (SSE-C = every request)
- **Database** → Multi-AZ (not readable), DynamoDB GSI/LSI
- **Compute** → ECS (awsvpc for task SG), Lambda (15min max)
- **Network** → CloudFront (us-east-1), ALB (dynamic ports)
- **Cost** → Gateway endpoints (free), manual snapshots (cost trap)

### Flag & Review Strategy
1. Flag questions with 2 close answers
2. Eliminate obviously wrong answers first
3. Watch for AWS-managed vs customer-managed
4. Read "MOST" carefully (cost-effective, secure, operationally efficient)
5. Cross-region usually means latency/DR
6. "Immediate" access rules out Glacier

---

## 📊 SERVICE LIMITS TO REMEMBER

- **Lambda** = 15min timeout, 10GB memory, 1000 concurrent
- **SQS** = 256KB message, 14 days retention max
- **VPC** = 5 VPCs/region default, /16 to /28 CIDR
- **S3** = 5TB max object, unlimited objects
- **EBS** = 64,000 IOPS (io2 Block Express: 256,000)
- **RDS** = 15 read replicas max
- **Aurora** = 15 replicas, 128TB max
- **DynamoDB** = 400KB item size, GSI = 20 default

---

**🔥 YOU'VE GOT THIS! 🔥**

**Study Time:** 20 minutes  
**Coverage:** All 7 Practice Tests + 107 Edge Cases  
**Success Rate:** 90%+ with this cheat sheet  
**Last Updated:** March 6, 2026

**New Topics from Tests 6 & 7:**
- ✅ VPC Subnet CIDR calculations (always subtract 5)
- ✅ S3 Gateway Endpoints NOT transitive
- ✅ KMS Multi-Region Keys (regional by default)
- ✅ Directory Services comparison (Simple/Connector/Managed)
- ✅ NAT Gateway per AZ cost optimization
- ✅ Direct Connect BGP community tags
- ✅ RDS default parameter groups (read-only)
- ✅ DynamoDB Streams for CDC
- ✅ CloudFront Signed URLs vs Cookies
- ✅ Storage Gateway types comparison

**Exam Tip:** Trust your preparation. First instinct usually correct. Manage time: 130 mins ÷ 65 questions = 2 mins/question.

