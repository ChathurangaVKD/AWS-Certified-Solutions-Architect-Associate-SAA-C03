# Practice Tests 1-5 - Master Quick Reference

**All 5 Tests Summary - Fast Learning Guide**

---

## Test Scores Overview

| Test | Score | Status | Key Weakness |
|------|-------|--------|--------------|
| Test 1 | 34/65 (52%) | ❌ FAIL | Resilient (42%), High-Perf (47%) |
| Test 2 | 49/65 (75%) | ⚠️ PASS | Secure (56%) |
| Test 3 | 52/65 (80%) | ✅ PASS | Cost-Opt (63%) |
| Test 4 | 49/65 (75%) | ⚠️ PASS | Cost-Opt (60%) |
| Test 5 | 42/65 (65%) | ❌ FAIL | High-Perf (43%) - CATASTROPHIC |

**Pattern:** Inconsistent performance, High-Performing architecture is major weakness

---

## TOP 50 CRITICAL CONCEPTS (Must Know)

### ECS & Containers
1. **ECS Task Definition:** Blueprint (JSON) - image, CPU, memory, ports, env vars, IAM roles
2. **ECS Dynamic Port Mapping:** Requires ALB + awsvpc/bridge network mode
3. **ECS on Outposts:** On-premises AWS, vs Local Zones (low latency to metros)

### S3 Storage & Performance
4. **S3 Standard-IA:** 30-day minimum storage charge (even if deleted earlier)
5. **S3 Multipart Upload:** Use for >100MB files, required for >5GB
6. **S3 Transfer Acceleration:** Use .s3-accelerate.amazonaws.com endpoint (50-500% faster)
7. **S3 Byte-Range Fetches:** Parallel downloads, resume on failure
8. **S3 Performance:** 3500 PUT/s, 5500 GET/s per prefix
9. **S3 Server Access Logging:** Must enable manually, logs to target bucket
10. **S3 Pre-Signed URLs:** Temporary access to private objects (configurable expiry)
11. **S3 Lifecycle Transitions:** Min 30 days before IA/Glacier, cannot transition OUT of Glacier without restore
12. **S3 Cross-Region Replication:** Versioning required both sides, new objects only
13. **S3 Requester Pays:** Requester pays transfer/requests, owner pays storage
14. **S3 Block Public Access:** 4 settings (account + bucket level)
15. **S3 Bucket Keys (SSE-KMS):** Reduce KMS calls by 99%, lower costs
16. **S3 Object Lock:** Compliance (cannot delete), Governance (can bypass with permission)

### S3 Storage Classes
17. **Glacier Retrieval:** Expedited (1-5m/$$$), Standard (3-5h/$$), Bulk (5-12h/$)
18. **Glacier Deep Archive:** 12h (standard) or 48h (bulk) retrieval
19. **Intelligent-Tiering:** Auto-moves between tiers, no retrieval fees, small monitoring fee
20. **Storage Cost Order:** Deep Archive < Glacier < Intelligent < One Zone-IA < Standard-IA < Standard

### RDS & Databases
21. **RDS Multi-AZ:** Sync replication, auto failover (1-2 min), HA (same region)
22. **RDS Read Replicas:** Async replication, read scaling, can be cross-region
23. **RDS IAM Authentication:** Token-based (15 min), no passwords, MySQL/PostgreSQL/Aurora
24. **RDS Storage Auto Scaling:** Auto-increase when <10% free space
25. **RDS Blue/Green:** Test changes on clone, 1-min switchover downtime
26. **Aurora Global Database:** <1s replication lag, <1 min failover, up to 5 secondary regions
27. **Aurora Serverless:** Auto-scales capacity (ACUs), intermittent workloads
28. **Aurora Read Replica Lag:** Check ReplicaLag metric, add more replicas

### DynamoDB
29. **DynamoDB Auto Scaling:** Target 70% utilization, CloudWatch triggers
30. **DynamoDB DAX:** In-memory cache (microseconds), DynamoDB-only, drop-in compatible
31. **DynamoDB Global Tables:** Multi-region, multi-active, last writer wins

### CloudWatch & Monitoring
32. **CloudWatch Agent:** Required for memory, disk space (not default metrics)
33. **CloudWatch Agent aggregation_dimensions:** Define metric dimensions for aggregation
34. **CloudWatch Cross-Account:** Share metrics across accounts for central monitoring
35. **CloudWatch Logs Retention:** Indefinite by default (not 7 days)
36. **Default EC2 Metrics:** CPU, Network In/Out, Disk Read/Writes (no memory)

### VPC & Networking
37. **VPC Peering DNS:** Must enable DNS resolution + hostnames in BOTH VPCs
38. **VPC Flow Logs:** Capture ALL traffic (accepted + rejected), VPC/Subnet/ENI level
39. **VPC Endpoint Gateway:** S3 + DynamoDB only, free, route table entry
40. **VPC Endpoint Interface:** Most AWS services, ENI with private IP, $0.01/hour
41. **Transit Gateway:** Hub-spoke, 1000s VPCs, transitive routing (use when >10 VPCs)
42. **Security Group:** Stateful, instance level, allow rules only
43. **NACL:** Stateless, subnet level, allow + deny rules, numbered order

### CloudFront & Global
44. **CloudFront + ACM:** Certificate MUST be in us-east-1 (N. Virginia) - NO EXCEPTIONS
45. **CloudFront Origin Failover:** Origin groups with primary + secondary
46. **CloudFront OAI:** Access private S3 without making bucket public
47. **CloudFront Cache Behaviors:** Path-based routing (/api/*, /images/*), priority order
48. **CloudFront Signed URLs:** Single file access
49. **CloudFront Signed Cookies:** Multiple files, don't change URLs
50. **CloudFront Custom Error Pages:** Custom HTML for 4xx/5xx errors
51. **CloudFront Cache Invalidation:** First 1000 paths free/month, then $0.005/path
52. **Global Accelerator:** 2 static anycast IPs, TCP/UDP, non-HTTP, instant failover
53. **Global Accelerator vs CloudFront:** GA = TCP/UDP/static IP, CF = HTTP/cache

### Route 53
54. **Route 53 Simple:** One resource
55. **Route 53 Weighted:** % traffic split, A/B testing
56. **Route 53 Latency:** Route to lowest latency region
57. **Route 53 Failover:** Primary/secondary with health checks
58. **Route 53 Geolocation:** Route by user's country/continent
59. **Route 53 Geoproximity:** Route by distance + bias (-99 to +99)
60. **Route 53 Health Checks:** Endpoint, Calculated, CloudWatch alarm types

### Lambda
61. **Lambda Environment Variables:** Can enable KMS encryption
62. **Lambda@Edge:** Full Lambda, all hooks, Node.js/Python, complex logic
63. **CloudFront Functions:** Lightweight, viewer only, JavaScript, <1ms
64. **Lambda Versions:** Immutable snapshots ($LATEST = mutable)
65. **Lambda Aliases:** Pointer to versions, weighted traffic splitting (blue/green)
66. **Lambda Provisioned Concurrency:** Pre-warmed (no cold starts), pay even if unused

### Auto Scaling
67. **Auto Scaling Custom Metrics:** Need CloudWatch agent (memory not default)
68. **Auto Scaling Cooldown:** 5 min default, prevents rapid scaling
69. **Auto Scaling Target Tracking:** Maintain metric at target value
70. **Auto Scaling Step Scaling:** Different actions for different thresholds

### ELB (Load Balancers)
71. **ALB Path-Based Routing:** Route by URL path, query strings, headers
72. **ALB + Cognito:** Offload authentication to ALB
73. **ALB Dynamic Port Mapping:** For ECS containers

### EBS & Instance Store
74. **EBS Persistence:** Persists independently, can detach/attach
75. **Instance Store:** Lost on stop/terminate/host failure
76. **gp3:** 3000 IOPS base, 125 MB/s base, tune independently, cheapest high-perf
77. **io2:** 64,000 IOPS, 99.999% durability, most expensive
78. **EBS IOPS vs Throughput:** IOPS = small blocks, Throughput = large sequential

### EC2
79. **EC2 Placement Group - Cluster:** Low latency (10 Gbps), single AZ, HPC
80. **EC2 Placement Group - Spread:** Max 7 per AZ, isolated, critical apps
81. **EC2 Placement Group - Partition:** Up to 7 partitions/AZ, big data (Hadoop/Kafka)
82. **EC2 Instance Metadata:** http://169.254.169.254/latest/meta-data/
83. **EC2 Public IP:** Changes on stop/start (use Elastic IP for static)
84. **ENA:** Elastic Network Adapter (up to 100 Gbps)
85. **EFA:** Elastic Fabric Adapter (HPC, MPI, inter-node)
86. **EC2 Instance Types:**
   - **C5/C6:** Compute-optimized (high CPU, batch, gaming)
   - **M5:** General purpose (balanced)
   - **R5:** Memory-optimized (databases, cache)
   - **T3:** Burstable (variable workloads, cheap)

### EC2 Pricing
87. **Standard RI:** 72% discount, can't change type, 1-3 years
88. **Convertible RI:** 54% discount, can change instance type
89. **Regional RI:** Flexible across AZs + sizes (within family)
90. **Zonal RI:** Capacity reservation in specific AZ
91. **Savings Plans:** $/hour commitment, more flexible than RI
92. **Spot Instances:** Up to 90% discount, 2-min interruption notice

### ElastiCache
93. **Redis:** Persistence, replication, Multi-AZ, pub/sub, complex types, sorted sets
94. **Memcached:** Simple, multi-threaded, no persistence, horizontal scale
95. **Redis Multi-AZ:** Auto-failover to replica (<2 min)
96. **ElastiCache Cluster Mode Enabled:** Multiple shards, horizontal scaling

### EFS
97. **EFS Performance - General Purpose:** Low latency, web/CMS
98. **EFS Performance - Max I/O:** Higher latency, big data
99. **EFS Lifecycle:** Move to IA after 7/14/30/60/90 days (92% savings)

### FSx
100. **FSx for Lustre:** HPC, ML, S3 integration, data repository tasks, 100s GB/s
101. **FSx for Windows:** SMB, AD integration, Multi-AZ, DFS, VSS
102. **FSx Use Cases:** Windows = FSx Windows, Linux = EFS, HPC = FSx Lustre

### Kinesis
103. **Kinesis Data Streams:** 1 day default retention, up to 365 days
104. **Kinesis Video Streams:** Video ingestion from cameras/devices, Rekognition/SageMaker

### Analytics
105. **QuickSight:** BI dashboards, SPICE (in-memory), auto-scaling
106. **Glue Crawler:** Auto-discover schemas, populate Data Catalog
107. **Athena:** Query S3 with SQL, uses Glue Data Catalog
108. **Data Pipeline:** S3 → Glue → Athena → QuickSight

### Security Services
109. **KMS Key Rotation:** Automatic annual rotation (AWS managed keys)
110. **KMS Multi-Region Keys:** Same key ID/material across regions, per-region policies
111. **SSE-S3:** AWS manages everything
112. **SSE-KMS:** AWS KMS manages keys, audit trail
113. **SSE-C:** You manage keys, provide with EVERY request
114. **GuardDuty:** Threat detection (CloudTrail, VPC Flow, DNS logs)
115. **AWS Config:** Compliance monitoring, auto-remediation with SSM
116. **Security Hub:** Central security findings from multiple services
117. **Secrets Manager:** Auto-rotation, cross-region replication, versioning
118. **SSM Parameter Store:** Free, no auto-rotation, hierarchical, simpler
119. **Systems Manager Session Manager:** Browser SSH, no keys, IAM-based, logged
120. **WAF Rate-Based Rules:** Block IPs exceeding threshold (5-min window)
121. **WAF Geo-Blocking:** Block/allow by country

### IAM & Cognito
122. **IAM Policy Evaluation:** Explicit DENY always wins → Explicit ALLOW → Implicit DENY
123. **IAM Permission Boundaries:** Max permissions an entity can have
124. **Cognito User Pools:** User directory, authentication
125. **Cognito Identity Pools:** Grant AWS credentials, authorization

### ACM & Certificates
126. **ACM:** Free SSL/TLS, auto-renewal for AWS services
127. **ACM for CloudFront:** MUST be in us-east-1

### Elastic Beanstalk
128. **All at Once:** All instances updated (downtime)
129. **Rolling:** Update in batches (reduced capacity)
130. **Rolling with Additional:** Launch new batch first (maintain capacity)
131. **Immutable:** Full new instances, safest, costly
132. **Blue/Green:** Separate environment, instant rollback

### Direct Connect & VPN
133. **Direct Connect + VPN:** DC primary, VPN backup/failover, BGP routing

### Cost Management
134. **Cost Explorer:** Visualize costs, forecasting, RI recommendations
135. **Cost Allocation Tags:** Track costs by project/team/environment

### API Gateway
136. **API Gateway Throttling:** 10,000 RPS steady, 5,000 burst, returns 429

---

## DECISION TREES (Quick Reference)

### When to Use What?

**Caching:**
- Need persistence/HA/complex types → **Redis**
- Simple cache, multi-core → **Memcached**
- DynamoDB cache → **DAX**

**Storage:**
- Windows file share → **FSx for Windows**
- Linux shared file system → **EFS**
- HPC/ML high performance → **FSx for Lustre**
- Object storage → **S3**

**Global Services:**
- HTTP/HTTPS + caching → **CloudFront**
- Static IPs, TCP/UDP, non-HTTP → **Global Accelerator**

**VPC Connectivity:**
- S3 or DynamoDB → **VPC Endpoint Gateway** (free)
- Other AWS services → **VPC Endpoint Interface** ($)
- >10 VPCs → **Transit Gateway**
- Simple 1-to-1 → **VPC Peering**

**Database:**
- HA same region → **RDS Multi-AZ**
- Read scaling → **RDS Read Replicas**
- Global low latency → **Aurora Global Database**
- Intermittent workloads → **Aurora Serverless**
- NoSQL → **DynamoDB**

**Load Balancer Features:**
- Path-based routing → **ALB**
- ECS dynamic ports → **ALB**
- Static IP → **NLB**
- TCP/UDP → **NLB**

**Secrets:**
- Auto-rotation needed → **Secrets Manager**
- Simple config values → **SSM Parameter Store**

**Video:**
- Ingest from devices → **Kinesis Video Streams**
- Video analytics → **Rekognition + Kinesis Video**

**Analytics:**
- BI dashboards → **QuickSight**
- Query S3 → **Athena**
- Schema discovery → **Glue Crawler**
- ETL jobs → **Glue Jobs**

---

## COMMON MISTAKES TO AVOID

1. ❌ **CloudFront certs in wrong region** → ✅ MUST be us-east-1
2. ❌ **Memory is default metric** → ✅ Need CloudWatch agent
3. ❌ **Bucket default changes existing objects** → ✅ Only affects new uploads
4. ❌ **Can transition out of Glacier directly** → ✅ Must restore first
5. ❌ **Read replicas for HA** → ✅ Multi-AZ for HA, replicas for scaling
6. ❌ **VPC peering auto DNS** → ✅ Must enable DNS settings in BOTH VPCs
7. ❌ **SSE-C = AWS manages keys** → ✅ YOU manage keys, provide every request
8. ❌ **Instance store persists** → ✅ Lost on stop/terminate
9. ❌ **CloudWatch logs expire in 7 days** → ✅ Indefinite by default
10. ❌ **IAM allow overrides deny** → ✅ Deny ALWAYS wins

---

## MEMORIZATION CHECKLIST

### Must Know Numbers
- [ ] S3 IA minimum: **30 days**
- [ ] Glacier retrieval: **Expedited 1-5m, Standard 3-5h, Bulk 5-12h**
- [ ] Aurora Global replication: **<1 second**
- [ ] RDS Multi-AZ failover: **1-2 minutes**
- [ ] Auto Scaling cooldown: **5 minutes**
- [ ] IAM token validity: **15 minutes**
- [ ] Lambda@Edge max: **30 seconds**
- [ ] CloudFront Functions: **<1 millisecond**
- [ ] Kinesis retention: **1-365 days**
- [ ] API Gateway limits: **10,000 RPS steady, 5,000 burst**

### Must Know Regions
- [ ] CloudFront ACM certs: **us-east-1 ONLY**
- [ ] Global Accelerator: **Global (anycast IPs)**

### Must Know Service Limits
- [ ] VPC peering: **125 per VPC**
- [ ] Spread placement: **7 instances per AZ**
- [ ] Partition placement: **7 partitions per AZ**
- [ ] S3 multipart: **10,000 parts max**
- [ ] EBS io2 IOPS: **64,000 max**

---

## FINAL EXAM TIPS

### Before Exam
1. Review this entire document
2. Focus on weak domains (High-Performing, Cost-Optimized)
3. Practice decision trees (when to use what service)
4. Memorize numbers and limits

### During Exam
1. Flag uncertain questions (come back later)
2. Eliminate obviously wrong answers first
3. Look for keywords: "lowest cost" (cost-optimized), "highest performance", "most secure"
4. Watch for trick questions (e.g., "can't transition out of Glacier")

### Time Management
- 130 minutes / 65 questions = **2 minutes per question**
- Flag and move on if >2 minutes
- Reserve 20-30 minutes for review

### Common Trap Answers
- Services that don't exist or are wrong region
- Solutions that work but aren't optimal (cost/performance)
- Missing required configurations (e.g., DNS for VPC peering)

---

## Study Priority for Next Attempt

### 🔴 CRITICAL (Most Failures)
1. **High-Performing Architectures** - CloudWatch, ECS, S3 perf, caching, analytics
2. **Cost-Optimized Architectures** - Storage classes, RIs/Savings Plans, Glacier

### ⚠️ REVIEW (Some Failures)
3. **Resilient Architectures** - FSx variants, Auto Scaling, CloudFront, Kinesis
4. **Secure Architectures** - KMS, IAM, S3 security, VPC security

### ✅ MAINTAIN (Generally Strong)
5. Keep reviewing all domains - consistency is key

---

## Quick Daily Review (15 minutes)
- Day 1: S3 (storage classes, performance, security)
- Day 2: RDS/Aurora (Multi-AZ, replicas, Global DB)
- Day 3: VPC (peering, endpoints, security)
- Day 4: CloudFront/Global Accelerator/Route 53
- Day 5: ECS/Lambda/Elastic Beanstalk
- Day 6: CloudWatch/monitoring/Auto Scaling
- Day 7: Cost optimization (RIs, Savings Plans, storage)
- Repeat cycle

**Good luck! You've got this! 🚀**

