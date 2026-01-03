# Compute Services - Mermaid Diagrams

## EC2 Overview

### EC2 Instance Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Pending: Launch Instance
    Pending --> Running: Instance Ready
    
    Running --> Stopping: Stop Instance
    Running --> ShuttingDown: Terminate Instance
    Running --> Running: Reboot Instance
    
    Stopping --> Stopped: Instance Stopped
    Stopped --> Pending: Start Instance
    Stopped --> Terminated: Terminate Instance
    
    ShuttingDown --> Terminated: Termination Complete
    Terminated --> [*]
    
    note right of Running
        Instance is billable
        Can connect and use
    end note
    
    note right of Stopped
        EBS volumes persist
        Not billable (only EBS)
    end note
```

### EC2 Instance Types (CRAM FACTS)

```mermaid
mindmap
    root((EC2 Instance<br/>Types))
        General Purpose
            T - Burstable
                t2, t3, t4g
                Web servers
                Dev environments
            M - Balanced
                m5, m6i, m7g
                Application servers
                Enterprise apps
        Compute Optimized
            C - Compute
                c5, c6i, c7g
                Batch processing
                Gaming servers
                HPC
                Machine learning
        Memory Optimized
            R - RAM
                r5, r6i, r7g
                Databases
                In-memory caches
            X - Extreme Memory
                x1, x2
                SAP HANA
                Big data
        Storage Optimized
            I - IOPS
                i3, i4i
                NoSQL databases
                Data warehousing
            D - Dense Storage
                d2, d3
                Hadoop
                Data lakes
            H - HDD Storage
                h1
                MapReduce
                HDFS
        Accelerated Computing
            P - GPU
                p3, p4
                ML training
                Deep learning
            G - Graphics
                g4, g5
                Video encoding
                Gaming
            F - FPGA
                f1
                Genomics
                Financial analysis
```

### EC2 Pricing Models Comparison

```mermaid
graph TB
    subgraph "Pricing Models"
        OnDemand[On-Demand<br/>💰 No Discount<br/>⏱️ Pay by hour/second<br/>📊 Flexible]
        Reserved[Reserved Instances<br/>💰 Up to 72% Discount<br/>⏱️ 1 or 3 years<br/>📊 Steady workloads]
        Savings[Savings Plans<br/>💰 Up to 66% Discount<br/>⏱️ 1 or 3 years<br/>📊 Flexible instance type]
        Spot[Spot Instances<br/>💰 Up to 90% Discount<br/>⏱️ Can be terminated<br/>📊 Fault-tolerant]
        Dedicated[Dedicated Hosts<br/>💰 No Discount<br/>⏱️ Physical server<br/>📊 Compliance/Licensing]
    end
    
    subgraph "Use Cases"
        OnDemand --> UC1[Short-term workloads<br/>Unpredictable patterns<br/>Development/Testing]
        Reserved --> UC2[Production databases<br/>Steady-state applications<br/>Predictable usage]
        Savings --> UC3[Flexible compute needs<br/>Commitment without lock-in<br/>Mixed workloads]
        Spot --> UC4[Batch jobs<br/>Data analysis<br/>Background processing<br/>CI/CD]
        Dedicated --> UC5[Regulatory requirements<br/>License restrictions<br/>Multi-tenant isolation]
    end
    
    style OnDemand fill:#FF9900
    style Reserved fill:#146EB4
    style Spot fill:#569A31
```

### EC2 Placement Groups

```mermaid
graph TB
    subgraph "Cluster Placement Group"
        direction LR
        AZ1[Same AZ]
        I1[Instance 1] -.Low Latency.-> I2[Instance 2]
        I2 -.Low Latency.-> I3[Instance 3]
        I3 -.Low Latency.-> I1
        I1 --> AZ1
        I2 --> AZ1
        I3 --> AZ1
    end
    
    subgraph "Spread Placement Group"
        direction TB
        AZa[AZ-1a: Max 7 Instances]
        AZb[AZ-1b: Max 7 Instances]
        AZc[AZ-1c: Max 7 Instances]
        
        S1[Instance 1<br/>Isolated Hardware] --> AZa
        S2[Instance 2<br/>Isolated Hardware] --> AZb
        S3[Instance 3<br/>Isolated Hardware] --> AZc
        S4[Instance 4<br/>Isolated Hardware] --> AZa
    end
    
    subgraph "Partition Placement Group"
        direction TB
        P1[Partition 1<br/>Rack 1<br/>Instances A,B,C]
        P2[Partition 2<br/>Rack 2<br/>Instances D,E,F]
        P3[Partition 3<br/>Rack 3<br/>Instances G,H,I]
    end
    
    Use1[HPC, Big Data<br/>Low Latency Required] -.Use.-> I1
    Use2[Critical Applications<br/>High Availability] -.Use.-> S1
    Use3[Hadoop, Kafka, Cassandra<br/>Large Distributed Systems] -.Use.-> P1
    
    style I1 fill:#C00
    style S1 fill:#FF9900
    style P1 fill:#146EB4
```

## Auto Scaling

### Auto Scaling Architecture

```mermaid
graph TB
    Users[Users] --> ALB[Application Load Balancer]
    
    subgraph "Auto Scaling Group"
        ASG[Auto Scaling Group<br/>Min: 2, Desired: 4, Max: 8]
        
        subgraph "AZ-1a"
            EC2_1a_1[EC2 Instance]
            EC2_1a_2[EC2 Instance]
        end
        
        subgraph "AZ-1b"
            EC2_1b_1[EC2 Instance]
            EC2_1b_2[EC2 Instance]
        end
        
        subgraph "AZ-1c"
            EC2_1c_1[EC2 Instance]
        end
    end
    
    ALB --> EC2_1a_1
    ALB --> EC2_1a_2
    ALB --> EC2_1b_1
    ALB --> EC2_1b_2
    ALB --> EC2_1c_1
    
    CloudWatch[CloudWatch Alarms] -->|CPU > 70%| ScaleOut[Scale Out +2]
    CloudWatch -->|CPU < 30%| ScaleIn[Scale In -1]
    
    ScaleOut --> ASG
    ScaleIn --> ASG
    
    LaunchTemplate[Launch Template<br/>AMI, Instance Type,<br/>Security Groups, IAM Role] -.Defines.-> ASG
    
    style ASG fill:#FF9900
    style CloudWatch fill:#8C4FFF
    style LaunchTemplate fill:#146EB4
```

### Auto Scaling Policies

```mermaid
graph TB
    subgraph "Scaling Policies"
        Target[Target Tracking Scaling<br/>Maintain metric at target<br/>e.g., CPU at 50%]
        Step[Step Scaling<br/>Scale based on CloudWatch alarms<br/>Different steps for different thresholds]
        Simple[Simple Scaling<br/>Single adjustment<br/>Wait for cooldown]
        Scheduled[Scheduled Scaling<br/>Time-based scaling<br/>Predictable patterns]
        Predictive[Predictive Scaling<br/>ML-based forecasting<br/>Analyze historical data]
    end
    
    subgraph "Metrics"
        Target --> M1[CPU Utilization<br/>Request Count<br/>Network I/O]
        Step --> M2[CPU > 80%: +3<br/>CPU > 60%: +2<br/>CPU > 40%: +1]
        Scheduled --> M3[Weekday 9AM: Scale to 10<br/>Weekday 6PM: Scale to 2]
        Predictive --> M4[Predict daily traffic patterns<br/>Pre-scale before load]
    end
    
    style Target fill:#FF9900
    style Predictive fill:#569A31
```

### Auto Scaling Lifecycle

```mermaid
sequenceDiagram
    participant ASG as Auto Scaling Group
    participant LC as Launch Template
    participant EC2
    participant ELB as Load Balancer
    participant CW as CloudWatch
    
    Note over ASG: Scale Out Event Triggered
    
    ASG->>LC: Request Instance Configuration
    LC->>ASG: Instance Details (AMI, Type, etc)
    ASG->>EC2: Launch New Instance
    EC2->>EC2: Pending → Running
    
    opt Lifecycle Hook
        EC2->>ASG: Pending:Wait
        Note over EC2: Run bootstrap scripts
        EC2->>ASG: Complete Lifecycle Action
    end
    
    EC2->>ELB: Register Instance
    ELB->>EC2: Health Check
    EC2->>ELB: Healthy
    ELB->>ASG: Instance InService
    
    Note over EC2: Instance now serving traffic
    
    EC2->>CW: Send Metrics
    CW->>ASG: Monitor Metrics
    
    alt Scale In Needed
        ASG->>ELB: Deregister Instance
        ELB->>ELB: Connection Draining (300s)
        ASG->>EC2: Terminate Instance
    end
    
    style ASG fill:#FF9900
```

## Elastic Load Balancing

### Load Balancer Types Comparison

```mermaid
graph TB
    subgraph "Application Load Balancer (ALB)"
        ALB[Layer 7 - HTTP/HTTPS]
        ALB --> ALBFeatures[• Path-based routing<br/>• Host-based routing<br/>• Lambda targets<br/>• WebSocket support<br/>• HTTP/2 support]
        ALBFeatures --> ALBUse[Microservices<br/>Containers<br/>Web Applications]
    end
    
    subgraph "Network Load Balancer (NLB)"
        NLB[Layer 4 - TCP/UDP/TLS]
        NLB --> NLBFeatures[• Ultra-high performance<br/>• Static IP addresses<br/>• Preserve source IP<br/>• Millions of req/sec]
        NLBFeatures --> NLBUse[Gaming<br/>IoT<br/>TCP/UDP traffic]
    end
    
    subgraph "Gateway Load Balancer (GWLB)"
        GWLB[Layer 3 - IP Packets]
        GWLB --> GWLBFeatures[• Deploy virtual appliances<br/>• Transparent to applications<br/>• GENEVE protocol]
        GWLBFeatures --> GWLBUse[Firewalls<br/>IDS/IPS<br/>Deep packet inspection]
    end
    
    subgraph "Classic Load Balancer (CLB)"
        CLB[Layer 4 & 7 - Legacy]
        CLB --> CLBNote[❌ Not recommended<br/>For new applications]
    end
    
    style ALB fill:#FF9900
    style NLB fill:#146EB4
    style GWLB fill:#569A31
    style CLB fill:#999
```

### ALB Request Routing

```mermaid
graph TB
    Client[Client Request] --> ALB[Application Load Balancer]
    
    ALB --> Rule1{Path: /api/*}
    ALB --> Rule2{Path: /images/*}
    ALB --> Rule3{Host: mobile.example.com}
    ALB --> Rule4{Header: X-Custom-Header}
    
    Rule1 -->|Match| TG1[Target Group 1<br/>API Servers<br/>Port 8080]
    Rule2 -->|Match| TG2[Target Group 2<br/>Image Servers<br/>Port 8081]
    Rule3 -->|Match| TG3[Target Group 3<br/>Mobile Backend<br/>Port 8082]
    Rule4 -->|Match| TG4[Target Group 4<br/>Lambda Functions]
    
    TG1 --> EC2_1[EC2 Instance 1]
    TG1 --> EC2_2[EC2 Instance 2]
    
    TG2 --> EC2_3[EC2 Instance 3]
    TG2 --> EC2_4[EC2 Instance 4]
    
    TG3 --> EC2_5[EC2 Instance 5]
    
    TG4 --> Lambda[Lambda Function]
    
    style ALB fill:#FF9900
    style TG1 fill:#146EB4
    style TG4 fill:#569A31
```

### Load Balancer with Health Checks

```mermaid
sequenceDiagram
    participant ELB as Load Balancer
    participant TG as Target Group
    participant EC2_1 as EC2 Instance 1
    participant EC2_2 as EC2 Instance 2
    participant EC2_3 as EC2 Instance 3
    
    loop Health Check (Every 30s)
        ELB->>EC2_1: GET /health
        EC2_1->>ELB: 200 OK (Healthy)
        
        ELB->>EC2_2: GET /health
        EC2_2->>ELB: 200 OK (Healthy)
        
        ELB->>EC2_3: GET /health
        EC2_3->>ELB: 500 Error (Unhealthy)
    end
    
    Note over ELB,EC2_3: After 2 consecutive failures
    
    ELB->>TG: Mark EC2_3 as Unhealthy
    
    Note over ELB: Traffic only to EC2_1 and EC2_2
    
    Client->>ELB: New Request
    ELB->>EC2_1: Route Traffic (EC2_3 excluded)
    
    loop Continue Health Checks
        ELB->>EC2_3: GET /health
        EC2_3->>ELB: 200 OK (Healthy)
    end
    
    Note over ELB,EC2_3: After 3 consecutive successes
    
    ELB->>TG: Mark EC2_3 as Healthy
    
    style ELB fill:#FF9900
```

### Cross-Zone Load Balancing

```mermaid
graph TB
    subgraph "With Cross-Zone Load Balancing"
        ALB1[Load Balancer]
        
        subgraph "AZ-1a"
            E1[EC2 - 25%]
            E2[EC2 - 25%]
        end
        
        subgraph "AZ-1b"
            E3[EC2 - 25%]
            E4[EC2 - 25%]
        end
        
        ALB1 --> E1
        ALB1 --> E2
        ALB1 --> E3
        ALB1 --> E4
    end
    
    subgraph "Without Cross-Zone Load Balancing"
        NLB1[Load Balancer Node 1<br/>AZ-1a]
        NLB2[Load Balancer Node 2<br/>AZ-1b]
        
        subgraph "AZ-1a "
            N1[EC2 - 25%]
            N2[EC2 - 25%]
        end
        
        subgraph "AZ-1b "
            N3[EC2 - 50%]
        end
        
        NLB1 --> N1
        NLB1 --> N2
        NLB2 --> N3
    end
    
    style ALB1 fill:#569A31
    style NLB1 fill:#C00
    style NLB2 fill:#C00
```

## AWS Lambda

### Lambda Execution Model

```mermaid
graph LR
    subgraph "Event Sources"
        API[API Gateway]
        S3[S3 Events]
        DDB[DynamoDB Streams]
        SQS[SQS Queue]
        SNS[SNS Topic]
        EventBridge[EventBridge]
        ALB[ALB]
    end
    
    subgraph "Lambda Function"
        Handler[Function Handler<br/>Your Code]
        Runtime[Runtime Environment<br/>Python/Node.js/Java/etc]
        Execution[Execution Context]
        
        Handler --> Runtime
        Runtime --> Execution
    end
    
    subgraph "AWS Services"
        S3Out[S3]
        DDBOut[DynamoDB]
        RDS[RDS Proxy]
        SES[SES]
    end
    
    API --> Handler
    S3 --> Handler
    DDB --> Handler
    SQS --> Handler
    SNS --> Handler
    EventBridge --> Handler
    ALB --> Handler
    
    Execution --> S3Out
    Execution --> DDBOut
    Execution --> RDS
    Execution --> SES
    
    IAM[IAM Execution Role] -.Permissions.-> Execution
    
    style Handler fill:#FF9900
    style Execution fill:#569A31
```

### Lambda Invocation Types

```mermaid
graph TB
    subgraph "Synchronous Invocation"
        Client1[Client] -->|Invoke| Lambda1[Lambda Function]
        Lambda1 -->|Return Response| Client1
        Examples1[Examples:<br/>• API Gateway<br/>• ALB<br/>• CLI invoke]
        
        Note1[⏱️ Wait for response<br/>🔁 Retry 0 times<br/>❌ Client handles errors]
    end
    
    subgraph "Asynchronous Invocation"
        Client2[Event Source] -->|Send Event| Queue[Event Queue]
        Queue -->|Process| Lambda2[Lambda Function]
        Lambda2 -.Success.-> Success[Success]
        Lambda2 -.Failure.-> Retry[Retry 2x]
        Retry -.Still Fails.-> DLQ[Dead Letter Queue<br/>SQS/SNS]
        
        Examples2[Examples:<br/>• S3<br/>• SNS<br/>• EventBridge<br/>• CloudWatch Events]
        
        Note2[⚡ Returns immediately<br/>🔁 Retry 2 times<br/>☠️ DLQ for failures]
    end
    
    subgraph "Event Source Mapping"
        Stream[Stream/Queue] -.Poll.-> Lambda3[Lambda Function]
        
        Kinesis[Kinesis Streams]
        DynamoDB[DynamoDB Streams]
        SQS2[SQS Queue]
        
        Kinesis --> Stream
        DynamoDB --> Stream
        SQS2 --> Stream
        
        Lambda3 --> Batch[Process Batch]
        
        Note3[📦 Batch processing<br/>🔁 Retry entire batch<br/>⏸️ Can pause polling]
    end
    
    style Lambda1 fill:#FF9900
    style Lambda2 fill:#146EB4
    style Lambda3 fill:#569A31
```

### Lambda Architecture Limits

```mermaid
graph TB
    subgraph "Lambda Limits"
        Memory[Memory<br/>128 MB - 10 GB<br/>⚙️ Configurable in 1 MB increments]
        
        Timeout[Timeout<br/>⏱️ 15 minutes maximum<br/>⚙️ Default: 3 seconds]
        
        Concurrent[Concurrent Executions<br/>🔢 1,000 default per region<br/>📈 Can request increase]
        
        EnvVars[Environment Variables<br/>📝 4 KB total<br/>🔐 Can encrypt with KMS]
        
        Deployment[Deployment Package<br/>📦 50 MB zipped<br/>📂 250 MB unzipped<br/>💾 /tmp storage: 512 MB - 10 GB]
        
        Layers[Lambda Layers<br/>📚 5 layers per function<br/>📦 50 MB per layer]
    end
    
    subgraph "Performance Tips"
        Memory --> Perf1[More Memory =<br/>More CPU Power]
        Timeout --> Perf2[Set realistic timeout<br/>to avoid waste]
        Concurrent --> Perf3[Reserve concurrent<br/>for critical functions]
        Deployment --> Perf4[Use layers for<br/>shared dependencies]
    end
    
    style Memory fill:#FF9900
    style Concurrent fill:#146EB4
```

### Lambda Cold Start vs Warm Start

```mermaid
sequenceDiagram
    participant Event
    participant Lambda Service
    participant Container
    participant Function
    
    Note over Event,Function: Cold Start (First Invocation)
    Event->>Lambda Service: Invoke Function
    Lambda Service->>Container: Download Code
    Lambda Service->>Container: Start New Container
    Container->>Container: Initialize Runtime
    Container->>Function: Load Function Code
    Function->>Function: Run Init Code (outside handler)
    Function->>Function: Execute Handler
    Function->>Event: Return Response
    Note over Container: Container kept warm for ~15 min
    
    Note over Event,Function: Warm Start (Subsequent Invocation)
    Event->>Lambda Service: Invoke Function
    Lambda Service->>Container: Use Existing Container
    Container->>Function: Execute Handler
    Function->>Event: Return Response
    
    Note over Event,Function: Cold Start: 100ms - several seconds<br/>Warm Start: Single-digit milliseconds
    
    style Container fill:#FF9900
    style Function fill:#569A31
```

## Container Services

### ECS Architecture

```mermaid
graph TB
    subgraph "ECS Cluster"
        subgraph "EC2 Launch Type"
            EC2_1[EC2 Instance 1<br/>ECS Agent]
            EC2_2[EC2 Instance 2<br/>ECS Agent]
            
            Task1[Task 1<br/>Container A<br/>Container B]
            Task2[Task 2<br/>Container C]
            Task3[Task 3<br/>Container D<br/>Container E]
            
            Task1 --> EC2_1
            Task2 --> EC2_1
            Task3 --> EC2_2
        end
        
        subgraph "Fargate Launch Type"
            FargateTask1[Task 1<br/>Serverless]
            FargateTask2[Task 2<br/>Serverless]
            FargateTask3[Task 3<br/>Serverless]
        end
    end
    
    ECR[Elastic Container Registry<br/>Docker Images] -.Pull Images.-> Task1
    ECR -.Pull Images.-> FargateTask1
    
    TaskDef[Task Definition<br/>Image, CPU, Memory,<br/>IAM Role, Networking] -.Defines.-> Task1
    TaskDef -.Defines.-> FargateTask1
    
    Service[ECS Service<br/>Desired Count,<br/>Auto Scaling,<br/>Load Balancer] -.Manages.-> Task1
    Service -.Manages.-> FargateTask1
    
    ALB[Application Load Balancer] --> Task1
    ALB --> FargateTask1
    
    style EC2_1 fill:#FF9900
    style FargateTask1 fill:#569A31
    style ECR fill:#146EB4
```

### ECS vs EKS vs Fargate

```mermaid
graph TB
    subgraph "Amazon ECS"
        ECS[Elastic Container Service]
        ECS --> ECSFeatures[• AWS-native<br/>• Simple setup<br/>• Deep AWS integration<br/>• ECS Agent]
        ECSFeatures --> ECSUse[Use when:<br/>AWS-focused<br/>Simpler orchestration<br/>Tight AWS integration]
    end
    
    subgraph "Amazon EKS"
        EKS[Elastic Kubernetes Service]
        EKS --> EKSFeatures[• Kubernetes-native<br/>• Standard K8s API<br/>• Portable workloads<br/>• Complex but powerful]
        EKSFeatures --> EKSUse[Use when:<br/>Already using Kubernetes<br/>Multi-cloud strategy<br/>Complex orchestration]
    end
    
    subgraph "AWS Fargate"
        Fargate[Fargate]
        Fargate --> FargateFeatures[• Serverless containers<br/>• No server management<br/>• Works with ECS & EKS<br/>• Pay per task]
        FargateFeatures --> FargateUse[Use when:<br/>Don't want to manage servers<br/>Unpredictable workloads<br/>Quick deployment]
    end
    
    Both[ECS & EKS] -.Can use.-> Fargate
    
    style ECS fill:#FF9900
    style EKS fill:#146EB4
    style Fargate fill:#569A31
```

### Container Task Networking (awsvpc Mode)

```mermaid
graph TB
    subgraph "VPC"
        subgraph "Subnet"
            ENI1[ENI 1<br/>Private IP: 10.0.1.10]
            ENI2[ENI 2<br/>Private IP: 10.0.1.11]
            ENI3[ENI 3<br/>Private IP: 10.0.1.12]
            
            Task1[ECS Task 1<br/>Container App] --> ENI1
            Task2[ECS Task 2<br/>Container App] --> ENI2
            Task3[ECS Task 3<br/>Container App] --> ENI3
        end
        
        SG[Security Group<br/>Port 80, 443]
        
        ENI1 --> SG
        ENI2 --> SG
        ENI3 --> SG
    end
    
    ALB[Load Balancer] --> ENI1
    ALB --> ENI2
    ALB --> ENI3
    
    Note[✅ Each task has own ENI<br/>✅ Full VPC networking<br/>✅ Security Groups per task<br/>✅ Required for Fargate]
    
    style Task1 fill:#FF9900
    style SG fill:#146EB4
```

## Elastic Beanstalk

### Beanstalk Architecture

```mermaid
graph TB
    Developer[Developer] -->|Upload Code| EB[Elastic Beanstalk]
    
    EB --> Components{Components Provisioned}
    
    Components --> EC2[EC2 Instances<br/>Auto Scaling Group]
    Components --> ELB[Elastic Load Balancer]
    Components --> RDS[RDS Database<br/>Optional]
    Components --> S3[S3 Bucket<br/>Code Storage]
    Components --> CloudWatch[CloudWatch<br/>Monitoring]
    
    subgraph "Deployment Options"
        AllAtOnce[All at Once<br/>⚡ Fastest<br/>❌ Downtime]
        Rolling[Rolling<br/>⚙️ Batch updates<br/>✅ No downtime<br/>⚠️ Reduced capacity]
        RollingExtra[Rolling with Extra Batch<br/>⚙️ Launch new batch first<br/>✅ Full capacity]
        Immutable[Immutable<br/>🆕 New ASG<br/>✅ Zero downtime<br/>💰 Double capacity temp]
        BlueGreen[Blue/Green<br/>🔄 Separate environment<br/>✅ Instant rollback<br/>💰 Double cost]
    end
    
    EB -.Deployment Strategy.-> AllAtOnce
    EB -.Deployment Strategy.-> Immutable
    
    style EB fill:#FF9900
    style Immutable fill:#569A31
```

### Beanstalk Environments

```mermaid
graph LR
    subgraph "Web Server Environment"
        WEB[Web Server Tier]
        WEB --> WEBComponents[• ELB<br/>• Auto Scaling Group<br/>• EC2 Instances<br/>• Security Groups]
        WEBComponents --> WEBUse[Traditional web apps<br/>REST APIs<br/>HTTP/HTTPS traffic]
    end
    
    subgraph "Worker Environment"
        WORKER[Worker Tier]
        WORKER --> WORKERComponents[• SQS Queue<br/>• Auto Scaling Group<br/>• EC2 Instances<br/>• IAM Roles]
        WORKERComponents --> WORKERUse[Background processing<br/>Batch jobs<br/>Async tasks]
    end
    
    Client[Client] --> WEB
    WEB -->|Send tasks| WORKER
    
    style WEB fill:#FF9900
    style WORKER fill:#146EB4
```

## Instance Metadata Service (IMDS)

### IMDS Access Pattern

```mermaid
sequenceDiagram
    participant App as Application on EC2
    participant IMDS as Instance Metadata Service
    participant IAM
    
    Note over App,IMDS: IMDSv2 (Session-based, more secure)
    
    App->>IMDS: PUT /latest/api/token<br/>X-aws-ec2-metadata-token-ttl-seconds: 21600
    IMDS->>App: Return Session Token
    
    App->>IMDS: GET /latest/meta-data/instance-id<br/>X-aws-ec2-metadata-token: [token]
    IMDS->>App: i-1234567890abcdef0
    
    App->>IMDS: GET /latest/meta-data/iam/security-credentials/role-name<br/>X-aws-ec2-metadata-token: [token]
    IMDS->>IAM: Retrieve temporary credentials
    IAM->>IMDS: Access Key, Secret, Token
    IMDS->>App: Return Credentials
    
    Note over App: Use credentials to access AWS services
    
    App->>IMDS: GET /latest/user-data<br/>X-aws-ec2-metadata-token: [token]
    IMDS->>App: Bootstrap script content
    
    style IMDS fill:#FF9900
```

### Common IMDS Endpoints

```mermaid
mindmap
    root((IMDS Endpoints<br/>169.254.169.254))
        /latest/meta-data/
            instance-id
            instance-type
            local-ipv4
            public-ipv4
            security-groups
            iam/security-credentials/
            placement/availability-zone
            network/interfaces/
        /latest/user-data/
            Bootstrap scripts
            Configuration data
        /latest/dynamic/
            instance-identity/document
            instance-identity/signature
```

