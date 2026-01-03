# Analytics Services - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company stores application logs in Amazon S3 in CSV format. A data analyst needs to run ad-hoc SQL queries on this data without setting up infrastructure. Which AWS service should be used?

A. Amazon EMR  
B. Amazon Athena  
C. Amazon Redshift  
D. AWS Glue  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Athena is serverless and queries S3 data using SQL
- No infrastructure to manage
- Pay per query (per TB scanned)
- Perfect for ad-hoc querying
- EMR requires cluster management
- Redshift requires data warehouse setup
- Glue is for ETL, not querying

**References:** Amazon Athena, Serverless Analytics
</details>

---

### Question 2
A solutions architect wants to reduce the cost of Athena queries on a large dataset stored in S3. The data is currently in CSV format and queries scan the entire dataset. What should be done to optimize costs?

A. Increase the Athena query timeout  
B. Convert data to Parquet format and partition by commonly queried fields  
C. Move data to Amazon Redshift  
D. Enable S3 versioning  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Athena charges per TB scanned ($5/TB)
- Parquet is columnar format, reduces data scanned by 30-90%
- Partitioning limits data scanned to relevant partitions
- Both optimizations significantly reduce costs
- Increasing timeout doesn't reduce scanned data
- Redshift adds infrastructure costs
- S3 versioning doesn't affect query performance

**References:** Athena Performance Optimization, Columnar Formats
</details>

---

### Question 3
A real-time analytics application needs to ingest clickstream data from a website, process it with custom business logic, and store results in DynamoDB. Which AWS service should be used for data ingestion?

A. Amazon Kinesis Data Streams  
B. Amazon Kinesis Data Firehose  
C. Amazon SQS  
D. AWS DataSync  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Kinesis Data Streams is for real-time streaming with custom processing
- Supports custom consumers (Lambda, EC2, KCL)
- Real-time processing capability
- Firehose is for loading data to destinations (S3, Redshift, etc.)
- SQS is for message queuing, not streaming analytics
- DataSync is for file transfers

**References:** Kinesis Data Streams, Real-Time Processing
</details>

---

### Question 4
A company wants to load streaming IoT sensor data into Amazon S3 for analysis with minimal operational overhead. The data should be delivered every 5 minutes and compressed. Which service is MOST appropriate?

A. Amazon Kinesis Data Streams with Lambda  
B. Amazon Kinesis Data Firehose  
C. Amazon SQS with Lambda  
D. AWS IoT Core with custom application  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Kinesis Data Firehose is fully managed, no infrastructure
- Automatically loads to S3
- Built-in compression (GZIP, Snappy)
- Buffer interval supports 60-900 seconds (5 minutes = 300 seconds)
- Minimal operational overhead
- Data Streams requires consumer application
- SQS adds unnecessary complexity
- Custom application requires maintenance

**References:** Kinesis Data Firehose, Serverless Data Loading
</details>

---

### Question 5
An Athena query is scanning 10 TB of data but only needs records from the last month. The S3 bucket structure is organized by year, month, and day. How can query performance and cost be improved?

A. Use S3 Select to filter data  
B. Create a partitioned table in Athena and query specific partitions  
C. Enable S3 Intelligent-Tiering  
D. Use Athena workgroups  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Partitioning allows queries to scan only relevant data
- WHERE clause with partition keys limits scan to specific partitions
- Dramatically reduces data scanned and costs
- Example: WHERE year='2024' AND month='01'
- S3 Select reduces transfer but doesn't work with Athena
- Intelligent-Tiering is for storage costs
- Workgroups organize queries but don't optimize scans

**References:** Athena Partitioning, Query Optimization
</details>

---

### Question 6
A company needs to process streaming data in real-time using SQL queries and send alerts when certain thresholds are exceeded. Which service should be used?

A. Amazon Athena  
B. Amazon Kinesis Data Analytics  
C. Amazon Kinesis Data Firehose  
D. AWS Glue  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Kinesis Data Analytics processes streaming data with SQL
- Real-time analytics on streaming data
- Can send results to Lambda for alerts
- Athena queries static data in S3
- Firehose loads data but doesn't analyze
- Glue is for ETL jobs

**References:** Kinesis Data Analytics, Stream Processing
</details>

---

### Question 7
A data engineering team needs to run Apache Spark jobs to process large datasets. They want a managed service that handles infrastructure provisioning. Which service should they use?

A. Amazon Athena  
B. Amazon EMR  
C. AWS Glue  
D. Amazon Kinesis  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- EMR (Elastic MapReduce) is managed big data platform
- Supports Apache Spark, Hadoop, Hive, etc.
- Handles cluster provisioning and scaling
- Optimized for large-scale data processing
- Athena is for SQL queries, not Spark
- Glue supports Spark but EMR provides more control
- Kinesis is for streaming, not batch processing

**References:** Amazon EMR, Big Data Processing
</details>

---

### Question 8
A company has streaming data in Kinesis Data Streams and wants to load it into Amazon Redshift for analytics. What is the MOST operationally efficient solution?

A. Use Lambda to read from Kinesis and write to Redshift  
B. Use Kinesis Data Firehose to load data into Redshift  
C. Use EC2 instances with custom scripts  
D. Use EMR to process and load data  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Firehose can read from Data Streams and load to Redshift
- Fully managed, no code required
- Automatically scales
- Loads via S3 (COPY command)
- Lambda requires custom code and error handling
- EC2 and EMR add operational overhead

**References:** Kinesis Data Firehose, Redshift Integration
</details>

---

### Question 9
An organization uses AWS Glue Crawlers to discover schemas for data in S3. The crawler should run automatically whenever new data arrives. How can this be configured?

A. Manually run the crawler daily  
B. Use EventBridge to trigger the crawler on S3 PutObject events  
C. Use AWS Config to detect changes  
D. Crawlers cannot be triggered automatically  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- EventBridge (formerly CloudWatch Events) can trigger on S3 events
- S3 PutObject events can invoke Glue Crawler
- Automated schema discovery when new data arrives
- Manual running isn't automatic
- Config tracks configuration, doesn't trigger workflows
- Glue supports multiple trigger types

**References:** AWS Glue, EventBridge Integration
</details>

---

### Question 10
A Kinesis Data Stream has 4 shards. Producers are writing 5,000 records per second. What is the likely issue and solution?

A. Shards are over capacity; add more shards  
B. Retention period is too short; increase it  
C. No issue, this is within limits  
D. Use Kinesis Data Firehose instead  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Each shard supports 1,000 records/sec write capacity
- 4 shards = 4,000 records/sec capacity
- 5,000 records/sec exceeds capacity
- Need at least 5 shards (or use on-demand mode)
- Will receive ProvisionedThroughputExceededException
- Retention doesn't affect write capacity
- Firehose is for different use cases

**Calculation:** 4 shards × 1,000 records/sec = 4,000 records/sec < 5,000 needed

**References:** Kinesis Data Streams, Shard Capacity
</details>

---

### Question 11
A company wants to visualize data from multiple sources including S3, RDS, and Redshift. They need interactive dashboards for business users. Which AWS service should be used?

A. Amazon Athena  
B. Amazon QuickSight  
C. Amazon CloudWatch  
D. Amazon Kinesis Data Analytics  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- QuickSight is business intelligence and visualization service
- Connects to multiple data sources (S3, RDS, Redshift, etc.)
- Creates interactive dashboards
- SPICE engine for fast analytics
- Athena queries data but doesn't visualize
- CloudWatch monitors infrastructure
- Kinesis analyzes streaming data

**References:** Amazon QuickSight, Business Intelligence
</details>

---

### Question 12
A solutions architect needs to ensure data in Kinesis Data Streams is retained for 7 days for reprocessing. What should be configured?

A. Set retention period to 168 hours (7 days)  
B. Use Kinesis Data Firehose with 7-day buffer  
C. Enable extended data retention in S3  
D. Kinesis cannot retain data beyond 24 hours  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Kinesis Data Streams supports retention from 24 hours to 365 days
- Default is 24 hours
- Extended retention has additional cost
- 7 days = 168 hours
- Firehose doesn't have 7-day buffer option
- S3 is separate storage, not Kinesis retention
- Extended retention is a supported feature

**References:** Kinesis Data Streams, Data Retention
</details>

---

### Question 13
An ETL pipeline needs to transform data from multiple sources, catalog the metadata, and run the jobs on a schedule. Which AWS service provides this functionality?

A. Amazon EMR  
B. AWS Glue  
C. AWS Data Pipeline  
D. Amazon Athena  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Glue is fully managed ETL service
- Glue Data Catalog stores metadata
- Glue Crawlers discover schemas
- Glue Jobs perform transformations
- Supports scheduling
- EMR requires more management
- Data Pipeline is older service
- Athena queries, doesn't transform

**References:** AWS Glue, ETL Pipeline
</details>

---

### Question 14
A company collects application logs in CloudWatch Logs and wants to analyze them using SQL queries. What is the MOST cost-effective solution?

A. Keep logs in CloudWatch and use Logs Insights  
B. Export logs to S3 and query with Athena  
C. Stream logs to Kinesis and use Data Analytics  
D. Load logs into Redshift  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudWatch Logs storage is expensive for long-term retention
- Export to S3 significantly reduces storage costs
- Athena queries S3 data with SQL ($5/TB scanned)
- Most cost-effective for infrequent analysis
- Logs Insights is good for recent logs
- Kinesis adds streaming costs
- Redshift requires cluster costs

**References:** CloudWatch Logs Export, Athena Cost Optimization
</details>

---

### Question 15
A Kinesis Data Firehose delivery stream should transform incoming JSON data using a Lambda function before storing in S3. How is this configured?

A. Firehose doesn't support transformations  
B. Enable data transformation and specify the Lambda function ARN  
C. Use Kinesis Data Analytics for transformation  
D. Transform data before sending to Firehose  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Kinesis Data Firehose supports Lambda transformation
- Configure transformation in delivery stream settings
- Firehose invokes Lambda for each batch
- Lambda can modify, filter, or enrich data
- Built-in feature, no separate service needed
- Transforming before Firehose is possible but not optimal

**References:** Kinesis Data Firehose, Data Transformation
</details>

---

### Question 16
An analytics application queries data in S3 using Athena. The queries are running slowly despite optimizations. The data is already in Parquet format and partitioned. What else can improve performance?

A. Optimize file sizes to 128 MB - 1 GB per file  
B. Switch to CSV format  
C. Disable partitioning  
D. Use smaller file sizes (1-10 MB)  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Too many small files causes performance issues
- Optimal file size is 128 MB - 1 GB
- Athena opens each file, many small files = overhead
- Combine small files into larger ones
- CSV is less efficient than Parquet
- Partitioning improves performance
- Very small files slow down queries

**References:** Athena Performance, File Size Optimization
</details>

---

### Question 17
A company uses Athena with a Glue Data Catalog. They want to ensure different teams can only query their own datasets. How should access be controlled?

A. Use S3 bucket policies  
B. Use IAM policies with Glue Catalog permissions  
C. Create separate AWS accounts  
D. Use Athena workgroups only  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- IAM policies control access to Glue Catalog databases and tables
- Fine-grained permissions per team
- Can combine with S3 bucket policies
- Separate accounts is overly complex
- Workgroups organize queries but don't enforce data access
- Glue Catalog permissions are the primary control

**References:** Athena Security, Glue Catalog Permissions
</details>

---

### Question 18
A real-time application needs guaranteed ordering of events for each user. Events should be processed in the order they arrive per user. Which Kinesis feature ensures this?

A. Use the same shard for all records  
B. Use the user ID as the partition key  
C. Enable Kinesis enhanced fan-out  
D. Use multiple shards with round-robin distribution  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Partition key determines which shard receives the record
- Same partition key always goes to the same shard
- Records in a shard are ordered by sequence number
- Using user ID ensures all user events go to same shard (ordered)
- One shard doesn't scale
- Enhanced fan-out is for parallel consumers
- Round-robin breaks ordering

**References:** Kinesis Data Streams, Ordering Guarantees
</details>

---

### Question 19
A company needs to load VPC Flow Logs into Amazon S3 for analysis with Athena. The solution should be fully managed with minimal setup. What should be configured?

A. Use Kinesis Data Streams with Lambda  
B. Use Kinesis Data Firehose as the Flow Logs destination  
C. Use CloudWatch Logs with manual export  
D. Use custom EC2 instances to collect logs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- VPC Flow Logs can deliver directly to Kinesis Data Firehose
- Firehose automatically loads to S3
- Fully managed, no code required
- Can compress and partition data
- Manual export isn't automated
- Data Streams requires consumer application
- EC2 instances add operational overhead

**References:** VPC Flow Logs, Kinesis Data Firehose
</details>

---

### Question 20
An Athena workgroup is configured with a data usage control of 1 TB per day. A user's query would scan 1.5 TB of data. What happens?

A. The query runs and scans 1.5 TB  
B. The query is rejected  
C. The query runs but only scans 1 TB  
D. The user receives a warning but query proceeds  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Workgroup data usage controls enforce limits
- Queries exceeding the limit are rejected
- Prevents cost overruns
- User must optimize query or request limit increase
- Query doesn't partially execute
- Hard enforcement, not just a warning

**References:** Athena Workgroups, Cost Controls
</details>

---

## Summary

### Key Concepts Tested:
1. **Amazon Athena**: Serverless SQL queries on S3, performance optimization, partitioning
2. **Kinesis Data Streams**: Real-time streaming, shard capacity, ordering, retention
3. **Kinesis Data Firehose**: Managed data loading, transformations, destinations
4. **Kinesis Data Analytics**: Real-time SQL analytics on streams
5. **Amazon EMR**: Managed big data processing, Spark/Hadoop
6. **AWS Glue**: ETL, Data Catalog, Crawlers
7. **Amazon QuickSight**: Business intelligence and visualization

### Exam Tips:
- ✅ Athena charges $5 per TB scanned - optimize with Parquet and partitions
- ✅ Each Kinesis shard: 1 MB/s or 1,000 records/s write, 2 MB/s read
- ✅ Use Firehose for simple loading to S3/Redshift/OpenSearch
- ✅ Use Data Streams for custom processing with ordering guarantees
- ✅ Partition key determines shard (same key = same shard = ordering)
- ✅ Glue Crawlers automatically discover schemas
- ✅ EMR for Apache Spark/Hadoop workloads
- ✅ QuickSight for dashboards and BI
- ✅ Parquet/ORC formats reduce costs 30-90% vs CSV/JSON

