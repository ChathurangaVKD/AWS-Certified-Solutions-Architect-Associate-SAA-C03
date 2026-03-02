# Practice Test 2 Review - Quick Reference

**Date:** Mar 2, 2026 | **Score:** 49/65 (75%) ⚠️ BORDERLINE PASS | **Improvement:** +7 from Test 1

## Domain Scores
| Domain | Score | Status |
|--------|-------|--------|
| Resilient Architectures | 13/15 (87%) | ✅ Strong |
| Cost-Optimized | 12/14 (86%) | ✅ Strong |
| High-Performing | 15/20 (75%) | ⚠️ Review |
| Secure Architectures | 9/16 (56%) | ❌ CRITICAL |

**Progress:** High-Performing +32%, Resilient +16%, Secure -22% (dropped), Cost -14%

---

## CRITICAL: Secure Architectures (7 Errors)

### Q7: CloudFront + ACM Certificate Region
- **Wrong:** Any region with CloudFront edge  
- **RIGHT:** MUST be us-east-1 (N. Virginia) ONLY
- **Why:** CloudFront is global, uses us-east-1 as control plane
- **Rule:** CloudFront certs ALWAYS us-east-1, no exceptions

### Q11: RDS IAM Authentication
- **Feature:** Database users authenticate with IAM tokens (not passwords)
- **Engines:** MySQL, PostgreSQL, Aurora
- **Benefits:** No passwords in code, centralized access control, automatic rotation
- **Token:** 15-min validity, obtained via AWS CLI/SDK

### Q29: S3 + CloudFront Origin Access Identity (OAI)
- **Purpose:** CloudFront accesses private S3 without making bucket public
- **Setup:** 1) Create OAI, 2) Grant OAI in S3 bucket policy, 3) Users → CloudFront only
- **Result:** Direct S3 access blocked, CloudFront access allowed

### Q30: AWS Secrets Manager vs SSM Parameter Store
- **Secrets Manager:** Auto rotation, cross-region replication, RDS integration, versioning
- **Parameter Store:** Free (standard), no auto rotation, simpler, hierarchical
- **Use Secrets Manager:** Database passwords, API keys needing rotation
- **Use Parameter Store:** Config values, non-rotating secrets

### Q34: GuardDuty
- **Function:** Threat detection service, analyzes logs (CloudTrail, VPC Flow, DNS)
- **Detects:** Compromised instances, reconnaissance, account compromise, crypto mining
- **Action:** Sends findings to EventBridge for automation
- **Cost:** Pay per GB analyzed

### Q44: S3 Pre-Signed URLs
- **Purpose:** Temporary access to private S3 objects
- **Validity:** Configurable (seconds to 7 days)
- **Use case:** Share private files, temporary uploads
- **Security:** URL expires, inherits creator's permissions

### Q54: WAF Geo-Blocking
- **Function:** Block/allow requests based on country
- **Use case:** Compliance, reduce attack surface
- **Attach to:** CloudFront, ALB, API Gateway
- **Rules:** Allow/block specific countries

---

## High-Performing Architecture (5 Errors)

### Q5: S3 Multipart Upload
- **When:** Files >100MB (required >5GB)
- **Benefits:** Parallel uploads, resume on failure, faster
- **Parts:** Min 5MB (except last), max 10,000 parts
- **Performance:** Can saturate network bandwidth

### Q9: ElastiCache Cluster Mode
- **Disabled:** Single node group, max 5 replicas, vertical scaling
- **Enabled:** Multiple shards, horizontal scaling, better performance
- **Use Enabled:** Need >5 replicas or horizontal scaling
- **Migration:** Can't switch modes, must create new cluster

### Q21: CloudFront Cache Behaviors
- **Default:** Applies to all requests
- **Additional:** Pattern-based routing (e.g., /api/*, /images/*)
- **Settings per behavior:** Origin, TTL, headers, cookies, query strings
- **Order:** Evaluated top to bottom, first match wins

### Q31: DynamoDB DAX (Accelerator)
- **Function:** In-memory cache for DynamoDB (microsecond latency)
- **Compatible:** Drop-in replacement, same API
- **Use case:** Read-heavy, eventually consistent reads
- **vs ElastiCache:** DAX = DynamoDB only, ElastiCache = general purpose

### Q49: EBS IOPS vs Throughput
- **IOPS:** I/O operations per second, important for small block sizes
- **Throughput:** MB/s, important for large sequential I/O
- **gp3:** 3000 IOPS base, 125 MB/s base, independent tuning
- **io2:** Up to 64,000 IOPS, 1000 MB/s, high performance

---

## Resilient Architectures (2 Errors)

### Q15: S3 Cross-Region Replication (CRR)
- **Requirements:** Versioning enabled on both buckets, IAM role
- **Replication:** New objects only (not retroactive)
- **Existing objects:** Use S3 Batch Replication
- **Delete markers:** Optional replication
- **Use case:** Compliance, lower latency, disaster recovery

### Q37: Route 53 Health Checks Types
- **Endpoint:** Monitor IP/domain (HTTP, HTTPS, TCP)
- **Calculated:** Combine multiple health checks (AND, OR, NOT)
- **CloudWatch alarm:** Monitor based on CloudWatch metric
- **Frequency:** 30s (standard) or 10s (fast)
- **Failover:** Route traffic away from unhealthy endpoints

---

## Cost-Optimized (2 Errors)

### Q3: EC2 Savings Plans vs Reserved Instances
- **Savings Plans:** Flexible (instance family, size, OS, region), $/hour commitment
- **Compute SP:** Most flexible, any instance type, 66% discount
- **EC2 Instance SP:** Specific family, 72% discount
- **Reserved Instance:** Specific instance type, 72% discount
- **Use SP:** More flexibility needed

### Q46: S3 Lifecycle Policy Minimum Days
- **Standard → Standard-IA:** 30 days minimum
- **Standard → Glacier:** 30 days minimum
- **IA → Glacier:** 30 days after transition to IA
- **Cannot:** Skip IA tiers, go directly Standard → Deep Archive (<90 days)

---

## Key Learnings

### Security Focus
- **CloudFront certs:** ALWAYS us-east-1
- **RDS IAM auth:** Token-based, no passwords
- **OAI:** CloudFront → private S3 access
- **Secrets Manager:** Auto-rotation, Secrets management
- **GuardDuty:** Threat detection from logs

### Performance
- **S3 multipart:** >100MB files, parallel uploads
- **DAX:** DynamoDB microsecond cache
- **ElastiCache cluster mode:** Horizontal scaling
- **CloudFront behaviors:** Path-based routing
- **gp3:** Tune IOPS + throughput independently

### Resilience
- **CRR:** Versioning required, new objects only
- **Health checks:** Endpoint, calculated, CloudWatch types

### Cost
- **Savings Plans:** More flexible than RIs
- **S3 lifecycle:** 30-day minimums before transitions

---

## Study Priority
1. **CRITICAL: Secure Architectures (56%)** - CloudFront+ACM, IAM auth, Secrets Manager, GuardDuty
2. **High-Performing (75%)** - S3 performance, caching (DAX, ElastiCache), EBS tuning
3. **Keep Strong:** Resilient (87%), Cost (86%)

## Quick Wins
- Memorize: CloudFront certs = us-east-1 ONLY
- Understand: Secrets Manager vs Parameter Store use cases
- Practice: S3 performance optimization (multipart, CRR)
- Review: ElastiCache cluster modes and DynamoDB DAX

