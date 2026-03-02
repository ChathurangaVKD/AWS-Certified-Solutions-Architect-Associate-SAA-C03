# Practice Test 2 (SAA-C03) - Exam Review

**Date:** March 2, 2026  
**Score:** 49/65 (75.38%) - ⚠️ **BORDERLINE PASS**  
**Time Taken:** Not recorded  
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
| **Questions Marked for Review** | 21 |

### Progress from Practice Test 1
- **Previous Score:** 42/65 (64.62%)
- **Current Score:** 49/65 (75.38%)
- **Improvement:** +7 questions (+10.76%) 📈

---

## 📈 Domain Performance Analysis

| Domain | Total | Correct | Incorrect | Score | Status |
|--------|-------|---------|-----------|-------|--------|
| **Design Resilient Architectures** | 15 | 13 | 2 | 86.67% | ✅ Strong |
| **Design Cost-Optimized Architectures** | 14 | 12 | 2 | 85.71% | ✅ Strong |
| **Design High-Performing Architectures** | 20 | 15 | 5 | 75.00% | ⚠️ Needs Review |
| **Design Secure Architectures** | 16 | 9 | 7 | 56.25% | ❌ **CRITICAL** |

### Performance Visualization
```
Design Resilient:           ████████░░ 87% ✅ STRONG
Design Cost-Optimized:      ████████░░ 86% ✅ STRONG  
Design High-Performing:     ███████░░░ 75% ⚠️
Design Secure:              █████░░░░░ 56% ❌ CRITICAL
```

---

## ❌ Incorrect Questions - Detailed Review

### Comparison with Practice Test 1
```
Domain                        Test 1  →  Test 2  Change
──────────────────────────────────────────────────────────
Design High-Performing         43%   →   75%    +32% 📈 HUGE
Design Resilient               71%   →   87%    +16% 📈
Design Secure                  78%   →   56%    -22% 📉 DROPPED
Design Cost-Optimized         100%   →   86%    -14% 📉
```

---

## 🔴 Critical Weak Areas (Detailed Analysis)

### Priority 1: Design Secure Architectures (56% - 7 incorrect) 🚨

#### Key Topics That Need IMMEDIATE Review:

##### 1. CloudFront + ACM Certificate Region ⚠️ CRITICAL
**Common Mistake:** Thinking certificate can be in any region

**THE RULE (Memorize This!):**
```
🔒 CloudFront + ACM Certificate:
   ✅ MUST be in us-east-1 (N. Virginia) ONLY
   
   ❌ Cannot use certificates from:
      - us-west-1, us-west-2
      - eu-west-1, eu-central-1
      - ap-southeast-1, ap-south-1
      - Any other region
   
   ✅ ONLY us-east-1 works with CloudFront
```

**Why us-east-1?**
- CloudFront is a GLOBAL service
- Control plane is in us-east-1
- All CloudFront certificates validated against us-east-1 ACM

**Correct Setup Steps:**
1. Request/Import certificate in **ACM us-east-1**
2. Add alternate domain names (CNAMEs) to CloudFront distribution
3. Associate ACM certificate (from us-east-1) with CloudFront
4. Create Route 53 alias record → CloudFront distribution

**Study Resources:**
- [Module 06: Networking - CloudFront](../06-Networking/README.md#cloudfront)
- [Module 07: Security - ACM](../07-Security/README.md#certificate-manager)

##### 2. S3 Cross-Account Access - Bucket Policies ⚠️
**Common Mistake:** Thinking SCPs grant cross-account access

**CRITICAL CONCEPT:**
```yaml
SCP (Service Control Policy):
  Purpose: RESTRICT permissions within YOUR organization
  Scope: AWS Organizations only
  Action: DENY certain actions
  Cross-Account: ❌ CANNOT grant access to external accounts
  
Bucket Policy:
  Purpose: GRANT permissions to resources
  Scope: Specific S3 bucket
  Action: ALLOW or DENY
  Cross-Account: ✅ CAN grant access to external accounts

Correct Cross-Account S3 Access:
  Method 1: Bucket Policy (BEST for S3)
    - Grant external account/IAM principal access
    - Resource-based policy on bucket
    
  Method 2: IAM Role
    - External account assumes role in your account
    - Identity-based access
    - Good for temporary access
```

**Example Bucket Policy for Cross-Account:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowExternalAccount",
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::123456789012:root"
    },
    "Action": [
      "s3:GetObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::my-bucket",
      "arn:aws:s3:::my-bucket/*"
    ],
    "Condition": {
      "Bool": {
        "aws:SecureTransport": "true"
      }
    }
  }]
}
```

**Study Resources:**
- [Module 02: IAM - SCPs](../02-IAM/README.md#service-control-policies)
- [Module 04: Storage - S3 Policies](../04-Storage/README.md#bucket-policies)
- [Module 07: Security - Cross-Account Access](../07-Security/README.md#cross-account)

##### 3. VPN & Encryption ⚠️
**Topics to review:**
- Site-to-Site VPN setup
- VPN encryption (IPsec)
- Client VPN vs Site-to-Site VPN
- Direct Connect + VPN for encryption

**Study Resources:**
- [Module 06: Networking - VPN](../06-Networking/README.md#vpn)

##### 4. IAM Roles & Federation ⚠️
**Topics to review:**
- IAM Roles vs IAM Users
- Federated access (SAML, OIDC)
- STS AssumeRole
- Cross-account roles

**Study Resources:**
- [Module 02: IAM - Roles](../02-IAM/README.md#iam-roles)
- [Module 07: Security - Federation](../07-Security/README.md#federation)

---

### Priority 2: Design High-Performing Architectures (75% - 5 incorrect)

#### Key Topics That Need Review:

##### 1. S3 Performance Optimization ⚠️
**Topics to review:**
- S3 Transfer Acceleration
- Multipart upload
- Byte-range fetches
- S3 Select & Glacier Select

**Study Resources:**
- [Module 04: Storage - S3 Performance](../04-Storage/README.md#s3-performance)

##### 2. Database Caching Strategies ⚠️
**Topics to review:**
- ElastiCache Redis vs Memcached
- DAX (DynamoDB Accelerator)
- RDS Proxy
- Application-level caching

**Study Resources:**
- [Module 05: Database - Caching](../05-Database/README.md#caching)

##### 3. Network Performance ⚠️
**Topics to review:**
- Enhanced Networking (ENA vs SR-IOV)
- Elastic Fabric Adapter (EFA)
- Placement Groups
- VPC Flow Logs

**Study Resources:**
- [Module 06: Networking - Performance](../06-Networking/README.md#performance)

---

### Priority 3: Design Cost-Optimized Architectures (86% - 2 incorrect)

#### Key Topics That Need Review:

##### 1. S3 Glacier Retrieval Costs ⚠️
**Common Mistake:** Choosing Instant Retrieval for cost optimization

**S3 Glacier Cost Comparison:**
```
Storage Class              | Retrieval Time | Cost Pattern
────────────────────────────────────────────────────────────
Glacier Instant Retrieval  | Milliseconds   | High retrieval cost
                          |                | No free quota
                          |                | ❌ Not cost-optimized
────────────────────────────────────────────────────────────
Glacier Flexible Retrieval | Minutes-Hours  | 10 GB/month FREE
                          |                | Low cost after quota
                          |                | ✅ Best for occasional access
────────────────────────────────────────────────────────────
Glacier Deep Archive      | 12-48 hours    | Lowest storage cost
                          |                | Bulk: $0.0025/GB retrieval
                          |                | Best for long-term archive
```

**Cost Optimization Strategy:**
- **Unpredictable access:** Flexible Retrieval (use free 10 GB quota)
- **Rare access (< 1x/year):** Deep Archive
- **Millisecond access needed:** Instant Retrieval (but expensive)

**Study Resources:**
- [Module 04: Storage - Glacier](../04-Storage/README.md#glacier)
- [Module 13: Cost Optimization - Storage](../13-Cost-Optimization/README.md#storage-costs)

##### 2. EC2 Pricing Models ⚠️
**Topics to review:**
- Savings Plans vs Reserved Instances
- Spot Instances strategies
- On-Demand Capacity Reservations

**Study Resources:**
- [Module 03: Compute - Pricing](../03-Compute/README.md#ec2-pricing)
- [Module 13: Cost Optimization - Compute](../13-Cost-Optimization/README.md)

---

## 📚 Recommended Study Plan

### Week 1: Fix Security Knowledge Gap (56% → 80%+)

#### Days 1-2: CloudFront, ACM, and HTTPS
- [ ] Read [Module 06: Networking - CloudFront](../06-Networking/README.md#cloudfront)
- [ ] Read [Module 07: Security - ACM](../07-Security/README.md#certificate-manager)
- [ ] **Memorize:** CloudFront certificates MUST be in us-east-1
- [ ] Complete CloudFront + ACM labs
- [ ] Practice HTTPS/SSL questions

#### Days 3-4: Cross-Account Access & IAM
- [ ] Read [Module 02: IAM](../02-IAM/README.md)
- [ ] Focus on cross-account access patterns
- [ ] Understand bucket policies vs IAM policies vs SCPs
- [ ] Complete cross-account access labs
- [ ] Practice IAM policy questions

#### Days 5-6: VPN & Encryption
- [ ] Read [Module 06: Networking - VPN](../06-Networking/README.md#vpn)
- [ ] Read [Module 07: Security - Encryption](../07-Security/README.md#encryption)
- [ ] Complete Site-to-Site VPN labs
- [ ] Review Direct Connect + VPN
- [ ] Practice encryption questions

#### Day 7: Security Domain Practice
- [ ] Complete all [Module 07 Practice Questions](../07-Security/PRACTICE-QUESTIONS.md)
- [ ] Complete [Module 02 Practice Questions](../02-IAM/PRACTICE-QUESTIONS.md)
- [ ] Review incorrect answers
- [ ] Create flashcards for security concepts

---

### Week 2: Improve High-Performing Knowledge (75% → 85%+)

#### Days 8-9: S3 Performance
- [ ] Read [Module 04: Storage - S3 Performance](../04-Storage/README.md#s3-performance)
- [ ] Complete S3 Transfer Acceleration lab
- [ ] Review multipart upload strategies
- [ ] Practice S3 performance questions

#### Days 10-11: Database & Caching
- [ ] Read [Module 05: Database - Caching](../05-Database/README.md#caching)
- [ ] Complete ElastiCache labs (Redis & Memcached)
- [ ] Review DAX for DynamoDB
- [ ] Practice database performance questions

#### Days 12-13: Network Performance
- [ ] Read [Module 06: Networking - Performance](../06-Networking/README.md#performance)
- [ ] Review Enhanced Networking (ENA, EFA)
- [ ] Study Placement Groups
- [ ] Practice network performance questions

#### Day 14: High-Performance Domain Practice
- [ ] Complete all [Module 04 Practice Questions](../04-Storage/PRACTICE-QUESTIONS.md)
- [ ] Complete all [Module 05 Practice Questions](../05-Database/PRACTICE-QUESTIONS.md)
- [ ] Review all flagged questions
- [ ] Take Practice Test 3

---

## 🎯 Quick Reference Cards

### Card 1: CloudFront + ACM (CRITICAL!)
```yaml
Rule: CloudFront Certificate Region
  MUST: us-east-1 (N. Virginia)
  CANNOT: Any other region
  
Setup Steps:
  1. Create/Import cert in ACM us-east-1
  2. Add CNAMEs to CloudFront
  3. Associate cert with CloudFront
  4. Create Route 53 alias → CloudFront
  
Exam Trap: Answer choices with other regions
Answer: Always choose us-east-1 for CloudFront
```

### Card 2: S3 Cross-Account Access
```yaml
Method 1: Bucket Policy (BEST for S3)
  - Attach policy to bucket
  - Grant external account/principal
  - No role assumption needed
  
Method 2: IAM Role
  - Create role with trust policy
  - External account assumes role
  - Good for temporary access
  
❌ SCP CANNOT grant cross-account access
   SCPs only RESTRICT within YOUR org
```

### Card 3: S3 Glacier Cost Optimization
```yaml
Unpredictable Access Pattern:
  Best: Flexible Retrieval
  Why: 10 GB/month FREE retrieval
  
Rare Access (< 1x/year):
  Best: Deep Archive
  Why: Lowest storage cost
  
Need Millisecond Access:
  Best: Instant Retrieval
  Why: Fast, but expensive
  
Cost from Low to High:
  Deep Archive < Flexible < Instant
```

### Card 4: IAM Policy Types
```yaml
Identity-Based (IAM):
  - Attached to: Users, Groups, Roles
  - Controls: What identity can do
  - Example: User can read S3
  
Resource-Based (Bucket):
  - Attached to: Resources (S3, KMS)
  - Controls: Who can access resource
  - Example: Account 123 can read bucket
  - ✅ Can grant cross-account access
  
SCP (Organizations):
  - Attached to: Accounts, OUs
  - Controls: Max permissions (DENY)
  - Example: Deny ec2:RunInstances
  - ❌ CANNOT grant permissions
  - ❌ CANNOT grant cross-account
```

---

## 📝 Key Takeaways

### What Went Right? ✅
1. **Huge Improvement in High-Performing** (43% → 75%)
   - +32% improvement from Practice Test 1
   - Study efforts are paying off!

2. **Strong Resilient Architectures** (87%)
   - Only 2 incorrect questions
   - Solid understanding of HA/DR

3. **Good Cost Optimization** (86%)
   - Minor gaps but mostly solid

### What Went Wrong? ❌
1. **Security Knowledge DROPPED** (78% → 56%)
   - Lost 22 percentage points
   - 7 incorrect questions (most in any domain)
   - Needs immediate attention

2. **Specific Weak Topics:**
   - CloudFront + ACM certificate region (us-east-1 rule)
   - Cross-account access (bucket policies vs SCPs)
   - VPN and encryption methods

### Critical Gaps to Fix:
1. **Memorize:** CloudFront certs MUST be in us-east-1
2. **Understand:** SCPs cannot grant cross-account access
3. **Review:** S3 Glacier retrieval costs and strategies
4. **Practice:** IAM policies, roles, and federation

---

## 🎓 Next Steps

### Immediate Actions (Today)
1. ✅ Review this document completely
2. [ ] **MEMORIZE:** CloudFront certificates = us-east-1 ONLY
3. [ ] **UNDERSTAND:** SCP vs Bucket Policy for cross-account
4. [ ] Read [Module 07: Security - CloudFront](../07-Security/README.md#cloudfront-security)

### This Week (Priority: Security)
1. [ ] Follow Week 1 study plan (Security focus)
2. [ ] Complete all Module 07 practice questions
3. [ ] Complete all Module 02 practice questions (IAM)
4. [ ] Create security flashcards

### Before Next Test
1. [ ] Complete Week 1 & 2 study plans
2. [ ] Retake all section quizzes
3. [ ] Review [ULTRA-FAST-LEARN](../ULTRA-FAST-LEARNING-INDEX.md)
4. [ ] Take Practice Test 3
5. [ ] Target: ≥80% (52+ correct)

---

## 📊 Performance Tracking

### Overall Progress
```
Practice Test 1: 42/65 (64.62%) ❌ FAIL
Practice Test 2: 49/65 (75.38%) ⚠️ BORDERLINE
Next Target:     52/65 (80.00%) ✅ STRONG PASS

Gap to Close: +3 questions
Study Focus: Security (critical)
```

### Domain Progress Tracking
```
Domain                    Test 1 → Test 2 → Target
────────────────────────────────────────────────────
High-Performing           43%  →  75%  →  85%
Resilient                 71%  →  87%  →  90%
Secure                    78%  →  56%  →  85% ⚠️
Cost-Optimized           100%  →  86%  →  90%
```

---

## 📌 Important Exam Tips

### Keywords to Watch For
- **"Cost-effective"** → Look for cheapest option (Glacier, Spot, S3 IA)
- **"High-performance"** → Look for low latency (ENA, Placement Groups, ElastiCache)
- **"Minimal operational overhead"** → Look for managed services (RDS, Fargate, Lambda)
- **"Secure"** → Look for encryption, IAM, VPC (not public access)

### Common Traps in This Test
1. ❌ CloudFront cert in wrong region → Always us-east-1
2. ❌ Using SCP for cross-account → Use bucket policy instead
3. ❌ Choosing expensive retrieval → Use Flexible with free quota
4. ❌ Over-complicating solutions → Simple is usually right

---

## 🔗 Related Resources

### Study Materials
- [Module 02: IAM](../02-IAM/README.md) - Identity & Access Management
- [Module 07: Security](../07-Security/README.md) - Security services
- [Module 06: Networking](../06-Networking/README.md) - CloudFront, VPN
- [Module 04: Storage](../04-Storage/README.md) - S3, Glacier
- [Module 13: Cost Optimization](../13-Cost-Optimization/README.md) - Cost strategies

### Quick References
- [Fast Learn Guide](../FAST-LEARN-GUIDE.md) - Quick review
- [Ultra Fast Learning Index](../ULTRA-FAST-LEARNING-INDEX.md) - Last-minute review
- [Security Quick Reference](../QUICK-REFERENCE.md#security) - Security concepts

---

**Remember:** You passed this test (75.38%) but security knowledge dropped significantly. Focus on security domain to ensure consistent performance!

**Critical Focus:** CloudFront + ACM (us-east-1), Cross-account access patterns, VPN & encryption

**Target for Practice Test 3:** ≥80% (52+ correct answers)

Good luck! You're making progress! 🚀📈

---

[← Previous: Practice Test 1 Review](2026-03-02-Practice-Test-1-Review.md) | [Back to Exam Reviews](README.md) | [Next: Practice Test 3 Review →](2026-03-01-Practice-Test-3-Review.md)

