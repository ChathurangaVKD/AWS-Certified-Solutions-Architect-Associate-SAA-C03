# ⚡ Fast Learning - Storage Services

> **Time to Complete**: 60-75 minutes | **Exam Weight**: ~15-20%

## 🎯 Must-Know Concepts (5 Minutes)

### Storage Service Selector (The SEFI Rule)
```
OBJECT STORAGE? → S3 (files, static content)
BLOCK STORAGE? → EBS (databases, OS)
FILE STORAGE? → EFS/FSx (shared file systems)
ARCHIVAL? → S3 Glacier (long-term backup)
```

**Memory Aid**: "SEF-I store data" = S3, EBS, EFS/FSx, Ice (Glacier)

## 📊 Quick Reference Tables

### S3 Storage Classes (Critical for Exam!)
| Class | Retrieval | Availability | Min Duration | Use Case | Cost |
|-------|-----------|--------------|--------------|----------|------|
| **Standard** | Instant | 99.99% | None | Frequently accessed | $$$$ |
| **Intelligent-Tiering** | Instant | 99.9% | 30 days | Unknown access | $$$ |
| **Standard-IA** | Instant | 99.9% | 30 days | Infrequent access | $$ |
| **One Zone-IA** | Instant | 99.5% | 30 days | Non-critical, infrequent | $ |
| **Glacier Instant** | Instant | 99.9% | 90 days | Archive, instant access | $ |
| **Glacier Flexible** | Min-Hours | 99.99% | 90 days | Archive, rare access | $ |
| **Glacier Deep** | 12 hours | 99.99% | 180 days | Long-term archive | $ |

**Memory Aid**: "SISO-GGG" = Standard, Intelligent, Standard-IA, One Zone-IA, Glacier x3

### EBS Volume Types (GISP)
| Type | Name | IOPS | Throughput | Use Case | Boot? |
|------|------|------|------------|----------|-------|
| **gp3** | General SSD | 16,000 | 1,000 MB/s | Most workloads | ✅ |
| **gp2** | General SSD | 16,000 | 250 MB/s | Legacy general | ✅ |
| **io2** | Provisioned SSD | 64,000+ | 1,000 MB/s | Mission-critical DB | ✅ |
| **io1** | Provisioned SSD | 64,000 | 1,000 MB/s | Legacy high perf | ✅ |
| **st1** | Throughput HDD | 500 | 500 MB/s | Big data, logs | ❌ |
| **sc1** | Cold HDD | 250 | 250 MB/s | Infrequent access | ❌ |

**Memory Aid**: "GP = General Purpose, IO = Input/Output intensive, ST = Streaming Throughput, SC = Slow/Cold"

## 🔥 Exam Hot Topics

### 1. S3 Features Quick Matrix
| Feature | Purpose | Exam Scenario |
|---------|---------|---------------|
| **Versioning** | Keep all versions | Protect from deletion |
| **Encryption** | Secure data | Compliance requirements |
| **MFA Delete** | Require MFA to delete | Critical data protection |
| **Lifecycle Rules** | Auto-transition/delete | Cost optimization |
| **Replication** | Copy to another bucket | DR, compliance |
| **Transfer Acceleration** | Fast global uploads | Worldwide users |
| **Static Hosting** | Host websites | Simple static sites |

### 2. S3 Encryption Options (SSEC)
```
SSE-S3 (AWS-managed keys)
└── AWS manages everything
└── AES-256 encryption
└── Default option

SSE-KMS (KMS-managed keys)
└── More control, audit trail
└── CloudTrail logs key usage
└── Can set key policies

SSE-C (Customer-provided keys)
└── You manage keys
└── AWS encrypts/decrypts
└── Keys sent with each request

Client-Side Encryption
└── Encrypt before upload
└── You manage everything
```

**Memory Aid**: SSE-S3 = Simple, SSE-KMS = Key control, SSE-C = Customer keys, Client = Complete control

### 3. EBS vs EFS vs Instance Store
| Feature | EBS | EFS | Instance Store |
|---------|-----|-----|----------------|
| **Type** | Block | File | Block |
| **Attach** | One instance* | Many instances | One instance |
| **AZ** | Single AZ | Multi-AZ | Single AZ |
| **Persist** | Yes | Yes | NO (ephemeral) |
| **Performance** | High | Shared | Very High |
| **Use Case** | DB, boot | Shared files | Cache, temp |

*Multi-attach available for io1/io2 in same AZ

**Memory Aid**: "BEI" = Block (EBS), Everyone shares (EFS), Instance-ephemeral (Instance Store)

### 4. S3 Consistency Model
```
✅ STRONG READ-AFTER-WRITE CONSISTENCY
└── PUT new object → Immediately readable
└── DELETE object → Immediately gone
└── UPDATE object → Immediately reflects new version

ALL OPERATIONS: Consistent since Dec 2020
```

## 💡 Common Exam Scenarios

### Scenario 1: Cost Optimization for Old Data
**Q**: Data accessed frequently first 30 days, rarely after 90 days
**✅ ANSWER**: Lifecycle policy: Standard → Standard-IA (30 days) → Glacier (90 days)

### Scenario 2: Protect Critical S3 Data
**Q**: Prevent accidental deletion of critical files
**✅ ANSWER**: Enable versioning + MFA Delete + Bucket policy with explicit deny

### Scenario 3: Share Files Across EC2 Instances
**Q**: Multiple EC2 instances need read/write to same files
**✅ ANSWER**: EFS (not EBS - only mounts to one instance)

### Scenario 4: Database Volume Performance
**Q**: Database needs 50,000 IOPS
**✅ ANSWER**: io2 EBS volume (up to 64,000+ IOPS)

### Scenario 5: Fast Global Uploads to S3
**Q**: Users worldwide uploading to S3, need speed
**✅ ANSWER**: S3 Transfer Acceleration

### Scenario 6: Compliance - Keep 7 Years
**Q**: Regulatory requirement to store 7 years, rarely accessed
**✅ ANSWER**: S3 Glacier Deep Archive (cheapest for long-term)

### Scenario 7: Temporary High-Speed Storage
**Q**: EC2 needs very fast temporary storage for processing
**✅ ANSWER**: Instance Store (ephemeral, fastest)

## 🎓 Speed Learning Tips

### S3 Bucket Naming Rules
- 3-63 characters
- Lowercase only
- No uppercase, no underscores
- Must start with letter or number
- Globally unique

### S3 Object Key = Full Path
```
Bucket: my-bucket
Key: folder/subfolder/file.txt
URL: https://my-bucket.s3.amazonaws.com/folder/subfolder/file.txt
```

### EBS Snapshot Facts
- Incremental backups
- Stored in S3 (managed by AWS)
- Can copy across regions
- Can create AMI from snapshot
- Can encrypt during copy
- First snapshot = full, rest = incremental

### S3 Replication Types
```
CRR (Cross-Region Replication)
└── Different regions
└── Compliance, lower latency
└── Disaster recovery

SRR (Same-Region Replication)
└── Same region
└── Log aggregation
└── Prod/test sync
```

**Requirements**: Versioning enabled on both buckets

## 📝 Rapid-Fire Facts

### S3 Limits
- Max object size: **5 TB**
- Single PUT: **5 GB**
- Multi-part upload: Required for > **5 GB**, recommended for > **100 MB**
- Max parts: **10,000**
- Part size: **5 MB to 5 GB**

### EBS Facts
- Single AZ only (can snapshot → restore to different AZ)
- Can detach/reattach (except boot volumes)
- Can resize on the fly
- Snapshots stored in S3 (multi-AZ)
- Can encrypt existing unencrypted volume via snapshot

### EFS Features
- Multi-AZ by default
- Auto-scales (no provisioning)
- Pay for what you use
- NFSv4.1 protocol
- Linux only
- Thousands of concurrent connections

### FSx Quick Comparison
| Type | OS | Protocol | Use Case |
|------|-----|----------|----------|
| **FSx for Windows** | Windows | SMB | Windows apps, AD |
| **FSx for Lustre** | Linux | Lustre | HPC, ML, big data |
| **FSx for NetApp ONTAP** | Any | NFS/SMB | Multi-protocol |
| **FSx for OpenZFS** | Linux | NFS | Linux workloads |

## 🚀 5-Minute Master Review

### Storage Decision Tree
```
1. What type of data?
   OBJECTS (files, images) → S3
   BLOCKS (OS, DB) → EBS or Instance Store
   FILES (shared) → EFS or FSx
   
2. For S3, how often accessed?
   FREQUENT → S3 Standard
   INFREQUENT → Standard-IA
   ARCHIVE → Glacier
   UNKNOWN → Intelligent-Tiering
   
3. For EBS, what performance?
   GENERAL → gp3
   HIGH IOPS → io2
   THROUGHPUT → st1
   COLD → sc1
   
4. For File Storage, what OS?
   LINUX → EFS
   WINDOWS → FSx for Windows
   HPC → FSx for Lustre
```

### S3 Lifecycle Rules Examples
```
Transition:
Standard → Standard-IA (30 days)
Standard-IA → Glacier (90 days)
Glacier → Deep Archive (180 days)

Expiration:
Delete objects after 365 days
Delete incomplete multipart uploads after 7 days
```

### Common Mistakes to Avoid
❌ Using EBS for shared storage (use EFS)
❌ Forgetting EBS is single AZ
❌ Not using lifecycle policies for cost savings
❌ Choosing wrong S3 storage class
❌ Forgetting to enable versioning before replication
❌ Using Standard for infrequently accessed data
❌ Instance Store for persistent data (it's ephemeral!)
❌ Not encrypting sensitive data

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Max S3 object size? __
2. Which EBS type for 50,000 IOPS? __
3. Does EFS work with Windows? __
4. S3 storage class for unknown access patterns? __
5. Can EBS attach to multiple instances? __
6. What protocol does EFS use? __
7. Where are EBS snapshots stored? __
8. Minimum storage duration for Glacier Deep Archive? __

---

### S3 Pre-signed URLs
- **Purpose**: Temporary access to private objects
- **Validity**: Configurable (seconds to days)
- **Use Case**: Download private files, upload to bucket
- **Example**: Share file for 1 hour without making public

### S3 Event Notifications
**Triggers**:
- Object created (PUT, POST, COPY)
- Object removed (DELETE)
- Object restored (from Glacier)
- Replication events

**Targets**:
- Lambda functions
- SQS queues
- SNS topics
- EventBridge

## 🔒 S3 Security Layers
```
1. IAM Policies (user/role permissions)
2. Bucket Policies (resource-based)
3. ACLs (legacy, not recommended)
4. Encryption (at rest)
5. SSL/TLS (in transit)
6. VPC Endpoints (private access)
7. Block Public Access (account level)
```

## ⏱️ Next Steps
- Time spent: ~60-75 min
- Practice: Create S3 bucket, lifecycle rules, EBS volume
- Ready for: Storage practice questions
- Move to: Module 05 - Database

---

**Quick Answers**: 
1) 5 TB
2) io2 or io1 (Provisioned IOPS SSD)
3) No (Linux only)
4) S3 Intelligent-Tiering
5) No (except io1/io2 multi-attach in same AZ)
6) NFSv4.1
7) S3 (managed by AWS)
8) 180 days

