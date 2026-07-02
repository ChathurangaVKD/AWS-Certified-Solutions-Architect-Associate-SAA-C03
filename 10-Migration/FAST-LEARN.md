# ⚡ Fast Learning - Migration & Transfer

> **Time to Complete**: 40-50 minutes | **Exam Weight**: ~8-12%

## 🎯 Must-Know Concepts (5 Minutes)

### Migration Service Selector (SDASMAD)
```
DATABASE? → DMS (Database Migration Service)
SERVERS? → Application Discovery Service, SMS
LARGE DATA? → Snowball, Snowmobile, DataSync
STORAGE? → Storage Gateway, Transfer Family
APPLICATIONS? → Application Migration Service (MGN)
```

**Memory Aid**: "Snow Delivers, DMS Migrates, DataSync Syncs, Storage Gateway Gates"

## 📊 Quick Reference Tables

### Snow Family (Physical Data Transfer)
| Device | Capacity | Use Case | Transfer Speed |
|--------|----------|----------|----------------|
| **Snowcone** | 8 TB | Edge computing, small transfers | Portable (fits in backpack) |
| **Snowball Edge Storage** | 80 TB | Large migrations, edge storage | Petabyte scale |
| **Snowball Edge Compute** | 42 TB + GPU | ML, processing at edge | Compute + storage |
| **Snowmobile** | 100 PB | Exabyte-scale migrations | Truck (literal!) |

**Decision**: Internet < 1 week → Direct transfer, Otherwise → Snow device

### Migration Services Matrix
| Service | What It Migrates | Direction | Use Case |
|---------|------------------|-----------|----------|
| **DMS** | Databases | Any ↔ AWS | Homogeneous/heterogeneous DB |
| **DataSync** | Files | On-prem ↔ AWS | NFS/SMB to S3/EFS/FSx |
| **Transfer Family** | Files via SFTP/FTP | Internet → S3/EFS | SFTP uploads to cloud |
| **Storage Gateway** | Hybrid storage | On-prem ↔ S3 | Hybrid cloud storage |
| **MGN** | Servers/VMs | On-prem → EC2 | Lift-and-shift migration |

## 🔥 Exam Hot Topics

### 1. AWS DMS (Database Migration Service)
```
CAPABILITIES:
├── Homogeneous (Oracle → Oracle)
├── Heterogeneous (Oracle → PostgreSQL)
│   └── Requires SCT (Schema Conversion Tool)
├── One-time migration
├── Continuous replication (CDC - Change Data Capture)
└── Migration + ongoing replication

SOURCES (20+):
├── On-premises databases
├── EC2 instances
├── RDS
├── S3
└── Azure SQL, MongoDB, etc.

TARGETS:
├── RDS, Aurora
├── Redshift
├── DynamoDB
├── S3
├── Elasticsearch
└── Kinesis, DocumentDB

EXAM TIP: Zero downtime migration
└── Source DB stays online during migration
```

### 2. Snow Family Deep Dive
```
SNOWCONE (Smallest)
├── 8 TB (HDD) or 14 TB (SSD)
├── 4 GB memory, 2 vCPUs
├── USB-C power (very portable)
├── DataSync agent pre-installed
└── Use: IoT, drone data, remote locations

SNOWBALL EDGE (Medium)
├── Storage Optimized: 80 TB
├── Compute Optimized: 42 TB + GPU
├── Can cluster up to 15 nodes
├── EC2/Lambda at edge
└── Use: Datacenter migrations, edge processing

SNOWMOBILE (Massive)
├── 100 PB capacity
├── Ruggedized shipping container
├── GPS tracked, video surveillance
├── Dedicated security team
└── Use: Exabyte-scale, datacenter shutdown
```

**Transfer Time Calculation**: 
- 100 TB over 100 Mbps = ~100 days
- Same with Snowball = ~1 week (including shipping)

### 3. AWS Storage Gateway Types
| Type | Interface | Use Case | Local Cache |
|------|-----------|----------|-------------|
| **File Gateway** | NFS/SMB | File storage in S3 | Yes |
| **Volume Gateway** | iSCSI | Block storage | Yes |
| **Tape Gateway** | iSCSI VTL | Backup (tape replacement) | Yes |

```
FILE GATEWAY
├── Files stored as objects in S3
├── SMB/NFS protocols
├── Local cache for frequent access
├── Lifecycle policies to Glacier
└── Use: File share backup to cloud

VOLUME GATEWAY (2 modes)
├── Cached Volumes: Primary in S3, cache local
└── Stored Volumes: Primary local, backup to S3

TAPE GATEWAY
├── Virtual Tape Library (VTL)
├── Integrates with backup software
├── Tapes archived to Glacier
└── Use: Replace physical tapes
```

### 4. AWS DataSync
```
WHAT: Automated data transfer service
PROTOCOLS: NFS, SMB
DESTINATIONS: S3, EFS, FSx

FEATURES:
├── Automatic encryption (in-transit)
├── Data validation/integrity checks
├── Bandwidth throttling
├── Schedule transfers
├── Up to 10 Gbps
└── Incremental transfers

AGENT: Required on-premises
USES: One-time migration or scheduled sync

VS STORAGE GATEWAY:
├── DataSync: One-time/scheduled transfers
└── Storage Gateway: Continuous hybrid storage
```

## 💡 Common Exam Scenarios

### Scenario 1: Migrate Oracle to PostgreSQL
**Q**: Migrate Oracle database to RDS PostgreSQL with minimal downtime
**✅ ANSWER**: DMS + SCT (Schema Conversion Tool) for heterogeneous migration

### Scenario 2: Transfer 80 TB, Slow Internet
**Q**: Transfer 80 TB data, internet is 100 Mbps (would take months)
**✅ ANSWER**: AWS Snowball Edge (1 week including shipping)

### Scenario 3: Continuous File Sync to S3
**Q**: On-prem file server needs to continuously sync to S3
**✅ ANSWER**: AWS Storage Gateway (File Gateway mode)

### Scenario 4: SFTP Upload to S3
**Q**: Third parties upload files via SFTP, need to land in S3
**✅ ANSWER**: AWS Transfer Family (SFTP, FTPS, FTP to S3)

### Scenario 5: One-Time NFS Migration
**Q**: Migrate 10 TB NFS share to EFS, one-time
**✅ ANSWER**: AWS DataSync

### Scenario 6: Entire Datacenter Migration
**Q**: Migrate 500 servers from on-prem to AWS
**✅ ANSWER**: AWS Application Migration Service (MGN)

### Scenario 7: Database with Continuous Replication
**Q**: MySQL on-prem, need ongoing replication to RDS
**✅ ANSWER**: DMS with CDC (Change Data Capture)

### Scenario 8: Exabyte-Scale Transfer
**Q**: 10 EB (exabytes) of data to migrate
**✅ ANSWER**: AWS Snowmobile (100 PB each, need ~100)

## 🎓 Speed Learning Tips

### DMS Replication Instance
```
WHAT: EC2 instance running DMS software
SIZE: Choose based on data volume & complexity
MULTI-AZ: Optional (for HA)

MIGRATION TYPES:
├── Full Load (one-time)
├── Full Load + CDC (ongoing)
└── CDC only (replicate changes)
```

### Schema Conversion Tool (SCT)
```
WHEN NEEDED: Heterogeneous migrations
├── Oracle → PostgreSQL ✅
├── SQL Server → MySQL ✅
├── Oracle → Aurora ✅
└── MySQL → MySQL ❌ (not needed)

CAPABILITIES:
├── Converts schema
├── Converts stored procedures
├── Converts views
├── Assessment report (compatibility)
└── Suggests cloud-native alternatives
```

### Transfer Acceleration Decision
```
When to use each:

DIRECT CONNECT:
✅ Dedicated, consistent bandwidth
✅ 1-100 Gbps
✅ Private connection
❌ Weeks to months setup
❌ Expensive

SNOWBALL:
✅ 10+ TB data
✅ Poor internet
✅ One-time migration
❌ Shipping time (days)

DATASYNC:
✅ Scheduled transfers
✅ NFS/SMB sources
✅ Automated
❌ Limited to 10 Gbps

TRANSFER FAMILY:
✅ SFTP/FTP protocol needed
✅ External users uploading
❌ Higher cost
```

## 📝 Rapid-Fire Facts

### Snow Family Comparison
```
CHOOSE SNOWCONE IF:
├── < 8-14 TB
├── Extreme portability needed
├── Edge computing (IoT)
└── Harsh environments

CHOOSE SNOWBALL IF:
├── 10 TB - 10 PB
├── Need clustering
├── Edge compute (EC2/Lambda)
└── Standard datacenter migration

CHOOSE SNOWMOBILE IF:
├── > 10 PB
├── Entire datacenter
└── Don't mind a truck showing up
```

### Application Migration Service (MGN)
```
FORMERLY: CloudEndure Migration

PROCESS:
1. Install agent on source servers
2. Continuous replication begins
3. Test in AWS (non-disruptive)
4. Cutover when ready
5. Source servers shut down

FEATURES:
├── Block-level replication
├── Minimal downtime (minutes)
├── Wide OS support
├── Automated conversion
└── Free (pay only for AWS resources)

VS SERVER MIGRATION SERVICE (SMS):
└── MGN is newer, recommended (SMS deprecated)
```

### Transfer Family Features
```
PROTOCOLS:
├── SFTP (SSH File Transfer Protocol)
├── FTPS (FTP over SSL)
└── FTP (File Transfer Protocol)

AUTHENTICATION:
├── Service-managed users
├── Custom identity provider (Lambda)
└── Active Directory/LDAP

DESTINATIONS:
├── Amazon S3
└── Amazon EFS

USE CASES:
├── Third-party file uploads
├── Replace on-prem SFTP servers
└── Secure file transfer to cloud
```

## 🚀 5-Minute Master Review

### Migration Decision Tree
```
1. What are you migrating?
   DATABASE → DMS (+ SCT if needed)
   FILES → DataSync or Storage Gateway
   SERVERS → Application Migration Service
   LARGE DATA → Snow family
   
2. For databases, same engine?
   YES → DMS only
   NO → DMS + SCT
   
3. For data transfer, how much?
   < 10 TB + good internet → Direct upload/DataSync
   10 TB - 10 PB + slow internet → Snowball
   > 10 PB → Snowmobile
   
4. Need ongoing sync?
   YES → Storage Gateway or DMS (CDC)
   NO → DataSync or Snow family
```

### Common Migration Patterns
```
1. DATABASE MIGRATION (Zero Downtime)
   On-prem DB → DMS (CDC) → RDS → Cutover
   
2. LIFT-AND-SHIFT (Servers)
   On-prem servers → MGN → EC2
   
3. FILE SHARE TO CLOUD
   On-prem NFS → DataSync → EFS → Cutover
   
4. LARGE DATA TRANSFER
   Datacenter → Snowball → S3 → Process
   
5. HYBRID STORAGE
   On-prem apps ←→ Storage Gateway ←→ S3
```

### DMS Best Practices
✅ Use Multi-AZ for production
✅ Enable CloudWatch logging
✅ Test with validation enabled
✅ Use CDC for minimal downtime
✅ Size replication instance appropriately
✅ Use SCT assessment before migration
✅ Migrate to Aurora when possible (better performance)

### Common Mistakes to Avoid
❌ Using internet for massive data transfer (use Snow)
❌ Not testing DMS migration before cutover
❌ Forgetting SCT for heterogeneous migrations
❌ Choosing wrong Snow device for data size
❌ Not considering bandwidth for transfer time
❌ Using deprecated SMS (use MGN instead)
❌ Not enabling validation in DMS
❌ Underestimating replication instance size

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Tool for heterogeneous DB migration? __
2. Snowball Edge storage capacity? __
3. Service for NFS to EFS migration? __
4. Can DMS do ongoing replication? __
5. Snowmobile capacity? __
6. What protocol does Transfer Family support? __
7. Storage Gateway type for file storage? __
8. Is SCT needed for MySQL to MySQL? __

---

### Migration Timelines
```
PLANNING PHASE:
├── Discovery (Application Discovery Service)
├── TCO calculation (AWS Pricing Calculator)
├── Migration strategy (6 R's)
└── Proof of concept

6 R'S OF MIGRATION:
├── Rehost (lift-and-shift) - MGN
├── Replatform (lift-tinker-shift) - Some optimization
├── Repurchase (SaaS) - New product
├── Refactor (re-architect) - Cloud-native
├── Retire (turn off) - Decommission
└── Retain (keep on-prem) - Not ready
```

### Application Discovery Service
```
TYPES:
├── Agentless (VMware vCenter)
│   └── VM inventory, config, performance
└── Agent-based (any server)
    └── Detailed dependencies, performance

OUTPUTS:
├── Server inventory
├── Application dependencies
├── Performance data
└── Migration planning data

INTEGRATES WITH:
├── AWS Migration Hub
├── Athena (query data)
└── S3 (export data)
```

## ⏱️ Next Steps
- Time spent: ~40-50 min
- Practice: Understand DMS, Snow device selection
- Ready for: Migration practice questions
- Move to: [Module 11 - Analytics](../11-Analytics/FAST-LEARN.md)

---

**Quick Answers**: 
1) SCT (Schema Conversion Tool) + DMS
2) 80 TB (Storage Optimized)
3) AWS DataSync
4) Yes (CDC - Change Data Capture)
5) 100 PB
6) SFTP, FTPS, FTP
7) File Gateway
8) No (same engine = homogeneous)

