# Architecture Patterns - Mermaid Diagrams

## Well-Architected Framework Pillars

### AWS Well-Architected Framework

```mermaid
mindmap
    root((AWS Well-Architected<br/>Framework))
        Operational Excellence
            IaC CloudFormation
            Runbooks
            Learn from failures
            Observability
            Event-driven
        Security
            Defense in depth
            Identity IAM
            Detective controls
            Data protection KMS
            Incident response
        Reliability
            Foundations
            Workload architecture
            Change management
            Failure management
            Multi-AZ RDS
        Performance Efficiency
            Selection
            Review
            Monitoring CloudWatch
            Tradeoffs
            Serverless Lambda
        Cost Optimization
            Practice financial mgmt
            Expenditure awareness
            Cost-effective resources
            Manage demand/supply
            Reserved Instances
        Sustainability
            Understand impact
            Establish goals
            Maximize utilization
            Adopt new efficient services
            Reduce downstream impact
```

## High Availability Architectures

### Multi-AZ Web Application

```mermaid
graph TB
    Users[Users] --> Route53["Route 53<br/>DNS with Health Checks"]
    
    Route53 --> CloudFront["CloudFront<br/>Global CDN<br/>Edge caching"]
    
    CloudFront --> Shield["AWS Shield<br/>DDoS Protection"]
    Shield --> WAF["AWS WAF<br/>Application firewall"]
    
    subgraph Region_us_east_1_Group["Region: us-east-1"]
        WAF --> ALB["Application Load Balancer<br/>Multi-AZ"]
        
        subgraph AZ_1a_Group["AZ-1a"]
            ASG1[Auto Scaling Group]
            Web1[Web Server 1]
            App1[App Server 1]
            
            ASG1 --> Web1
            Web1 --> App1
        end
        
        subgraph AZ_1b_Group["AZ-1b"]
            ASG2[Auto Scaling Group]
            Web2[Web Server 2]
            App2[App Server 2]
            
            ASG2 --> Web2
            Web2 --> App2
        end
        
        subgraph AZ_1c_Group["AZ-1c"]
            ASG3[Auto Scaling Group]
            Web3[Web Server 3]
            App3[App Server 3]
            
            ASG3 --> Web3
            Web3 --> App3
        end
        
        ALB --> Web1
        ALB --> Web2
        ALB --> Web3
        
        App1 --> RDS["RDS Multi-AZ<br/>Primary in AZ-1a<br/>Standby in AZ-1b"]
        App2 --> RDS
        App3 --> RDS
        
        App1 --> ElastiCache["ElastiCache Redis<br/>Cluster mode<br/>Multi-AZ"]
        App2 --> ElastiCache
        App3 --> ElastiCache
    end
    
    RDS --> S3["S3<br/>Static assets<br/>Backups"]
    
    CloudWatch["CloudWatch<br/>Monitoring & Alarms"] -.Monitor.-> ALB
    CloudWatch -.Monitor.-> RDS
    CloudWatch -.Scale.-> ASG1
    
    classDef style1 fill:#8C4FFF
    class Route53 style1
    classDef style2 fill:#FF9900
    class ALB style2
    classDef style3 fill:#3B48CC
    class RDS style3
    classDef style4 fill:#569A31
    class S3 style4
```

### Multi-Region Active-Active

```mermaid
graph TB
    Users[Global Users] --> Route53["Route 53<br/>Geolocation or Latency Routing"]
    
    subgraph Primary_Region_us_east_1_Group["Primary Region: us-east-1"]
        ALB1[Application Load Balancer]
        
        ASG1["Auto Scaling Group<br/>EC2 Instances"]
        
        RDS1["Aurora Global Database<br/>Primary Region<br/>Read/Write"]
        
        S3_1["S3 Bucket<br/>us-east-1"]
        
        ALB1 --> ASG1
        ASG1 --> RDS1
        ASG1 --> S3_1
    end
    
    subgraph Secondary_Region_eu_west_1_Group["Secondary Region: eu-west-1"]
        ALB2[Application Load Balancer]
        
        ASG2["Auto Scaling Group<br/>EC2 Instances"]
        
        RDS2["Aurora Global Database<br/>Secondary Region<br/>Read/Write"]
        
        S3_2["S3 Bucket<br/>eu-west-1"]
        
        ALB2 --> ASG2
        ASG2 --> RDS2
        ASG2 --> S3_2
    end
    
    Route53 -->|US Traffic| ALB1
    Route53 -->|EU Traffic| ALB2
    
    RDS1 <-.Async Replication<br/>< 1 second.-> RDS2
    S3_1 <-.S3 Cross-Region<br/>Replication.-> S3_2
    
    DynamoDB["DynamoDB Global Tables<br/>Multi-region, multi-active"] --> ASG1
    DynamoDB --> ASG2
    
    Benefits["Benefits:<br/>✅ Low latency globally<br/>✅ High availability<br/>✅ Disaster recovery<br/>✅ Read/write in any region<br/>⚠️ Increased cost"]
    
    classDef style1 fill:#8C4FFF
    class Route53 style1
    classDef style2 fill:#3B48CC
    class RDS1 style2
    classDef style3 fill:#3B48CC
    class RDS2 style3
```

## Disaster Recovery Patterns

### DR Strategies Comparison

```mermaid
graph TB
    subgraph Backup_Restore_Group["Backup & Restore"]
        BR["Backup & Restore<br/>💰 Lowest cost<br/>⏱️ RTO: Hours-Days<br/>⏱️ RPO: Hours"]
        
        BR_Desc["• Data backed up to S3<br/>• Restore when needed<br/>• AMIs, DB snapshots<br/>• Manual or automated<br/>Use: Non-critical systems"]
    end
    
    subgraph Pilot_Light_Group["Pilot Light"]
        PL["Pilot Light<br/>💰 Low cost<br/>⏱️ RTO: Minutes-Hours<br/>⏱️ RPO: Minutes"]
        
        PL_Desc["• Core services always running<br/>• Database replication<br/>• Scale up when needed<br/>• Critical data ready<br/>Use: Core business systems"]
    end
    
    subgraph Warm_Standby_Group["Warm Standby"]
        WS["Warm Standby<br/>💰 Medium cost<br/>⏱️ RTO: Minutes<br/>⏱️ RPO: Seconds"]
        
        WS_Desc["• Scaled-down version running<br/>• All services active<br/>• Scale up for failover<br/>• DNS failover<br/>Use: Business-critical apps"]
    end
    
    subgraph Multi_Site_Active_Active_Group["Multi-Site Active/Active"]
        MS["Multi-Site<br/>💰 Highest cost<br/>⏱️ RTO: Real-time<br/>⏱️ RPO: Near-zero"]
        
        MS_Desc["• Full production in multiple regions<br/>• Active-active traffic<br/>• Instant failover<br/>• Route 53 routing<br/>Use: Mission-critical systems"]
    end
    
    BR --> PL
    PL --> WS
    WS --> MS
    
    Spectrum["Cost increases -&gt;<br/>RTO/RPO decreases -&gt;"]
    
    classDef style1 fill:#569A31
    class BR style1
    classDef style2 fill:#FF9900
    class PL style2
    classDef style3 fill:#146EB4
    class WS style3
    classDef style4 fill:#C00
    class MS style4
```

### Pilot Light Architecture

```mermaid
graph TB
    subgraph Production_Region_us_east_1_Group["Production Region: us-east-1"]
        Prod["Production Environment<br/>Fully operational"]
        
        ProdApp["Application Servers<br/>Auto Scaling"]
        ProdDB["RDS Primary<br/>Read/Write"]
        ProdS3["S3 Bucket<br/>Application data"]
        
        Prod --> ProdApp
        Prod --> ProdDB
        Prod --> ProdS3
    end
    
    subgraph DR_Region_us_west_2_Group["DR Region: us-west-2"]
        DR["DR Environment<br/>Pilot Light"]
        
        DRCore["Core Services:<br/>✅ Database running<br/>✅ Data replication active<br/>❌ App servers stopped<br/>❌ Minimal compute"]
        
        DRDB["RDS Replica<br/>Read-only replica<br/>Can be promoted"]
        DRS3["S3 Bucket<br/>Cross-region replication"]
        
        AMI["AMIs & Templates<br/>Ready to launch"]
        
        DR --> DRCore
        DR --> DRDB
        DR --> DRS3
        DR --> AMI
    end
    
    ProdDB -.Async Replication.-> DRDB
    ProdS3 -.Cross-Region Replication.-> DRS3
    
    Disaster[Disaster Event] -.Triggers.-> Failover["Failover Process:<br/>1. Promote RDS replica<br/>2. Launch app servers from AMI<br/>3. Update Route 53 DNS<br/>4. Scale to production capacity"]
    
    Failover --> DRCore
    
    Timeline["Timeline:<br/>Normal: Only DB running<br/>Disaster: 10-30 minutes to full capacity"]
    
    classDef style1 fill:#569A31
    class Prod style1
    classDef style2 fill:#FF9900
    class DR style2
    classDef style3 fill:#C00
    class Disaster style3
```

## Serverless Architectures

### Serverless Web Application

```mermaid
graph TB
    Users[Users] --> CloudFront["CloudFront<br/>CDN"]
    
    CloudFront --> S3Web["S3<br/>Static Website<br/>React/Angular/Vue"]
    
    S3Web --> API["API Gateway<br/>REST or HTTP API<br/>WebSocket"]
    
    API --> Cognito["Amazon Cognito<br/>User authentication<br/>JWT tokens"]
    
    API --> Lambda["Lambda Functions<br/>Business logic<br/>Node.js/Python"]
    
    Lambda --> DynamoDB["DynamoDB<br/>NoSQL database<br/>On-demand capacity"]
    
    Lambda --> S3Data["S3<br/>Object storage<br/>User uploads"]
    
    DynamoDB --> Streams[DynamoDB Streams]
    Streams --> LambdaStream["Lambda<br/>Stream processing"]
    
    LambdaStream --> SES["Amazon SES<br/>Email notifications"]
    
    S3Data --> EventBridge[EventBridge]
    EventBridge --> LambdaEvent["Lambda<br/>Event processing"]
    
    CloudWatch["CloudWatch<br/>Logs & Metrics"] -.Monitor.-> Lambda
    XRay["X-Ray<br/>Distributed tracing"] -.Trace.-> Lambda
    
    Benefits["Benefits:<br/>✅ No servers to manage<br/>✅ Auto-scaling<br/>✅ Pay per use<br/>✅ High availability built-in<br/>✅ Fast development"]
    
    classDef style1 fill:#FF9900
    class API style1
    classDef style2 fill:#569A31
    class Lambda style2
    classDef style3 fill:#146EB4
    class DynamoDB style3
```

### Event-Driven Serverless

```mermaid
graph LR
    subgraph Event_Sources_Group["Event Sources"]
        S3["S3<br/>File upload"]
        DDB["DynamoDB<br/>Table change"]
        SQS["SQS<br/>Message queue"]
        Schedule["EventBridge<br/>Schedule/Cron"]
    end
    
    subgraph Event_Processing_Group["Event Processing"]
        Lambda1["Lambda Function 1<br/>Image processing"]
        Lambda2["Lambda Function 2<br/>Data validation"]
        Lambda3["Lambda Function 3<br/>Notification"]
        Lambda4["Lambda Function 4<br/>Cleanup task"]
    end
    
    subgraph Orchestration_Group["Orchestration"]
        StepFunctions["Step Functions<br/>Workflow coordination<br/>Error handling"]
    end
    
    subgraph Destinations_Group["Destinations"]
        S3Out["S3<br/>Processed files"]
        SNS["SNS<br/>Notifications"]
        DDBOut["DynamoDB<br/>Results"]
        SQS_DLQ["SQS<br/>Dead letter queue"]
    end
    
    S3 -->|Trigger| Lambda1
    DDB -->|Stream| Lambda2
    SQS -->|Poll| Lambda3
    Schedule -->|Invoke| Lambda4
    
    Lambda1 --> StepFunctions
    Lambda2 --> StepFunctions
    
    StepFunctions --> S3Out
    StepFunctions --> SNS
    StepFunctions --> DDBOut
    
    Lambda1 -.Failures.-> SQS_DLQ
    Lambda2 -.Failures.-> SQS_DLQ
    
    classDef style1 fill:#FF9900
    class Lambda1 style1
    classDef style2 fill:#569A31
    class StepFunctions style2
```

## Microservices Patterns

### Container-Based Microservices

```mermaid
graph TB
    Users[Users] --> ALB["Application<br/>Load Balancer"]
    
    subgraph Amazon_ECS_EKS_Cluster_Group["Amazon ECS/EKS Cluster"]
        ALB --> Service1["User Service<br/>ECS Task<br/>Container"]
        ALB --> Service2["Product Service<br/>ECS Task<br/>Container"]
        ALB --> Service3["Order Service<br/>ECS Task<br/>Container"]
        
        Service1 --> ServiceMesh["AWS App Mesh<br/>Service mesh<br/>Traffic management"]
        Service2 --> ServiceMesh
        Service3 --> ServiceMesh
    end
    
    subgraph Data_Layer_Group["Data Layer"]
        Service1 --> DDB1["DynamoDB<br/>User data"]
        Service2 --> RDS1["RDS<br/>Product catalog"]
        Service3 --> Aurora["Aurora<br/>Orders"]
    end
    
    subgraph Async_Communication_Group["Async Communication"]
        Service1 --> SNS[SNS Topic]
        SNS --> SQS1[SQS Queue 1]
        SNS --> SQS2[SQS Queue 2]
        
        SQS1 --> Service2
        SQS2 --> Service3
    end
    
    subgraph Service_Discovery_Group["Service Discovery"]
        CloudMap["AWS Cloud Map<br/>Service registry<br/>DNS-based discovery"]
        
        Service1 -.Register.-> CloudMap
        Service2 -.Register.-> CloudMap
        Service3 -.Register.-> CloudMap
    end
    
    ECR["Amazon ECR<br/>Container registry"] -.Pull images.-> Service1
    
    Observability["CloudWatch Container Insights<br/>X-Ray tracing<br/>Centralized logging"] -.Monitor.-> Service1
    
    classDef style1 fill:#FF9900
    class ServiceMesh style1
    classDef style2 fill:#569A31
    class CloudMap style2
```

### API-First Microservices

```mermaid
graph TB
    Mobile[Mobile Apps] --> API["API Gateway<br/>Unified API"]
    Web[Web Apps] --> API
    Partners[Partner APIs] --> API
    
    subgraph API_Gateway_Features_Group["API Gateway Features"]
        Auth["Authorization<br/>Cognito/Lambda"]
        Cache[Response Caching]
        Throttle[Throttling & Quotas]
        Transform["Request/Response<br/>Transformation"]
        
        API --> Auth
        API --> Cache
        API --> Throttle
        API --> Transform
    end
    
    subgraph Microservices_Group["Microservices"]
        Lambda1["Lambda<br/>User Service"]
        Lambda2["Lambda<br/>Product Service"]
        ECS["ECS<br/>Order Service"]
        EC2["EC2<br/>Legacy Service"]
    end
    
    subgraph Backend_for_Frontend_BFF_Group["Backend for Frontend BFF"]
        BFF_Mobile["Mobile BFF<br/>Optimized for mobile"]
        BFF_Web["Web BFF<br/>Optimized for web"]
    end
    
    Auth --> Lambda1
    Auth --> Lambda2
    Auth --> ECS
    Auth --> EC2
    
    Lambda1 --> BFF_Mobile
    Lambda2 --> BFF_Mobile
    ECS --> BFF_Web
    
    Lambda1 --> DDB[DynamoDB]
    Lambda2 --> S3[S3]
    ECS --> RDS[RDS]
    
    WAF[AWS WAF] -.Protect.-> API
    Shield[AWS Shield] -.DDoS Protection.-> API
    
    classDef style1 fill:#FF9900
    class API style1
    classDef style2 fill:#569A31
    class Lambda1 style2
```

## Data Lake Architecture

### Comprehensive Data Lake

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        Streaming["Streaming Data<br/>Kinesis, IoT"]
        Batch["Batch Data<br/>Databases, Files"]
        RealTime["Real-time Apps<br/>APIs, Logs"]
    end
    
    subgraph Ingestion_Layer_Group["Ingestion Layer"]
        Kinesis["Kinesis Firehose<br/>Streaming ingestion"]
        DataSync["AWS DataSync<br/>Batch transfer"]
        DMS["AWS DMS<br/>Database migration"]
    end
    
    subgraph Storage_Layer_S3_Group["Storage Layer - S3"]
        Raw["Raw Zone<br/>Landing area<br/>Original format<br/>All data retained"]
        
        Processed["Processed Zone<br/>Cleaned & validated<br/>Parquet/ORC format<br/>Partitioned"]
        
        Curated["Curated Zone<br/>Business-ready<br/>Aggregated views<br/>Optimized for queries"]
    end
    
    subgraph Cataloging_Group["Cataloging"]
        Crawler["Glue Crawlers<br/>Schema discovery"]
        Catalog["Glue Data Catalog<br/>Metadata repository"]
        
        Crawler --> Catalog
    end
    
    subgraph Processing_Group["Processing"]
        Glue["AWS Glue<br/>ETL jobs<br/>Serverless Spark"]
        
        EMR["Amazon EMR<br/>Complex analytics<br/>ML processing"]
        
        Lambda["Lambda<br/>Real-time transforms"]
    end
    
    subgraph Analytics_ML_Group["Analytics & ML"]
        Athena["Athena<br/>Interactive SQL"]
        Redshift["Redshift Spectrum<br/>Data warehouse"]
        SageMaker["SageMaker<br/>Machine learning"]
        QuickSight["QuickSight<br/>BI dashboards"]
    end
    
    Streaming --> Kinesis
    Batch --> DataSync
    Batch --> DMS
    
    Kinesis --> Raw
    DataSync --> Raw
    DMS --> Raw
    
    Raw --> Glue
    Glue --> Processed
    
    Processed --> EMR
    EMR --> Curated
    
    Raw --> Crawler
    Processed --> Crawler
    Curated --> Crawler
    
    Catalog --> Athena
    Catalog --> Redshift
    
    Curated --> Athena
    Curated --> Redshift
    Curated --> SageMaker
    
    Athena --> QuickSight
    Redshift --> QuickSight
    
    LakeFormation["AWS Lake Formation<br/>Centralized governance<br/>Access control<br/>Data quality"] -.Governs.-> Raw
    
    classDef style1 fill:#C00
    class Raw style1
    classDef style2 fill:#FF9900
    class Processed style2
    classDef style3 fill:#569A31
    class Curated style3
    classDef style4 fill:#146EB4
    class Catalog style4
```

## Hybrid Cloud Patterns

### Hybrid Cloud Architecture

```mermaid
graph TB
    subgraph On_Premises_Data_Center_Group["On-Premises Data Center"]
        OnPrem[Corporate Network]
        AD[Active Directory]
        VMs[Virtual Machines]
        Storage[Storage Arrays]
        Apps[Legacy Applications]
    end
    
    subgraph AWS_Connectivity_Group["AWS Connectivity"]
        VPN["AWS VPN<br/>Encrypted tunnel"]
        DX["AWS Direct Connect<br/>Dedicated connection"]
        
        TGW["Transit Gateway<br/>Central hub"]
    end
    
    subgraph AWS_Cloud_Group["AWS Cloud"]
        subgraph VPC_Group["VPC"]
            PrivateSubnet[Private Subnets]
            Workloads[EC2 Workloads]
            
            PrivateSubnet --> Workloads
        end
        
        subgraph Hybrid_Services_Group["Hybrid Services"]
            DirectoryService["AWS Managed<br/>Microsoft AD<br/>Trust relationship"]
            
            StorageGW["Storage Gateway<br/>Hybrid storage"]
            
            Outposts["AWS Outposts<br/>On-prem AWS"]
            
            VMware["VMware Cloud<br/>on AWS"]
        end
        
        subgraph AWS_Services_Group["AWS Services"]
            S3[S3]
            RDS[RDS]
            Lambda[Lambda]
        end
    end
    
    OnPrem --> VPN
    OnPrem --> DX
    
    VPN --> TGW
    DX --> TGW
    
    TGW --> PrivateSubnet
    
    AD <-.Trust.-> DirectoryService
    Storage <-.Sync.-> StorageGW
    VMs -.Migrate.-> VMware
    
    StorageGW --> S3
    Workloads --> RDS
    Workloads --> Lambda
    
    SSM["Systems Manager<br/>Unified management"] -.Manage.-> Workloads
    SSM -.Manage.-> OnPrem
    
    classDef style1 fill:#FF9900
    class TGW style1
    classDef style2 fill:#569A31
    class DirectoryService style2
    classDef style3 fill:#146EB4
    class DX style3
```

## Caching Strategies

### Multi-Layer Caching

```mermaid
graph TB
    User[User Request] --> CF["CloudFront<br/>Edge Cache<br/>TTL: Hours/Days<br/>Global distribution"]
    
    CF -->|Cache Miss| ALB["Application<br/>Load Balancer"]
    CF -->|Cache Hit| UserHit1["Return cached<br/>response"]
    
    ALB --> AppServer["Application Server<br/>EC2/ECS"]
    
    AppServer --> AppCache{"Application<br/>Cache Layer?"}
    
    AppCache -->|Check| ElastiCache["ElastiCache Redis<br/>In-memory cache<br/>TTL: Minutes/Hours<br/>Session data, objects"]
    
    ElastiCache -->|Cache Hit| AppServer
    ElastiCache -->|Cache Miss| DBQuery[Query Database]
    
    DBQuery --> RDS["RDS with<br/>Read Replicas<br/>Query cache enabled"]
    
    RDS --> ElastiCache
    ElastiCache --> AppServer
    AppServer --> CF
    CF --> User
    
    Strategies["Caching Strategies:<br/><br/>CloudFront: Static content, API responses<br/>ElastiCache: Session data, computed results<br/>RDS: Query results<br/>Application: Business logic results<br/><br/>Benefits:<br/>✅ Reduced latency<br/>✅ Lower database load<br/>✅ Cost savings<br/>✅ Better user experience"]
    
    classDef style1 fill:#146EB4
    class CF style1
    classDef style2 fill:#C00
    class ElastiCache style2
    classDef style3 fill:#3B48CC
    class RDS style3
```

