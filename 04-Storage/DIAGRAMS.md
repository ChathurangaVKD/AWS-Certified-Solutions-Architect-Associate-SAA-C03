# Storage Services - Mermaid Diagrams

## Amazon S3 Overview

### S3 Storage Classes Hierarchy

```mermaid
graph TB
    S3["Amazon S3 Storage Classes"]
    
    S3 --> Standard["S3 Standard<br/>💰 Most Expensive<br/>⚡ Frequent Access<br/>📊 99.99% Availability<br/>🛡️ 11 9's Durability"]
    
    S3 --> Intelligent["S3 Intelligent-Tiering<br/>🤖 Auto-optimization<br/>📊 Unknown access patterns<br/>💰 Small monitoring fee"]
    
    S3 --> IA[Infrequent Access Tier]
    IA --> StandardIA["S3 Standard-IA<br/>💰 Lower cost<br/>⏱️ Min 30 days<br/>📊 99.9% Availability"]
    IA --> OneZoneIA["S3 One Zone-IA<br/>💰 20% cheaper than Standard-IA<br/>⚠️ Single AZ<br/>📊 99.5% Availability"]
    
    S3 --> Glacier[Archive Tier]
    Glacier --> GlacierInstant["S3 Glacier Instant Retrieval<br/>⏱️ Millisecond retrieval<br/>💰 Archive pricing<br/>📅 Min 90 days"]
    Glacier --> GlacierFlexible["S3 Glacier Flexible Retrieval<br/>⏱️ Minutes to hours<br/>💰 Very low cost<br/>📅 Min 90 days"]
    Glacier --> GlacierDeep["S3 Glacier Deep Archive<br/>⏱️ 12-48 hours<br/>💰 Lowest cost<br/>📅 Min 180 days"]
    
    classDef style1 fill:#FF9900
    class Standard style1
    classDef style2 fill:#146EB4
    class Intelligent style2
    classDef style3 fill:#569A31
    class StandardIA style3
    classDef style4 fill:#8C4FFF
    class GlacierDeep style4
```

### S3 Lifecycle Policy Flow

```mermaid
stateDiagram-v2
    [*] --> S3Standard: Upload Object
    
    S3Standard --> StandardIA: After 30 days<br/>Transition Rule
    StandardIA --> IntelligentTiering: Based on access pattern
    StandardIA --> GlacierFlexible: After 90 days<br/>Transition Rule
    
    GlacierFlexible --> GlacierDeep: After 365 days<br/>Transition Rule
    
    GlacierDeep --> [*]: After 7 years<br/>Expiration Rule
    
    note right of S3Standard
        Frequently accessed
        Full availability
    end note
    
    note right of GlacierDeep
        Long-term archive
        Compliance retention
    end note
```

### S3 Data Flow and Access

```mermaid
graph TB
    subgraph Clients_Group["Clients"]
        App[Application]
        User[End User]
        CLI[AWS CLI]
    end
    
    subgraph Amazon_S3_Group["Amazon S3"]
        Bucket["S3 Bucket<br/>my-bucket"]
        
        subgraph Objects_Group["Objects"]
            Obj1["File1.jpg<br/>Key: photos/2024/file1.jpg"]
            Obj2["Data.csv<br/>Key: data/2024/data.csv"]
            Obj3["Video.mp4<br/>Key: videos/video.mp4"]
        end
        
        Versioning[Versioning: Enabled]
        Encryption[Encryption: SSE-S3]
        
        Bucket --> Obj1
        Bucket --> Obj2
        Bucket --> Obj3
        Bucket --> Versioning
        Bucket --> Encryption
    end
    
    subgraph Access_Control_Group["Access Control"]
        BucketPolicy["Bucket Policy<br/>Resource-based"]
        IAMPolicy["IAM Policy<br/>Identity-based"]
        ACL["ACL<br/>Legacy"]
        BlockPublic[Block Public Access]
    end
    
    App --> IAMPolicy
    IAMPolicy --> Bucket
    BucketPolicy --> Bucket
    BlockPublic -.Prevents.-> Bucket
    
    CloudFront[CloudFront CDN] --> Bucket
    
    classDef style1 fill:#569A31
    class Bucket style1
    classDef style2 fill:#FF9900
    class BucketPolicy style2
    classDef style3 fill:#146EB4
    class CloudFront style3
```

### S3 Versioning

```mermaid
sequenceDiagram
    participant User
    participant S3 as S3 Bucket (Versioning Enabled(
    
    User->>S3: PUT file.txt (First Upload(
    S3->>S3: Create Version ID: v1
    S3->>User: Success (Version: v1(
    
    User->>S3: PUT file.txt (Update(
    S3->>S3: Create Version ID: v2
    Note over S3: Previous version v1 kept
    S3->>User: Success (Version: v2(
    
    User->>S3: PUT file.txt (Update Again(
    S3->>S3: Create Version ID: v3
    Note over S3: Versions v1 and v2 kept
    S3->>User: Success (Version: v3(
    
    User->>S3: DELETE file.txt
    S3->>S3: Add Delete Marker (v4(
    Note over S3: All versions still exist
    S3->>User: Success (Delete Marker(
    
    User->>S3: GET file.txt
    S3->>User: 404 Not Found (Delete Marker(
    
    User->>S3: DELETE Delete Marker
    S3->>User: Success - File Restored
    
    User->>S3: GET file.txt?versionId=v2
    S3->>User: Return Version v2
    
```

### S3 Replication (CRR & SRR)

```mermaid
graph LR
    subgraph Source_Region_us_east_1_Group["Source Region: us-east-1"]
        SourceBucket["Source S3 Bucket<br/>Versioning: Enabled"]
        SourceData[Objects]
        
        SourceData --> SourceBucket
    end
    
    subgraph Destination_Region_eu_west_1_Group["Destination Region: eu-west-1"]
        DestBucket["Destination S3 Bucket<br/>Versioning: Enabled"]
        ReplicatedData[Replicated Objects]
        
        ReplicatedData --> DestBucket
    end
    
    SourceBucket -->|Cross-Region Replication<br/>CRR| DestBucket
    
    Requirements["Requirements:<br/>✅ Versioning enabled on both<br/>✅ IAM role for replication<br/>✅ Different regions (CRR)<br/>✅ Same region (SRR)"]
    
    UseCases["Use Cases:<br/>• Compliance<br/>• Lower latency<br/>• Disaster recovery<br/>• Replication across accounts"]
    
    SourceBucket -.Requires.-> Requirements
    DestBucket -.Use Cases.-> UseCases
    
    Note1["📝 Only new objects replicated<br/>📝 Delete markers optional<br/>📝 No chaining"]
    
    classDef style1 fill:#FF9900
    class SourceBucket style1
    classDef style2 fill:#569A31
    class DestBucket style2
```

### S3 Encryption Options

```mermaid
graph TB
    S3Encryption[S3 Encryption Methods]
    
    S3Encryption --> ServerSide["Server-Side Encryption<br/>Encrypted at rest"]
    S3Encryption --> ClientSide["Client-Side Encryption<br/>Encrypted before upload"]
    
    ServerSide --> SSE_S3["SSE-S3<br/>🔑 AWS Managed Keys<br/>🔒 AES-256<br/>✅ Default option<br/>Header: x-amz-server-side-encryption: AES256"]
    
    ServerSide --> SSE_KMS["SSE-KMS<br/>🔑 AWS KMS Keys<br/>✅ Audit trail via CloudTrail<br/>✅ User control<br/>⚠️ KMS quota limits<br/>Header: x-amz-server-side-encryption: aws:kms"]
    
    ServerSide --> SSE_C["SSE-C<br/>🔑 Customer-Provided Keys<br/>✅ Full control<br/>⚠️ HTTPS required<br/>⚠️ Keys not stored by AWS"]
    
    ClientSide --> ClientLib["Encrypt using client libraries<br/>Upload encrypted data<br/>Decrypt on download<br/>Full client control"]
    
    classDef style1 fill:#569A31
    class SSE_S3 style1
    classDef style2 fill:#FF9900
    class SSE_KMS style2
    classDef style3 fill:#146EB4
    class SSE_C style3
```

### S3 Access Points

```mermaid
graph TB
    subgraph S3_Bucket_company_data_Group["S3 Bucket: company-data"]
        Data1["/finance/* objects"]
        Data2["/hr/* objects"]
        Data3["/engineering/* objects"]
    end
    
    subgraph S3_Access_Points_Group["S3 Access Points"]
        AP1["Finance Access Point<br/>finance-ap<br/>Policy: Allow finance/*"]
        AP2["HR Access Point<br/>hr-ap<br/>Policy: Allow hr/*"]
        AP3["Engineering Access Point<br/>engineering-ap<br/>Policy: Allow engineering/*"]
    end
    
    subgraph Users_Applications_Group["Users/Applications"]
        FinanceApp[Finance Application] --> AP1
        HRApp[HR Application] --> AP2
        EngApp[Engineering Application] --> AP3
    end
    
    AP1 --> Data1
    AP2 --> Data2
    AP3 --> Data3
    
    VPC["VPC Access Point<br/>Restrict to VPC only"] -.VPC Access.-> AP1
    
    classDef style1 fill:#FF9900
    class AP1 style1
    classDef style2 fill:#FF9900
    class AP2 style2
    classDef style3 fill:#FF9900
    class AP3 style3
```

### S3 Event Notifications

```mermaid
graph TB
    S3[S3 Bucket] --> Events{Event Types}
    
    Events --> Create["Object Created<br/>s3:ObjectCreated:*"]
    Events --> Delete["Object Removed<br/>s3:ObjectRemoved:*"]
    Events --> Restore["Object Restore<br/>s3:ObjectRestore:*"]
    Events --> Replication["Replication<br/>s3:Replication:*"]
    
    Create --> Targets{Notification Targets}
    Delete --> Targets
    
    Targets --> SNS["SNS Topic<br/>Email/SMS notifications"]
    Targets --> SQS["SQS Queue<br/>Decouple processing"]
    Targets --> Lambda["Lambda Function<br/>Process immediately"]
    Targets --> EventBridge["EventBridge<br/>18+ AWS services<br/>Advanced filtering"]
    
    Lambda --> Processing["Example:<br/>• Image resize<br/>• Video transcoding<br/>• Data processing<br/>• Trigger workflows"]
    
    classDef style1 fill:#569A31
    class S3 style1
    classDef style2 fill:#FF9900
    class Lambda style2
    classDef style3 fill:#8C4FFF
    class EventBridge style3
```

### S3 Performance Optimization

```mermaid
graph TB
    subgraph Upload_Optimization_Group["Upload Optimization"]
        Multipart["Multipart Upload<br/>📦 &gt; 100 MB recommended<br/>📦 Required for &gt; 5 GB<br/>✅ Parallel uploads<br/>✅ Resume capability"]
        
        TransferAcc["S3 Transfer Acceleration<br/>🌐 Use CloudFront Edge<br/>⚡ 50-500% faster<br/>💰 Additional cost"]
    end
    
    subgraph Download_Optimization_Group["Download Optimization"]
        ByteRange["Byte-Range Fetches<br/>📥 Parallel downloads<br/>✅ Resilient to failures<br/>✅ Partial file retrieval"]
        
        S3Select["S3 Select<br/>📊 SQL on S3 objects<br/>⚡ 400% faster<br/>💰 80% cheaper<br/>✅ Filter server-side"]
    end
    
    subgraph Request_Optimization_Group["Request Optimization"]
        Prefixes["Use Prefixes<br/>3,500 PUT/s per prefix<br/>5,500 GET/s per prefix<br/>Spread across prefixes"]
        
        CloudFront["CloudFront Caching<br/>🌐 Edge caching<br/>⚡ Low latency<br/>✅ Reduce S3 load"]
    end
    
    LargeFile[Large File Upload] --> Multipart
    GlobalUsers[Global Users] --> TransferAcc
    
    BigData[Big Data Analysis] --> S3Select
    LargeDownload[Large File Download] --> ByteRange
    
    HighTraffic[High Traffic] --> Prefixes
    StaticContent[Static Content] --> CloudFront
    
    classDef style1 fill:#569A31
    class Multipart style1
    classDef style2 fill:#FF9900
    class TransferAcc style2
    classDef style3 fill:#146EB4
    class S3Select style3
```

## Amazon EBS (Elastic Block Store)

### EBS Volume Types

```mermaid
graph TB
    EBS[EBS Volume Types]
    
    EBS --> SSD["SSD-backed<br/>Small random I/O"]
    EBS --> HDD["HDD-backed<br/>Large sequential I/O"]
    
    SSD --> GP3["gp3 - General Purpose SSD<br/>💰 20% cheaper than gp2<br/>📊 3,000-16,000 IOPS<br/>💾 125-1,000 MB/s<br/>✅ Predictable performance<br/>Use: Boot volumes, dev/test"]
    
    SSD --> GP2["gp2 - General Purpose SSD<br/>📊 3 IOPS per GB<br/>💾 Max 16,000 IOPS<br/>⚡ Burst to 3,000 IOPS<br/>Use: Boot volumes"]
    
    SSD --> IO2["io2/io2 Block Express - Provisioned IOPS SSD<br/>📊 Up to 256,000 IOPS<br/>💾 Up to 4,000 MB/s<br/>🛡️ 99.999% durability<br/>Use: Critical databases, high performance"]
    
    SSD --> IO1["io1 - Provisioned IOPS SSD<br/>📊 Up to 64,000 IOPS<br/>💾 Up to 1,000 MB/s<br/>Use: Databases"]
    
    HDD --> ST1["st1 - Throughput Optimized HDD<br/>💾 Up to 500 MB/s<br/>💰 Low cost<br/>🚫 Cannot be boot volume<br/>Use: Big data, data warehouses, log processing"]
    
    HDD --> SC1["sc1 - Cold HDD<br/>💾 Up to 250 MB/s<br/>💰 Lowest cost<br/>🚫 Cannot be boot volume<br/>Use: Infrequently accessed data"]
    
    classDef style1 fill:#569A31
    class GP3 style1
    classDef style2 fill:#FF9900
    class IO2 style2
    classDef style3 fill:#146EB4
    class ST1 style3
```

### EBS Volume Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Creating: Create Volume
    Creating --> Available: Volume Ready
    
    Available --> InUse: Attach to EC2
    InUse --> Available: Detach from EC2
    
    Available --> Snapshot: Create Snapshot
    Snapshot --> Available: Snapshot Complete
    
    Snapshot --> NewVolume: Restore from Snapshot
    NewVolume --> Available
    
    Available --> Deleting: Delete Volume
    InUse --> Deleting: Force Delete
    
    Deleting --> [*]
    
    note right of InUse
        Mounted to EC2
        Data can be read/written
    end note
    
    note right of Snapshot
        Incremental backup
        Stored in S3
    end note
```

### EBS Snapshots Architecture

```mermaid
graph TB
    subgraph AZ_us_east_1a_Group["AZ: us-east-1a"]
        EC2_1[EC2 Instance]
        EBS1["EBS Volume<br/>100 GB Data"]
        
        EC2_1 --> EBS1
    end
    
    EBS1 -->|Create Snapshot| Snapshot1["Snapshot 1<br/>Full Backup: 100 GB<br/>Incremental"]
    
    Snapshot1 --> S3["Amazon S3<br/>Regional Service<br/>Automatic Multi-AZ"]
    
    EBS1 -->|After changes: +10 GB| Snapshot2["Snapshot 2<br/>Incremental: +10 GB only<br/>References Snapshot 1"]
    
    Snapshot2 --> S3
    
    S3 -->|Copy Snapshot| S3_DR["S3 in eu-west-1<br/>Disaster Recovery"]
    
    S3 -->|Restore| NewEBS["New EBS Volume<br/>Any AZ in region"]
    
    subgraph AZ_us_east_1b_Group["AZ: us-east-1b"]
        NewEBS
        EC2_2[New EC2 Instance] --> NewEBS
    end
    
    Features["Features:<br/>✅ Incremental backups<br/>✅ Copy across regions<br/>✅ Create AMI from snapshot<br/>✅ Fast snapshot restore<br/>💰 Pay for stored data only"]
    
    classDef style1 fill:#FF9900
    class EBS1 style1
    classDef style2 fill:#569A31
    class S3 style2
    classDef style3 fill:#146EB4
    class Snapshot1 style3
```

### EBS Multi-Attach (io1/io2 only)

```mermaid
graph TB
    subgraph Availability_Zone_Group["Availability Zone"]
        EBS["EBS io2 Volume<br/>Multi-Attach Enabled<br/>Up to 16 instances"]
        
        EC2_1["EC2 Instance 1<br/>Clustered App"]
        EC2_2["EC2 Instance 2<br/>Clustered App"]
        EC2_3["EC2 Instance 3<br/>Clustered App"]
        
        EC2_1 -.Read/Write.-> EBS
        EC2_2 -.Read/Write.-> EBS
        EC2_3 -.Read/Write.-> EBS
    end
    
    Limitations["Limitations:<br/>⚠️ Same AZ only<br/>⚠️ io1/io2 only<br/>⚠️ Cluster-aware file system<br/>⚠️ Up to 16 instances"]
    
    UseCases["Use Cases:<br/>• Teradata<br/>• Clustered databases<br/>• Applications requiring higher availability<br/>• Must manage concurrent writes"]
    
    classDef style1 fill:#FF9900
    class EBS style1
    classDef style2 fill:#C00
    class Limitations style2
```

## Amazon EFS (Elastic File System)

### EFS Architecture

```mermaid
graph TB
    subgraph Region_us_east_1_Group["Region: us-east-1"]
        EFS["Amazon EFS<br/>Network File System<br/>Managed Service"]
        
        subgraph AZ_us_east_1a_Group["AZ: us-east-1a"]
            MT1[Mount Target 1]
            EC2_1a[EC2 Instance]
            Lambda1[Lambda Function]
            
            EC2_1a --> MT1
            Lambda1 --> MT1
        end
        
        subgraph AZ_us_east_1b_Group["AZ: us-east-1b"]
            MT2[Mount Target 2]
            EC2_1b[EC2 Instance]
            
            EC2_1b --> MT2
        end
        
        subgraph AZ_us_east_1c_Group["AZ: us-east-1c"]
            MT3[Mount Target 3]
            EC2_1c[EC2 Instance]
            ECS[ECS Tasks]
            
            EC2_1c --> MT3
            ECS --> MT3
        end
        
        MT1 --> EFS
        MT2 --> EFS
        MT3 --> EFS
    end
    
    OnPrem["On-Premises<br/>via VPN/Direct Connect"] -.NFSv4.-> MT1
    
    Features["Features:<br/>✅ Multi-AZ by default<br/>✅ Automatic scaling<br/>✅ Pay for what you use<br/>✅ 1000s concurrent connections<br/>✅ POSIX-compliant<br/>✅ Linux only"]
    
    classDef style1 fill:#569A31
    class EFS style1
    classDef style2 fill:#FF9900
    class MT1 style2
```

### EFS Storage Classes

```mermaid
graph TB
    EFS[EFS File System]
    
    EFS --> Standard["Standard Storage Class<br/>⚡ Frequent access<br/>💰 Higher cost<br/>📊 Multi-AZ"]
    
    EFS --> IA["EFS Infrequent Access<br/>💰 92% lower cost<br/>⏱️ Lower throughput<br/>📊 Multi-AZ"]
    
    EFS --> OneZone["EFS One Zone<br/>💰 47% cheaper than Standard<br/>⚠️ Single AZ<br/>⚡ Frequent access"]
    
    EFS --> OneZoneIA["EFS One Zone-IA<br/>💰 Lowest cost<br/>⚠️ Single AZ<br/>⏱️ Infrequent access"]
    
    Lifecycle["Lifecycle Management<br/>Auto-move files to IA<br/>Based on access pattern<br/>7, 14, 30, 60, 90 days"]
    
    Standard -.Lifecycle Policy.-> IA
    OneZone -.Lifecycle Policy.-> OneZoneIA
    
    Standard -.Access.-> IA
    IA -.Access.-> Standard
    
    classDef style1 fill:#FF9900
    class Standard style1
    classDef style2 fill:#569A31
    class IA style2
    classDef style3 fill:#146EB4
    class OneZone style3
```

### EFS Performance Modes

```mermaid
graph TB
    subgraph Performance_Modes_Group["Performance Modes"]
        General["General Purpose<br/>⚡ Low latency<br/>📊 Up to 7,000 files ops/sec<br/>✅ Default choice<br/>Use: Web servers, CMS"]
        
        MaxIO["Max I/O<br/>📊 Higher latency<br/>📈 &gt; 7,000 files ops/sec<br/>📊 Highly parallel<br/>Use: Big data, media processing"]
    end
    
    subgraph Throughput_Modes_Group["Throughput Modes"]
        Bursting["Bursting Throughput<br/>📊 Scales with size<br/>50 MB/s per TB<br/>⚡ Burst to 100 MB/s"]
        
        Provisioned["Provisioned Throughput<br/>📊 Set throughput independent of size<br/>💰 Additional cost<br/>Use: High throughput to storage ratio"]
        
        Elastic["Elastic Throughput<br/>🤖 Auto-scales<br/>📊 Up to 3 GB/s reads, 1 GB/s writes<br/>💰 Pay for what you use<br/>✅ Recommended"]
    end
    
    WebApp[Web Application] --> General
    WebApp --> Elastic
    
    BigData[Big Data Analytics] --> MaxIO
    BigData --> Provisioned
    
    classDef style1 fill:#569A31
    class General style1
    classDef style2 fill:#FF9900
    class Elastic style2
```

## AWS Storage Gateway

### Storage Gateway Types

```mermaid
graph TB
    OnPrem["On-Premises<br/>Data Center"]
    
    OnPrem --> Gateway{Storage Gateway}
    
    Gateway --> S3File["S3 File Gateway<br/>📁 NFS/SMB protocol<br/>☁️ Store as S3 objects<br/>💾 Local cache<br/>Use: File shares, backups"]
    
    Gateway --> FSx["FSx File Gateway<br/>📁 SMB protocol<br/>☁️ Amazon FSx for Windows<br/>💾 Local cache<br/>Use: Windows file shares"]
    
    Gateway --> Volume["Volume Gateway<br/>💾 iSCSI protocol<br/>Block storage"]
    
    Volume --> Cached["Cached Volumes<br/>💾 Primary data in S3<br/>🔄 Frequently accessed cached<br/>📦 Up to 32 volumes<br/>📊 32 TiB each"]
    
    Volume --> Stored["Stored Volumes<br/>💾 Primary data on-premises<br/>☁️ Async backup to S3<br/>📦 Up to 32 volumes<br/>📊 16 TiB each"]
    
    Gateway --> Tape["Tape Gateway<br/>📼 Virtual Tape Library (VTL)<br/>☁️ Backup to S3 & Glacier<br/>✅ Works with backup software<br/>Use: Backup & archive"]
    
    S3File --> S3[Amazon S3]
    FSx --> FSxService[Amazon FSx]
    Cached --> S3
    Stored --> S3
    Tape --> S3
    Tape --> Glacier[S3 Glacier]
    
    classDef style1 fill:#FF9900
    class Gateway style1
    classDef style2 fill:#569A31
    class S3File style2
    classDef style3 fill:#146EB4
    class Tape style3
```

### Storage Gateway Hybrid Architecture

```mermaid
graph TB
    subgraph On_Premises_Data_Center_Group["On-Premises Data Center"]
        Apps[Applications]
        Gateway["Storage Gateway<br/>VM or Hardware Appliance"]
        Cache["Local Cache<br/>Frequently accessed data"]
        
        Apps --> Gateway
        Gateway --> Cache
    end
    
    subgraph AWS_Cloud_Group["AWS Cloud"]
        S3["Amazon S3<br/>Primary Storage"]
        Glacier["S3 Glacier<br/>Archive"]
        EBS[EBS Snapshots]
        
        S3 --> Glacier
    end
    
    Gateway -->|HTTPS| S3
    Gateway -->|Snapshots| EBS
    
    Lifecycle[Lifecycle Policies] -.Auto-archive.-> Glacier
    
    Benefits["Benefits:<br/>✅ Low-latency local access<br/>✅ Durable cloud storage<br/>✅ Seamless migration<br/>✅ Disaster recovery<br/>✅ Reduced on-prem storage costs"]
    
    classDef style1 fill:#FF9900
    class Gateway style1
    classDef style2 fill:#569A31
    class S3 style2
```

## AWS Snow Family

### Snow Family Devices

```mermaid
graph TB
    SnowFamily["AWS Snow Family<br/>Physical Data Transfer & Edge Computing"]
    
    SnowFamily --> Snowcone["Snowcone<br/>📦 Smallest device<br/>💾 8-14 TB usable<br/>⚡ 2 CPUs, 4 GB RAM<br/>🔋 Battery powered<br/>Use: Edge computing, IoT, remote locations"]
    
    SnowFamily --> Snowball[Snowball Edge]
    
    Snowball --> SnowballStorage["Snowball Edge Storage Optimized<br/>💾 80 TB usable<br/>💪 40 vCPUs, 80 GB RAM<br/>📊 1 TB SSD for block volumes<br/>Use: Large data migrations, local storage"]
    
    Snowball --> SnowballCompute["Snowball Edge Compute Optimized<br/>💾 42-28 TB usable<br/>💪 52 vCPUs, 208 GB RAM<br/>📊 Optional GPU<br/>Use: ML, video processing, analytics"]
    
    SnowFamily --> Snowmobile["Snowmobile<br/>🚛 Shipping container<br/>💾 100 PB capacity<br/>🔒 GPS tracking, security<br/>Use: Exabyte-scale migration"]
    
    subgraph Use_Cases_Group["Use Cases"]
        Snowcone --> UC1["Remote locations<br/>Harsh environments<br/>Drones"]
        SnowballStorage --> UC2["Data center migration<br/>Disaster recovery<br/>Content distribution"]
        SnowballCompute --> UC3["Machine learning<br/>Video processing<br/>Analytics at edge"]
        Snowmobile --> UC4["Complete data center<br/>shutdown/migration<br/>Massive datasets"]
    end
    
    classDef style1 fill:#569A31
    class Snowcone style1
    classDef style2 fill:#FF9900
    class SnowballStorage style2
    classDef style3 fill:#146EB4
    class Snowmobile style3
```

### Snow Family Data Migration Flow

```mermaid
sequenceDiagram
    participant Customer as Customer Data Center
    participant AWS as AWS
    participant Device as Snow Device
    participant S3 as Amazon S3
    
    Customer->>AWS: 1. Request Snow device via Console
    AWS->>Customer: 2. Ship device (encrypted(
    Customer->>Device: 3. Connect to local network
    Customer->>Device: 4. Install Snowball client
    Customer->>Device: 5. Copy data (days/weeks(
    Note over Device: Data encrypted automatically
    Customer->>AWS: 6. Ship device back
    AWS->>Device: 7. Receive at AWS facility
    Device->>S3: 8. Import data to S3
    S3->>Customer: 9. Notify completion
    AWS->>Device: 10. Securely erase device
    
    Note over Customer,S3: Timeline: 1-2 weeks including shipping
    
```

## Amazon FSx

### FSx Family Overview

```mermaid
graph TB
    FSx["Amazon FSx<br/>Managed File Systems"]
    
    FSx --> Windows["FSx for Windows File Server<br/>🪟 Windows-native<br/>📁 SMB protocol<br/>✅ Active Directory integration<br/>✅ DFS Namespaces<br/>📊 SSD & HDD options<br/>Use: Windows apps, SQL Server, SharePoint"]
    
    FSx --> Lustre["FSx for Lustre<br/>⚡ High-performance computing<br/>📊 100+ GB/s, millions IOPS<br/>🔗 S3 integration<br/>⚙️ Sub-millisecond latencies<br/>Use: ML, HPC, video processing, financial modeling"]
    
    FSx --> NetApp["FSx for NetApp ONTAP<br/>🔧 NetApp ONTAP features<br/>📁 NFS, SMB, iSCSI<br/>✅ Multi-protocol access<br/>📸 Snapshots, replication<br/>Use: Enterprise apps, multi-protocol access"]
    
    FSx --> OpenZFS["FSx for OpenZFS<br/>🐧 Linux workloads<br/>📁 NFS protocol<br/>⚡ Up to 1 million IOPS<br/>📸 Point-in-time snapshots<br/>Use: Linux apps, data analytics"]
    
    subgraph Key_Differences_Group["Key Differences"]
        Windows --> WinNote["Windows environment<br/>SMB shares<br/>AD integration"]
        Lustre --> LustreNote["HPC workloads<br/>Parallel file system<br/>S3 backend"]
        NetApp --> NetAppNote["Enterprise features<br/>Multi-protocol<br/>Data management"]
        OpenZFS --> ZFSNote["Linux workloads<br/>ZFS file system<br/>High performance"]
    end
    
    classDef style1 fill:#FF9900
    class Windows style1
    classDef style2 fill:#569A31
    class Lustre style2
    classDef style3 fill:#146EB4
    class NetApp style3
```

### FSx for Lustre with S3 Integration

```mermaid
graph TB
    subgraph Compute_Resources_Group["Compute Resources"]
        EC2_1[EC2 Instance 1]
        EC2_2[EC2 Instance 2]
        EC2_3[EC2 Instance 3]
        Cluster[HPC Cluster]
    end
    
    subgraph FSx_for_Lustre_Group["FSx for Lustre"]
        FSxLustre["FSx for Lustre<br/>High-performance file system<br/>Parallel I/O"]
        Cache[File System Cache]
        
        FSxLustre --> Cache
    end
    
    subgraph Amazon_S3_Group["Amazon S3"]
        S3Input["S3 Bucket<br/>Input Data"]
        S3Output["S3 Bucket<br/>Output Results"]
    end
    
    EC2_1 --> FSxLustre
    EC2_2 --> FSxLustre
    EC2_3 --> FSxLustre
    Cluster --> FSxLustre
    
    S3Input -->|Lazy Load| FSxLustre
    FSxLustre -->|Write Back| S3Output
    
    Process["Process:<br/>1. Data in S3<br/>2. FSx lazy-loads on demand<br/>3. Parallel processing<br/>4. Results written to S3"]
    
    DeploymentOptions["Deployment Options:<br/>• Scratch: Temporary, no replication<br/>• Persistent: HA, auto-replication"]
    
    classDef style1 fill:#569A31
    class FSxLustre style1
    classDef style2 fill:#FF9900
    class S3Input style2
```

## Storage Comparison Matrix

### When to Use Which Storage Service

```mermaid
graph TB
    Start([Choose Storage Service])
    
    Start --> Q1{Data Type?}
    
    Q1 -->|Object Storage| S3Decision{Access Pattern?}
    Q1 -->|Block Storage| BlockDecision{Shared Access?}
    Q1 -->|File Storage| FileDecision{OS Type?}
    
    S3Decision -->|Frequent| S3Standard[S3 Standard]
    S3Decision -->|Infrequent| S3IA[S3 Standard-IA]
    S3Decision -->|Archive| Glacier[S3 Glacier]
    S3Decision -->|Unknown| Intelligent[S3 Intelligent-Tiering]
    
    BlockDecision -->|No| EBSChoice["EBS Volume<br/>Single EC2 instance"]
    BlockDecision -->|Yes, same AZ| EBSMulti["EBS Multi-Attach<br/>io1/io2 only"]
    BlockDecision -->|Yes, multi-AZ| InstanceStore[Consider EFS instead]
    
    FileDecision -->|Linux| LinuxFile{Performance?}
    FileDecision -->|Windows| WindowsFile{Location?}
    
    LinuxFile -->|Standard| EFS[Amazon EFS]
    LinuxFile -->|HPC| Lustre[FSx for Lustre]
    LinuxFile -->|Enterprise| OpenZFS[FSx for OpenZFS]
    
    WindowsFile -->|AWS| FSxWindows[FSx for Windows]
    WindowsFile -->|On-Premises| StorageGW[Storage Gateway]
    
    classDef style1 fill:#569A31
    class S3Standard style1
    classDef style2 fill:#FF9900
    class EBSChoice style2
    classDef style3 fill:#146EB4
    class EFS style3
    classDef style4 fill:#8C4FFF
    class Lustre style4
```

