# 03: Compute Services - Ultra Fast Learning 🚀

## EC2 Instance Types (CRAMFGPDI)
- **C**: Compute optimized (CPU-intensive)
- **R**: RAM optimized (memory databases, big data)
- **A**: ARM-based (cost-effective)
- **M**: Medium/General purpose (balanced)
- **T**: Burstable (credits for CPU bursts)
- **F**: FPGA (hardware acceleration)
- **G**: GPU (graphics, ML)
- **P**: GPU (parallel processing, ML)
- **D**: Dense storage (data warehousing)
- **I**: I/O optimized (NoSQL, databases)

## EC2 Pricing
| Model | Discount | Use Case |
|-------|----------|----------|
| On-Demand | 0% | Short, unpredictable |
| Reserved (1-3 yr) | Up to 72% | Steady state |
| Savings Plans | Up to 66% | Flexible commitment |
| Spot | Up to 90% | Fault-tolerant, flexible |
| Dedicated Host | 0% | Compliance, BYOL |
| Dedicated Instance | 0% | Hardware isolation |

## EC2 Storage
- **Instance Store**: Ephemeral, lost on stop/termination, high IOPS
- **EBS**: Network attached, persistent, AZ-locked
- **EFS**: Network file system, multi-AZ, Linux only

## Placement Groups
- **Cluster**: Same AZ, low latency (10 Gbps), HPC
- **Spread**: Max 7/AZ, critical apps, different hardware
- **Partition**: Divide instances into partitions, Hadoop/Kafka

## Auto Scaling
- **Target Tracking**: Maintain metric (e.g., CPU 50%)
- **Step Scaling**: Add/remove based on CloudWatch alarms
- **Scheduled**: Predictable patterns
- **Cooldown**: 300 sec default (wait before next scaling)
- **Health Checks**: EC2 (default) or ELB (better)

## Load Balancers
| Type | Layer | Use Case | Features |
|------|-------|----------|----------|
| ALB | 7 (HTTP/HTTPS) | Web apps | Path/host routing, WebSocket |
| NLB | 4 (TCP/UDP) | High performance | Million req/sec, static IP |
| GLB | 3 (IP) | Firewall/IDS | GENEVE protocol |
| CLB | 4 & 7 | Legacy | Deprecated |

### Load Balancer Features
- **Cross-Zone**: Distribute evenly across all AZs (ALB: always on, NLB: off by default)
- **Sticky Sessions**: Same instance for session (ALB: target group, NLB: source IP)
- **Connection Draining**: Wait for in-flight requests (1-3600 sec)

## Lambda
- **Max execution time**: 15 minutes
- **Max memory**: 10 GB
- **Max deployment package**: 50 MB (zipped), 250 MB (unzipped)
- **Environment variables**: 4 KB max
- **Concurrency**: 1,000 default (can increase)
- **Pricing**: Requests + Duration (GB-seconds)
- **Free tier**: 1M requests + 400K GB-sec/month

### Lambda Best Practices
- Reuse execution context (global variables)
- Use environment variables for config
- Use /tmp for temporary files (512 MB - 10 GB)
- Use layers for dependencies
- Enable X-Ray for tracing

## ECS (Elastic Container Service)
- **Launch Types**: EC2 (manage instances) vs Fargate (serverless)
- **Task Definition**: Blueprint (Docker image, CPU, memory)
- **Service**: Run and maintain tasks
- **Cluster**: Logical grouping
- **Use IAM Roles**: Task role (app permissions) + Execution role (ECS agent)

## EKS (Elastic Kubernetes Service)
- Managed Kubernetes
- **Control plane**: AWS manages
- **Worker nodes**: EC2 or Fargate
- **Use cases**: Complex orchestration, hybrid cloud

## Elastic Beanstalk
- **PaaS**: Upload code, Beanstalk handles deployment
- **Free**: Pay only for underlying resources
- **Supports**: Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker
- **Components**: Application → Version → Environment

## Quick Exam Tips
- **EC2**: Use roles, not access keys
- **Spot**: Can be terminated with 2-min notice
- **Reserved**: 1 or 3 years, can sell unused
- **Auto Scaling**: Combines with ELB for high availability
- **ALB**: Layer 7, path-based routing
- **NLB**: Layer 4, static IP, high performance
- **Lambda**: Serverless, 15 min max
- **ECS Fargate**: Serverless containers
- **User Data**: Bootstrap script (runs once at launch)
- **AMI**: Region-specific, must copy for other regions

