# ⚡ Fast Learning - Storage Services

> **完了時間**: 60-75 分 | **試験配点**: ~15-20%

## 🎯 必須理解コンセプト（5分）

### Storage Service Selector (The SEFI Rule)
```
OBJECT STORAGE? → S3 (files, static content)
BLOCK STORAGE? → EBS (databases, OS)
FILE STORAGE? → EFS/FSx (shared file systems)
ARCHIVAL? → S3 Glacier (long-term backup)
```

**記憶法**: "SEF-I store data" = S3, EBS, EFS/FSx, Ice (Glacier)

## 📊 クイックリファレンステーブル

### S3 Storage Classes (試験最重要!)
| Class | Retrieval | Availability | Min Duration | 用途 | Cost |
|-------|-----------|--------------|--------------|----------|------|
| **Standard** | Instant | 99.99% | なしne | Frequently accessed | $$$$ |
| **Intelligent-Tiering** | Instant | 99.9% | 30 days | Unknown access | $$$ |
| **Standard-IA** | Instant | 99.9% | 30 days | Infrequent access | $$ |
| **One Zone-IA** | Instant | 99.5% | 30 days | なしn-critical, infrequent | $ |
| **Glacier Instant** | Instant | 99.9% | 90 days | Archive, instant access | $ |
| **Glacier 柔軟** | Min-Hours | 99.99% | 90 days | Archive, rare access | $ |
| **Glacier Deep** | 12 hours | 99.99% | 180 days | Long-term archive | $ |

**記憶法**: "SISO-GGG" = Standard, Intelligent, Standard-IA, One Zone-IA, Glacier x3

### EBS Volume Types (GISP)
| Type | Name | IOPS | Throughput | 用途 | Boot? |
|------|------|------|------------|----------|-------|
| **gp3** | General SSD | 16,000 | 1,000 MB/s | Most workloads | ✅ |
| **gp2** | General SSD | 16,000 | 250 MB/s | 旧世代 general | ✅ |
| **io2** | Provisioned SSD | 64,000+ | 1,000 MB/s | Mission-critical DB | ✅ |
| **io1** | Provisioned SSD | 64,000 | 1,000 MB/s | 旧世代 high perf | ✅ |
| **st1** | Throughput HDD | 500 | 500 MB/s | Big data, logs | ❌ |
| **sc1** | Cold HDD | 250 | 250 MB/s | Infrequent access | ❌ |

**記憶法**: "GP = General 目的, IO = Input/Output intensive, ST = Streaming Throughput, SC = Slow/Cold"

## 🔥 試験頻出トピック

### 1. S3 Features 早見表
| Feature | 目的 | Exam Scenario |
|---------|---------|---------------|
| **Versioning** | Keep all versions | Protect from deletion |
| **Encryption** | Secure data | Compliance requirements |
| **MFA Delete** | Require MFA to delete | Critical data protection |
| **Lifecycle Rules** | Auto-transition/delete | Cost optimization |
| **Replication** | Copy to another bucket | DR, compliance |
| **Transfer Acceleration** | Fast global uploads | Worldwide users |
| **Static Hosting** | Host Websites | Simple static sites |

### 2. S3 Encryption Options (SSEC)
```
SSE-S3 (AWS-managed keys)
└── AWS manages everything
└── AES-256 encryption
└── デフォルト option

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

**記憶法**: SSE-S3 = Simple, SSE-KMS = Key control, SSE-C = Customer keys, Client = Complete control

### 3. EBS vs EFS vs Instance Store
| Feature | EBS | EFS | Instance Store |
|---------|-----|-----|----------------|
| **Type** | Block | File | Block |
| **Attach** | One instance* | Many instances | One instance |
| **AZ** | Single AZ | Multi-AZ | Single AZ |
| **Persist** | Yes | Yes | NO (ephemeral) |
| **Performance** | High | Shared | Very High |
| **用途** | DB, boot | Shared files | Cache, temp |

*Multi-attach available for io1/io2 in same AZ

**記憶法**: "BEI" = Block (EBS), Everyone shares (EFS), Instance-ephemeral (Instance Store)

### 4. S3 Consistency Model
```
✅ STRONG READ-AFTER-WRITE CONSISTENCY
└── PUT new object → Immediately readable
└── DELETE object → Immediately gone
└── UPDATE object → Immediately reflects new version

ALL OPERATIONS: Consistent since Dec 2020
```

## 💡 よくある試験シナリオ

### Scenario 1: コスト最適化 for Old Data
**質問**: Data accessed frequently first 30 days, rarely after 90 days
**✅ 正解**: Lifecycle policy: Standard → Standard-IA (30 days) → Glacier (90 days)

### Scenario 2: Protect Critical S3 Data
**質問**: Prevent accidental deletion of critical files
**✅ 正解**: Enable versioning + MFA Delete + Bucket policy with explicit deny

### Scenario 3: Share Files Across EC2 Instances
**質問**: Multiple EC2 instances need read/write to same files
**✅ 正解**: EFS (not EBS - のみ mounts to one instance)

### Scenario 4: Database Volume Performance
**質問**: Database needs 50,000 IOPS
**✅ 正解**: io2 EBS volume (up to 64,000+ IOPS)

### Scenario 5: Fast グローバル Uploads to S3
**質問**: Users worldwide uploading to S3, need speed
**✅ 正解**: S3 Transfer Acceleration

### Scenario 6: Compliance - Keep 7 Years
**質問**: Regulatory requirement to store 7 years, rarely accessed
**✅ 正解**: S3 Glacier Deep Archive (cheapest for long-term)

### Scenario 7: Temporary High-Speed Storage
**質問**: EC2 needs very fast temporary storage for processing
**✅ 正解**: Instance Store (ephemeral, fastest)

## 🎓 速習のコツ

### S3 Bucket Naming Rules
- 3-63 characters
- Lowercase のみ
- なし uppercase, no underscores
- Must start with letter or number
- グローバルly unique

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

## 📝 ラピッドファイア事実集

### S3 Limits
- 最大 object size: **5 TB**
- Single PUT: **5 GB**
- Multi-part upload: Required for > **5 GB**, recommended for > **100 MB**
- 最大 parts: **10,000**
- Part size: **5 MB to 5 GB**

### EBS Facts
- Single AZ のみ (can snapshot → restore to different AZ)
- Can detach/reattach (except boot volumes)
- Can resize on the fly
- Snapshots stored in S3 (multi-AZ)
- Can encrypt existing unencrypted volume via snapshot

### EFS Features
- Multi-AZ by デフォルト
- Auto-scales (no provisioning)
- Pay for what you use
- NFSv4.1 protocol
- Linux のみ
- Thousands of concurrent connections

### FSx Quick Comparison
| Type | OS | Protocol | 用途 |
|------|-----|----------|----------|
| **FSx for Windows** | Windows | SMB | Windows apps, AD |
| **FSx for Lustre** | Linux | Lustre | HPC, ML, big data |
| **FSx for NetApp ONTAP** | Any | NFS/SMB | Multi-protocol |
| **FSx for OpenZFS** | Linux | NFS | Linux workloads |

## 🚀 5分マスターレビュー

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

### 避けるべきよくあるミス
❌ Using EBS for shared storage (use EFS)
❌ Forgetting EBS is single AZ
❌ なしt using lifecycle policies for cost savings
❌ Choosing wrong S3 storage class
❌ Forgetting to enable versioning before replication
❌ Using Standard for infrequently accessed data
❌ Instance Store for persistent data (it's ephemeral!)
❌ なしt encrypting sensitive data

## 🎯 試験練習スピードラン

**Quick 質問s**（答えは下）

1. 最大 S3 object size? __
2. Which EBS type for 50,000 IOPS? __
3. Does EFS work with Windows? __
4. S3 storage class for unknown access patterns? __
5. Can EBS attach to multiple instances? __
6. What protocol does EFS use? __
7. Where are EBS snapshots stored? __
8. Minimum storage duration for Glacier Deep Archive? __

---

### S3 Pre-signed URLs
- **目的**: Temporary access to private objects
- **Validity**: Configurable (seconds to days)
- **用途**: Download private files, upload to bucket
- **Example**: Share file for 1 hour without making public

### S3 Event なしtifications
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

## 🔒 S3 Security レイヤーs
```
1. IAM Policies (user/role permissions)
2. Bucket Policies (resource-based)
3. ACLs (legacy, not recommended)
4. Encryption (at rest)
5. SSL/TLS (in transit)
6. VPC Endpoints (private access)
7. Block Public Access (account level)
```

## ⏱️ 次のステップ
- 学習時間: ~60-75分
- 演習: Create S3 bucket, lifecycle rules, EBS volume
- 準備完了: Storage practice questions
- 次へ: Module 05 - Database

---

**Quick 答えs**: 
1) 5 TB
2) io2 or io1 (Provisioned IOPS SSD)
3) なし (Linux のみ)
4) S3 Intelligent-Tiering
5) なし (except io1/io2 multi-attach in same AZ)
6) NFSv4.1
7) S3 (managed by AWS)
8) 180 days

