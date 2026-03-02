# Practice Test 5 Review - Quick Reference

**Date:** Mar 2, 2026 | **Score:** 42/65 (65%) ❌ FAILED | **Time:** 130 min

## Domain Scores
| Domain | Score | Status |
|--------|-------|--------|
| Cost-Optimized | 3/3 (100%) | ✅ Perfect |
| Secure | 14/18 (78%) | ⚠️ Review |
| Resilient | 15/21 (71%) | ⚠️ Review |
| High-Performing | 10/23 (43%) | ❌ CATASTROPHIC |

**Trend:** Test 3: 80% → Test 4: 75% → Test 5: 65% ❌ (Major regression)

**Pattern:** 39 questions marked for review (60% uncertainty)

---

## CATASTROPHIC: High-Performing (13 Errors - 43%)

### Q1: QuickSight - Analytics & Visualization
- **Purpose:** BI service, interactive dashboards, ML insights
- **Data sources:** S3, RDS, Redshift, Athena, 3rd party
- **Features:** SPICE (in-memory), auto-scaling, embedded analytics
- **vs Kibana:** QuickSight = AWS-native BI, Kibana = log analytics

### Q2: CloudWatch Agent Configuration - aggregation_dimensions
- **Purpose:** Define metric dimensions for aggregation
- **Example:** Aggregate by InstanceId, AutoScalingGroup, InstanceType
- **Use case:** See metrics at instance level AND aggregate level
- **Config:** JSON in CloudWatch agent config file

### Q8: ECS on Outposts vs Local Zones
- **Outposts:** On-premises AWS infrastructure, same APIs, full control
- **Local Zones:** AWS infrastructure near metros, low latency, limited services
- **Use Outposts:** Data residency, on-prem processing
- **Use Local Zones:** Low latency for end users

### Q12: CloudWatch Cross-Account Observability
- **Feature:** Share CloudWatch data across accounts
- **Use case:** Central monitoring account, multi-account visibility
- **Setup:** Monitoring account + source accounts linked
- **Permissions:** IAM roles for cross-account access

### Q13: ALB Path-Based Routing
- **Feature:** Route to different targets based on URL path
- **Example:** /api/* → API servers, /images/* → image servers
- **Rules:** Evaluated by priority, first match wins
- **Flexible:** Query strings, headers, source IP conditions

### Q15: EC2 Instance Metadata Service (IMDS)
- **Endpoint:** http://169.254.169.254/latest/meta-data/
- **Data:** Instance ID, type, public/private IP, security groups, IAM role
- **IMDSv2:** Token-based (more secure), prevents SSRF
- **Use case:** Apps query their own metadata/credentials

### Q16: Global Accelerator Static IPs
- **Feature:** 2 static anycast IPs for global traffic
- **Use case:** Non-HTTP protocols, gaming, IoT, static IP requirement
- **Benefits:** DDoS protection, instant failover, performance
- **vs CloudFront:** GA = TCP/UDP/static IP, CF = HTTP/cache

### Q19: S3 Performance Optimization
- **Multipart upload:** >100MB files, parallel parts
- **Transfer Acceleration:** Use edge locations (50-500% faster)
- **Byte-range fetches:** Parallel downloads
- **Prefix distribution:** 3500 PUT/s, 5500 GET/s per prefix
- **Avoid:** Sequential LIST operations (slow)

### Q22: EC2 Placement Group - Cluster
- **Purpose:** Low latency, high throughput (10 Gbps)
- **Location:** Single AZ, same rack ideally
- **Use case:** HPC, big data, tightly coupled apps
- **Limitation:** Single AZ (no HA)

### Q26: ElastiCache Redis Multi-AZ
- **Feature:** Automatic failover to replica
- **Replication:** Async, can have multiple replicas
- **Failover:** <2 minutes typically
- **Use case:** HA caching, session store

### Q27: ECS Dynamic Port Mapping
- **Requirement:** Application Load Balancer
- **How:** ALB routes to ephemeral ports (32768-65535)
- **Benefit:** Multiple containers per instance, efficient resource use
- **Network mode:** awsvpc or bridge

### Q31: Glue Data Catalog Crawler
- **Purpose:** Automatically discover schema, populate data catalog
- **Sources:** S3, RDS, Redshift, DynamoDB
- **Output:** Tables in Glue Data Catalog (for Athena, EMR, Redshift)
- **Schedule:** On-demand or scheduled

### Q50: EC2 Public IP Change on Stop/Start
- **Behavior:** Public IP changes on stop/start
- **Elastic IP:** Static public IP, persists through stop/start
- **Private IP:** Never changes
- **Solution:** Allocate Elastic IP and associate

---

## Resilient Architectures (6 Errors - 71%)

### Q17: FSx for Lustre - S3 Data Repository
- **Feature:** Link FSx to S3, lazy load data
- **Data Repository Task:** Schedule S3 sync (import/export)
- **Use case:** Process S3 data with high performance
- **Performance:** 100s GB/s throughput, millions IOPS

### Q18: FSx for Windows File Server
- **Protocol:** SMB, Windows-native
- **Features:** Active Directory integration, DFS, VSS
- **Multi-AZ:** Automatic failover
- **Access:** VPC peering, Transit Gateway, Direct Connect

### Q21: Auto Scaling Cooldown
- **Purpose:** Prevent scaling thrashing
- **Default:** 300 seconds (5 min)
- **During cooldown:** No new instances launched (unless critical)
- **Best practice:** Set appropriate cooldown for warm-up time

### Q23: Kinesis Video Streams
- **Purpose:** Ingest video from millions of devices
- **Sources:** Cameras, smartphones, drones, vehicles
- **Use case:** Live streaming, video analytics, ML
- **Processing:** Rekognition, SageMaker, custom consumers

### Q24: CloudFront Custom Error Pages
- **Feature:** Return custom HTML for 4xx/5xx errors
- **Configure:** Error page path in S3, cache duration
- **Use case:** Branded error pages, maintenance page
- **Status codes:** Can customize per error code

### Q25: CloudFront Cache Invalidation
- **Purpose:** Remove objects from edge cache before TTL expires
- **Cost:** First 1000 paths free per month, then $0.005/path
- **Pattern:** Can use wildcards (/images/*)
- **Alternative:** Versioned filenames (better practice)

---

## Secure Architectures (4 Errors - 78%)

### Q6: S3 Object Lock - Compliance vs Governance
- **Compliance:** Cannot delete, even by root (WORM)
- **Governance:** Can delete with special permission (s3:BypassGovernanceRetention)
- **Legal hold:** Indefinite lock, no expiration
- **Use compliance:** Regulatory requirements (SEC, FINRA)

### Q14: VPC Flow Logs - Traffic Types
- **ALL:** Capture accepted + rejected traffic
- **ACCEPT:** Only accepted traffic
- **REJECT:** Only rejected traffic
- **Level:** VPC, Subnet, or ENI
- **Destination:** CloudWatch Logs, S3, Kinesis Firehose

### Q41: ALB + Cognito Authentication
- **Feature:** ALB authenticates users via Cognito
- **Flow:** User → ALB → Cognito → ALB → App (with user info)
- **Benefits:** Offload auth from app, integrate social/enterprise identity
- **Headers:** ALB passes user claims in headers

### Q62: Security Hub
- **Purpose:** Central security findings from multiple services
- **Integrations:** GuardDuty, Inspector, Macie, IAM Access Analyzer, Config
- **Standards:** CIS, PCI-DSS, AWS Foundational Security Best Practices
- **Action:** Aggregate findings, prioritize, automate response

---

## Key Problem Areas

### CloudWatch & Monitoring (Critical Gap)
- **Agent config:** aggregation_dimensions for metric grouping
- **Cross-account:** Central monitoring setup
- **Custom metrics:** Publish from applications

### ECS & Containers
- **Outposts vs Local Zones:** Deployment locations
- **Dynamic ports:** Requires ALB, efficient resource use
- **Network modes:** awsvpc, bridge, host differences

### S3 Performance
- **Multipart:** Parallel uploads for large files
- **Transfer Acceleration:** Use edge locations
- **Byte-range:** Parallel downloads
- **Prefix scaling:** 3500 PUT/5500 GET per prefix

### Storage & File Systems
- **FSx Lustre:** S3 integration, data repository tasks
- **FSx Windows:** SMB, AD integration, Multi-AZ
- **ElastiCache:** Redis Multi-AZ for HA

### Analytics Services
- **QuickSight:** BI dashboards, SPICE engine
- **Glue Crawler:** Auto-discover schemas
- **Athena:** Query S3 with SQL (uses Glue catalog)

### Global Services
- **Global Accelerator:** Static IPs, TCP/UDP, non-HTTP
- **CloudFront:** HTTP/HTTPS, caching, error pages, invalidation

### Auto Scaling
- **Cooldown:** Prevents rapid scaling
- **Target tracking:** Maintain metric at target
- **Step scaling:** Different actions for different thresholds

---

## Study Priority (URGENT)

### 1. HIGH-PERFORMING (43%) - CATASTROPHIC
- **Module 03 (Compute):** CloudWatch agent, ECS deployment, Auto Scaling
- **Module 11 (Analytics):** QuickSight, Glue, Athena, Redshift monitoring
- **Module 04 (Storage):** S3 performance optimization
- **Module 06 (Networking):** Global Accelerator, ALB routing, placement groups

### 2. RESILIENT (71%) - BELOW PASSING
- **FSx variants:** Lustre (HPC), Windows (SMB), NetApp, OpenZFS
- **Kinesis:** Video Streams, Data Streams, Firehose
- **CloudFront:** Error pages, cache invalidation, behaviors
- **Auto Scaling:** Cooldown, policies, AZ rebalancing

### 3. SECURE (78%) - NEEDS IMPROVEMENT
- **S3 Object Lock:** Compliance vs Governance modes
- **VPC Flow Logs:** Capture levels and destinations
- **ALB + Cognito:** Authentication integration
- **Security Hub:** Central security posture management

---

## Quick Wins for Next Test

### Must Memorize
1. **CloudWatch agent:** aggregation_dimensions for metric grouping
2. **ECS dynamic ports:** Requires ALB + awsvpc/bridge mode
3. **IMDS endpoint:** http://169.254.169.254/latest/meta-data/
4. **S3 performance:** Multipart (>100MB), Transfer Acceleration, byte-range
5. **Global Accelerator:** Static IPs, TCP/UDP, instant failover
6. **ElastiCache Redis:** Multi-AZ for HA with auto-failover
7. **FSx Lustre:** Direct S3 integration, data repository tasks
8. **Glue Crawler:** Auto-discover schemas for Athena/EMR
9. **Auto Scaling cooldown:** 5 min default, prevents thrashing
10. **S3 Object Lock:** Compliance (cannot delete), Governance (can bypass)

### Practice Focus
- Set up CloudWatch agent with custom metrics
- Practice ECS task definitions and service configurations
- Review S3 performance optimization techniques
- Understand FSx types and use cases
- Study Global Accelerator vs CloudFront decision tree
- Review analytics pipeline: S3 → Glue → Athena → QuickSight

### Pattern Recognition
- **Static IP needed:** Global Accelerator or Elastic IP
- **Video ingestion:** Kinesis Video Streams
- **HPC storage:** FSx for Lustre
- **Windows file share:** FSx for Windows
- **Schema discovery:** Glue Crawler
- **BI dashboards:** QuickSight
- **Low latency caching:** ElastiCache (Redis for HA)

## Critical Actions
⚠️ **URGENT:** Re-study High-Performing domain (dropped 34 points)
⚠️ **URGENT:** Complete hands-on labs for CloudWatch, ECS, S3 optimization
⚠️ Review FSx types and Kinesis services
⚠️ Practice analytics services workflow

