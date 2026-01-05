# 05: Database Services - Ultra Fast Learning 🚀

## RDS (Relational Database Service)

### Supported Engines
- PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, **Aurora**

### Key Features
- **Automated backups**: 1-35 days (default 7), PITR
- **Manual snapshots**: Retained forever
- **Multi-AZ**: Synchronous replication, **disaster recovery** (not read scaling)
- **Read Replicas**: Asynchronous, **read scaling**, max **15**
- **Storage Auto Scaling**: Auto-increase when low

### Multi-AZ vs Read Replicas
| Feature | Multi-AZ | Read Replica |
|---------|----------|--------------|
| Purpose | High availability | Read scaling |
| Replication | Synchronous | Asynchronous |
| Failover | Automatic | Manual promotion |
| Same Region | Yes | Can be cross-region |
| Endpoint | Single DNS | Separate DNS |
| Standby Readable | No | Yes |

### RDS Backups
- **Automated**: Daily full + transaction logs every 5 min
- **Deleted with instance** (can retain)
- **Manual snapshots**: User-triggered, kept forever

## Aurora

### Aurora Features
- **AWS proprietary** (MySQL/PostgreSQL compatible)
- **5x MySQL, 3x PostgreSQL** performance
- **Storage**: 10 GB → 128 TB (auto-grows in 10 GB increments)
- **6 copies** across 3 AZs (4/6 write quorum, 3/6 read quorum)
- **Self-healing** (peer-to-peer replication)
- **Auto-failover** <30 seconds
- **15 read replicas** (MySQL has max 5)

### Aurora Endpoints
- **Writer Endpoint**: Points to master (read/write)
- **Reader Endpoint**: Load balancing across read replicas
- **Custom Endpoint**: Subset of instances

### Aurora Serverless
- **Auto-scaling** based on load
- **Pay per second** used
- **Use case**: Infrequent, unpredictable workloads

### Aurora Global Database
- **1 primary region** (read/write)
- **Up to 5 secondary regions** (read-only)
- **<1 second** replication lag
- **RTO <1 minute** for disaster recovery

## DynamoDB

### DynamoDB Basics
- **NoSQL** key-value and document database
- **Single-digit millisecond** latency
- **Serverless**, fully managed
- **Max item size**: 400 KB
- **Auto-scaling** capacity

### Primary Keys
- **Partition Key**: Hash, unique identifier
- **Partition Key + Sort Key**: Composite, flexible queries

### Read/Write Capacity
- **Provisioned**: Set RCU/WCU (cheaper, predictable)
- **On-Demand**: Pay per request (unpredictable workload)
- **1 WCU** = 1 KB/sec write
- **1 RCU** = 4 KB/sec strongly consistent (or 8 KB/sec eventually consistent)

### DynamoDB Features
- **Global Tables**: Multi-region, multi-active, <1 sec replication
- **DynamoDB Streams**: Ordered stream of item changes (24 hr retention)
- **TTL**: Auto-delete expired items
- **DAX**: In-memory cache, microsecond latency
- **Backup**: On-demand or PITR (35 days)

### DynamoDB Indexes
- **Local Secondary Index (LSI)**: Same partition key, different sort key, **max 5**, **must create with table**
- **Global Secondary Index (GSI)**: Different partition/sort key, **max 20**, can create anytime

## ElastiCache

### ElastiCache Engines
- **Redis**: Persistence, backup/restore, multi-AZ, read replicas, pub/sub
- **Memcached**: Simple, multi-threaded, no persistence

### Caching Strategies
- **Lazy Loading**: Cache on read miss (stale data possible)
- **Write-Through**: Write to cache when DB updated (no stale data)
- **TTL**: Add expiration to cache items

### Redis vs Memcached
| Feature | Redis | Memcached |
|---------|-------|-----------|
| Persistence | ✅ | ❌ |
| Backup | ✅ | ❌ |
| Multi-AZ | ✅ | ❌ |
| Read Replicas | ✅ | ❌ |
| Pub/Sub | ✅ | ❌ |
| Multi-threaded | ❌ | ✅ |

## Redshift
- **Data warehouse** (OLAP, analytics)
- **Columnar** storage, parallel query execution
- **Petabyte-scale**
- **Not for OLTP** (use RDS/Aurora)
- **Redshift Spectrum**: Query S3 directly

## DocumentDB
- **MongoDB compatible**
- Fully managed, HA
- Replicates 6 copies across 3 AZs

## Neptune
- **Graph database**
- Social networks, fraud detection
- Knowledge graphs

## QLDB (Quantum Ledger Database)
- **Immutable** ledger
- Cryptographically verifiable
- Financial transactions, supply chain

## Timestream
- **Time-series** database
- IoT, operational metrics

## Quick Exam Tips
- **Multi-AZ**: Disaster recovery, not read scaling
- **Read Replicas**: Read scaling, can be cross-region
- **Aurora**: Best performance, AWS proprietary
- **DynamoDB**: NoSQL, single-digit ms latency
- **ElastiCache**: Sub-millisecond latency
- **Redis**: Advanced features, persistence
- **Memcached**: Simple, multi-threaded
- **Redshift**: Data warehouse, analytics
- **Encryption at rest**: Available for all databases
- **Automated backups**: RDS 1-35 days

