# Database Services - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company needs a relational database with automatic scaling, high availability across multiple AZs, and automatic failover. They want minimal database administration. Which service should be used?

A. Amazon RDS MySQL  
B. Amazon Aurora  
C. Amazon DynamoDB  
D. Amazon Redshift  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon Aurora** provides:
  - MySQL/PostgreSQL compatibility
  - 5x performance of MySQL, 3x of PostgreSQL
  - Automatic scaling (storage up to 128 TB)
  - Multi-AZ by design (6 copies across 3 AZs)
  - Automatic failover (< 30 seconds)
  - Serverless option available

**Aurora vs RDS**:
- **Aurora**: Better performance, auto-scaling storage, faster replication
- **RDS**: Standard MySQL/PostgreSQL, simpler

**Aurora Features**:
- Up to 15 read replicas
- Continuous backup to S3
- Point-in-time recovery
- Backtrack (rewind database)

**References:** Amazon Aurora, RDS vs Aurora
</details>

---

### Question 2
An application requires sub-millisecond latency for read/write operations with automatic scaling to handle millions of requests per second. Which database should be used?

A. Amazon RDS  
B. Amazon DynamoDB  
C. Amazon Aurora  
D. Amazon DocumentDB  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon DynamoDB** is fully managed NoSQL database
  - Single-digit millisecond latency
  - Scales to 10+ trillion requests/day
  - Automatic scaling
  - Multi-AZ replication built-in
  - Serverless option (on-demand pricing)

**DynamoDB Features**:
- Key-value and document database
- DynamoDB Streams (change data capture)
- Global Tables (multi-region replication)
- DynamoDB Accelerator (DAX) for microsecond latency
- Point-in-time recovery
- On-demand and provisioned capacity modes

**When to use DynamoDB**:
- Need extreme scale
- Variable workloads
- Need sub-10ms latency
- Key-value or document data model

**References:** Amazon DynamoDB, NoSQL Databases
</details>

---

### Question 3
A company wants to cache database query results to reduce read load on their RDS database and improve response times. Which service should be used?

A. Amazon CloudFront  
B. Amazon ElastiCache  
C. DynamoDB Accelerator (DAX)  
D. Amazon S3  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon ElastiCache** provides in-memory caching
  - Redis or Memcached engines
  - Microsecond latency
  - Reduces database load
  - Session storage
  - Leaderboards, real-time analytics

**ElastiCache Engines**:

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data Types** | Advanced (strings, sets, sorted sets) | Simple (strings) |
| **Persistence** | Yes (snapshots) | No |
| **Replication** | Yes (Multi-AZ) | No |
| **Pub/Sub** | Yes | No |
| **Sorted Sets** | Yes (leaderboards) | No |
| **Multi-threaded** | No | Yes |

**Common Pattern**: Application → ElastiCache → RDS (cache-aside)

**References:** Amazon ElastiCache, Caching Strategies
</details>

---

### Question 4
A data warehouse requires complex analytical queries across petabytes of data. Which AWS database service is MOST appropriate?

A. Amazon RDS  
B. Amazon DynamoDB  
C. Amazon Redshift  
D. Amazon Aurora  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon Redshift** is data warehouse service
  - Columnar storage
  - Massively parallel processing (MPP)
  - Petabyte-scale
  - SQL queries (PostgreSQL-compatible)
  - Integration with S3, EMR, Glue

**Redshift Features**:
- Columnar storage (better compression, faster queries)
- Redshift Spectrum (query S3 data directly)
- Automatic backups and snapshots
- Encryption at rest and in transit
- Concurrency Scaling (handle burst queries)
- Result caching

**Redshift vs RDS**:
- **Redshift**: Analytics, OLAP, data warehouse
- **RDS**: Transactional, OLTP, operational database

**Use Cases**:
- Business intelligence
- Historical data analysis
- Large-scale analytics
- Reporting

**References:** Amazon Redshift, Data Warehousing
</details>

---

### Question 5
A MongoDB application needs to be migrated to AWS with minimal changes. Which service should be used?

A. Amazon RDS  
B. Amazon DynamoDB  
C. Amazon DocumentDB  
D. Amazon Neptune  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon DocumentDB** is MongoDB-compatible document database
  - Fully managed
  - MongoDB 3.6 and 4.0 compatibility
  - Scales to millions of requests/second
  - Multi-AZ replication
  - Automatic backups

**DocumentDB Features**:
- Document data model (JSON)
- MongoDB drivers and tools compatible
- Storage auto-scales to 64 TB
- Up to 15 read replicas
- Continuous backup to S3

**Migration**: Use AWS Database Migration Service (DMS)

**When to use**:
- Existing MongoDB workloads
- Document-oriented data
- Need managed service

**References:** Amazon DocumentDB, MongoDB on AWS
</details>

---

### Question 6
An application needs to store relationships between data entities (social network connections, fraud detection). Which database is MOST suitable?

A. Amazon RDS  
B. Amazon DynamoDB  
C. Amazon Neptune  
D. Amazon DocumentDB  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon Neptune** is graph database
  - Store and query highly connected data
  - Supports Gremlin and SPARQL
  - Fast relationship queries
  - Multi-AZ replication

**Neptune Use Cases**:
- Social networks
- Fraud detection
- Recommendation engines
- Knowledge graphs
- Network topology
- Supply chain

**Graph vs Relational**:
- **Graph**: Complex relationships, traversals
- **Relational**: Joins become expensive for deep relationships
- Graph databases optimize for relationship queries

**References:** Amazon Neptune, Graph Databases
</details>

---

### Question 7
A company needs to run an RDS database with automatic failover to a standby instance in another AZ. What should be configured?

A. RDS Read Replicas  
B. RDS Multi-AZ Deployment  
C. RDS Snapshots  
D. RDS Cross-Region Replication  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **RDS Multi-AZ** provides high availability
  - Synchronous replication to standby
  - Automatic failover (1-2 minutes)
  - Same region, different AZ
  - No manual intervention

**Multi-AZ vs Read Replicas**:

| Feature | Multi-AZ | Read Replicas |
|---------|----------|---------------|
| **Purpose** | High availability | Read scaling |
| **Replication** | Synchronous | Asynchronous |
| **Failover** | Automatic | Manual promotion |
| **Access** | Standby not accessible | Can read from replicas |
| **Region** | Same | Same or cross-region |

**Multi-AZ Failover Triggers**:
- AZ failure
- Instance failure
- Storage failure
- Software patching (planned)

**References:** RDS Multi-AZ, High Availability
</details>

---

### Question 8
An application requires DynamoDB but needs to support complex queries with multiple attributes. What feature should be used?

A. DynamoDB Streams  
B. DynamoDB Global Secondary Index (GSI)  
C. DynamoDB Auto Scaling  
D. DynamoDB Accelerator (DAX)  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Global Secondary Index (GSI)**:
  - Query on non-primary key attributes
  - Different partition and sort keys than base table
  - Eventually consistent reads
  - Can be added after table creation

**DynamoDB Index Types**:

| Type | Keys | Projection | Creation |
|------|------|------------|----------|
| **LSI** | Same partition key | Can choose | At table creation only |
| **GSI** | Different keys | Can choose | Anytime |

**GSI Use Cases**:
- Query by different attributes
- Support multiple access patterns
- Flexible querying

**Example**:
- Table: Partition Key = UserID
- GSI: Partition Key = Email
- Can now query by email

**References:** DynamoDB Indexes, GSI vs LSI
</details>

---

### Question 9
A company wants to achieve microsecond latency for DynamoDB read operations. Which feature should be enabled?

A. DynamoDB Streams  
B. DynamoDB Global Tables  
C. DynamoDB Accelerator (DAX)  
D. DynamoDB Auto Scaling  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **DynamoDB Accelerator (DAX)**:
  - In-memory cache for DynamoDB
  - Microsecond latency (vs millisecond)
  - Fully managed, highly available
  - No application code changes (drop-in replacement)

**DAX Benefits**:
- 10x performance improvement for read-heavy workloads
- Reduces read load on DynamoDB
- Eventually consistent reads
- Write-through cache

**DAX vs ElastiCache**:
- **DAX**: DynamoDB-specific, easier integration
- **ElastiCache**: General purpose, more control

**When to use DAX**:
- Read-heavy workloads
- Need microsecond latency
- Repeated reads of same items
- Real-time bidding, gaming

**References:** DynamoDB Accelerator (DAX), Caching
</details>

---

### Question 10
An RDS database needs to handle increased read traffic. Write traffic is low. What is the MOST cost-effective solution?

A. Upgrade to larger instance  
B. Enable RDS Multi-AZ  
C. Create RDS Read Replicas  
D. Use ElastiCache  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **RDS Read Replicas**:
  - Asynchronous replication
  - Offload read traffic from primary
  - Up to 15 replicas (Aurora)
  - Same region or cross-region
  - Can be promoted to standalone

**Read Replica Use Cases**:
- Read-heavy workloads
- Reporting/analytics (separate from production)
- Cross-region disaster recovery (promotion)
- Read scaling

**Benefits**:
- Cost-effective scaling for reads
- No impact on primary instance
- Can use different instance types

**Replication Lag**: Monitor with CloudWatch metric

**References:** RDS Read Replicas, Read Scaling
</details>

---

### Question 11
A global application requires DynamoDB tables to be replicated across multiple AWS regions with low-latency local reads and writes. Which feature should be used?

A. DynamoDB Streams  
B. DynamoDB Global Tables  
C. DynamoDB Cross-Region Replication  
D. AWS Database Migration Service  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **DynamoDB Global Tables**:
  - Multi-region, multi-active replication
  - Bi-directional replication
  - Local read/write in each region
  - Sub-second latency
  - Conflict resolution (last writer wins)

**Global Tables Requirements**:
- DynamoDB Streams enabled
- Same table name across regions
- Same primary key structure

**Use Cases**:
- Global applications
- Disaster recovery
- Multi-region high availability
- Reduce latency for global users

**References:** DynamoDB Global Tables, Multi-Region
</details>

---

### Question 12
A company needs to ensure RDS database backups are retained for 90 days for compliance. What should be configured?

A. Automated Backups with 90-day retention  
B. Manual Snapshots  
C. Both automated backups (35 days) and manual snapshots  
D. RDS Cross-Region Replication  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **RDS Automated Backups**: Max 35 days retention
- **Manual Snapshots**: Retained until explicitly deleted
- For > 35 days: Use manual snapshots

**RDS Backup Types**:

| Type | Retention | Deleted with DB | Use Case |
|------|-----------|-----------------|----------|
| **Automated** | 1-35 days | Yes | Point-in-time recovery |
| **Manual** | Until deleted | No | Long-term retention |

**Best Practice for Long Retention**:
1. Enable automated backups (35 days)
2. Create manual snapshots for long-term
3. Use lifecycle policies to copy to S3/Glacier

**Automated Backup Features**:
- Daily full snapshot
- Transaction logs every 5 minutes
- Point-in-time recovery within retention period

**References:** RDS Backups, Backup Retention
</details>

---

### Question 13
An application needs time-series data storage for IoT sensor data with automatic data retention policies. Which database is MOST appropriate?

A. Amazon DynamoDB  
B. Amazon RDS  
C. Amazon Timestream  
D. Amazon Redshift  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon Timestream** is purpose-built for time-series data
  - IoT, DevOps, analytics
  - Automatic data lifecycle management
  - Built-in time-series analytics
  - 1000x faster, 1/10th cost vs relational

**Timestream Features**:
- Automatic tiering (memory → magnetic)
- Built-in time-series functions
- Serverless, auto-scaling
- SQL queries

**Use Cases**:
- IoT sensor data
- Application monitoring
- DevOps metrics
- Industrial telemetry

**Timestream vs Alternatives**:
- **DynamoDB**: General NoSQL, manual TTL
- **Redshift**: Data warehouse, not optimized for time-series
- **Timestream**: Purpose-built, best for time-series

**References:** Amazon Timestream, Time-Series Databases
</details>

---

### Question 14
A company wants to migrate an on-premises Oracle database to AWS with minimal downtime. Which service should be used?

A. AWS Database Migration Service (DMS)  
B. AWS DataSync  
C. AWS Snowball  
D. Manual export/import  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **AWS DMS** (Database Migration Service):
  - Migrate databases with minimal downtime
  - Source database remains operational
  - Supports homogeneous and heterogeneous migrations
  - Continuous data replication

**DMS Migration Types**:
1. **Homogeneous**: Oracle → Oracle, MySQL → Aurora MySQL
2. **Heterogeneous**: Oracle → Aurora PostgreSQL (use SCT)

**DMS Features**:
- Continuous replication
- Multi-AZ for high availability
- Automatic failover
- Supports many database engines

**Migration Steps**:
1. Create replication instance
2. Configure source and target endpoints
3. Create migration task
4. Full load + CDC (Change Data Capture)
5. Cutover when ready

**References:** AWS Database Migration Service, Database Migration
</details>

---

### Question 15
An application uses RDS MySQL. The company wants to encrypt an existing unencrypted database. What is the correct approach?

A. Enable encryption on the existing database  
B. Create encrypted snapshot, restore to new encrypted instance  
C. Use AWS KMS to encrypt in-place  
D. Export data and re-import to encrypted instance  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Cannot encrypt existing RDS instance directly**
- Must create encrypted copy

**Encryption Process**:
1. Create snapshot of unencrypted DB
2. Copy snapshot with encryption enabled
3. Restore encrypted snapshot to new DB instance
4. Update application endpoint
5. Delete old instance

**RDS Encryption**:
- Uses AWS KMS for key management
- Encrypts data at rest (storage, backups, snapshots, read replicas)
- Cannot disable encryption once enabled
- Minimal performance impact

**Alternative**: Use AWS DMS to migrate with encryption enabled

**References:** RDS Encryption, Encrypting Existing Databases
</details>

---

### Question 16
A DynamoDB table experiences variable traffic patterns throughout the day. What capacity mode should be used to optimize costs?

A. Provisioned Capacity  
B. On-Demand Capacity  
C. Reserved Capacity  
D. Auto Scaling  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **On-Demand Capacity**:
  - Pay per request
  - No capacity planning
  - Scales automatically
  - Ideal for unpredictable/variable workloads

**Capacity Modes Comparison**:

| Mode | Best For | Pricing | Scaling |
|------|----------|---------|---------|
| **On-Demand** | Variable traffic | Per request | Automatic |
| **Provisioned** | Predictable traffic | Per hour (RCU/WCU) | Manual or Auto Scaling |

**When to Use**:
- **On-Demand**: New tables, unpredictable, spiky traffic
- **Provisioned**: Predictable, steady traffic, cost optimization

**Cost**: On-Demand can be more expensive for consistent workloads

**Can switch between modes** once per 24 hours

**References:** DynamoDB Capacity Modes, On-Demand vs Provisioned
</details>

---

### Question 17
An application requires ACID transactions across multiple DynamoDB tables. Which feature should be used?

A. DynamoDB Streams  
B. DynamoDB Transactions  
C. DynamoDB Batch Operations  
D. DynamoDB Global Tables  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **DynamoDB Transactions**:
  - ACID properties (Atomicity, Consistency, Isolation, Durability)
  - All-or-nothing operations
  - Up to 100 items or 4 MB per transaction
  - TransactWriteItems and TransactGetItems

**Transaction Use Cases**:
- Financial transactions
- Order processing
- Inventory management
- Need data consistency across items

**Transaction APIs**:
- `TransactWriteItems`: Atomic writes
- `TransactGetItems`: Snapshot reads

**Cost**: 2x the cost of standard reads/writes

**References:** DynamoDB Transactions, ACID Compliance
</details>

---

### Question 18
A company wants to track changes to DynamoDB items in real-time to update materialized views and trigger workflows. Which feature should be used?

A. DynamoDB Auto Scaling  
B. DynamoDB Streams  
C. DynamoDB Backups  
D. CloudWatch Events  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **DynamoDB Streams**:
  - Ordered record of item-level changes
  - Near real-time (typically < 1 second)
  - 24-hour retention
  - Exactly-once delivery

**Stream View Types**:
- **KEYS_ONLY**: Only key attributes
- **NEW_IMAGE**: Entire item after change
- **OLD_IMAGE**: Entire item before change
- **NEW_AND_OLD_IMAGES**: Both before and after

**Use Cases**:
- Update materialized views
- Trigger Lambda functions
- Cross-region replication (Global Tables)
- Data pipelines
- Analytics

**Common Pattern**: DynamoDB Streams → Lambda → Process changes

**References:** DynamoDB Streams, Change Data Capture
</details>

---

### Question 19
An Aurora database cluster needs to handle analytics queries without impacting production traffic. What should be configured?

A. Aurora Read Replicas  
B. Aurora Serverless  
C. Aurora Global Database  
D. RDS Read Replicas  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **Aurora Read Replicas**:
  - Up to 15 replicas
  - Low replication lag (< 10ms)
  - Offload read traffic
  - Can have custom endpoints

**Aurora Custom Endpoints**:
- Direct specific workloads to specific replicas
- Example: Analytics queries to larger instances

**Reader Endpoint**:
- Load balances across all read replicas
- Automatic failover if primary fails

**Aurora Auto Scaling**:
- Automatically add/remove replicas based on load

**References:** Aurora Read Replicas, Aurora Endpoints
</details>

---

### Question 20
A serverless application needs a database that automatically scales capacity based on workload. Which option is MOST suitable?

A. RDS with Auto Scaling  
B. Aurora Serverless  
C. DynamoDB On-Demand  
D. Both B and C  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
Both are suitable for serverless applications:

**Aurora Serverless**:
- Automatically scales compute capacity
- Pay per second for compute
- Ideal for intermittent/unpredictable workloads
- SQL database (PostgreSQL/MySQL)

**DynamoDB On-Demand**:
- Automatically scales throughput
- Pay per request
- NoSQL database
- Sub-10ms latency

**Choose Based On**:
- **Need SQL, relational** → Aurora Serverless
- **Need NoSQL, extreme scale** → DynamoDB On-Demand
- **Intermittent workloads** → Both work
- **Dev/test environments** → Aurora Serverless
- **Serverless apps** → Both work

**References:** Aurora Serverless, DynamoDB On-Demand, Serverless Databases
</details>

---

### Question 21
A development team needs a fully managed, scalable, and highly available Apache Cassandra-compatible database for their application. Which AWS service should they use?

A. Amazon Keyspaces  
B. Amazon DynamoDB  
C. Amazon RDS for PostgreSQL  
D. Amazon Aurora  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon Keyspaces is a managed Cassandra-compatible database
- Supports Cassandra Query Language (CQL)
- DynamoDB is NoSQL but not Cassandra-compatible
- RDS and Aurora are relational databases

**References:** Amazon Keyspaces, Managed Cassandra
</details>

---

### Question 22
A financial institution needs a fully managed, immutable, cryptographically verifiable ledger database for recording transactions. Which AWS service should they use?

A. Amazon QLDB  
B. Amazon Aurora  
C. Amazon RDS  
D. Amazon DynamoDB  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon QLDB (Quantum Ledger Database) is a fully managed ledger database
- Provides immutable, cryptographically verifiable transaction log
- Aurora, RDS, and DynamoDB are not ledger databases

**References:** Amazon QLDB, Ledger Database
</details>

---

## Summary

**Total Questions**: 22  
**Topics Covered**:
- Amazon RDS (Multi-AZ, Read Replicas, Backups, Encryption)
- Amazon Aurora (Features, Read Replicas, Serverless)
- Amazon DynamoDB (Capacity Modes, Indexes, Streams, Transactions, DAX, Global Tables)
- Amazon ElastiCache (Redis vs Memcached)
- Amazon Redshift (Data Warehousing)
- Amazon DocumentDB (MongoDB-compatible)
- Amazon Neptune (Graph Database)
- Amazon Timestream (Time-Series)
- AWS Database Migration Service (DMS)
- Amazon Keyspaces (Cassandra-compatible)
- Amazon QLDB (Ledger Database)

**Exam Tips**:

**Database Selection**:
- **Relational (OLTP)**: RDS, Aurora
- **NoSQL Key-Value**: DynamoDB
- **NoSQL Document**: DocumentDB
- **Graph**: Neptune
- **Data Warehouse (OLAP)**: Redshift
- **Time-Series**: Timestream
- **In-Memory Cache**: ElastiCache

**RDS vs Aurora**:
- **Aurora**: Better performance, auto-scaling, more expensive
- **RDS**: Standard engines, simpler

**High Availability**:
- **RDS Multi-AZ**: Automatic failover, synchronous
- **Read Replicas**: Read scaling, asynchronous

**DynamoDB**:
- **GSI**: Query different attributes, add anytime
- **LSI**: Same partition key, create with table
- **Streams**: Track changes, trigger Lambda
- **Transactions**: ACID compliance
- **DAX**: Microsecond latency cache
- **Global Tables**: Multi-region replication

**ElastiCache**:
- **Redis**: Advanced features, persistence, replication
- **Memcached**: Simple, multi-threaded

**Migration**:
- **AWS DMS**: Minimal downtime migration
- **SCT**: Convert schema for heterogeneous migrations

**Capacity Planning**:
- **Predictable**: Provisioned capacity
- **Variable**: On-Demand or Auto Scaling
- **Intermittent**: Serverless (Aurora Serverless, DynamoDB On-Demand)

**Next Steps**:
- Understand use cases for each database type
- Know when to use Multi-AZ vs Read Replicas
- Memorize DynamoDB features and when to use them
- Practice database selection based on requirements
