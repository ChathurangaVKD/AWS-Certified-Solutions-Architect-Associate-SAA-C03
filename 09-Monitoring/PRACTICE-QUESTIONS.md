# Monitoring & Management - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company wants to monitor the memory utilization of its EC2 instances and trigger an alarm when memory usage exceeds 80%. Which combination of actions should the solutions architect take?

A. Enable detailed monitoring on EC2 instances and create a CloudWatch alarm on the default memory metric  
B. Install the CloudWatch Agent on EC2 instances, configure it to send memory metrics, and create a CloudWatch alarm  
C. Use AWS Systems Manager Session Manager to view memory metrics and manually create alerts  
D. Enable CloudTrail logging and use CloudWatch Logs Insights to query memory usage  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- EC2 instances do NOT send memory metrics by default
- The CloudWatch Agent must be installed to collect memory metrics
- Once the agent sends metrics to CloudWatch, you can create alarms
- Option A is incorrect because memory is not a default metric
- Option C doesn't provide automated alerting
- Option D is for auditing API calls, not performance metrics

**References:** CloudWatch Agent, EC2 Monitoring, Custom Metrics
</details>

---

### Question 2
A security team needs to identify which IAM user terminated a critical EC2 instance last week. Which AWS service should they use?

A. Amazon CloudWatch Logs  
B. AWS Config  
C. AWS CloudTrail  
D. AWS Systems Manager  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- CloudTrail records API calls including WHO made them
- It tracks management events like TerminateInstances
- CloudTrail logs include user identity, timestamp, and action
- Option A (CloudWatch Logs) monitors application logs, not API calls
- Option B (Config) tracks resource configuration, not who made changes
- Option D (Systems Manager) is for operational management

**References:** CloudTrail, API Call Auditing, Governance
</details>

---

### Question 3
A company needs to ensure all S3 buckets have versioning enabled and receive automatic notifications when this requirement is violated. Which AWS service should be used?

A. AWS CloudTrail with CloudWatch Logs  
B. Amazon CloudWatch with custom metrics  
C. AWS Config with AWS Managed Rules  
D. AWS Systems Manager State Manager  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS Config evaluates resource configurations against rules
- Managed rule `s3-bucket-versioning-enabled` checks versioning
- Config can send SNS notifications when non-compliant
- CloudTrail tracks who made changes but doesn't evaluate compliance
- CloudWatch monitors performance metrics, not configuration compliance
- Systems Manager State Manager is for EC2 instance configuration

**References:** AWS Config, Config Rules, Compliance Auditing
</details>

---

### Question 4
A solutions architect needs to access EC2 instances for troubleshooting without opening port 22 or managing SSH keys. Which AWS service provides this capability?

A. AWS CloudShell  
B. AWS Systems Manager Session Manager  
C. Amazon EC2 Instance Connect  
D. AWS Direct Connect  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Session Manager provides secure shell access without SSH keys or open ports
- Uses IAM permissions for access control
- Session logs can be sent to S3 or CloudWatch Logs
- EC2 Instance Connect still requires port 22 to be open
- CloudShell is for running AWS CLI commands, not accessing instances
- Direct Connect is for network connectivity

**References:** Systems Manager Session Manager, Secure Access
</details>

---

### Question 5
A company wants to automatically patch all EC2 instances in their fleet during a scheduled maintenance window. Which AWS service should they use?

A. AWS CloudFormation with custom scripts  
B. AWS Systems Manager Patch Manager  
C. Amazon EventBridge with Lambda  
D. AWS Config with remediation actions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Patch Manager automates OS and application patching
- Maintenance windows define when to patch
- Patch baselines specify which patches to install
- CloudFormation is for infrastructure as code, not patching
- EventBridge could trigger patching but isn't purpose-built
- Config evaluates compliance but doesn't patch

**References:** Systems Manager Patch Manager, Maintenance Windows
</details>

---

### Question 6
An application writes log data to CloudWatch Logs. The operations team needs to be alerted when the word "ERROR" appears more than 10 times in 5 minutes. How should this be configured?

A. Use CloudWatch Logs Insights to query for errors and manually check  
B. Create a metric filter to count "ERROR" occurrences, then create an alarm on that metric  
C. Export logs to S3 and use Athena to query for errors  
D. Use CloudTrail to track error events and create SNS notifications  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Metric filters extract metrics from log data
- Filter pattern can count occurrences of "ERROR"
- CloudWatch alarm can trigger on the custom metric
- This provides automated, real-time alerting
- Option A requires manual intervention
- Option C adds unnecessary complexity and isn't real-time
- CloudTrail is for API calls, not application logs

**References:** CloudWatch Logs, Metric Filters, CloudWatch Alarms
</details>

---

### Question 7
A company needs to track all configuration changes to security groups across multiple AWS accounts and regions. What is the MOST efficient solution?

A. Enable CloudTrail in each account and region  
B. Create Lambda functions to monitor security group changes  
C. Use AWS Config with a Config Aggregator  
D. Use CloudWatch Events in each region  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS Config records resource configuration changes
- Config Aggregator provides centralized view across accounts and regions
- Tracks configuration history and relationships
- CloudTrail tracks who made changes but doesn't aggregate configurations
- Lambda would require custom development and maintenance
- CloudWatch Events could detect changes but doesn't provide historical tracking

**References:** AWS Config, Config Aggregator, Multi-Account Management
</details>

---

### Question 8
A solutions architect needs to run a script on all EC2 instances fleet-wide without SSH access. The script should install security updates. Which service provides this capability?

A. AWS Systems Manager Run Command  
B. AWS Lambda with EC2 API  
C. Amazon CloudWatch Events  
D. AWS Config Remediation  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Run Command executes commands on managed instances remotely
- No SSH required, uses IAM permissions
- Provides rate control and error handling
- Command history recorded in CloudTrail
- Lambda could invoke Run Command but isn't the direct solution
- CloudWatch Events can trigger Run Command but isn't the execution service
- Config Remediation uses SSM Automation Documents

**References:** Systems Manager Run Command, Fleet Management
</details>

---

### Question 9
An organization wants to detect unusual API activity, such as a sudden spike in EC2 instance creation. Which CloudTrail feature should be enabled?

A. CloudTrail Data Events  
B. CloudTrail Management Events  
C. CloudTrail Insights Events  
D. CloudTrail Multi-Region Trails  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- CloudTrail Insights uses machine learning to detect unusual activity
- Identifies anomalies like spikes in resource provisioning or IAM actions
- Management Events track API calls but don't detect anomalies
- Data Events track high-volume operations (S3 objects, Lambda invocations)
- Multi-Region Trails collect logs but don't analyze patterns

**References:** CloudTrail Insights, Anomaly Detection
</details>

---

### Question 10
A company needs to store CloudWatch Logs for 10 years to meet compliance requirements. What is the MOST cost-effective approach?

A. Keep logs in CloudWatch Logs with 10-year retention  
B. Export logs to S3, then transition to S3 Glacier Deep Archive  
C. Export logs to S3, then use S3 Intelligent-Tiering  
D. Stream logs to Kinesis Data Firehose and store in Redshift  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudWatch Logs retention is expensive for long-term storage
- Export to S3 for cost-effective long-term storage
- S3 Glacier Deep Archive is cheapest for archival ($0.00099 per GB/month)
- S3 Intelligent-Tiering is more expensive than Glacier Deep Archive
- Redshift is for analytics, not cost-effective archival

**References:** CloudWatch Logs Export, S3 Glacier Deep Archive, Cost Optimization
</details>

---

### Question 11
A development team needs to query application logs to troubleshoot issues. The logs are stored in CloudWatch Logs. Which feature should they use for ad-hoc log analysis?

A. CloudWatch Metrics  
B. CloudWatch Logs Insights  
C. CloudWatch Dashboards  
D. CloudWatch Alarms  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudWatch Logs Insights provides interactive log analytics
- Purpose-built query language for searching and analyzing logs
- Can find errors, count events, calculate percentiles
- Metrics are for numerical performance data
- Dashboards visualize but don't query
- Alarms trigger on thresholds

**References:** CloudWatch Logs Insights, Log Analytics
</details>

---

### Question 12
A company wants to automatically remediate non-compliant resources. For example, when an S3 bucket is created without encryption, it should be automatically encrypted. Which solution accomplishes this?

A. AWS Config Rules with automatic remediation using SSM Automation Documents  
B. CloudWatch Events with Lambda functions  
C. AWS CloudTrail with SNS notifications  
D. Systems Manager State Manager  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Config Rules evaluate compliance
- Automatic remediation uses SSM Automation Documents
- Can trigger remediation when resources become non-compliant
- CloudWatch Events could work but Config is purpose-built for compliance
- CloudTrail only tracks changes, doesn't remediate
- State Manager maintains EC2 configuration, not S3

**References:** AWS Config, Auto Remediation, SSM Automation
</details>

---

### Question 13
A solutions architect needs to store sensitive configuration data like database passwords that can be accessed by EC2 instances and Lambda functions. The solution must support encryption and version history. Which service should be used?

A. AWS Secrets Manager  
B. AWS Systems Manager Parameter Store  
C. Amazon S3 with versioning  
D. AWS Config  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Parameter Store securely stores configuration data and secrets
- Supports encryption with KMS
- Maintains version history
- Integrates with EC2, Lambda, CloudFormation
- Secrets Manager is also valid but more expensive (includes auto-rotation)
- For exam context, Parameter Store is part of Systems Manager
- S3 isn't designed for configuration management
- Config is for compliance tracking

**References:** Systems Manager Parameter Store, Secrets Management
</details>

---

### Question 14
A company has a multi-region application and needs to create a unified dashboard showing CloudWatch metrics from all regions. Is this possible?

A. No, CloudWatch dashboards are region-specific only  
B. Yes, CloudWatch dashboards support cross-region metrics  
C. Yes, but only with CloudWatch Logs, not metrics  
D. Yes, but requires CloudWatch Events to aggregate data  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudWatch dashboards support cross-region and cross-account views
- Can add graphs from multiple regions to single dashboard
- Global view of distributed applications
- No additional aggregation service required

**References:** CloudWatch Dashboards, Cross-Region Monitoring
</details>

---

### Question 15
An operations team needs to collect metadata about all EC2 instances including installed applications, OS details, and network configuration. Which Systems Manager feature should they use?

A. Systems Manager Session Manager  
B. Systems Manager Inventory  
C. Systems Manager Patch Manager  
D. Systems Manager Run Command  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Systems Manager Inventory collects metadata from managed instances
- Gathers information about OS, applications, network config
- Can query and visualize with Inventory dashboard
- Session Manager is for shell access
- Patch Manager is for patching
- Run Command executes commands

**References:** Systems Manager Inventory, Metadata Collection
</details>

---

### Question 16
A company needs to ensure CloudTrail logs haven't been tampered with for compliance audits. Which feature should be enabled?

A. CloudTrail Multi-Region Trails  
B. CloudTrail Log File Integrity Validation  
C. CloudTrail Insights  
D. CloudTrail Data Events  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Log File Integrity Validation uses digital signatures
- Ensures logs haven't been modified after delivery
- Required for compliance and forensic investigations
- Multi-Region Trails enable logging across regions
- Insights detect unusual activity
- Data Events track resource operations

**References:** CloudTrail, Log Integrity, Compliance
</details>

---

### Question 17
A solutions architect needs to process CloudWatch Logs in real-time and send filtered data to an analytics application. Which solution should be used?

A. Export logs to S3 and use Athena  
B. Use CloudWatch Logs Subscriptions with Kinesis Data Streams  
C. Use CloudWatch Logs Insights with scheduled queries  
D. Export logs to S3 and use Lambda  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudWatch Logs Subscriptions enable real-time processing
- Can send to Kinesis Data Streams for real-time analytics
- Also supports Kinesis Data Firehose and Lambda
- S3 export is not real-time (batch process)
- Logs Insights is for ad-hoc queries, not streaming

**References:** CloudWatch Logs Subscriptions, Real-Time Processing
</details>

---

### Question 18
A company wants to track when a specific IAM policy was attached to a role and view the complete configuration history. Which service provides this capability?

A. AWS CloudTrail only  
B. AWS Config only  
C. Both CloudTrail and Config  
D. IAM Access Analyzer  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- CloudTrail shows WHO attached the policy and WHEN (API call details)
- Config shows configuration history and timeline of changes
- Both services complement each other for complete visibility
- CloudTrail: "Who did what, when"
- Config: "What does it look like now and over time"
- IAM Access Analyzer analyzes resource policies for external access

**References:** CloudTrail vs Config, Configuration History
</details>

---

### Question 19
An application needs to maintain a desired state on EC2 instances, ensuring specific software is always installed and running. Which Systems Manager feature should be used?

A. Systems Manager Run Command  
B. Systems Manager State Manager  
C. Systems Manager Automation  
D. Systems Manager Patch Manager  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- State Manager maintains desired state configuration
- Creates associations between documents and instances
- Continuously enforces configuration
- Run Command executes one-time commands
- Automation runs workflows
- Patch Manager handles patching

**References:** Systems Manager State Manager, Configuration Management
</details>

---

### Question 20
A company needs to query 5 years of CloudTrail logs to investigate security incidents. What is the MOST efficient solution?

A. Download all logs from S3 and use local tools  
B. Use Amazon Athena to query CloudTrail logs in S3  
C. Use CloudTrail Lake to query logs with SQL  
D. Import logs into Elasticsearch  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- CloudTrail Lake is purpose-built for querying CloudTrail logs
- Uses SQL to query events
- Can retain events for up to 7 years
- Aggregates logs from multiple accounts/regions
- Athena could work but CloudTrail Lake is optimized for this use case
- Option A is inefficient and not scalable
- Elasticsearch adds unnecessary complexity

**References:** CloudTrail Lake, Log Query and Analysis
</details>

---

## Summary

### Key Concepts Tested:
1. **CloudWatch**: Metrics, Logs, Alarms, Dashboards, Agent
2. **CloudTrail**: API auditing, Who/What/When, Log integrity
3. **AWS Config**: Configuration tracking, Compliance rules, Remediation
4. **Systems Manager**: Session Manager, Patch Manager, Run Command, State Manager, Parameter Store, Inventory
5. **Service Comparisons**: CloudTrail vs Config vs CloudWatch

### Exam Tips:
- ✅ EC2 memory metrics require CloudWatch Agent
- ✅ CloudTrail for "who made changes"
- ✅ Config for "what does it look like"
- ✅ Session Manager eliminates need for SSH keys and open ports
- ✅ Metric filters create metrics from log data
- ✅ Config Aggregator for multi-account/region compliance
- ✅ CloudTrail Insights detects unusual API activity
- ✅ Parameter Store for configuration and secrets management

