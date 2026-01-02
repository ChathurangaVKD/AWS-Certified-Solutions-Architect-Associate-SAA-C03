# Module 03: Compute Services

## 📚 Overview

AWS compute services for SAA-C03 exam: EC2, Lambda, containers, Auto Scaling, and Load Balancers.

**Exam Weight**: ~20-25%

---

## 🎯 Key Services

1. **Amazon EC2** - Virtual servers
2. **AWS Lambda** - Serverless functions
3. **Auto Scaling** - Automatic capacity management
4. **Elastic Load Balancing** - Distribute traffic
5. **ECS/EKS/Fargate** - Container services
6. **Elastic Beanstalk** - PaaS deployment

---

## 1. Amazon EC2

### Instance Types (CRAM FACTS)
- **C** - Compute Optimized
- **R** - Memory Optimized (RAM)
- **M** - General Purpose (Medium)
- **T** - Burstable Performance
- **I/D/H** - Storage Optimized

### Pricing Models
| Model | Discount | Use Case |
|-------|----------|----------|
| On-Demand | None | Short-term, unpredictable |
| Reserved (1-3 yr) | Up to 72% | Steady state |
| Savings Plans | Up to 66% | Flexible commitment |
| Spot | Up to 90% | Fault-tolerant workloads |
| Dedicated | None | Compliance, licensing |

### Placement Groups
- **Cluster**: Low latency, same AZ
- **Spread**: Max 7/AZ, critical apps
- **Partition**: Distributed apps (Hadoop, Kafka)

---

## 2. Auto Scaling

### Scaling Policies
1. **Target Tracking**: Maintain metric (e.g., CPU 50%)
2. **Step Scaling**: Add/remove based on alarms
3. **Scheduled**: Time-based scaling
4. **Predictive**: ML-based forecasting

### Key Concepts
- Min/Desired/Max capacity
- Health checks
- Lifecycle hooks
- Cooldown periods (default 300s)

---

## 3. Elastic Load Balancing

| Type | Layer | Use Case | Features |
|------|-------|----------|----------|
| ALB | 7 (HTTP/HTTPS) | Microservices, containers | Path/host routing, Lambda targets |
| NLB | 4 (TCP/UDP) | Extreme performance | Static IP, millions req/sec |
| GWLB | 3 (Network) | Virtual appliances | Firewalls, IDS |
| CLB | 4 & 7 | Legacy | Not recommended |

### Features
- Health checks
- Sticky sessions
- Cross-zone load balancing
- SSL/TLS termination

---

## 4. AWS Lambda

### Limits
- Max execution: **15 minutes**
- Memory: 128 MB - 10 GB
- /tmp storage: 512 MB - 10 GB
- Concurrent executions: 1,000 (default)

### Invocation Types
1. **Synchronous**: API Gateway, CLI
2. **Asynchronous**: S3, SNS, EventBridge
3. **Event Source Mapping**: SQS, Kinesis, DynamoDB Streams

### Pricing
- $0.20 per 1M requests
- $0.00001667 per GB-second

---

## 5. Container Services

### ECS (Elastic Container Service)
**Launch Types:**
- **EC2**: You manage instances
- **Fargate**: Serverless, AWS manages

**Components:**
- Task Definition
- Task
- Service
- Cluster

### EKS (Elastic Kubernetes Service)
- Managed Kubernetes
- Compatible with standard K8s
- $0.10/hour cluster cost

### Fargate
- Serverless containers
- Works with ECS and EKS
- Pay per task

---

## 6. Other Services

### Elastic Beanstalk (PaaS)
- Deploy code, AWS handles infrastructure
- Supports: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker
- Auto scaling, load balancing included

### AWS Batch
- Managed batch computing
- Automatic resource provisioning
- Uses Spot instances for cost savings

### Lightsail
- Simple VPS
- Fixed monthly pricing
- Pre-configured templates

---

## 🎯 Exam Tips

### Decision Tree
```
Need compute?
├─ Run code without servers? → Lambda
├─ Containers?
│  ├─ Without managing servers? → Fargate
│  ├─ With Kubernetes? → EKS
│  └─ AWS orchestration? → ECS
├─ Just deploy code? → Elastic Beanstalk
└─ Full control? → EC2
```

### Common Scenarios
- **Variable workload** → Auto Scaling + Spot
- **Lowest latency networking** → Cluster placement group
- **Content-based routing** → ALB
- **Millions of req/sec, static IP** → NLB
- **Steady 3-year workload** → Reserved Instances
- **Fault-tolerant batch job** → Spot Instances
- **Run code on events** → Lambda
- **Serverless containers** → Fargate

### Key Points
- EC2 instance store = ephemeral (lost on stop)
- EBS = persistent block storage (AZ-specific)
- T instances = burstable CPU
- Spot instances = 2-minute warning before termination
- Lambda max = 15 minutes
- ALB = Layer 7, content routing
- NLB = Layer 4, extreme performance
- Auto Scaling ensures min/max capacity

---

**Estimated Study Time**: 8-10 hours  
**Difficulty**: ⭐⭐⭐

[⬅️ Previous: IAM](../02-IAM/README.md) | [Next: Storage ➡️](../04-Storage/README.md) | [📚 Main](../README.md)

