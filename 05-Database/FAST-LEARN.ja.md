# ⚡ Fast Learning - Database Services

> **完了時間**: 60-75 分 | **試験配点**: ~15-20%

## 🎯 必須理解コンセプト（5分）

### Database Service Selector (RANDI-NERD)
```
RELATIONAL SQL? → RDS (managed RDBMS)
NOSQL KEY-VALUE? → DynamoDB
CACHE? → ElastiCache (Redis/Memcached)
DATA WAREHOUSE? → Redshift
GRAPH? → Neptune
IN-MEMORY? → ElastiCache
TIME-SERIES? → Timestream
LEDGER? → QLDB
DOCUMENT? → DocumentDB (MongoDB compatible)
```

**記憶法**: "RDS for Relational, Dynamo for Dynamic data"

## 📊 クイックリファレンステーブル

### RDS Database Engines
| Engine | Type | 最大 Storage | 用途 |
|--------|------|-------------|----------|
| **MySQL** | Open source | 64 TiB | Web apps, general |
| **PostgreSQL** | Open source | 64 TiB | Advanced features |
| **MariaDB** | Open source | 64 TiB | MySQL fork |
| **Oracle** | Commercial | 64 TiB | Enterprise apps |
| **SQL Server** | Commercial | 16 TiB | Microsoft ecosystem |
| **Aurora** | AWS proprietary | 128 TiB | High performance |

### RDS vs Aurora vs DynamoDB
| Feature | RDS | Aurora | DynamoDB |
|---------|-----|--------|----------|
| **Type** | SQL | SQL | なしSQL |
| **AZ** | Single/Multi | Multi (デフォルト) | Multi (デフォルト) |
| **Read Replicas** | Up to 5 | Up to 15 | N/A |
| **Scaling** | Vertical | Vertical + Horizontal | Horizontal (auto) |
| **Performance** | Standard | 5x MySQL, 3x PostgreSQL | Milliseconds |
| **Maintenance** | Some required | Minimal | なしne |
| **Cost** | $$ | $$$ | $ (pay per use) |

## 🔥 試験頻出トピック

### 1. RDS Multi-AZ vs Read Replicas
```
MULTI-AZ (High Availability)
├── Synchronous replication
├── Automatic failover (< 2分)
├── Same region のみ
├── One DNS name (automatic)
├── Standby NOT readable
└── Use: Disaster Recovery, HA

READ REPLICAS (Read Scaling)
├── Asynchronous replication
├── なし automatic failover
├── Cross-region supported
├── Each has own DNS
├── Replicas ARE readable
└── Use: Read-heavy workloads, reporting
```

**記憶法**: Multi-AZ = Availability, Read Replica = Read performance

### 2. Aurora Features (Critical!)
```
AURORA ADVANTAGES
├── 5x faster than MySQL
├── 3x faster than PostgreSQL
├── Up to 15 read replicas
├── Auto-scaling storage (10GB → 128TB)
├── 6 copies across 3 AZs
├── Self-healing storage
├── Automatic failover < 30 seconds
└── Backtrack (point-in-time without restore)

AURORA SERVERLESS
├── Auto-scales compute
├── Pay per second
├── Good for unpredictable workloads
└── Automatic pause when idle
```

### 3. DynamoDB 主要コンセプト
| Concept | Description | 試験のコツ |
|---------|-------------|----------|
| **Partition Key** | Primary key (hash) | Unique identifier |
| **Sort Key** | Optional second key | Range queries |
| **GSI** | グローバル Secondary Index | Query on non-key attributes |
| **LSI** | Local Secondary Index | Same partition key, different sort |
| **Streams** | Change data capture | Trigger Lambda |
| **DAX** | In-memory cache | Microsecond latency |

**Capacity Modes**:
- **Provisioned**: Set RCU/WCU (cheaper if predictable)
- **On-Demand**: Pay per request (unpredictable traffic)

### 4. ElastiCache Quick Comparison
| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data Types** | Complex (lists, sets) | Simple (strings) |
| **Persistence** | Yes (snapshots) | なし |
| **Replication** | Yes (Multi-AZ) | なし |
| **Backup** | Yes | なし |
| **Multi-threaded** | なし | Yes |
| **用途** | Advanced caching | Simple caching |

**記憶法**: "Redis = Rich features, Memcached = Memory のみ"

## 💡 よくある試験シナリオ

### Scenario 1: High Availability for RDS
**質問**: Database must survive AZ failure with minimal downtime
**✅ 正解**: Enable RDS Multi-AZ deployment (automatic failover)

### Scenario 2: Read-Heavy Workload
**質問**: Database experiencing heavy read traffic, writes are normal
**✅ 正解**: Add RDS Read Replicas (up to 5 or 15 for Aurora)

### Scenario 3: グローバル Low-Latency Reads
**質問**: Users worldwide need fast read access to data
**✅ 正解**: DynamoDB グローバル Tables (multi-region, active-active)

### Scenario 4: Reduce Database Load
**質問**: Same queries repeatedly hitting database
**✅ 正解**: ElastiCache (Redis or Memcached) in front of database

### Scenario 5: Unpredictable Database Usage
**質問**: Database usage varies greatly, sometimes idle
**✅ 正解**: Aurora Serverless (auto-scales, pay per second)

### Scenario 6: Point-in-Time Recovery
**質問**: Need to recover database to specific time yesterday
**✅ 正解**: RDS automated backups (retention 1-35 days) + restore

### Scenario 7: なしSQL with Consistent Performance
**質問**: Need single-digit millisecond latency at any scale
**✅ 正解**: DynamoDB (fully managed なしSQL)

### Scenario 8: Data Warehouse for Analytics
**質問**: Run complex queries on petabytes of data
**✅ 正解**: Amazon Redshift (columnar storage, MPP)

## 🎓 速習のコツ

### RDS Backup Types
```
AUTOMATED BACKUPS
├── Daily full backup during maintenance window
├── Transaction logs every 5 分
├── Point-in-time recovery (1-35 days retention)
├── Deleted when RDS instance deleted
└── Free storage = DB size

MANUAL SNAPSHOTS
├── User-initiated
├── Kept indefinitely
├── Can copy to another region
├── NOT deleted when RDS instance deleted
└── Charged for storage
```

### DynamoDB Consistency
```
EVENTUALLY CONSISTENT READS (デフォルト)
├── May not reflect recent write
├── Cheaper (1 RCU = 8 KB)
└── Use: Most use cases

STRONGLY CONSISTENT READS
├── Reflects all successful writes
├── More expensive (1 RCU = 4 KB)
└── Use: When latest data required
```

### RDS Scaling Options
```
VERTICAL SCALING
└── Change instance type
└── Requires downtime (Multi-AZ分imizes)
└── Use: More CPU/RAM needed

HORIZONTAL SCALING (Reads)
└── Add Read Replicas
└── なし downtime
└── Use: Read-heavy workloads

STORAGE SCALING
└── Increase storage size
└── なし downtime
└── Auto-scaling available
```

## 📝 ラピッドファイア事実集

### RDS Important Limits
- **最大 Read Replicas**: 5 (regular RDS), 15 (Aurora)
- **Backup Retention**: 0-35 days (0 = disabled)
- **Multi-AZ**: Automatic failover < 2 分
- **Encryption**: Cannot encrypt existing DB (must create new)
- **Instance Types**: db.t3, db.m5, db.r5, etc.

### DynamoDB Performance
- **Single-digit millisecond** latency
- **DAX**: Microsecond latency (in-memory cache)
- **Partition Key**: Choose high-cardinality (many unique values)
- **Hot Partitions**: Avoid → Distribute access evenly

### Aurora Pricing Components
1. **Storage**: $0.10/GB-month (automatically scales)
2. **I/O Requests**: $0.20/million requests
3. **Backups**: Free up to DB size
4. **Data Transfer**: Standard AWS rates

### Redshift Quick Facts
- **Type**: データウェアハウス (OLAP, not OLTP)
- **Columnar Storage**: Fast for analytics
- **Massively Parallel Processing (MPP)**
- **Petabyte scale**
- **Single-AZ** (not Multi-AZ)
- **Snapshots**: To S3, can copy to other regions

## 🚀 5分マスターレビュー

### Database Decision Tree
```
1. What type of data?
   RELATIONAL (SQL) → Continue to 2
   KEY-VALUE (なしSQL) → DynamoDB
   CACHE → ElastiCache
   ANALYTICS → Redshift
   
2. Need AWS-optimized?
   あり → Aurora (5x MySQL, 3x PostgreSQL)
   NO → RDS (MySQL, PostgreSQL, etc.)
   
3. For ElastiCache, need persistence?
   あり → Redis
   NO → Memcached
   
4. For DynamoDB, predictable traffic?
   あり → Provisioned capacity
   NO → On-Demand capacity
```

### RDS ベストプラクティス
✅ Enable automated backups (1-35 days)
✅ Use Multi-AZ for production
✅ Encrypt databases with sensitive data
✅ Use Read Replicas for read-heavy loads
✅ Monitor with CloudWatch/Performance Insights
✅ Regular maintenance windows
✅ Use IAM database authentication
✅ Enable deletion protection for production

### DynamoDB ベストプラクティス
✅ Choose good partition key (high cardinality)
✅ Use GSI for alternate query patterns
✅ Enable DynamoDB Streams for change tracking
✅ Use DAX for read-heavy, cache-friendly workloads
✅ Enable point-in-time recovery for critical tables
✅ Use on-demand for unpredictable traffic
✅ Enable encryption at rest

### 避けるべきよくあるミス
❌ Using Multi-AZ for read scaling (use Read Replicas)
❌ なしt enabling automated backups
❌ Choosing wrong DynamoDB partition key (hot partitions)
❌ Using Redshift for OLTP (it's for OLAP)
❌ Forgetting Aurora is MySQL/PostgreSQL compatible のみ
❌ なしt using ElastiCache for repeated queries
❌ Thinking Multi-AZ standby is readable (it's not!)
❌ Using provisioned capacity for unpredictable DynamoDB traffic

## 🎯 試験練習スピードラン

**Quick 質問s**（答えは下）

1. 最大 Read Replicas for Aurora? __
2. Is Multi-AZ standby readable? __
3. DynamoDB consistency models? __
4. Which cache supports persistence? __
5. 最大 backup retention for RDS? __
6. Aurora storage scales up to? __
7. What's faster: Redis or DAX for DynamoDB? __
8. Redshift is for OLTP or OLAP? __

---

### RDS Encryption
```
ENCRYPTION AT REST
├── KMS encryption
├── Must enable at creation
├── Cannot encrypt existing (create new from snapshot)
└── Encrypts: data, backups, snapshots, replicas

ENCRYPTION IN TRANSIT
├── SSL/TLS certificates
└── Force with rds.force_ssl parameter
```

### Database Migration Options
| Source | Target | Tool |
|--------|--------|------|
| On-prem DB | RDS | DMS (Database Migration Service) |
| RDS | RDS | Snapshots or DMS |
| Different engines | Any | DMS + SCT (Schema Conversion) |
| Large datasets | RDS | Snowball + DMS |

### Aurora グローバル Database
- **Regions**: Up to 5 secondary regions
- **Latency**: < 1 second cross-region replication
- **Recovery**: < 1分ute RTO
- **Read replicas**: 16 per region
- **用途**: グローバル applications, DR

## ⏱️ 次のステップ
- 学習時間: ~60-75分
- 演習: Create RDS instance, DynamoDB table
- 準備完了: Database practice questions
- 次へ: Module 06 - Networking

---

**Quick 答えs**: 
1) 15
2) なし (のみ in failover)
3) Eventually consistent & Strongly consistent
4) Redis (Memcached does not)
5) 35 days
6) 128 TiB
7) DAX (microseconds vs milliseconds)
8) OLAP (analytics, not transactions)

