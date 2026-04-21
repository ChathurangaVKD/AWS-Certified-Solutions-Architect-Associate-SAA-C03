# Cost Optimization - Mermaid Diagrams

## Cost Optimization Strategies

### Cost Optimization Pillars

```mermaid
mindmap
    root((Cost<br/>Optimization))
        Right-Sizing
            Match instances to workload
            CloudWatch metrics
            Compute Optimizer
            Downsize over-provisioned
        Purchase Options
            On-Demand baseline
            Reserved Instances 1-3 year
            Savings Plans flexible
            Spot Instances 90% off
        Storage Optimization
            S3 Lifecycle policies
            EBS snapshot cleanup
            Intelligent-Tiering
            Archive to Glacier
        Monitoring & Governance
            Cost allocation tags
            AWS Budgets
            Cost Explorer
            Trusted Advisor
        Serverless & Managed
            Lambda pay-per-use
            DynamoDB on-demand
            Fargate containers
            Aurora Serverless
```

## EC2 Cost Optimization

### EC2 Pricing Models Comparison

```mermaid
graph TB
    subgraph On_Demand_Instances_Group["On-Demand Instances"]
        OD["On-Demand<br/>💰 Full price<br/>⏱️ No commitment<br/>📊 Flexible"]
        
        OD_Use["Use Cases:<br/>• Unpredictable workloads<br/>• Development/testing<br/>• Short-term spikes<br/>• New applications"]
        
        OD_Price["Pricing:<br/>Linux t3.medium:<br/>$0.0416/hour<br/>$30/month"]
    end
    
    subgraph Reserved_Instances_Group["Reserved Instances"]
        RI["Reserved Instances<br/>💰 Up to 72% discount<br/>⏱️ 1 or 3 years<br/>📊 Predictable"]
        
        RI_Types["Types:<br/>• Standard RI 72% off<br/>• Convertible RI 54% off<br/>• Scheduled RI specific times"]
        
        RI_Use["Use Cases:<br/>• Steady-state workloads<br/>• Databases<br/>• Base capacity<br/>• Long-term projects"]
        
        RI_Price["Pricing:<br/>Linux t3.medium 3yr:<br/>$0.0116/hour<br/>$8.50/month<br/>72% savings"]
    end
    
    subgraph Savings_Plans_Group["Savings Plans"]
        SP["Savings Plans<br/>💰 Up to 66% discount<br/>⏱️ 1 or 3 years<br/>📊 More flexible"]
        
        SP_Types["Types:<br/>• Compute SP 66% off any instance<br/>• EC2 Instance SP 72% off specific<br/>• SageMaker SP ML workloads"]
        
        SP_Use["Use Cases:<br/>• Consistent usage<br/>• Flexible instance types<br/>• Cross-service usage<br/>• Container workloads"]
    end
    
    subgraph Spot_Instances_Group["Spot Instances"]
        Spot["Spot Instances<br/>💰 Up to 90% discount<br/>⏱️ Can be interrupted<br/>📊 Fault-tolerant"]
        
        Spot_Use["Use Cases:<br/>• Batch processing<br/>• Big data analysis<br/>• CI/CD pipelines<br/>• Containerized workloads<br/>• Fault-tolerant apps"]
        
        Spot_Price["Pricing:<br/>Linux t3.medium:<br/>$0.0125/hour avg<br/>$9/month<br/>70% savings"]
    end
    
    Recommendation["Recommendation:<br/>Mix of pricing models:<br/>• Base capacity: Reserved/Savings Plans<br/>• Variable load: On-Demand<br/>• Batch jobs: Spot Instances"]
    
    classDef style1 fill:#569A31
    class RI style1
    classDef style2 fill:#FF9900
    class Spot style2
    classDef style3 fill:#146EB4
    class SP style3
```

### Reserved Instance Types

```mermaid
graph TB
    RI[Reserved Instances]
    
    RI --> Standard["Standard RI<br/>💰 Up to 72% discount<br/>📊 Cannot change instance family<br/>✅ Best for steady workloads"]
    
    RI --> Convertible["Convertible RI<br/>💰 Up to 54% discount<br/>🔄 Change instance family<br/>🔄 Change OS, tenancy<br/>✅ Flexibility with savings"]
    
    RI --> Scheduled["Scheduled RI<br/>Deprecated<br/>Use Savings Plans instead"]
    
    subgraph Payment_Options_Group["Payment Options"]
        Standard --> AllUpfront["All Upfront<br/>💰 Maximum discount<br/>Pay 100% upfront"]
        
        Standard --> PartialUpfront["Partial Upfront<br/>💰 Good discount<br/>Pay ~50% upfront<br/>Monthly payments"]
        
        Standard --> NoUpfront["No Upfront<br/>💰 Lower discount<br/>Monthly payments only"]
    end
    
    subgraph Scope_Group["Scope"]
        Regional["Regional RI<br/>✅ AZ flexibility<br/>✅ Instance size flexibility<br/>Linux only<br/>Recommended"]
        
        Zonal["Zonal RI<br/>✅ Capacity reservation<br/>❌ No flexibility<br/>Specific AZ"]
    end
    
    Marketplace["RI Marketplace<br/>Buy/Sell unused RIs"] -.Trade.-> Standard
    
    classDef style1 fill:#569A31
    class Standard style1
    classDef style2 fill:#FF9900
    class Convertible style2
```

### Spot Instance Strategies

```mermaid
graph TB
    subgraph Spot_Instance_Best_Practices_Group["Spot Instance Best Practices"]
        Fleet["Spot Fleet<br/>Combination of instance types<br/>Automatic diversification"]
        
        Fallback["Spot + On-Demand<br/>Maintain capacity"]
        
        Checkpointing["Checkpointing<br/>Save state regularly<br/>Resume on interruption"]
        
        Interruption["Spot Instance<br/>Interruption Notice<br/>2-minute warning"]
    end
    
    subgraph Use_Cases_Group["Use Cases"]
        Batch["Batch Processing<br/>✅ Divisible workloads<br/>✅ Can pause/resume<br/>e.g., Video encoding"]
        
        BigData["Big Data Analytics<br/>✅ EMR with Spot<br/>✅ Task nodes on Spot<br/>Core nodes on On-Demand"]
        
        CI_CD["CI/CD Pipelines<br/>✅ Build servers<br/>✅ Test environments<br/>✅ Ephemeral workloads"]
        
        Containers["Container Workloads<br/>✅ ECS/EKS with Spot<br/>✅ Stateless services<br/>✅ Auto-scaling groups"]
    end
    
    subgraph Spot_Fleet_Strategy_Group["Spot Fleet Strategy"]
        Diversified["Diversified<br/>Multiple instance types<br/>Multiple AZs<br/>Reduce interruption"]
        
        LowestPrice["Lowest Price<br/>Cheapest available<br/>Higher interruption risk"]
        
        CapacityOptimized["Capacity Optimized<br/>Least likely interrupted<br/>Recommended for most"]
    end
    
    Fleet --> Diversified
    Fleet --> LowestPrice
    Fleet --> CapacityOptimized
    
    AutoScaling["EC2 Auto Scaling<br/>with Spot"] -.Use.-> Fleet
    
    Interruption --> Checkpointing
    
    classDef style1 fill:#FF9900
    class Fleet style1
    classDef style2 fill:#569A31
    class CapacityOptimized style2
```

## Storage Cost Optimization

### S3 Storage Classes Cost Comparison

```mermaid
graph TB
    Data[Your Data] --> Decision{Access Pattern?}
    
    Decision -->|Frequent| Standard["S3 Standard<br/>💰 $0.023/GB/month<br/>📊 99.99% availability<br/>⚡ Millisecond access"]
    
    Decision -->|Unknown| Intelligent["S3 Intelligent-Tiering<br/>💰 $0.0025 monitoring<br/>🤖 Auto-moves between tiers<br/>💡 No retrieval fees"]
    
    Decision -->|Infrequent| IA_Decision{Critical?}
    
    IA_Decision -->|Yes| StandardIA["S3 Standard-IA<br/>💰 $0.0125/GB/month<br/>💰 $0.01/GB retrieval<br/>📊 99.9% availability<br/>⏱️ 30 day minimum"]
    
    IA_Decision -->|No| OneZoneIA["S3 One Zone-IA<br/>💰 $0.01/GB/month<br/>💰 $0.01/GB retrieval<br/>📊 99.5% availability<br/>⚠️ Single AZ"]
    
    Decision -->|Archive| Archive_Decision{Speed needed?}
    
    Archive_Decision -->|Instant| GlacierInstant["S3 Glacier Instant<br/>💰 $0.004/GB/month<br/>💰 $0.03/GB retrieval<br/>⚡ Millisecond access<br/>⏱️ 90 day minimum"]
    
    Archive_Decision -->|Minutes-Hours| GlacierFlexible["S3 Glacier Flexible<br/>💰 $0.0036/GB/month<br/>💰 $0.02/GB retrieval<br/>⏱️ 1-5 min or 3-5 hrs<br/>⏱️ 90 day minimum"]
    
    Archive_Decision -->|12-48 Hours| GlacierDeep["S3 Glacier Deep Archive<br/>💰 $0.00099/GB/month<br/>💰 $0.02/GB retrieval<br/>⏱️ 12-48 hours<br/>⏱️ 180 day minimum<br/>💡 Lowest cost"]
    
    Example["Example 1 TB/month:<br/>Standard: $23.55<br/>Standard-IA: $12.80<br/>Glacier Instant: $4.10<br/>Glacier Flexible: $3.69<br/>Glacier Deep: $1.01"]
    
    classDef style1 fill:#C00
    class Standard style1
    classDef style2 fill:#FF9900
    class Intelligent style2
    classDef style3 fill:#569A31
    class StandardIA style3
    classDef style4 fill:#146EB4
    class GlacierDeep style4
```

### S3 Lifecycle Policies

```mermaid
stateDiagram-v2
    [*] --> Standard: Upload ([[Day 0(
    
    Standard --> StandardIA: After 30 days<br/>Transition
    
    StandardIA --> IntelligentTiering: After 60 days<br/>Transition
    
    IntelligentTiering --> GlacierFlexible: After 90 days<br/>Transition
    
    GlacierFlexible --> GlacierDeep: After 365 days<br/>Transition
    
    GlacierDeep --> [*]: After 7 years<br/>Expire & Delete
    
    note right of Standard
        Frequently accessed
        First 30 days
        Cost: $0.023/GB
    end note
    
    note right of GlacierDeep
        Long-term archive
        Compliance retention
        Cost: $0.00099/GB
        99% cost reduction!
    end note
```

### EBS Cost Optimization

```mermaid
graph TB
    subgraph EBS_Volume_Types_by_Cost_Group["EBS Volume Types by Cost"]
        GP3["gp3 General Purpose SSD<br/>💰 $0.08/GB/month<br/>📊 3,000-16,000 IOPS<br/>💾 125-1,000 MB/s<br/>✅ 20% cheaper than gp2<br/>Recommended"]
        
        GP2["gp2 General Purpose SSD<br/>💰 $0.10/GB/month<br/>📊 3 IOPS/GB baseline<br/>💾 Max 250 MB/s<br/>Legacy option"]
        
        ST1["st1 Throughput Optimized HDD<br/>💰 $0.045/GB/month<br/>💾 Max 500 MB/s<br/>✅ 55% cheaper than gp3<br/>Use: Big data, logs"]
        
        SC1["sc1 Cold HDD<br/>💰 $0.015/GB/month<br/>💾 Max 250 MB/s<br/>✅ 81% cheaper than gp3<br/>Use: Infrequent access"]
        
        IO2["io2 Provisioned IOPS SSD<br/>💰 $0.125/GB/month<br/>💰 $0.065/IOPS/month<br/>📊 Up to 64,000 IOPS<br/>Use: Critical databases"]
    end
    
    subgraph Optimization_Strategies_Group["Optimization Strategies"]
        Snapshot["Delete Old Snapshots<br/>💰 $0.05/GB/month<br/>Keep only needed<br/>Automated cleanup"]
        
        DeleteUnused["Delete Unattached Volumes<br/>Find with Trusted Advisor<br/>Stop paying for unused"]
        
        RightSize["Right-size Volumes<br/>CloudWatch metrics<br/>Reduce if underutilized<br/>Can't shrink, must migrate"]
        
        ChooseType["Choose Right Type<br/>gp3 for most workloads<br/>st1/sc1 for throughput<br/>io2 only when needed"]
    end
    
    Example["Example 1 TB volume/month:<br/>gp3: $81.92<br/>gp2: $102.40<br/>st1: $46.08<br/>sc1: $15.36<br/>io2 base: $128"]
    
    classDef style1 fill:#569A31
    class GP3 style1
    classDef style2 fill:#146EB4
    class SC1 style2
    classDef style3 fill:#C00
    class IO2 style3
```

## Database Cost Optimization

### RDS Cost Optimization

```mermaid
graph TB
    subgraph RDS_Pricing_Options_Group["RDS Pricing Options"]
        OnDemand["On-Demand<br/>💰 Full price<br/>Pay per hour<br/>No commitment"]
        
        RI["Reserved Instances<br/>💰 Up to 69% discount<br/>1 or 3 years<br/>All/Partial/No upfront"]
        
        Aurora["Aurora Serverless<br/>💰 Pay per ACU-hour<br/>Auto-pause when idle<br/>Good for variable workloads"]
    end
    
    subgraph Storage_Optimization_Group["Storage Optimization"]
        GP3Storage["Use gp3 Storage<br/>💰 Cheaper than gp2<br/>Better performance<br/>20% cost reduction"]
        
        BackupRetention["Optimize Backups<br/>Reduce retention period<br/>7 days vs 35 days<br/>Snapshot cleanup"]
        
        ReadReplicas["Right-size Read Replicas<br/>Use only when needed<br/>Delete unused<br/>Use smaller instances"]
    end
    
    subgraph Instance_Optimization_Group["Instance Optimization"]
        RightSize["Right-size Instances<br/>CloudWatch metrics<br/>Performance Insights<br/>Start smaller, scale up"]
        
        BurstableT["Use Burstable Instances<br/>db.t3, db.t4g<br/>Good for dev/test<br/>70% cheaper than m5"]
        
        Graviton["Use Graviton2/3<br/>db.t4g, db.m6g, db.r6g<br/>20% better price/perf<br/>ARM-based"]
    end
    
    subgraph Alternative_Options_Group["Alternative Options"]
        DynamoDB["DynamoDB On-Demand<br/>For key-value workloads<br/>No idle costs<br/>Serverless"]
        
        Aurora_Serverless["Aurora Serverless v2<br/>Auto-scaling<br/>Pay per second<br/>Scale to zero not supported"]
    end
    
    Example["Example db.t3.medium:<br/>On-Demand: $61/month<br/>1yr RI Partial: $36/month 41% off<br/>3yr RI All: $23/month 62% off<br/><br/>db.t4g.medium Graviton:<br/>On-Demand: $49/month 20% cheaper"]
    
    classDef style1 fill:#569A31
    class RI style1
    classDef style2 fill:#FF9900
    class Graviton style2
    classDef style3 fill:#146EB4
    class Aurora style3
```

## Data Transfer Costs

### Data Transfer Pricing

```mermaid
graph TB
    subgraph Data_Transfer_IN_Group["Data Transfer IN"]
        Internet_In["From Internet to AWS<br/>💰 FREE<br/>All regions<br/>All services"]
        
        S3_In["To S3 from Internet<br/>💰 FREE<br/>Upload data<br/>No charge"]
    end
    
    subgraph Data_Transfer_OUT_Group["Data Transfer OUT"]
        First_GB["First 1 GB/month<br/>💰 FREE<br/>All services"]
        
        To_Internet["To Internet<br/>💰 $0.09/GB first 10 TB<br/>💰 $0.085/GB next 40 TB<br/>💰 $0.07/GB next 100 TB<br/>💰 $0.05/GB over 150 TB"]
        
        CloudFront_Out["Via CloudFront<br/>💰 $0.085/GB<br/>💡 Cheaper + global<br/>+ caching benefits"]
    end
    
    subgraph AWS_Internal_Transfer_Group["AWS Internal Transfer"]
        Same_AZ["Same AZ<br/>💰 FREE<br/>Using private IP"]
        
        Cross_AZ["Cross-AZ same region<br/>💰 $0.01/GB in<br/>💰 $0.01/GB out<br/>Both directions charged"]
        
        Cross_Region["Cross-Region<br/>💰 $0.02/GB<br/>Between regions"]
    end
    
    subgraph Cost_Optimization_Group["Cost Optimization"]
        Use_Private["Use Private IPs<br/>Avoid public IPs<br/>Save cross-AZ charges"]
        
        Single_AZ["Single AZ when possible<br/>For cost-sensitive<br/>Trade-off: HA vs cost"]
        
        CloudFront["Use CloudFront<br/>Reduce data transfer<br/>Cache at edge<br/>Better performance"]
        
        VPC_Endpoints["VPC Endpoints<br/>S3, DynamoDB free<br/>Avoid NAT gateway costs<br/>Avoid data transfer fees"]
    end
    
    Example["Example: Transfer 10 TB/month<br/>Direct to Internet: $900<br/>Via CloudFront: $850 + caching<br/>Cross-AZ: $200 10 TB both ways<br/>VPC Endpoint S3: $0"]
    
    classDef style1 fill:#569A31
    class Internet_In style1
    classDef style2 fill:#C00
    class To_Internet style2
    classDef style3 fill:#FF9900
    class VPC_Endpoints style3
```

## AWS Cost Management Tools

### Cost Management Architecture

```mermaid
graph TB
    subgraph Cost_Visibility_Group["Cost Visibility"]
        CE["AWS Cost Explorer<br/>Visualize costs<br/>Historical data<br/>Forecasting"]
        
        CUR["Cost & Usage Report<br/>Most detailed<br/>Hourly granularity<br/>S3 delivery"]
        
        Billing["AWS Billing Dashboard<br/>Current month spend<br/>Previous invoices<br/>Payment methods"]
    end
    
    subgraph Cost_Control_Group["Cost Control"]
        Budgets["AWS Budgets<br/>Set spending limits<br/>Alerts via SNS<br/>Actual & forecasted"]
        
        CostAnomaly["Cost Anomaly Detection<br/>ML-based alerts<br/>Unusual spending<br/>Root cause analysis"]
    end
    
    subgraph Optimization_Recommendations_Group["Optimization Recommendations"]
        ComputeOptimizer["Compute Optimizer<br/>Right-sizing recommendations<br/>ML-based analysis<br/>EC2, Lambda, EBS, Auto Scaling"]
        
        TrustedAdvisor["Trusted Advisor<br/>Cost optimization checks<br/>Idle resources<br/>Underutilized instances"]
        
        Savings["Savings Plans<br/>Recommendations<br/>Commitment analysis<br/>Flexible discounts"]
    end
    
    subgraph Governance_Group["Governance"]
        Tags["Cost Allocation Tags<br/>Track by:<br/>• Environment<br/>• Project<br/>• Team<br/>• Cost center"]
        
        Organizations["AWS Organizations<br/>Consolidated billing<br/>Volume discounts<br/>Centralized management"]
        
        SCP["Service Control Policies<br/>Prevent expensive<br/>Instance types<br/>Region restrictions"]
    end
    
    CloudWatch[CloudWatch] --> Budgets
    Budgets --> SNS[SNS Notifications]
    SNS --> Lambda[Lambda Auto-remediation]
    
    CUR --> Athena["Athena<br/>Query CUR data"]
    Athena --> QuickSight["QuickSight<br/>Custom dashboards"]
    
    ComputeOptimizer --> Actions["Automated Actions<br/>Right-size instances<br/>Modify Auto Scaling<br/>Delete unused resources"]
    
    classDef style1 fill:#FF9900
    class CE style1
    classDef style2 fill:#569A31
    class Budgets style2
    classDef style3 fill:#146EB4
    class ComputeOptimizer style3
```

### AWS Budgets and Alerts

```mermaid
sequenceDiagram
    participant User as Cost Admin
    participant Budgets as AWS Budgets
    participant CW as CloudWatch
    participant SNS
    participant Lambda
    participant Resources as AWS Resources
    
    User->>Budgets: Create budget<br/>Monthly: $10,000<br/>Alerts: 80%, 100%, 110%
    
    Note over Resources: Services consuming costs
    
    Resources->>Budgets: Cost accumulates
    Budgets->>Budgets: 80% of budget ($8,000(
    
    Budgets->>SNS: Alert: 80% threshold
    SNS->>User: Email notification
    
    Note over Resources: Costs continue
    
    Resources->>Budgets: 100% of budget ($10,000(
    Budgets->>SNS: Alert: 100% threshold
    SNS->>User: Email + SMS
    SNS->>Lambda: Trigger remediation
    
    Lambda->>Resources: Stop non-prod instances<br/>Reduce Auto Scaling
    
    Resources->>Budgets: 110% of budget ($11,000(
    Budgets->>SNS: Critical alert
    SNS->>User: Email + SMS + Slack
    
    Note over User: Take corrective action
    
```

### Cost Optimization Workflow

```mermaid
flowchart TD
    Start((Monthly Cost Review)) --> Analyze["Analyze Costs<br/>Cost Explorer<br/>CUR reports"]
    
    Analyze --> Identify{"Identify<br/>Optimization<br/>Opportunities"}
    
    Identify --> RightSize["Right-Size Resources<br/>Compute Optimizer<br/>CloudWatch metrics"]
    
    Identify --> UnusedResources["Remove Unused<br/>Trusted Advisor<br/>Idle ELBs, EBS, RDS"]
    
    Identify --> CommitmentSavings["Evaluate Commitments<br/>Reserved Instances<br/>Savings Plans"]
    
    Identify --> StorageOpt["Optimize Storage<br/>S3 Lifecycle<br/>Delete old snapshots"]
    
    RightSize --> Implement[Implement Changes]
    UnusedResources --> Implement
    CommitmentSavings --> Implement
    StorageOpt --> Implement
    
    Implement --> Tag["Apply Cost Tags<br/>Track by project<br/>Environment, owner"]
    
    Tag --> Monitor["Monitor Impact<br/>Cost Explorer<br/>Compare periods"]
    
    Monitor --> SetBudgets["Set Budgets & Alerts<br/>Prevent overruns<br/>Anomaly detection"]
    
    SetBudgets --> Document["Document Savings<br/>Report to stakeholders<br/>Continuous improvement"]
    
    Document --> End((Next Month Review))
    
    Automate["Automation Options:<br/>• Lambda for auto-shutdown<br/>• Instance Scheduler<br/>• Auto Scaling policies<br/>• Lifecycle policies"] -.Enhance.-> Implement
    
    classDef style1 fill:#FF9900
    class Analyze style1
    classDef style2 fill:#569A31
    class Implement style2
    classDef style3 fill:#146EB4
    class Monitor style3
```

## Cost Optimization Best Practices

### Cost Optimization Checklist

```mermaid
mindmap
    root((Cost<br/>Optimization<br/>Checklist))
        Compute
            ✅ Right-size instances
            ✅ Use Savings Plans
            ✅ Leverage Spot for batch
            ✅ Auto Scaling enabled
            ✅ Graviton instances
            ✅ Serverless where possible
        Storage
            ✅ S3 Lifecycle policies
            ✅ Delete old snapshots
            ✅ Use gp3 over gp2
            ✅ Intelligent-Tiering
            ✅ Delete unattached EBS
            ✅ Optimize backup retention
        Database
            ✅ RDS Reserved Instances
            ✅ Right-size DB instances
            ✅ Aurora Serverless for variable
            ✅ Delete unused read replicas
            ✅ Use gp3 storage
            ✅ Optimize backup retention
        Networking
            ✅ Use VPC endpoints
            ✅ CloudFront for static
            ✅ Private IPs same AZ
            ✅ Minimize cross-region
            ✅ Delete idle load balancers
            ✅ Use NAT instances not gateways
        Monitoring
            ✅ Cost allocation tags
            ✅ AWS Budgets set
            ✅ Anomaly detection on
            ✅ Monthly reviews
            ✅ Trusted Advisor checks
            ✅ Compute Optimizer enabled
```

### Potential Savings Summary

```mermaid
graph LR
    subgraph Compute_Savings_Group["Compute Savings"]
        C1["EC2 Reserved: 72%<br/>$100K -&gt; $28K"]
        C2["Use Spot: 90%<br/>$50K -&gt; $5K"]
        C3["Right-size: 30%<br/>$80K -&gt; $56K"]
    end
    
    subgraph Storage_Savings_Group["Storage Savings"]
        S1["S3 Lifecycle: 95%<br/>$10K -&gt; $0.5K"]
        S2["Delete Snapshots: 80%<br/>$5K -&gt; $1K"]
        S3["gp3 vs gp2: 20%<br/>$10K -&gt; $8K"]
    end
    
    subgraph Database_Savings_Group["Database Savings"]
        D1["RDS Reserved: 69%<br/>$60K -&gt; $18.6K"]
        D2["Aurora Serverless: 50%<br/>$40K -&gt; $20K"]
        D3["Right-size: 40%<br/>$30K -&gt; $18K"]
    end
    
    subgraph Networking_Savings_Group["Networking Savings"]
        N1["VPC Endpoints: 100%<br/>$5K -&gt; $0"]
        N2["CloudFront: 50%<br/>$20K -&gt; $10K"]
        N3["Delete Idle LB: 100%<br/>$2K -&gt; $0"]
    end
    
    Total["Total Potential Savings:<br/>Before: $412K/year<br/>After: $164K/year<br/>💰 Savings: $248K 60%"]
    
    C1 --> Total
    C2 --> Total
    S1 --> Total
    D1 --> Total
    N1 --> Total
    
    classDef style1 fill:#569A31
    class Total style1
    classDef style2 fill:#FF9900
    class C1 style2
    classDef style3 fill:#146EB4
    class S1 style3
```

