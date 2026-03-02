# Practice Test 3 Review - Quick Reference

**Date:** Mar 1, 2026 | **Score:** 52/65 (80%) ✅ PASS | **Time:** 97 min

## Domain Scores
| Domain | Score | Status |
|--------|-------|--------|
| High-Performing | 15/17 (88%) | ✅ Strong |
| Resilient | 13/16 (81%) | ⚠️ Review |
| Secure | 18/23 (78%) | ⚠️ Review |
| Cost-Optimized | 5/8 (63%) | ❌ Weak |

**Progress:** Test 1: 65% → Test 2: 75% → Test 3: 80% (steady improvement)

---

## CRITICAL: Cost-Optimized (3 Errors)

### Q4: S3 Glacier to Intelligent-Tiering Migration
- **Wrong:** Change bucket default storage class  
- **RIGHT:** Restore from Glacier → Copy to Intelligent-Tiering → Delete Glacier
- **Why:** Bucket default only affects NEW uploads, not existing objects
- **Process:** Cannot transition directly FROM Glacier classes
- **Rule:** Glacier Deep Archive → must restore first (12-48 hours)

### Q36: EC2 Instance Types - Compute Optimized
- **Wrong:** t3.large (burstable, general purpose)  
- **RIGHT:** c5.large (compute-optimized)
- **C5/C6:** Compute-optimized, high CPU, batch processing, gaming, ML inference
- **T3:** Burstable, variable workloads, cheap
- **M5:** General purpose, balanced
- **R5:** Memory-optimized

### Q63: RDS Storage Auto Scaling
- **Feature:** Automatically increases storage when space low
- **Triggers:** <10% free space, low storage >5 min, 6+ hours since last scaling
- **Max:** Set maximum storage threshold
- **Benefits:** No downtime, prevents out-of-space errors
- **Engines:** All RDS engines support it

---

## Resilient Architectures (3 Errors)

### Q17: FSx for Lustre + DataSync
- **Wrong:** Use DataSync to continuously sync  
- **RIGHT:** FSx Lustre links directly to S3 (no DataSync needed)
- **FSx Lustre features:**
  - Native S3 integration (import/export)
  - Data repository tasks (scheduled sync)
  - High performance (100s GB/s, millions IOPS)
- **Use DataSync:** For on-premises → AWS, or different AWS services
- **FSx use case:** HPC, ML training, video processing

### Q18: FSx for Windows Multi-AZ
- **Feature:** Multi-AZ deployment for HA
- **Access:** From different VPCs via VPC peering or Transit Gateway
- **Protocol:** SMB, supports Active Directory integration
- **vs EFS:** Windows = FSx, Linux = EFS

### Q23: Kinesis Video Streams
- **Purpose:** Ingest video from devices (cameras, phones, drones)
- **Use case:** Video analytics, ML, live/on-demand streaming
- **vs Data Streams:** Video Streams = video, Data Streams = any data
- **Output:** S3, Rekognition, SageMaker

---

## Secure Architectures (5 Errors)

### Q10: IAM Policy Evaluation Logic
- **Order:**
  1. Explicit DENY (always wins)
  2. Explicit ALLOW
  3. Implicit DENY (default)
- **Rule:** Deny always overrides allow
- **Example:** If one policy denies S3, even if another allows, DENY wins

### Q14: S3 Bucket Keys (SSE-KMS)
- **Purpose:** Reduce KMS API calls (cost savings)
- **How:** S3 generates bucket-level key, uses it for objects
- **Benefit:** 99% fewer KMS requests
- **Cost:** Lower CloudTrail log volume (fewer KMS calls)
- **Enable:** Per bucket setting

### Q28: Transit Gateway vs VPC Peering
- **VPC Peering:** Direct connection, max 125 peerings per VPC, no transitive routing
- **Transit Gateway:** Hub-and-spoke, connect 1000s VPCs, transitive routing
- **Use TGW:** >10 VPCs, need central management, on-premises integration
- **Use Peering:** Simple 1-to-1 connections, lower cost

### Q42: AWS Config Rules
- **Purpose:** Evaluate resource compliance against rules
- **Managed rules:** Pre-built (e.g., encrypted-volumes, required-tags)
- **Custom rules:** Lambda-based custom logic
- **Remediation:** Auto-remediate with SSM automation
- **vs CloudTrail:** Config = compliance state, CloudTrail = API audit

### Q57: KMS Multi-Region Keys
- **Feature:** Identical key in multiple regions (same key ID, material)
- **Use case:** Encrypt in one region, decrypt in another (DR, global apps)
- **vs Regional:** Standard KMS keys are regional only
- **Replication:** Key material replicated, policies per-region

---

## High-Performing (2 Errors)

### Q22: Route 53 Geoproximity Routing + Bias
- **Function:** Route based on location + optional bias adjustment
- **Bias:** -99 to +99, positive = more traffic, negative = less traffic
- **Use case:** Shift traffic gradually between regions
- **vs Geolocation:** Geoproximity uses distance, Geolocation uses user's region

### Q48: Lambda Provisioned Concurrency
- **Purpose:** Pre-warmed instances (no cold starts)
- **Use case:** Latency-sensitive apps
- **Cost:** Pay for provisioned capacity even if unused
- **vs Reserved:** Provisioned = instant, Reserved = cost savings

---

## Key Patterns Identified

### Storage Migrations
- **FROM Glacier:** Must restore first, can't directly transition out
- **Bucket defaults:** Only affect new uploads, not existing objects
- **FSx Lustre:** Native S3 integration, no DataSync needed

### Security & Compliance
- **IAM deny:** Always wins over allow
- **S3 Bucket Keys:** Reduce KMS costs by 99%
- **Config:** Compliance monitoring + auto-remediation
- **Transit Gateway:** Scalable VPC connectivity (>10 VPCs)

### Performance Optimization
- **Geoproximity bias:** Fine-tune traffic distribution
- **Lambda provisioned:** Eliminate cold starts
- **FSx Lustre:** Extreme performance for HPC/ML

### Cost Control
- **Instance types:** Match workload (C5=compute, R5=memory, T3=burstable)
- **RDS auto scaling:** Automatic storage growth
- **S3 Bucket Keys:** Reduce KMS request costs

---

## Study Priority
1. **Cost-Optimized (63%)** - Storage classes, instance types, RDS features
2. **Resilient (81%)** - FSx types, Kinesis Video, Multi-AZ
3. **Secure (78%)** - IAM evaluation, KMS features, Transit Gateway, Config

## Quick Wins
- **Remember:** Cannot transition OUT of Glacier without restoring
- **FSx Lustre:** Direct S3 link, HPC workloads
- **FSx Windows:** Windows = FSx, Linux = EFS
- **IAM:** Explicit deny always wins
- **S3 Bucket Keys:** Enable to reduce KMS costs 99%
- **Transit Gateway:** Use when >10 VPCs need connectivity

## Improvement Tips
- Review S3 storage class transition rules and restrictions
- Practice FSx use cases (Lustre vs Windows vs NetApp vs OpenZFS)
- Understand KMS cost optimization techniques
- Study EC2 instance family purposes (C/M/R/T/I/D)

