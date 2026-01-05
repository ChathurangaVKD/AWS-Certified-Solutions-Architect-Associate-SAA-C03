# 11: Analytics Services - Ultra Fast Learning 🚀

## Amazon Athena
- **Serverless** SQL queries on S3
- **Pay per query**: $5 per TB scanned
- **No infrastructure** to manage
- **ANSI SQL** (uses Presto engine)
- **Formats**: CSV, JSON, Parquet, ORC, Avro

### Athena Performance
- **Partition data**: Reduce scan (`/year/month/day`)
- **Columnar formats**: Parquet, ORC (huge savings)
- **Compress data**: gzip, snappy, zstd
- **Larger files**: Combine small files (>128 MB optimal)
- **Federated queries**: Query across data sources (Lambda)

### Athena Use Cases
- Ad-hoc analysis, log analysis
- Query S3 data without ETL
- BI tools integration (QuickSight)

## Amazon Kinesis

### Kinesis Data Streams
- **Real-time** streaming data
- **Retention**: 1-365 days
- **Shards**: Provision throughput
  - **Write**: 1 MB/s or 1,000 records/s per shard
  - **Read**: 2 MB/s per shard
- **Consumers**: Lambda, KCL, Kinesis Data Analytics
- **Replay**: Re-process data

### Kinesis Data Firehose
- **Near real-time** (60 sec buffer minimum)
- **Load to**: S3, Redshift, OpenSearch, Splunk, HTTP endpoints
- **Auto-scaling** (no shards)
- **Transformations**: Lambda
- **Compression**: GZIP, Snappy, Zip
- **Pay per GB** ingested

### Kinesis Data Analytics
- **Real-time SQL** queries on streaming data
- **Input**: Kinesis Streams or Firehose
- **Output**: Kinesis Streams, Firehose, Lambda
- **Use case**: Real-time dashboards, metrics, alerts

### Kinesis Video Streams
- **Stream video** from devices
- **Use case**: Computer vision, ML, video playback

## EMR (Elastic MapReduce)
- **Big data processing** (Hadoop, Spark, HBase, Presto, Flink)
- **Cluster**: Master, core, task nodes
- **Storage**: HDFS, EMRFS (S3), instance store
- **Spot instances**: Save cost on task nodes
- **Use case**: Big data, ML, genomics, log analysis

### EMR Node Types
- **Master**: Manage cluster, coordinate tasks
- **Core**: Run tasks, store HDFS data
- **Task**: Run tasks only (optional), use Spot

## AWS Glue
- **Serverless ETL** (Extract, Transform, Load)
- **Glue Data Catalog**: Metadata repository (tables, schemas)
- **Glue Crawler**: Auto-discover schema
- **Glue Jobs**: ETL scripts (Spark/Python)
- **Integration**: Athena, Redshift, EMR

### Glue Components
- **Data Catalog**: Central metadata repository
- **Crawlers**: Discover data and populate catalog
- **ETL Jobs**: Transform data
- **Triggers**: Schedule or event-driven
- **Development Endpoints**: Test ETL scripts

### Glue Use Cases
- Prepare data for analytics
- Migrate databases
- Build data lake
- Data discovery

## Amazon Redshift
- **Data warehouse** (OLAP, analytics)
- **Columnar** storage, parallel queries
- **Petabyte-scale**
- **Not for OLTP** (use RDS/Aurora)
- **Cluster**: Leader node + compute nodes

### Redshift Features
- **Compression**: Auto-compression
- **Massively Parallel Processing (MPP)**
- **Result caching**: Fast repeated queries
- **Backup**: Automated (1-35 days), manual snapshots
- **Redshift Spectrum**: Query S3 directly (no load)

### Redshift Pricing
- **On-Demand**: Pay per hour
- **Reserved**: 1-3 years (up to 75% discount)

## QuickSight
- **Serverless BI** (Business Intelligence)
- **Visualizations**, dashboards, ad-hoc analysis
- **Auto-scaling**, pay per session
- **Data sources**: Redshift, RDS, Aurora, Athena, S3, on-premises
- **SPICE engine**: In-memory calculation (fast)
- **ML Insights**: Anomaly detection, forecasting

## Amazon OpenSearch (Elasticsearch)
- **Search and analytics** engine
- **Use cases**: Log analytics, full-text search, real-time app monitoring
- **Managed service**: Previously called Elasticsearch Service
- **Kibana**: Visualization (included)
- **Integration**: Kinesis Firehose, Lambda, CloudWatch Logs

## AWS Data Pipeline
- **Legacy** (use Glue or Step Functions)
- Orchestrate data movement and transformation
- **On-premises + AWS** data sources

## AWS Lake Formation
- **Build data lakes** easily
- **Centralized permissions** (fine-grained access control)
- **Built on Glue**: Uses Glue Data Catalog
- **Features**: Data ingestion, cataloging, transformation, security

## MSK (Managed Streaming for Apache Kafka)
- **Managed Apache Kafka** service
- **Alternative to Kinesis**
- **Use case**: Existing Kafka workloads, need full Kafka features

### MSK vs Kinesis
| Feature | MSK | Kinesis |
|---------|-----|---------|
| Management | More control | Fully managed |
| Compatibility | Apache Kafka | AWS proprietary |
| Use case | Kafka migration | New AWS apps |
| Cost | Generally cheaper | Pay for shards |

## AWS Batch
- **Batch processing** at any scale
- **Dynamically provisions** EC2 or Spot
- **Jobs**: Units of work (Docker containers)
- **Job queues**: Priority-based
- **Use case**: Image processing, genomics, financial modeling

## Quick Exam Tips
- **Athena**: Serverless SQL on S3, $5/TB
- **Kinesis Streams**: Real-time, shards, 1-365 days retention
- **Kinesis Firehose**: Near real-time, load to S3/Redshift, no shards
- **EMR**: Hadoop/Spark, big data processing
- **Glue**: Serverless ETL, Data Catalog
- **Redshift**: Data warehouse, OLAP, columnar
- **Redshift Spectrum**: Query S3 without loading
- **QuickSight**: Serverless BI, SPICE engine
- **OpenSearch**: Search, log analytics, Kibana
- **Lake Formation**: Build data lakes, centralized permissions
- **MSK**: Managed Kafka (migrate existing workloads)
- **AWS Batch**: Batch jobs, EC2/Spot provisioning
- **Use Parquet/ORC**: Reduce Athena costs significantly

