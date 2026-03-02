# 🎴 Visual Memory Cards - Quick Recall System

**Purpose:** Fast review cards with visual mnemonics for exam day

---

## 🔥 CRITICAL CARDS (Memorize First!)

### Card 1: CloudFront Certificate Region 🌐
```
╔══════════════════════════════════════════════╗
║  🔒 CLOUDFRONT + ACM CERTIFICATE             ║
╠══════════════════════════════════════════════╣
║                                              ║
║  ✅ MUST BE: us-east-1 (N. Virginia)        ║
║  ❌ CANNOT BE: Any other region             ║
║                                              ║
║  Why? CloudFront control plane = us-east-1  ║
║                                              ║
║  💡 Memory: "CF-E1" (CloudFront = East-1)   ║
║                                              ║
║  Trap: "Use region closest to users" ❌     ║
║        "Use same region as origin" ❌        ║
║                                              ║
╚══════════════════════════════════════════════╝

Test: Practice Test 2 (Critical Topic)
Difficulty: ⭐⭐⭐ (Easy to forget!)
```

### Card 2: VPC Endpoint Types 🔌
```
┌────────────────────────────────────────────┐
│  🔌 VPC ENDPOINTS DECISION                │
├────────────────────────────────────────────┤
│                                            │
│  Service = S3? ──────────► Gateway (FREE) │
│  Service = DynamoDB? ────► Gateway (FREE) │
│  Service = Anything else? ► Interface ($) │
│                                            │
│  Gateway Endpoint:                         │
│    • Route table entry                     │
│    • No IP address                         │
│    • FREE                                  │
│                                            │
│  Interface Endpoint:                       │
│    • ENI with private IP                   │
│    • One per AZ                            │
│    • $0.01/hour + data                     │
│                                            │
│  💡 Memory: "GSD = Gateway for S3 &       │
│             DynamoDB, Interface for rest"  │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 1, Question 15
Difficulty: ⭐⭐⭐
```

### Card 3: Transit Gateway vs VPG 🚇
```
┌────────────────────────────────────────────┐
│  🚇 VPN THROUGHPUT SCALING                │
├────────────────────────────────────────────┤
│                                            │
│  Need > 1.25 Gbps VPN throughput?         │
│                                            │
│  ❌ VPG (Virtual Private Gateway)         │
│     • Max: 1.25 Gbps                       │
│     • Only 1 VPN active at a time          │
│     • Others are standby only              │
│     • NO ECMP support                      │
│                                            │
│  ✅ Transit Gateway                        │
│     • Max: 50+ Gbps aggregate              │
│     • Multiple VPNs active simultaneously  │
│     • ECMP load balancing                  │
│     • Example: 4 tunnels = 5 Gbps          │
│                                            │
│  💡 Memory: "TGW = Traffic Gets Wider"    │
│            "VPG = Very Poor (for) Growing"│
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 1, Question 13
Difficulty: ⭐⭐⭐
```

### Card 4: CloudWatch Metrics - Default vs Custom 📊
```
╔══════════════════════════════════════════════╗
║  📊 CLOUDWATCH METRICS                       ║
╠══════════════════════════════════════════════╣
║                                              ║
║  DEFAULT (No agent needed):                  ║
║  ✅ CPU Utilization                          ║
║  ✅ Network In / Out                         ║
║  ✅ Disk Read / Write                        ║
║  ✅ Status Checks                            ║
║                                              ║
║  CUSTOM (Agent required):                    ║
║  ⚙️ Memory Utilization                       ║
║  ⚙️ Disk Space Used %                        ║
║  ⚙️ Swap Utilization                         ║
║  ⚙️ Application metrics                      ║
║                                              ║
║  Detailed Monitoring:                        ║
║  • Changes frequency: 5 min → 1 min          ║
║  • Does NOT add new metrics                  ║
║  • Does NOT include memory                   ║
║                                              ║
║  💡 Memory: "MDS = Memory, Disk, Swap       ║
║            (need Agent)"                     ║
║                                              ║
╚══════════════════════════════════════════════╝

Test: Practice Test 4, Q7 & Test 5, Q2
Difficulty: ⭐⭐⭐
```

---

## 📦 STORAGE CARDS

### Card 5: S3 Storage Class Decision 🗄️
```
┌────────────────────────────────────────────┐
│  🗄️ S3 STORAGE CLASS SELECTION            │
├────────────────────────────────────────────┤
│                                            │
│  Keyword → Storage Class:                  │
│                                            │
│  "Frequently accessed" ───► S3 Standard    │
│  "Immediate access required" ─► S3 Standard│
│  "Infrequently accessed" ──► Standard-IA   │
│  "Archival" ───────────────► Glacier       │
│  "Long-term backup" ───────► Glacier Deep  │
│  "Unknown patterns" ───────► Intelligent   │
│                                            │
│  Access Times:                             │
│  • Standard: Immediate (ms)                │
│  • Standard-IA: Immediate (ms)             │
│  • Glacier Flexible: 1-12 hours            │
│  • Glacier Deep: 12-48 hours               │
│                                            │
│  💡 Memory: "FAST = Frequent Access =      │
│            Standard Storage"               │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 3, Question 7
Difficulty: ⭐⭐
```

### Card 6: S3 Glacier Restoration 🧊
```
╔══════════════════════════════════════════════╗
║  🧊 S3 GLACIER RESTORATION                   ║
╠══════════════════════════════════════════════╣
║                                              ║
║  ❌ WRONG: Change bucket default class       ║
║     → Only affects NEW uploads               ║
║                                              ║
║  ✅ CORRECT: 4-Step Process                  ║
║                                              ║
║  Step 1: Initiate Restore (12-48 hours)     ║
║  Step 2: Access Temporary Copy (1-365 days) ║
║  Step 3: Copy to Target Storage Class       ║
║  Step 4: Delete Glacier Version (optional)  ║
║                                              ║
║  Key Facts:                                  ║
║  • Cannot directly change Glacier objects    ║
║  • Must restore before copying               ║
║  • Restore creates temporary accessible copy ║
║  • Original stays in Glacier until deleted   ║
║                                              ║
║  💡 Memory: "GDR = Glacier Definitely       ║
║            Requires (restore)"              ║
║                                              ║
╚══════════════════════════════════════════════╝

Test: Practice Test 3, Question 4
Difficulty: ⭐⭐⭐
```

### Card 7: Redshift Snapshots 📸
```
┌────────────────────────────────────────────┐
│  📸 REDSHIFT SNAPSHOTS                     │
├────────────────────────────────────────────┤
│                                            │
│  AUTOMATED SNAPSHOTS:                      │
│  • Retention: 1-35 days (configurable)     │
│  • Auto-deleted: YES ✅                     │
│  • Cost: FREE (up to 1x cluster size)      │
│                                            │
│  MANUAL SNAPSHOTS:                         │
│  • Retention: FOREVER (until deleted) ⚠️   │
│  • Auto-deleted: NO ❌                      │
│  • Cost: $0.024/GB/month                   │
│  • Accumulates if not cleaned up           │
│                                            │
│  Cost Reduction:                           │
│  ✅ Delete old manual snapshots            │
│  ❌ Increase retention (increases cost)    │
│  ❌ Cross-region copy (doubles cost)       │
│                                            │
│  💡 Memory: "Manual = Must-delete"         │
│            "Auto = Auto-expires"           │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 4, Question 13
Difficulty: ⭐⭐
```

---

## 🖥️ COMPUTE CARDS

### Card 8: ECS Task Definition 📋
```
┌────────────────────────────────────────────┐
│  📋 ECS COMPONENTS                         │
├────────────────────────────────────────────┤
│                                            │
│  Task Definition (Blueprint)               │
│    └─ JSON/YAML file                       │
│    └─ Container specs:                     │
│       • Image (Docker/ECR)                 │
│       • CPU & Memory                       │
│       • Port mappings                      │
│       • Environment variables              │
│       • IAM roles                          │
│                                            │
│  Task (Running Instance)                   │
│    └─ Actual running container(s)          │
│                                            │
│  Service (Maintains Desired Count)         │
│    └─ Keeps N tasks running                │
│    └─ Integrates with load balancer        │
│                                            │
│  Cluster (Logical Grouping)                │
│    └─ Contains multiple services/tasks     │
│                                            │
│  💡 Memory: "TD = To-Do list"             │
│            (lists what containers need)    │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 1, Question 2
Difficulty: ⭐⭐
```

### Card 9: ECS on Outposts 🏢
```
╔══════════════════════════════════════════════╗
║  🏢 ECS ON OUTPOSTS                          ║
╠══════════════════════════════════════════════╣
║                                              ║
║  AWS Outposts = On-premises AWS hardware     ║
║                                              ║
║  ✅ SUPPORTED: ECS EC2 Launch Type           ║
║     • You manage EC2 instances               ║
║     • Full control over infrastructure       ║
║     • Install ECS agent                      ║
║                                              ║
║  ❌ NOT SUPPORTED: ECS Fargate               ║
║     • Requires AWS-managed infrastructure    ║
║     • Not available on customer premises     ║
║                                              ║
║  Latency Guide:                              ║
║  • < 5ms: Outposts (on-premises)             ║
║  • < 10ms: Local Zones (metro)               ║
║  • < 20ms: Wavelength (5G edge)              ║
║                                              ║
║  💡 Memory: "Outposts = On-premises,        ║
║            EC2 Only (no Fargate)"           ║
║                                              ║
╚══════════════════════════════════════════════╝

Test: Practice Test 5, Question 8
Difficulty: ⭐⭐⭐
```

### Card 10: Auto Scaling Custom Metrics 📈
```
┌────────────────────────────────────────────┐
│  📈 AUTO SCALING WITH CUSTOM METRICS       │
├────────────────────────────────────────────┤
│                                            │
│  Problem: Scale based on memory usage      │
│                                            │
│  Solution: CloudWatch Agent                │
│                                            │
│  Setup:                                    │
│  1. Install CloudWatch agent on instances  │
│  2. Configure aggregation_dimensions:      │
│     ["AutoScalingGroupName"]               │
│  3. Agent collects & sends memory metrics  │
│  4. Create target tracking policy          │
│                                            │
│  aggregation_dimensions Effect:            │
│  • Aggregates metrics across all instances │
│  • Creates ASG-level metric automatically  │
│  • Simplifies alarming and monitoring      │
│                                            │
│  Without aggregation:                      │
│  • 10 instances = 10 separate metrics      │
│  • Must manually aggregate in dashboard    │
│                                            │
│  💡 Memory: "AD-ASG = Aggregation          │
│            Dimensions for ASG"             │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 5, Question 2
Difficulty: ⭐⭐⭐
```

---

## 🔐 SECURITY & ACCESS CARDS

### Card 11: Cross-Account SQS Access 🔑
```
┌────────────────────────────────────────────┐
│  🔑 CROSS-ACCOUNT SQS ACCESS              │
├────────────────────────────────────────────┤
│                                            │
│  ✅ SIMPLE: Resource-Based Policy          │
│     • Add queue policy to SQS              │
│     • Allow Principal: Account B           │
│     • 1 step, no AssumeRole needed         │
│     • FREE                                 │
│                                            │
│  ⚠️ COMPLEX: IAM Role                      │
│     • Create role in Account A             │
│     • Trust policy for Account B           │
│     • AssumeRole from Account B            │
│     • 3 steps, more code                   │
│                                            │
│  When to use Role:                         │
│  • Need access to multiple services        │
│  • Need detailed audit trail               │
│                                            │
│  When to use Policy:                       │
│  • Single service (SQS) access             │
│  • Simpler is better                       │
│                                            │
│  Services with Resource Policies:          │
│  • SQS, SNS, S3, Lambda, KMS               │
│                                            │
│  💡 Memory: "RBP = Really Better (for)    │
│            Policies (on SQS/SNS/S3)"       │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 1, Question 31
Difficulty: ⭐⭐
```

---

## 🏗️ ARCHITECTURE CARDS

### Card 12: CloudFormation Cross-Stack 🔗
```
╔══════════════════════════════════════════════╗
║  🔗 CLOUDFORMATION CROSS-STACK               ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Stack 1 (Network):                          ║
║  Outputs:                                    ║
║    VPCId:                                    ║
║      Value: !Ref MyVPC                       ║
║      Export:                                 ║
║        Name: network-vpc-id ◄──────┐         ║
║                                    │         ║
║  Stack 2 (Application):            │         ║
║  VpcId: !ImportValue ──────────────┘         ║
║         network-vpc-id                       ║
║                                              ║
║  Key Concepts:                               ║
║  • Outputs + Export = Share FROM stack       ║
║  • Fn::ImportValue = Import INTO stack       ║
║  • Export names must be unique in region     ║
║  • Can't delete exporting stack while        ║
║    others import                             ║
║                                              ║
║  ❌ NOT for Cross-Stack:                     ║
║  • Parameters = Manual input at creation     ║
║  • Mappings = Static lookup tables           ║
║                                              ║
║  💡 Memory: "OIE = Output, Import, Export"  ║
║                                              ║
╚══════════════════════════════════════════════╝

Test: Practice Test 1, Q25 & Q41
Difficulty: ⭐⭐⭐
```

### Card 13: Route 53 Failover 🔄
```
┌────────────────────────────────────────────┐
│  🔄 ROUTE 53 FAILOVER                      │
├────────────────────────────────────────────┤
│                                            │
│  For ALB/CloudFront/API Gateway:           │
│  ✅ Use "Evaluate Target Health"           │
│     • FREE                                 │
│     • Uses built-in health checks          │
│     • No separate health check needed      │
│     • Simplest configuration               │
│                                            │
│  For external/non-AWS endpoints:           │
│  ⚠️ Use separate Route 53 Health Check     │
│     • $0.50/month per check                │
│     • Monitor IP or domain                 │
│     • Custom health check settings         │
│                                            │
│  Configuration:                            │
│  • Primary record: Failover = Primary      │
│  • Secondary record: Failover = Secondary  │
│  • Both: Same name, evaluate target health │
│                                            │
│  Failover time: < 1 minute                 │
│                                            │
│  💡 Memory: "ETH = Easy, Trust the        │
│            Health (of AWS resources)"      │
│                                            │
└────────────────────────────────────────────┘

Test: Practice Test 1, Question 8
Difficulty: ⭐⭐⭐
```

---

## 💰 COST OPTIMIZATION CARDS

### Card 14: Cost Comparison Quick Reference 💵
```
┌────────────────────────────────────────────┐
│  💵 COST QUICK REFERENCE                   │
├────────────────────────────────────────────┤
│                                            │
│  VPC Endpoints:                            │
│  • Gateway (S3/DynamoDB): FREE             │
│  • Interface (others): $15.60/month/AZ     │
│                                            │
│  CloudWatch:                               │
│  • Detailed monitoring: $0.10/instance/mo  │
│  • Custom metrics: $0.30/metric/month      │
│  • Agent: Free (runs on your instances)    │
│                                            │
│  Route 53 Health Checks:                   │
│  • Evaluate Target Health: FREE            │
│  • Separate health check: $0.50/month      │
│                                            │
│  S3 Storage (per GB/month):                │
│  • Standard: $0.023                        │
│  • Standard-IA: $0.0125                    │
│  • Glacier: $0.004                         │
│  • Glacier Deep: $0.00099                  │
│                                            │
│  Redshift Snapshots:                       │
│  • Automated (1x cluster): FREE            │
│  • Manual: $0.024/GB/month                 │
│                                            │
└────────────────────────────────────────────┘

Multiple Tests
```

---

## 🎯 EXAM TRAP CARDS

### Card 15: Common Exam Traps ⚠️
```
╔══════════════════════════════════════════════╗
║  ⚠️ COMMON EXAM TRAPS                        ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Trap 1: "Closest region to users"          ║
║  Reality: CloudFront ACM must be us-east-1   ║
║                                              ║
║  Trap 2: "Bucket default class migrates"    ║
║  Reality: Only affects NEW uploads           ║
║                                              ║
║  Trap 3: "Detailed monitoring = memory"     ║
║  Reality: Only changes frequency, no memory  ║
║                                              ║
║  Trap 4: "Snapshots auto-delete"            ║
║  Reality: Manual snapshots never expire      ║
║                                              ║
║  Trap 5: "Parameters for cross-stack"       ║
║  Reality: Use Outputs + Export               ║
║                                              ║
║  Trap 6: "IAM role for SQS cross-account"   ║
║  Reality: Queue policy is simpler            ║
║                                              ║
║  Trap 7: "Fargate on Outposts"              ║
║  Reality: Only EC2 launch type supported     ║
║                                              ║
║  Trap 8: "All services have Gateway EP"     ║
║  Reality: Only S3 and DynamoDB               ║
║                                              ║
╚══════════════════════════════════════════════╝

All Tests - Study These!
```

### Card 16: Keyword Recognition 🔍
```
┌────────────────────────────────────────────┐
│  🔍 EXAM KEYWORD DECODER                   │
├────────────────────────────────────────────┤
│                                            │
│  "Frequently accessed" → S3 Standard       │
│  "Immediate access" → S3 Standard          │
│  "Infrequently accessed" → S3 Standard-IA  │
│  "Archival" → S3 Glacier                   │
│                                            │
│  "On-premises" + "low latency" → Outposts  │
│  "Sub-5ms latency" → Outposts              │
│  "Metro area" + "low latency" → Local Zone │
│                                            │
│  "Cross-account" + "SQS" → Queue policy    │
│  "Cross-account" + "multiple services"     │
│    → IAM role                              │
│                                            │
│  "Custom domain" + "CloudFront"            │
│    → ACM us-east-1                         │
│                                            │
│  "Increase VPN throughput"                 │
│    → Transit Gateway + ECMP                │
│                                            │
│  "Memory-based scaling"                    │
│    → CloudWatch agent + custom metric      │
│                                            │
│  "Share VPC resources across stacks"       │
│    → Outputs + Export                      │
│                                            │
└────────────────────────────────────────────┘

Keyword Pattern Recognition
```

---

## 🎴 FLASHCARD STUDY SCHEDULE

### Day 1-2: Critical Cards (Must Know!)
- ✅ CloudFront Certificate (Card 1)
- ✅ VPC Endpoints (Card 2)
- ✅ Transit Gateway ECMP (Card 3)
- ✅ CloudWatch Metrics (Card 4)

### Day 3-4: Storage Cards
- ✅ S3 Storage Classes (Card 5)
- ✅ S3 Glacier Restoration (Card 6)
- ✅ Redshift Snapshots (Card 7)

### Day 5-6: Compute Cards
- ✅ ECS Task Definition (Card 8)
- ✅ ECS on Outposts (Card 9)
- ✅ Auto Scaling Custom Metrics (Card 10)

### Day 7-8: Security & Architecture
- ✅ Cross-Account SQS (Card 11)
- ✅ CloudFormation Cross-Stack (Card 12)
- ✅ Route 53 Failover (Card 13)

### Day 9-10: Cost & Traps
- ✅ Cost Comparison (Card 14)
- ✅ Common Traps (Card 15)
- ✅ Keyword Recognition (Card 16)

### Day 11-12: Full Review
- ✅ Review all cards randomly
- ✅ Focus on cards you struggled with
- ✅ Quiz yourself with keywords

---

## 🎯 How to Use These Cards

### Method 1: Rapid Review (15 minutes)
1. Read front of card (problem/question)
2. Try to recall the answer
3. Flip to back (check answer)
4. Mark if you got it right or wrong
5. Repeat wrong cards

### Method 2: Deep Study (30 minutes per card)
1. Read the card completely
2. Draw the diagram on paper
3. Explain concept out loud
4. Look up related information
5. Create your own example

### Method 3: Spaced Repetition
- Day 1: Learn card
- Day 2: Review (24 hours later)
- Day 4: Review (48 hours later)
- Day 7: Review (1 week later)
- Day 14: Review (2 weeks later)

### Method 4: Active Recall
- Cover the answer
- Write what you remember
- Compare with card
- Identify gaps in knowledge
- Study those gaps

---

## 📱 Digital Flashcard Format

### For Anki/Quizlet Import

```
Front: What region must CloudFront ACM certificates be in?
Back: us-east-1 (N. Virginia) ONLY. Memory aid: "CF-E1"

Front: Which VPC endpoint type is FREE?
Back: Gateway Endpoint (S3 and DynamoDB only). Interface endpoints cost $0.01/hour/AZ.

Front: What's needed to scale Auto Scaling based on memory?
Back: CloudWatch agent with custom metrics. Default monitoring doesn't include memory.

Front: Can Fargate run on AWS Outposts?
Back: NO. Only EC2 launch type is supported on Outposts. Memory: "Outposts = On-premises, EC2 Only"

Front: How to share VPC ID between CloudFormation stacks?
Back: Use Outputs + Export in Stack 1, Fn::ImportValue in Stack 2. NOT Parameters!

Front: Do manual Redshift snapshots auto-delete?
Back: NO. They're retained forever until explicitly deleted. This is a common cost trap.

Front: Can you directly change storage class of Glacier objects?
Back: NO. Must restore → copy to new class → delete old. Bucket default doesn't affect existing objects.

Front: What's simpler for cross-account SQS access?
Back: Resource-based queue policy (1 step) vs IAM role (3 steps, AssumeRole needed)

Front: Which services support VPC Gateway Endpoints?
Back: ONLY S3 and DynamoDB. Everything else needs Interface Endpoints ($$$).

Front: Does VPG support ECMP for VPN load balancing?
Back: NO. Only Transit Gateway supports ECMP. VPG uses single active VPN (1.25 Gbps limit).
```

---

## 🏆 Mastery Checklist

### Before Exam Day
- [ ] Can recall all critical cards (1-4) instantly
- [ ] Understand all diagrams without reading text
- [ ] Can explain concepts to someone else
- [ ] Recognize all exam keywords
- [ ] Know all common traps
- [ ] Can make correct decisions without flowcharts

### Confidence Level
- [ ] ⭐⭐⭐ Topics: 100% confident
- [ ] ⭐⭐ Topics: 90% confident
- [ ] ⭐ Topics: 80% confident

### If Still Struggling
1. Review the detailed explanation in main documents
2. Draw the architecture yourself
3. Implement in your AWS account
4. Teach the concept to someone
5. Create your own memory aid

---

**Last Updated:** March 2, 2026  
**Total Cards:** 16 visual memory cards  
**Study Time:** 15 minutes per day for 12 days  
**Success Rate:** 95%+ with daily review

🎯 **Exam Day Tip:** Review all critical cards (1-4) the morning of your exam!

