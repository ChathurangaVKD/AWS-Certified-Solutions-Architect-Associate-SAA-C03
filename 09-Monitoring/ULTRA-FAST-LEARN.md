# 09: Monitoring & Management - Ultra Fast Learning 🚀

## CloudWatch

### CloudWatch Metrics
- **AWS services**: Automatic (CPU, network, disk, status)
- **Default**: 5-min intervals
- **Detailed monitoring**: 1-min intervals (extra cost)
- **Custom metrics**: PutMetricData API, 1-sec intervals possible
- **EC2 memory**: NOT default (need CloudWatch agent)

### CloudWatch Alarms
- **States**: OK, ALARM, INSUFFICIENT_DATA
- **Period**: 10 sec to 1 day
- **Actions**: SNS, Auto Scaling, EC2 action (stop/terminate/reboot)
- **Composite alarms**: AND/OR multiple alarms

### CloudWatch Logs
- **Log groups**: Collection of log streams
- **Log streams**: Sequence of log events
- **Retention**: 1 day to 10 years (never expire)
- **Subscription filters**: Stream to Lambda, Kinesis, Firehose
- **Metric filters**: Extract metrics from logs
- **CloudWatch Logs Insights**: Query language for logs

### CloudWatch Agent
- **Collect logs and metrics** from EC2/on-premises
- **Metrics**: Memory, disk, processes, netstat
- **Logs**: Application logs, system logs
- **Unified agent**: Logs + metrics

### CloudWatch Dashboards
- **Visualize metrics**
- **Global** (cross-region)
- **3 dashboards free** (up to 50 metrics)
- **Auto-refresh**: 1 min to 15 min

### EventBridge (CloudWatch Events)
- **React to events** from AWS services
- **Schedule**: Cron/rate expressions
- **Event pattern**: Match specific events
- **Targets**: Lambda, SQS, SNS, Step Functions, etc.

## CloudTrail
- **API call logging** (governance, compliance, audit)
- **Who, what, when, where**: User, action, time, IP
- **Event History**: 90 days free
- **Trails**: Long-term storage to S3
- **Management events**: Control plane (free for trail)
- **Data events**: Data plane (S3 GetObject, Lambda invoke) - paid
- **Insights**: Detect unusual API activity (ML)

### CloudTrail Use Cases
- Security analysis, resource change tracking, compliance
- Troubleshooting, forensic investigation

## AWS Config
- **Audit resource configurations**
- **Record changes** over time
- **Compliance**: Evaluate against rules
- **Remediation**: Auto-fix non-compliant (SSM Automation)
- **Not free**: Pay per config item + rule evaluation

### Config Components
- **Configuration items**: Resource configuration snapshot
- **Configuration history**: Changes over time
- **Configuration recorder**: Records changes
- **Config rules**: Compliance evaluation (AWS managed or custom)
- **Conformance packs**: Collection of rules + remediation

### Config Use Cases
- Compliance auditing, security analysis
- Change management, troubleshooting
- Example rules: S3 bucket versioning, encrypted EBS, required tags

## CloudWatch vs CloudTrail vs Config
| Service | What it monitors | Use case |
|---------|------------------|----------|
| CloudWatch | Performance metrics, logs | Performance, alarms |
| CloudTrail | API calls (who did what) | Security, audit |
| Config | Resource config changes | Compliance, governance |

## X-Ray
- **Distributed tracing**
- **Trace requests** across microservices
- **Service map**: Visual representation
- **Segments**: Work done by single component
- **Subsegments**: Granular timing
- **Annotations**: Indexed for filtering
- **Metadata**: Not indexed
- **Sampling**: Reduce cost (trace % of requests)

### X-Ray Use Cases
- Identify performance bottlenecks
- Understand dependencies
- Find errors and exceptions
- Pinpoint issues in microservices

## Trusted Advisor
- **Best practice recommendations**
- **5 categories**: Cost optimization, performance, security, fault tolerance, service limits
- **Free**: 7 core checks (Basic/Developer support)
- **Paid**: All checks (Business/Enterprise support)

### Core Checks (Free)
- S3 bucket permissions
- Security groups (unrestricted ports)
- IAM use
- MFA on root
- EBS public snapshots
- RDS public snapshots
- Service limits

### All Checks (Paid)
- Full access to all recommendations
- CloudWatch integration
- Programmatic access via API

## Systems Manager (SSM)

### SSM Key Features
- **Manage EC2 and on-premises** servers
- **Free** (pay for underlying resources)
- **SSM Agent**: Must be installed (pre-installed on Amazon Linux 2, Ubuntu)

### SSM Components

**Session Manager**
- **Secure shell access** without SSH/bastion host
- No inbound ports, no SSH keys
- Audit with CloudTrail
- Log sessions to S3 or CloudWatch

**Run Command**
- Execute commands on multiple instances
- Rate control, error threshold
- Integration with IAM, CloudTrail
- No SSH required

**Patch Manager**
- Automate OS patching
- Patch baselines, maintenance windows
- Compliance reporting

**Parameter Store**
- **Secure storage** for config/secrets
- **Free** (standard tier)
- **Hierarchical** structure (`/app/prod/db-password`)
- **Integration**: CloudFormation, Lambda, ECS
- **SecureString**: KMS encryption

**Automation**
- Automate common maintenance tasks
- Predefined runbooks
- Integration with Lambda, EventBridge

**Inventory**
- Collect metadata from instances
- OS, applications, configurations
- Query with Resource Data Sync

**State Manager**
- Maintain desired state configuration
- Apply configurations automatically

## Personal Health Dashboard
- **Alerts and guidance** for AWS events
- **Proactive notifications** for scheduled activities
- **Personalized** view (not general AWS status)

## Service Health Dashboard
- **Public AWS service status**
- **General** (not account-specific)
- Historical data

## Quick Exam Tips
- **CloudWatch**: Metrics, alarms, logs, dashboards
- **CloudWatch Agent**: Memory metrics for EC2
- **CloudTrail**: API logging, 90 days free
- **Config**: Resource configuration, compliance
- **X-Ray**: Distributed tracing, microservices
- **Trusted Advisor**: Best practices, 7 free checks
- **SSM Session Manager**: SSH without SSH/bastion
- **SSM Parameter Store**: Free config storage
- **SSM Run Command**: Execute on multiple instances
- **Personal Health Dashboard**: Account-specific alerts
- **Detailed Monitoring**: 1-min intervals (extra cost)
- **CloudWatch Logs retention**: 1 day to 10 years

