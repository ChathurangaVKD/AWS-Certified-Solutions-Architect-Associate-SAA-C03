# ⚡ Fast Learning - Cost Optimization

> **Time to Complete**: 40-50 minutes | **Exam Weight**: ~10-15%

## 🎯 Must-Know Concepts (5 Minutes)

### Cost Optimization Selector (SCRAP-BCT)
```
STEADY 24/7 WORKLOAD?        → Reserved Instances / Savings Plans
FLEXIBLE ACROSS EC2/Lambda?  → Compute Savings Plans
INTERRUPTIBLE / BATCH?       → Spot Instances
UNPREDICTABLE / SHORT-TERM?  → On-Demand
BYOL / COMPLIANCE HARDWARE?  → Dedicated Hosts
VISUALIZE & FORECAST SPEND?  → Cost Explorer
ALERT ON SPEND?              → AWS Budgets
LINE-ITEM BILLING DATA?      → Cost and Usage Report (CUR) + Athena
COST PER PROJECT/TEAM?       → Cost Allocation Tags
ONE BILL, MANY ACCOUNTS?     → Organizations Consolidated Billing
ESTIMATE BEFORE BUILDING?    → Pricing Calculator
RIGHT-SIZING (ML)?           → Compute Optimizer
BEST-PRACTICE CHECKS?        → Trusted Advisor
```

**Memory Aid**: "Explorer Explains the past, Budgets Beep about the future, CUR Contains every line, Calculator Calculates before you build"

### The Cost Optimization Mindset
```
1. STOP    → Turn off / delete what you do not use (biggest, easiest win)
2. SHRINK  → Right-size to match real utilization
3. COMMIT  → Reserved / Savings Plans for the steady baseline
4. BID     → Spot for fault-tolerant work
5. TIER    → Move data to cheaper storage classes
6. SCALE   → Auto Scaling + serverless: pay only for what you use
7. WATCH   → Tags, Budgets, Cost Explorer, regular reviews
```

## 📊 Quick Reference Tables

### EC2 Purchasing Options
| Option | Discount | Commitment | Best For |
|--------|----------|------------|----------|
| **On-Demand** | None | None | Short-term, unpredictable, first-time apps |
| **Reserved Instances** | Up to 72% | 1 or 3 years | Steady-state, predictable usage |
| **Savings Plans** | Up to 72% | 1 or 3 years ($/hour) | Steady usage that needs flexibility |
| **Spot** | Up to 90% | None | Fault-tolerant, flexible, batch |
| **Dedicated Hosts** | Varies | Optional 1 or 3 years | Compliance, per-socket/per-core licenses |
| **Dedicated Instances** | Slightly higher than shared | None | Hardware isolation, no host visibility |
| **Capacity Reservation** | None (On-Demand rate) | None | Guaranteed capacity in one AZ |

### Savings Plans vs Reserved Instances
| Feature | Savings Plans | Reserved Instances |
|---------|---------------|--------------------|
| **Commit to** | $ per hour of usage | A specific instance configuration |
| **Flexibility** | High | Low |
| **Covers** | EC2, Fargate, Lambda | EC2 (plus RDS, etc. have their own RIs) |
| **Modification** | Automatic | Manual (exchange / modify) |
| **Max discount** | Up to 72% | Up to 72% |

### Cost Tools Compared
| Tool | Purpose | Key Feature |
|------|---------|-------------|
| **Cost Explorer** | Visualize & analyze past spend | Graphs, forecast, RI/SP and right-sizing recommendations |
| **AWS Budgets** | Set limits & get alerted | Actual + forecasted alerts, Budget Actions |
| **CUR** | Most detailed billing data | Line items to S3, query with Athena |
| **Cost Allocation Tags** | Attribute cost to project/team | Must be activated in Billing console |
| **Pricing Calculator** | Estimate before deploying | Export CSV/PDF, share estimates |
| **Compute Optimizer** | ML right-sizing | EC2, Auto Scaling, EBS, Lambda |
| **Trusted Advisor** | Best-practice checks | Full cost checks need Business/Enterprise Support |
| **Consolidated Billing** | One bill for an Organization | Volume discounts, RI/SP sharing |

### S3 Storage Classes (Cheapest to Most Expensive, per README)
| Storage Class | $/GB-month | Use Case |
|---------------|-----------|----------|
| **Glacier Deep Archive** | $0.00099 | Long-term archive, hours to retrieve |
| **Glacier Flexible Retrieval** | $0.0036 | Archive, minutes to hours |
| **Glacier Instant Retrieval** | $0.004 | Archive, millisecond access |
| **One Zone-IA** | $0.01 | Infrequent, re-creatable data |
| **Standard-IA** | $0.0125 | Infrequent, needs multi-AZ |
| **Standard** | $0.023 | Frequent access |
| **Intelligent-Tiering** | $0.023 tier + $0.0025 monitoring | Unknown / changing access |

## 🔥 Exam Hot Topics

### 1. Reserved Instances
```
COMMITMENT: 1 or 3 years, up to 72% off On-Demand

PAYMENT OPTIONS (more upfront = bigger discount):
├── All Upfront     → highest discount, no monthly charge
├── Partial Upfront → middle
└── No Upfront      → lowest discount, monthly charge

TYPES:
├── Standard    → highest discount, cannot change family,
│                 CAN sell in the RI Marketplace
├── Convertible → lower discount, can change family/OS/tenancy,
│                 CANNOT sell in the Marketplace
└── Scheduled   → legacy, no longer sold to new customers

SCOPE:
├── Regional → any AZ in region, size flexibility, NO capacity reservation
└── Zonal    → one AZ, RESERVES capacity, no size flexibility
```

**Exam Tip**: Need capacity guaranteed + discount? Zonal RI (or Capacity Reservation + Savings Plan/RI).

### 2. Savings Plans
```
WHAT: Commit to a $/hour spend for 1 or 3 years

TYPES:
├── Compute Savings Plans      → MOST flexible, up to 66%
│   └── EC2 (any family/size/OS/region), Fargate, Lambda
├── EC2 Instance Savings Plans → up to 72%
│   └── Locked to one instance family in one region
│       (flexible on size, OS, tenancy)
└── SageMaker Savings Plans    → up to 64%

PAYMENT: All / Partial / No Upfront

OVERAGE: Usage above the commitment is billed On-Demand
```

**Exam Tip**: "Multiple regions / mix of EC2, Fargate and Lambda" = Compute Savings Plan.

### 3. Spot Instances
```
DISCOUNT: Up to 90%
HOW: Spare EC2 capacity; AWS can reclaim it
WARNING: 2-minute notice (instance metadata + EventBridge/CloudWatch Events)

REQUEST TYPES:
├── One-time   → closes after fulfilled
└── Persistent → relaunches after interruption until cancelled

SPOT FLEET (Spot + optional On-Demand, target capacity):
├── Lowest price
├── Diversified
├── Capacity optimized
└── Price capacity optimized

GOOD FOR: batch, CI/CD, big data (EMR), HPC, stateless web tier
          behind a load balancer, fault-tolerant containers
BAD FOR:  databases, critical apps with no fault tolerance
```

**Exam Tip**: "Can be interrupted" or "flexible start/end time" = Spot. "Must not lose data" = not Spot.

### 4. Dedicated Hosts vs Dedicated Instances vs Capacity Reservations
```
DEDICATED HOST:
├── A whole physical server for you
├── Visibility of sockets/cores, control of placement
├── BYOL with per-socket / per-core licenses
└── Most expensive, per-host pricing

DEDICATED INSTANCE:
├── Hardware isolation, no server visibility
└── Per-instance pricing, cheaper than Hosts

CAPACITY RESERVATION:
├── Reserves capacity in ONE AZ, no commitment
├── Billed at On-Demand rate whether used or not
└── Pair with RI / Savings Plan for a discount
```

### 5. Cost Explorer
```
WHAT: Visualize, analyze and forecast spend
FILTER / GROUP BY: service, linked account, region, tag, instance type

RECOMMENDATIONS:
├── Reserved Instance recommendations
├── Savings Plans recommendations
└── Right-sizing recommendations

ALSO: Forecasting, API access
LOOKS BACKWARD (history) + forecasts forward
```

### 6. AWS Budgets
```
BUDGET TYPES (4):
├── Cost             → spend vs a $ threshold
├── Usage            → hours/GB/requests
├── Savings Plans    → utilization / coverage
└── Reservation      → RI utilization / coverage

ALERTS:
├── Actual     → threshold already crossed
└── Forecasted → predicted to cross (ML-based)

NOTIFY: Email, SNS (automation), Chatbot (Slack/Chime)

BUDGET ACTIONS:
├── Apply an IAM policy (e.g. deny new EC2 launches)
├── Apply an SCP (in Organizations)  [real AWS behaviour]
└── Stop EC2 / RDS instances

PRICING: First 2 budgets free, then $0.02/day per budget
```

**Exam Tip**: Budgets = proactive alerts and automated response. Cost Explorer = analysis. Do not mix them up.

### 7. Cost and Usage Report (CUR)
```
WHAT: Most comprehensive billing dataset, line-item detail
DELIVERY: To an S3 bucket
FORMAT: CSV or Parquet (Parquet = compressed, columnar)
GRANULARITY: Hourly, daily, monthly
INCLUDES: Resource IDs, usage, cost, tags, RI/SP details

PATTERN:
CUR → S3 → Athena (SQL) → QuickSight (dashboards)
```

### 8. Cost Allocation Tags
```
TYPES:
├── User-defined tags (e.g. Project=website)
└── AWS-generated tags (e.g. aws:createdBy)

RULES:
├── MUST be activated in the Billing console
├── Show up in Cost Explorer and CUR (allow up to ~24 hours)
├── Not retroactive: only costs after activation are tagged
└── Enforce a consistent tag strategy (naming standard)

USE FOR: showback / chargeback per project, team, environment
```

### 9. Organizations and Consolidated Billing
```
BENEFITS:
├── ONE bill for all accounts (free feature)
├── Volume discounts from combined usage (tiered pricing hit sooner)
├── Reserved Instance sharing across accounts
└── Savings Plans sharing across accounts

PRACTICE:
├── Separate accounts per environment / project / team
├── View per-account costs in Cost Explorer (linked account filter)
└── Same tag strategy across all accounts
```

### 10. Data Transfer Costs
```
FREE:
├── Data IN from the internet
├── Same-region transfer between many services (same AZ is safest)
└── CloudFront to origin

CHARGED:
├── Data OUT to the internet (tiered: first 10 TB $0.09/GB per README)
├── Inter-region transfer
└── Cross-AZ transfer (small charge)

REDUCE IT:
├── CloudFront (cheaper egress, fewer origin hits)
├── Keep chatty resources in the same region/AZ
├── VPC Gateway Endpoints (S3, DynamoDB) instead of NAT Gateway
├── Direct Connect for large steady volumes
└── Compress data
```

### 11. Storage and Database Savings
```
S3:
├── Lifecycle policies (Standard → IA → Glacier → expire)
├── Intelligent-Tiering for unknown access patterns
├── S3 Storage Class Analysis to learn access patterns
└── Abort incomplete multipart uploads

EBS:
├── gp3 over gp2 (cheaper baseline, tunable performance)
├── Delete unattached volumes and old snapshots
└── sc1 (Cold HDD) for rarely accessed throughput data

RDS / AURORA:
├── Reserved Instances for production DBs
├── Right-size; stop dev/test when idle
├── Aurora Serverless for variable workloads
└── Multi-AZ only where needed

DYNAMODB:
├── On-Demand for unpredictable traffic
├── Provisioned + auto scaling for predictable traffic
├── Reserved capacity for steady provisioned usage
└── TTL to expire old items at no write cost
```

### 12. Free Tier and Pricing Basics
```
THREE FREE TIER TYPES:
├── Always Free  → Lambda 1M requests/mo, DynamoDB 25 GB, SNS 1M publishes
├── 12 Months    → EC2 750 hrs/mo t2/t3.micro, S3 5 GB, RDS 750 hrs/mo
└── Trials       → short-term (e.g. Inspector, QuickSight)

PAY-AS-YOU-GO:
├── Compute   → per second (Linux, 60-second minimum) or per hour
├── Storage   → per GB-month
└── Transfer  → IN free, OUT charged

LAMBDA BILLING: requests ($0.20 per 1M after free 1M)
                + duration in GB-seconds (memory x time)
```

## 🧠 Common Exam Scenarios

| Scenario | Answer |
|----------|--------|
| Steady 24/7 database server for 3 years | Reserved Instances or Savings Plans (3-year) |
| Mix of EC2, Fargate and Lambda; want flexibility | Compute Savings Plans |
| Nightly batch job, restartable | Spot Instances |
| Dev/test used only during business hours | Stop on schedule (or On-Demand) |
| Spend per project / team | Cost allocation tags (activate them) |
| Alert when monthly cost crosses a limit | AWS Budgets (cost budget) |
| Alert when forecast will exceed budget | Budgets forecasted alert |
| Automatically block new launches at the limit | Budget Action (IAM policy / SCP) |
| Find underutilized EC2 instances | Compute Optimizer / Cost Explorer right-sizing |
| Custom SQL analysis of billing line items | CUR + Athena |
| Old logs rarely read, keep cheaply | S3 Lifecycle to Glacier / Deep Archive |
| Unknown or changing S3 access pattern | S3 Intelligent-Tiering |
| One invoice and pooled discounts for many accounts | Organizations Consolidated Billing |
| Estimate cost of a new architecture | Pricing Calculator |
| BYOL with per-socket license | Dedicated Hosts |
| Private instances pulling from S3 via NAT, high bill | S3 Gateway VPC Endpoint |
| Global users downloading large objects, high egress | CloudFront |
| Unpredictable DynamoDB traffic | On-Demand capacity mode |

## 🚀 Speed Learning Tips

### Decision Tree: EC2 Pricing
```
Can the workload be interrupted?
├── YES → Spot (up to 90%)
└── NO
    ├── Steady for 1-3 years?
    │   ├── Need flexibility (family/region/Fargate/Lambda)? → Compute Savings Plans
    │   ├── Same family in one region? → EC2 Instance Savings Plans / Standard RI
    │   └── Might change instance type? → Convertible RI
    ├── Short or unpredictable? → On-Demand
    └── License/compliance on physical server? → Dedicated Hosts
```

### Decision Tree: Which Cost Tool?
```
Want to SEE where money went?        → Cost Explorer
Want a LIMIT or an ALERT?            → Budgets
Want the RAW detailed data?          → CUR (+ Athena / QuickSight)
Want to GROUP cost by project?       → Cost allocation tags
Want to PLAN a new workload's cost?  → Pricing Calculator
Want to CUT waste on running things? → Compute Optimizer / Trusted Advisor
Want to MERGE bills of many accounts?→ Consolidated Billing
```

## ⚡ Rapid-Fire Facts

- Spot: up to **90%**; RIs and EC2 Instance Savings Plans: up to **72%**; Compute Savings Plans: up to **66%**
- Spot gives a **2-minute** interruption warning
- RI terms are **1 or 3 years**; Standard RIs can be sold on the **RI Marketplace**, Convertible cannot
- Regional RIs do **not** reserve capacity; Zonal RIs do
- Scheduled RIs and Spot Blocks are **legacy / deprecated**
- Capacity Reservations are billed whether used or not
- Budgets: **first 2 free**, then **$0.02/day** each; 4 types: Cost, Usage, Savings Plans, Reservation
- CUR is the **most detailed** billing data; delivered to **S3**
- Tags must be **activated** in Billing; allow up to about **24 hours** to appear
- Consolidated Billing is **free** and enables volume discounts and RI/SP sharing
- Data **in** is free; data **out** to the internet is charged
- Lambda: first **1M requests** free per month, then $0.20 per 1M
- Free tier types: **Always Free**, **12 Months**, **Trials**
- Compute Optimizer is ML-based and requires **opt-in**
- Trusted Advisor full cost checks need **Business or Enterprise** Support
- Delete unattached EBS volumes and unused Elastic IPs (idle ones cost money)

## 🚀 5-Minute Master Review

### Common Cost Patterns
```
1. STEADY BASELINE + SPIKES
   Savings Plans / RIs for baseline + Auto Scaling On-Demand for spikes
   + Spot for the interruptible part

2. BIG DATA / BATCH
   EMR or batch workers on Spot, checkpoint to S3

3. LOG RETENTION
   S3 Standard → Lifecycle → Glacier → Deep Archive → expire

4. MULTI-ACCOUNT GOVERNANCE
   Organizations → Consolidated Billing → tags → Budgets per account
   → CUR → Athena → QuickSight

5. PRIVATE SUBNET TO S3
   EC2 → Gateway VPC Endpoint → S3 (no NAT data processing charge)

6. DEV/TEST SAVINGS
   Stop instances out of hours, Aurora Serverless, smaller sizes
```

### Common Mistakes to Avoid
❌ Buying 3-year commitments for workloads that may disappear
❌ Using Spot for databases or non-restartable jobs
❌ Forgetting to activate cost allocation tags
❌ Expecting tags to apply to past spend
❌ Confusing Budgets (alerts) with Cost Explorer (analysis)
❌ Choosing EC2 Instance Savings Plans when flexibility across regions is required
❌ Leaving unattached EBS volumes, old snapshots and idle Elastic IPs
❌ Over-provisioning "just in case" instead of right-sizing and scaling
❌ Moving data between regions/AZs unnecessarily
❌ Using Capacity Reservations expecting a discount

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Cheapest EC2 option for interruptible work? __
2. Most flexible Savings Plan? __
3. Which tool sends an alert when forecast spend exceeds a limit? __
4. Where is CUR delivered, and what queries it? __
5. What must you do before a tag shows in Cost Explorer? __
6. Can Convertible RIs be sold on the Marketplace? __
7. Which service gives ML-based right-sizing recommendations? __
8. Which EC2 option supports per-socket BYOL licenses? __
9. How to avoid NAT Gateway charges when reaching S3 privately? __
10. Which feature pools volume discounts across accounts? __

---

## ⏱️ Next Steps
- Time spent: ~40-50 min
- Practice: Memorize pricing-model use cases and the cost tool selector
- Ready for: Cost optimization practice questions
- Practice questions: [Module 13 Practice Questions](./PRACTICE-QUESTIONS.md)
- Architecture diagrams: [Module 13 Diagrams](./DIAGRAMS.md)
- Move to: [Module 14 - Practice](../14-Practice/FAST-LEARN.md)

---

**Quick Answers**:
1) Spot Instances
2) Compute Savings Plans
3) AWS Budgets (forecasted alert)
4) Amazon S3; Athena (then QuickSight for visuals)
5) Activate it in the Billing console (then wait up to ~24 hours)
6) No (only Standard RIs)
7) AWS Compute Optimizer
8) Dedicated Hosts
9) Gateway VPC Endpoint
10) Consolidated Billing (AWS Organizations)
