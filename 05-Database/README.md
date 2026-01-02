# Module 05: Database Services

## Overview
AWS offers a comprehensive range of database services for different use cases. This module covers relational, NoSQL, caching, and data warehouse services.

## Learning Objectives
- Understand RDS and Aurora features
- Master DynamoDB for NoSQL workloads
- Implement caching with ElastiCache and DAX
- Work with Redshift for analytics
- Choose the right database for your use case

---

## 1. Amazon RDS (Relational Database Service)

### What is RDS?
- **Managed relational database** service
- Automated provisioning, patching, backups, recovery
- Multi-AZ for disaster recovery
- Read Replicas for scalability
- Supports: **PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora**

### RDS Features

**Automated Backups**
- Daily full backup during maintenance window
- Transaction logs backed up every 5 minutes
- Retention: **1 to 35 days** (default 7)
- Point-in-Time Recovery (PITR)
- Backups deleted when you delete RDS instance (can retain)

**Manual Snapshots**
- Manually triggered by user
- Retention: **As long as you want**
- Can copy across regions

**Storage Auto Scaling**
- Automatically increase storage
- Set Maximum Storage Threshold
- Useful for unpredictable workloads

### RDS Multi-AZ (Disaster Recovery)
- **Synchronous replication** to standby in different AZ
- **One DNS name** - automatic failover
- Increase **availability** (not performance)
- Failover in case of:
  - AZ outage
  - Primary DB failure
  - Instance type change
  - OS patching
- **Automatic failover** (60-120 seconds)
- Not used for scaling (use Read Replicas)

### RDS Read Replicas (Scaling Reads)
- **Asynchronous replication** (eventually consistent)
- Up to **15 Read Replicas**
  - Within AZ
  - Cross-AZ
  - Cross-Region
- **Promote to independent database**
- Each replica has **own DNS endpoint**
- Use cases: Reporting, analytics, read-heavy workloads

**Network Cost**:
- **Free** for same-region replicas
- **Charged** for cross-region replication

### RDS Security
- **Encryption at rest**: KMS (must enable at launch)
  - Master encrypted → replicas encrypted
  - Can't encrypt existing unencrypted DB (snapshot → encrypt → restore)
- **Encryption in transit**: SSL/TLS
- **IAM Authentication**: For MySQL and PostgreSQL
- **Security Groups**: Control network access
- **No SSH access** (except RDS Custom)

### RDS Proxy
- Fully managed database proxy
- **Connection pooling** - reduce database load
- **Serverless, auto-scaling**
- Improves database efficiency by reducing stress
- **Reduce failover time by 66%**
- Enforce **IAM authentication**
- Must be accessed from VPC (not public)

### RDS Custom
- For **Oracle and SQL Server**
- Access to underlying OS and database
- Configure settings, install patches
- Deactivate automation to perform customization
- Better to use **EC2** if you need full control

---

## 2. Amazon Aurora

### What is Aurora?
- **AWS proprietary** database (cloud-optimized)
- Compatible with **PostgreSQL and MySQL**
- **5x performance of MySQL**, **3x performance of PostgreSQL**
- Storage auto-scales: **10 GB to 128 TB**
- Up to **15 Read Replicas** (faster replication than RDS)
- **Automatic failover** in less than 30 seconds
- 20% more expensive than RDS

### Aurora High Availability
- **6 copies of data across 3 AZs**:
  - 4/6 copies for writes
  - 3/6 copies for reads
- Self-healing with peer-to-peer replication
- Storage striped across 100s of volumes
- **One master** for writes (failover in 30 sec)
- **Cross-Region Replication** (< 1 second lag)

### Aurora DB Cluster
- **Writer Endpoint**: Points to master (failover)
- **Reader Endpoint**: Load balancing across Read Replicas
- **Custom Endpoints**: Subset of Aurora instances

### Aurora Features

**Aurora Replicas - Auto Scaling**
- Automatically add/remove replicas based on metrics
- Reader Endpoint automatically tracks replicas

**Aurora Custom Endpoints**
- Define subset of instances
- Example: Analytical queries on specific instances

**Aurora Serverless**
- **Automated database instantiation** and auto-scaling
- Pay per second
- Good for **infrequent, intermittent, unpredictable** workloads
- No capacity planning
- Example: Dev/test environments

**Aurora Multi-Master**
- **Continuous write availability**
- Every node performs reads and writes
- Immediate failover (high availability for writes)

**Aurora Global Database**
- **1 primary region** (read/write)
- Up to **5 secondary regions** (read-only)
- Up to **16 Read Replicas per secondary region**
- **< 1 second** replication lag
- **< 1 minute** to promote secondary region (disaster recovery)

**Aurora Machine Learning**
- Integration with **SageMaker** and **Comprehend**
- Predictions using SQL interface
- Use cases: Fraud detection, sentiment analysis, product recommendations

**Aurora Backtrack**
- **Restore to any point in time** without backups
- Available for MySQL-compatible Aurora

---

## 3. Amazon DynamoDB

### What is DynamoDB?
- Fully managed **NoSQL** database
- **Serverless** with auto-scaling
- **Millions of requests/second**
- **Low latency** (single-digit milliseconds)
- **Highly available** (3 AZs)
- **Integrated with IAM**

### DynamoDB Basics

**Tables**
- Collection of items
- **Primary Key** required (decided at creation)
- Infinite number of items (rows)

**Items**
- Similar to rows
- Max size **400 KB**

**Attributes**
- Similar to columns
- Can be nested (up to 32 levels)
- Can be added over time

**Primary Keys**

*Partition Key (HASH)*:
- Must be unique
- Must be diverse (evenly distributed)
- Example: user_id

*Partition Key + Sort Key (HASH + RANGE)*:
- Combination must be unique
- Data grouped by partition key
- Example: user_id + timestamp

### DynamoDB Read/Write Capacity Modes

**Provisioned Mode (default)**
- Specify RCU (Read Capacity Units) and WCU (Write Capacity Units)
- Plan capacity beforehand
- Pay for provisioned capacity
- Auto-scaling available
- **1 RCU** = 1 strongly consistent read/sec (or 2 eventually consistent) for item up to 4 KB
- **1 WCU** = 1 write/sec for item up to 1 KB

**On-Demand Mode**
- Automatically scales
- No capacity planning
- Pay per request (more expensive)
- Good for **unpredictable workloads**
- **2.5x more expensive** than provisioned

### DynamoDB Advanced Features

**DynamoDB Accelerator (DAX)**
- **In-memory cache** for DynamoDB
- **Microsecond latency**
- No application code changes
- 5-minute TTL (default)
- Multi-AZ (3 nodes minimum)
- Solves Hot Key problem

**DynamoDB Streams**
- **Ordered stream of modifications** to table
- Retention: **24 hours**
- Use cases:
  - React to changes in real-time
  - Analytics
  - Insert into derivative tables
  - Cross-region replication
- Can be read by:
  - Lambda (Event Source Mapping)
  - Kinesis Data Streams (newer)

**Global Tables**
- **Multi-region, multi-active** replication
- Active-active replication
- Low latency for global users
- **DynamoDB Streams must be enabled**
- Read and write in any region

**DynamoDB Time To Live (TTL)**
- Automatically delete items after expiry timestamp
- No additional cost
- Use case: Regulatory compliance, reduce storage

**DynamoDB Backups**

*On-Demand Backups*:
- Full backups for long-term retention
- No performance impact
- Restore to new table

*Point-In-Time Recovery (PITR)*:
- Continuous backups for last 35 days
- Restore to any point in time
- Must be enabled

**DynamoDB Indexes**

*Local Secondary Index (LSI)*:
- **Alternative Sort Key**
- Same Partition Key
- Must be created at table creation
- Up to **5 LSIs** per table

*Global Secondary Index (GSI)*:
- **Alternative Partition Key + optional Sort Key**
- Can be created after table creation
- Up to **20 GSIs** per table
- Has own RCU/WCU

### DynamoDB Transactions
- **ACID** transactions
- Coordinated all-or-nothing operations
- **Read Modes**: Eventual, Strong, Transactional
- **Write Modes**: Standard, Transactional
- Consumes 2x RCU/WCU

### DynamoDB Security
- VPC Endpoints
- IAM policies for access control
- Encryption at rest (KMS) and in transit (SSL/TLS)
- Point-in-time recovery
- Global tables
- DynamoDB Streams integration with Lambda

---

## 4. Amazon ElastiCache

### What is ElastiCache?
- Managed **in-memory database**
- **Redis** or **Memcached**
- High performance, low latency
- Reduce load on databases for read-intensive workloads
- Make application **stateless**

### Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data Types** | Advanced (Sets, Sorted Sets, Lists) | Simple (Strings) |
| **Replication** | Multi-AZ with failover | Multi-node (sharding) |
| **Persistence** | Snapshots, AOF | No persistence |
| **Backup/Restore** | Yes | No |
| **Transactions** | Yes | No |
| **Pub/Sub** | Yes | No |
| **Lua Scripts** | Yes | No |
| **Geospatial** | Yes | No |
| **Multi-threaded** | No | Yes |

### ElastiCache Strategies

**Lazy Loading / Cache-Aside**
1. Application checks cache
2. If miss, read from database
3. Write to cache
- Pros: Only requested data cached
- Cons: Cache miss penalty, stale data

**Write Through**
1. Application writes to database
2. Also writes to cache
- Pros: Data never stale
- Cons: Write penalty, unnecessary data cached

**Time To Live (TTL)**
- Add expiration to cached data
- Balance between staleness and cache misses

### Redis Specific Features

**Redis Sorted Sets**
- Leaderboards, ranking
- Real-time updates

**Redis Replication**
- **Cluster Mode Disabled**:
  - One primary, up to 5 replicas
  - Asynchronous replication
  - Multi-AZ for automatic failover
- **Cluster Mode Enabled**:
  - Data partitioned across shards
  - Up to 500 nodes per cluster
  - Better write scalability

---

## 5. Amazon Redshift

### What is Redshift?
- **Data warehouse** (OLAP - Online Analytical Processing)
- **Columnar storage**
- Massively Parallel Query Execution (MPP)
- **Faster than Athena** for complex queries
- Pay per node provisioned
- Integrated with BI tools (Tableau, PowerBI, QuickSight)

### Redshift Architecture
- **Leader Node**: Query planning, result aggregation
- **Compute Nodes**: Execute queries, send results to leader
- **Node Types**:
  - Dense Compute (dc2): High performance
  - Dense Storage (ds2): Large datasets
  - RA3: Managed storage, separate compute and storage

### Redshift Spectrum
- Query data in **S3 without loading**
- Massively parallel processing
- Use existing Redshift cluster
- Support for structured and unstructured data

### Redshift Features

**Snapshots**
- Point-in-time backups
- Automated: Every 8 hours or 5 GB
- Retention: 1-35 days
- Manual snapshots: Retained until deleted
- Can copy to another region

**Redshift Enhanced VPC Routing**
- Forces all traffic through VPC
- Better security and monitoring

**Concurrency Scaling**
- Automatically add capacity for burst of queries
- Pay per second for additional clusters

**Workload Management (WLM)**
- Prioritize queries
- Queue management

---

## 6. Amazon DocumentDB

### What is DocumentDB?
- **MongoDB-compatible** document database
- Fully managed
- Storage auto-scales to 64 TB
- **3 AZ replication**
- Millions of requests/second
- Similar to Aurora for MongoDB

---

## 7. Amazon Neptune

### What is Neptune?
- Fully managed **graph database**
- Store billions of relations
- Query graph with millisecond latency
- **Multi-AZ**, Read Replicas
- Use cases:
  - Social networking
  - Knowledge graphs
  - Fraud detection
  - Recommendation engines

---

## 8. Amazon Keyspaces

### What is Keyspaces?
- **Apache Cassandra**-compatible database
- Serverless
- Auto-scaling
- Tables replicate 3 times across multiple AZs
- CQL (Cassandra Query Language)

---

## 9. Amazon QLDB (Quantum Ledger Database)

### What is QLDB?
- **Ledger database**
- **Immutable** system of record
- Cryptographically verifiable
- Track all changes over time
- **Central authority** (not decentralized like blockchain)
- Use cases: Financial transactions, supply chain, legal records

---

## 10. Amazon Timestream

### What is Timestream?
- **Time series database**
- Serverless, auto-scaling
- Store and analyze trillions of events/day
- 1000x faster, 1/10th cost vs relational databases
- Built-in analytics functions
- Use cases: IoT, operational applications, real-time analytics

---

## Database Comparison

| Database | Type | Use Case |
|----------|------|----------|
| **RDS** | Relational (SQL) | OLTP, traditional applications |
| **Aurora** | Relational (SQL) | Cloud-native, high performance |
| **DynamoDB** | NoSQL (Key-Value) | Serverless, low latency, mobile/web |
| **ElastiCache** | In-Memory | Caching, session storage |
| **Redshift** | Data Warehouse | OLAP, analytics, BI |
| **DocumentDB** | NoSQL (Document) | MongoDB workloads |
| **Neptune** | Graph | Social networks, fraud detection |
| **Keyspaces** | NoSQL (Wide Column) | Cassandra workloads |
| **QLDB** | Ledger | Immutable, verifiable history |
| **Timestream** | Time Series | IoT, metrics, events |

---

## Practice Questions

1. **Which database service provides automatic failover in less than 30 seconds?**
   - A. RDS MySQL
   - B. Aurora
   - C. DynamoDB
   - D. Redshift
   
   **Answer**: B

2. **What is the maximum retention period for automated RDS backups?**
   - A. 7 days
   - B. 30 days
   - C. 35 days
   - D. 90 days
   
   **Answer**: C

3. **Which DynamoDB feature provides microsecond latency?**
   - A. DynamoDB Streams
   - B. Global Tables
   - C. DAX
   - D. PITR
   
   **Answer**: C

4. **Which AWS service is best for caching with persistence and backup capabilities?**
   - A. ElastiCache for Memcached
   - B. ElastiCache for Redis
   - C. DynamoDB
   - D. RDS
   
   **Answer**: B

---

## Hands-On Labs

### Lab 1: RDS Multi-AZ
1. Create RDS MySQL instance with Multi-AZ
2. Connect and create sample database
3. Enable automated backups
4. Create manual snapshot
5. Restore from snapshot

### Lab 2: Aurora Read Replicas
1. Create Aurora cluster
2. Add Read Replicas
3. Connect to writer and reader endpoints
4. Test load balancing

### Lab 3: DynamoDB
1. Create DynamoDB table
2. Add items using console
3. Create GSI
4. Query using partition key and GSI
5. Enable DynamoDB Streams

### Lab 4: ElastiCache
1. Create ElastiCache Redis cluster
2. Configure security group
3. Connect from EC2 instance
4. Test set/get operations
5. Monitor with CloudWatch

---

## Key Takeaways

✅ RDS Multi-AZ is for disaster recovery (synchronous), Read Replicas for scaling (asynchronous)  
✅ Aurora is 5x faster than MySQL, auto-scales storage, up to 15 Read Replicas  
✅ DynamoDB is serverless NoSQL with DAX for microsecond latency  
✅ ElastiCache Redis supports persistence and replication, Memcached is simpler  
✅ Redshift is for data warehousing (OLAP), not OLTP  
✅ Use RDS Proxy to reduce database connection overhead  
✅ DynamoDB Global Tables for multi-region active-active replication  
✅ Aurora Global Database has < 1 second replication lag  
✅ Choose database based on: Relational vs NoSQL, OLTP vs OLAP, latency requirements  
✅ RDS automated backups are deleted when instance is deleted (unless retained)  

---

## Additional Resources

- [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/)
- [Amazon Aurora Documentation](https://docs.aws.amazon.com/aurora/)
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [Amazon ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/)
- [Database Comparison Guide](https://aws.amazon.com/products/databases/)

---

**Previous Module**: [Module 04: Storage Services](../04-Storage/README.md)  
**Next Module**: [Module 06: Networking & Content Delivery](../06-Networking/README.md)

