# Practice Test 1 Review - Quick Reference

**Date:** Feb 22, 2026 | **Score:** 34/65 (52%) ❌ FAILED | **Pass:** 72% | **Gap:** Need 13 more

## Domain Scores
| Domain | Score | Status |
|--------|-------|--------|
| Resilient Architectures | 8/19 (42%) | ❌ CRITICAL |
| High-Performing | 8/17 (47%) | ❌ CRITICAL |
| Secure Architectures | 12/19 (63%) | ⚠️ Review |
| Cost-Optimized | 6/10 (60%) | ⚠️ Review |

---

## CRITICAL ERRORS - Must Know

### Q2: ECS Task Definition
- **Wrong:** AWS Service definition  
- **Right:** ECS Task Definition (JSON)
- **Key:** Blueprint for containers: image, CPU, memory, ports, env vars, IAM roles
- **Components:** Container defs, task role, execution role, network mode, launch type

### Q5: S3 Standard-IA Minimum Storage Duration
- **Wrong:** No minimum duration  
- **Right:** 30 days minimum
- **Key:** Charged for full 30 days even if deleted earlier
- **Costs:** $0.01/GB storage + $0.01/GB retrieval + 30-day minimum

### Q7: VPC Peering DNS Resolution
- **Wrong:** Automatic DNS resolution  
- **Right:** Must enable DNS resolution + DNS hostnames in BOTH VPCs
- **Steps:** 1) Create peering 2) Accept 3) Update route tables 4) Enable DNS settings

### Q10: S3 SSE-C (Customer Keys)
- **Wrong:** AWS manages keys  
- **Right:** YOU manage keys, AWS encrypts/decrypts
- **Key:** Must provide key with EVERY request (GET/PUT)
- **vs SSE-S3:** AWS manages everything
- **vs SSE-KMS:** AWS KMS manages keys

### Q12: ECS Dynamic Port Mapping
- **Wrong:** Works with EC2 launch type + bridge mode  
- **Right:** Requires ALB + awsvpc or host network mode
- **ALB:** Routes to dynamic ports automatically
- **NLB/CLB:** Cannot do dynamic port mapping

### Q14: Aurora Read Replica Lag
- **Wrong:** Increase write instance size  
- **Right:** Check replica lag metric, add more replicas
- **Causes:** Heavy write load, slow replica instance, network issues
- **Monitoring:** ReplicaLag metric in CloudWatch

### Q15: CloudFront Origin Failover
- **Wrong:** Multiple distributions  
- **Right:** Origin groups with primary + secondary origins
- **Behavior:** Auto failover on 5xx errors or timeouts
- **Use case:** S3 primary, S3 backup in different region

### Q19: RDS Multi-AZ Automatic Failover
- **Wrong:** Manual intervention required  
- **Right:** Automatic failover (1-2 minutes)
- **Triggers:** AZ failure, instance failure, storage failure, network failure
- **DNS:** CNAME automatically updates to standby

### Q21: EBS vs Instance Store Persistence
- **Wrong:** Instance store persists after stop  
- **Right:** EBS persists, instance store LOST on stop/terminate
- **Instance Store:** Lost on stop, terminate, or host failure
- **EBS:** Persists independently, can detach/attach

### Q24: DynamoDB Auto Scaling
- **Wrong:** Manual capacity adjustment  
- **Right:** Auto scaling based on target utilization
- **Target:** 70% utilization default
- **CloudWatch:** Triggers scaling based on consumed capacity

### Q28: S3 Transfer Acceleration
- **Wrong:** Use standard S3 endpoints  
- **Right:** Use .s3-accelerate.amazonaws.com endpoint
- **How:** Upload to CloudFront edge → AWS backbone network → S3
- **Speed:** 50-500% faster for long distances

### Q31: API Gateway Throttling
- **Wrong:** Requests queued indefinitely  
- **Right:** Returns 429 Too Many Requests
- **Limits:** 10,000 RPS steady, 5,000 burst per account
- **Per method:** Can set custom limits

### Q32: RDS Read Replicas vs Multi-AZ
- **Wrong:** Read replicas for HA  
- **Right:** Read replicas for READ SCALING, Multi-AZ for HA
- **Read Replica:** Async replication, can be cross-region, read-only
- **Multi-AZ:** Sync replication, same region, auto failover

### Q35: Lambda Environment Variables Encryption
- **Wrong:** Automatically encrypted  
- **Right:** Can enable KMS encryption for sensitive data
- **Default:** Encrypted at rest with AWS key
- **KMS:** Use your own key for extra control

### Q37: VPC Flow Logs Capture Level
- **Wrong:** Only accepted traffic  
- **Right:** ALL traffic (accepted + rejected)
- **Levels:** VPC, Subnet, or ENI level
- **Destination:** CloudWatch Logs or S3

### Q39: EC2 Placement Groups
- **3 Types:**
  - **Cluster:** Low latency (10 Gbps), single AZ, HPC
  - **Spread:** Max 7 instances per AZ, critical apps, isolated
  - **Partition:** Up to 7 partitions per AZ, big data (Hadoop, Kafka)

### Q42: CloudWatch Logs Retention
- **Wrong:** 7 days default  
- **Right:** Indefinite (never expire) by default
- **Can set:** 1 day to 10 years, or indefinite
- **Cost:** Charged per GB stored

### Q45: S3 Lifecycle Policy Transitions
- **Rules:**
  - Standard → Standard-IA: Min 30 days
  - Standard → Glacier: Min 30 days
  - Cannot: Glacier → Standard (must restore first)
- **One-Zone IA:** Min 30 days before transition

### Q48: DynamoDB Global Tables
- **Wrong:** Manual replication  
- **Right:** Multi-region, multi-active replication (automatic)
- **Conflicts:** Last writer wins
- **Use case:** Global low-latency reads/writes

### Q52: Kinesis Data Streams Retention
- **Wrong:** 7 days max  
- **Right:** 1 day default, up to 365 days
- **Extended retention:** Additional cost per shard-hour

### Q56: AWS Direct Connect + VPN Backup
- **Setup:** Direct Connect (primary) + VPN (backup/failover)
- **Routing:** BGP failover to VPN if Direct Connect fails
- **Use case:** Hybrid connectivity with HA

### Q58: S3 Server Access Logging
- **Wrong:** Enabled by default  
- **Right:** Must enable manually, logs to target bucket
- **Logs:** Access requests, requester, time, response status
- **vs CloudTrail:** API calls, S3 logging = access logs

### Q61: Aurora Serverless
- **Wrong:** Manual scaling  
- **Right:** Auto scales capacity based on demand
- **ACU:** Aurora Capacity Units (2GB RAM each)
- **Use case:** Intermittent, unpredictable workloads

---

## High-Performing Architecture Errors

### Q3: EBS Volume Types
- **gp3:** 3000 IOPS base, up to 16,000 IOPS, cheapest
- **gp2:** 3 IOPS/GB, burstable to 3000, legacy
- **io2:** 64,000 IOPS, 99.999% durability, expensive
- **io1:** 64,000 IOPS, 99.9% durability
- **Use io2/io1:** When need >16,000 IOPS

### Q6: S3 GET Request Performance
- **Wrong:** Single GET is fastest  
- **Right:** Use CloudFront CDN or S3 Transfer Acceleration
- **CloudFront:** Edge caching, global performance
- **Multipart download:** Use byte-range GETs for large files

### Q17: ElastiCache Redis vs Memcached
- **Redis:** Persistence, replication, Multi-AZ, pub/sub, complex types
- **Memcached:** Simple, multi-threaded, no persistence, horizontal scale
- **Use Redis:** Need persistence, HA, complex data
- **Use Memcached:** Simple cache, multi-core utilization

### Q20: RDS Read Replica Promotion
- **Process:** Promote replica → becomes standalone DB
- **Use case:** Disaster recovery, testing, regional expansion
- **After promotion:** No longer replicates from master

### Q25: Lambda@Edge vs CloudFront Functions
- **Lambda@Edge:** Full Lambda, viewer/origin request/response, Node.js/Python
- **CloudFront Functions:** Lightweight, viewer request/response only, JavaScript
- **Use Lambda@Edge:** Complex logic, network calls
- **Use CF Functions:** Simple transforms, <1ms execution

### Q29: Route 53 Routing Policies
- **Simple:** One resource
- **Weighted:** % traffic split, A/B testing
- **Latency:** Route to lowest latency region
- **Failover:** Primary/secondary, health checks
- **Geolocation:** Route by user location
- **Geoproximity:** Route by geographic distance with bias
- **Multi-value:** Multiple IPs with health checks

### Q40: EFS Performance Modes
- **General Purpose:** Low latency, web serving, CMS
- **Max I/O:** Higher latency, big data, media processing
- **Throughput modes:** Bursting (default) or Provisioned

### Q47: Global Accelerator vs CloudFront
- **Global Accelerator:** Static IP, TCP/UDP, non-HTTP, gaming, IoT
- **CloudFront:** HTTP/HTTPS, caching, dynamic content
- **Use GA:** Need static IPs, TCP/UDP, instant failover

---

## Secure Architectures Errors

### Q1: S3 Bucket Policy vs IAM Policy
- **Bucket Policy:** Attached to bucket, grants access to others, cross-account
- **IAM Policy:** Attached to users/roles, defines what user can do
- **Both needed:** IAM allows user + bucket policy allows bucket

### Q8: KMS Key Rotation
- **Wrong:** Manual rotation  
- **Right:** Automatic annual rotation (AWS managed)
- **Custom keys:** Can enable automatic rotation
- **Imported keys:** Must rotate manually

### Q16: WAF Rate-Based Rules
- **Function:** Block IPs exceeding request threshold (5 min window)
- **Use case:** DDoS protection, brute force prevention
- **Threshold:** Set requests per 5-minute period

### Q27: VPC Security Group vs NACL
- **Security Group:** Stateful, instance level, allow rules only
- **NACL:** Stateless, subnet level, allow + deny rules, numbered
- **Use SG:** Most cases, simple
- **Use NACL:** Need deny rules, subnet-level control

### Q34: S3 Block Public Access
- **4 Settings:** Block public ACLs, ignore public ACLs, block public policies, restrict cross-account
- **Account level:** Can set for entire AWS account
- **Bucket level:** Can set per bucket

### Q43: Cognito User Pools vs Identity Pools
- **User Pools:** User directory, sign-in/sign-up, authentication
- **Identity Pools:** Grant AWS credentials, authorization to AWS resources
- **Together:** User Pool authenticates → Identity Pool gives AWS access

### Q50: IAM Permission Boundaries
- **Function:** Max permissions an IAM entity can have
- **Use case:** Delegate admin permissions safely
- **Logic:** Effective perms = Identity policy AND Boundary

### Q54: AWS Certificate Manager (ACM)
- **Free:** SSL/TLS certificates for AWS services
- **Auto renewal:** Managed certificates auto-renew
- **Services:** CloudFront, ALB, API Gateway, Elastic Beanstalk
- **Note:** CloudFront certs MUST be in us-east-1

---

## Cost-Optimized Errors

### Q4: S3 Storage Classes Cost
- **Cheapest → Most expensive:**
  1. S3 Glacier Deep Archive ($0.00099/GB)
  2. S3 Glacier Flexible ($0.004/GB)
  3. S3 Intelligent-Tiering ($0.0025-0.023/GB)
  4. S3 One Zone-IA ($0.01/GB)
  5. S3 Standard-IA ($0.0125/GB)
  6. S3 Standard ($0.023/GB)

### Q11: Reserved Instances Types
- **Standard RI:** Max discount (72%), can't change, 1-3 years
- **Convertible RI:** Less discount (54%), can change instance type
- **Scheduled RI:** Reserve for recurring schedules
- **Savings Plans:** Flexible, commitment in $/hour

### Q30: S3 Intelligent-Tiering
- **Function:** Auto moves objects between tiers based on access
- **Tiers:** Frequent, Infrequent (30d), Archive (90d), Deep Archive (180d)
- **No fees:** No retrieval fees, small monitoring fee
- **Use case:** Unknown or changing access patterns

### Q46: EC2 Spot Instances
- **Discount:** Up to 90% off On-Demand
- **Risk:** Can be interrupted with 2-min notice
- **Use case:** Fault-tolerant, flexible workloads (batch, big data)
- **Spot Fleet:** Mix of Spot + On-Demand for availability

---

## Study Priority (Ranked by Weakness)

1. **CRITICAL: Resilient Architectures (42%)** - ECS, RDS, Aurora, S3, CloudFront
2. **CRITICAL: High-Performing (47%)** - EBS, ElastiCache, Lambda, Global Accelerator
3. **Secure Architectures (63%)** - S3 security, KMS, Cognito, VPC security
4. **Cost-Optimized (60%)** - S3 storage classes, RIs, Spot instances

## Quick Tips
- **ECS:** Task definition = blueprint, awsvpc for dynamic ports
- **S3:** 30-day minimum for IA classes, lifecycle rules one-way
- **RDS:** Multi-AZ = HA (sync), Read Replica = scale (async)
- **VPC:** SG = stateful/allow only, NACL = stateless/allow+deny
- **Caching:** Redis = features, Memcached = simple/multi-thread
- **Global:** CloudFront = HTTP/cache, GA = static IP/TCP/UDP

