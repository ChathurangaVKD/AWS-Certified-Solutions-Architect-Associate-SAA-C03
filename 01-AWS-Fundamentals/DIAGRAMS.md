# AWS Fundamentals - Mermaid Diagrams

## AWS Global Infrastructure

### Regions and Availability Zones Architecture

```mermaid
graph TB
    subgraph "AWS Global Infrastructure"
        subgraph "Region: us-east-1"
            AZ1[AZ: us-east-1a<br/>Data Center 1<br/>Data Center 2]
            AZ2[AZ: us-east-1b<br/>Data Center 1<br/>Data Center 2]
            AZ3[AZ: us-east-1c<br/>Data Center 1<br/>Data Center 2]
        end
        
        subgraph "Region: eu-west-1"
            AZ4[AZ: eu-west-1a<br/>Data Center 1<br/>Data Center 2]
            AZ5[AZ: eu-west-1b<br/>Data Center 1<br/>Data Center 2]
            AZ6[AZ: eu-west-1c<br/>Data Center 1<br/>Data Center 2]
        end
        
        subgraph "Region: ap-southeast-1"
            AZ7[AZ: ap-southeast-1a<br/>Data Center 1<br/>Data Center 2]
            AZ8[AZ: ap-southeast-1b<br/>Data Center 1<br/>Data Center 2]
            AZ9[AZ: ap-southeast-1c<br/>Data Center 1<br/>Data Center 2]
        end
    end
    
    AZ1 -.Low Latency Link.-> AZ2
    AZ2 -.Low Latency Link.-> AZ3
    AZ3 -.Low Latency Link.-> AZ1
    
    AZ4 -.Low Latency Link.-> AZ5
    AZ5 -.Low Latency Link.-> AZ6
    AZ6 -.Low Latency Link.-> AZ4
    
    AZ7 -.Low Latency Link.-> AZ8
    AZ8 -.Low Latency Link.-> AZ9
    AZ9 -.Low Latency Link.-> AZ7
    
    style AZ1 fill:#FF9900
    style AZ2 fill:#FF9900
    style AZ3 fill:#FF9900
    style AZ4 fill:#FF9900
    style AZ5 fill:#FF9900
    style AZ6 fill:#FF9900
    style AZ7 fill:#FF9900
    style AZ8 fill:#FF9900
    style AZ9 fill:#FF9900
```

### Edge Locations and CloudFront Distribution

```mermaid
graph LR
    User1[User in NYC] --> Edge1[Edge Location<br/>New York]
    User2[User in London] --> Edge2[Edge Location<br/>London]
    User3[User in Tokyo] --> Edge3[Edge Location<br/>Tokyo]
    User4[User in Sydney] --> Edge4[Edge Location<br/>Sydney]
    
    Edge1 --> CloudFront[Amazon CloudFront<br/>CDN]
    Edge2 --> CloudFront
    Edge3 --> CloudFront
    Edge4 --> CloudFront
    
    CloudFront --> Origin[Origin Server<br/>S3 / EC2 / ALB]
    
    style Edge1 fill:#146EB4
    style Edge2 fill:#146EB4
    style Edge3 fill:#146EB4
    style Edge4 fill:#146EB4
    style CloudFront fill:#FF9900
    style Origin fill:#569A31
```

### Region Selection Decision Flow

```mermaid
flowchart TD
    Start([Start: Need to Choose Region]) --> Q1{Data Sovereignty<br/>Requirements?}
    Q1 -->|Yes| RegionCompliance[Choose Region<br/>Based on Compliance]
    Q1 -->|No| Q2{Where are<br/>your users?}
    
    Q2 --> Proximity[Choose Closest Region<br/>for Low Latency]
    
    Proximity --> Q3{Service Available<br/>in Region?}
    Q3 -->|Yes| Q4{Check Pricing}
    Q3 -->|No| AltRegion[Choose Alternative<br/>Region]
    
    Q4 --> Final[Selected Region]
    RegionCompliance --> Final
    AltRegion --> Q3
    
    style Start fill:#232F3E
    style Final fill:#569A31
    style Q1 fill:#FF9900
    style Q2 fill:#FF9900
    style Q3 fill:#FF9900
    style Q4 fill:#FF9900
```

## AWS Well-Architected Framework

### Six Pillars Overview

```mermaid
mindmap
    root((AWS Well-Architected<br/>Framework))
        Operational Excellence
            IaC
            Monitoring
            Learn from Failures
            Frequent Small Changes
        Security
            IAM
            Detective Controls
            Infrastructure Protection
            Data Protection
            Incident Response
        Reliability
            Foundations
            Workload Architecture
            Change Management
            Failure Management
        Performance Efficiency
            Selection
            Review
            Monitoring
            Tradeoffs
        Cost Optimization
            Practice Cloud Financial Management
            Expenditure Awareness
            Cost-Effective Resources
            Manage Demand and Supply
        Sustainability
            Understand Impact
            Maximize Utilization
            Adopt New Services
            Reduce Downstream Impact
```

### Well-Architected Framework Pillars Details

```mermaid
graph TB
    subgraph "Operational Excellence"
        OE1[Infrastructure as Code]
        OE2[Annotated Documentation]
        OE3[Frequent Small Reversible Changes]
        OE4[Refine Operations Procedures]
        OE5[Learn from Failures]
    end
    
    subgraph "Security"
        S1[Identity & Access Management]
        S2[Detective Controls]
        S3[Infrastructure Protection]
        S4[Data Protection]
        S5[Incident Response]
    end
    
    subgraph "Reliability"
        R1[Recover from Failures]
        R2[Test Recovery Procedures]
        R3[Scale Horizontally]
        R4[Manage Change Automatically]
    end
    
    subgraph "Performance Efficiency"
        P1[Use Advanced Technologies]
        P2[Deploy Globally in Minutes]
        P3[Use Serverless]
        P4[Experiment More Often]
    end
    
    subgraph "Cost Optimization"
        C1[Adopt Consumption Model]
        C2[Measure Overall Efficiency]
        C3[Stop Spending on Undifferentiated Work]
        C4[Analyze and Attribute]
    end
    
    subgraph "Sustainability"
        SU1[Understand Impact]
        SU2[Establish Sustainability Goals]
        SU3[Maximize Utilization]
        SU4[Use Managed Services]
    end
    
    style OE1 fill:#FF9900
    style S1 fill:#FF9900
    style R1 fill:#FF9900
    style P1 fill:#FF9900
    style C1 fill:#FF9900
    style SU1 fill:#FF9900
```

## Shared Responsibility Model

### Security Responsibility Division

```mermaid
graph TB
    subgraph "Customer Responsibility<br/>(Security IN the Cloud)"
        C1[Customer Data]
        C2[Platform, Applications, IAM]
        C3[Operating System, Network,<br/>Firewall Configuration]
        C4[Client-Side Data Encryption]
        C5[Server-Side Encryption]
        C6[Network Traffic Protection]
    end
    
    subgraph "AWS Responsibility<br/>(Security OF the Cloud)"
        A1[Hardware/AWS Global Infrastructure]
        A2[Regions, AZs, Edge Locations]
        A3[Compute, Storage, Database,<br/>Networking]
        A4[Software - Managed Services]
        A5[Physical Security of Data Centers]
    end
    
    C1 --> Line[Shared Responsibility Line]
    Line --> A1
    
    style C1 fill:#FF9900
    style C2 fill:#FF9900
    style C3 fill:#FF9900
    style A1 fill:#146EB4
    style A2 fill:#146EB4
    style A3 fill:#146EB4
    style Line fill:#232F3E
```

### Service-Specific Responsibility Model

```mermaid
graph LR
    subgraph "Infrastructure Services (EC2, EBS, VPC)"
        direction TB
        I1[Customer Manages:<br/>• OS Patching<br/>• Security Groups<br/>• Network Config<br/>• Application Security]
        I2[AWS Manages:<br/>• Infrastructure<br/>• Virtualization Layer]
    end
    
    subgraph "Container Services (RDS, EMR)"
        direction TB
        Co1[Customer Manages:<br/>• Security Groups<br/>• IAM<br/>• Data Encryption]
        Co2[AWS Manages:<br/>• OS Patching<br/>• Database Patching<br/>• Infrastructure]
    end
    
    subgraph "Abstracted Services (S3, DynamoDB)"
        direction TB
        A1[Customer Manages:<br/>• IAM<br/>• Data Encryption<br/>• Client-Side Protection]
        A2[AWS Manages:<br/>• Infrastructure<br/>• Platform<br/>• Operating System]
    end
    
    I1 --> I2
    Co1 --> Co2
    A1 --> A2
    
    style I1 fill:#FF9900
    style Co1 fill:#FF9900
    style A1 fill:#FF9900
    style I2 fill:#146EB4
    style Co2 fill:#146EB4
    style A2 fill:#146EB4
```

## AWS Management Tools

### Management Console Access Flow

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant Console as AWS Console
    participant IAM
    participant Service as AWS Service
    
    User->>Browser: Navigate to console.aws.amazon.com
    Browser->>Console: HTTPS Request
    Console->>User: Login Page
    User->>Console: Enter Credentials + MFA
    Console->>IAM: Authenticate User
    IAM->>Console: Return Session Token
    Console->>User: Dashboard
    User->>Service: Perform Action
    Service->>IAM: Check Permissions
    IAM->>Service: Authorization Result
    Service->>User: Action Result
```

### AWS CLI and SDK Architecture

```mermaid
graph TB
    subgraph "Client Environment"
        CLI[AWS CLI]
        SDK[AWS SDK<br/>Python/Java/JS/etc]
        Scripts[Automation Scripts]
    end
    
    subgraph "Authentication"
        Creds[Credentials File<br/>~/.aws/credentials]
        Config[Config File<br/>~/.aws/config]
        EnvVars[Environment Variables]
        IAMRole[IAM Role<br/>for EC2/Lambda]
    end
    
    subgraph "AWS Services"
        S3[S3]
        EC2[EC2]
        Lambda[Lambda]
        RDS[RDS]
        Others[Other Services]
    end
    
    CLI --> Creds
    CLI --> Config
    SDK --> Creds
    SDK --> IAMRole
    Scripts --> EnvVars
    
    Creds --> S3
    Config --> EC2
    IAMRole --> Lambda
    EnvVars --> RDS
    
    style CLI fill:#FF9900
    style SDK fill:#FF9900
    style IAMRole fill:#569A31
```

## AWS Service Categories

### Service Categories Map

```mermaid
mindmap
    root((AWS Services))
        Compute
            EC2
            Lambda
            ECS/EKS
            Elastic Beanstalk
            Lightsail
        Storage
            S3
            EBS
            EFS
            Storage Gateway
            Snow Family
        Database
            RDS
            DynamoDB
            Aurora
            ElastiCache
            Redshift
        Networking
            VPC
            Route 53
            CloudFront
            Direct Connect
            API Gateway
        Security
            IAM
            Cognito
            Secrets Manager
            WAF & Shield
            KMS
        Analytics
            Athena
            EMR
            Kinesis
            QuickSight
            Glue
        Integration
            SQS
            SNS
            EventBridge
            Step Functions
            AppSync
        Management
            CloudWatch
            CloudFormation
            Systems Manager
            CloudTrail
            Config
```

### Service Selection Decision Tree

```mermaid
flowchart TD
    Start([What do you need?]) --> Type{Service Type?}
    
    Type -->|Compute| Compute{Workload Type?}
    Type -->|Storage| Storage{Data Type?}
    Type -->|Database| Database{Data Model?}
    Type -->|Network| Network{Use Case?}
    
    Compute -->|Traditional| EC2[EC2]
    Compute -->|Serverless| Lambda[Lambda]
    Compute -->|Containers| Container{Managed?}
    Container -->|Yes| Fargate[Fargate]
    Container -->|No| ECS[ECS/EKS]
    
    Storage -->|Object| S3[S3]
    Storage -->|Block| EBS[EBS]
    Storage -->|File| File{Protocol?}
    File -->|NFS| EFS[EFS]
    File -->|SMB/Windows| FSx[FSx]
    
    Database -->|Relational| RDS[RDS/Aurora]
    Database -->|NoSQL| NoSQL{Key-Value?}
    NoSQL -->|Yes| DynamoDB[DynamoDB]
    NoSQL -->|Document| DocumentDB[DocumentDB]
    
    Network -->|Isolation| VPC[VPC]
    Network -->|DNS| Route53[Route 53]
    Network -->|CDN| CloudFront[CloudFront]
    
    style Start fill:#232F3E
    style EC2 fill:#FF9900
    style Lambda fill:#FF9900
    style S3 fill:#FF9900
    style RDS fill:#FF9900
    style VPC fill:#FF9900
```

## AWS Account Management

### Account Structure with AWS Organizations

```mermaid
graph TB
    Root[Root Account<br/>Management Account]
    
    Root --> OU1[Organizational Unit:<br/>Production]
    Root --> OU2[Organizational Unit:<br/>Development]
    Root --> OU3[Organizational Unit:<br/>Security]
    
    OU1 --> ProdAcct1[Production Account 1]
    OU1 --> ProdAcct2[Production Account 2]
    
    OU2 --> DevAcct1[Dev Account 1]
    OU2 --> DevAcct2[Dev Account 2]
    
    OU3 --> SecAcct1[Security Account]
    OU3 --> SecAcct2[Audit Account]
    
    SCP1[Service Control Policy<br/>Deny S3 Public Access] -.Applies to.-> OU1
    SCP2[Service Control Policy<br/>Restrict Regions] -.Applies to.-> OU2
    
    style Root fill:#232F3E
    style OU1 fill:#FF9900
    style OU2 fill:#FF9900
    style OU3 fill:#FF9900
    style SCP1 fill:#146EB4
    style SCP2 fill:#146EB4
```

### Billing and Cost Management Flow

```mermaid
flowchart LR
    Services[AWS Services<br/>Usage] --> CostExplorer[AWS Cost Explorer]
    Services --> Budgets[AWS Budgets]
    Services --> Bill[AWS Bill]
    
    CostExplorer --> Analysis[Cost Analysis<br/>& Visualization]
    Budgets --> Alerts[Budget Alerts]
    Bill --> Pay[Payment]
    
    Analysis --> Actions[Cost Optimization<br/>Actions]
    Alerts --> Actions
    
    Tags[Cost Allocation<br/>Tags] -.Tag Resources.-> Services
    
    style Services fill:#FF9900
    style CostExplorer fill:#146EB4
    style Budgets fill:#146EB4
    style Actions fill:#569A31
```

### Multi-Account Strategy

```mermaid
graph TB
    subgraph "Management Account"
        Billing[Consolidated Billing]
        Org[AWS Organizations]
    end
    
    subgraph "Security OU"
        LogArchive[Log Archive Account]
        Security[Security Tooling Account]
    end
    
    subgraph "Infrastructure OU"
        Network[Network Account]
        SharedServices[Shared Services Account]
    end
    
    subgraph "Workloads"
        Prod[Production Account]
        Dev[Development Account]
        Test[Test Account]
    end
    
    Org --> Security
    Org --> Infrastructure
    Org --> Workloads
    
    Billing --> Security
    Billing --> Infrastructure
    Billing --> Workloads
    
    LogArchive -.Logs.-> Prod
    LogArchive -.Logs.-> Dev
    LogArchive -.Logs.-> Test
    
    Network -.VPC Peering/Transit Gateway.-> Prod
    Network -.VPC Peering/Transit Gateway.-> Dev
    
    style Billing fill:#FF9900
    style LogArchive fill:#146EB4
    style Prod fill:#569A31
```

## High Availability Multi-AZ Deployment

```mermaid
graph TB
    subgraph "Region: us-east-1"
        Route53[Route 53<br/>DNS]
        
        subgraph "AZ: us-east-1a"
            ALB1[Application Load Balancer]
            App1[Application Server 1]
            DB1[(Primary Database)]
        end
        
        subgraph "AZ: us-east-1b"
            App2[Application Server 2]
            DB2[(Standby Database<br/>Sync Replication)]
        end
        
        subgraph "AZ: us-east-1c"
            App3[Application Server 3]
        end
    end
    
    Users[Users] --> Route53
    Route53 --> ALB1
    
    ALB1 --> App1
    ALB1 --> App2
    ALB1 --> App3
    
    App1 --> DB1
    App2 --> DB1
    App3 --> DB1
    
    DB1 -.Synchronous<br/>Replication.-> DB2
    
    style Route53 fill:#8C4FFF
    style ALB1 fill:#FF9900
    style DB1 fill:#3B48CC
    style DB2 fill:#3B48CC
```

