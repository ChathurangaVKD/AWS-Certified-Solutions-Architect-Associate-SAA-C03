# Quiz Remediation Flashcards - SAA-C03
## Based on Quiz Attempt Report (March 2, 2026)

> **Your Performance Summary:**
> - **Total Score:** 42/65 (64.62%)
> - **Incorrect Questions:** 23
> - **Need to Review:** Focus on High-Performing Architectures (13 incorrect) and Resilient Architectures (6 incorrect)

---

## 🎯 Design High-Performing Architectures (13 Incorrect)

### Q: CloudWatch Agent - Custom Metrics & Aggregation
**Question:** How to capture custom application metrics from EC2 instances and aggregate them at the Auto Scaling group level?

**❌ Wrong Answer:** Use detailed monitoring (only provides standard EC2 metrics)

**✅ Correct Answer:** Install unified CloudWatch agent and use `aggregation_dimensions` parameter

**Key Concepts:**
```yaml
CloudWatch Agent Features:
  Custom Metrics:
    - Application-level metrics
    - Memory utilization
    - Disk space usage
    - Process metrics
  
  Aggregation Dimensions:
    - Groups metrics by ASG name
    - {AutoScalingGroupName} dimension
    - Maintains instance-level detail
    - No extra API calls needed

Default EC2 Metrics (NO Agent):
  ✅ CPU Utilization
  ✅ Network In/Out
  ✅ Disk Read/Write
  ✅ Status Checks
  ❌ Memory (need agent)
  ❌ Application metrics (need agent)
```

**Memory Aid:** "Custom App → CloudWatch Agent + aggregation_dimensions = ASG-level view"

---

### Q: ECS Deployment - Low Latency from On-Premises
**Question:** Deploy containerized apps on ECS with lowest latency from on-premises network?

**❌ Wrong Answer:** ECS Fargate on AWS Outposts (Fargate not supported on Outposts)

**✅ Correct Answer:** ECS EC2 launch type on AWS Outposts

**Key Concepts:**
```yaml
AWS Outposts:
  - AWS infrastructure on your premises
  - Same AZs, APIs, tools
  - Lowest latency (local network)
  - Fully managed by AWS

ECS Launch Types on Outposts:
  ✅ ECS EC2 Launch Type
    - Full control over instances
    - Consistent CPU/memory
    - Runs on Outpost racks
  
  ❌ ECS Fargate
    - NOT available on Outposts
    - Only in AWS Regions

Local Zones vs Outposts:
  Local Zones:
    - Metro-adjacent AWS extensions
    - Still off-premises
    - Lower latency than Region
  
  Outposts:
    - On your premises
    - Lowest possible latency
    - Connected to AWS Region
```

**Memory Aid:** "On-prem + Lowest Latency = Outposts. ECS EC2 (not Fargate) on Outposts"

---

### Q: Amazon Redshift - Performance Monitoring
**Question:** Where to analyze query performance and TLS handshake times for Network Load Balancer at petabyte scale?

**❌ Wrong Answer:** CloudTrail (tracks API calls, not query performance)

**✅ Correct Answer:** Redshift console with custom queries on system tables

**Key Concepts:**
```yaml
Redshift Performance Monitoring:
  Redshift Console:
    ✅ Query Monitoring Rules (QMR)
    ✅ WLM queue stats
    ✅ System tables (STL/STV)
    ✅ Cluster performance metrics
    ✅ Minutely CloudWatch metrics
  
  System Tables for Analysis:
    - STL_QUERY: Query execution details
    - STL_WLM_QUERY: Workload management
    - STV_RECENTS: Recent queries
    - STL_SCAN: Table scan details

Wrong Services:
  CloudWatch: ❌ Cluster metrics only, no query-level details
  Trusted Advisor: ❌ Best practices, not performance
  CloudTrail: ❌ API audit, not SQL workload
```

**Memory Aid:** "Redshift Query Performance → Redshift Console + System Tables"

---

### Q: AWS Global Accelerator - IoT Device Ingestion
**Question:** How to provide static IPs for IoT devices connecting to AWS (avoid DNS caching issues)?

**❌ Wrong Answer:** Route 53 with PrivateLink (Route 53 has no PrivateLink endpoint)

**✅ Correct Answer:** AWS Global Accelerator (provides 2 anycast static IPs)

**Key Concepts:**
```yaml
AWS Global Accelerator:
  Features:
    - 2 static anycast IPv4 addresses
    - Global edge network routing
    - Automatic failover
    - No DNS caching issues
    - Health-based traffic steering
  
  Use Cases:
    ✅ IoT devices with static IPs
    ✅ Gaming applications
    ✅ VoIP services
    ✅ Global applications

Route 53 Limitations:
  ❌ No PrivateLink endpoint
  ❌ DNS caching on devices
  ❌ TTL propagation delays
  ❌ No static IP solution

Comparison:
  Route 53:
    - DNS-based routing
    - Domain names
    - Cached by clients
  
  Global Accelerator:
    - Static IP addresses
    - Network layer routing
    - No caching issues
```

**Memory Aid:** "Static IPs + IoT = Global Accelerator (2 anycast IPs)"

---

### Q: EC2 Instance Metadata - AMI ID Retrieval
**Question:** What HTTP path retrieves AMI ID from instance metadata (IMDSv2)?

**❌ Wrong Answer:** Wrong IP address or path

**✅ Correct Answer:** `http://169.254.169.254/latest/meta-data/ami-id`

**Key Concepts:**
```yaml
Instance Metadata Service (IMDS):
  Link-Local Address:
    - 169.254.169.254 (ONLY this IP)
  
  Path Structure:
    /latest/meta-data/    → Instance metadata
    /latest/user-data/    → User data script
    /latest/dynamic/      → Dynamic data (identity doc)
  
  Common Metadata Keys:
    ami-id                → AMI used to launch
    instance-id           → Instance identifier
    instance-type         → Instance type
    local-ipv4            → Private IP
    public-ipv4           → Public IP
    security-groups       → Security group names

IMDSv2 (Session-Oriented):
  1. Get token: PUT /latest/api/token
  2. Use token: Header: X-aws-ec2-metadata-token
  3. Call metadata: GET with token header
```

**Memory Aid:** "169.254.169.254/latest/meta-data/ami-id"

---

### Q: Auto Scaling Cooldown Period
**Question:** Why doesn't Auto Scaling respond to CloudWatch alarm?

**❌ Wrong Answer:** Minimum size = 0 (doesn't block scaling)

**✅ Correct Answer:** Auto Scaling group is in cooldown period

**Key Concepts:**
```yaml
Auto Scaling Cooldown:
  Purpose:
    - Prevent rapid scaling actions
    - Let metrics stabilize
    - Avoid thrashing
  
  Default: 300 seconds (5 minutes)
  
  Behavior:
    ✅ Scale-out completed
    → Cooldown starts
    → Additional alarms suppressed
    → Cooldown ends
    → Scaling resumes

Scaling Policies:
  Simple Scaling:
    - Uses cooldown period
    - One action at a time
  
  Step Scaling:
    - No cooldown (warmup instead)
    - Multiple steps
  
  Target Tracking:
    - No cooldown
    - Continuous adjustment
    - Scale-in cooldown: 300s default

Why Not Other Options:
  Min size = 0: ❌ Doesn't block scale-out
  Desired = 0: ❌ Can still scale up
  Wrong metric: ❌ Alarm already fired
```

**Memory Aid:** "ASG not scaling? Check cooldown period!"

---

### Q: Amazon S3 - Write Performance Optimization
**Question:** How to improve S3 write performance when processing billions of web pages (80% write bottleneck)?

**❌ Wrong Answer:** Migrate to RDS (wrong service for object storage)

**✅ Correct Answers:**
1. Use S3 Transfer Acceleration, Multipart Upload, parallelization, well-designed key prefixes
2. Build DynamoDB/OpenSearch catalog instead of LIST operations

**Key Concepts:**
```yaml
S3 Performance Optimization:
  Write Performance (80% bottleneck):
    ✅ Multipart Upload:
      - Objects > 100 MB
      - Part size: 8-64 MB
      - Parallel uploads
      - Resume capability
    
    ✅ S3 Transfer Acceleration:
      - CloudFront edge locations
      - Long-haul optimization
      - 50-500% faster
    
    ✅ Key Prefix Distribution:
      - 3,500 PUT/s per prefix
      - Random prefixes prevent hotspots
      - Example: hash/uuid/timestamp
    
    ✅ Parallelization:
      - Multiple connections
      - Thread pool
      - Concurrent PUTs

  Read/LIST Optimization (20% bottleneck):
    ❌ Avoid: Repeated LIST operations
    ✅ Use: DynamoDB catalog
    ✅ Use: OpenSearch index
    ✅ Use: S3 Inventory + Athena
    
    Benefits:
      - Predictable latency
      - No bucket traversal
      - Queryable metadata
      - Real-time discovery

S3 Request Rates:
  Per Prefix Limits:
    - 3,500 PUT/COPY/POST/DELETE per second
    - 5,500 GET/HEAD per second
  
  Scale: Add prefixes for more throughput
```

**Memory Aid:** "S3 Write Speed → Multipart + Parallel + Good Prefixes. LIST slow → Catalog!"

---

### Q: Application Load Balancer - Internet Connectivity
**Question:** Why can't clients reach internet-facing ALB?

**❌ Wrong Answer:** Targets in public subnet (irrelevant)

**✅ Correct Answer:** ALB subnet route table lacks route to Internet Gateway

**Key Concepts:**
```yaml
Internet-Facing ALB Requirements:
  ALB Subnets (MUST be public):
    ✅ Route table: 0.0.0.0/0 → IGW
    ✅ At least 2 AZs
    ✅ /27 or larger CIDR
  
  Target Subnets (can be private):
    - Private subnets OK
    - ALB routes to targets via ENI
    - Security groups control access

Public vs Private Subnet:
  Public Subnet:
    ✅ Route to IGW (0.0.0.0/0 → igw-xxx)
    ✅ Resources can get public IP
    ✅ Internet accessible
  
  Private Subnet:
    ❌ No route to IGW
    ✅ Route to NAT Gateway (for outbound)
    ❌ Not directly internet accessible

ALB Networking:
  Scheme: internet-facing
    → Requires: Public subnets
    → Gets: AWS-managed public IPs
    → No: Manual EIP attachment

  Scheme: internal
    → Private subnets OK
    → Private IPs only
```

**Memory Aid:** "Internet ALB → Public subnets → Route to IGW!"

---

### Q: Amazon Athena - Query S3 Data
**Question:** Tool to quickly analyze NLB access logs in S3 (cost-effective, no visualization)?

**❌ Wrong Answer:** QuickSight (adds visualization cost unnecessarily)

**✅ Correct Answer:** Amazon Athena (serverless SQL on S3)

**Key Concepts:**
```yaml
Amazon Athena:
  What:
    - Serverless SQL query service
    - Query data in S3
    - Pay per query (TB scanned)
  
  Use Cases:
    ✅ Ad-hoc log analysis
    ✅ NLB/ALB/CloudFront logs
    ✅ CloudTrail event analysis
    ✅ CSV/JSON/Parquet data
  
  Cost Model:
    - $5 per TB scanned
    - No infrastructure
    - No provisioning
    - Compressed = less cost

Athena vs Other Tools:
  Athena:
    ✅ Serverless
    ✅ SQL interface
    ✅ S3 directly
    ✅ Low ops
  
  QuickSight:
    + Visualization
    + Dashboards
    - Higher cost
    - Not needed for analysis only
  
  S3 Select:
    + Cheaper
    - Single object
    - Limited SQL
  
  Third-party:
    - Egress costs
    - Integration complexity
```

**Memory Aid:** "Quick S3 Analysis → Athena (Serverless SQL)"

---

### Q: Data Scientist Shared Storage
**Question:** Shared, low-latency storage for global data science teams (cost-optimized)?

**❌ Wrong Answer:** EBS Multi-Attach (single AZ, limited instances)

**✅ Correct Answer:** Amazon S3 Standard (shared, scalable, cost-effective)

**Key Concepts:**
```yaml
Storage Options Comparison:
  S3 Standard:
    ✅ Shared globally
    ✅ Multi-AZ automatic
    ✅ Massive scale
    ✅ Low latency (ms)
    ✅ Cost-effective
    ✅ Versioning available
    Use: Shared datasets, data lakes
  
  EFS:
    ✅ POSIX file system
    ✅ Regional sharing
    - Higher $/GB than S3
    Use: Linux workloads, NFS
  
  EBS Multi-Attach:
    ❌ Single AZ only
    ❌ Max 16 instances
    ❌ io1/io2 only
    Use: Clustered apps
  
  Instance Store:
    ❌ Ephemeral
    ❌ Single instance
    ❌ Lost on stop
    Use: Temporary cache

Data Science Pattern:
  Raw Data: S3 Standard
  Processing: EC2/EMR/SageMaker
  Results: S3 → Athena/QuickSight
  Caching: S3 → CloudFront (if static)
```

**Memory Aid:** "Shared + Global + Cost → S3 Standard"

---

### Q: CloudFront Stale Content Issue
**Question:** How to immediately remove stale cached file in CloudFront after origin update?

**❌ Wrong Answer:** Wait 24 hours for TTL expiration (too slow)

**✅ Correct Answer:** Invalidate the object in CloudFront

**Key Concepts:**
```yaml
CloudFront Cache Management:
  Invalidation:
    ✅ Immediate removal
    ✅ Specify paths or wildcards
    ✅ First 1,000/month free
    Cost: $0.005 per path after
    
    Example:
      /config/app.json
      /images/*
      /*
  
  Cache Behaviors:
    - Default TTL: 86400s (24h)
    - Min TTL: 0s
    - Max TTL: 31536000s (1yr)
  
  Alternatives:
    Versioned URLs:
      ✅ app.json?v=2
      ✅ app-v2.json
      ✅ No invalidation needed
      Best practice!
    
    Set TTL = 0:
      ❌ Disables caching
      ❌ High origin load
      Not recommended

Cache-Control Headers:
  Origin Response:
    Cache-Control: max-age=3600
    Cache-Control: no-cache
    Cache-Control: no-store
```

**Memory Aid:** "Stale CloudFront → Invalidate OR Version URLs"

---

### Q: Kinesis Data Streams - Missing Data
**Question:** Why is data missing from S3 when exporting from Kinesis every 2 days?

**❌ Wrong Answer:** S3 can only store data for 1 day (wrong - S3 stores indefinitely)

**✅ Correct Answer:** Default Kinesis retention is 24 hours (data expired before export)

**Key Concepts:**
```yaml
Kinesis Data Streams Retention:
  Default: 24 hours
  Extended: 7 days (standard)
  Long-term: Up to 365 days
  
  Issue:
    Export interval: 48 hours
    Retention: 24 hours
    → Data older than 24h is gone!

Solutions:
  1. Increase Retention:
     - Set to 7 days
     - Or match export interval
  
  2. Export More Frequently:
     - Every 12 hours
     - Every hour
  
  3. Use Kinesis Data Firehose:
     - Automatic S3 delivery
     - No retention concern
     - Built-in transformation

Kinesis vs S3:
  Kinesis:
    - Streaming buffer
    - Time-limited retention
    - Real-time processing
  
  S3:
    - Permanent storage
    - Lifecycle policies
    - No automatic expiry
```

**Memory Aid:** "Kinesis Default = 24h! Export before it expires!"

---

### Q: EC2 Public IP After Stop/Start
**Question:** Why can't developers SSH to EC2 instances after weekend restart?

**❌ Wrong Answer:** EIP changed (EIPs don't change when attached)

**✅ Correct Answer:** Public IPv4 address changed on restart (ephemeral IP)

**Key Concepts:**
```yaml
EC2 IP Addresses:
  Elastic IP (EIP):
    ✅ Static public IPv4
    ✅ Persists across stop/start
    ✅ Associated to instance/ENI
    ✅ Can be remapped
    Cost: Free when in use
  
  Auto-assigned Public IP:
    ❌ Changes on stop/start
    ❌ Released on stop
    ❌ New IP on start
    Use: Temporary workloads
  
  Private IP:
    ✅ Static within VPC
    ✅ Persists stop/start
    ✅ Never changes

Stop/Start Behavior:
  EBS-backed instance:
    ✅ Can stop/start
    ✅ Data persists
    ✅ Private IP same
    ❌ Public IP changes (unless EIP)
  
  Instance-store:
    ❌ Cannot stop
    ✅ Can only terminate
    ❌ Data lost

Solution:
  Attach Elastic IP to instances
  OR use DNS (Route 53) pointing to private IP via VPN/Direct Connect
```

**Memory Aid:** "Stop/Start → Public IP changes! Use EIP for static IP"

---

## 🛡️ Design Resilient Architectures (6 Incorrect)

### Q: Auto Scaling Group - Lifecycle Management
**Question:** How to upgrade one EC2 instance in ASG with zero traffic during maintenance?

**❌ Wrong Answer:** Use lifecycle hooks (for launch/terminate, not in-place maintenance)

**✅ Correct Answer:** Put instance in Standby state, upgrade, return to InService

**Key Concepts:**
```yaml
ASG Lifecycle States:
  Standby:
    ✅ Removes from load balancer
    ✅ Keeps in ASG
    ✅ No traffic routed
    ✅ ASG doesn't replace it
    ✅ Can perform maintenance
    Process:
      1. Put instance in Standby
      2. Update/patch instance
      3. Test changes
      4. Return to InService
  
  Lifecycle Hooks:
    - Launch hook: Before InService
    - Terminate hook: Before termination
    ❌ Not for running instance maintenance

Wrong Approaches:
  Hibernate: ❌ ASG may replace
  Cooldown: ❌ Affects scaling, not traffic
  Detach: ❌ Removes from ASG

ASG Maintenance Pattern:
  Standby → Maintenance → InService
  
  Benefits:
    - Zero downtime
    - No ASG disruption
    - Controlled rollout
```

**Memory Aid:** "ASG Maintenance → Standby (not hooks or cooldown)"

---

### Q: Auto Scaling Cooldown Not Responding
**Question:** ASG with SQS doesn't scale when CloudWatch alarm fires?

**❌ Wrong Answer:** Min size = 0 blocks scaling (doesn't block scale-out)

**✅ Correct Answer:** Auto Scaling group is in cooldown period

**Key Concepts:**
```yaml
Auto Scaling Cooldown:
  Default: 300 seconds (5 minutes)
  
  Behavior:
    ✅ Scale action completes
    → Cooldown timer starts
    → Additional scale actions blocked
    → Timer expires
    → Scaling resumes
  
  Rationale:
    - Let new instances warm up
    - Prevent scaling storms
    - Allow metrics to stabilize

SQS-based Scaling:
  Metric: ApproximateNumberOfMessagesVisible
  Policy: Target tracking on backlog per instance
  
  Cooldown Impact:
    High queue depth
    → Scale out triggered
    → Cooldown starts
    → More messages arrive
    → Alarm fires again
    → BLOCKED by cooldown!

Solutions:
  1. Use target tracking (no cooldown)
  2. Reduce cooldown period
  3. Use step scaling
  4. Adjust scale-out amount

Scaling Policy Types:
  Simple: Uses cooldown
  Step: Uses warmup (no cooldown)
  Target Tracking: No cooldown
```

**Memory Aid:** "ASG + Cooldown = Temporary scaling pause"

---

### Q: ECS Dynamic Port Mapping
**Question:** Which load balancers support ECS dynamic port mapping?

**❌ Wrong Answer:** NLB only (both ALB and NLB support it)

**✅ Correct Answer:** Application Load Balancer or Network Load Balancer

**Key Concepts:**
```yaml
ECS Dynamic Port Mapping:
  Concept:
    - Container port: Fixed (e.g., 8080)
    - Host port: 0 (ephemeral)
    - ECS assigns available port
  
  Benefits:
    ✅ Multiple tasks per host
    ✅ Port conflict avoided
    ✅ Better resource utilization

Load Balancer Support:
  Application Load Balancer (ALB):
    ✅ Dynamic port mapping
    ✅ Target groups
    ✅ Layer 7 routing
    ✅ Path/host-based routing
  
  Network Load Balancer (NLB):
    ✅ Dynamic port mapping
    ✅ Target groups
    ✅ Layer 4 (TCP/UDP)
    ✅ Static IPs
  
  Classic Load Balancer (CLB):
    ❌ No dynamic port mapping
    ❌ One port per instance
    ❌ Legacy

Target Group Registration:
  ECS Service:
    - Registers tasks automatically
    - Uses instance ID + port
    - Health checks per task
```

**Memory Aid:** "ECS Dynamic Ports → ALB or NLB (not CLB)"

---

### Q: Amazon RDS - Read-Heavy Scaling
**Question:** RDS CPU at 100% from read-heavy load. How to scale? (Select THREE)

**❌ Wrong Answer:** Storage Auto Scaling (doesn't add CPU/read capacity)

**✅ Correct Answers:**
1. Add RDS Read Replicas
2. Use ElastiCache
3. Shard across multiple RDS instances

**Key Concepts:**
```yaml
RDS Read Scaling Options:
  1. Read Replicas:
     ✅ Offload read traffic
     ✅ Up to 5 per master (15 for Aurora)
     ✅ Async replication
     ✅ Can promote to master
     Pattern: App → Read replica for reports/analytics
  
  2. ElastiCache:
     ✅ In-memory cache (Redis/Memcached)
     ✅ Sub-millisecond latency
     ✅ Reduce DB queries 90%+
     Patterns:
       - Cache-aside (lazy loading)
       - Write-through
       - Session store
  
  3. Database Sharding:
     ✅ Horizontal partitioning
     ✅ Distribute data/load
     ✅ Independent scaling
     Examples:
       - By customer ID
       - By geographic region
       - By date range

NOT Solutions:
  Storage Auto Scaling:
    ❌ Only increases disk space
    ❌ Doesn't add CPU
    ❌ Doesn't add memory
  
  Multi-AZ:
    ❌ For availability (failover)
    ❌ Standby not for reads
    ❌ Doesn't scale read capacity

Scaling Strategy:
  Stage 1: Read Replicas (easiest)
  Stage 2: Add ElastiCache
  Stage 3: Vertical scaling (larger instance)
  Stage 4: Sharding (complex)
```

**Memory Aid:** "RDS Read Scale → Replicas + Cache + Sharding"

---

### Q: Multi-Region RDS Failover
**Question:** Multi-Region active-passive. US-EAST-1 fails. How to recover?

**❌ Wrong Answer:** Update EIP (wrong - use CNAME for RDS endpoint)

**✅ Correct Answer:** Promote us-west-2 read replica, update CNAME to new endpoint

**Key Concepts:**
```yaml
RDS Cross-Region DR:
  Setup:
    - Primary: us-east-1 (read-write)
    - Replica: us-west-2 (read-only)
    - App uses: CNAME → primary endpoint
  
  Failover Steps:
    1. Promote us-west-2 replica
       → Becomes standalone DB
       → Read-write enabled
    
    2. Update app CNAME
       → Points to us-west-2 endpoint
    
    3. Verify connectivity
    
    4. Resume operations

RDS Endpoint Types:
  Instance Endpoint:
    - AWS-managed DNS
    - Format: dbname.xxx.region.rds.amazonaws.com
    - Cannot modify
  
  Application CNAME:
    ✅ Route 53 record
    ✅ Points to RDS endpoint
    ✅ Easy failover (update CNAME)
    ✅ No app code changes

Multi-AZ vs Cross-Region:
  Multi-AZ:
    - Same region
    - Automatic failover (1-2 min)
    - Synchronous replication
    - Same endpoint
  
  Cross-Region:
    - Different regions
    - Manual promotion
    - Async replication (lag)
    - Different endpoints

Read Replica Promotion:
  - Stops replication
  - Becomes independent DB
  - Can take 5-10 minutes
  - Data lag risk (async)
```

**Memory Aid:** "Region Failover → Promote Replica + Update CNAME"

---

### Q: S3 Versioning for Data Protection
**Question:** How to protect S3 data against accidental deletions and restore when needed?

**❌ Wrong Answer:** Make bucket read-only (blocks normal operations)

**✅ Correct Answer:** Enable S3 versioning

**Key Concepts:**
```yaml
S3 Versioning:
  Features:
    ✅ Keeps all versions of objects
    ✅ Delete marker (not permanent delete)
    ✅ Can restore previous versions
    ✅ Undelete by removing delete marker
    ✅ Protects against overwrites
  
  States:
    - Unversioned (default)
    - Enabled
    - Suspended (cannot be disabled)
  
  Behavior:
    PUT (new): Version ID assigned
    PUT (exists): New version created
    DELETE: Delete marker added
    GET: Returns latest non-deleted version
    GET (version): Returns specific version

Additional Protection:
  MFA Delete:
    ✅ Requires MFA for:
      - Deleting object versions
      - Suspending versioning
    ✅ Extra security layer
  
  Object Lock:
    ✅ WORM (Write-Once-Read-Many)
    ✅ Compliance/Governance mode
    ✅ Time-based retention
    ✅ Legal hold

Versioning + Lifecycle:
  Transition old versions to cheaper storage:
    Current → S3 Standard
    30 days → S3 IA
    90 days → Glacier
  
  Expire old versions:
    Delete after 365 days

NOT Solutions:
  Read-only: ❌ Blocks writes
  SSE-KMS: ❌ Encryption, not recovery
  Lifecycle: ❌ Moves/deletes, doesn't protect
```

**Memory Aid:** "Accidental Deletes → Enable Versioning (+ MFA Delete)"

---

## 🔒 Design Secure Architectures (4 Incorrect)

### Q: AWS CloudHSM Backup Encryption
**Question:** What keys does CloudHSM use for secure backups?

**❌ Wrong Answer:** Uses KMS CMK (CloudHSM has its own key hierarchy)

**✅ Correct Answer:** Ephemeral Backup Key (EBK) encrypts data, Persistent Backup Key (PBK) encrypts EBK, saved to S3 in same region

**Key Concepts:**
```yaml
CloudHSM Backup Process:
  1. Generate EBK (AES-256):
     - Unique per backup
     - Encrypts cluster data
     - Ephemeral (temporary)
  
  2. Generate PBK (AES-256):
     - Long-term key
     - Encrypts the EBK
     - Persistent
  
  3. Store in S3:
     - Same region as cluster
     - Encrypted backup
     - AWS managed

CloudHSM vs KMS:
  CloudHSM:
    ✅ Dedicated hardware
    ✅ FIPS 140-2 Level 3
    ✅ Single-tenant
    ✅ You control keys
    ❌ You manage HA/backup
  
  KMS:
    ✅ Managed service
    ✅ Multi-tenant
    ✅ AWS manages hardware
    ✅ Regional HA automatic
    ❌ FIPS 140-2 Level 2

Backup Location:
  ✅ S3 in same region
  ❌ NOT cross-region by default
  - For DR: Copy to another region manually

Key Hierarchy:
  PBK (Persistent)
    └── EBK (Ephemeral)
        └── Cluster Data
```

**Memory Aid:** "CloudHSM Backup → EBK encrypts data, PBK encrypts EBK → S3 same region"

---

### Q: AWS Organizations - Admin Notifications
**Question:** Service to trigger notifications on Organization admin actions?

**❌ Wrong Answer:** AWS Config (tracks resource config, not all admin actions)

**✅ Correct Answer:** AWS CloudTrail

**Key Concepts:**
```yaml
CloudTrail for Organizations:
  Organization Trail:
    ✅ Logs all member accounts
    ✅ Centralized in master account
    ✅ API call auditing
    ✅ Who, what, when, where
  
  Organization Events:
    - CreateAccount
    - InviteAccountToOrganization
    - RemoveAccountFromOrganization
    - AttachPolicy
    - DetachPolicy
    - UpdatePolicy

Notification Pattern:
  CloudTrail → CloudWatch Logs → Metric Filter → Alarm → SNS
  
  OR:
  
  CloudTrail → EventBridge → Lambda/SNS

Service Comparison:
  CloudTrail:
    ✅ API activity logging
    ✅ Who made API calls
    ✅ Management events
    ✅ Data events (S3, Lambda)
  
  Config:
    ❌ Resource configuration changes
    ❌ Compliance tracking
    ❌ Not all admin actions
  
  CloudWatch Logs:
    ❌ Log storage/analysis
    ❌ Not event source
  
  EventBridge:
    ✅ Event routing
    ✅ Works with CloudTrail
    ❌ Not event source itself
```

**Memory Aid:** "Admin Actions → CloudTrail (not Config)"

---

### Q: Network ACL for DoS Protection
**Question:** How to protect DB subnet from external connection flood (DoS)?

**❌ Wrong Answer:** Security Group with restricted inbound (SGs don't support deny)

**✅ Correct Answer:** Change Network ACL inbound rules to deny access

**Key Concepts:**
```yaml
Network ACL vs Security Group:
  Network ACL:
    ✅ Subnet level
    ✅ Supports DENY rules
    ✅ Stateless (return traffic explicit)
    ✅ Numbered rules (priority)
    ✅ Processes rules in order
    Use: Block specific IPs/CIDRs
  
  Security Group:
    ❌ Instance/ENI level
    ❌ Allow rules ONLY
    ✅ Stateful (return traffic automatic)
    Use: Application access control

DoS Protection Pattern:
  1. Network ACL:
     Rule 10: DENY tcp from 10.0.0.0/8 port 3306
     Rule 100: ALLOW tcp from 172.16.0.0/12 port 3306
     Rule 200: DENY all
  
  2. Security Group:
     ALLOW tcp from sg-app port 3306 (legitimate traffic)

Defense in Depth:
  Layer 1: AWS Shield (DDoS)
  Layer 2: WAF (application layer)
  Layer 3: Network ACL (network layer)
  Layer 4: Security Group (instance layer)

NACL Best Practices:
  - Use explicit deny for known bad actors
  - Keep allow rules specific
  - Default deny at end
  - Use ephemeral port range (1024-65535)
```

**Memory Aid:** "Block IPs → NACL (SGs can't deny)"

---

### Q: EBS Volume - Cross-AZ Migration
**Question:** How to move EBS volume to instance in different AZ?

**❌ Wrong Answer:** Detach and attach to instance in other AZ (EBS is AZ-scoped)

**✅ Correct Answer:** Create snapshot, then create volume from snapshot in other AZ

**Key Concepts:**
```yaml
EBS Volume Scope:
  ❌ AZ-locked: Cannot attach across AZs
  ✅ Region-scoped snapshots
  
  Migration Process:
    1. Create snapshot (any time)
    2. Copy snapshot to other region (if needed)
    3. Create volume from snapshot in target AZ
    4. Attach to instance in target AZ

Snapshot Features:
  ✅ Incremental backups
  ✅ Region-scoped (not AZ)
  ✅ Encrypted snapshots stay encrypted
  ✅ Can change volume type on restore
  ✅ Can increase size on restore
  
  Fast Snapshot Restore (FSR):
    ✅ No lazy-loading wait
    ✅ Instant full performance
    Cost: $0.75 per DSU-month

EBS Multi-Attach:
  Limitations:
    ✅ io1/io2 only
    ❌ Same AZ only
    ❌ Max 16 instances
    - Nitro instances required
    - Cluster-aware file system needed

Cross-Region:
  Snapshot → Copy to region → Volume
  OR: Use EBS direct APIs (async)

Elastic Volumes:
  ✅ Change type (gp2→gp3, etc.)
  ✅ Change size
  ✅ Change IOPS/throughput
  ❌ Cannot change AZ
```

**Memory Aid:** "EBS to other AZ → Snapshot → New volume in target AZ"

---

## 💰 Design Cost-Optimized Architectures (0 Incorrect)

✅ **Perfect Score!** Great job on cost optimization questions!

---

## 📝 Practice Questions Based on Incorrect Answers

### Question 1: CloudWatch Custom Metrics (Design High-Performing)
Your application running on EC2 instances in an Auto Scaling group needs to publish custom business metrics (order processing rate, API latency percentiles) that should be visible both per-instance and aggregated at the ASG level for scaling decisions. How should you configure this?

**A.** Enable detailed monitoring on the ASG and create custom CloudWatch dashboards
**B.** Install CloudWatch agent with `aggregation_dimensions` set to `{AutoScalingGroupName}`
**C.** Use CloudWatch PutMetricData API with dimension `AutoScalingGroupName`
**D.** Configure CloudWatch Logs Insights with aggregation queries

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- CloudWatch agent with `aggregation_dimensions` automatically creates aggregate metrics at ASG level
- Maintains per-instance granularity for drilling down
- No manual aggregation needed in dashboards
- Option C would work but requires more code and doesn't auto-aggregate
- Detailed monitoring (A) only provides standard EC2 metrics, not custom app metrics
- Logs Insights (D) is for log analysis, not real-time metrics
</details>

---

### Question 2: ECS on Outposts (Design High-Performing)
A manufacturing company needs to run containerized edge analytics applications with guaranteed low latency (<10ms) from on-premises factory systems. The solution must integrate with AWS services for management and provide consistent compute resources. Which deployment architecture should they choose?

**A.** Amazon ECS with Fargate in Local Zones
**B.** Amazon ECS with EC2 launch type on AWS Outposts
**C.** Amazon ECS with Fargate on AWS Outposts
**D.** Amazon EKS in a nearby AWS Region with Direct Connect

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- AWS Outposts brings AWS infrastructure to your premises = lowest latency
- ECS EC2 launch type is supported on Outposts, Fargate is not
- EC2 launch type provides consistent, guaranteed compute resources
- Local Zones (A) are still off-premises (metro-adjacent)
- Fargate on Outposts (C) is not available
- Region with Direct Connect (D) has higher latency than on-prem Outposts
</details>

---

### Question 3: Kinesis Data Retention (Design High-Performing)
Your IoT platform ingests sensor data into Kinesis Data Streams. A batch job runs every 3 days to export all data to S3 for compliance. Users report that data from 2+ days ago is consistently missing from exports. What is the most likely cause and solution?

**A.** S3 has a 24-hour retention limit; use S3 Glacier for longer retention
**B.** Kinesis default retention is 24 hours; increase to at least 7 days
**C.** The export job is overwhelming the stream; add more shards
**D.** Cross-region replication is delayed; use same-region export

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- Kinesis default retention: 24 hours
- Export interval: 72 hours (3 days)
- Data older than 24 hours is automatically deleted
- Solution: Increase Kinesis retention to 7 days or export more frequently
- S3 doesn't have automatic retention limits (A is wrong)
- Shard capacity (C) would cause throughput errors, not missing old data
- Region (D) is irrelevant to the retention issue
</details>

---

### Question 4: Auto Scaling Cooldown (Design Resilient)
An Auto Scaling group uses simple scaling policy to scale based on SQS queue depth. CloudWatch alarm fires when queue depth > 100, but the ASG doesn't launch new instances. Current capacity is 2 instances (min=1, max=10, desired=2). What is the most likely cause?

**A.** The scaling policy is configured incorrectly
**B.** The Auto Scaling group is in cooldown period after a recent scaling activity
**C.** The minimum size prevents scaling out
**D.** CloudWatch alarm is in INSUFFICIENT_DATA state

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- Simple scaling policies use cooldown periods (default 300 seconds)
- After any scaling action, cooldown blocks additional actions
- Cooldown lets metrics stabilize and new instances register
- Min size=1, current=2, so scale-out is possible (C is wrong)
- Alarm already fired, so not INSUFFICIENT_DATA (D is wrong)
- Policy likely correct if alarm triggered (A less likely)
- Solution: Use target tracking or step scaling instead of simple scaling
</details>

---

### Question 5: S3 Write Performance (Design High-Performing)
A media processing pipeline writes millions of 50MB video chunks to S3 per hour. Write latency is causing job backlog. Current implementation: Single-threaded sequential PUTs with keys like `videos/YYYY-MM-DD/video001.mp4`. How should you optimize write performance?

**A.** Enable S3 Transfer Acceleration only
**B.** Use multipart upload with parallel parts + randomize key prefixes
**C.** Migrate to EBS volumes for staging, then batch upload to S3
**D.** Enable S3 versioning and lifecycle policies

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- Multipart upload: Parallel upload of parts (8-64 MB each) = higher throughput
- Random prefixes: Distribute load across partitions (avoid hot keys)
- Example: `videos/abc123/YYYY-MM-DD/video001.mp4` (hash prefix)
- S3 scales at 3,500 PUT/s per prefix
- Transfer Acceleration helps for long distances but doesn't solve sequential + hotkey issues
- EBS staging (C) adds complexity and doesn't improve S3 write speed
- Versioning/lifecycle (D) don't affect write performance
</details>

---

### Question 6: CloudTrail for Org Monitoring (Design Secure)
You need to receive email alerts whenever an administrator creates, removes, or modifies accounts in your AWS Organization. Which combination provides this with minimal operational overhead?

**A.** AWS Config → Config Rule → EventBridge → SNS
**B.** CloudTrail (Organization trail) → EventBridge → SNS
**C.** GuardDuty → Findings → SNS
**D.** CloudWatch Logs → Metric Filter → Alarm → SNS

<details>
<summary>Show Answer</summary>

**Correct Answer: B**

**Explanation:**
- CloudTrail logs ALL API actions, including Organizations APIs
- Organization trail: Centralized logging for all member accounts
- EventBridge: Trigger on specific CloudTrail events (CreateAccount, etc.)
- SNS: Send email/SMS notifications
- Config (A) tracks resource configuration, not all API actions
- GuardDuty (C) is for threat detection, not activity monitoring
- CloudWatch Logs (D) can work but requires more setup vs EventBridge
</details>

---

## 🎯 Key Takeaways from This Quiz

### Top 3 Weak Areas:
1. **High-Performing Architectures (56% incorrect)** → Focus on:
   - CloudWatch agent custom metrics and aggregation
   - S3 performance optimization (multipart, prefixes, Transfer Acceleration)
   - Kinesis data retention and streaming patterns
   - ECS deployment models (Fargate vs EC2, Outposts vs Local Zones)

2. **Resilient Architectures (29% incorrect)** → Focus on:
   - Auto Scaling lifecycle management (Standby vs Hooks vs Cooldown)
   - RDS read scaling strategies (replicas, caching, sharding)
   - Multi-region DR patterns (RDS promotion, DNS failover)

3. **Secure Architectures (22% incorrect)** → Focus on:
   - CloudHSM backup encryption (EBK/PBK hierarchy)
   - Network ACLs vs Security Groups (deny rules)
   - EBS cross-AZ migration (snapshots required)

### Study Strategy:
1. **Review incorrect questions** in this flashcard deck daily
2. **Complete hands-on labs** for weak areas (especially ECS, Auto Scaling, S3 performance)
3. **Practice more questions** focused on High-Performing Architectures domain
4. **Revisit core concepts**: Outposts vs Local Zones, CloudWatch agent, Kinesis retention

---

**Next Steps:**
- [ ] Review all 23 flashcards above
- [ ] Complete related practice questions
- [ ] Read AWS documentation for services you missed
- [ ] Take another practice test in 3-5 days
- [ ] Track improvement in weak areas

Good luck with your AWS SAA-C03 preparation! 🚀

