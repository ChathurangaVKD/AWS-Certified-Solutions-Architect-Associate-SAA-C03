# Practice Test 4 Review - Quick Reference

**Date:** Mar 1, 2026 | **Score:** 49/65 (75%) ⚠️ BORDERLINE | **Time:** 99 min

## Domain Scores
| Domain | Score | Status |
|--------|-------|--------|
| Secure Architectures | 11/13 (85%) | ✅ Strong |
| High-Performing | 17/22 (77%) | ⚠️ Review |
| Resilient | 14/19 (74%) | ⚠️ Review |
| Cost-Optimized | 6/10 (60%) | ❌ CRITICAL |

**Trend:** Test 3: 80% → Test 4: 75% (-5%, slight regression)

---

## CRITICAL: Cost-Optimized (4 Errors)

### Q10: S3 Requester Pays
- **Feature:** Requester pays transfer + request costs (bucket owner pays storage)
- **Use case:** Share large datasets, shift costs to users
- **Requirement:** Requester must be authenticated (not anonymous)
- **Enable:** Bucket property setting

### Q25: Glacier Retrieval Options
- **Expedited:** 1-5 min, most expensive ($0.03/GB)
- **Standard:** 3-5 hours, moderate ($0.01/GB)
- **Bulk:** 5-12 hours, cheapest ($0.0025/GB)
- **Deep Archive Retrieval:**
  - Standard: 12 hours
  - Bulk: 48 hours

### Q43: EC2 Reserved Instance Scope
- **Regional RI:** Flexibility across AZs + instance sizes (within family)
- **Zonal RI:** Capacity reservation in specific AZ, less flexible
- **Convertible RI:** Change instance family, OS, tenancy (54% discount)
- **Standard RI:** Cannot change instance type (72% discount)

### Q54: AWS Cost Explorer
- **Function:** Visualize, understand, manage AWS costs
- **Features:** Forecasting, RI recommendations, cost allocation tags
- **Granularity:** Monthly, daily, hourly
- **Reports:** Service, account, tag, region breakdown

---

## Resilient Architectures (5 Errors)

### Q7: Auto Scaling Metrics - Default vs Custom
- **Default (no agent):** CPU, Network In/Out, Disk Read/Writes
- **Custom (needs agent):** Memory utilization, disk space, custom metrics
- **Memory:** Requires CloudWatch agent installed
- **Target tracking:** Can use custom metrics once published

### Q21: Auto Scaling Cooldown Period
- **Purpose:** Prevent rapid scaling actions
- **Default:** 300 seconds (5 min)
- **Behavior:** No scaling during cooldown (except if urgent)
- **Override:** Can set per scaling policy
- **Use case:** Let previous scaling action stabilize

### Q24: EFS Lifecycle Management
- **IA transition:** Move to Infrequent Access after N days (7, 14, 30, 60, 90)
- **Cost savings:** Up to 92% vs Standard storage
- **Transparent:** Automatic, no app changes needed
- **Access:** Automatically moved back to Standard on access

### Q30: Lambda Versions + Aliases
- **Version:** Immutable snapshot ($LATEST = mutable)
- **Alias:** Pointer to version(s), can split traffic (blue/green)
- **Use case:** Gradual deployments, testing, rollback
- **Example:** Alias "prod" → 90% v2 + 10% v3

### Q60: RDS Blue/Green Deployments
- **Purpose:** Test changes (schema, parameters) on clone before production
- **Process:** Create green (clone), test, promote with minimal downtime
- **Downtime:** 1 min during switchover
- **Rollback:** Keep blue environment for quick rollback

---

## High-Performing (5 Errors)

### Q2: Aurora Global Database
- **Feature:** Single primary region, up to 5 secondary regions
- **Replication:** <1 second lag between regions
- **RPO:** 1 second, RTO: <1 minute (promote secondary)
- **Use case:** DR, global low-latency reads
- **vs Read Replicas:** Global DB = region-level DR, Replicas = scaling

### Q4: S3 Byte-Range Fetches
- **Function:** Request specific byte ranges of object
- **Use case:** Download large files in parallel, resume downloads
- **Performance:** Can saturate network, faster than single request
- **Failure resilience:** Retry only failed range, not entire file

### Q17: Elastic Beanstalk Deployment Policies
- **All at once:** All instances updated simultaneously (downtime)
- **Rolling:** Update in batches (reduced capacity)
- **Rolling with additional:** Launch new batch first (maintain capacity)
- **Immutable:** Full new instances, swap all at once (safest, costly)
- **Blue/Green:** Separate environment, swap URLs (instant rollback)

### Q40: EC2 Network Performance
- **Placement Groups:** Cluster = lowest latency (10 Gbps)
- **Enhanced Networking:** SR-IOV, 25-100 Gbps
- **ENA:** Elastic Network Adapter (up to 100 Gbps)
- **EFA:** Elastic Fabric Adapter (HPC, MPI, inter-node communication)

### Q55: CloudFront Signed URLs vs Signed Cookies
- **Signed URLs:** Single file access, RTMP
- **Signed Cookies:** Multiple files, don't change URLs
- **Use URLs:** Individual files, RTMP streaming
- **Use Cookies:** Multiple files, existing URLs unchanged

---

## Secure Architectures (2 Errors)

### Q8: VPC Endpoint Gateway vs Interface
- **Gateway:** S3 + DynamoDB only, free, route table entry
- **Interface (PrivateLink):** Most AWS services, ENI with private IP, $0.01/hour
- **Use Gateway:** S3 or DynamoDB (free, simple)
- **Use Interface:** Other services, need private IP, on-premises access

### Q47: AWS Systems Manager Session Manager
- **Feature:** Browser-based shell access to EC2, no SSH keys needed
- **Benefits:** IAM-based, logged in CloudTrail, no bastion host, no open ports
- **Requirement:** SSM agent installed (pre-installed on Amazon Linux)
- **vs SSH:** No keys, no security group rules, centralized audit

---

## Key Patterns

### Cost Optimization
- **Requester Pays:** Shift costs to data consumers
- **Glacier tiers:** Expedited (fast/$$$), Standard (medium/$$), Bulk (slow/$)
- **RI scope:** Regional = flexible, Zonal = capacity reservation
- **Cost Explorer:** Visualize, forecast, optimize

### Auto Scaling & Deployments
- **Custom metrics:** Need CloudWatch agent for memory
- **Cooldown:** Prevents rapid scaling thrashing
- **Lambda aliases:** Weighted traffic splitting
- **Beanstalk:** Immutable = safest, rolling = economy
- **RDS Blue/Green:** Test safely before production

### Performance
- **Aurora Global:** <1s lag, <1 min failover
- **S3 byte-range:** Parallel downloads
- **ENA vs EFA:** ENA = general, EFA = HPC/MPI
- **CloudFront signed:** URLs = 1 file, Cookies = multiple

### Security & Access
- **VPC Endpoint:** Gateway (S3/DDB, free), Interface (others, paid)
- **Session Manager:** SSH replacement, IAM-based, no keys

---

## Study Priority
1. **CRITICAL: Cost-Optimized (60%)** - S3 costs, Glacier, RIs, Cost Explorer
2. **Resilient (74%)** - Auto Scaling details, EFS, Lambda versions, RDS deployments
3. **High-Performing (77%)** - Aurora Global, S3 performance, Beanstalk, networking

## Quick Wins
- **Auto Scaling:** Memory needs CloudWatch agent (not default)
- **Cooldown:** 5 min default, prevents rapid scaling
- **Lambda alias:** Weighted traffic for gradual deployments
- **Aurora Global:** <1s replication, <1 min failover
- **VPC Endpoint:** Gateway (S3/DDB, free), Interface (others, paid)
- **Session Manager:** No SSH keys, IAM-based access

## Memorize
- **Glacier retrieval times:** Expedited (1-5 min), Standard (3-5h), Bulk (5-12h)
- **RI types:** Standard (72%, no change), Convertible (54%, can change)
- **RI scope:** Regional (flexible AZ/size), Zonal (fixed AZ)
- **EFS IA transition:** 7, 14, 30, 60, 90 days options

