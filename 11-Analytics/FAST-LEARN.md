# ⚡ Fast Learning - Analytics Services

> **Time to Complete**: 45-60 minutes | **Exam Weight**: ~8-12%

## 🎯 Must-Know Concepts (5 Minutes)

### Analytics Service Selector (AREKGLQ)
```
QUERY S3 DATA? → Athena (serverless SQL)
DATA WAREHOUSE? → Redshift (petabyte-scale)
ETL? → Glue (serverless ETL)
ELASTICSEARCH? → OpenSearch (search & analytics)
BIG DATA? → EMR (Hadoop, Spark)
REAL-TIME? → Kinesis (streaming analytics)
LAKE? → Lake Formation (data lake)
QUICK VIZ? → QuickSight (BI dashboards)
```

**Memory Aid**: "Athena Asks, Redshift Reduces, EMR Executes, Kinesis Keeps streaming, Glue Glues, Lake Lakes, QuickSight Shows"

## 📊 Quick Reference Tables

### Analytics Services Matrix
| Service | Type | Use Case | Query Language | Serverless |
|---------|------|----------|----------------|------------|
| **Athena** | Interactive query | Ad-hoc SQL on S3 | SQL | ✅ |
| **Redshift** | Data warehouse | OLAP, BI | SQL | ❌ |
| **EMR** | Big data framework | Hadoop/Spark jobs | Various | ❌ |
| **Glue** | ETL | Data transformation | Python/Scala | ✅ |
| **OpenSearch** | Search engine | Search, log analytics | Query DSL | ❌ |
| **QuickSight** | BI tool | Dashboards, visualizations | N/A | ✅ |

### Redshift vs Athena vs RDS
| Feature | Redshift | Athena | RDS |
|---------|----------|--------|-----|
| **Purpose** | Data warehouse (OLAP) | Query S3 | Transactional (OLTP) |
| **Performance** | Very fast | Fast | Fast |
| **Scale** | Petabytes | Exabytes | Terabytes |
| **Cost** | $$$ (provisioned) | $ (pay per query) | $$ |
| **Loading** | Load data first | Query in place | N/A |
| **Query** | SQL | SQL | SQL |

## 🔥 Exam Hot Topics

### 1. Amazon Athena
```
WHAT: Serverless SQL queries on S3
PRICING: $5 per TB scanned
FORMAT: Parquet, ORC, JSON, CSV, Avro

KEY FEATURES:
├── No infrastructure
├── Pay per query (TB scanned)
├── Integrates with Glue Data Catalog
├── JDBC/ODBC drivers
├── Supports partitioning
└── Can query VPC Flow Logs, CloudTrail, ALB logs

OPTIMIZATION:
├── Use columnar formats (Parquet, ORC) - 90% cheaper
├── Compress data (GZIP, Snappy)
├── Partition data (by date, region, etc.)
├── Use larger files (> 128 MB)
└── Limit columns selected (not SELECT *)

COMMON PATTERN:
S3 → Glue Crawler → Glue Catalog → Athena → QuickSight
```

**Exam Tip**: Athena charges by TB scanned, so compression & columnar format = huge savings

### 2. Amazon Redshift
```
ARCHITECTURE:
├── Leader Node (query planning, aggregation)
└── Compute Nodes (query execution, data storage)

NODE TYPES:
├── Dense Compute (dc2): Compute-intensive
└── Dense Storage (ds2): Storage-heavy

KEY FEATURES:
├── Columnar storage (OLAP optimized)
├── Massively Parallel Processing (MPP)
├── Automatic compression
├── Snapshot to S3 (incremental)
├── Enhanced VPC Routing
├── Redshift Spectrum (query S3)
└── Concurrency Scaling (auto)

REDSHIFT SPECTRUM:
├── Query S3 directly without loading
├── Use existing Redshift cluster
├── Scales independently
└── Charged by TB scanned

DISASTER RECOVERY:
├── Snapshots stored in S3 (11 9's durability)
├── Automated snapshots (retention 1-35 days)
├── Manual snapshots (until deleted)
└── Can copy to another region
```

### 3. AWS Glue
```
COMPONENTS:
├── Glue Crawler: Discovers schema
├── Glue Catalog: Metadata repository
├── Glue ETL: Transform data
└── Glue Jobs: Scheduled or triggered

ETL PROCESS:
1. Crawl source data → Populate catalog
2. Define transformation (Python/Scala)
3. Run job (transform data)
4. Load to target (S3, Redshift, etc.)

TRIGGERS:
├── Scheduled (cron)
├── On-demand
└── Event-driven (JobRun completion)

FEATURES:
├── Serverless (auto-scaling)
├── Pay per second (job run time)
├── Data Catalog (shared metadata)
├── Supports Spark & Python
└── BookmarkMemory (tracks processed data)
```

### 4. Amazon EMR (Elastic MapReduce)
```
WHAT: Managed Hadoop framework

FRAMEWORKS SUPPORTED:
├── Hadoop (MapReduce)
├── Spark (in-memory)
├── HBase (NoSQL)
├── Presto (interactive queries)
├── Flink (stream processing)
├── Hive (SQL on Hadoop)
└── 20+ more

CLUSTER TYPES:
├── Transient (temporary, cost-effective)
└── Long-running (persistent)

NODE TYPES:
├── Master Node (manage cluster)
├── Core Nodes (run tasks, HDFS storage)
└── Task Nodes (run tasks only, no storage)

STORAGE OPTIONS:
├── HDFS (on cluster)
├── EMRFS (S3 as HDFS)
└── Local instance store

USE CASES:
├── Big data processing
├── Machine learning
├── Log analysis
└── ETL at scale
```

## 💡 Common Exam Scenarios

### Scenario 1: Query S3 Logs with SQL
**Q**: Analyze CloudTrail logs in S3 using SQL, no infrastructure
**✅ ANSWER**: Amazon Athena

### Scenario 2: Petabyte-Scale Analytics
**Q**: Business intelligence on petabytes of structured data
**✅ ANSWER**: Amazon Redshift (data warehouse)

### Scenario 3: Reduce Athena Costs
**Q**: Athena queries costing too much
**✅ ANSWER**: Convert to Parquet/ORC format, compress, partition data

### Scenario 4: ETL Pipeline
**Q**: Transform CSV data in S3, load to Redshift nightly
**✅ ANSWER**: AWS Glue (serverless ETL with scheduler)

### Scenario 5: Real-Time Log Search
**Q**: Search application logs in real-time, need full-text search
**✅ ANSWER**: Amazon OpenSearch (formerly Elasticsearch)

### Scenario 6: Interactive Dashboards
**Q**: Create business dashboards from Athena/Redshift data
**✅ ANSWER**: Amazon QuickSight

### Scenario 7: Spark Processing
**Q**: Run Apache Spark jobs on large datasets
**✅ ANSWER**: Amazon EMR with Spark

### Scenario 8: Query Both S3 and Redshift
**Q**: Need to join data in S3 with data in Redshift
**✅ ANSWER**: Redshift Spectrum

## 🎓 Speed Learning Tips

### Athena Partitioning
```
WITHOUT PARTITION:
s3://bucket/data/year2024month01day01.csv
s3://bucket/data/year2024month01day02.csv
└── Scans all files (expensive)

WITH PARTITION:
s3://bucket/data/year=2024/month=01/day=01/data.csv
s3://bucket/data/year=2024/month=01/day=02/data.csv
└── Query: WHERE year=2024 AND month=01
└── Scans only relevant partition (cheap!)

PARTITION PROJECTION:
├── No need to run MSCK REPAIR
├── Athena auto-discovers partitions
└── Best for time-based partitions
```

### Redshift Best Practices
✅ Use columnar storage (it's automatic)
✅ Choose appropriate distribution key
✅ Use sort keys for query performance
✅ Enable compression (auto)
✅ Use Redshift Spectrum for S3 data
✅ Regular VACUUM and ANALYZE
✅ Use Concurrency Scaling for bursts
✅ Snapshot for backup/DR

### Glue vs EMR vs Lambda
```
USE GLUE WHEN:
✅ Serverless ETL needed
✅ Simple transformations
✅ Metadata catalog
✅ Python/Scala jobs
✅ Don't want to manage infrastructure

USE EMR WHEN:
✅ Complex big data processing
✅ Need specific Hadoop ecosystem tools
✅ Custom configurations
✅ Cost optimization (Spot instances)
✅ Large-scale ML

USE LAMBDA WHEN:
✅ Simple transformations
✅ < 15 minutes execution
✅ Event-driven processing
✅ Small data volumes
```

## 📝 Rapid-Fire Facts

### Athena Query Optimization
```
COSTS COMPARISON (1 TB data):
├── CSV uncompressed: $5.00
├── CSV compressed (GZIP): $1.25 (75% saving)
├── Parquet uncompressed: $0.50 (90% saving)
└── Parquet compressed: $0.15 (97% saving!)

PERFORMANCE:
├── Columnar (Parquet) = 10x faster
├── Compression = Faster (less data read)
└── Partitioning = Only scan needed data
```

### Redshift Distribution Styles
| Style | When to Use | Example |
|-------|-------------|---------|
| **EVEN** | No clear join patterns | Fact table (default) |
| **KEY** | Frequently joined tables | Join on customer_id |
| **ALL** | Small dimension tables | Broadcast to all nodes |
| **AUTO** | Let Redshift decide | Most cases |

### QuickSight Quick Facts
```
WHAT: Business Intelligence (BI) service
PRICING: Per user/session
USERS: Standard ($9/user), Enterprise ($18/user)

DATA SOURCES:
├── Athena, Redshift, RDS
├── S3
├── SaaS (Salesforce, etc.)
└── On-premises databases

FEATURES:
├── ML Insights (anomaly detection)
├── Embedded analytics
├── SPICE (in-memory, 10 GB free/user)
├── Auto-refresh
└── Mobile apps

SPICE (Super-fast, Parallel, In-memory Calculation Engine):
└── Import data for faster queries
```

### OpenSearch (Elasticsearch) Use Cases
```
PRIMARY USES:
├── Log analytics (ELK stack)
├── Full-text search
├── Application monitoring
├── Security analytics
└── Clickstream analysis

FEATURES:
├── Multi-AZ deployment
├── Automated snapshots to S3
├── Encryption at rest & transit
├── Fine-grained access control
└── Integrated with Kibana

NOT A REPLACEMENT FOR:
❌ Relational database (use RDS)
❌ Data warehouse (use Redshift)
```

## 🚀 5-Minute Master Review

### Analytics Decision Tree
```
1. What's your data source?
   S3 → Athena (query in place)
   Database → Redshift (warehouse)
   
2. What's your use case?
   AD-HOC QUERIES → Athena
   BI/REPORTING → Redshift + QuickSight
   ETL → Glue
   BIG DATA PROCESSING → EMR
   SEARCH → OpenSearch
   STREAMING → Kinesis Analytics
   
3. Need serverless?
   YES → Athena, Glue, QuickSight
   NO → Redshift, EMR, OpenSearch
   
4. Data size?
   < 1 TB → Athena
   TB to PB → Redshift
   PB+ → EMR or Redshift
```

### Common Analytics Patterns
```
1. DATA LAKE PATTERN
   S3 (data lake) → Glue (catalog) → Athena (query) → QuickSight (viz)
   
2. DATA WAREHOUSE PATTERN
   Sources → Glue ETL → Redshift → QuickSight
   
3. LOG ANALYSIS PATTERN
   Logs → Kinesis Firehose → S3 → Athena → OpenSearch
   
4. BIG DATA PROCESSING
   S3 → EMR (Spark) → Process → S3/Redshift
   
5. HYBRID QUERY PATTERN
   Redshift + Redshift Spectrum → Query S3 & Redshift together
```

### Data Formats Comparison
| Format | Type | Compression | Splittable | Athena Performance |
|--------|------|-------------|------------|-------------------|
| **CSV** | Row | Fair | Yes | Slow, expensive |
| **JSON** | Row | Fair | Yes | Slow, expensive |
| **Parquet** | Columnar | Excellent | Yes | ⭐ Best |
| **ORC** | Columnar | Excellent | Yes | ⭐ Best |
| **Avro** | Row | Good | Yes | Good |

### Common Mistakes to Avoid
❌ Using Athena on uncompressed CSV (expensive!)
❌ Not partitioning S3 data for Athena
❌ Using Redshift for OLTP (use RDS)
❌ SELECT * in Athena (scans all columns)
❌ Not using Redshift Spectrum for S3 data
❌ Running EMR long-term for simple ETL (use Glue)
❌ Forgetting to terminate EMR clusters (cost!)
❌ Not using SPICE in QuickSight (slow queries)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. Cheapest way to query S3 data? __
2. Best format for Athena queries? __
3. What type of database is Redshift? __
4. Serverless ETL service? __
5. What is Redshift Spectrum? __
6. Can Athena query compressed data? __
7. Service for Hadoop/Spark? __
8. QuickSight in-memory engine name? __

---

### AWS Lake Formation
```
WHAT: Build secure data lakes
SIMPLIFIES:
├── Data ingestion from multiple sources
├── Data cataloging (uses Glue Catalog)
├── Data transformation
├── Fine-grained access control
└── Security at scale

FEATURES:
├── Blueprints for common sources
├── Column/row-level security
├── Centralized permissions
├── Data deduplication
└── Machine learning transforms

INTEGRATES WITH:
├── Athena, Redshift, EMR
├── QuickSight
└── SageMaker
```

### Kinesis Data Analytics
```
WHAT: Real-time analytics on streaming data
INPUT: Kinesis Data Streams, Kinesis Firehose
QUERY: SQL or Apache Flink

USE CASES:
├── Real-time dashboards
├── Real-time metrics
├── Anomaly detection
└── Time-series analytics

OUTPUTS:
├── Kinesis Data Streams
├── Kinesis Data Firehose
├── Lambda
└── S3 (via Firehose)
```

## ⏱️ Next Steps
- Time spent: ~45-60 min
- Practice: Run Athena query, understand Redshift
- Ready for: Analytics practice questions
- Move to: Module 12 - Architecture Patterns

---

**Quick Answers**: 
1) Athena (pay per query, serverless)
2) Parquet or ORC (columnar, compressed)
3) OLAP / Data Warehouse (not OLTP)
4) AWS Glue
5) Query S3 data from Redshift without loading
6) Yes (saves costs!)
7) Amazon EMR (Elastic MapReduce)
8) SPICE

