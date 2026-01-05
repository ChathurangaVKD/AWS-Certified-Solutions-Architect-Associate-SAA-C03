# 08: Application Integration - Ultra Fast Learning 🚀

## SQS (Simple Queue Service)

### SQS Basics
- **Message queue** for decoupling
- **Unlimited** throughput and messages
- **Retention**: 1 min to 14 days (default 4 days)
- **Low latency**: <10 ms
- **Max message size**: 256 KB

### Queue Types
| Feature | Standard | FIFO |
|---------|----------|------|
| Throughput | Unlimited | 300 msg/s (3K with batch) |
| Ordering | Best-effort | Strict order |
| Delivery | At-least-once | Exactly-once |
| Name | Any | Must end in `.fifo` |

### SQS Features
- **Visibility Timeout**: 30 sec default (max 12 hr), message invisible after receive
- **Long Polling**: Wait for messages (1-20 sec), reduce API calls
- **DLQ (Dead Letter Queue)**: Send failed messages after max receives
- **Message Delay**: 0-15 min (delay queue or per message)

## SNS (Simple Notification Service)

### SNS Basics
- **Pub/Sub** messaging
- **1 topic** → **many subscribers**
- **Push-based** (not pull)
- **100K topics** per account

### SNS Subscribers
- SQS, Lambda, HTTP/HTTPS, Email, SMS, Mobile push
- **Kinesis Data Firehose**

### SNS Features
- **Fan-out**: SNS → multiple SQS queues
- **Message filtering**: Subscribers filter by attributes
- **Message attributes**: Metadata (not part of body)
- **FIFO Topics**: Order + deduplication (with SQS FIFO)

## SNS + SQS Fan-out Pattern
```
Application → SNS Topic → [SQS Queue 1, SQS Queue 2, Lambda]
```
- **Use case**: Same message to multiple services
- **Benefits**: Decoupling, parallel processing

## EventBridge (CloudWatch Events)

### EventBridge Basics
- **Serverless event bus**
- React to events from AWS services
- **Schedule**: Cron or rate expressions
- **Event patterns**: Match specific events

### EventBridge Components
- **Event Bus**: Default (AWS services), partner, custom
- **Rules**: Match events and route to targets
- **Targets**: Lambda, SQS, SNS, Step Functions, Kinesis, etc. (20+ services)

### EventBridge vs CloudWatch Events
- EventBridge = CloudWatch Events (enhanced)
- EventBridge adds: Schema registry, partner integrations, custom buses

## Step Functions

### Step Functions Basics
- **Orchestrate workflows** (state machines)
- **Visual workflow**
- **Serverless**
- Coordinate: Lambda, ECS, Fargate, SNS, SQS, DynamoDB, etc.

### Workflow Types
- **Standard**: Max 1 year, exactly-once, audit trail
- **Express**: Max 5 min, at-least-once, high-volume (IoT, streaming)

### State Types
- **Task**: Do work (Lambda, activity)
- **Choice**: Conditional logic
- **Parallel**: Execute branches in parallel
- **Wait**: Delay
- **Succeed/Fail**: Terminal states
- **Pass**: Pass input to output
- **Map**: Iterate over items

## SWF (Simple Workflow Service)
- **Legacy** (use Step Functions instead)
- Human-involved workflows
- **Activity workers** and **deciders**

## AppSync
- **Managed GraphQL** API
- Real-time and offline data sync
- **Data sources**: DynamoDB, Lambda, HTTP, RDS
- **Use case**: Mobile/web apps needing real-time

## AppFlow
- **SaaS integration** (no code)
- Transfer data: Salesforce, SAP, Slack → S3, Redshift
- **Bidirectional**, scheduled or event-driven

## MQ (Amazon MQ)
- **Managed message broker**
- **RabbitMQ, ActiveMQ**
- **Use case**: Migrate existing apps (lift-and-shift)
- If building new, use SQS/SNS instead

## Kinesis (Data Streaming)

### Kinesis Data Streams
- **Real-time** data streaming
- **Shards**: 1 MB/s or 1K records/s write, 2 MB/s read
- **Retention**: 1-365 days
- **Consumers**: Lambda, Kinesis Data Analytics, EC2

### Kinesis Data Firehose
- **Load streaming data** to destinations
- **Near real-time** (60 sec buffer)
- **Destinations**: S3, Redshift, OpenSearch, Splunk, HTTP
- **Auto-scaling**, no shards to manage
- **Transformations**: Lambda

### Kinesis Data Analytics
- **SQL queries** on streaming data
- Real-time analytics
- **Input**: Kinesis Data Streams, Firehose
- **Output**: S3, Redshift, OpenSearch, Streams

### Kinesis vs SQS
| Feature | Kinesis | SQS |
|---------|---------|-----|
| Use case | Real-time streaming | Message queue |
| Retention | 1-365 days | 1-14 days |
| Consumers | Multiple (same data) | One per message |
| Ordering | Per shard | FIFO queue |
| Throughput | Shard-based | Unlimited |

## Quick Exam Tips
- **SQS**: Decouple, queue, 256 KB max
- **SQS Standard**: Unlimited throughput, at-least-once, best-effort order
- **SQS FIFO**: 300 msg/s, exactly-once, strict order, name ends `.fifo`
- **SNS**: Pub/Sub, push, fan-out
- **SNS + SQS**: Fan-out pattern (1 message → many queues)
- **EventBridge**: Event-driven, schedule, 20+ targets
- **Step Functions**: Orchestrate workflows, visual, serverless
- **Kinesis Streams**: Real-time streaming, shards, multiple consumers
- **Kinesis Firehose**: Load to S3/Redshift, near real-time, no shards
- **MQ**: Managed RabbitMQ/ActiveMQ (legacy migrations)
- **AppSync**: GraphQL API, real-time, offline sync

