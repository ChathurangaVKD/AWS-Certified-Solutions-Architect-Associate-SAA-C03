# Application Integration - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A microservices architecture needs asynchronous communication where multiple services must process the same message independently. Which AWS service is MOST appropriate?

A. Amazon SQS Standard Queue  
B. Amazon SNS  
C. Amazon Kinesis Data Streams  
D. AWS Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon SNS** (Simple Notification Service) provides pub/sub messaging pattern
- One message published → Multiple subscribers receive copy
- Push-based delivery (proactive)
- Perfect for fan-out scenarios

**SNS Architecture**:
```
Publisher (Microservice A)
      ↓
   SNS Topic
      ↓
   ┌──┴──┬──────┬──────┐
   ↓     ↓      ↓      ↓
Service B  C    D    Lambda
```

**SNS Features**:
- **Message Filtering**: Subscribers receive only relevant messages
- **Multiple Protocols**: SQS, Lambda, HTTP/HTTPS, Email, SMS, Mobile Push
- **Message Attributes**: Metadata for filtering
- **Fan-out**: 1-to-many delivery
- **FIFO Topics**: Ordered, exactly-once delivery

**SNS vs SQS**:

| Feature | SNS | SQS |
|---------|-----|-----|
| **Pattern** | Pub/Sub (1-to-many) | Queue (1-to-1) |
| **Delivery** | Push | Pull |
| **Subscribers** | Multiple (fan-out) | Single consumer per message |
| **Retention** | No retention | Up to 14 days |
| **Use Case** | Notifications, fan-out | Decoupling, buffering |

**Example Use Case**:
```
Order Placed Event → SNS Topic
  ├→ Inventory Service (update stock)
  ├→ Payment Service (charge customer)
  ├→ Shipping Service (create shipment)
  ├→ Email Service (send confirmation)
  └→ Analytics Service (track metrics)
```

**Message Filtering Example**:
```json
{
  "FilterPolicy": {
    "order_type": ["premium", "express"],
    "amount": [{"numeric": [">=", 100]}]
  }
}
```

**References:** Amazon SNS, Pub/Sub Messaging, Fan-out Pattern
</details>

---

### Question 2
An application needs to decouple components with message buffering. Messages must be processed exactly once in strict order. Which service should be used?

A. Amazon SQS Standard Queue  
B. Amazon SQS FIFO Queue  
C. Amazon SNS  
D. Amazon Kinesis Data Streams  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon SQS FIFO Queue** provides exactly-once processing with strict ordering
- Messages processed in the order received
- Content-based deduplication prevents duplicates
- Message groups enable parallel processing

**SQS Standard vs FIFO**:

| Feature | Standard | FIFO |
|---------|----------|------|
| **Ordering** | Best-effort | Guaranteed (FIFO) |
| **Delivery** | At-least-once | Exactly-once |
| **Throughput** | Unlimited | 300 msg/s (3000 batched) |
| **Deduplication** | No | Yes (5 min window) |
| **Use Case** | High throughput | Order critical |

**FIFO Queue Features**:

**1. Message Ordering**:
```
Send: A → B → C
Receive: A → B → C (always)
```

**2. Message Groups**:
- Multiple groups for parallel processing
- Order maintained within each group
- Different groups can process simultaneously

```python
# Send with message group
sqs.send_message(
    QueueUrl='https://sqs.../MyQueue.fifo',
    MessageBody='Order payment processed',
    MessageGroupId='order-12345',  # Group by order ID
    MessageDeduplicationId='payment-abc-123'
)
```

**3. Content-Based Deduplication**:
- SHA-256 hash of message body
- Automatic duplicate detection (5 minutes)
- Or use MessageDeduplicationId

**4. High Throughput Mode**:
- 3,000 messages per second with batching
- 9,000 TPS per group (with batching)

**FIFO Queue Naming**:
- Must end with `.fifo` suffix
- Example: `OrderQueue.fifo`

**Use Cases**:
- **Financial transactions**: No duplicate charges
- **Order processing**: Correct sequence
- **Command execution**: Sequential operations
- **Event sourcing**: Order matters

**Message Groups Example**:
```
Order Processing Queue.fifo
├─ Group: order-001 → Payment → Shipping → Confirmation
├─ Group: order-002 → Payment → Shipping → Confirmation
└─ Group: order-003 → Payment → Shipping → Confirmation

Each group processes in order, groups process in parallel
```

**Best Practices**:
1. Use message groups for parallelism
2. Enable content-based deduplication
3. Set appropriate visibility timeout
4. Use batch operations (10 messages per batch)
5. Monitor `ApproximateAgeOfOldestMessage`

**References:** Amazon SQS FIFO, Exactly-Once Processing, Message Ordering
</details>

---

### Question 3
A serverless application needs to process real-time streaming data from thousands of IoT devices. Each device sends data every second. Which service is MOST appropriate?

A. Amazon SQS  
B. Amazon SNS  
C. Amazon Kinesis Data Streams  
D. Amazon MQ  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon Kinesis Data Streams** designed for real-time streaming data
- Handles massive data ingestion from thousands of producers
- Multiple consumers can read same data stream
- Data retention (24 hours to 365 days)
- Ordered records per shard

**Kinesis Data Streams Architecture**:
```
IoT Devices (producers)
   ↓
Kinesis Stream (shards)
   ├→ Lambda (real-time processing)
   ├→ Kinesis Data Analytics (SQL queries)
   ├→ Kinesis Data Firehose (S3/Redshift)
   └→ Custom consumers (EC2, containers)
```

**Kinesis Key Concepts**:

**1. Shards**:
- Throughput unit
- 1 MB/s write, 2 MB/s read per shard
- 1,000 records/s write per shard
- Ordered within shard

**2. Records**:
- Partition key (determines shard)
- Sequence number (order within shard)
- Data blob (up to 1 MB)

**3. Consumers**:
- Multiple consumers can read same stream
- Enhanced fan-out (dedicated 2 MB/s per consumer)
- Shared throughput mode (2 MB/s total)

**Kinesis Features**:

| Feature | Description |
|---------|-------------|
| **Retention** | 24 hours default, up to 365 days |
| **Ordering** | Per partition key/shard |
| **Replay** | Can reprocess data |
| **Scaling** | Add/remove shards |
| **Encryption** | At rest (KMS), in transit (HTTPS) |

**Capacity Planning**:
```
Incoming Data: 1,000 devices × 1 KB/s = 1 MB/s
Required Shards: 1 MB/s ÷ 1 MB/s per shard = 1 shard

Incoming Data: 5,000 devices × 1 KB/s = 5 MB/s
Required Shards: 5 MB/s ÷ 1 MB/s per shard = 5 shards
```

**Kinesis Producer** (Python):
```python
import boto3
import json

kinesis = boto3.client('kinesis')

def send_iot_data(device_id, temperature, humidity):
    data = {
        'device_id': device_id,
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': int(time.time())
    }
    
    kinesis.put_record(
        StreamName='IoTDataStream',
        Data=json.dumps(data),
        PartitionKey=device_id  # Routes to specific shard
    )
```

**Kinesis Consumer** (Lambda):
```python
def lambda_handler(event, context):
    for record in event['Records']:
        # Kinesis data is base64 encoded
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        # Process IoT data
        device_id = data['device_id']
        temperature = data['temperature']
        
        # Alert if temperature too high
        if temperature > 80:
            send_alert(device_id, temperature)
```

**Kinesis Family**:

| Service | Use Case |
|---------|----------|
| **Data Streams** | Custom real-time processing |
| **Data Firehose** | Load to S3, Redshift, ES (easier) |
| **Data Analytics** | SQL on streaming data |
| **Video Streams** | Video ingestion and processing |

**Kinesis vs SQS**:

| Feature | Kinesis | SQS |
|---------|---------|-----|
| **Ordering** | Per shard | FIFO queue only |
| **Multiple Consumers** | Yes | No (fanout via SNS) |
| **Retention** | Up to 365 days | Up to 14 days |
| **Replay** | Yes | No |
| **Use Case** | Streaming, analytics | Decoupling, buffering |

**When to Use Kinesis**:
- Real-time analytics
- Log and event data collection
- IoT data ingestion
- Multiple consumers need same data
- Need to replay data
- Streaming ETL

**References:** Amazon Kinesis Data Streams, Real-Time Streaming, IoT Data Ingestion
</details>

---

### Question 4
A company wants to implement a fan-out pattern where an SNS message triggers multiple SQS queues for different services. What is this architecture called?

A. SQS Message Chaining  
B. SNS to SQS Fan-out  
C. Kinesis Fan-out  
D. EventBridge Routing  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **SNS to SQS Fan-out** is common pattern for parallel, asynchronous processing
- Single message to SNS triggers multiple SQS queues
- Each service consumes from its own queue
- Decoupled, resilient architecture

**SNS-SQS Fan-out Architecture**:
```
Event Source
     ↓
  SNS Topic
     ↓
  ┌──┴──┬────────┬────────┐
  ↓     ↓        ↓        ↓
SQS-1  SQS-2   SQS-3    SQS-4
  ↓     ↓        ↓        ↓
Svc-A  Svc-B   Svc-C    Svc-D
```

**Benefits**:

**1. Parallel Processing**:
- Services process independently
- No blocking between services

**2. Reliability**:
- SQS provides message persistence
- Retries on failure
- Dead Letter Queue for failed messages

**3. Scalability**:
- Each service scales independently
- Add new subscribers without changes

**4. Decoupling**:
- Services don't know about each other
- Add/remove services easily

**Configuration**:

**Step 1: Create SNS Topic**:
```bash
aws sns create-topic --name OrderEvents
```

**Step 2: Create SQS Queues**:
```bash
aws sqs create-queue --queue-name InventoryQueue
aws sqs create-queue --queue-name PaymentQueue
aws sqs create-queue --queue-name ShippingQueue
```

**Step 3: Subscribe Queues to Topic**:
```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:OrderEvents \
  --protocol sqs \
  --notification-endpoint arn:aws:sqs:us-east-1:123456789012:InventoryQueue
```

**Step 4: Update SQS Policy** (allow SNS to send):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "sns.amazonaws.com"},
    "Action": "SQS:SendMessage",
    "Resource": "arn:aws:sqs:us-east-1:123456789012:InventoryQueue",
    "Condition": {
      "ArnEquals": {
        "aws:SourceArn": "arn:aws:sns:us-east-1:123456789012:OrderEvents"
      }
    }
  }]
}
```

**Real-World Example - E-commerce Order**:

```
Customer Places Order
        ↓
  SNS: OrderPlaced
        ↓
  ┌─────┴─────┬──────────┬──────────┐
  ↓           ↓          ↓          ↓
Inventory  Payment  Shipping   Email
  Queue     Queue     Queue     Queue
  ↓           ↓          ↓          ↓
Update    Process   Create    Send
 Stock    Payment  Shipment   Conf.
```

**Message Filtering** (each service gets relevant messages only):
```json
{
  "InventoryQueue": {
    "FilterPolicy": {
      "order_type": ["physical_goods"]
    }
  },
  "EmailQueue": {
    "FilterPolicy": {
      "notification_type": ["order_confirmation"]
    }
  }
}
```

**Error Handling - Dead Letter Queue**:
```
SQS Queue → Process → Failure (after retries)
                            ↓
                     Dead Letter Queue
                            ↓
                    Alert/Manual Review
```

**Best Practices**:
1. Use message filtering to reduce unnecessary processing
2. Configure Dead Letter Queues for failed messages
3. Set appropriate visibility timeout
4. Use batching for cost optimization
5. Monitor queue depth (CloudWatch)
6. Implement idempotency in consumers

**SNS-SQS vs Kinesis**:
- **SNS-SQS**: Different processing per service
- **Kinesis**: Same data, different consumers

**References:** SNS to SQS Fan-out, Asynchronous Processing, Decoupling Patterns
</details>

---

### Question 5
A serverless workflow needs to coordinate multiple Lambda functions with conditional logic, parallel execution, and error handling. Which service should be used?

A. Amazon SQS with multiple queues  
B. Amazon SNS with message filtering  
C. AWS Step Functions  
D. Amazon EventBridge  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Step Functions** orchestrates serverless workflows
- Visual workflow designer
- Built-in error handling and retries
- Parallel execution, conditional logic, wait states
- Integration with 200+ AWS services

**Step Functions State Machine Example**:
```json
{
  "Comment": "Order Processing Workflow",
  "StartAt": "ValidateOrder",
  "States": {
    "ValidateOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:ValidateOrder",
      "Next": "CheckInventory",
      "Catch": [{
        "ErrorEquals": ["ValidationError"],
        "Next": "OrderFailed"
      }]
    },
    "CheckInventory": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:CheckInventory",
      "Next": "InventoryAvailable?"
    },
    "InventoryAvailable?": {
      "Type": "Choice",
      "Choices": [{
        "Variable": "$.inventoryAvailable",
        "BooleanEquals": true,
        "Next": "ParallelProcessing"
      }],
      "Default": "OutOfStock"
    },
    "ParallelProcessing": {
      "Type": "Parallel",
      "Branches": [
        {
          "StartAt": "ProcessPayment",
          "States": {
            "ProcessPayment": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:...:function:ProcessPayment",
              "End": true
            }
          }
        },
        {
          "StartAt": "ReserveInventory",
          "States": {
            "ReserveInventory": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:...:function:ReserveInventory",
              "End": true
            }
          }
        },
        {
          "StartAt": "SendConfirmation",
          "States": {
            "SendConfirmation": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:...:function:SendEmail",
              "End": true
            }
          }
        }
      ],
      "Next": "CreateShipment"
    },
    "CreateShipment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:CreateShipment",
      "End": true
    },
    "OutOfStock": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:...:function:NotifyOutOfStock",
      "End": true
    },
    "OrderFailed": {
      "Type": "Fail",
      "Error": "OrderValidationFailed",
      "Cause": "Order validation failed"
    }
  }
}
```

**Step Functions State Types**:

| State Type | Purpose | Example |
|------------|---------|---------|
| **Task** | Execute work (Lambda, ECS, SNS, etc.) | Call API, process data |
| **Choice** | Conditional logic (if/else) | Check inventory status |
| **Parallel** | Execute branches simultaneously | Payment + Inventory + Email |
| **Wait** | Delay (seconds, timestamp) | Wait for approval |
| **Pass** | Pass input to output, transform | Data transformation |
| **Map** | Iterate over array | Process batch items |
| **Succeed** | Successful termination | Order complete |
| **Fail** | Failed termination | Validation failed |

**Error Handling**:

**1. Retry**:
```json
{
  "Retry": [{
    "ErrorEquals": ["States.TaskFailed"],
    "IntervalSeconds": 2,
    "MaxAttempts": 3,
    "BackoffRate": 2.0
  }]
}
```

**2. Catch**:
```json
{
  "Catch": [{
    "ErrorEquals": ["PaymentFailed"],
    "Next": "RefundAndCancel"
  }]
}
```

**Step Functions Workflow Types**:

| Type | Duration | Execution Rate | Use Case |
|------|----------|----------------|----------|
| **Standard** | Up to 1 year | 2,000/s | Long-running, exactly-once |
| **Express** | Up to 5 min | 100,000/s | High-volume, at-least-once |

**Integration with AWS Services**:
- **Lambda**: Execute functions
- **ECS/Fargate**: Run containers
- **DynamoDB**: Read/write data
- **SNS/SQS**: Send messages
- **Glue**: Run ETL jobs
- **SageMaker**: ML training/inference
- **Batch**: Run batch jobs

**Step Functions vs Alternatives**:

| Tool | Best For |
|------|----------|
| **Step Functions** | Complex workflows, orchestration |
| **Lambda** | Single tasks |
| **SQS** | Queue-based processing |
| **EventBridge** | Event routing |

**Real-World Use Cases**:
1. **ETL Pipelines**: Extract → Transform → Load
2. **Order Processing**: Validate → Payment → Fulfillment
3. **Video Processing**: Upload → Transcode → Thumbnail → Delivery
4. **Machine Learning**: Data prep → Training → Deploy → Monitor
5. **Approval Workflows**: Submit → Review → Approve/Reject → Execute

**Visual Workflow Benefits**:
- Easy to understand complex logic
- Debug with execution history
- See exactly where failures occur
- Modify without code changes (drag-and-drop)

**Best Practices**:
1. Use Express Workflows for high-volume, short-duration
2. Implement error handling at each step
3. Use Parallel states for independent tasks
4. Monitor with CloudWatch metrics
5. Use input/output filtering to manage data size
6. Implement idempotency in Lambda functions

**References:** AWS Step Functions, Serverless Orchestration, Workflow Management
</details>

---

### Question 6
An application needs to load streaming data into S3, Redshift, and Elasticsearch with minimal code. Which service is MOST appropriate?

A. Amazon Kinesis Data Streams with custom consumers  
B. Amazon Kinesis Data Firehose  
C. AWS Lambda triggered by Kinesis  
D. Amazon SQS with Lambda consumers  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon Kinesis Data Firehose** is fully managed service for loading streaming data
- No code required (vs Data Streams which needs custom consumers)
- Automatic scaling
- Built-in data transformation (Lambda)
- Direct delivery to S3, Redshift, Elasticsearch, HTTP endpoints

**Kinesis Data Firehose Architecture**:
```
Data Producers
  ├─ Applications
  ├─ IoT Devices
  ├─ Clickstream
  └─ Logs
       ↓
Kinesis Data Firehose
  ├─ Optional: Lambda transformation
  ├─ Optional: Format conversion (Parquet, ORC)
  └─ Buffering (size/time)
       ↓
Destinations
  ├─ Amazon S3
  ├─ Amazon Redshift (via S3)
  ├─ Amazon Elasticsearch
  ├─ Splunk
  └─ HTTP endpoints
```

**Firehose Features**:

**1. Automatic Scaling**:
- No capacity planning
- Scales to gigabytes per second
- Pay for data volume

**2. Buffering**:
- Buffer by size (1-128 MB)
- Buffer by time (60-900 seconds)
- Delivers when either threshold met

**3. Data Transformation**:
- Lambda function processes each record
- Format conversion (JSON to Parquet/ORC)
- Compression (GZIP, ZIP, Snappy)

**4. Backup**:
- Backup source data to S3
- Failed records to separate S3 prefix

**Firehose Delivery Configuration**:
```json
{
  "DeliveryStreamName": "WebLogsToS3",
  "S3DestinationConfiguration": {
    "RoleARN": "arn:aws:iam::123456789012:role/FirehoseRole",
    "BucketARN": "arn:aws:s3:::my-logs-bucket",
    "Prefix": "logs/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/",
    "BufferingHints": {
      "SizeInMBs": 5,
      "IntervalInSeconds": 300
    },
    "CompressionFormat": "GZIP",
    "CloudWatchLoggingOptions": {
      "Enabled": true,
      "LogGroupName": "/aws/kinesisfirehose/WebLogs"
    }
  },
  "ProcessingConfiguration": {
    "Enabled": true,
    "Processors": [{
      "Type": "Lambda",
      "Parameters": [{
        "ParameterName": "LambdaArn",
        "ParameterValue": "arn:aws:lambda:...:function:TransformLogs"
      }]
    }]
  }
}
```

**Data Transformation Example** (Lambda):
```python
import base64
import json

def lambda_handler(event, context):
    output = []
    
    for record in event['records']:
        # Decode input data
        payload = base64.b64decode(record['data']).decode('utf-8')
        data = json.loads(payload)
        
        # Transform data
        transformed = {
            'timestamp': data['timestamp'],
            'user_id': data['user_id'],
            'event_type': data['event_type'],
            'country': data.get('country', 'UNKNOWN')
        }
        
        # Encode output
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(
                json.dumps(transformed).encode('utf-8')
            ).decode('utf-8')
        }
        output.append(output_record)
    
    return {'records': output}
```

**Delivery Destinations**:

**1. Amazon S3**:
- Object storage
- Data lake
- Archive
- Partitioning by time

**2. Amazon Redshift**:
- Data warehouse
- Analytics
- Data via S3 COPY command

**3. Amazon Elasticsearch**:
- Search and analytics
- Log analysis
- Real-time dashboards

**4. Splunk**:
- Security monitoring
- Operational intelligence

**5. HTTP Endpoints**:
- Custom destinations
- Third-party services

**Firehose vs Data Streams**:

| Feature | Data Firehose | Data Streams |
|---------|---------------|--------------|
| **Management** | Fully managed | Manage shards |
| **Destinations** | Built-in (S3, Redshift, ES) | Custom code |
| **Scaling** | Automatic | Manual shard management |
| **Retention** | No retention | 24h to 365 days |
| **Consumers** | One (delivery) | Multiple possible |
| **Use Case** | Load to destinations | Custom processing |

**Cost Comparison**:
```
Data Firehose: $0.029/GB + destination costs
Data Streams: $0.015/shard/hour + $0.014/million PUT units
```

**When to Use Firehose**:
- Load data to S3, Redshift, ES, Splunk
- Don't need multiple consumers
- Want fully managed solution
- Near real-time (60+ seconds latency)
- Simple transformations

**When to Use Data Streams**:
- Need real-time processing (< 1 second)
- Multiple consumers
- Custom processing logic
- Need to replay data
- Order matters within shard

**Real-World Examples**:

**1. Clickstream Analytics**:
```
Website → Firehose → S3 (Parquet) → Athena/QuickSight
```

**2. Log Aggregation**:
```
Applications → Firehose → Elasticsearch → Kibana
```

**3. Data Lake**:
```
IoT Devices → Firehose → S3 (partitioned) → Glue → Athena
```

**Best Practices**:
1. Use buffering to optimize cost (batch writes)
2. Enable S3 backup for source records
3. Use compression (GZIP) to reduce storage costs
4. Convert to columnar formats (Parquet/ORC) for analytics
5. Partition S3 data by time for better query performance
6. Monitor delivery to CloudWatch

**References:** Amazon Kinesis Data Firehose, Streaming Data Delivery, Data Lake
</details>

---

### Question 7
A company wants to route events from multiple AWS services to different targets based on event content. Which service provides centralized event routing?

A. Amazon SNS  
B. Amazon SQS  
C. Amazon EventBridge  
D. AWS Step Functions  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon EventBridge** is serverless event bus for application and AWS service events
- Content-based routing using event patterns
- 100+ AWS service integrations as event sources
- 20+ AWS services as targets

**EventBridge Architecture**:
```
Event Sources
├─ AWS Services (EC2, S3, Lambda, etc.)
├─ Custom Applications
├─ SaaS Partners (Salesforce, Datadog, etc.)
       ↓
   EventBridge Bus
       ↓
   Event Rules (filtering)
       ↓
   Targets
   ├─ Lambda
   ├─ Step Functions
   ├─ SQS
   ├─ SNS
   ├─ Kinesis
   └─ API Gateway
```

**EventBridge Components**:

**1. Events**:
```json
{
  "version": "0",
  "id": "event-id",
  "detail-type": "EC2 Instance State-change Notification",
  "source": "aws.ec2",
  "account": "123456789012",
  "time": "2026-01-03T12:00:00Z",
  "region": "us-east-1",
  "resources": ["arn:aws:ec2:us-east-1:123456789012:instance/i-0123456789"],
  "detail": {
    "instance-id": "i-0123456789",
    "state": "running"
  }
}
```

**2. Event Rules** (pattern matching):
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["terminated"]
  }
}
```

**3. Event Buses**:
- **Default**: AWS service events
- **Custom**: Application events
- **Partner**: SaaS provider events

**4. Targets**:
- Multiple targets per rule (up to 5)
- Input transformation
- Retry policies

**Real-World Examples**:

**Example 1: Security Automation**
```json
{
  "EventPattern": {
    "source": ["aws.guardduty"],
    "detail-type": ["GuardDuty Finding"],
    "detail": {
      "severity": [7, 8, 9]  // High and Critical
    }
  },
  "Targets": [
    {
      "Arn": "arn:aws:lambda:...:function:IsolateInstance",
      "Id": "1"
    },
    {
      "Arn": "arn:aws:sns:...:SecurityAlerts",
      "Id": "2"
    }
  ]
}
```

**Example 2: Multi-Account Event Aggregation**
```
Production Account Events
       ↓
 EventBridge Rule
       ↓
Cross-Account Event Bus (Security Account)
       ↓
Centralized Monitoring/Alerting
```

**Example 3: Scheduled Events** (cron/rate):
```json
{
  "ScheduleExpression": "rate(5 minutes)",
  "Targets": [{
    "Arn": "arn:aws:lambda:...:function:HealthCheck",
    "Id": "1"
  }]
}

// Or cron syntax
{
  "ScheduleExpression": "cron(0 12 * * ? *)",  // Noon daily
  "Targets": [{
    "Arn": "arn:aws:lambda:...:function:DailyReport",
    "Id": "1"
  }]
}
```

**EventBridge Features**:

**1. Content-Based Filtering**:
- Match specific event attributes
- Numeric matching (>, <, >=, <=, range)
- Prefix matching
- Exists checking
- IP address matching

**2. Input Transformation**:
```json
{
  "InputTransformer": {
    "InputPathsMap": {
      "instance": "$.detail.instance-id",
      "state": "$.detail.state"
    },
    "InputTemplate": "\"Instance <instance> is now <state>\""
  }
}
```

**3. Dead Letter Queue**:
- Failed invocations sent to DLQ
- Retry configuration
- Maximum age and retry attempts

**4. Archive and Replay**:
- Archive events for retention
- Replay events for testing/recovery

**EventBridge vs SNS vs SQS**:

| Feature | EventBridge | SNS | SQS |
|---------|-------------|-----|-----|
| **Pattern** | Event routing | Pub/Sub | Queue |
| **Filtering** | Advanced (content-based) | Basic (attributes) | No filtering |
| **Sources** | 100+ AWS services | Applications | Applications |
| **Targets** | 20+ AWS services | Limited | Consumers |
| **Scheduling** | Built-in (cron) | No | No |
| **Use Case** | Event-driven architecture | Fan-out notifications | Decoupling |

**Advanced Pattern Examples**:

**IP Address Matching**:
```json
{
  "detail": {
    "sourceIPAddress": [{
      "cidr": "10.0.0.0/8"
    }]
  }
}
```

**Numeric Matching**:
```json
{
  "detail": {
    "temperature": [{
      "numeric": [">", 80]
    }]
  }
}
```

**Anything-but**:
```json
{
  "detail": {
    "state": [{
      "anything-but": ["running", "stopped"]
    }]
  }
}
```

**Common Use Cases**:
1. **Security Automation**:
- GuardDuty findings → Lambda → Isolate instance
- Config non-compliance → SNS → Alert

2. **Application Integration**:
- Custom app events → EventBridge → Trigger workflows
- SaaS webhooks → EventBridge → Process data

3. **Scheduled Tasks**:
- Daily reports
- Periodic cleanup
- Health checks

4. **Cross-Account Event Aggregation**:
- Multiple accounts → Central event bus
- Centralized monitoring

5. **Event Replay**:
- Archive production events
- Replay for testing
- Disaster recovery

**Best Practices**:
1. Use content-based filtering to reduce target invocations
2. Implement dead letter queues for failed events
3. Archive critical events for replay
4. Use cross-account event buses for multi-account architectures
5. Monitor rule metrics in CloudWatch
6. Use input transformers to send only needed data

**References:** Amazon EventBridge, Event-Driven Architecture, Serverless Integration
</details>

---

### Question 8
A legacy application uses Java Message Service (JMS) API. What is the BEST AWS migration path with minimal code changes?

A. Migrate to Amazon SQS  
B. Migrate to Amazon SNS  
C. Migrate to Amazon MQ  
D. Rewrite using Kinesis  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon MQ** is managed message broker for Apache ActiveMQ and RabbitMQ
- JMS, AMQP, MQTT, OpenWire, STOMP protocols
- Minimal code changes for lift-and-shift
- Compatible with existing messaging APIs

**Amazon MQ vs SQS/SNS**:

| Feature | Amazon MQ | SQS/SNS |
|---------|-----------|---------|
| **Protocols** | JMS, AMQP, MQTT, STOMP | AWS API only |
| **Migration** | Minimal code changes | Requires code changes |
| **Use Case** | Legacy app migration | Cloud-native apps |
| **Scaling** | Limited | Highly scalable |
| **Management** | Managed broker | Fully serverless |
| **Cost** | Instance-based | Pay per use |

**Amazon MQ Deployment**:
```
Applications (JMS/AMQP)
      ↓
Amazon MQ Broker
├─ Active/Standby (Multi-AZ)
├─ Apache ActiveMQ or RabbitMQ
├─ Persistent storage (EBS/EFS)
└─ Built-in monitoring
```

**Amazon MQ Features**:

**1. Broker Engines**:
- **ActiveMQ**: JMS, OpenWire, STOMP, MQTT, WSS
- **RabbitMQ**: AMQP 0-9-1, MQTT, STOMP

**2. High Availability**:
- Active/Standby deployment (Multi-AZ)
- Automatic failover
- Durable message storage

**3. Network Connectivity**:
- VPC deployment
- Private connectivity
- Security groups

**4. Authentication**:
- Simple authentication
- LDAP integration

**Migration Strategy**:

**Before (On-Premises)**:
```java
// Existing JMS code
ConnectionFactory factory = new ActiveMQConnectionFactory(
    "tcp://on-prem-broker:61616"
);
Connection connection = factory.createConnection();
Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
Queue queue = session.createQueue("OrderQueue");
MessageProducer producer = session.createProducer(queue);
```

**After (Amazon MQ)** - Minimal changes:
```java
// Just change broker endpoint
ConnectionFactory factory = new ActiveMQConnectionFactory(
    "ssl://b-xxx-yyy.mq.us-east-1.amazonaws.com:61617"
);
// Rest of the code remains the same
Connection connection = factory.createConnection("username", "password");
Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
Queue queue = session.createQueue("OrderQueue");
MessageProducer producer = session.createProducer(queue);
```

**When to Use Amazon MQ**:
- Migrating from on-premises message brokers
- Existing applications using JMS, AMQP
- Need protocol compatibility
- Complex message routing
- Message selectors and filters

**When to Use SQS/SNS**:
- Cloud-native applications
- Need massive scale
- Serverless architecture
- Cost optimization
- Can rewrite code

**Amazon MQ Configuration**:
```json
{
  "BrokerName": "ProductionBroker",
  "EngineType": "ActiveMQ",
  "EngineVersion": "5.16.5",
  "DeploymentMode": "ACTIVE_STANDBY_MULTI_AZ",
  "HostInstanceType": "mq.m5.large",
  "PubliclyAccessible": false,
  "SecurityGroups": ["sg-12345"],
  "SubnetIds": ["subnet-1", "subnet-2"],
  "Users": [{
    "Username": "admin",
    "Password": "SecurePassword123!",
    "ConsoleAccess": true
  }],
  "MaintenanceWindowStartTime": {
    "DayOfWeek": "MONDAY",
    "TimeOfDay": "03:00",
    "TimeZone": "America/New_York"
  }
}
```

**Cost Comparison**:

**Amazon MQ**:
- Instance costs (hourly)
- Storage costs (EBS/EFS)
- Data transfer

**SQS/SNS**:
- Per request
- No instance costs
- Generally cheaper at scale

**Best Practices**:
1. Use Multi-AZ for production
2. Configure automatic minor version upgrades
3. Enable CloudWatch logging
4. Use VPC endpoints for secure access
5. Implement message selectors for filtering
6. Monitor broker metrics

**References:** Amazon MQ, Message Brokers, JMS Migration
</details>

---

### Question 9
An application publishes custom metrics to CloudWatch. These metrics should trigger automated responses. What is the BEST approach?

A. Poll CloudWatch API periodically  
B. Use CloudWatch Alarms with SNS  
C. Use EventBridge rule for CloudWatch events  
D. Use Lambda to check metrics  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **CloudWatch Alarms** monitor metrics and trigger actions automatically
- SNS integration for notifications and automated responses
- Can trigger Auto Scaling, EC2 actions, SNS, Systems Manager

**CloudWatch Alarms Architecture**:
```
Custom Application
       ↓
CloudWatch Custom Metrics
       ↓
CloudWatch Alarm (threshold)
       ↓
SNS Topic
  ├→ Email notifications
  ├→ Lambda (automated remediation)
  ├→ SQS (queue for processing)
  └→ Auto Scaling (scale up/down)
```

**CloudWatch Alarm States**:
- **OK**: Metric within threshold
- **ALARM**: Metric breached threshold
- **INSUFFICIENT_DATA**: Not enough data

**Alarm Configuration**:
```python
import boto3

cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='HighCPUUtilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=300,  # 5 minutes
    Statistic='Average',
    Threshold=80.0,
    ActionsEnabled=True,
    AlarmActions=[
        'arn:aws:sns:us-east-1:123456789012:AlertTopic',
        'arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:...'
    ],
    AlarmDescription='Alert when CPU exceeds 80%',
    Dimensions=[{
        'Name': 'InstanceId',
        'Value': 'i-1234567890abcdef0'
    }]
)
```

**Custom Metrics Example**:
```python
# Publish custom metric
cloudwatch.put_metric_data(
    Namespace='MyApp/Orders',
    MetricData=[{
        'MetricName': 'OrdersProcessed',
        'Value': 150,
        'Unit': 'Count',
        'Timestamp': datetime.datetime.utcnow(),
        'Dimensions': [{
            'Name': 'Environment',
            'Value': 'Production'
        }]
    }]
)

# Create alarm on custom metric
cloudwatch.put_metric_alarm(
    AlarmName='LowOrderProcessing',
    ComparisonOperator='LessThanThreshold',
    EvaluationPeriods=1,
    MetricName='OrdersProcessed',
    Namespace='MyApp/Orders',
    Period=60,
    Statistic='Sum',
    Threshold=100.0,
    ActionsEnabled=True,
    AlarmActions=['arn:aws:sns:...'],
    Dimensions=[{
        'Name': 'Environment',
        'Value': 'Production'
    }]
)
```

**Alarm Actions**:

**1. SNS Notifications**:
```
Alarm → SNS → Email/SMS/Lambda/HTTP
```

**2. Auto Scaling**:
```
Alarm → Auto Scaling Policy → Scale EC2/ECS
```

**3. EC2 Actions**:
```
Alarm → Stop/Terminate/Reboot Instance
```

**4. Systems Manager Actions**:
```
Alarm → SSM Automation → Run playbook
```

**Automated Response Example** (Lambda):
```python
def lambda_handler(event, context):
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    alarm_name = message['AlarmName']
    new_state = message['NewStateValue']
    reason = message['NewStateReason']
    
    if new_state == 'ALARM':
        # Automated remediation
        if 'HighCPU' in alarm_name:
            scale_up_instances()
        elif 'LowOrders' in alarm_name:
            investigate_issue()
            send_alert_to_team()
```

**Composite Alarms** (multiple conditions):
```python
cloudwatch.put_composite_alarm(
    AlarmName='CriticalSystemHealth',
    AlarmRule='(ALARM(HighCPU) OR ALARM(HighMemory)) AND ALARM(HighErrorRate)',
    ActionsEnabled=True,
    AlarmActions=['arn:aws:sns:...']
)
```

**Alarm Statistics**:
- **Average**: Mean value
- **Sum**: Total
- **Minimum**: Lowest value
- **Maximum**: Highest value
- **SampleCount**: Number of data points
- **p99**: 99th percentile

**Best Practices**:
1. Use meaningful alarm names
2. Set appropriate evaluation periods (avoid flapping)
3. Use composite alarms for complex conditions
4. Test alarms with CloudWatch Alarm Testing
5. Document alarm thresholds
6. Review and adjust thresholds regularly

**CloudWatch Alarms vs EventBridge**:
- **Alarms**: Metric-based thresholds
- **EventBridge**: Event-driven (state changes, API calls)

**References:** CloudWatch Alarms, Automated Monitoring, Metric-Based Actions
</details>

---

### Question 10
A company wants to implement API Gateway to trigger different Lambda functions based on the API path. What feature enables this?

A. API Gateway Stages  
B. API Gateway Methods  
C. API Gateway Resources with Lambda Integration  
D. API Gateway Authorizers  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **API Gateway Resources** define API paths
- Each resource/method can integrate with different Lambda functions
- Enables REST API routing to microservices

**API Gateway Lambda Integration**:
```
GET /users → Lambda: ListUsers
POST /users → Lambda: CreateUser
GET /users/{id} → Lambda: GetUser
PUT /users/{id} → Lambda: UpdateUser
DELETE /users/{id} → Lambda: DeleteUser
```

**API Gateway Structure**:
```
REST API: UserService
├─ /users (Resource)
│  ├─ GET (Method) → Lambda: ListUsers
│  ├─ POST (Method) → Lambda: CreateUser
│  └─ /{id} (Resource)
│     ├─ GET (Method) → Lambda: GetUser
│     ├─ PUT (Method) → Lambda: UpdateUser
│     └─ DELETE (Method) → Lambda: DeleteUser
└─ /orders (Resource)
   ├─ GET → Lambda: ListOrders
   └─ POST → Lambda: CreateOrder
```

**API Gateway Integration Types**:

| Type | Use Case |
|------|----------|
| **Lambda** | Serverless backend |
| **HTTP** | HTTP endpoints |
| **AWS Service** | Direct AWS service integration |
| **Mock** | Testing, return fixed response |
| **VPC Link** | Private VPC resources |

**Lambda Integration Configuration**:
```json
{
  "httpMethod": "POST",
  "type": "AWS_PROXY",  // Lambda proxy integration
  "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:CreateUser/invocations",
  "credentials": "arn:aws:iam::123456789012:role/APIGatewayLambdaRole",
  "requestTemplates": {
    "application/json": "{\"body\": $input.json('$')}"
  }
}
```

**Lambda Proxy Integration** (recommended):
```python
def lambda_handler(event, context):
    # event contains full request details
    path = event['path']  # /users/123
    method = event['httpMethod']  # GET
    headers = event['headers']
    query_params = event['queryStringParameters']
    body = json.loads(event['body']) if event['body'] else {}
    
    # Process request
    if path == '/users' and method == 'GET':
        users = get_all_users()
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(users)
        }
```

**API Gateway Features**:

**1. Request Validation**:
- Validate request parameters
- Validate request body against JSON schema
- Reject invalid requests before invoking Lambda

**2. Request/Response Transformation**:
- Transform request data
- Map response from Lambda
- Change content types

**3. Throttling**:
- Rate limiting (requests per second)
- Burst capacity
- Per-client throttling (API keys)

**4. Caching**:
- Cache responses at API Gateway
- Reduce Lambda invocations
- Configurable TTL

**5. CORS Support**:
- Enable cross-origin requests
- Configure allowed origins, headers, methods

**6. Authentication/Authorization**:
- AWS IAM
- Cognito User Pools
- Lambda Authorizers
- API Keys

**API Gateway Stages**:
```
API: UserService
├─ dev (Stage)
│  └─ https://api.example.com/dev/users
├─ test (Stage)
│  └─ https://api.example.com/test/users
└─ prod (Stage)
   └─ https://api.example.com/prod/users
```

**Stage Variables** (environment-specific):
```json
{
  "stageVariables": {
    "lambdaAlias": "prod",
    "dbEndpoint": "prod-db.example.com"
  }
}

// Use in integration
{
  "uri": "arn:aws:lambda:...:function:MyFunction:${stageVariables.lambdaAlias}"
}
```

**API Gateway Deployment**:
```bash
# Deploy to stage
aws apigateway create-deployment \
  --rest-api-id abc123 \
  --stage-name prod \
  --stage-description 'Production deployment' \
  --description 'Release v1.2.3'
```

**Best Practices**:
1. Use Lambda proxy integration for simplicity
2. Enable request validation
3. Use stages for environments (dev/test/prod)
4. Enable caching for read-heavy APIs
5. Implement authentication/authorization
6. Enable CloudWatch logging
7. Use custom domain names
8. Implement rate limiting
9. Version your APIs
10. Monitor with X-Ray

**API Gateway Pricing**:
- REST API: $3.50 per million requests
- HTTP API: $1.00 per million requests (cheaper)
- WebSocket API: $1.00 per million messages
- Data transfer out

**HTTP API vs REST API**:
- **HTTP API**: Simpler, cheaper, faster
- **REST API**: More features (request validation, caching, API keys)

**References:** API Gateway, Lambda Integration, REST API Routing
</details>

---

### Question 41
A SaaS company needs to automate the transfer of customer data from Salesforce to Amazon S3 for analytics. The solution must be fully managed and require minimal code. Which AWS service should be used?

A. Amazon AppFlow  
B. AWS Glue  
C. Amazon Kinesis Data Firehose  
D. AWS DataSync  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon AppFlow is a fully managed integration service
- Automates data transfer between SaaS apps (e.g., Salesforce) and AWS
- No code required, supports scheduling and transformation
- Glue is for ETL, not direct SaaS integration
- Firehose is for streaming, not SaaS connectors
- DataSync is for file transfers, not SaaS data

**References:** Amazon AppFlow, SaaS Integration
</details>

---

### Question 42
A development team is building a GraphQL API for a mobile app and wants to minimize backend management. Which AWS service should they use?

A. AWS AppSync  
B. Amazon API Gateway  
C. AWS Lambda  
D. Amazon Cognito  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS AppSync is a managed GraphQL API service
- Handles real-time data sync, subscriptions, and offline access
- API Gateway is for REST/HTTP APIs
- Lambda is compute, not API management
- Cognito is for authentication, not APIs

**References:** AWS AppSync, GraphQL APIs
</details>

---

### Question 43
A company needs to deploy containerized workloads to on-premises servers and manage them using AWS services. Which solution should they use?

A. Amazon ECS Anywhere  
B. Amazon EKS Anywhere  
C. AWS Outposts  
D. AWS Fargate  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- ECS Anywhere extends ECS to on-premises servers
- Centralized management from AWS Console
- EKS Anywhere is for Kubernetes, not ECS
- Outposts is for running AWS infrastructure on-premises
- Fargate is serverless containers in AWS only

**References:** Amazon ECS Anywhere, Hybrid Deployments
</details>

---

### Question 44
A mobile development team wants to test their app on a wide range of real devices in the cloud. Which AWS service should they use?

A. AWS Device Farm  
B. AWS Amplify  
C. Amazon Pinpoint  
D. Amazon API Gateway  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- AWS Device Farm provides cloud-based testing on real mobile devices
- Supports Android and iOS
- Automates testing and provides detailed reports
- Amplify is for app development and hosting
- Pinpoint is for user engagement, not testing
- API Gateway is for APIs, not device testing

**References:** AWS Device Farm, Mobile Testing
</details>

---

### Question 45
A marketing team wants to send targeted push notifications, emails, and SMS messages to users based on their behavior in a mobile app. Which AWS service should be used?

A. Amazon Pinpoint  
B. Amazon SNS  
C. AWS Amplify  
D. Amazon SQS  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon Pinpoint is a multi-channel marketing and analytics service
- Supports push, email, SMS, and in-app messaging
- Provides segmentation, analytics, and campaign management
- SNS is for basic notifications, not targeted campaigns
- Amplify is for app development, not marketing
- SQS is for queuing, not messaging users

**References:** Amazon Pinpoint, User Engagement
</details>

---

### Question 46
A company needs to integrate its on-premises Apache Kafka workloads with AWS analytics and storage services. Which AWS service provides a fully managed, highly available Kafka environment?

A. Amazon MSK  
B. Amazon Kinesis Data Streams  
C. Amazon SQS  
D. AWS Glue Streaming  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Amazon MSK (Managed Streaming for Apache Kafka) provides a fully managed Kafka service
- Handles provisioning, patching, and scaling
- Integrates with Kinesis, Lambda, S3, Redshift
- Kinesis is a separate streaming service, not Kafka-compatible
- SQS is for message queuing, not streaming
- Glue Streaming is for ETL, not Kafka management

**References:** Amazon MSK, Streaming Data
</details>

---

## Summary

**Total Questions**: 46  
**Topics Covered**:
- Amazon SNS (Pub/Sub, Fan-out)
- Amazon SQS (Standard vs FIFO Queues)
- Amazon Kinesis (Data Streams, Data Firehose)
- SNS-SQS Fan-out Pattern
- AWS Step Functions (Workflow Orchestration)
- Amazon EventBridge (Event Routing)
- Amazon MQ (Message Broker Migration)
- CloudWatch Alarms (Metric-Based Triggers)
- API Gateway (Lambda Integration)
- Amazon AppFlow (SaaS Integration)
- AWS AppSync (GraphQL APIs)
- Amazon ECS Anywhere (Hybrid Container Deployment)
- AWS Device Farm (Mobile Testing)
- Amazon Pinpoint (User Engagement)
- Amazon MSK (Managed Kafka)

**Exam Tips**:

**Messaging Patterns**:
- **1-to-Many (Fan-out)**: SNS or EventBridge
- **1-to-1 (Queue)**: SQS
- **Exactly-once, Ordered**: SQS FIFO
- **Real-time Streaming**: Kinesis Data Streams
- **Load to Destinations**: Kinesis Data Firehose

**SQS**:
- **Standard**: Unlimited throughput, at-least-once, best-effort ordering
- **FIFO**: 300 msg/s (3000 batched), exactly-once, ordered

**SNS-SQS Fan-out**:
- Multiple services process same event independently
- Reliable, scalable, decoupled

**Kinesis**:
- **Data Streams**: Custom processing, multiple consumers, replay
- **Data Firehose**: Managed delivery to S3, Redshift, ES

**Step Functions**:
- Orchestrate complex workflows
- Visual designer
- Error handling, retries, parallel execution

**EventBridge**:
- Event-driven architecture
- Content-based routing
- 100+ AWS services as sources
- Scheduled events (cron)

**Amazon MQ**:
- JMS/AMQP migration
- Minimal code changes
- Not for greenfield (use SQS/SNS instead)

**CloudWatch Alarms**:
- Metric-based triggers
- SNS integration for notifications
- Auto Scaling integration

**API Gateway**:
- REST, HTTP, WebSocket APIs
- Lambda proxy integration (recommended)
- Stages for environments
- Built-in authentication, throttling, caching

**AppFlow**:
- SaaS data integration (e.g., Salesforce to S3)
- Fully managed, no code

**AppSync**:
- Managed GraphQL APIs
- Real-time data sync, subscriptions

**ECS Anywhere**:
- Deploy containers to on-premises
- Manage with AWS services

**Device Farm**:
- Test mobile apps on real devices
- Cloud-based, wide range of devices

**Pinpoint**:
- Targeted push notifications, emails, SMS
- User behavior analytics

**MSK**:
- Managed Kafka service
- Integrates with AWS analytics and storage

**Service Selection**:
```
Need                          → Use
─────────────────────────────────────────
Fan-out (same message, many services) → SNS
Queue (decouple, buffer)               → SQS
Exactly-once, ordered                  → SQS FIFO
Real-time stream processing            → Kinesis Data Streams
Load stream to S3/Redshift/ES         → Kinesis Data Firehose
Complex workflows                      → Step Functions
Event routing (AWS services)           → EventBridge
JMS/AMQP migration                    → Amazon MQ
Metric-based automation               → CloudWatch Alarms
REST API for Lambda                   → API Gateway
SaaS data integration                  → AppFlow
GraphQL API                           → AppSync
Hybrid container deployment            → ECS Anywhere
Mobile app testing                    → Device Farm
Targeted user messaging                → Pinpoint
Managed Kafka                          → MSK
```

**Next Steps**:
- Understand when to use each messaging service
- Practice building SNS-SQS fan-out patterns
- Learn Step Functions state types
- Know EventBridge vs SNS differences
- Understand SQS Standard vs FIFO trade-offs

