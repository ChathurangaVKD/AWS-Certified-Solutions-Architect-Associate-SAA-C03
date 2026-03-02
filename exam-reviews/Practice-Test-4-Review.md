# Practice Test 4 (SAA-C03) - Exam Review

**Date:** March 1, 2026  
**Score:** 49/65 (75.38%) - ⚠️ **BORDERLINE PASS**  
**Time Taken:** 98 minutes 56 seconds  
**Status:** Above passing threshold but needs improvement  
**Passing Score:** 72% (need 47/65 correct)

---

---

## 📊 Performance Summary

| Metric | Result |
|--------|--------|
| **Total Questions** | 65 |
| **Correct Answers** | 49 (75.38%) |
| **Incorrect Answers** | 16 (24.62%) |
| **Pass/Fail** | **BORDERLINE PASS** ⚠️ |
| **Passing Score** | 72% |
| **Gap from Test 3** | -4.62% (3 fewer correct) |

### Performance Trend
```
Test 1: 42/65 (64.62%) ❌ FAIL
Test 2: 49/65 (75.38%) ⚠️ BORDERLINE
Test 3: 52/65 (80.00%) ✅ PASS
Test 4: 49/65 (75.38%) ⚠️ BORDERLINE (-4.62%)
─────────────────────────────────────────────
Trend: ⚠️ Slight regression from Test 3
```

---

## 📈 Domain Performance Analysis

| Domain | Total | Correct | Incorrect | Score | Status |
|--------|-------|---------|-----------|-------|--------|
| **Design Secure Architectures** | 13 | 11 | 2 | 84.62% | ✅ Strong |
| **Design High-Performing Architectures** | 22 | 17 | 5 | 77.27% | ⚠️ Needs Review |
| **Design Resilient Architectures** | 19 | 14 | 5 | 73.68% | ⚠️ Needs Review |
| **Design Secure Applications** | 1 | 1 | 0 | 100.00% | ✅ Perfect |
| **Design Cost-Optimized Architectures** | 10 | 6 | 4 | 60.00% | ❌ **CRITICAL** |

### Domain Analysis

#### ✅ Strengths
- **Design Secure Architectures (84.62%)** - Strong understanding of security controls
- **Design High-Performing Architectures (77.27%)** - Good grasp of performance optimization

#### ⚠️ Areas Needing Improvement
- **Design Resilient Architectures (73.68%)** - Focus on fault tolerance and disaster recovery

#### ❌ Critical Weaknesses
- **Design Cost-Optimized Architectures (60.00%)** - **CRITICAL AREA**
  - EC2 pricing models (Reserved Instances, Savings Plans, Spot)

---

## ❌ Incorrect Questions - Detailed Review
   - Storage lifecycle policies
   - Cost allocation and billing

---

## ❌ Incorrect Questions Analysis

### Question 7: Auto Scaling Metrics ❌
**Topic:** Design Resilient Architectures  
**Your Answer:** Network Out  
**Correct Answer:** Memory Utilization  

**Why You Got It Wrong:**
- Memory Utilization is NOT a predefined metric for Auto Scaling target tracking
- Requires CloudWatch agent to publish custom metrics
- All other options (CPU, Network In/Out) are predefined

**Key Takeaway:**
> 🔑 **EC2 does not publish memory metrics by default. You must install CloudWatch agent for memory-based scaling.**

---

### Question 13: Redshift Snapshot Costs ❌
**Topic:** Design Cost-Optimized Architectures  
**Your Answer:** Increase automated snapshot retention to 35 days  
**Correct Answer:** Delete unneeded manual snapshots  

**Why You Got It Wrong:**
- Manual snapshots persist until explicitly deleted and incur storage charges
- Increasing retention INCREASES cost, not reduces it
- Should audit and delete old manual snapshots first

**Key Takeaway:**
> 💰 **Manual Redshift snapshots are retained indefinitely. Always clean up old manual backups to reduce costs.**

---

### Question 17: S3 Glacier Retrieval ❌
**Topic:** Design Cost-Optimized Architectures  
**Your Answer:** Expedited  
**Correct Answer:** Standard  

**Why You Got It Wrong:**
- Expedited (1-5 min) is faster but more expensive
- Standard (3-5 hours) meets the requirement and is cost-effective
- Bulk (5-12 hours) is too slow

**Key Takeaway:**
> ⏱️ **S3 Glacier Flexible Retrieval tiers: Expedited (1-5min, $$), Standard (3-5hr, $), Bulk (5-12hr, ¢)**

---

### Question 18: Backend Security Group ❌
**Topic:** Design Resilient Architectures  
**Your Answer:** Use the launch configuration as the source  
**Correct Answer:** Use the frontend security group ID as the source  

**Why You Got It Wrong:**
- Security group rules accept other SG IDs as sources
- Launch configurations cannot be used in SG rules
- SG-to-SG references automatically handle IP changes

**Key Takeaway:**
> 🔒 **Security groups can reference other security groups. This provides automatic, scalable access control.**

---

### Question 19: Multi-Tier Savings Plans ❌
**Topic:** Design Cost-Optimized Architectures  
**Your Answer:** EC2 Instance SP for web; Compute SP for app and DB  
**Correct Answer:** Compute SP for web; EC2 Instance SP for app; RDS RI for DB  

**Why You Got It Wrong:**
- Web tier (varied families) needs Compute Savings Plan flexibility
- App tier (stable family) benefits from higher EC2 Instance SP discount
- RDS requires its own Reserved Instances, not covered by EC2 SPs

**Key Takeaway:**
> 💡 **Compute SP = flexibility; EC2 Instance SP = highest discount; RDS = separate RIs**

---

### Question 25: CloudTrail Log Integrity ❌
**Topic:** Design Secure Architectures  
**Your Answer:** Use SSE-KMS encryption for the CloudTrail logs  
**Correct Answer:** Enable CloudTrail log file integrity validation  

**Why You Got It Wrong:**
- Encryption protects confidentiality, not integrity
- Log file integrity validation uses SHA-256 hashes + digital signatures
- Provides cryptographic proof logs weren't tampered with

**Key Takeaway:**
> 🔐 **CloudTrail log file integrity validation = tamper detection. Encryption = confidentiality.**

---

### Question 28: Auto Scaling Lifecycle ❌
**Topic:** Design High-Performing Architectures  
**Your Answer:** Customize the termination policy to copy data  
**Correct Answer:** Add lifecycle hooks to the Auto Scaling group  

**Why You Got It Wrong:**
- Termination policies decide WHICH instance to terminate
- Lifecycle hooks allow custom actions BEFORE termination
- Hooks provide wait state for cleanup scripts/data copy

**Key Takeaway:**
> ⏸️ **Lifecycle hooks = pause before termination. Termination policies = choose which instance.**

---

### Question 34: Mixed Instance Auto Scaling ❌
**Topic:** Design Cost-Optimized Architectures  
**Your Answer:** Use all t2.micro On-Demand instances  
**Correct Answer:** Use mixed instances policy: On-Demand base = 2; above that 20% On-Demand / 80% Spot  

**Why You Got It Wrong:**
- Downgrading to t2.micro may hurt performance
- Mixed instances policy balances cost and reliability
- Keep base capacity On-Demand, use Spot for burst

**Key Takeaway:**
> 🎯 **Mixed instances policy: stable base (On-Demand) + cost-effective burst (Spot)**

---

### Question 36: CloudFormation Drift Detection ❌
**Topic:** Design High-Performing Architectures  
**Your Answer:** Grant additional Read permissions to drift detection  
**Correct Answer:** Explicitly set the property values in the template  

**Why You Got It Wrong:**
- Drift detection only tracks explicitly declared properties
- Default values are not monitored
- Must declare all properties to detect drift

**Key Takeaway:**
> 📝 **CloudFormation drift detection: if not in template, it's not tracked. Declare defaults explicitly.**

---

### Question 38: Multi-Account ALB Access ❌
**Topic:** Design High-Performing Architectures  
**Your Answer:** B and D (missing C)  
**Correct Answer:** B and C  

**Why You Got It Wrong:**
- Both inbound rule for parent objects AND disabling Block Public Access are needed
- Missed the critical step of allowing public reads via bucket policy

**Key Takeaway:**
> 🌐 **S3 public website: (1) Disable Block Public Access + (2) Bucket policy for public reads**

---

### Question 45: Session Storage ❌
**Topic:** Design High-Performing Architectures  
**Your Answer:** C and D (ELB + ElastiCache)  
**Correct Answer:** B and D (DynamoDB + ElastiCache)  

**Why You Got It Wrong:**
- ELB does not store session data, only provides sticky sessions
- DynamoDB is a proper session store with TTL support
- ElastiCache is correct for in-memory caching

**Key Takeaway:**
> 💾 **Session stores: DynamoDB (durable, TTL) + ElastiCache (fast, in-memory)**

---

### Question 48: ALB Access Logging ❌
**Topic:** Design Secure Architectures  
**Your Answer:** AWS CloudTrail data events for the ALB  
**Correct Answer:** ALB access logs to Amazon S3  

**Why You Got It Wrong:**
- CloudTrail logs control plane API calls, not data plane requests
- ALB access logs record every request with client IP details
- Access logs are designed for forensics and compliance

**Key Takeaway:**
> 📊 **CloudTrail = control plane (API calls). ALB access logs = data plane (requests).**

---

### Question 56: EBS Cross-Region ❌
**Topic:** Design Resilient Architectures  
**Your Answer:** Enable Amazon S3 CRR on the snapshot storage bucket  
**Correct Answer:** Copy the EBS snapshot from us-east-1 to ap-south-1  

**Why You Got It Wrong:**
- Snapshots are stored in AWS-managed S3, you can't configure CRR
- Must use built-in snapshot copy feature
- Can copy across regions with optional encryption changes

**Key Takeaway:**
> 📸 **EBS snapshots: use snapshot copy API, not S3 replication**

---

### Question 58: Restore S3 Versioned Object ❌
**Topic:** Design Resilient Architectures  
**Your Answer:** Option D (partial understanding)  
**Correct Answer:** Delete the delete marker  

**Why You Got It Wrong:**
- Deleting with versioning creates a delete marker
- Must remove the delete marker to restore visibility
- Simply retrieving version ID doesn't restore normal access

**Key Takeaway:**
> 🗑️ **S3 versioning: delete = add marker. Restore = delete the marker.**

---

---

## 📚 Study Recommendations

### Priority 1: Cost Optimization (60% - CRITICAL)
**Time:** 3-4 hours

1. **EC2 Pricing Models**
   - Review: Reserved Instances vs Savings Plans
   - Module: `13-Cost-Optimization/README.md`
   - Practice: Cost calculator scenarios

2. **Storage Lifecycle & Glacier**
   - Understand: Standard → Standard-IA → Glacier tiers
   - Review: Glacier retrieval options (Expedited, Standard, Bulk)
   - Module: `04-Storage/README.md`

3. **Redshift Snapshots**
   - Manual vs automated snapshots
   - Snapshot retention and cleanup
   - Module: `11-Analytics/README.md`

### Priority 2: Auto Scaling & Resilience (73.68%)
**Time:** 2-3 hours

1. **Auto Scaling Metrics**
   - Default vs custom metrics
   - CloudWatch agent for memory/disk metrics
   - Module: `03-Compute/README.md`

2. **Lifecycle Hooks**
   - Termination policies vs lifecycle hooks
   - Use cases for graceful shutdown
   - Module: `12-Architecture-Patterns/README.md`

3. **Security Group Referencing**
   - SG-to-SG rules
   - Automatic scaling benefits
   - Module: `06-Networking/README.md`

### Priority 3: CloudFormation & Drift
**Time:** 1-2 hours

1. **Drift Detection**
   - Explicit vs implicit properties
   - Best practices for templates
   - Module: `12-Architecture-Patterns/README.md`

### Priority 4: CloudTrail vs Service Logs
**Time:** 1 hour

1. **Logging Comparison**
   - CloudTrail (control plane)
   - ALB access logs (data plane)
   - VPC Flow Logs (network layer)
   - Module: `09-Monitoring/README.md`

---

## 🎯 Quick Reference Cards

### Cost Optimization Cheat Sheet

```
EC2 PRICING:
├─ On-Demand: Pay per second, no commitment
├─ Reserved Instances: 1-3 year commit, specific family/size
├─ Savings Plans
│  ├─ Compute SP: Flexible (family/size/region), lower discount
│  └─ EC2 Instance SP: Fixed family, highest discount
└─ Spot: Up to 90% off, can be interrupted

GLACIER RETRIEVAL:
├─ Expedited: 1-5 minutes, $$$
├─ Standard: 3-5 hours, $
└─ Bulk: 5-12 hours, ¢

REDSHIFT SNAPSHOTS:
├─ Automated: Retained per policy, auto-deleted
└─ Manual: Persist forever, must delete manually ⚠️
```

### Security & Logging

```
CLOUDTRAIL LOG INTEGRITY:
├─ Enable: Log file integrity validation
├─ Creates: SHA-256 hashes + digital signatures
└─ Proves: Logs not tampered/deleted

LOGGING TYPES:
├─ CloudTrail: Control plane (CreateBucket, ModifyDB)
├─ ALB Access Logs: Data plane (HTTP requests, client IPs)
├─ VPC Flow Logs: Network (IP traffic, 5-tuple)
└─ S3 Access Logs: Bucket requests

SECURITY GROUP RULES:
├─ Can reference: Other SG IDs (auto-scales)
├─ Cannot reference: Launch configs, ASG names
└─ Stateful: Return traffic auto-allowed
```

### Auto Scaling & Resilience

```
AUTO SCALING METRICS:
├─ Predefined: CPU, Network In/Out, ALB RequestCount
└─ Custom: Memory, Disk (needs CloudWatch agent) ⚠️

LIFECYCLE HOOKS:
├─ Purpose: Run custom actions before termination
├─ States: Terminating:Wait, Launching:Wait
└─ Use cases: Backup data, drain connections

TERMINATION POLICIES:
├─ Purpose: Choose WHICH instance to terminate
├─ Types: OldestInstance, NewestInstance, ClosestToNextInstanceHour
└─ Not for: Running custom cleanup scripts ⚠️
```

---

## 📊 Progress Tracking

### Test Comparison

| Test | Score | Change | Resilient | High-Perf | Secure | Cost |
|------|-------|--------|-----------|-----------|--------|------|
| Test 1 | 64.62% | - | 71% | 43% | 78% | 100% |
| Test 2 | 75.38% | +10.76% | 87% | 75% | 56% | 86% |
| Test 3 | 80.00% | +4.62% | 81% | 88% | 78% | 63% |
| Test 4 | 75.38% | -4.62% | 74% | 77% | 85% | 60% |

### Weak Area Consistency

**Cost Optimization** has been consistently weak:
- Test 1: 100% (only 3 questions)
- Test 2: 86%
- Test 3: 63%
- Test 4: 60% ⚠️ **Getting worse!**

**Action:** Dedicate focused study session to cost optimization concepts.

---

## 🎯 Action Plan for Test 5

### Before Next Test (Target: 85%+)

1. ✅ **Complete cost optimization module** (4 hours)
   - [ ] Review pricing models
   - [ ] Practice cost calculator
   - [ ] Understand Glacier tiers

2. ✅ **Review auto scaling deep dive** (2 hours)
   - [ ] Lifecycle hooks vs termination policies
   - [ ] Custom metrics setup

3. ✅ **CloudFormation drift detection** (1 hour)
   - [ ] Template best practices

4. ✅ **Take focused quiz on weak areas** (14-Practice folder)

### During Test 5

- ⏰ Time management: ~2 minutes per question
- 🔍 Read EVERY word carefully (especially "MOST", "LEAST")
- 📌 Flag uncertain questions for review
- ✅ Focus on eliminating wrong answers first

---

## 📝 Notes

### Patterns Observed
1. **Cost questions consistently missed** - Need dedicated review
2. **Confusion between similar services** - Create comparison tables
3. **Missing "explicit" requirements** - CloudFormation defaults issue

### Test-Taking Issues
1. Rushed through cost questions (need to slow down)
2. Misread "control plane vs data plane" logging question
3. Overlooked security group referencing capability

---

**Next Steps:**
1. Review this document thoroughly
2. Focus on Priority 1 & 2 study areas
3. Take focused practice questions on weak domains
4. Schedule Test 5 after completing review (target: 1 week)

**Target for Test 5:** 55+/65 (85%+) ✅

---

[← Back to Exam Reviews](README.md) | [Main Guide](../README.md)

