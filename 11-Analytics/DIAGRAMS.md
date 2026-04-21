# Analytics - Mermaid Diagrams

## Amazon Athena

### Athena Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        S3["S3 Data Lake<br/>CSV, JSON, Parquet, ORC<br/>Partitioned data"]
        CloudTrail[CloudTrail Logs]
        VPCFlow[VPC Flow Logs]
        ELB_Logs[ELB Access Logs]
    end
    
    subgraph AWS_Athena_Group["AWS Athena"]
        Athena["Amazon Athena<br/>Serverless SQL queries<br/>Presto-based"]
        
        GlueCatalog["AWS Glue Data Catalog<br/>Table definitions<br/>Schema metadata"]
        
        Athena --> GlueCatalog
    end
    
    subgraph Query_Analysis_Group["Query & Analysis"]
        Query["SQL Queries<br/>SELECT, JOIN, GROUP BY<br/>Standard SQL"]
        
        Results["Query Results<br/>Stored in S3"]
        
        Query --> Results
    end
    
    subgraph Visualization_Group["Visualization"]
        QuickSight["Amazon QuickSight<br/>Business intelligence"]
        JDBC["JDBC/ODBC<br/>BI Tools<br/>Tableau, PowerBI"]
    end
    
    S3 --> GlueCatalog
    CloudTrail --> GlueCatalog
    VPCFlow --> GlueCatalog
    ELB_Logs --> GlueCatalog
    
    GlueCatalog --> Query
    
    Results --> QuickSight
    Results --> JDBC
    
    Features["Features:<br/>✅ Serverless - no infrastructure<br/>✅ Pay per query $5 per TB scanned<br/>✅ Supports partitioning<br/>✅ Columnar formats for cost savings<br/>✅ Federated queries<br/>💡 Use Parquet for 90% cost reduction"]
    
    classDef style1 fill:#FF9900
    class Athena style1
    classDef style2 fill:#569A31
    class GlueCatalog style2
```

### Athena Performance Optimization

```mermaid
graph TB
    Original["Original S3 Data<br/>CSV format<br/>1 TB data<br/>$5 per query"]
    
    Optimizations{"Performance<br/>Optimizations"}
    
    Original --> Optimizations
    
    Optimizations --> Partition["Partition Data<br/>By year/month/day<br/>Only scan relevant partitions"]
    
    Optimizations --> Columnar["Use Columnar Format<br/>Parquet or ORC<br/>Only read needed columns"]
    
    Optimizations --> Compress["Compress Data<br/>Snappy, GZIP, LZO<br/>Smaller file sizes"]
    
    Optimizations --> Larger["Larger Files<br/>&gt; 128 MB per file<br/>Reduce overhead"]
    
    Partition --> Result1["Scan only 1 month:<br/>83 GB instead of 1 TB<br/>$0.42 per query<br/>92% savings"]
    
    Columnar --> Result2["Select 2 of 10 columns:<br/>200 GB instead of 1 TB<br/>$1 per query<br/>80% savings"]
    
    Compress --> Result3["Compress by 50%:<br/>500 GB instead of 1 TB<br/>$2.50 per query<br/>50% savings"]
    
    Combined["Combined Optimizations:<br/>Partition + Parquet + Compress<br/>10 GB scanned<br/>$0.05 per query<br/>99% cost reduction!"]
    
    Result1 --> Combined
    Result2 --> Combined
    Result3 --> Combined
    
    classDef style1 fill:#C00
    class Original style1
    classDef style2 fill:#569A31
    class Combined style2
    classDef style3 fill:#FF9900
    class Optimizations style3
```

## Amazon EMR (Elastic MapReduce)

### EMR Cluster Architecture

```mermaid
graph TB
    subgraph EMR_Cluster_Group["EMR Cluster"]
        Master["Master Node<br/>Manage cluster<br/>Coordinate jobs<br/>Track status"]
        
        subgraph Core_Nodes_Group["Core Nodes"]
            Core1["Core Node 1<br/>Run tasks<br/>Store data in HDFS"]
            Core2["Core Node 2<br/>Run tasks<br/>Store data in HDFS"]
        end
        
        subgraph Task_Nodes_Optional_Group["Task Nodes Optional"]
            Task1["Task Node 1<br/>Run tasks only<br/>No HDFS<br/>Spot instances OK"]
            Task2["Task Node 2<br/>Run tasks only<br/>No HDFS<br/>Spot instances OK"]
        end
        
        Master --> Core1
        Master --> Core2
        Master --> Task1
        Master --> Task2
    end
    
    subgraph Storage_Group["Storage"]
        HDFS["HDFS<br/>Distributed file system<br/>On core nodes"]
        
        EMRFS["EMRFS<br/>Access S3 as HDFS<br/>Persistent storage"]
    end
    
    subgraph Data_Sources_Targets_Group["Data Sources & Targets"]
        S3["Amazon S3<br/>Input & Output<br/>Persistent data"]
        
        DynamoDB["DynamoDB<br/>Read/Write"]
        
        RDS["RDS/Aurora<br/>JDBC connections"]
    end
    
    Core1 --> HDFS
    Core2 --> HDFS
    
    Master --> EMRFS
    EMRFS --> S3
    
    Master --> DynamoDB
    Master --> RDS
    
    Frameworks["Big Data Frameworks:<br/>• Hadoop MapReduce<br/>• Apache Spark<br/>• Apache Hive<br/>• Apache HBase<br/>• Presto<br/>• Flink<br/>• Hudi"]
    
    classDef style1 fill:#FF9900
    class Master style1
    classDef style2 fill:#569A31
    class S3 style2
```

### EMR Deployment Options

```mermaid
graph TB
    EMR[Amazon EMR]
    
    EMR --> EC2["EMR on EC2<br/>Traditional clusters"]
    EMR --> EKS["EMR on EKS<br/>Kubernetes pods"]
    EMR --> Outposts["EMR on Outposts<br/>On-premises"]
    EMR --> Serverless["EMR Serverless<br/>No cluster management"]
    
    subgraph EMR_on_EC2_Group["EMR on EC2"]
        EC2_Features["• Full control<br/>• Instance types<br/>• Persistent or transient<br/>• Spot instances<br/>• Auto-scaling"]
    end
    
    subgraph EMR_on_EKS_Group["EMR on EKS"]
        EKS_Features["• Shared EKS cluster<br/>• Multiple teams<br/>• Better resource utilization<br/>• Faster startup"]
    end
    
    subgraph EMR_Serverless_Group["EMR Serverless"]
        Serverless_Features["• No cluster management<br/>• Auto-scaling<br/>• Pay per use<br/>• Sub-minute startup<br/>• Ideal for: Ad-hoc, batch"]
    end
    
    EC2 --> EC2_Features
    EKS --> EKS_Features
    Serverless --> Serverless_Features
    
    Comparison["Choose:<br/>• Control needed -&gt; EC2<br/>• Kubernetes -&gt; EKS<br/>• Simplicity -&gt; Serverless"]
    
    classDef style1 fill:#FF9900
    class EMR style1
    classDef style2 fill:#569A31
    class Serverless style2
```

## Amazon Kinesis

### Kinesis Services Overview

```mermaid
mindmap
    root((Amazon Kinesis<br/>Real-time Streaming))
        Kinesis Data Streams
            Real-time data ingestion
            Custom processing
            Shards for scaling
            Retain: 1-365 days
            Producers & Consumers
        Kinesis Data Firehose
            Load streaming data
            Near real-time
            No management
            Transform with Lambda
            Destinations: S3, Redshift, OpenSearch
        Kinesis Data Analytics
            SQL on streaming data
            Apache Flink
            Real-time analytics
            No servers to manage
        Kinesis Video Streams
            Stream video
            WebRTC
            ML processing
            Video playback
```

### Kinesis Data Streams Architecture

```mermaid
graph LR
    subgraph Producers_Group["Producers"]
        App["Applications<br/>Kinesis Producer Library"]
        Agent["Kinesis Agent<br/>Log files"]
        SDK["AWS SDK<br/>PutRecord API"]
        IoT[IoT Devices]
    end
    
    subgraph Kinesis_Data_Stream_Group["Kinesis Data Stream"]
        Stream["Kinesis Data Stream<br/>my-stream"]
        
        Shard1["Shard 1<br/>1 MB/s in<br/>2 MB/s out"]
        Shard2["Shard 2<br/>1 MB/s in<br/>2 MB/s out"]
        Shard3["Shard 3<br/>1 MB/s in<br/>2 MB/s out"]
        
        Stream --> Shard1
        Stream --> Shard2
        Stream --> Shard3
    end
    
    subgraph Consumers_Group["Consumers"]
        Lambda["Lambda<br/>Event processing"]
        EC2["EC2/ECS<br/>Kinesis Client Library"]
        Firehose["Kinesis Firehose<br/>Load to S3/Redshift"]
        Analytics["Kinesis Analytics<br/>SQL queries"]
    end
    
    App --> Shard1
    Agent --> Shard2
    SDK --> Shard3
    IoT --> Shard1
    
    Shard1 --> Lambda
    Shard2 --> EC2
    Shard3 --> Firehose
    Shard1 --> Analytics
    
    Features["Features:<br/>✅ Real-time 70ms-200ms<br/>✅ Replay capability<br/>✅ Retention: 1-365 days<br/>✅ Immutable records<br/>✅ Ordered per shard<br/>💰 Pay per shard-hour + PUT"]
    
    classDef style1 fill:#FF9900
    class Stream style1
    classDef style2 fill:#569A31
    class Shard1 style2
```

### Kinesis Data Firehose

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        DirectPut["Direct PUT<br/>Applications, SDK"]
        KinesisStreams[Kinesis Data Streams]
        CloudWatch[CloudWatch Logs]
        IoTCore[AWS IoT]
    end
    
    subgraph Kinesis_Firehose_Group["Kinesis Firehose"]
        Firehose["Kinesis Data Firehose<br/>Fully managed<br/>Auto-scaling<br/>Near real-time"]
        
        Transform["Optional Transformation<br/>Lambda function<br/>Convert, enrich, filter"]
        
        Batch["Batching<br/>Buffer: 1 MB - 128 MB<br/>Interval: 60s - 900s"]
        
        Firehose --> Transform
        Transform --> Batch
    end
    
    subgraph Destinations_Group["Destinations"]
        S3["Amazon S3<br/>Data lake<br/>Parquet, ORC, JSON"]
        
        Redshift["Amazon Redshift<br/>Copy via S3"]
        
        OpenSearch["Amazon OpenSearch<br/>Log analytics"]
        
        Splunk["Splunk<br/>3rd party"]
        
        HTTP["Custom HTTP Endpoint<br/>Datadog, New Relic"]
    end
    
    subgraph Backup_Group["Backup"]
        BackupS3["Backup S3 Bucket<br/>All source records<br/>Failed records"]
    end
    
    DirectPut --> Firehose
    KinesisStreams --> Firehose
    CloudWatch --> Firehose
    IoTCore --> Firehose
    
    Batch --> S3
    Batch --> Redshift
    Batch --> OpenSearch
    Batch --> Splunk
    Batch --> HTTP
    
    Firehose -.Optional.-> BackupS3
    
    VsStreams["Firehose vs Data Streams:<br/>Firehose: Fully managed, near real-time, destinations<br/>Streams: Real-time, custom processing, replay"]
    
    classDef style1 fill:#FF9900
    class Firehose style1
    classDef style2 fill:#569A31
    class S3 style2
```

### Kinesis Data Analytics

```mermaid
graph TB
    subgraph Input_Streams_Group["Input Streams"]
        KinesisIn["Kinesis Data Streams<br/>Real-time input"]
        FirehoseIn["Kinesis Firehose<br/>Near real-time input"]
        S3Reference["S3 Reference Data<br/>Enrich streaming data"]
    end
    
    subgraph Kinesis_Data_Analytics_Group["Kinesis Data Analytics"]
        Analytics[Kinesis Data Analytics]
        
        SQL["SQL Application<br/>Standard SQL queries<br/>Windowing, aggregations"]
        
        Flink["Apache Flink Application<br/>Java, Scala, Python<br/>Advanced processing"]
        
        Analytics --> SQL
        Analytics --> Flink
    end
    
    subgraph Output_Destinations_Group["Output Destinations"]
        KinesisOut["Kinesis Data Streams<br/>Further processing"]
        FirehoseOut["Kinesis Firehose<br/>Load to destinations"]
        Lambda["Lambda<br/>Custom processing"]
    end
    
    KinesisIn --> SQL
    FirehoseIn --> SQL
    S3Reference -.Enrich.-> SQL
    
    KinesisIn --> Flink
    
    SQL --> KinesisOut
    SQL --> FirehoseOut
    SQL --> Lambda
    
    Flink --> KinesisOut
    Flink --> FirehoseOut
    
    UseCases["Use Cases:<br/>• Real-time dashboards<br/>• Real-time metrics<br/>• Streaming ETL<br/>• Anomaly detection<br/>• IoT analytics"]
    
    Features["Features:<br/>✅ Serverless<br/>✅ Auto-scaling<br/>✅ Pay for processing<br/>✅ IAM for access control<br/>✅ Schema discovery"]
    
    classDef style1 fill:#FF9900
    class Analytics style1
    classDef style2 fill:#569A31
    class SQL style2
```

## AWS Glue

### Glue ETL Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        S3_Source[S3 Data Lake]
        RDS_Source[RDS Databases]
        DynamoDB_Source[DynamoDB]
        JDBC_Source["JDBC Sources<br/>On-premises DBs"]
    end
    
    subgraph AWS_Glue_Group["AWS Glue"]
        Crawler["Glue Crawler<br/>Auto-discover schema<br/>Populate catalog"]
        
        Catalog["Glue Data Catalog<br/>Central metadata repository<br/>Table definitions<br/>Schema versions"]
        
        ETL["Glue ETL Jobs<br/>Serverless Spark/Python<br/>Transform data<br/>Auto-scaling"]
        
        Scheduler["Job Scheduler<br/>Time-based triggers<br/>Event-based triggers"]
        
        Crawler --> Catalog
        Catalog --> ETL
        Scheduler --> ETL
    end
    
    subgraph Data_Targets_Group["Data Targets"]
        S3_Target["S3 Data Lake<br/>Parquet, ORC, CSV"]
        Redshift_Target["Redshift<br/>Data warehouse"]
        RDS_Target["RDS/Aurora<br/>Analytics DB"]
    end
    
    S3_Source --> Crawler
    RDS_Source --> Crawler
    DynamoDB_Source --> Crawler
    JDBC_Source --> Crawler
    
    ETL --> S3_Target
    ETL --> Redshift_Target
    ETL --> RDS_Target
    
    Athena[Amazon Athena] -.Query.-> Catalog
    EMR[Amazon EMR] -.Use.-> Catalog
    Redshift2[Redshift Spectrum] -.Use.-> Catalog
    
    Features["Features:<br/>✅ Serverless<br/>✅ Pay per second for ETL<br/>✅ Python or Scala<br/>✅ Built-in transformations<br/>✅ Job bookmarks<br/>✅ Development endpoints"]
    
    classDef style1 fill:#FF9900
    class Catalog style1
    classDef style2 fill:#569A31
    class ETL style2
```

### Glue Data Catalog

```mermaid
graph TB
    subgraph Data_Catalog_Components_Group["Data Catalog Components"]
        Catalog["Glue Data Catalog<br/>Metadata repository"]
        
        Database["Databases<br/>Logical grouping"]
        
        Tables["Tables<br/>Schema definition<br/>Column types<br/>Partitions"]
        
        Crawler_Config["Crawlers<br/>Scan data sources<br/>Infer schema"]
        
        Catalog --> Database
        Database --> Tables
        Catalog --> Crawler_Config
    end
    
    subgraph Services_Using_Catalog_Group["Services Using Catalog"]
        Athena["Amazon Athena<br/>SQL queries"]
        
        Redshift_Spectrum["Redshift Spectrum<br/>Query S3"]
        
        EMR["Amazon EMR<br/>Spark, Hive"]
        
        Glue_ETL["Glue ETL Jobs<br/>Transform data"]
    end
    
    Tables --> Athena
    Tables --> Redshift_Spectrum
    Tables --> EMR
    Tables --> Glue_ETL
    
    Benefits["Benefits:<br/>✅ Single source of truth<br/>✅ Avoid data silos<br/>✅ Schema evolution<br/>✅ Partition discovery<br/>✅ Cross-service metadata<br/>💰 First million objects stored free"]
    
    Hive["Hive Metastore Compatible<br/>Import existing Hive catalogs"] -.Compatible.-> Catalog
    
    classDef style1 fill:#FF9900
    class Catalog style1
    classDef style2 fill:#569A31
    class Tables style2
```

## Amazon QuickSight

### QuickSight Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        RDS["RDS/Aurora"]
        Redshift[Redshift]
        Athena[Athena]
        S3[S3]
        Salesforce[Salesforce]
        Excel[Excel, CSV]
        OnPrem["On-Premises DBs<br/>via VPC"]
    end
    
    subgraph QuickSight_Group["QuickSight"]
        SPICE["SPICE In-Memory Engine<br/>Super-fast Performance<br/>Interactive Caching Engine<br/>Columnar storage"]
        
        Datasets["Datasets<br/>Data preparation<br/>Joins, filters, transforms"]
        
        Analysis["Analysis<br/>Visual exploration<br/>Drag-and-drop"]
        
        Dashboards["Dashboards<br/>Published views<br/>Share with users"]
        
        Datasets --> SPICE
        SPICE --> Analysis
        Analysis --> Dashboards
    end
    
    subgraph Features_Group["Features"]
        ML["QuickSight ML Insights<br/>Anomaly detection<br/>Forecasting<br/>Natural language queries"]
        
        Embedded["Embedded Analytics<br/>Embed in applications<br/>Custom branding"]
        
        Enterprise["Enterprise Edition<br/>Row-level security<br/>AD integration<br/>Encryption at rest"]
    end
    
    RDS --> Datasets
    Redshift --> Datasets
    Athena --> Datasets
    S3 --> Datasets
    Salesforce --> Datasets
    Excel --> Datasets
    OnPrem --> Datasets
    
    Dashboards --> ML
    Dashboards --> Embedded
    Dashboards --> Enterprise
    
    Pricing["Pricing:<br/>💰 Standard: $9/user/month<br/>💰 Enterprise: $18/user/month<br/>💰 SPICE: $0.25/GB/month<br/>💰 Readers: $0.30/session $5 max"]
    
    classDef style1 fill:#FF9900
    class SPICE style1
    classDef style2 fill:#569A31
    class Dashboards style2
```

## Amazon OpenSearch (ElasticSearch)

### OpenSearch Architecture

```mermaid
graph TB
    subgraph Data_Ingestion_Group["Data Ingestion"]
        Kinesis["Kinesis Firehose<br/>Streaming logs"]
        Logstash["Logstash<br/>Log shipping"]
        CloudWatch[CloudWatch Logs]
        Lambda[Lambda Functions]
        IoT[AWS IoT]
    end
    
    subgraph OpenSearch_Domain_Group["OpenSearch Domain"]
        Master["Master Nodes<br/>Cluster management<br/>Optional, dedicated"]
        
        Data1["Data Node 1<br/>Store & search<br/>Instance types"]
        Data2["Data Node 2<br/>Store & search"]
        Data3["Data Node 3<br/>Store & search"]
        
        UltraWarm["UltraWarm Nodes<br/>Read-only<br/>S3-backed<br/>Cost-effective"]
        
        ColdStorage["Cold Storage<br/>S3-based<br/>Infrequent access<br/>Lowest cost"]
        
        Master --> Data1
        Master --> Data2
        Master --> Data3
        
        Data1 --> UltraWarm
        UltraWarm --> ColdStorage
    end
    
    subgraph Access_Visualization_Group["Access & Visualization"]
        Kibana["OpenSearch Dashboards<br/>Formerly Kibana<br/>Visualization"]
        
        API["REST API<br/>Search queries<br/>CRUD operations"]
        
        SQL["SQL Support<br/>Query with SQL<br/>JDBC driver"]
    end
    
    Kinesis --> Data1
    Logstash --> Data2
    CloudWatch --> Data3
    Lambda --> Data1
    IoT --> Data2
    
    Data1 --> Kibana
    Data1 --> API
    Data1 --> SQL
    
    Features["Features:<br/>✅ Multi-AZ deployment<br/>✅ Built-in dashboards<br/>✅ Full-text search<br/>✅ Application monitoring<br/>✅ Log analytics<br/>💰 Pay per instance hour"]
    
    UseCases["Use Cases:<br/>• Log analytics<br/>• Application monitoring<br/>• Security analytics<br/>• Full-text search<br/>• Clickstream analytics"]
    
    classDef style1 fill:#FF9900
    class Master style1
    classDef style2 fill:#569A31
    class Data1 style2
    classDef style3 fill:#146EB4
    class Kibana style3
```

## Analytics Architecture Patterns

### Real-Time Analytics Pipeline

```mermaid
graph LR
    subgraph Data_Sources_Group["Data Sources"]
        Website[Website Clickstream]
        Mobile[Mobile App Events]
        IoT[IoT Sensors]
    end
    
    subgraph Real_Time_Ingestion_Group["Real-Time Ingestion"]
        Kinesis["Kinesis Data Streams<br/>Real-time collection"]
    end
    
    subgraph Stream_Processing_Group["Stream Processing"]
        Lambda["Lambda<br/>Transform"]
        Analytics["Kinesis Analytics<br/>Windowing, aggregation"]
    end
    
    subgraph Storage_Analysis_Group["Storage & Analysis"]
        Firehose[Kinesis Firehose]
        S3["S3 Data Lake<br/>Parquet format"]
        OpenSearch["OpenSearch<br/>Real-time dashboards"]
    end
    
    subgraph Batch_Analysis_Group["Batch Analysis"]
        Glue["Glue ETL<br/>Nightly processing"]
        Athena["Athena<br/>Ad-hoc queries"]
        Redshift["Redshift<br/>Data warehouse"]
    end
    
    subgraph Visualization_Group["Visualization"]
        QuickSight["QuickSight<br/>BI dashboards"]
        Kibana["OpenSearch Dashboards<br/>Real-time monitoring"]
    end
    
    Website --> Kinesis
    Mobile --> Kinesis
    IoT --> Kinesis
    
    Kinesis --> Lambda
    Kinesis --> Analytics
    
    Lambda --> Firehose
    Analytics --> Firehose
    
    Firehose --> S3
    Firehose --> OpenSearch
    
    S3 --> Glue
    Glue --> Redshift
    S3 --> Athena
    
    Redshift --> QuickSight
    Athena --> QuickSight
    OpenSearch --> Kibana
    
    classDef style1 fill:#FF9900
    class Kinesis style1
    classDef style2 fill:#569A31
    class S3 style2
    classDef style3 fill:#146EB4
    class QuickSight style3
```

### Batch Analytics Pipeline

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        Databases["RDS/Aurora<br/>Transactional DBs"]
        Apps["Application Logs<br/>S3 buckets"]
        OnPrem["On-Premises<br/>DataSync"]
    end
    
    subgraph Data_Lake_S3_Group["Data Lake - S3"]
        Raw["Raw Zone<br/>Original data<br/>All formats"]
        
        Processed["Processed Zone<br/>Cleaned data<br/>Parquet/ORC"]
        
        Curated["Curated Zone<br/>Business views<br/>Aggregated"]
    end
    
    subgraph ETL_Processing_Group["ETL Processing"]
        Glue["AWS Glue<br/>Serverless ETL<br/>Scheduled jobs"]
        
        EMR["Amazon EMR<br/>Complex transformations<br/>Spark jobs"]
    end
    
    subgraph Data_Catalog_Group["Data Catalog"]
        Catalog["Glue Data Catalog<br/>Metadata<br/>Schema registry"]
    end
    
    subgraph Analytics_Group["Analytics"]
        Athena["Athena<br/>SQL queries<br/>Interactive"]
        
        Redshift["Redshift<br/>Data warehouse<br/>OLAP"]
        
        SageMaker["SageMaker<br/>ML training"]
    end
    
    Databases --> Raw
    Apps --> Raw
    OnPrem --> Raw
    
    Raw --> Glue
    Glue --> Processed
    Glue --> Catalog
    
    Processed --> EMR
    EMR --> Curated
    EMR --> Catalog
    
    Catalog --> Athena
    Catalog --> Redshift
    
    Curated --> Athena
    Curated --> Redshift
    Curated --> SageMaker
    
    Athena --> QuickSight["QuickSight<br/>Dashboards"]
    Redshift --> QuickSight
    
    classDef style1 fill:#C00
    class Raw style1
    classDef style2 fill:#FF9900
    class Processed style2
    classDef style3 fill:#569A31
    class Curated style3
```

