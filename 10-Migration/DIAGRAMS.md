# Migration & Transfer - Mermaid Diagrams

## AWS Migration Strategies (7 Rs)

### The 7 Rs of Migration

```mermaid
mindmap
    root((7 Rs of Migration))
        Retire
            Decommission
            Turn off unused
            Reduce costs
            10-20% of portfolio
        Retain
            Keep on-premises
            Not ready to migrate
            Compliance requirements
            Recent upgrade
        Relocate
            VMware Cloud on AWS
            Lift-and-shift VMs
            Same versions
            Minimal changes
        Rehost
            Lift and Shift
            Move as-is to AWS
            EC2 instances
            Quick migration
            Minimal changes
        Replatform
            Lift, Tinker, and Shift
            Optimize during migration
            Use RDS instead of DB on EC2
            Some cloud benefits
        Repurchase
            Drop and Shop
            Move to SaaS
            Replace with cloud-native
            e.g., Salesforce, Workday
        Refactor/Re-architect
            Redesign application
            Cloud-native architecture
            Serverless, containers
            Maximum cloud benefits
            Most expensive/time
```

### Migration Decision Tree

```mermaid
flowchart TD
    Start([Application to Migrate])
    
    Start --> Q1{Still needed?}
    Q1 -->|No| Retire["Retire: Decommission"]
    Q1 -->|Yes| Q2{Ready to migrate?}
    
    Q2 -->|No| Retain["Retain: Keep on-premises"]
    Q2 -->|Yes| Q3{Migration urgency?}
    
    Q3 -->|Very Urgent| Q4{VMware workload?}
    Q3 -->|Not Urgent| Q5{Willing to redesign?}
    
    Q4 -->|Yes| Relocate["Relocate: VMware Cloud on AWS"]
    Q4 -->|No| Rehost["Rehost: Lift & Shift to EC2"]
    
    Q5 -->|No| Q6{Some optimization OK?}
    Q5 -->|Yes| Q7{Budget available?}
    
    Q6 -->|Yes| Replatform["Replatform: Use managed services"]
    Q6 -->|No| Rehost
    
    Q7 -->|No| Repurchase["Repurchase: Move to SaaS"]
    Q7 -->|Yes| Refactor["Refactor: Cloud-native redesign"]
    
    classDef style1 fill:#232F3E
    class Start style1
    classDef style2 fill:#FF9900
    class Rehost style2
    classDef style3 fill:#569A31
    class Refactor style3
    classDef style4 fill:#C00
    class Retire style4
```

## AWS Migration Hub

### Migration Hub Architecture

```mermaid
graph TB
    subgraph On_Premises_Environment_Group["On-Premises Environment"]
        Servers["Physical/Virtual Servers<br/>Databases<br/>Applications"]
    end
    
    subgraph Discovery_Group["Discovery"]
        Connector["AWS Application<br/>Discovery Service<br/>Agent-based or agentless"]
        
        Import["Import via CSV<br/>Manual entry<br/>Partner tools"]
        
        Servers --> Connector
    end
    
    subgraph AWS_Migration_Hub_Group["AWS Migration Hub"]
        Hub["Migration Hub<br/>Central tracking dashboard"]
        
        Groups["Application Groups<br/>Logical grouping"]
        
        Status["Migration Status<br/>Track progress"]
        
        Hub --> Groups
        Hub --> Status
    end
    
    subgraph Migration_Tools_Group["Migration Tools"]
        DMS["AWS DMS<br/>Database migration"]
        SMS["AWS SMS<br/>Server migration"]
        MGN["AWS MGN<br/>Application Migration"]
        DataSync["AWS DataSync<br/>Data transfer"]
    end
    
    subgraph AWS_Cloud_Group["AWS Cloud"]
        EC2[EC2 Instances]
        RDS[RDS Databases]
        S3[S3 Storage]
    end
    
    Connector --> Hub
    Import --> Hub
    
    Hub --> DMS
    Hub --> SMS
    Hub --> MGN
    Hub --> DataSync
    
    DMS --> RDS
    SMS --> EC2
    MGN --> EC2
    DataSync --> S3
    
    classDef style1 fill:#FF9900
    class Hub style1
    classDef style2 fill:#569A31
    class MGN style2
```

## AWS Application Discovery Service

### Discovery Service Options

```mermaid
graph TB
    subgraph Agentless_Discovery_Group["Agentless Discovery"]
        Agentless["AWS Agentless<br/>Discovery Connector<br/>VMware vCenter"]
        
        Agentless_Data["Collects:<br/>• VM inventory<br/>• Configuration<br/>• Performance metrics<br/>• Network connections<br/>⚠️ VMware only"]
    end
    
    subgraph Agent_based_Discovery_Group["Agent-based Discovery"]
        Agent["AWS Discovery Agent<br/>Install on each server"]
        
        Agent_Data["Collects:<br/>• System config<br/>• Performance<br/>• Running processes<br/>• Network connections<br/>• Dependencies<br/>✅ Works on any server"]
    end
    
    subgraph Data_Analysis_Group["Data Analysis"]
        MigrationHub["Migration Hub<br/>Analyze data"]
        
        Athena["Amazon Athena<br/>Query discovery data"]
        
        QuickSight["Amazon QuickSight<br/>Visualize data"]
    end
    
    Agentless --> Agentless_Data
    Agent --> Agent_Data
    
    Agentless_Data --> MigrationHub
    Agent_Data --> MigrationHub
    
    MigrationHub --> Athena
    MigrationHub --> QuickSight
    
    Use["Use Cases:<br/>• Discover application dependencies<br/>• Plan migration wave<br/>• Rightsizing recommendations<br/>• TCO analysis"]
    
    classDef style1 fill:#FF9900
    class Agentless style1
    classDef style2 fill:#569A31
    class Agent style2
```

## AWS Database Migration Service (DMS)

### DMS Architecture

```mermaid
graph TB
    subgraph Source_Databases_Group["Source Databases"]
        Oracle[Oracle]
        SQLServer[SQL Server]
        MySQL[MySQL]
        PostgreSQL[PostgreSQL]
        MongoDB[MongoDB]
        SAP[SAP ASE]
        S3Source[Amazon S3]
    end
    
    subgraph AWS_DMS_Group["AWS DMS"]
        Replication["DMS Replication Instance<br/>EC2 instance running DMS"]
        
        Tasks["Migration Tasks<br/>Source -&gt; Target mapping"]
        
        SCT["Schema Conversion Tool<br/>Heterogeneous migrations"]
        
        Replication --> Tasks
    end
    
    subgraph Target_Databases_Group["Target Databases"]
        RDS[Amazon RDS]
        Aurora[Amazon Aurora]
        Redshift[Amazon Redshift]
        S3Target[Amazon S3]
        DynamoDB[DynamoDB]
        OpenSearch[OpenSearch]
        Kinesis[Kinesis Data Streams]
    end
    
    Oracle --> SCT
    SQLServer --> SCT
    
    SCT --> Replication
    
    MySQL --> Replication
    PostgreSQL --> Replication
    MongoDB --> Replication
    SAP --> Replication
    S3Source --> Replication
    
    Tasks --> RDS
    Tasks --> Aurora
    Tasks --> Redshift
    Tasks --> S3Target
    Tasks --> DynamoDB
    Tasks --> OpenSearch
    Tasks --> Kinesis
    
    CDC["Continuous Data Capture CDC<br/>Ongoing replication<br/>Minimal downtime"] -.Feature.-> Replication
    
    classDef style1 fill:#FF9900
    class Replication style1
    classDef style2 fill:#569A31
    class SCT style2
```

### DMS Migration Types

```mermaid
graph LR
    subgraph Full_Load_Group["Full Load"]
        FL["Full Load Migration<br/>One-time migration<br/>Snapshot of data"]
        
        FL_Steps["1. Stop writes to source<br/>2. Migrate all data<br/>3. Switch to target<br/>⚠️ Downtime required"]
    end
    
    subgraph Full_Load_CDC_Group["Full Load + CDC"]
        FLCDC["Full Load + CDC<br/>Minimal downtime<br/>Recommended approach"]
        
        FLCDC_Steps["1. Full load starts<br/>2. CDC captures changes<br/>3. Apply cached changes<br/>4. Ongoing replication<br/>✅ Minimal downtime"]
    end
    
    subgraph CDC_Only_Group["CDC Only"]
        CDC["CDC Only<br/>Replicate ongoing changes<br/>Assumes data already migrated"]
        
        CDC_Steps["1. Existing data in target<br/>2. Replicate changes only<br/>3. Keep in sync<br/>Use: After full load"]
    end
    
    FL --> FL_Steps
    FLCDC --> FLCDC_Steps
    CDC --> CDC_Steps
    
    Recommendation["Recommendation:<br/>Use Full Load + CDC<br/>for production migrations"]
    
    classDef style1 fill:#569A31
    class FLCDC style1
    classDef style2 fill:#FF9900
    class FL style2
```

### DMS with Schema Conversion Tool

```mermaid
sequenceDiagram
    participant Source as Oracle Database On-Premises
    participant SCT as Schema Conversion Tool
    participant DMS as DMS Replication Instance
    participant Target as Amazon Aurora PostgreSQL
    
    Note over Source,Target: Heterogeneous Migration
    
    Source->>SCT: 1. Assess database schema
    SCT->>SCT: 2. Analyze compatibility
    SCT->>SCT: 3. Generate migration report
    
    Note over SCT: Conversion Assessment Report
    Note over SCT: Automatic 80%, Manual 20%
    
    SCT->>Target: 4. Convert and create schema
    Note over Target: Tables, indexes, constraints created
    
    Source->>DMS: 5. Start full load migration
    DMS->>Target: 6. Migrate data
    
    Note over Source,Target: During migration
    
    Source->>DMS: 7. CDC captures ongoing changes
    DMS->>Target: 8. Apply changes continuously
    
    Note over Source,Target: Cutover
    
    Source->>Source: 9. Stop application
    DMS->>Target: 10. Final CDC sync
    Target->>Target: 11. Switch application to target
    
```

## AWS Application Migration Service (MGN)

### MGN CloudEndure Migration

```mermaid
graph TB
    subgraph Source_Environment_Group["Source Environment"]
        Physical[Physical Servers]
        Virtual[Virtual Machines]
        Cloud["Other Cloud<br/>Azure, GCP"]
        
        Agent["MGN Replication Agent<br/>Installed on each server"]
        
        Physical --> Agent
        Virtual --> Agent
        Cloud --> Agent
    end
    
    subgraph AWS_Migration_Service_Group["AWS Migration Service"]
        MGN["AWS Application<br/>Migration Service<br/>Automated Lift-and-Shift"]
        
        Staging["Staging Area<br/>Low-cost replication<br/>EBS volumes"]
        
        MGN --> Staging
    end
    
    subgraph Target_AWS_Group["Target AWS"]
        Testing["Test Instances<br/>Non-disruptive testing<br/>Isolated environment"]
        
        Production["Production Instances<br/>Cutover when ready<br/>Minimal downtime"]
    end
    
    Agent -.Continuous<br/>Block-level replication.-> Staging
    
    Staging --> Testing
    Testing -.Launch cutover.-> Production
    
    Cutover["Cutover Process:<br/>1. Stop replication agent<br/>2. Launch target instances<br/>3. Switch DNS/network<br/>4. Application running on AWS<br/>Downtime: Minutes"]
    
    Features["Features:<br/>✅ Continuous replication<br/>✅ Non-disruptive testing<br/>✅ Automated conversion<br/>✅ Minimal downtime &lt;1 hour<br/>✅ Any source to AWS"]
    
    classDef style1 fill:#FF9900
    class MGN style1
    classDef style2 fill:#569A31
    class Production style2
```

## AWS DataSync

### DataSync Architecture

```mermaid
graph TB
    subgraph Source_Locations_Group["Source Locations"]
        NFS["NFS Server<br/>On-premises"]
        SMB["SMB Server<br/>On-premises"]
        HDFS["HDFS Cluster<br/>Hadoop"]
        S3Compatible[S3-compatible storage]
        
        Agent["DataSync Agent<br/>VM on-premises<br/>or EC2"]
        
        NFS --> Agent
        SMB --> Agent
        HDFS --> Agent
    end
    
    subgraph AWS_DataSync_Service_Group["AWS DataSync Service"]
        DataSync["AWS DataSync<br/>Managed data transfer<br/>Accelerated, encrypted"]
        
        Schedule["Scheduled Tasks<br/>Hourly, daily, weekly<br/>or one-time"]
        
        Verification["Data Verification<br/>Integrity checks<br/>End-to-end"]
        
        DataSync --> Schedule
        DataSync --> Verification
    end
    
    subgraph Destination_Locations_Group["Destination Locations"]
        S3["Amazon S3<br/>All storage classes"]
        EFS["Amazon EFS<br/>File system"]
        FSx["Amazon FSx<br/>Windows/Lustre/NetApp/OpenZFS"]
    end
    
    Agent --> DataSync
    S3Compatible --> DataSync
    
    DataSync --> S3
    DataSync --> EFS
    DataSync --> FSx
    
    Features["Features:<br/>✅ 10x faster than open-source tools<br/>✅ Bandwidth throttling<br/>✅ Data encryption in-transit<br/>✅ Data integrity validation<br/>✅ Pay per GB transferred<br/>✅ Incremental transfers"]
    
    VsSnowball["DataSync vs Snowball:<br/>DataSync: Online transfer, recurring<br/>Snowball: Offline, one-time large migration"]
    
    classDef style1 fill:#FF9900
    class DataSync style1
    classDef style2 fill:#569A31
    class Agent style2
```

### DataSync Transfer Flow

```mermaid
sequenceDiagram
    participant OnPrem as On-Premises NFS
    participant Agent as DataSync Agent
    participant DataSync as AWS DataSync
    participant S3 as Amazon S3
    
    OnPrem->>Agent: 1. Configure source
    Agent->>DataSync: 2. Create task
    DataSync->>S3: 3. Create destination location
    
    loop Scheduled Transfer
        DataSync->>Agent: 4. Start task execution
        Agent->>OnPrem: 5. Read files
        Agent->>Agent: 6. Compress & encrypt
        Agent->>DataSync: 7. Transfer over network
        DataSync->>DataSync: 8. Optimize transfer
        DataSync->>S3: 9. Write to S3
        DataSync->>DataSync: 10. Verify data integrity
        DataSync->>DataSync: 11. Generate report
    end
    
    DataSync->>CloudWatch: Send metrics & logs
    
    Note over OnPrem,S3: Features: TLS encryption, Bandwidth throttling, Incremental transfers, Metadata preservation
    
```

## AWS Transfer Family

### Transfer Family Services

```mermaid
graph TB
    subgraph Clients_Group["Clients"]
        SFTP_Client[SFTP Clients]
        FTPS_Client[FTPS Clients]
        FTP_Client[FTP Clients]
        AS2_Client[AS2 EDI Partners]
    end
    
    subgraph AWS_Transfer_Family_Group["AWS Transfer Family"]
        SFTP["Transfer for SFTP<br/>SSH File Transfer Protocol"]
        FTPS["Transfer for FTPS<br/>FTP over SSL/TLS"]
        FTP["Transfer for FTP<br/>File Transfer Protocol"]
        AS2["Transfer for AS2<br/>EDI B2B"]
        
        Auth["Authentication:<br/>• Service-managed<br/>• Active Directory<br/>• Custom Lambda<br/>• Okta, Auth0"]
        
        SFTP --> Auth
        FTPS --> Auth
        FTP --> Auth
        AS2 --> Auth
    end
    
    subgraph Storage_Backends_Group["Storage Backends"]
        S3["Amazon S3<br/>Object storage"]
        EFS["Amazon EFS<br/>File storage"]
    end
    
    subgraph Features_Group["Features"]
        VPC["VPC Hosted<br/>Private endpoints"]
        Public["Internet-facing<br/>Public endpoints"]
        DNS["Custom DNS<br/>Your domain"]
    end
    
    SFTP_Client --> SFTP
    FTPS_Client --> FTPS
    FTP_Client --> FTP
    AS2_Client --> AS2
    
    SFTP --> S3
    SFTP --> EFS
    FTPS --> S3
    FTP --> S3
    AS2 --> S3
    
    SFTP -.Deploy.-> VPC
    SFTP -.Deploy.-> Public
    SFTP -.Use.-> DNS
    
    UseCase["Use Cases:<br/>• Legacy application migration<br/>• B2B file exchange<br/>• Data lake ingestion<br/>• Replace on-prem FTP servers<br/>💰 Pay per hour + data transferred"]
    
    classDef style1 fill:#FF9900
    class SFTP style1
    classDef style2 fill:#569A31
    class S3 style2
```

## AWS Snow Family Migration

### Snow Family Device Comparison

```mermaid
graph TB
    Decision["📊 Choose Your Device:<br/>• &lt; 10 TB → Snowcone<br/>• 10-80 TB → Snowball<br/>• &gt; 10 PB → Snowmobile"]
    
    subgraph Snowcone_Group["Snowcone"]
        Snowcone["AWS Snowcone<br/>Smallest device"]
        
        Snowcone_Specs["Specs:<br/>💾 8-14 TB usable<br/>💪 2 vCPUs, 4 GB RAM<br/>📦 4.5 lbs / 2 kg<br/>🔋 Battery optional<br/>📡 Wi-Fi optional"]
        
        Snowcone_Use["Use Cases:<br/>• Edge computing<br/>• IoT<br/>• Remote locations<br/>• Drones<br/>• Vehicles"]
        
        Snowcone --> Snowcone_Specs
        Snowcone_Specs --> Snowcone_Use
    end
    
    subgraph Snowball_Group["Snowball Edge"]
        Snowball["AWS Snowball Edge"]
        
        Storage["Storage Optimized<br/>💾 80 TB usable<br/>💪 40 vCPUs, 80 GB RAM<br/>📦 50 lbs"]
        
        Compute["Compute Optimized<br/>💾 42-28 TB usable<br/>💪 52 vCPUs, 208 GB RAM<br/>🎮 Optional GPU"]
        
        Snowball_Use["Use Cases:<br/>• Data center migration<br/>• Disaster recovery<br/>• Content distribution<br/>• Local processing"]
        
        Snowball --> Storage
        Snowball --> Compute
        Storage --> Snowball_Use
        Compute --> Snowball_Use
    end
    
    subgraph Snowmobile_Group["Snowmobile"]
        Snowmobile["AWS Snowmobile<br/>Shipping container"]
        
        Snowmobile_Specs["Specs:<br/>💾 100 PB capacity<br/>🚛 45-foot container<br/>🔒 GPS tracking<br/>👮 Security escort<br/>📹 Video surveillance"]
        
        Snowmobile_Use["Use Cases:<br/>• Exabyte-scale migration<br/>• Complete datacenter<br/>• Video libraries<br/>• Massive datasets"]
        
        Snowmobile --> Snowmobile_Specs
        Snowmobile_Specs --> Snowmobile_Use
    end
    
    Decision -.-> Snowcone
    Decision -.-> Snowball
    Decision -.-> Snowmobile
    
    classDef style1 fill:#569A31,stroke:#333,stroke-width:2px,color:#fff
    classDef style2 fill:#FF9900,stroke:#333,stroke-width:2px,color:#fff
    classDef style3 fill:#146EB4,stroke:#333,stroke-width:2px,color:#fff
    classDef decisionStyle fill:#232F3E,stroke:#FF9900,stroke-width:3px,color:#fff
    
    class Snowcone,Snowcone_Specs,Snowcone_Use style1
    class Snowball,Storage,Compute,Snowball_Use style2
    class Snowmobile,Snowmobile_Specs,Snowmobile_Use style3
    class Decision decisionStyle
```

### Snow Family with Edge Computing

```mermaid
graph TB
    subgraph Edge_Location_Remote_Site_Group["Edge Location Remote Site"]
        Snowball["Snowball Edge<br/>Compute Optimized"]
        
        LocalData["Local Data Sources<br/>Sensors, Cameras, IoT"]
        
        EC2["EC2 Instances<br/>Running on Snowball"]
        
        Lambda["Lambda Functions<br/>Local processing"]
        
        LocalData --> Snowball
        Snowball --> EC2
        Snowball --> Lambda
    end
    
    subgraph Processing_at_Edge_Group["Processing at Edge"]
        Analysis["Data Analysis<br/>ML inference<br/>Video processing<br/>Image recognition"]
        
        Storage["Local Storage<br/>Buffer data<br/>80 TB capacity"]
        
        EC2 --> Analysis
        Analysis --> Storage
    end
    
    subgraph AWS_Cloud_Group["AWS Cloud"]
        S3["Amazon S3<br/>Final destination"]
        
        CloudProcessing["Cloud Processing<br/>ML training<br/>Analytics<br/>Long-term storage"]
    end
    
    Storage -.Ship device back.-> S3
    Storage -.DataSync over network.-> S3
    
    S3 --> CloudProcessing
    
    UseCase["Edge Computing Use Cases:<br/>• Oil & gas exploration<br/>• Military operations<br/>• Cruise ships<br/>• Mining sites<br/>• Manufacturing floors<br/>• Disaster zones"]
    
    OpsHub["AWS OpsHub<br/>GUI management tool<br/>Manage Snow devices"] -.Manages.-> Snowball
    
    classDef style1 fill:#FF9900
    class Snowball style1
    classDef style2 fill:#569A31
    class Analysis style2
```

## Migration Timeline

### Typical Large-Scale Migration

```mermaid
gantt
    title AWS Migration Project Timeline
    dateFormat YYYY-MM-DD
    section Assessment
    Discovery & Assessment          :2024-01-01, 30d
    Business Case & Planning        :2024-01-15, 45d
    
    section Mobilize
    Setup Landing Zone             :2024-02-01, 20d
    Security & Compliance          :2024-02-10, 30d
    Training & Enablement          :2024-02-15, 45d
    
    section Migrate
    Wave 1 - Non-critical Apps     :2024-03-01, 60d
    Wave 2 - Dev/Test              :2024-03-15, 60d
    Wave 3 - Production Apps       :2024-04-15, 90d
    Wave 4 - Databases             :2024-05-01, 75d
    
    section Optimize
    Cost Optimization              :2024-06-01, 90d
    Performance Tuning             :2024-06-15, 60d
    Decommission On-Prem           :2024-07-15, 45d
```

