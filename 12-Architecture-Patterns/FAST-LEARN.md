# ⚡ Fast Learning - Architecture Patterns

> **Time to Complete**: 60-75 minutes | **Exam Weight**: ~25-30%

## 🎯 Must-Know Concepts (5 Minutes)

### Architecture Pattern Selector (WMSEDCS)
```
WEB APP, CLASSIC?        → 3-Tier (ALB + EC2 Auto Scaling + RDS Multi-AZ)
NO SERVERS, SPIKY LOAD?  → Serverless (API Gateway + Lambda + DynamoDB)
LOOSE COUPLING?          → Event-driven / queues (SQS, SNS, EventBridge)
INDEPENDENT TEAMS?       → Microservices (ECS/EKS/Lambda + Cloud Map)
SURVIVE AZ FAILURE?      → Multi-AZ (RDS Multi-AZ, ELB, Auto Scaling)
SURVIVE REGION FAILURE?  → Multi-Region + DR strategy (Route 53 failover)
SLOW / HEAVY READS?      → Caching (CloudFront, ElastiCache, DAX)
SECURITY?                → Defense in depth (WAF > SG/NACL > IAM > KMS)
```

**Memory Aid**: "Web tiers, Microservices split, Serverless scales, Events decouple, Duplicate for DR, Cache for speed, Secure every layer"

### The Golden Rules of Architecture Questions
```
1. Find the KEYWORD in the requirement:
   "least operational overhead" → managed / serverless
   "highly available"           → Multi-AZ + Auto Scaling + ELB
   "decouple" / "buffer"        → SQS (or SNS / EventBridge)
   "lowest cost"                → Spot, Reserved, Savings Plans, lifecycle
   "lowest latency globally"    → CloudFront / Global Accelerator / Global DB
   "minimal downtime DR"        → Warm Standby / Multi-Site
2. Eliminate answers with a single point of failure
3. Eliminate answers that need manual steps when automation exists
4. Pick the MOST managed option that still meets the requirement
```

## 📊 Quick Reference Tables

### Six Pillars of the Well-Architected Framework
| Pillar | Core Idea | Key Services |
|--------|-----------|--------------|
| **Operational Excellence** | Run & monitor, improve continuously | CloudFormation, CDK, CloudWatch, CI/CD |
| **Security** | Protect data & systems | IAM, KMS, GuardDuty, CloudTrail, Config |
| **Reliability** | Recover from failure, meet demand | Multi-AZ, Auto Scaling, Route 53, backups |
| **Performance Efficiency** | Right resource for the job | Right instance types, CloudFront, serverless |
| **Cost Optimization** | Avoid unneeded spend | Cost Explorer, Budgets, Savings Plans, Spot |
| **Sustainability** | Minimize environmental impact | Managed services, Auto Scaling, fewer idle resources |

**Memory Aid**: "**O**ften **S**ecure **R**eliable **P**ipelines **C**ost **S**ustainably" (O-S-R-P-C-S)

### Compute / Database / Storage / Integration Choice
| Need | Pick | Why |
|------|------|-----|
| Full OS control | **EC2** | Custom OS, licensing, special hardware |
| Event-driven, short tasks (< 15 min) | **Lambda** | No servers, pay per use |
| Containers you manage | **ECS / EKS** | Microservices, portability (EKS = Kubernetes) |
| Containers without servers | **Fargate** | Serverless containers |
| Relational + ACID | **RDS / Aurora** | SQL, transactions |
| NoSQL, serverless, huge scale | **DynamoDB** | Single-digit ms, scales automatically |
| In-memory cache | **ElastiCache** | Offload DB reads |
| Analytics / warehouse | **Redshift** | OLAP |
| Objects / static content | **S3** | Durable, cheap, static website hosting |
| Block storage for one EC2 | **EBS** | Boot / data volumes |
| Shared file system | **EFS** | Many instances, Linux |
| Windows / HPC file system | **FSx** | SMB / Lustre |
| Synchronous call | **API Gateway / ALB** | Request-response |
| Asynchronous | **SQS / SNS / EventBridge** | Decoupled |
| Streaming | **Kinesis / MSK** | Real-time data |

### SQS vs SNS vs EventBridge vs Kinesis
| Service | Model | Consumers | Typical Use |
|---------|-------|-----------|-------------|
| **SQS** | Queue (pull) | One consumer group per message | Buffer / decouple, worker fleets |
| **SNS** | Pub/Sub (push) | Many subscribers (fan-out) | Notify multiple systems at once |
| **EventBridge** | Event bus with rules | Many targets, filters | AWS / SaaS / custom events, automation |
| **Kinesis** | Stream | Many consumers re-reading same data | Real-time, ordered per shard/partition |

## 🔥 Exam Hot Topics

### 1. Classic 3-Tier Architecture
```
Users → Route 53 → CloudFront
              ↓
        ALB (PUBLIC subnets)
              ↓
   EC2 Auto Scaling Group (PRIVATE subnets, 2+ AZs)
              ↓
   RDS Multi-AZ + Read Replicas (PRIVATE subnets)
   + ElastiCache to reduce DB load

TIERS:
├── Presentation: Route 53, CloudFront, ALB
├── Application:  EC2 Auto Scaling (private)
└── Data:         RDS / Aurora (private)

BEST PRACTICES:
├── Deploy across multiple AZs
├── Auto Scaling for elasticity
├── Caching layer in front of the database
├── Only the ALB is internet-facing
└── Security Groups reference each other (ALB SG → App SG → DB SG)
```

**Exam Tip**: Web servers and databases belong in PRIVATE subnets; only the load balancer is public. Read Replicas = read SCALING, Multi-AZ = availability.

### 2. Serverless Architecture
```
Users → CloudFront + S3 (static site)
              ↓
        API Gateway (REST / WebSocket)
              ↓
          Lambda
         ↙      ↘
  DynamoDB       S3

EXTRAS:
├── Cognito: user sign-up / authentication
├── Step Functions: orchestrate multi-step workflows
├── X-Ray: tracing
└── CloudWatch: logs and metrics

BENEFITS:
├── No server management
├── Automatic scaling
├── Pay per use (no idle cost)
├── High availability built in
└── Lowest operational overhead

USE CASES: web apps, mobile backends, APIs, file processing, stream processing
```

**Exam Tip**: "Unpredictable traffic" + "least operational overhead" + "pay per use" = Serverless (API Gateway + Lambda + DynamoDB).

### 3. Event-Driven Architecture
```
PRODUCERS (S3, DynamoDB, IoT, custom apps)
        ↓
EVENT BUS / QUEUE / STREAM (EventBridge, SNS, SQS, Kinesis)
        ↓
CONSUMERS (Lambda, ECS, EC2)

THREE CORE PATTERNS:
├── Pub/Sub (SNS):   1 message → many subscribers (fan-out)
├── Queue (SQS):     producer → queue → consumer polls (buffer)
└── Stream (Kinesis): ordered records, many consumers read same stream

COMMON EVENT SOURCES:
├── S3 events (object created / deleted)
├── DynamoDB Streams (table changes)
├── Kinesis (real-time streams)
└── EventBridge (AWS services, SaaS, custom apps)
```

**Fan-out pattern (very common)**:
```
Application → SNS Topic → [SQS Queue 1, SQS Queue 2, Lambda]
```

**Exam Tip**: "Send one event to multiple consumers" = SNS fan-out to SQS. "Handle bursts without losing work" = SQS in front of the consumers.

### 4. Microservices Architecture
```
API Gateway / ALB
   ↓       ↓       ↓
 User    Order    Payment      ← each service: own compute + own data store
 (Lambda) (ECS)   (Lambda)
   ↓       ↓       ↓
DynamoDB  Aurora  DynamoDB

TOOLS:
├── Compute: Lambda, ECS, EKS, Fargate
├── API: API Gateway, ALB
├── Discovery: AWS Cloud Map, ECS Service Discovery
├── Communication: SQS, SNS, EventBridge
├── Orchestration: Step Functions
└── Monitoring: CloudWatch, X-Ray

BENEFITS: independent deployment, fault isolation, per-service scaling, team autonomy
```

### 5. High Availability (Multi-AZ vs Multi-Region)
```
MULTI-AZ (survive a data-center failure):
├── RDS Multi-AZ: automatic failover to standby
├── ELB: spreads traffic across AZs, health checks
├── Auto Scaling: launches / replaces instances in several AZs
└── S3: 11 nines durability, data stored across multiple AZs

MULTI-REGION (survive a regional failure / go global):
├── Route 53: failover, latency, weighted routing
├── Global Accelerator: static anycast IPs
├── DynamoDB Global Tables: multi-Region active-active
├── Aurora Global Database: < 1 second replication lag
└── CloudFront: edge locations worldwide

ACTIVE-ACTIVE: all sites serve traffic (Route 53 weighted / latency)
ACTIVE-PASSIVE: standby site waits (Route 53 failover routing)
```

**Exam Tip**: Multi-AZ = high availability inside a Region. Multi-Region = disaster recovery or global users.

### 6. Disaster Recovery Strategies
```
COST / SPEED LADDER (cheap + slow → expensive + fast):

BACKUP & RESTORE   → RPO hours,   RTO hours-days   | $
PILOT LIGHT        → RPO minutes, RTO hours        | $$
WARM STANDBY       → RPO seconds, RTO minutes      | $$$
MULTI-SITE ACTIVE  → RPO ~zero,   RTO ~zero        | $$$$

WHAT RUNS IN THE DR REGION:
├── Backup & Restore: nothing; backups in S3 / Glacier
├── Pilot Light:      core only (e.g., replicated database), compute OFF
├── Warm Standby:     full stack at REDUCED capacity, ready to scale
└── Multi-Site:       full production capacity, serving traffic

DR TOOLS:
├── AWS Backup: centralized backups
├── S3 Cross-Region Replication
├── RDS Read Replicas (can be promoted)
├── Aurora Global Database (< 1 sec lag)
├── DynamoDB Global Tables
├── Route 53 failover routing
└── CloudFormation: rebuild infrastructure fast
```

**Memory Aid**: "**B**ig **P**anic? **W**ait, **M**ove!" → Backup, Pilot, Warm, Multi-site (left = cheapest/slowest, right = priciest/fastest)

**RPO vs RTO**:
```
RPO = how much DATA you can lose  (time between last backup and failure)
RTO = how much TIME to be back up (time from failure to recovery)
```

### 7. Caching Layers
```
User → CloudFront (edge) → API Gateway (API cache) → App
     → ElastiCache / DAX (in-memory) → Database

LAYER 1: CloudFront     → static content at edge, default TTL 24 hours
LAYER 2: API Gateway    → cache API responses
LAYER 3: ElastiCache    → cache DB query results, sub-millisecond
LAYER 4: DAX            → DynamoDB-only cache, microsecond reads

BEST PRACTICES:
├── Cache at multiple layers
├── Set sensible TTLs
├── Plan invalidation
├── Cache-aside (lazy loading) pattern
└── Monitor cache hit rate
```

**Exam Tip**: DynamoDB reads slow? DAX. Relational DB reads slow? ElastiCache. Global static content? CloudFront.

### 8. Defense in Depth
```
EDGE:        CloudFront, WAF, Shield
NETWORK:     VPC, public/private subnets, NACLs, Security Groups
APPLICATION: IAM, Cognito
DATA:        KMS encryption at rest, TLS in transit

PRINCIPLES:
├── Least privilege (IAM)
├── Encrypt at rest and in transit
├── Isolate with private subnets
├── Monitor: CloudTrail, GuardDuty, Config
└── Automate response: EventBridge + Lambda
```

## 💡 Common Exam Scenarios

### Scenario 1: Global Static Website
**Q**: Low-latency static site for worldwide users, minimal ops
**✅ ANSWER**: S3 static hosting + CloudFront

### Scenario 2: Unpredictable API Traffic
**Q**: Spiky API traffic, pay only for usage, no servers
**✅ ANSWER**: API Gateway + Lambda + DynamoDB

### Scenario 3: Absorb Traffic Spikes
**Q**: Web tier overwhelms the order-processing tier during sales
**✅ ANSWER**: Put an SQS queue between tiers; Auto Scaling consumers scale on queue depth

### Scenario 4: Notify Many Systems
**Q**: One order event must trigger billing, shipping and analytics independently
**✅ ANSWER**: SNS topic fanning out to SQS queues (or Lambda) per consumer

### Scenario 5: Survive an AZ Outage
**Q**: Web app must stay up if one Availability Zone fails
**✅ ANSWER**: ALB + Auto Scaling group across 2+ AZs + RDS Multi-AZ

### Scenario 6: Cheap DR
**Q**: Non-critical app, DR must be as cheap as possible, hours of downtime OK
**✅ ANSWER**: Backup and Restore (backups to S3, restore on demand)

### Scenario 7: Near-Zero Downtime DR
**Q**: Mission-critical, RTO and RPO near zero
**✅ ANSWER**: Multi-Site active-active (Route 53 + Aurora Global / DynamoDB Global Tables)

### Scenario 8: DynamoDB Read Latency
**Q**: Read-heavy DynamoDB table needs microsecond latency
**✅ ANSWER**: DynamoDB Accelerator (DAX)

### Scenario 9: Cheap Overnight Batch
**Q**: Fault-tolerant overnight data processing, minimize cost
**✅ ANSWER**: Spot Instances (up to 90% savings), S3 storage, Step Functions for workflow

## 🎓 Speed Learning Tips

### Decision Tree: Which Architecture?
```
1. Do you want to manage servers?
   NO  → Serverless (Lambda, Fargate, DynamoDB)
   YES → EC2 Auto Scaling behind ALB

2. Do components need to scale independently?
   YES → Decouple with SQS / SNS / EventBridge
         (or microservices)

3. Availability requirement?
   One AZ failure     → Multi-AZ
   One Region failure → Multi-Region + DR strategy

4. DR budget vs recovery time?
   Cheapest, slow     → Backup & Restore
   Core always on     → Pilot Light
   Minutes, reduced   → Warm Standby
   Instant, full      → Multi-Site

5. Reads too slow?
   DynamoDB           → DAX
   RDS / Aurora       → ElastiCache or Read Replicas
   Static / global    → CloudFront
```

### Read Replicas vs Multi-AZ
```
RDS MULTI-AZ:
├── Purpose: HIGH AVAILABILITY
├── Standby is NOT used for reads (in a standard Multi-AZ instance)
├── Automatic failover
└── Synchronous replication

RDS READ REPLICA:
├── Purpose: READ SCALING (and DR via promotion)
├── Serves read traffic
├── Asynchronous replication
└── Can be cross-Region
```

## 📝 Rapid-Fire Facts

### Well-Architected Design Principles
```
├── Stop guessing capacity (Auto Scaling)
├── Test at production scale (cheap in the cloud)
├── Automate (IaC, CI/CD)
├── Allow evolutionary architectures
├── Drive architectures using data
├── Improve through game days
└── Design for failure ("everything fails, all the time")
```

### Key Numbers
```
Lambda max run time:        15 minutes
S3 durability:              99.999999999% (11 nines)
Aurora Global DB lag:       typically < 1 second
CloudFront default TTL:     24 hours
Spot savings:               up to ~90%
ElastiCache latency:        sub-millisecond
DAX latency:                microseconds
```

### Pattern Cheat Sheet
| Pattern | Core Services | Remember |
|---------|---------------|----------|
| 3-Tier | Route 53, ALB, EC2 ASG, RDS | Public ALB, private app + data |
| Serverless | S3, API Gateway, Lambda, DynamoDB | No servers, pay per use |
| Fan-out | SNS → SQS | One event, many consumers |
| Buffering | SQS + Auto Scaling | Queue depth drives scaling |
| Microservices | ECS/EKS/Lambda + Cloud Map | Independent deploy and scale |
| Active-Passive | Route 53 failover | Standby Region waits |
| Active-Active | Route 53 weighted/latency | Both Regions serve traffic |
| Big data pipeline | Kinesis → Lambda/Analytics → S3 → Athena → QuickSight | Ingest, process, store, query, visualize |
| Video streaming | S3 + CloudFront + MediaConvert + Cognito | Signed URLs restrict access |
| E-commerce | CloudFront/S3, API Gateway/Lambda, DynamoDB + RDS, OpenSearch, ElastiCache | Right DB per job |

## 🚀 5-Minute Master Review

### The 6 Things to Remember
```
1. 6 PILLARS: Ops Excellence, Security, Reliability, Performance,
              Cost, Sustainability
2. 3-TIER: public ALB → private EC2 ASG → private RDS Multi-AZ
3. SERVERLESS: API Gateway + Lambda + DynamoDB (least ops)
4. DECOUPLE: SQS (queue), SNS (fan-out), EventBridge (event rules),
             Kinesis (stream)
5. DR LADDER: Backup & Restore → Pilot Light → Warm Standby → Multi-Site
6. CACHE: CloudFront (edge) → ElastiCache (app/DB) → DAX (DynamoDB)
```

### Common Mistakes to Avoid
❌ Choosing Multi-AZ when the question needs Multi-Region (or the reverse)
❌ Using Read Replicas for high availability (that is Multi-AZ)
❌ Picking Multi-Site DR when "cost-effective" is the requirement
❌ Putting EC2 or databases in public subnets
❌ Tightly coupling tiers instead of using a queue
❌ Using ElastiCache when the question says DynamoDB and microsecond (DAX)
❌ Running Lambda for jobs that exceed 15 minutes
❌ Ignoring the words "least operational overhead" (choose managed/serverless)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Which pillar covers IaC and post-incident learning? __
2. Which DR strategy keeps only core services like a replicated database running? __
3. Service that fans one message out to many subscribers? __
4. Cache designed specifically for DynamoDB? __
5. Where should EC2 application servers live in a 3-tier design? __
6. Which RDS feature gives automatic failover, Multi-AZ or Read Replica? __
7. Cheapest DR strategy? __
8. Maximum Lambda execution time? __
9. Tool for service discovery between microservices? __
10. Database offering < 1 second cross-Region replication lag? __

## ⏱️ Next Steps
- Time spent: ~60-75 min
- Practice: Sketch a 3-tier and a serverless design from memory, then label the DR ladder
- Ready for: [Architecture Patterns practice questions](./PRACTICE-QUESTIONS.md)
- Review visuals: [Architecture Patterns diagrams](./DIAGRAMS.md)
- Move to: [Module 13 - Cost Optimization](../13-Cost-Optimization/README.md)

---

**Quick Answers**: 
1) Operational Excellence
2) Pilot Light
3) Amazon SNS (pub/sub fan-out)
4) DAX (DynamoDB Accelerator)
5) Private subnets, in an Auto Scaling group across multiple AZs
6) Multi-AZ (Read Replicas are for read scaling)
7) Backup and Restore
8) 15 minutes
9) AWS Cloud Map (or ECS Service Discovery)
10) Aurora Global Database
