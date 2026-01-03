# ⚡ Fast Learning - Application Integration

> **Time to Complete**: 45-60 minutes | **Exam Weight**: ~10-15%

## 🎯 Must-Know Concepts (5 Minutes)

### Integration Service Selector (SSKE-AS)
```
MESSAGE QUEUE? → SQS (Simple Queue Service)
PUB/SUB? → SNS (Simple Notification Service)
EVENT BUS? → EventBridge
ORCHESTRATION? → Step Functions
API GATEWAY? → API Gateway
STREAMING? → Kinesis
APP WORKFLOW? → SWF (legacy, use Step Functions)
```

**Memory Aid**: "SQS Sends, SNS Notifies, Kinesis Streams, EventBridge Acts, Step functions Sequence"

## 📊 Quick Reference Tables

### SQS vs SNS vs EventBridge
| Feature | SQS | SNS | EventBridge |
|---------|-----|-----|-------------|
| **Type** | Queue (pull) | Pub/Sub (push) | Event bus |
| **Pattern** | Point-to-point | Fan-out (1-to-many) | Event routing |
| **Persistence** | Yes (4-14 days) | No (immediate delivery) | No |
| **Consumers** | Poll for messages | Push to subscribers | Rules route events |
| **Use Case** | Decouple apps | Notifications | Event-driven architecture |
| **Max Size** | 256 KB | 256 KB | 256 KB |

### SQS Queue Types
| Feature | Standard | FIFO |
|---------|----------|------|
| **Order** | Best-effort | Guaranteed |
| **Duplicates** | Possible | Exactly-once |
| **Throughput** | Unlimited | 300 msg/s (batch: 3,000) |
| **Use Case** | High throughput | Order matters |
| **Naming** | Any name | Must end in .fifo |

**Memory Aid**: "FIFO = First In First Out, ordered, Fewer messages"

## 🔥 Exam Hot Topics

### 1. SQS Deep Dive
```
KEY CONCEPTS:
├── Visibility Timeout (default 30s, max 12h)
│   └── Message invisible to other consumers after polling
├── Message Retention (default 4 days, max 14 days)
│   └── How long messages stay in queue
├── Long Polling (0-20s)
│   └── Wait for messages (reduces costs, preferred)
├── Short Polling (default)
│   └── Immediate return (can return empty)
└── Dead Letter Queue (DLQ)
    └── Failed messages after max receives

LIMITS:
├── Message size: 256 KB (max)
├── Max retention: 14 days
├── Visibility timeout: 12 hours (max)
└── Delay: 0-900 seconds (15 min)
```

**Common Pattern**: Producer → SQS → Consumer (Auto Scaling based on queue depth)

### 2. SNS Features
```
SUBSCRIBERS:
├── HTTP/HTTPS endpoints
├── Email/Email-JSON
├── SMS (text messages)
├── SQS queues
├── Lambda functions
├── Mobile push (APNS, GCM, etc.)
└── Kinesis Data Firehose

FEATURES:
├── Message filtering (subscribers choose)
├── FIFO topics (ordering + deduplication)
├── Encryption (at rest with KMS)
├── Access policies
└── Message attributes

USE CASES:
├── Fan-out pattern (SNS → multiple SQS)
├── Alerts and notifications
├── Mobile push notifications
└── Email campaigns
```

### 3. SNS + SQS Fan-Out Pattern
```
        [SNS Topic]
            |
    ________|________
    |       |       |
  [SQS]  [SQS]  [SQS]
    |       |       |
 [App1] [App2] [App3]

BENEFITS:
✅ Fully decoupled
✅ No data loss
✅ Parallel asynchronous processing
✅ Add subscribers easily
```

### 4. Kinesis Family
| Service | Purpose | Use Case | Data Retention |
|---------|---------|----------|----------------|
| **Data Streams** | Real-time streaming | Process streaming data | 1-365 days |
| **Data Firehose** | Load streams to storage | ETL to S3/Redshift | None (immediate) |
| **Data Analytics** | SQL on streams | Real-time analytics | N/A |
| **Video Streams** | Video streaming | Security cameras, video | 1-7 days |

**Memory Aid**: "DFAV" = Data streams (raw), Firehose (load), Analytics (analyze), Video

## 💡 Common Exam Scenarios

### Scenario 1: Decouple Application Tiers
**Q**: Web tier and processing tier need to be independent
**✅ ANSWER**: SQS queue between tiers

### Scenario 2: Send Same Message to Multiple Services
**Q**: One event needs to trigger 3 different Lambda functions
**✅ ANSWER**: SNS topic with 3 Lambda subscriptions

### Scenario 3: Process Messages in Order
**Q**: Orders must be processed in exact sequence
**✅ ANSWER**: SQS FIFO queue (not Standard)

### Scenario 4: Handle Traffic Spikes
**Q**: Application receives 10,000 requests in 1 minute, process over 1 hour
**✅ ANSWER**: SQS Standard queue + Auto Scaling based on queue depth

### Scenario 5: Real-Time Log Processing
**Q**: Process millions of log records per second in real-time
**✅ ANSWER**: Kinesis Data Streams

### Scenario 6: Send to S3 and Multiple SQS Queues
**Q**: S3 upload event needs to trigger 3 different processing workflows
**✅ ANSWER**: S3 → SNS → 3 SQS queues (fan-out pattern)

### Scenario 7: Coordinate Microservices
**Q**: Multi-step workflow with error handling and retries
**✅ ANSWER**: AWS Step Functions (state machine)

### Scenario 8: Route Events to Different Targets
**Q**: Different EC2 state changes go to different Lambda functions
**✅ ANSWER**: EventBridge with rules

## 🎓 Speed Learning Tips

### API Gateway Quick Facts
```
TYPES:
├── REST API (feature-rich)
├── HTTP API (cheaper, simpler)
└── WebSocket API (bidirectional)

FEATURES:
├── Caching
├── Request/response transformation
├── Authentication (IAM, Cognito, Lambda)
├── Throttling (rate limiting)
├── API versioning
└── CORS support

INTEGRATION TARGETS:
├── Lambda (serverless)
├── HTTP endpoints
├── AWS services (S3, DynamoDB)
├── VPC Link (private resources)
└── Mock responses
```

### Step Functions Basics
```
WHAT: Serverless orchestration
HOW: Visual workflows (state machines)

STATE TYPES:
├── Task - Do work (Lambda, etc.)
├── Choice - Branching logic
├── Parallel - Run in parallel
├── Wait - Delay
├── Succeed/Fail - End states
└── Map - Loop over items

WORKFLOW TYPES:
├── Standard (max 1 year, exactly-once)
└── Express (max 5 min, at-least-once)

USE CASES:
├── Multi-step applications
├── ETL processes
├── Order processing
└── Human approval workflows
```

### EventBridge Key Concepts
```
COMPONENTS:
├── Event Bus (receives events)
├── Rules (filter & route)
├── Targets (where to send)
└── Schema Registry (structure)

EVENT SOURCES:
├── AWS services (100+)
├── Custom applications
├── SaaS partners (Zendesk, etc.)
└── Scheduled (cron)

TARGETS:
├── Lambda functions
├── SQS queues
├── SNS topics
├── Step Functions
├── EC2 actions
└── 20+ AWS services

VS CloudWatch Events:
└── EventBridge = CloudWatch Events + SaaS + custom apps
```

## 📝 Rapid-Fire Facts

### SQS Important Settings
```
VISIBILITY TIMEOUT
├── Default: 30 seconds
├── Max: 12 hours
├── Purpose: Prevent duplicate processing
└── ChangeMessageVisibility API to extend

RECEIVE MESSAGE WAIT TIME (Long Polling)
├── Default: 0 (short polling)
├── Max: 20 seconds
├── Benefit: Reduce costs, fewer empty responses
└── Recommended: Enable long polling

DELAY QUEUES
├── Default: 0 seconds
├── Max: 15 minutes (900 seconds)
├── Purpose: Postpone message delivery
└── Use: Implement delays in processing
```

### SNS vs SQS Decision
```
Use SNS when:
✅ Multiple subscribers
✅ Push-based delivery
✅ Real-time notifications
✅ Mobile push
✅ Email/SMS needed

Use SQS when:
✅ Decouple applications
✅ Buffer requests
✅ Pull-based processing
✅ Persist messages
✅ Control processing rate
```

### Kinesis Data Streams
- **Shards**: Throughput unit (1 MB/s in, 2 MB/s out)
- **Retention**: 1-365 days (default 24 hours)
- **Partition Key**: Determines which shard
- **Consumers**: Multiple can read same data
- **Use**: Real-time analytics, log processing

### Kinesis Firehose
- **No shards**: Fully managed scaling
- **Destinations**: S3, Redshift, Elasticsearch, Splunk
- **Transformations**: Lambda can transform data
- **Buffering**: By size (1-128 MB) or time (60-900s)
- **Use**: Load streaming data to storage

## 🚀 5-Minute Master Review

### Integration Decision Tree
```
1. What's your pattern?
   QUEUE (pull) → SQS
   PUB/SUB (push) → SNS
   STREAMING → Kinesis
   ORCHESTRATION → Step Functions
   API → API Gateway
   EVENT ROUTING → EventBridge
   
2. For queuing, need order?
   YES → SQS FIFO
   NO → SQS Standard
   
3. For streaming, need processing?
   RAW STREAMING → Data Streams
   LOAD TO STORAGE → Firehose
   ANALYTICS → Data Analytics
   
4. Multiple consumers for same message?
   YES → SNS (pub/sub)
   NO → SQS (queue)
```

### Common Patterns
```
1. DECOUPLING PATTERN
   App1 → SQS → App2
   
2. FAN-OUT PATTERN
   S3 → SNS → [SQS, SQS, SQS] → [Lambda, Lambda, Lambda]
   
3. LOAD LEVELING
   Requests → SQS → Auto Scaling Group (process at own pace)
   
4. PRIORITY QUEUE
   High priority → SQS1
   Low priority → SQS2
   
5. EVENT-DRIVEN
   AWS Service → EventBridge → Lambda
```

### Common Mistakes to Avoid
❌ Using SNS when you need message persistence (use SQS)
❌ Not setting appropriate visibility timeout (messages reprocess)
❌ Using SQS Standard when order matters (use FIFO)
❌ Forgetting to enable long polling (higher costs)
❌ Not using Dead Letter Queue for failed messages
❌ Polling empty SQS queues frequently (use long polling)
❌ Not implementing exponential backoff for retries
❌ Using Step Functions for simple tasks (use Lambda)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. SQS max message size? __
2. SQS max retention period? __
3. What ensures message order in SQS? __
4. SNS delivers to how many types of endpoints? __
5. What enables fan-out pattern? __
6. Which Kinesis service loads to S3? __
7. Max visibility timeout for SQS? __
8. API Gateway can integrate with? __

---

### AppSync (GraphQL)
```
WHAT: Managed GraphQL service
USE: Mobile/web apps with real-time data

FEATURES:
├── Real-time subscriptions
├── Offline sync
├── Multiple data sources
├── Automatic scaling
└── Built-in security

DATA SOURCES:
├── DynamoDB
├── Lambda
├── HTTP endpoints
├── RDS (via Lambda)
└── Elasticsearch
```

### Amazon MQ
```
WHAT: Managed message broker
PROTOCOLS: AMQP, MQTT, OpenWire, STOMP, WebSocket
ENGINES: ActiveMQ, RabbitMQ

WHEN TO USE:
✅ Migrating from on-premises message brokers
✅ Need industry-standard protocols
✅ Existing applications using JMS, AMQP

WHEN NOT TO USE:
❌ New cloud-native apps (use SQS/SNS)
```

## ⏱️ Next Steps
- Time spent: ~45-60 min
- Practice: Create SQS queue, SNS topic, fan-out pattern
- Ready for: Application Integration practice questions
- Move to: Module 09 - Monitoring

---

**Quick Answers**: 
1) 256 KB
2) 14 days
3) FIFO queue
4) 6+ (HTTP, Email, SMS, SQS, Lambda, Kinesis, etc.)
5) SNS → multiple SQS queues
6) Kinesis Data Firehose
7) 12 hours
8) Lambda, HTTP, AWS services, VPC Link

