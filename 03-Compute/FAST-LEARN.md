# ⚡ Fast Learning - Compute Services

> **Time to Complete**: 60-90 minutes | **Exam Weight**: ~20-25%

## 🎯 Must-Know Concepts (5 Minutes)

### Compute Service Selector
```
NEED VMS? → EC2
NEED SERVERLESS? → Lambda
NEED CONTAINERS? → ECS/EKS/Fargate
NEED PAAS? → Elastic Beanstalk
NEED AUTO-SCALE? → Auto Scaling Group
NEED LOAD BALANCE? → ALB/NLB/GWLB
```

**Memory Aid**: "VeLoCiraptor Eats Lamb" = VM, Lambda, Containers, Elastic Beanstalk, Auto Scale, Load Balance

## 📊 Quick Reference Tables

### EC2 Instance Types (CRAM-FACTS-PIG)
| Family | Name | Use Case | Example |
|--------|------|----------|---------|
| **C** | Compute | CPU-intensive | Batch processing, gaming |
| **R** | RAM | Memory-intensive | Databases, caching |
| **M** | Medium | General purpose | Web servers, apps |
| **T** | Tiny/Turbo | Burstable | Dev/test, low traffic |
| **P/G** | GPU | Graphics/ML | Machine learning, rendering |
| **I/D/H** | I/O | Storage-intensive | Databases, data warehousing |

**Format**: `t3.medium` = Family(t) + Generation(3) + Size(medium)

### EC2 Pricing Models (OSRSD)
| Model | Discount | Commitment | Use Case | Interruption |
|-------|----------|------------|----------|--------------|
| **O**n-Demand | 0% | None | Short-term, unpredictable | No |
| **S**pot | Up to 90% | None | Fault-tolerant | YES (2 min notice) |
| **R**eserved | Up to 72% | 1-3 years | Steady state | No |
| **S**avings Plans | Up to 66% | 1-3 years | Flexible | No |
| **D**edicated | 0% | None/1-3 yr | Compliance, licensing | No |

## 🔥 Exam Hot Topics

### 1. Load Balancer Selection (Critical!)
| Type | Layer | Protocol | Use Case | Key Features |
|------|-------|----------|----------|--------------|
| **ALB** | 7 | HTTP/HTTPS | Microservices, containers | Path/host routing, Lambda targets |
| **NLB** | 4 | TCP/UDP/TLS | Extreme performance | Static IP, millions req/s |
| **GWLB** | 3 | IP | Security appliances | Firewalls, IDS/IPS |
| **CLB** | 4 & 7 | HTTP/TCP | Legacy (avoid) | Deprecated |

**Memory Aid**: "ALN your Goals" = ALB (apps), NLB (network), GWLB (gateway)

### 2. Auto Scaling Policies
```
1. TARGET TRACKING (Most Common)
   └── "Keep CPU at 50%"
   
2. STEP SCALING
   └── CPU 60-70% → +1 instance
   └── CPU 70-80% → +2 instances
   
3. SCHEDULED SCALING
   └── "Add 10 instances at 8 AM daily"
   
4. PREDICTIVE SCALING
   └── ML-based forecasting
```

**Exam Tip**: Target Tracking = Set it and forget it (easiest)

### 3. Placement Groups
| Type | Placement | AZ | Use Case | Max Performance |
|------|-----------|-----|----------|-----------------|
| **Cluster** | Same rack | Single | HPC, low latency | 10 Gbps |
| **Spread** | Different racks | Multi | Critical instances | 7/AZ max |
| **Partition** | Different racks | Multi | Distributed apps (Hadoop) | Multiple partitions |

**Memory Aid**: "CSP" = Cluster (Speed), Spread (Safety), Partition (Parts)

### 4. Lambda Essentials
```
MAX TIMEOUT: 15 minutes
MAX MEMORY: 10,240 MB (10 GB)
MAX /tmp STORAGE: 10 GB
MAX DEPLOYMENT SIZE: 50 MB (zipped), 250 MB (unzipped)
CONCURRENT EXECUTIONS: 1,000 (default, can increase)
```

**Pricing**: Pay per request + duration (GB-seconds)

## 💡 Common Exam Scenarios

### Scenario 1: Cost Optimization
**Q**: Database runs 24/7, how to reduce cost?
**✅ ANSWER**: Reserved Instances (1-3 year commitment)

### Scenario 2: Handle Variable Traffic
**Q**: Traffic spikes unpredictably, need to scale
**✅ ANSWER**: Auto Scaling Group with Target Tracking policy

### Scenario 3: Extreme Performance Required
**Q**: Need millions of requests/sec, static IP
**✅ ANSWER**: Network Load Balancer (NLB)

### Scenario 4: Microservices Routing
**Q**: Route /api to API servers, /images to image servers
**✅ ANSWER**: Application Load Balancer with path-based routing

### Scenario 5: Short Tasks, No Servers
**Q**: Process images when uploaded, run < 5 min
**✅ ANSWER**: Lambda triggered by S3 event

### Scenario 6: Batch Job Interruption OK
**Q**: Batch processing, can restart if interrupted
**✅ ANSWER**: Spot Instances (up to 90% cheaper)

### Scenario 7: Low Latency HPC Cluster
**Q**: High-performance computing, need lowest latency
**✅ ANSWER**: Cluster Placement Group

## 🎓 Speed Learning Tips

### EC2 User Data vs Metadata
```
USER DATA (Bootstrap)
└── Scripts run at launch
└── http://169.254.169.254/latest/user-data

METADATA (Instance info)
└── Instance info, IP, security groups
└── http://169.254.169.254/latest/meta-data
```

### Auto Scaling Key Concepts
- **Min**: Minimum instances (always running)
- **Desired**: Current target
- **Max**: Maximum instances (cost limit)
- **Cooldown**: Wait period (default 300s)
- **Health Check**: EC2 status or ELB health

### Load Balancer Features Matrix
| Feature | ALB | NLB | GWLB |
|---------|-----|-----|------|
| Path routing | ✅ | ❌ | ❌ |
| Host routing | ✅ | ❌ | ❌ |
| Lambda targets | ✅ | ❌ | ❌ |
| Static IP | ❌ | ✅ | ❌ |
| PrivateLink | ❌ | ✅ | ✅ |
| Cross-zone LB | ✅ (always) | ❌ (optional) | ✅ |

## 📝 Rapid-Fire Facts

### Reserved Instance Types
1. **Standard**: 72% discount, can't change instance family
2. **Convertible**: 66% discount, can change instance family
3. **Scheduled**: For predictable schedules

### Savings Plans Types
1. **Compute**: Most flexible (EC2, Lambda, Fargate)
2. **EC2**: Less flexible (specific instance family)
3. **SageMaker**: ML workloads only

### Container Services Quick Pick
| Service | Management | Use Case |
|---------|------------|----------|
| **ECS** | AWS-native | AWS-only containers |
| **EKS** | Kubernetes | K8s compatibility |
| **Fargate** | Serverless | No server management |

**Memory Aid**: ECS = Easy, EKS = Kubernetes, Fargate = Forget servers

### Lambda Triggers (Common)
- API Gateway (REST APIs)
- S3 Events (upload/delete)
- DynamoDB Streams
- CloudWatch Events/EventBridge
- SQS queues
- SNS topics
- ALB targets

## 🚀 5-Minute Master Review

### The Compute Decision Tree
```
1. Need servers? 
   NO → Lambda (if < 15 min) or Fargate
   YES → Continue
   
2. Steady state 24/7?
   YES → Reserved Instances
   NO → Continue
   
3. Can tolerate interruption?
   YES → Spot Instances
   NO → On-Demand
   
4. Need load balancing?
   HTTP/HTTPS → ALB
   TCP/extreme performance → NLB
   Security appliances → GWLB
```

### Auto Scaling Best Practices
✅ Use Target Tracking (simplest)
✅ Multi-AZ for high availability
✅ Use ELB health checks (better than EC2)
✅ Set appropriate cooldown period
✅ Monitor with CloudWatch

### Common Mistakes to Avoid
❌ Using On-Demand for steady workloads (use Reserved)
❌ Not using Auto Scaling for variable loads
❌ Single AZ deployment (no HA)
❌ ALB for TCP/UDP (use NLB)
❌ Forgetting Spot can be interrupted
❌ Lambda for long-running tasks (15 min max)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Max Lambda timeout? __
2. Best load balancer for microservices? __
3. Cheapest pricing for fault-tolerant workloads? __
4. Max instances per AZ in Spread placement group? __
5. Which LB has static IP? __
6. Auto Scaling cooldown default? __
7. What layer is ALB? __
8. Can Reserved Instances be interrupted? __

---

### Instance Store vs EBS
```
INSTANCE STORE (Ephemeral)
├── Physically attached
├── Very fast
├── Data lost on stop/terminate
└── Use: Temporary data, cache

EBS (Persistent)
├── Network attached
├── Fast
├── Data persists
└── Use: Database, OS, permanent data
```

### EBS Volume Types Quick Reference
| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| gp3/gp2 | 16,000 | 1,000 MB/s | General purpose (boot) |
| io2/io1 | 64,000+ | 1,000 MB/s | Databases, critical |
| st1 | 500 | 500 MB/s | Big data, logs |
| sc1 | 250 | 250 MB/s | Cold data |

## ⏱️ Next Steps
- Time spent: ~60-90 min
- Practice: Launch EC2, create ASG, configure ALB
- Ready for: Compute practice questions
- Move to: [Module 04 - Storage](../04-Storage/FAST-LEARN.md)

---

**Quick Answers**: 
1) 15 minutes
2) ALB (Application Load Balancer)
3) Spot Instances (up to 90% off)
4) 7 instances
5) NLB (Network Load Balancer)
6) 300 seconds
7) Layer 7 (Application)
8) No

