# Module 10: Migration & Transfer Services

## Overview
AWS provides a comprehensive set of services to migrate applications, databases, and data to the cloud. This module covers migration strategies, tools, and best practices for moving workloads to AWS.

## Learning Objectives
- Understand the 6 R's of migration strategy
- Use AWS DataSync for data transfer
- Migrate databases with AWS Database Migration Service (DMS)
- Track migrations using AWS Migration Hub
- Plan and execute cloud migrations effectively

---

## 1. Migration Strategies (6 R's)

### The 6 R's of Migration

1. **Rehost (Lift and Shift)**
   - Move applications as-is to AWS
   - Fastest migration approach
   - Use AWS Application Migration Service (MGN)
   - Example: Move VM-based applications to EC2

2. **Replatform (Lift, Tinker, and Shift)**
   - Make a few cloud optimizations
   - No core architecture changes
   - Example: Migrate database to RDS instead of EC2

3. **Repurchase (Drop and Shop)**
   - Move to a different product (usually SaaS)
   - Example: Migrate CRM to Salesforce

4. **Refactor/Re-architect**
   - Reimagine how application is architected
   - Use cloud-native features
   - Example: Move monolith to microservices on ECS/Lambda

5. **Retire**
   - Identify IT assets that are no longer useful
   - Turn off unnecessary applications
   - Reduce cost and complexity

6. **Retain (Revisit)**
   - Keep applications in source environment
   - Applications not ready for migration
   - Plan to migrate later

---

## 2. AWS DataSync

### What is AWS DataSync?
- **Automated data transfer service**
- Move data between on-premises storage and AWS
- Transfer data between AWS storage services
- Secure, fast, and simple data migration

### Key Features
- **Fast**: Up to 10x faster than open-source tools
- **Automated**: Handles data transfer, encryption, validation
- **Secure**: Encryption in-transit with TLS
- **Cost-effective**: Pay only for data copied

### DataSync Architecture

```
┌─────────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  On-Premises        │         │   AWS DataSync   │         │  AWS Storage    │
│                     │         │                  │         │                 │
│  - NFS              │◄───────►│  - Agent         │◄───────►│  - S3           │
│  - SMB              │         │  - Task          │         │  - EFS          │
│  - HDFS             │         │  - Scheduling    │         │  - FSx          │
└─────────────────────┘         └──────────────────┘         └─────────────────┘
```

### Use Cases
1. **Data Migration**: Move on-premises data to AWS
2. **Data Replication**: Replicate data for backup/DR
3. **Data Processing Workflows**: Transfer data for processing
4. **Archive Cold Data**: Move infrequently accessed data to S3 Glacier

### Supported Storage Systems

**Source Locations:**
- NFS shares (Network File System)
- SMB shares (Server Message Block)
- HDFS (Hadoop Distributed File System)
- Self-managed object storage
- AWS Snowcone
- Amazon S3
- Amazon EFS
- Amazon FSx for Windows File Server
- Amazon FSx for Lustre
- Amazon FSx for OpenZFS
- Amazon FSx for NetApp ONTAP

**Destination Locations:**
- Amazon S3 (all storage classes)
- Amazon EFS
- Amazon FSx for Windows File Server
- Amazon FSx for Lustre
- Amazon FSx for OpenZFS
- Amazon FSx for NetApp ONTAP

### DataSync Agent
- **Virtual machine** deployed on-premises or in-cloud
- Connects to your storage system
- Communicates with AWS DataSync service
- Download from AWS Console as VMware, Hyper-V, or KVM image

### Creating a DataSync Task

**Step 1: Deploy the Agent**
```bash
# Agent installed on-premises as VM
# Agent activated through AWS Console
```

**Step 2: Configure Source and Destination**
- Source location: On-premises NFS/SMB server
- Destination location: S3, EFS, FSx

**Step 3: Configure Task Settings**
- Data verification options
- Bandwidth throttling
- Filtering (include/exclude patterns)
- Scheduling

**Step 4: Execute and Monitor**
- Run task manually or on schedule
- Monitor progress in CloudWatch

### DataSync Features

**Data Integrity Verification:**
- Checks data consistency at source and destination
- Verifies data after transfer

**Bandwidth Management:**
- Throttle bandwidth to limit network impact
- Configure limits per task

**Filtering:**
```bash
# Include only specific file patterns
Include: *.log, *.txt

# Exclude directories
Exclude: /temp/*, /cache/*
```

**Scheduling:**
- Hourly, daily, weekly, or custom schedules
- Automated recurring transfers

### Pricing
- **Per-GB transferred**: $0.0125 per GB
- No upfront fees or software licenses
- No charge for data transferred within same AWS Region

### Exam Tips
✅ **DataSync vs Snow Family**
   - DataSync: For ongoing or regular transfers over network
   - Snow Family: For one-time large migrations or limited bandwidth

✅ **DataSync vs S3 Transfer Acceleration**
   - DataSync: For file systems (NFS, SMB) to AWS
   - S3 Transfer Acceleration: For direct uploads to S3

✅ **DataSync vs Storage Gateway**
   - DataSync: Data migration and transfer
   - Storage Gateway: Hybrid cloud storage with local caching

---

## 3. AWS Database Migration Service (DMS)

### What is AWS DMS?
- **Managed database migration service**
- Migrate databases to AWS quickly and securely
- Source database remains operational during migration
- Supports homogeneous and heterogeneous migrations

### Key Features
- **Minimal Downtime**: Source database stays operational
- **Continuous Data Replication**: Keep databases in sync
- **Broad Database Support**: 20+ database engines
- **Low Cost**: Pay only for compute resources and log storage

### DMS Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     AWS DMS Process                         │
│                                                             │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────┐ │
│  │   Source     │─────►│ Replication  │─────►│  Target  │ │
│  │   Database   │      │   Instance   │      │ Database │ │
│  │              │      │   (EC2)      │      │          │ │
│  └──────────────┘      └──────────────┘      └──────────┘ │
│                              │                             │
│                              ▼                             │
│                        ┌──────────┐                        │
│                        │ DMS Task │                        │
│                        └──────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

### Migration Types

**1. Homogeneous Migration**
- Same database engine (Oracle → Oracle)
- Source and target are same type
- Simple schema and data migration

**2. Heterogeneous Migration**
- Different database engines (Oracle → PostgreSQL)
- Requires AWS Schema Conversion Tool (SCT)
- More complex, needs schema conversion

### Supported Databases

**Source Databases:**
- Oracle
- Microsoft SQL Server
- MySQL
- MariaDB
- PostgreSQL
- MongoDB
- SAP ASE
- IBM Db2
- Azure SQL Database
- Amazon RDS
- Amazon Aurora
- Amazon S3
- Amazon DocumentDB

**Target Databases:**
- Oracle
- Microsoft SQL Server
- MySQL
- MariaDB
- PostgreSQL
- Amazon RDS
- Amazon Aurora
- Amazon Redshift
- Amazon DynamoDB
- Amazon S3
- Amazon OpenSearch
- Amazon Kinesis Data Streams
- Amazon DocumentDB
- Amazon Neptune
- Redis

### DMS Components

**1. Replication Instance**
- EC2 instance that runs DMS tasks
- Performs actual data migration
- Size based on workload and data volume

**2. Endpoints**
- Source endpoint: Connection to source database
- Target endpoint: Connection to target database
- Configure connection details and credentials

**3. Replication Tasks**
- Defines what tables to migrate
- Configures migration type
- Sets transformation rules

### Migration Task Types

**1. Full Load (Migrate Existing Data)**
- One-time migration of all data
- Snapshots source database and loads to target
- Good for static data or initial load

**2. CDC (Change Data Capture)**
- Replicate ongoing changes
- Captures changes after full load
- Keeps source and target in sync

**3. Full Load + CDC**
- Initial full load followed by ongoing replication
- Most common migration pattern
- Minimize downtime

### AWS Schema Conversion Tool (SCT)

**Purpose:**
- Convert database schema from one engine to another
- Handles heterogeneous migrations
- Converts stored procedures, functions, views

**Use Cases:**
- Oracle → PostgreSQL
- SQL Server → MySQL
- Oracle → Amazon Aurora

**Process:**
```
1. Connect to source database
2. Analyze and assess compatibility
3. Convert schema automatically
4. Manually fix incompatible code
5. Apply schema to target database
6. Use DMS for data migration
```

**Assessment Report:**
- Identifies what can be automatically converted
- Highlights manual changes needed
- Provides complexity estimates

### DMS Task Configuration

**Table Mappings:**
```json
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "include-all-tables",
      "object-locator": {
        "schema-name": "myschema",
        "table-name": "%"
      },
      "rule-action": "include"
    }
  ]
}
```

**Transformation Rules:**
```json
{
  "rule-type": "transformation",
  "rule-id": "2",
  "rule-name": "rename-schema",
  "rule-action": "rename",
  "rule-target": "schema",
  "object-locator": {
    "schema-name": "myschema"
  },
  "value": "newschema"
}
```

### Multi-AZ Deployment
- High availability for replication instance
- Automatic failover
- Synchronous replication to standby
- Used for production migrations

### DMS Monitoring
- **CloudWatch Metrics**: CPU, memory, disk usage
- **Task Logs**: Detailed migration logs
- **Table Statistics**: Row counts, errors
- **Validation**: Compare source and target data

### Best Practices

1. **Right-Size Replication Instance**
   - T3 instances for testing
   - C5 instances for production migrations
   - R5 instances for large tables

2. **Use Multi-AZ for Production**
   - High availability
   - Minimal downtime

3. **Enable Validation**
   - Verify data integrity
   - Detect discrepancies

4. **Optimize Performance**
   - Use parallel load for large tables
   - Batch apply for better throughput
   - LOB (Large Object) optimization

5. **Test Before Production**
   - Run test migrations
   - Validate data and performance
   - Plan cutover strategy

### Pricing
- **Replication Instance**: Hourly pricing based on instance type
- **Storage**: $0.115 per GB-month for change logs
- **Data Transfer**: Standard data transfer rates

### Exam Tips
✅ **DMS for ongoing replication**: Continuous data replication with CDC

✅ **SCT for heterogeneous migrations**: Different database engines require Schema Conversion Tool

✅ **Multi-AZ for production**: High availability for critical migrations

✅ **Snowball + DMS**: Use Snowball Edge for initial large data load, then DMS for CDC

---

## 4. AWS Migration Hub

### What is AWS Migration Hub?
- **Single location to track migrations**
- Centralized dashboard for migration progress
- Integrates with AWS and partner migration tools
- Free service (pay only for underlying tools)

### Key Features
- **Track Application Migrations**: Monitor servers and databases
- **Visualize Progress**: Unified view across tools
- **Integration**: Works with CloudEndure, DMS, Server Migration Service
- **Grouping**: Organize servers into applications

### Migration Hub Architecture

```
┌──────────────────────────────────────────────────────────────┐
│              AWS Migration Hub Console                       │
│                                                              │
│  ┌────────────┐  ┌────────────┐  ┌─────────────────────┐   │
│  │ Application│  │  Server    │  │   Migration Status  │   │
│  │  Grouping  │  │ Discovery  │  │    Dashboard        │   │
│  └────────────┘  └────────────┘  └─────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
           │                 │                    │
           ▼                 ▼                    ▼
    ┌────────────┐    ┌─────────────┐    ┌──────────────┐
    │    DMS     │    │   Server    │    │  CloudEndure │
    │            │    │  Migration  │    │   Migration  │
    └────────────┘    │   Service   │    └──────────────┘
                      └─────────────┘
```

### Core Components

**1. Application Discovery**
- Discover on-premises servers
- Understand dependencies
- Group servers into applications

**2. Migration Tools Integration**
- AWS Application Migration Service (MGN)
- AWS Database Migration Service (DMS)
- AWS Server Migration Service (SMS)
- Partner tools (CloudEndure, ATADATA, etc.)

**3. Migration Tracking**
- Server-level migration status
- Application-level migration status
- Timeline and progress tracking

### AWS Application Discovery Service

**Purpose:**
- Plan migrations by gathering data about on-premises infrastructure
- Discover servers, VMs, and applications

**Discovery Types:**

**Agentless Discovery (VMware vCenter)**
- VM information (CPU, memory, disk)
- No software installation required
- Limited to VMware environments

**Agent-based Discovery**
- Detailed information (processes, network connections)
- Install AWS Discovery Agent on servers
- Works on physical and virtual servers

**Discovery Data Collected:**
- Server specifications (CPU, memory, disk)
- Network dependencies and connections
- Running processes and performance data
- Resource utilization over time

### Migration Hub Strategy Recommendations

**Purpose:**
- Automated migration strategy recommendations
- Analyze application portfolio
- Recommend optimal 6 R strategy

**Features:**
- Assess applications for migration readiness
- Recommend migration patterns (rehost, replatform, etc.)
- Estimate migration effort and cost
- Prioritize applications for migration

### Setting Up Migration Hub

**Step 1: Choose Home Region**
- Select single home region for Migration Hub
- All migration data stored in this region

**Step 2: Connect Migration Tools**
- Authorize tools to send data to Migration Hub
- Configure DMS, MGN, or SMS

**Step 3: Group Applications**
- Create application groups
- Add servers and databases to groups

**Step 4: Track Progress**
- Monitor migration status
- View updates from integrated tools

### Application Grouping

**Why Group Applications?**
- Track related resources together
- Understand application dependencies
- Coordinate migration of entire apps

**Example Application Group:**
```
Application: E-Commerce Website
├── Web Server (3 instances)
├── Application Server (2 instances)
├── Database Server (MySQL)
└── Cache Server (Redis)
```

### Migration Status Tracking

**Server Status:**
- Not Started
- In Progress
- Completed
- Failed

**Migration Phases:**
1. **Discovery**: Identify and assess servers
2. **Planning**: Group and plan migrations
3. **Migration**: Execute using tools
4. **Validation**: Verify successful migration

### AWS Server Migration Service (SMS) - Legacy

**Note:** Being replaced by AWS Application Migration Service (MGN)

**Features:**
- Automate VM migration to AWS
- Incremental replication
- Schedule migration windows
- Minimal downtime

### AWS Application Migration Service (MGN)

**Purpose:**
- Lift-and-shift migration (Rehost)
- Replaces CloudEndure and SMS
- Automated infrastructure conversion

**How It Works:**
```
1. Install AWS Replication Agent on source servers
2. Continuous block-level replication to AWS
3. Launch test instances for validation
4. Cutover to production instances
5. Decommission source servers
```

**Key Features:**
- Continuous data replication
- Non-disruptive testing
- Point-in-time recovery
- Automated orchestration

**Use Cases:**
- Large-scale lift-and-shift migrations
- Disaster recovery
- Cloud-based testing and development

### Integration with Other AWS Services

**AWS CloudFormation:**
- Infrastructure as code for migrated resources
- Template-based deployment

**AWS Systems Manager:**
- Manage migrated instances
- Patch management and automation

**Amazon CloudWatch:**
- Monitor migration performance
- Set up alarms for migration tasks

### Best Practices

1. **Start with Discovery**
   - Use Application Discovery Service
   - Understand dependencies before migration

2. **Group Related Resources**
   - Create application groups
   - Migrate entire applications together

3. **Choose Right Migration Tool**
   - DMS for databases
   - MGN for servers (lift-and-shift)
   - DataSync for file systems

4. **Test Before Cutover**
   - Validate in test environment
   - Performance testing
   - Application functionality testing

5. **Monitor Progress**
   - Use Migration Hub dashboard
   - Track completion percentage
   - Address issues promptly

### Migration Hub Pricing
- **Free service**
- Pay only for underlying migration tools
- No additional charge for tracking and monitoring

### Exam Tips
✅ **Centralized tracking**: Migration Hub provides single dashboard for all migrations

✅ **Application Discovery Service**: Discover servers and dependencies before migration

✅ **Integration**: Works with DMS, MGN, and partner tools

✅ **Application grouping**: Group servers and databases by application

✅ **Strategy Recommendations**: Automated recommendations for 6 R's migration strategy

---

## 5. Other Migration Services

### AWS Transfer Family
- **Managed file transfer service**
- Supports SFTP, FTPS, FTP, AS2 protocols
- Transfer files directly into S3 or EFS
- No infrastructure management

**Use Cases:**
- Replace legacy file transfer systems
- Share files with partners
- Data lake ingestion

### AWS Snow Family

**AWS Snowcone**
- Small, portable edge computing and data transfer device
- 8 TB usable storage
- Use for edge computing and data transfer
- Can run EC2 instances and Lambda functions

**AWS Snowball Edge**
- 80 TB or 210 TB of usable storage
- Compute capabilities (EC2, Lambda)
- Storage Optimized or Compute Optimized options
- For large data migrations and edge computing

**AWS Snowmobile**
- Exabyte-scale data transfer
- 100 PB per Snowmobile
- Physical truck for massive migrations
- For datacenter migrations

**When to Use:**
- Limited bandwidth
- Large data volumes (> 10 TB)
- One-time migrations
- Secure data transfer

### AWS Application Discovery Service
- Already covered in Migration Hub section
- Discovers on-premises infrastructure
- Agentless or agent-based discovery

### AWS Migration Evaluator
- **Assess on-premises infrastructure**
- Build business case for cloud migration
- Analyze cost and performance
- Formerly TSO Logic

**Features:**
- Quick insights into current state
- Cost projections for AWS
- Right-sizing recommendations
- ROI analysis

### AWS Mainframe Modernization
- Migrate and modernize mainframe applications
- Automated refactoring or replatforming
- Managed runtime environment
- Supports COBOL, PL/I, JCL

---

## 6. Migration Best Practices

### Migration Phases

**1. Assess**
- Discover current infrastructure
- Identify dependencies
- Create business case
- Estimate costs

**2. Mobilize**
- Create migration plan
- Set up landing zone
- Build migration team
- Security and compliance planning

**3. Migrate & Modernize**
- Execute migration using appropriate tools
- Validate and test
- Optimize and modernize
- Decommission on-premises resources

### AWS Cloud Adoption Framework (CAF)

**6 Perspectives:**

**Business:**
- Align IT with business goals
- Create business case
- ROI justification

**People:**
- Training and organizational change
- Skill development
- Change management

**Governance:**
- Cloud governance model
- Cost management
- Risk management

**Platform:**
- Architecture design
- Landing zone setup
- Cloud-native capabilities

**Security:**
- Identity and access management
- Data protection
- Compliance

**Operations:**
- Monitoring and logging
- Incident management
- Business continuity

### Security During Migration

1. **Encryption in Transit**: TLS/SSL for data transfer
2. **Encryption at Rest**: Encrypt data in AWS storage
3. **IAM Policies**: Least privilege access
4. **VPN/Direct Connect**: Secure network connectivity
5. **Compliance**: Maintain compliance during migration

### Performance Optimization

1. **Network Optimization**
   - Use AWS Direct Connect for large transfers
   - Enable Multi-Part Upload for S3
   - Use DataSync for optimal performance

2. **Parallel Processing**
   - Migrate multiple servers simultaneously
   - Parallel table loads in DMS

3. **Compression**
   - Compress data before transfer
   - Reduce transfer time and cost

---

## 7. Exam Tips Summary

### Key Concepts to Remember

✅ **6 R's of Migration**
   - Rehost, Replatform, Repurchase, Refactor, Retire, Retain
   - Choose based on business needs and complexity

✅ **DataSync**
   - Automated data transfer (NFS/SMB to AWS)
   - 10x faster than open-source tools
   - Use agent for on-premises sources

✅ **DMS (Database Migration Service)**
   - Minimal downtime database migration
   - Supports homogeneous and heterogeneous migrations
   - Use SCT for schema conversion (different engines)
   - CDC for continuous replication

✅ **Migration Hub**
   - Centralized tracking dashboard
   - Integrates with DMS, MGN, and partner tools
   - Application grouping and progress tracking
   - Free service

✅ **Snow Family**
   - Snowcone: 8 TB, edge computing
   - Snowball: 80-210 TB, large migrations
   - Snowmobile: 100 PB, datacenter migrations
   - Use when bandwidth is limited

✅ **Application Migration Service (MGN)**
   - Lift-and-shift (rehost) migrations
   - Continuous replication
   - Automated cutover
   - Replaces CloudEndure and SMS

### Common Scenarios

**Scenario 1: Large Database Migration**
- Solution: DMS with Multi-AZ, Full Load + CDC
- For heterogeneous: Use SCT first

**Scenario 2: Ongoing File Sync**
- Solution: DataSync with scheduled tasks
- Alternative: Storage Gateway for hybrid access

**Scenario 3: Migrate 500 Servers**
- Solution: Application Migration Service (MGN)
- Track with Migration Hub

**Scenario 4: Limited Bandwidth, 50 TB Data**
- Solution: AWS Snowball Edge
- Follow up with DataSync for incremental changes

**Scenario 5: Track Multiple Migration Tools**
- Solution: AWS Migration Hub
- Centralized dashboard for all tools

---

## 8. Hands-On Practice

### Lab 1: DMS Database Migration
1. Create source and target databases (RDS)
2. Create DMS replication instance
3. Configure source and target endpoints
4. Create migration task (Full Load + CDC)
5. Monitor migration progress
6. Validate data

### Lab 2: DataSync File Transfer
1. Set up source NFS share (or use S3)
2. Deploy DataSync agent (if on-premises)
3. Create DataSync task
4. Configure destination (S3, EFS)
5. Execute task and monitor

### Lab 3: Migration Hub Setup
1. Choose home region
2. Connect migration tools
3. Discover servers (Application Discovery Service)
4. Create application groups
5. Track migration progress

---

## 9. Additional Resources

### AWS Documentation
- [AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/)
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/)
- [AWS DataSync](https://docs.aws.amazon.com/datasync/)
- [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/)

### AWS Whitepapers
- AWS Cloud Adoption Framework
- AWS Migration Best Practices
- Database Migration Guide

### AWS Training
- AWS Migration Learning Plan
- Deep Dive on AWS Migration Services
- Hands-on DMS Workshop

---

## Quick Reference

| Service | Purpose | Key Feature |
|---------|---------|-------------|
| **DataSync** | Automated data transfer | 10x faster, agent-based |
| **DMS** | Database migration | Minimal downtime, CDC |
| **Migration Hub** | Track migrations | Centralized dashboard |
| **SCT** | Schema conversion | Heterogeneous DB migrations |
| **MGN** | Server migration | Lift-and-shift, continuous replication |
| **Snow Family** | Physical data transfer | Limited bandwidth scenarios |
| **Transfer Family** | Managed file transfer | SFTP/FTPS to S3/EFS |

---

**Next Module:** [11-Analytics →](../11-Analytics/README.md)

**Previous Module:** [← 09-Monitoring](../09-Monitoring/README.md)

