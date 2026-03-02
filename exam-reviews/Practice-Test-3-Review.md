# Practice Test 3 (SAA-C03) - Exam Review

**Date:** March 1, 2026  
**Score:** 52/65 (80.00%) - ✅ **PASS**  
**Time Taken:** 97 minutes 17 seconds  
**Status:** Solid pass, consistent improvement  
**Passing Score:** 72% (need 47/65 correct)

---

---

## 📊 Performance Summary

| Metric | Result |
|--------|--------|
| **Total Questions** | 65 |
| **Correct Answers** | 52 (80.00%) |
| **Incorrect Answers** | 13 (20.00%) |
| **Pass/Fail** | **PASS** ✅ |
| **Passing Score** | 72% |
| **Questions Marked for Review** | 22 |

### Progress from Previous Tests
- **Test 1:** 42/65 (64.62%) ❌
- **Test 2:** 49/65 (75.38%) ⚠️
- **Test 3:** 52/65 (80.00%) ✅
- **Improvement:** +3 questions (+4.62%) 📈

---

## 📈 Domain Performance Analysis

| Domain | Total | Correct | Incorrect | Score | Status |
|--------|-------|---------|-----------|-------|--------|
| **Design High-Performing Architectures** | 17 | 15 | 2 | 88.24% | ✅ Strong |
| **Design Resilient Architectures** | 16 | 13 | 3 | 81.25% | ⚠️ Needs Review |
| **Design Secure Architectures** | 23 | 18 | 5 | 78.26% | ⚠️ Needs Review |
| **Design Secure Applications and Architectures** | 1 | 1 | 0 | 100% | ✅ Perfect |
| **Design Cost-Optimized Architectures** | 8 | 5 | 3 | 62.50% | ❌ Weak Area |

---

## ❌ Incorrect Questions - Detailed Review

### 1. Question 4: S3 Glacier to Intelligent-Tiering Migration
**Domain:** Design Cost-Optimized Architectures  
**Status:** ❌ Incorrect (Marked for Review)

**Question Summary:**
A media company wants to move archived videos from S3 Glacier Deep Archive to S3 Intelligent-Tiering for re-use.

**Your Answer:**
- Change the bucket's default storage class to Intelligent-Tiering so existing objects are automatically migrated

**Correct Answer:**
- Restore objects from Glacier Deep Archive in the S3 console, copy them into Intelligent-Tiering while the temporary restore is active, then delete old archived versions

**Why You Got It Wrong:**
- Changing bucket default storage class only affects NEW uploads, not existing objects
- Glacier Deep Archive objects cannot be directly copied without restoration first

**Key Learning Points:**
- ⚠️ S3 Glacier restoration is required before changing storage class
- ⚠️ Bucket default storage class ≠ existing object migration
- ⚠️ Restore → Copy → Delete workflow for Glacier objects

**Study Resources:**
- [Module 04: Storage - S3 Storage Classes](../04-Storage/README.md)
- [AWS Docs: Restoring Objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html)

---

### 2. Question 7: S3 Storage for Multi-Tenant Transcription Platform
**Domain:** Design Cost-Optimized Architectures  
**Status:** ❌ Incorrect (Marked for Review)

**Question Summary:**
A transcription platform needs highly durable, scalable storage for audio files and transcripts with frequent access.

**Your Answer:**
- Archive files in S3 Glacier vault to minimize storage cost

**Correct Answer:**
- Store audio and text files as objects in an Amazon S3 bucket

**Why You Got It Wrong:**
- Glacier is for infrequent access/archival, not frequent access
- Requirement stated "frequently access" - Glacier has retrieval delays

**Key Learning Points:**
- 🎯 S3 Standard = frequent access, high durability
- 🎯 S3 Glacier = archival, infrequent access, retrieval delays
- 🎯 Read requirements carefully: "frequent access" keyword

**Study Resources:**
- [Module 04: Storage - S3 Storage Classes Decision](../04-Storage/README.md)
- [Module 13: Cost Optimization - Storage Pricing](../13-Cost-Optimization/README.md)

---

### 3. Question 9: Database Migration - SQL Server to MySQL
**Domain:** Design Secure Architectures  
**Status:** ❌ Incorrect (Marked for Review)

**Question Summary:**
Migrate mission-critical SQL Server to MySQL with minimal downtime and real-time monitoring.

**Your Answer:**
- AWS Database Migration Service (DMS) and AWS Application Migration Service (MGN)

**Correct Answer:**
- AWS Database Migration Service (DMS) and AWS Migration Hub

**Why You Got It Wrong:**
- Application Migration Service (MGN) is for server/VM migration, not database-specific monitoring
- Migration Hub provides centralized tracking and monitoring for DMS tasks

**Key Learning Points:**
- 🔄 AWS DMS = Database migration (homogeneous & heterogeneous)
- 🔄 AWS Migration Hub = Centralized migration tracking and monitoring
- 🔄 AWS MGN = Server/VM lift-and-shift, not for DB monitoring

**Study Resources:**
- [Module 10: Migration - DMS vs Migration Hub](../10-Migration/README.md)
- [AWS Docs: Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)

---

### 4. Question 14: AWS WAF for PHP Application Protection
**Domain:** Design Secure Architectures  
**Status:** ❌ Incorrect

**Question Summary:**
Block PHP vulnerability patterns with minimal operational overhead.

**Your Answer:**
- Subscribe to AWS Shield Advanced and enable the PHP rule set

**Correct Answer:**
- Configure AWS WAF web ACL and add AWS-AWSManagedRulesPHPRuleSet

**Why You Got It Wrong:**
- AWS Shield Advanced = DDoS protection, NOT application-layer PHP vulnerabilities
- AWS WAF = Application layer (Layer 7) web application firewall

**Key Learning Points:**
- 🛡️ AWS WAF = Layer 7 (application) protection, managed rule sets
- 🛡️ AWS Shield = DDoS protection (Layer 3/4)
- 🛡️ Managed rule sets available for common vulnerabilities (PHP, SQL injection, etc.)

**Study Resources:**
- [Module 07: Security - WAF vs Shield](../07-Security/README.md)
- [AWS Docs: WAF Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html)

---

### 5. Question 16: Service Control Policies (SCPs) in AWS Organizations
**Domain:** Design Secure Architectures  
**Status:** ❌ Incorrect

**Question Summary:**
Project_OU denies ec2:DeleteFlowLogs, but Dev_OU (child) allows it. Can users delete flow logs?

**Your Answer:**
- Yes. The allow statement in Dev_OU grants permission even if parent OU denies

**Correct Answer:**
- No. Explicit deny in Project_OU applies to all child OUs and cannot be overridden

**Why You Got It Wrong:**
- Forgot the fundamental SCP rule: **Explicit DENY always wins**
- Parent OU deny cannot be overridden by child OU allow

**Key Learning Points:**
- ⚠️ SCPs: Explicit DENY > Allow (always)
- ⚠️ Parent OU policies apply to ALL child OUs
- ⚠️ SCPs define maximum permissions, not grant them

**Study Resources:**
- [Module 02: IAM - Organizations and SCPs](../02-IAM/README.md)
- [AWS Docs: SCP Evaluation Logic](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html)

---

### 6. Question 20: CloudWatch and SNS for RDS Monitoring
**Domain:** Design High-Performing Architectures  
**Status:** ❌ Incorrect (Partially correct)

**Question Summary:**
Monitor RDS CPU/memory and send email notifications when exceeding threshold.

**Your Answer:**
- Amazon Simple Email Service (SES)
- Amazon CloudWatch

**Correct Answer:**
- Amazon CloudWatch
- Amazon Simple Notification Service (SNS)

**Why You Got It Wrong:**
- Selected SES instead of SNS for CloudWatch alarm notifications
- SES = transactional emails, not alarm notifications
- SNS = pub/sub notification service, integrates directly with CloudWatch alarms

**Key Learning Points:**
- 📧 CloudWatch Alarms → SNS → Email/SMS/Lambda
- 📧 SES = bulk/transactional emails, not monitoring
- 📧 SNS = notification service for alarms and events

**Study Resources:**
- [Module 09: Monitoring - CloudWatch Alarms](../09-Monitoring/README.md)
- [AWS Docs: SNS with CloudWatch](https://docs.aws.amazon.com/sns/latest/dg/welcome-features.html)

---

### 7. Question 31: HPC Networking - EFA vs ENA
**Domain:** Design High-Performing Architectures  
**Status:** ❌ Incorrect (Marked for Review)

**Question Summary:**
HPC cluster requiring extremely low latency and high bandwidth for inter-node communication.

**Your Answer:**
- Enable enhanced networking with Elastic Network Adapter (ENA)

**Correct Answer:**
- Use Elastic Fabric Adapter (EFA) on supported EC2 instances

**Why You Got It Wrong:**
- ENA = enhanced networking but not HPC-optimized
- EFA = specialized for HPC with OS-bypass capabilities

**Key Learning Points:**
- 🚀 EFA = HPC workloads, ultra-low latency, OS-bypass, MPI support
- 🚀 ENA = general enhanced networking, good but not HPC-specific
- 🚀 HPC keyword → think EFA

**Study Resources:**
- [Module 03: Compute - HPC and Networking](../03-Compute/README.md)
- [AWS Docs: Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)

---

### 8. Question 35: ECS Auto Scaling Based on SQS Queue Depth
**Domain:** Design Resilient Architectures  
**Status:** ❌ Incorrect (Marked for Review)

**Question Summary:**
Photo-processing pipeline with SQS queue - which metric should drive ECS task auto-scaling?

**Your Answer:**
- Memory utilization of the ECS container tasks

**Correct Answer:**
- The number of visible messages in the SQS queue

**Why You Got It Wrong:**
- Memory utilization = resource-based, not workload-based
- SQS queue depth = direct indicator of pending work

**Key Learning Points:**
- 📊 SQS queue depth (ApproximateNumberOfMessagesVisible) = best metric for queue-based scaling
- 📊 Memory/CPU = resource metrics, not workload indicators
- 📊 Scale based on work pending, not resource consumption

**Study Resources:**
- [Module 08: Application Integration - SQS Scaling Patterns](../08-Application-Integration/README.md)
- [AWS Docs: Auto Scaling with SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)

---

### 9. Question 40: RDS Automated Backups and Point-in-Time Recovery
**Domain:** Design Resilient Architectures  
**Status:** ❌ Incorrect (Marked for Review - Partially correct)

**Question Summary:**
How do RDS automated backups work for point-in-time recovery?

**Your Answer (Selected 2 of 3 correct):**
- ❌ (Missing) Amazon RDS creates storage volume snapshot once per day. Transaction logs uploaded to S3 every 5 minutes
- ✅ Amazon RDS automated backups allow PITR by combining daily snapshot with continuous transaction logs
- ✅ (Incorrect selection) You must manually enable transaction log backups for PITR

**Correct Answers:**
- ✅ Daily snapshot + transaction logs every 5 minutes
- ✅ PITR combines snapshot + transaction logs
- ❌ Transaction logs are AUTOMATIC, not manual

**Why You Got It Wrong:**
- Didn't select the snapshot frequency answer
- Incorrectly thought transaction logs needed manual enablement

**Key Learning Points:**
- 💾 RDS Automated Backups = Daily snapshot + transaction logs every 5 minutes
- 💾 PITR = Snapshot + transaction logs (automatic)
- 💾 No manual intervention needed for transaction logs

**Study Resources:**
- [Module 05: Database - RDS Backups](../05-Database/README.md)
- [AWS Docs: RDS Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

---

### 10. Question 52: AWS Organizations - Moving Management Account
**Domain:** Design Resilient Architectures  
**Status:** ❌ Incorrect (Marked for Review - Partially correct)

**Question Summary:**
Move management account from Company A's organization to Company B's organization (select 3).

**Your Answer (Selected 2 of 3 correct):**
- ✅ Sign in as root and remove all member accounts
- ❌ (Missing) Delete Company A's organization to make it standalone
- ✅ Accept invitation from Company B's organization
- ✅ (Incorrect) Enable all features in Company B before sending invitation

**Correct Answers:**
- ✅ Remove all member accounts from Company A
- ✅ Delete Company A's organization (makes account standalone)
- ✅ Accept invitation from Company B

**Why You Got It Wrong:**
- Forgot the critical step: DELETE organization to convert to standalone account
- Incorrectly thought "all features" was required (it's not mandatory for invitation)

**Key Learning Points:**
- 🏢 Management account cannot move while organization exists
- 🏢 Must DELETE organization to become standalone
- 🏢 Then accept invitation from target organization

**Study Resources:**
- [Module 02: IAM - AWS Organizations](../02-IAM/README.md)
- [AWS Docs: Removing Accounts from Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html)

---

### 11. Question 53: Amazon Cognito - IAM Roles for Mobile App
**Domain:** Design Secure Architectures  
**Status:** ❌ Incorrect

**Question Summary:**
Mobile app users authenticate via Google/Facebook, need temporary AWS credentials for DynamoDB.

**Your Answer:**
- Enable CloudTrail and GuardDuty to monitor DynamoDB calls and provision credentials

**Correct Answer:**
- Create IAM role with trust policy trusting Cognito/IdP, attach DynamoDB permissions. Configure Cognito identity pools to assume role and issue temporary credentials

**Why You Got It Wrong:**
- CloudTrail/GuardDuty = monitoring/security, NOT credential provisioning
- Cognito Identity Pools = credential provisioning for federated users

**Key Learning Points:**
- 🔐 Cognito Identity Pools = temporary AWS credentials for federated users
- 🔐 IAM Role + Trust Policy + Cognito = proper architecture
- 🔐 CloudTrail/GuardDuty = monitoring, not authentication

**Study Resources:**
- [Module 02: IAM - Cognito Identity Pools](../02-IAM/README.md)
- [AWS Docs: Cognito IAM Roles](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html)

---

### 12. Question 62: S3 Transfer Acceleration vs CloudFront
**Domain:** Design Cost-Optimized Architectures  
**Status:** ❌ Incorrect

**Question Summary:**
Media streaming company - users in remote regions reporting slow load times for videos from S3.

**Your Answer:**
- Enable S3 Transfer Acceleration on the bucket

**Correct Answer:**
- Place S3 bucket behind Amazon CloudFront distribution and update DNS

**Why You Got It Wrong:**
- Transfer Acceleration = improves uploads/downloads via S3 API
- CloudFront = caching at edge locations for content delivery (better for streaming)

**Key Learning Points:**
- 🌐 CloudFront = content delivery, caching at edge (best for streaming)
- 🌐 S3 Transfer Acceleration = faster uploads/downloads via S3 API
- 🌐 Static website + remote users = CloudFront

**Study Resources:**
- [Module 04: Storage - CloudFront vs Transfer Acceleration](../04-Storage/README.md)
- [Module 13: Cost Optimization - Content Delivery](../13-Cost-Optimization/README.md)

---

### 13. Question 64: AWS Site-to-Site VPN vs Direct Connect
**Domain:** Design Secure Architectures  
**Status:** ❌ Incorrect

**Question Summary:**
Start-up needs FAST and COST-EFFECTIVE connectivity from on-premises to VPC for testing.

**Your Answer:**
- Provision AWS Direct Connect connection with IPsec tunnels

**Correct Answer:**
- Create AWS Site-to-Site VPN (IPsec VPN connection)

**Why You Got It Wrong:**
- Direct Connect = weeks to provision, expensive
- Site-to-Site VPN = minutes to provision, cost-effective
- Keyword: "fast" and "cost-effective" = VPN, not Direct Connect

**Key Learning Points:**
- ⚡ Site-to-Site VPN = fast setup (minutes), cost-effective
- ⚡ Direct Connect = weeks to provision, expensive, but high performance
- ⚡ Keywords matter: fast + cost-effective = VPN

**Study Resources:**
- [Module 06: Networking - VPN vs Direct Connect](../06-Networking/README.md)
- [AWS Docs: Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/site-site-architectures.html)

---

## 📚 Study Recommendations

### 🔴 Priority 1: Critical Weak Areas (< 70%)

#### Design Cost-Optimized Architectures (62.50%)
**Focus Topics:**
- S3 storage class transitions and lifecycle policies
- CloudFront vs S3 Transfer Acceleration decision criteria
- Cost optimization patterns for storage

**Recommended Actions:**
1. Re-read [Module 13: Cost Optimization](../13-Cost-Optimization/README.md)
2. Review [Module 04: Storage - S3 Storage Classes](../04-Storage/README.md)
3. Practice questions on S3 storage class migrations
4. Create decision matrix: CloudFront vs Transfer Acceleration vs Direct Access

---

### 🟡 Priority 2: Need Improvement (70-85%)

#### Design Resilient Architectures (81.25%)
**Focus Topics:**
- RDS backup strategies and PITR
- Auto-scaling metrics selection (SQS queue depth)
- AWS Organizations account management

**Recommended Actions:**
1. Review [Module 05: Database - RDS Backups](../05-Database/README.md)
2. Study [Module 08: Application Integration - SQS Patterns](../08-Application-Integration/README.md)
3. Deep dive: [Module 02: IAM - AWS Organizations](../02-IAM/README.md)

#### Design Secure Architectures (78.26%)
**Focus Topics:**
- AWS WAF vs AWS Shield
- Amazon Cognito Identity Pools architecture
- Service Control Policies (SCPs) evaluation logic
- VPN vs Direct Connect decision criteria

**Recommended Actions:**
1. Master [Module 07: Security - WAF, Shield, Cognito](../07-Security/README.md)
2. Practice SCP evaluation scenarios
3. Create comparison chart: Site-to-Site VPN vs Direct Connect

---

### 🟢 Priority 3: Strong Areas (> 85%)

#### Design High-Performing Architectures (88.24%) ✅
**Minor gaps:**
- EFA vs ENA for HPC workloads

**Quick Review:**
- [Module 03: Compute - HPC Networking](../03-Compute/README.md)

#### Design Secure Applications and Architectures (100%) ✅
**Perfect score - maintain with periodic review**

---

## 🎯 Action Plan for Next 7 Days

### Day 1-2: Cost Optimization Deep Dive
- [ ] Re-read Module 13 completely
- [ ] Create S3 storage class decision flowchart
- [ ] Practice 20 questions on storage cost optimization
- [ ] Hands-on: Configure S3 lifecycle policies

### Day 3-4: Security & Identity
- [ ] Review AWS WAF managed rule sets
- [ ] Study Cognito Identity Pools + IAM Roles architecture
- [ ] Practice SCP evaluation scenarios
- [ ] Create WAF vs Shield comparison chart

### Day 5-6: Resilient Architectures
- [ ] Deep dive: RDS backup and PITR mechanisms
- [ ] Study auto-scaling metrics selection
- [ ] Review AWS Organizations account management
- [ ] Hands-on: Configure RDS automated backups

### Day 7: Networking & Final Review
- [ ] VPN vs Direct Connect decision matrix
- [ ] Review all 13 incorrect questions
- [ ] Take another practice test
- [ ] Focus on weak areas identified

---

## 📊 Key Exam Patterns Observed

### Common Pitfalls to Avoid
1. ⚠️ **Reading too quickly** - Missing keywords like "fast", "cost-effective", "frequent access"
2. ⚠️ **Confusing similar services** - WAF vs Shield, EFA vs ENA, SNS vs SES
3. ⚠️ **Forgetting hierarchy rules** - SCPs explicit deny, parent > child
4. ⚠️ **Overlooking operational steps** - Glacier restore before migration, delete org before move

### Exam Success Patterns
1. ✅ **Read all options carefully** before selecting
2. ✅ **Identify keywords** in questions (fast, cost-effective, high-performance)
3. ✅ **Eliminate wrong answers** first, then choose best remaining
4. ✅ **Watch for "most", "least", "best"** qualifiers

---

## 📝 Quick Reference Cards

### S3 Storage Class Decision
```
Frequent Access (< 30 days) → S3 Standard
Infrequent Access (30-90 days) → S3 Standard-IA
Rare Access (90+ days, immediate) → S3 Glacier Instant Retrieval
Archival (minutes wait OK) → S3 Glacier Flexible Retrieval
Archival (hours wait OK) → S3 Glacier Deep Archive
Unknown Pattern → S3 Intelligent-Tiering
```

### Monitoring & Notifications
```
CloudWatch Alarms → SNS → Email/SMS/Lambda
NOT: CloudWatch → SES (SES is for transactional emails)
```

### HPC Networking
```
General Enhanced Networking → ENA
High Performance Computing (HPC) → EFA (OS-bypass, MPI)
```

### VPN vs Direct Connect
```
Fast + Cost-Effective → Site-to-Site VPN (minutes, $)
High Performance + Long-term → Direct Connect (weeks, $$$)
```

### AWS WAF vs Shield
```
Application Layer (L7) Protection → AWS WAF
DDoS Protection (L3/L4) → AWS Shield
```

---

## 🎓 Next Steps

1. **Immediate Actions (Next 24 Hours):**
   - [ ] Review all 13 incorrect questions
   - [ ] Create flashcards for confusing service pairs
   - [ ] Read Module 13: Cost Optimization completely

2. **This Week:**
   - [ ] Follow 7-day action plan above
   - [ ] Take another practice test
   - [ ] Focus on cost optimization (weakest domain)

3. **Before Exam:**
   - [ ] Review this document completely
   - [ ] Quick refresh: [Ultra-Fast Learning Index](../ULTRA-FAST-LEARNING-INDEX.md)
   - [ ] Day before: [Quick Study Notes](../QUICK-STUDY-NOTES.md)

---

## 💪 Motivational Note

**Great job on passing with 80%!** 🎉

You're well on your way to certification success. Your strong performance in high-performing architectures (88%) shows solid understanding. Focus on cost optimization (62%) and security patterns, and you'll be ready for the real exam.

**Remember:**
- 80% on practice = you're in good shape
- Focus on the 13 incorrect questions patterns
- Don't just memorize - understand WHY each answer is correct
- You've got this! 💪

---

**Document Version:** 1.0  
**Last Updated:** March 2, 2026  
**Next Review:** After next practice test

---

[← Back to Practice Tests](../14-Practice/README.md) | [Study Roadmap →](../STUDY-ROADMAP.md)

