# Module 11: Analytics Services

## Overview
AWS provides a comprehensive suite of analytics services for collecting, processing, analyzing, and visualizing data at any scale. This module covers key analytics services essential for the Solutions Architect certification.

## Learning Objectives
- Query data in S3 using Amazon Athena
- Process streaming data with Amazon Kinesis
- Run big data frameworks with Amazon EMR
- Build ETL pipelines with AWS Glue
- Create visualizations with Amazon QuickSight
- Understand data lake architecture on AWS

---

## 1. Amazon Athena

### What is Amazon Athena?
- **Serverless interactive query service**
- Query data in S3 using standard SQL
- Pay per query (amount of data scanned)
- No infrastructure to manage
- Integrated with AWS Glue Data Catalog

### Key Features
- **Serverless**: No servers to provision or manage
- **Pay-per-Query**: Charged based on data scanned ($5 per TB)
- **Standard SQL**: ANSI SQL compliant (uses Presto)
- **Fast**: Interactive query performance
- **Versatile**: Query structured, semi-structured, and unstructured data

### Athena Architecture

```
┌────────────────────────────────────────────────────────────┐
│                     Amazon Athena                          │
│                                                            │
│  ┌──────────────┐         ┌─────────────────────────┐    │
│  │   SQL Query  │────────►│   Query Engine (Presto)  │    │
│  └──────────────┘         └─────────────────────────┘    │
│                                    │                       │
└────────────────────────────────────┼───────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
              ┌─────▼──────┐                   ┌─────▼──────┐
              │   AWS      │                   │  Amazon S3 │
              │   Glue     │                   │   Data     │
              │  Catalog   │                   │   Buckets  │
              └────────────┘                   └────────────┘
```

### Supported Data Formats
- **CSV**
- **JSON**
- **Apache Parquet** ⭐ (Columnar, best performance)
- **Apache ORC** ⭐ (Columnar, optimized)
- **Apache Avro**
- **TSV**
- **Text files with custom delimiters**

### Creating Tables in Athena

**Using DDL (Data Definition Language):**
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sales (
  sale_id INT,
  product_name STRING,
  sale_date DATE,
  amount DOUBLE,
  region STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://my-bucket/sales-data/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

**Using AWS Glue Crawler:**
- Automatically discovers schema
- Creates tables in Glue Data Catalog
- Athena queries use Glue Catalog

### Query Examples

**Basic SELECT:**
```sql
SELECT region, SUM(amount) as total_sales
FROM sales
WHERE sale_date >= DATE '2024-01-01'
GROUP BY region
ORDER BY total_sales DESC;
```

**Partitioned Data Query:**
```sql
SELECT *
FROM sales
WHERE year='2024' AND month='01'
LIMIT 100;
```

**Join Multiple Tables:**
```sql
SELECT s.product_name, p.category, SUM(s.amount) as revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY s.product_name, p.category;
```

### Partitioning for Performance

**Why Partition?**
- Reduce data scanned per query
- Lower costs (pay per TB scanned)
- Faster query performance

**Partition Strategy:**
```
s3://my-bucket/sales-data/
  ├── year=2024/
  │   ├── month=01/
  │   │   ├── day=01/
  │   │   │   └── data.parquet
  │   │   └── day=02/
  │   │       └── data.parquet
  │   └── month=02/
  │       └── day=01/
  │           └── data.parquet
```

**Create Partitioned Table:**
```sql
CREATE EXTERNAL TABLE sales_partitioned (
  sale_id INT,
  product_name STRING,
  amount DOUBLE
)
PARTITIONED BY (year STRING, month STRING, day STRING)
STORED AS PARQUET
LOCATION 's3://my-bucket/sales-data/';
```

**Add Partitions:**
```sql
-- Add single partition
ALTER TABLE sales_partitioned 
ADD PARTITION (year='2024', month='01', day='01')
LOCATION 's3://my-bucket/sales-data/year=2024/month=01/day=01/';

-- Or use MSCK REPAIR to auto-discover partitions
MSCK REPAIR TABLE sales_partitioned;
```

### Performance Optimization

**1. Use Columnar Formats:**
- Parquet or ORC instead of CSV/JSON
- 30-90% less data scanned
- Better compression

**2. Compress Data:**
- Gzip, Snappy, or LZO compression
- Reduce storage and scan costs

**3. Partition Data:**
- Organize by commonly queried fields
- year, month, day, region, etc.

**4. Optimize File Sizes:**
- Target 128 MB - 1 GB per file
- Avoid many small files

**5. Use Column Projection:**
```sql
-- Good: Select only needed columns
SELECT product_name, amount FROM sales;

-- Bad: Select all columns
SELECT * FROM sales;
```

**6. Filter Early:**
```sql
-- Use WHERE clause to limit data scanned
SELECT * FROM sales 
WHERE year='2024' AND month='01';
```

### Athena Workgroups
- **Isolate queries and costs** per team/project
- Set data usage limits and thresholds
- Enforce query result encryption
- Track query metrics per workgroup

**Create Workgroup:**
- Specify S3 output location
- Enable query result encryption
- Set data scanned limits
- Configure CloudWatch metrics

### Query Result Storage
- Results stored in S3 bucket
- Specify output location per workgroup
- Can be encrypted (SSE-S3, SSE-KMS)
- Automatically retained for 45 days (configurable)

### Integration with AWS Glue
- **Glue Data Catalog**: Centralized metadata repository
- **Glue Crawlers**: Automatically discover schema
- **Glue ETL**: Prepare data for Athena queries

### Use Cases
1. **Ad-hoc querying**: Business intelligence, log analysis
2. **Data Lake analytics**: Query data in S3 data lake
3. **Log analysis**: VPC Flow Logs, CloudTrail logs, ALB logs
4. **Business reporting**: Generate reports from S3 data
5. **Cost analysis**: Query AWS Cost and Usage Reports

### Pricing
- **$5.00 per TB of data scanned**
- No charge for DDL statements (CREATE, ALTER, DROP)
- Reduced cost with compression and columnar formats
- Cancelled queries charged based on data scanned

### Exam Tips
✅ **Serverless and SQL-based**: No infrastructure, standard SQL queries

✅ **Pay per TB scanned**: Optimize with partitioning, compression, columnar formats

✅ **S3 data source**: Queries data directly in S3

✅ **Integration with Glue**: Use Glue Catalog for metadata

✅ **Supported formats**: CSV, JSON, Parquet, ORC, Avro

---

## 2. Amazon Kinesis

### What is Amazon Kinesis?
- **Real-time data streaming platform**
- Collect, process, and analyze streaming data
- Scalable and durable
- Multiple services for different use cases

### Kinesis Services Overview

| Service | Purpose | Use Case |
|---------|---------|----------|
| **Kinesis Data Streams** | Real-time data streaming | Custom processing applications |
| **Kinesis Data Firehose** | Load streaming data into AWS | Easy delivery to S3, Redshift, OpenSearch |
| **Kinesis Data Analytics** | Real-time analytics with SQL | Real-time dashboards, metrics |
| **Kinesis Video Streams** | Stream video data | Video analytics, ML |

---

### 2.1 Amazon Kinesis Data Streams

**What is it?**
- **Real-time data streaming service**
- Capture and store streaming data
- Build custom processing applications
- Durable, scalable, and elastic

**Architecture:**
```
┌──────────────┐         ┌─────────────────────┐         ┌──────────────┐
│  Producers   │────────►│  Kinesis Data       │────────►│  Consumers   │
│              │         │  Stream (Shards)    │         │              │
│ - Apps       │         │                     │         │ - Lambda     │
│ - IoT        │         │  Shard 1 │ Shard 2 │         │ - EC2        │
│ - Logs       │         │  Shard 3 │ Shard 4 │         │ - KCL Apps   │
└──────────────┘         └─────────────────────┘         └──────────────┘
```

**Key Concepts:**

**Shards:**
- Basic unit of capacity
- Each shard provides:
  - **Write**: 1 MB/sec or 1,000 records/sec
  - **Read**: 2 MB/sec or 5 transactions/sec (with GetRecords)
- Scale by adding/removing shards

**Records:**
- Data blob (up to 1 MB)
- Partition key (determines shard)
- Sequence number (unique identifier)

**Retention:**
- Default: 24 hours
- Can extend to 365 days (at additional cost)

**Producers (Data Sources):**
- AWS SDK
- Kinesis Producer Library (KPL)
- Kinesis Agent
- CloudWatch Logs
- IoT devices
- Third-party libraries

**Consumers (Data Processing):**
- AWS Lambda
- Kinesis Data Analytics
- Kinesis Data Firehose
- EC2 instances with KCL (Kinesis Client Library)
- Custom applications

**Partition Keys:**
- Determines which shard receives the record
- Same partition key → same shard (ordering)
- Use high-cardinality keys to distribute load

**Capacity Modes:**

**Provisioned Mode:**
- Manually manage shard count
- Predictable cost
- Pay per shard-hour

**On-Demand Mode:**
- Automatic scaling
- Pay per GB of data in/out
- Good for unpredictable workloads

**Use Cases:**
- Real-time log and event processing
- IoT data ingestion
- Clickstream analysis
- Real-time metrics and monitoring

---

### 2.2 Amazon Kinesis Data Firehose

**What is it?**
- **Fully managed service to load streaming data**
- No code required
- Automatic scaling
- Near real-time delivery (60 seconds latency minimum)

**Architecture:**
```
┌──────────────┐       ┌────────────────────┐       ┌─────────────────┐
│  Producers   │──────►│ Kinesis Firehose   │──────►│  Destinations   │
│              │       │                    │       │                 │
│ - Apps       │       │ - Transform (opt)  │       │ - S3            │
│ - IoT        │       │ - Buffer           │       │ - Redshift      │
│ - Logs       │       │ - Compress         │       │ - OpenSearch    │
│ - Kinesis    │       │ - Encrypt          │       │ - Splunk        │
└──────────────┘       └────────────────────┘       │ - HTTP endpoint │
                                                     └─────────────────┘
```

**Key Features:**

**Automatic Scaling:**
- No capacity provisioning
- Scales automatically with throughput

**Data Transformation:**
- Use Lambda to transform data before delivery
- Format conversion (JSON to Parquet/ORC)
- Enrichment, filtering

**Buffering:**
- Buffer size: 1 MB - 128 MB
- Buffer interval: 60 - 900 seconds
- Delivers when either threshold is met

**Compression:**
- GZIP, ZIP, Snappy, or Hadoop-compatible Snappy
- Reduces storage costs

**Supported Destinations:**
- **Amazon S3**
- **Amazon Redshift** (via S3 COPY)
- **Amazon OpenSearch Service**
- **Splunk**
- **HTTP endpoints**
- **Third-party services** (Datadog, New Relic, MongoDB)

**Data Transformation Example:**
```python
import base64
import json

def lambda_handler(event, context):
    output = []
    for record in event['records']:
        # Decode data
        payload = base64.b64decode(record['data'])
        data = json.loads(payload)
        
        # Transform data
        transformed = {
            'timestamp': data['timestamp'],
            'value': data['value'] * 2  # Example transformation
        }
        
        # Encode result
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(transformed).encode())
        }
        output.append(output_record)
    
    return {'records': output}
```

**Firehose vs Data Streams:**

| Feature | Data Streams | Firehose |
|---------|-------------|----------|
| **Complexity** | More control, custom code | Fully managed, no code |
| **Latency** | Real-time (70-200 ms) | Near real-time (60s min) |
| **Scaling** | Manual or on-demand | Automatic |
| **Retention** | 24 hours - 365 days | No retention |
| **Consumers** | Custom applications | Predefined destinations |
| **Cost** | Per shard-hour | Per GB ingested |

**Use Cases:**
- Stream data to S3 data lakes
- Load data into Redshift or OpenSearch
- Send logs to Splunk
- Transform and deliver streaming data

---

### 2.3 Amazon Kinesis Data Analytics

**What is it?**
- **Real-time analytics on streaming data**
- Use SQL or Apache Flink
- Serverless, automatic scaling
- Analyze data from Kinesis Data Streams or Firehose

**Architecture:**
```
┌─────────────────┐      ┌──────────────────────┐      ┌──────────────┐
│  Input Stream   │─────►│  Kinesis Analytics   │─────►│   Output     │
│                 │      │                      │      │              │
│ - Data Streams  │      │  - SQL Queries       │      │ - Lambda     │
│ - Firehose      │      │  - Flink Apps        │      │ - S3         │
│                 │      │  - Windowing         │      │ - Kinesis    │
└─────────────────┘      └──────────────────────┘      │ - Firehose   │
                                                        └──────────────┘
```

**Two Engines:**

**1. SQL Applications:**
- Use standard SQL to query streaming data
- Windowing functions (tumbling, sliding, session)
- Aggregations, filtering, joins
- Easy to use for simple analytics

**2. Apache Flink Applications:**
- Advanced stream processing
- Java or Scala code
- Stateful computations
- Complex event processing

**SQL Example:**
```sql
-- Create input stream
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
    ticker_symbol VARCHAR(4),
    avg_price DOUBLE,
    event_time TIMESTAMP
);

-- Compute average price per ticker in 1-minute windows
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM 
    ticker_symbol,
    AVG(price) AS avg_price,
    ROWTIME AS event_time
FROM "SOURCE_SQL_STREAM_001"
GROUP BY 
    ticker_symbol,
    STEP("SOURCE_SQL_STREAM_001".ROWTIME BY INTERVAL '1' MINUTE);
```

**Windowing Concepts:**

**Tumbling Window:**
- Fixed size, non-overlapping
- Example: 1-minute windows

**Sliding Window:**
- Fixed size, overlapping
- Example: 1-minute window, slides every 30 seconds

**Session Window:**
- Variable size based on activity
- Gaps in activity create new windows

**Use Cases:**
- Real-time dashboards
- Real-time metrics and KPIs
- Real-time anomaly detection
- Live leaderboards (gaming)
- Real-time ETL

---

### 2.4 Amazon Kinesis Video Streams

**What is it?**
- **Capture, process, and store video streams**
- Securely ingest video from millions of devices
- Machine learning and video processing

**Use Cases:**
- Smart home security cameras
- Industrial automation
- Computer vision applications
- ML-powered video analytics

---

## 3. Amazon EMR (Elastic MapReduce)

### What is Amazon EMR?
- **Managed Hadoop framework**
- Process vast amounts of data
- Run big data frameworks (Spark, Hadoop, HBase, Presto, Flink)
- Cost-effective and scalable

### Key Features
- **Managed Cluster**: Automatic provisioning and configuration
- **Scalable**: Add/remove instances dynamically
- **Flexible**: Run on EC2, EKS, or Outposts
- **Cost-Effective**: Use Spot Instances for task nodes
- **Integrated**: Works with S3, DynamoDB, Redshift

### EMR Architecture

```
┌──────────────────────────────────────────────────────┐
│                   EMR Cluster                        │
│                                                      │
│  ┌────────────────┐                                 │
│  │  Master Node   │  (Manage cluster, YARN)         │
│  └────────────────┘                                 │
│          │                                           │
│  ┌───────┴────────┐                                 │
│  │                │                                  │
│  ▼                ▼                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   Core   │  │   Core   │  │   Core   │          │
│  │   Node   │  │   Node   │  │   Node   │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│  (HDFS + Compute)                                   │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   Task   │  │   Task   │  │   Task   │          │
│  │   Node   │  │   Node   │  │   Node   │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│  (Compute only - optional)                          │
└──────────────────────────────────────────────────────┘
```

### Node Types

**Master Node:**
- Manages the cluster
- Coordinates distribution of data and tasks
- Tracks status of tasks
- Monitors cluster health
- **Critical**: Single point of failure (use multi-master for HA)

**Core Nodes:**
- Run tasks and store data in HDFS
- Can be scaled up (not down easily)
- Both compute and storage

**Task Nodes (Optional):**
- Run tasks only (no HDFS)
- Can be added/removed for extra capacity
- Perfect for Spot Instances
- Cost optimization

### Supported Frameworks

**Apache Spark:**
- Fast in-memory processing
- Batch and streaming
- SQL, ML, Graph processing

**Apache Hadoop:**
- MapReduce for batch processing
- HDFS for distributed storage

**Apache HBase:**
- NoSQL database
- Real-time read/write access

**Presto:**
- Distributed SQL query engine
- Interactive queries

**Apache Flink:**
- Stream processing
- Real-time analytics

**Apache Hive:**
- Data warehouse
- SQL-like queries

**Others:**
- Pig, Hue, Zeppelin, Livy, Sqoop, Oozie

### Storage Options

**HDFS (Hadoop Distributed File System):**
- Distributed across Core nodes
- High throughput
- Data lost if cluster terminates

**EMRFS:**
- EMR File System
- Access S3 as if it were HDFS
- Data persists after cluster termination
- **Recommended for most use cases**

**Local File System:**
- Instance store volumes
- Temporary storage

### Cluster Types

**Transient Clusters:**
- Short-lived (hours to days)
- Terminate after job completion
- Save costs
- Data stored in S3

**Long-Running Clusters:**
- Weeks, months, or years
- Interactive workloads
- Real-time processing
- Higher costs

### Instance Types

**Master Node:**
- m5.xlarge (general purpose)
- Not compute-intensive

**Core Nodes:**
- r5 (memory-optimized) for Spark
- m5 (general purpose) for balanced workloads

**Task Nodes:**
- Spot Instances for cost savings
- Same instance type as Core nodes

### Purchasing Options

**On-Demand Instances:**
- Predictable cost
- No interruptions
- Use for Master and Core nodes

**Reserved Instances:**
- Long-running clusters
- Up to 75% discount
- 1 or 3-year commitment

**Spot Instances:**
- Up to 90% discount
- Can be interrupted
- **Best practice**: Use for Task nodes only
- Spot Block: 1-6 hours without interruption

### Auto Scaling
- Add/remove instances based on metrics
- Scale Core or Task nodes
- Custom scaling policies
- Based on YARN metrics (ContainerPending, YARNMemoryAvailablePercentage)

### EMR Security

**Encryption:**
- At rest: S3, EBS, local disk
- In transit: TLS between nodes

**IAM Roles:**
- EMR service role
- EC2 instance profile
- Auto Scaling role

**Security Groups:**
- Master, Core, and Task node security groups
- Control inbound/outbound traffic

**Kerberos:**
- Strong authentication
- Enterprise integration

**Lake Formation Integration:**
- Fine-grained access control
- Column-level security

### EMR Notebooks
- Jupyter notebook interface
- Interactive development
- Works with Spark clusters
- Stored in S3

### EMR Studio
- Integrated development environment (IDE)
- Build, visualize, debug applications
- Collaborative workspace

### Use Cases
1. **Log processing and analysis**
2. **Clickstream analysis**
3. **Machine learning**
4. **Genomics data processing**
5. **Financial risk modeling**
6. **ETL pipelines**

### Pricing
- **EC2 instance costs** (On-Demand, Reserved, Spot)
- **EMR cost**: Additional charge per instance hour
- **Data transfer**: Standard rates

### Exam Tips
✅ **Managed Hadoop**: Use EMR for big data frameworks (Spark, Hadoop)

✅ **Node types**: Master (manage), Core (HDFS + compute), Task (compute only)

✅ **Spot Instances**: Use for Task nodes to reduce costs

✅ **EMRFS**: Store data in S3 for persistence

✅ **Transient clusters**: Terminate after job completion to save costs

---

## 4. AWS Glue

### What is AWS Glue?
- **Serverless ETL service**
- Discover, prepare, and transform data
- Data catalog for metadata management
- No infrastructure to manage

### Key Features
- **Serverless**: No servers to provision
- **Data Catalog**: Centralized metadata repository
- **Crawlers**: Automatically discover schemas
- **ETL Jobs**: Transform data using Spark or Python
- **Visual ETL**: Drag-and-drop interface (AWS Glue Studio)

### AWS Glue Architecture

```
┌────────────────────────────────────────────────────────────┐
│                      AWS Glue                              │
│                                                            │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────────┐  │
│  │   Crawler   │───►│     Data     │◄───│  ETL Jobs   │  │
│  │             │    │   Catalog    │    │             │  │
│  └─────────────┘    └──────────────┘    └─────────────┘  │
│         │                   │                   │          │
└─────────┼───────────────────┼───────────────────┼──────────┘
          │                   │                   │
          ▼                   ▼                   ▼
   ┌────────────┐      ┌──────────┐       ┌──────────┐
   │  Data      │      │  Query   │       │  Output  │
   │  Sources   │      │  Tools   │       │  Data    │
   │  (S3, RDS) │      │ (Athena) │       │  (S3)    │
   └────────────┘      └──────────┘       └──────────┘
```

### Components

**1. AWS Glue Data Catalog:**
- Centralized metadata repository
- Stores table definitions, schemas, locations
- Used by Athena, EMR, Redshift Spectrum
- Versioned schemas
- Compatible with Apache Hive Metastore

**2. AWS Glue Crawlers:**
- Automatically discover data
- Infer schemas
- Create/update tables in Data Catalog
- Schedule crawlers to run periodically

**3. AWS Glue ETL Jobs:**
- Transform data using Spark or Python
- Generate code or write custom scripts
- Built-in transformations
- Job bookmarks (track processed data)

**4. AWS Glue Studio:**
- Visual interface for creating ETL jobs
- Drag-and-drop transformations
- No code required

**5. AWS Glue DataBrew:**
- Visual data preparation tool
- Clean and normalize data
- 250+ pre-built transformations

### Data Catalog

**Purpose:**
- Store metadata about data sources
- Table definitions, schemas, partitions
- Shared across AWS analytics services

**Catalog Structure:**
```
Database
  ├── Table 1
  │   ├── Schema
  │   ├── Location (S3)
  │   ├── Format (Parquet, CSV, JSON)
  │   └── Partitions
  └── Table 2
      ├── Schema
      ├── Location (S3)
      └── Format
```

**Populating the Catalog:**
1. **Crawlers**: Automatically discover and catalog
2. **Manual**: Define tables using AWS Console or API
3. **ETL Jobs**: Create tables as output

### Glue Crawlers

**What Crawlers Do:**
- Connect to data store (S3, RDS, DynamoDB, JDBC)
- Determine schema
- Create or update tables in Data Catalog
- Detect partitions

**Crawler Configuration:**
- **Data source**: S3 path, database connection
- **IAM role**: Permissions to access data
- **Schedule**: Run on-demand or scheduled
- **Output database**: Where to store tables

**Example:**
```
Data Source: s3://my-bucket/sales-data/
Crawler discovers:
  - Format: Parquet
  - Schema: sale_id, product, amount, date
  - Partitions: year, month
  
Creates table: sales_data in database: analytics_db
```

### Glue ETL Jobs

**Types of Jobs:**

**1. Spark Jobs:**
- Scala or Python (PySpark)
- Distributed processing
- Large datasets

**2. Python Shell Jobs:**
- Pure Python scripts
- Smaller datasets
- Simple transformations

**Job Components:**
- **Data source**: From Data Catalog or direct S3
- **Transformations**: Map, filter, join, aggregate
- **Data target**: S3, database, Data Catalog

**Sample PySpark Script:**
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "analytics_db",
    table_name = "sales_data"
)

# Transform
filtered = Filter.apply(frame = datasource, 
                       f = lambda x: x["amount"] > 100)

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = filtered,
    connection_type = "s3",
    connection_options = {"path": "s3://output-bucket/filtered-sales/"},
    format = "parquet"
)

job.commit()
```

**Built-in Transformations:**
- **ApplyMapping**: Rename/drop fields
- **Filter**: Filter records
- **Join**: Join datasets
- **DropFields**: Remove columns
- **SelectFields**: Keep specific columns
- **SplitFields**: Split into multiple frames
- **Relationalize**: Flatten nested data

### Job Bookmarks
- Track data that has already been processed
- Prevent duplicate processing
- State information preserved between runs
- Useful for incremental ETL

### Development Endpoints
- Test and debug ETL scripts
- Interactive development
- Connect with notebooks (Zeppelin, Jupyter)

### Glue DataBrew
- **Visual data preparation**
- Profile data quality
- 250+ transformations
- No code data cleaning

**Use Cases:**
- Remove duplicates
- Fill missing values
- Normalize data formats
- Filter outliers

### Glue Triggers
- **Automate job execution**
- Schedule-based or event-based
- On-demand, scheduled, or conditional
- Chain multiple jobs together

**Trigger Types:**
- **Scheduled**: Cron expression
- **On-demand**: Manual trigger
- **Conditional**: Based on job completion

### Workflow Example
```
Crawler (S3) → Trigger → ETL Job 1 → Trigger → ETL Job 2 → Trigger → Crawler (Output)
```

### Glue vs EMR

| Feature | AWS Glue | Amazon EMR |
|---------|----------|------------|
| **Management** | Fully serverless | Managed clusters |
| **Use Case** | ETL, data catalog | Big data frameworks |
| **Scaling** | Automatic | Manual or auto-scaling |
| **Cost** | Pay per DPU-hour | Pay per instance-hour |
| **Frameworks** | Spark, Python | Spark, Hadoop, Presto, etc. |
| **Complexity** | Simple, less control | More control, complex |

### Use Cases
1. **Data Lake ETL**: Transform data in S3
2. **Metadata Management**: Centralized catalog
3. **Schema Discovery**: Automatic with crawlers
4. **Data Preparation**: Clean and normalize data
5. **Cross-service Integration**: Athena, EMR, Redshift

### Pricing
- **Crawler**: $0.44 per DPU-hour
- **ETL Job**: $0.44 per DPU-hour
- **Data Catalog**: First million objects free, then $1 per 100,000 objects/month
- **Development Endpoint**: $0.44 per DPU-hour

### Exam Tips
✅ **Serverless ETL**: No infrastructure management

✅ **Data Catalog**: Shared metadata for Athena, EMR, Redshift Spectrum

✅ **Crawlers**: Automatic schema discovery

✅ **Job Bookmarks**: Track processed data, prevent duplicates

✅ **Glue vs EMR**: Glue for simple ETL, EMR for complex big data processing

---

## 5. Amazon QuickSight

### What is Amazon QuickSight?
- **Serverless business intelligence (BI) service**
- Create interactive dashboards and visualizations
- Machine learning-powered insights
- Pay-per-session pricing

### Key Features
- **Fast**: SPICE in-memory engine
- **Serverless**: No infrastructure management
- **ML Insights**: Anomaly detection, forecasting
- **Embedded**: Embed dashboards in applications
- **Mobile**: iOS and Android apps

### QuickSight Architecture

```
┌──────────────────────────────────────────────────────────┐
│                  Amazon QuickSight                       │
│                                                          │
│  ┌──────────────┐    ┌──────────┐    ┌──────────────┐  │
│  │ Data Sources │───►│  SPICE   │───►│  Dashboards  │  │
│  │              │    │  Engine  │    │              │  │
│  └──────────────┘    └──────────┘    └──────────────┘  │
│                                              │           │
└──────────────────────────────────────────────┼───────────┘
                                               │
                                               ▼
                                        ┌──────────────┐
                                        │    Users     │
                                        │  - Readers   │
                                        │  - Authors   │
                                        │  - Admins    │
                                        └──────────────┘
```

### Data Sources

**AWS Data Sources:**
- Amazon RDS
- Amazon Aurora
- Amazon Redshift
- Amazon Athena
- Amazon S3
- Amazon OpenSearch
- AWS IoT Analytics

**Third-Party Sources:**
- Salesforce
- Jira
- GitHub
- ServiceNow
- Adobe Analytics
- Twitter

**File Uploads:**
- CSV, TSV, Excel
- JSON, XML
- ELF, CLF (log formats)

**Databases via JDBC:**
- MySQL, PostgreSQL
- SQL Server, Oracle
- Teradata, Presto

### SPICE (Super-fast, Parallel, In-memory Calculation Engine)

**What is SPICE?**
- In-memory data engine
- Fast query performance
- Automatically replicates for high availability
- Pay for capacity used

**Benefits:**
- **Fast**: Sub-second query response
- **Scalable**: Automatically scales
- **Durable**: Data replicated across AZs

**SPICE Capacity:**
- 10 GB per user (Enterprise)
- 1 GB per user (Standard)
- Purchase additional capacity

### User Types

**Readers:**
- View and interact with dashboards
- Cannot create analyses or dashboards
- Lower cost

**Authors:**
- Create analyses and dashboards
- Connect to data sources
- Share dashboards
- Higher cost

**Admins:**
- Manage users and subscriptions
- All author permissions

### Visualizations

**Chart Types:**
- **Bar charts**: Comparison
- **Line charts**: Trends over time
- **Pie charts**: Proportions
- **Scatter plots**: Correlations
- **Heat maps**: Patterns in data
- **Pivot tables**: Summarize data
- **KPIs**: Key metrics
- **Geo maps**: Location-based data
- **Tree maps**: Hierarchical data
- **Waterfall**: Cumulative effect

### ML Insights

**Anomaly Detection:**
- Automatically find outliers
- Detect unusual patterns
- Root cause analysis

**Forecasting:**
- Predict future trends
- Based on historical data
- Confidence intervals

**Auto-Narratives:**
- Natural language summaries
- Key insights in plain English

**Suggested Insights:**
- ML-powered recommendations
- Discover hidden patterns

### Dashboards and Analyses

**Analysis:**
- Working area to create visualizations
- Explore and prepare data
- Not shared with others

**Dashboard:**
- Read-only snapshot of analysis
- Share with users
- Interactive filtering

**Publishing:**
1. Create analysis
2. Add visualizations
3. Publish as dashboard
4. Share with users or groups

### Sharing and Permissions

**Share Dashboards:**
- Share with individual users
- Share with groups
- Email report schedules

**Row-Level Security (RLS):**
- Restrict data based on user
- Different users see different data
- Define rules in dataset

**Example RLS:**
```
User: john@example.com → Region: US-East
User: jane@example.com → Region: US-West

Dashboard shows only relevant region data per user
```

### Embedded Analytics
- Embed dashboards in applications
- White-label BI
- API-based integration
- SSO support

### Paginated Reports
- Printable, formatted reports
- Pixel-perfect layouts
- Scheduled email delivery
- Export to PDF, Excel

### QuickSight Q
- **Natural language queries**
- Ask questions in plain English
- Powered by ML
- "What were sales last quarter?"

### Pricing

**Standard Edition:**
- **Authors**: $12/month per user
- **Readers**: $0.30 per session (max $5/month)
- **SPICE**: $0.25 per GB/month

**Enterprise Edition:**
- **Authors**: $18/month per user
- **Readers**: $0.30 per session (max $5/month)
- **SPICE**: $0.38 per GB/month
- Additional features: Encryption, AD integration, hourly refresh

**Pay-per-Session:**
- Readers pay only when accessing dashboards
- Max $5 per reader per month
- Cost-effective for infrequent users

### Use Cases
1. **Business dashboards**: Sales, marketing, operations
2. **Embedded analytics**: SaaS applications
3. **Ad-hoc analysis**: Self-service BI
4. **Executive reporting**: KPIs and metrics
5. **Data exploration**: Interactive visualizations

### Exam Tips
✅ **Serverless BI**: No infrastructure, pay-per-session

✅ **SPICE engine**: In-memory for fast performance

✅ **ML Insights**: Anomaly detection, forecasting

✅ **Data sources**: Connect to RDS, Redshift, Athena, S3

✅ **Embedded**: Embed dashboards in applications

---

## 6. Other Analytics Services

### Amazon OpenSearch Service (formerly Elasticsearch)
- **Search and analytics engine**
- Full-text search
- Log analytics
- Real-time application monitoring

**Use Cases:**
- Log and event data analysis
- Full-text search
- Clickstream analytics
- Security information and event management (SIEM)

### Amazon Redshift
- Covered in Database module
- **Data warehouse**
- Petabyte-scale analytics
- Columnar storage

### AWS Data Pipeline
- **Orchestrate data workflows**
- Move data between AWS services
- Schedule and monitor pipelines
- **Note**: Being replaced by AWS Glue workflows

### AWS Lake Formation
- **Build and manage data lakes**
- Centralized security and governance
- Fine-grained access control
- Blueprint for common ingestion patterns

**Features:**
- Import data from multiple sources
- Tag-based access control
- Column-level security
- Audit and compliance

### Amazon Managed Streaming for Apache Kafka (MSK)
- **Fully managed Apache Kafka**
- Build streaming data pipelines
- Alternative to Kinesis

**MSK vs Kinesis:**
- MSK: For existing Kafka users, more control
- Kinesis: Fully managed, AWS-native, simpler

---

## 7. Data Lake Architecture on AWS

### What is a Data Lake?
- **Centralized repository** for all structured and unstructured data
- Store data at any scale
- Run analytics without moving data

### Data Lake on AWS

```
┌─────────────────────────────────────────────────────────────┐
│                       Data Lake (S3)                        │
│                                                             │
│  Raw Zone      │    Processed Zone    │   Curated Zone     │
│  (Landing)     │    (Transformed)     │   (Analytics-ready)│
└─────────────────────────────────────────────────────────────┘
      │                    │                       │
      ▼                    ▼                       ▼
┌──────────┐        ┌───────────┐          ┌──────────────┐
│  Glue    │───────►│   Glue    │─────────►│   Athena     │
│ Crawler  │        │  ETL Job  │          │   EMR        │
└──────────┘        └───────────┘          │   Redshift   │
                                           │   QuickSight │
                                           └──────────────┘
```

### Best Practices

**1. Organize by Zones:**
- **Raw**: Original data
- **Processed**: Cleansed, transformed
- **Curated**: Business-ready, aggregated

**2. Use Partitioning:**
- Organize by date, region, etc.
- Improve query performance
- Reduce costs

**3. Choose Right Format:**
- **CSV/JSON**: Human-readable, larger size
- **Parquet/ORC**: Columnar, compressed, best for analytics

**4. Implement Cataloging:**
- Use AWS Glue Data Catalog
- Centralized metadata

**5. Security:**
- Encryption at rest (S3)
- Encryption in transit (TLS)
- IAM and bucket policies
- Lake Formation for fine-grained access

---

## 8. Exam Tips Summary

### Key Concepts

✅ **Athena**
- Serverless SQL queries on S3
- Pay per TB scanned
- Use Parquet/ORC and partitioning for cost savings
- Integrates with Glue Data Catalog

✅ **Kinesis Data Streams**
- Real-time streaming, custom processing
- Shards for capacity (1 MB/sec write, 2 MB/sec read per shard)
- Retention: 24 hours to 365 days

✅ **Kinesis Firehose**
- Fully managed, near real-time delivery
- No code, automatic scaling
- Destinations: S3, Redshift, OpenSearch, Splunk
- 60-second minimum latency

✅ **Kinesis Data Analytics**
- Real-time analytics with SQL or Flink
- Streaming data processing

✅ **EMR**
- Managed Hadoop/Spark clusters
- Node types: Master, Core (HDFS + compute), Task (compute only)
- Use Spot Instances for Task nodes
- Store data in S3 (EMRFS) for persistence

✅ **Glue**
- Serverless ETL
- Data Catalog for metadata
- Crawlers for schema discovery
- Job Bookmarks to track processed data

✅ **QuickSight**
- Serverless BI and dashboards
- SPICE in-memory engine
- Pay-per-session pricing
- ML insights (anomaly detection, forecasting)

### Common Scenarios

**Scenario 1: Ad-hoc SQL queries on S3 data**
- **Solution**: Amazon Athena + Glue Data Catalog
- Use Parquet format and partitioning

**Scenario 2: Real-time log ingestion and storage**
- **Solution**: Kinesis Firehose → S3
- Transform with Lambda if needed

**Scenario 3: Real-time analytics on streaming data**
- **Solution**: Kinesis Data Streams → Kinesis Data Analytics → Output

**Scenario 4: Large-scale data transformation (Spark)**
- **Solution**: AWS Glue (serverless) or EMR (managed cluster)
- Glue for simpler ETL, EMR for complex processing

**Scenario 5: Business intelligence dashboards**
- **Solution**: QuickSight
- Connect to Athena, Redshift, or RDS

**Scenario 6: Build data lake**
- **Solution**: S3 + Glue + Lake Formation
- Athena for querying, QuickSight for visualization

---

## 9. Hands-On Practice

### Lab 1: Athena + Glue
1. Create S3 bucket and upload CSV data
2. Run Glue Crawler to discover schema
3. Query data using Athena
4. Create partitioned table
5. Optimize with Parquet format

### Lab 2: Kinesis Firehose
1. Create Firehose delivery stream
2. Configure S3 destination
3. Send data using AWS SDK or CLI
4. Add Lambda transformation
5. Verify data in S3

### Lab 3: Glue ETL Job
1. Create Glue database
2. Run Crawler on source data
3. Create ETL job in Glue Studio
4. Add transformations
5. Run job and verify output

### Lab 4: QuickSight Dashboard
1. Sign up for QuickSight
2. Connect to Athena or S3
3. Create dataset
4. Build visualizations
5. Publish dashboard

---

## 10. Additional Resources

### AWS Documentation
- [Amazon Athena](https://docs.aws.amazon.com/athena/)
- [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/)
- [Amazon EMR](https://docs.aws.amazon.com/emr/)
- [AWS Glue](https://docs.aws.amazon.com/glue/)
- [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/)

### Whitepapers
- Big Data Analytics Options on AWS
- AWS Glue Best Practices
- Building Data Lakes on AWS

---

**Next Module:** [12-Architecture-Patterns →](../12-Architecture-Patterns/README.md)

**Previous Module:** [← 10-Migration](../10-Migration/README.md)

