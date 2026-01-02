# Module 13: Cost Optimization

## Overview
Cost optimization is a critical aspect of cloud architecture and a key pillar of the AWS Well-Architected Framework. This module covers AWS pricing models, cost management tools, and strategies to optimize your AWS spending.

## Learning Objectives
- Understand AWS pricing models and purchasing options
- Use AWS Cost Explorer for cost analysis
- Set up budgets and alerts
- Implement cost optimization strategies
- Use AWS cost management tools effectively
- Understand the AWS Free Tier

---

## 1. AWS Pricing Fundamentals

### Pay-As-You-Go Pricing
- **No upfront costs**: Pay only for what you use
- **No minimum commitments**: Scale up or down freely
- **No termination fees**: Stop using services anytime

### Key Pricing Principles

**1. Compute**
- Pay for compute time (per second or per hour)
- Stop paying when you stop instances

**2. Storage**
- Pay for data stored (per GB)
- Different storage classes have different prices

**3. Data Transfer**
- **Inbound**: Generally free
- **Outbound**: Charges apply (varies by destination)
- **Between AWS services in same region**: Often free
- **Between regions**: Charges apply

### AWS Free Tier

**Three Types:**

**1. Always Free**
- Services that are always free within limits
- Examples:
  - **Lambda**: 1M free requests/month
  - **DynamoDB**: 25 GB storage
  - **SNS**: 1M publishes/month
  - **CloudWatch**: 10 custom metrics

**2. 12 Months Free**
- Free for first 12 months after AWS account creation
- Examples:
  - **EC2**: 750 hours/month of t2.micro or t3.micro
  - **S3**: 5 GB standard storage
  - **RDS**: 750 hours/month of db.t2.micro
  - **CloudFront**: 50 GB data transfer out

**3. Trials**
- Short-term free trials for specific services
- Examples:
  - **SageMaker**: 250 hours/2 months of t2.medium
  - **Redshift**: 750 hours/2 months
  - **Inspector**: 90-day trial

### Total Cost of Ownership (TCO)

**On-Premises Costs:**
- Hardware (servers, storage, networking)
- Software licenses
- Data center costs (space, power, cooling)
- IT staff (salary, training)
- Maintenance and support

**AWS Costs:**
- Compute, storage, network
- Reduced or eliminated on-premises costs
- **TCO Calculator**: Compare on-premises vs AWS costs

---

## 2. EC2 Pricing Models

### Overview of Purchasing Options

| Option | Use Case | Discount | Commitment |
|--------|----------|----------|------------|
| **On-Demand** | Short-term, unpredictable workloads | None | None |
| **Reserved** | Steady-state, predictable usage | Up to 72% | 1 or 3 years |
| **Savings Plans** | Flexible compute usage | Up to 72% | 1 or 3 years |
| **Spot Instances** | Fault-tolerant, flexible workloads | Up to 90% | None |
| **Dedicated Hosts** | Compliance, licensing | Varies | 1 or 3 years (optional) |
| **Dedicated Instances** | Hardware isolation | Slightly higher | None |

---

### 2.1 On-Demand Instances

**Characteristics:**
- Pay by the second (Linux/Windows, minimum 60 seconds)
- No long-term commitments
- No upfront payments

**When to Use:**
- **Short-term workloads**: Development, testing
- **Unpredictable workloads**: Cannot forecast usage
- **First-time applications**: Testing new applications
- **Spiky workloads**: Irregular usage patterns

**Pricing Example:**
```
t3.medium in us-east-1: $0.0416/hour
Running 24/7 for 1 month: $0.0416 × 730 hours = $30.37/month
```

---

### 2.2 Reserved Instances (RIs)

**Characteristics:**
- **1 or 3-year commitment**
- **Up to 72% discount** vs On-Demand
- Reserve capacity in an Availability Zone
- Three payment options

**Payment Options:**

**1. All Upfront**
- Pay entire amount upfront
- Highest discount (~72%)
- No monthly charges

**2. Partial Upfront**
- Pay portion upfront
- Lower monthly rate
- Moderate discount (~50-60%)

**3. No Upfront**
- No upfront payment
- Monthly charges
- Lower discount (~40-50%)

**RI Types:**

**Standard RIs:**
- Highest discount (up to 72%)
- Cannot change instance family
- Can change instance size within same family
- Can sell in RI Marketplace

**Convertible RIs:**
- Lower discount (up to 54%)
- Can change instance family, OS, tenancy
- More flexibility
- Cannot sell in marketplace

**Scheduled RIs:**
- Reserve capacity for specific time windows
- Example: Every Friday 8 AM - 5 PM
- **Note**: No longer available for new purchases (legacy)

**RI Scope:**

**Regional RIs:**
- Apply to any AZ in the region
- No capacity reservation
- Instance size flexibility

**Zonal RIs:**
- Apply to specific AZ only
- Reserve capacity in that AZ
- No instance size flexibility

**When to Use:**
- Steady-state workloads (databases, always-on servers)
- Predictable usage patterns
- Long-term projects

**Pricing Example:**
```
t3.medium On-Demand: $0.0416/hour = $304/year
t3.medium RI (1-year, All Upfront): ~$182/year
Savings: ~40%

t3.medium RI (3-year, All Upfront): ~$109/year
Savings: ~65%
```

---

### 2.3 Savings Plans

**What are Savings Plans?**
- **Flexible pricing model**
- Commit to consistent usage ($/hour) for 1 or 3 years
- Up to 72% discount vs On-Demand
- More flexible than Reserved Instances

**Types of Savings Plans:**

**1. Compute Savings Plans**
- **Most flexible**
- Up to 66% discount
- Apply to:
  - EC2 (any instance family, size, OS, region)
  - Fargate
  - Lambda
- Automatically apply to eligible usage

**2. EC2 Instance Savings Plans**
- Up to 72% discount
- Apply to specific instance family in specific region
- Flexible across:
  - Instance size (e.g., large, xlarge)
  - OS (Linux, Windows)
  - Tenancy (shared, dedicated)
- Less flexible than Compute Savings Plans

**3. SageMaker Savings Plans**
- Up to 64% discount
- For SageMaker instances

**Payment Options:**
- All Upfront
- Partial Upfront
- No Upfront

**How It Works:**
```
Commit: $10/hour for 1 year (Compute Savings Plan)

Usage:
- 5× m5.large in us-east-1: $6/hour → Covered by plan
- 3× c5.xlarge in eu-west-1: $4/hour → Covered by plan
- 2× Fargate tasks: $2/hour → Partially covered
- Total: $12/hour
  - $10/hour at Savings Plan rate (discounted)
  - $2/hour at On-Demand rate
```

**Savings Plans vs Reserved Instances:**

| Feature | Savings Plans | Reserved Instances |
|---------|---------------|-------------------|
| **Flexibility** | High (instance family, region) | Low (specific instance) |
| **Discount** | Up to 72% | Up to 72% |
| **Applies to** | EC2, Fargate, Lambda | EC2 only |
| **Commitment** | $/hour usage | Specific instance |
| **Modification** | Automatic | Manual |

**When to Use:**
- Steady usage but need flexibility
- Multi-region workloads
- Mix of EC2, Fargate, Lambda

---

### 2.4 Spot Instances

**Characteristics:**
- **Up to 90% discount** vs On-Demand
- Use spare EC2 capacity
- Can be interrupted by AWS with 2-minute warning
- Set maximum price (optional)

**How Spot Instances Work:**
1. You request Spot Instances at your max price
2. Instances run when spot price < your max price
3. AWS can reclaim instances when capacity is needed
4. You get 2-minute warning before termination

**Spot Instance Interruption:**
```
AWS sends notification → 2-minute warning → Instance terminated
```

**Spot Instance Termination Handling:**
- EC2 sends termination notice to instance metadata
- CloudWatch Events notification
- Use: Save work, checkpoint, gracefully shutdown

**Spot Request Types:**

**One-Time Request:**
- Instances launched once
- Request closes when fulfilled

**Persistent Request:**
- Request stays open
- Relaunches instances if interrupted
- Until you cancel the request

**Spot Fleet:**
- Collection of Spot and On-Demand instances
- Define target capacity
- Launch templates with instance types
- Strategies:
  - **Lowest price**: Launch instances from lowest price pool
  - **Diversified**: Distribute across all pools
  - **Capacity optimized**: Launch in pools with optimal capacity
  - **Price capacity optimized**: Best price for capacity

**Spot Blocks (Deprecated):**
- Reserve Spot Instances for 1-6 hours
- No longer available for new users

**When to Use Spot Instances:**
- **Batch processing**: Data analysis, image processing
- **CI/CD workloads**: Build servers, testing
- **Big data and analytics**: EMR, Hadoop, Spark
- **Containerized workloads**: ECS, EKS with fault tolerance
- **Web servers behind load balancer**: With Auto Scaling
- **High-performance computing (HPC)**

**When NOT to Use:**
- Databases (risk of data loss)
- Critical applications without fault tolerance
- Applications that cannot handle interruptions

**Best Practices:**
1. **Diversify**: Use multiple instance types and AZs
2. **Graceful shutdown**: Handle termination notices
3. **Checkpointing**: Save progress regularly
4. **Combine with On-Demand**: Use Spot Fleet with On-Demand fallback

**Pricing Example:**
```
c5.large On-Demand: $0.085/hour
c5.large Spot: $0.025/hour (typical)
Savings: ~70%

Note: Spot prices fluctuate based on supply/demand
```

---

### 2.5 Dedicated Hosts

**Characteristics:**
- **Physical EC2 server** dedicated to your use
- Full control over instance placement
- Use existing server-bound software licenses
- Most expensive option

**Use Cases:**
- **Compliance requirements**: Regulatory requirements for dedicated hardware
- **Licensing**: Bring Your Own License (BYOL) - per-socket, per-core licenses
- **Visibility**: Physical server details needed

**Pricing:**
- Per-host pricing (not per instance)
- On-Demand or Reserved (1 or 3 years)

**Dedicated Hosts vs Dedicated Instances:**

| Feature | Dedicated Hosts | Dedicated Instances |
|---------|----------------|---------------------|
| **Isolation** | Physical server | Hardware-level isolation |
| **Visibility** | Full server visibility | No server visibility |
| **Licensing** | BYOL supported | Limited BYOL |
| **Placement** | Control instance placement | No control |
| **Pricing** | Per-host | Per-instance |
| **Cost** | Higher | Lower than hosts |

---

### 2.6 Capacity Reservations

**What are Capacity Reservations?**
- **Reserve capacity in a specific AZ**
- No commitment required
- Charged at On-Demand rate whether used or not

**When to Use:**
- Guarantee capacity for critical workloads
- Short-term capacity needs
- Disaster recovery scenarios

**Types:**
- **On-Demand Capacity Reservations**: Reserve capacity, no discount
- **With RIs or Savings Plans**: Get billing discount + capacity reservation

---

## 3. Other AWS Service Pricing

### S3 Pricing

**Components:**
1. **Storage**: Per GB-month
2. **Requests**: PUT, GET, LIST, etc.
3. **Data Transfer**: Outbound data transfer
4. **Management**: Inventory, analytics, replication

**Storage Classes Pricing (us-east-1):**

| Storage Class | $/GB-month | Use Case |
|--------------|------------|----------|
| **S3 Standard** | $0.023 | Frequent access |
| **S3 Intelligent-Tiering** | $0.023 + $0.0025 monitoring | Unknown access patterns |
| **S3 Standard-IA** | $0.0125 | Infrequent access |
| **S3 One Zone-IA** | $0.01 | Infrequent, non-critical |
| **S3 Glacier Instant** | $0.004 | Archive, instant retrieval |
| **S3 Glacier Flexible** | $0.0036 | Archive, minutes-hours |
| **S3 Glacier Deep Archive** | $0.00099 | Long-term archive, 12-48h |

**Cost Optimization:**
- Use appropriate storage class
- Lifecycle policies to move objects
- S3 Intelligent-Tiering for unknown patterns
- Delete incomplete multipart uploads
- Use S3 Analytics to understand access patterns

---

### RDS Pricing

**Components:**
1. **Instance hours**: Size and type of DB instance
2. **Storage**: GB-month (magnetic, SSD, Provisioned IOPS)
3. **I/O requests**: For magnetic storage
4. **Backups**: Backup storage beyond free allocation
5. **Data Transfer**: Outbound data transfer

**Cost Optimization:**
- Right-size instances
- Use Reserved Instances for production DBs
- Delete unnecessary snapshots
- Use Aurora Serverless for variable workloads
- Multi-AZ only where needed

---

### Lambda Pricing

**Components:**
1. **Requests**: First 1M free, then $0.20 per 1M requests
2. **Duration**: GB-second (memory × execution time)
   - First 400,000 GB-seconds free
   - $0.0000166667 per GB-second after

**Example:**
```
Function: 512 MB memory, runs 100ms
Executions: 1M/month

Request charges: Free (within free tier)
Duration: 1M × 0.512 GB × 0.1s = 51,200 GB-seconds
Charges: 51,200 - 400,000 = 0 (within free tier)
Total: $0
```

**Cost Optimization:**
- Right-size memory allocation
- Optimize function execution time
- Use reserved concurrency wisely (it's charged even if not used)

---

### Data Transfer Pricing

**General Rules:**

**Free:**
- Inbound data transfer (from internet to AWS)
- Data transfer between services in same region
- Data transfer from CloudFront to origin

**Charged:**
- Outbound to internet (tiered pricing)
- Inter-region data transfer
- Data transfer between AZs (small charge)

**Pricing Tiers (Outbound to Internet):**
```
First 10 TB: $0.09/GB
Next 40 TB: $0.085/GB
Next 100 TB: $0.07/GB
Over 150 TB: $0.05/GB
```

**Cost Optimization:**
- Use CloudFront to reduce data transfer costs
- Keep resources in same region
- Use VPC endpoints to avoid NAT Gateway data transfer
- Compress data before transfer

---

## 4. AWS Cost Explorer

### What is Cost Explorer?
- **Visualize and analyze AWS costs**
- Interactive graphs and charts
- Historical data (up to 12 months)
- Forecast future costs (up to 12 months)
- Free to use (API calls are charged)

### Key Features

**1. Cost and Usage Reports:**
- View costs by service, account, region, tag
- Daily or monthly granularity
- Filter and group by multiple dimensions

**2. Graphs and Charts:**
- Time-based trends
- Bar charts, line graphs
- Stacked comparisons

**3. Forecasting:**
- Predict next 3-12 months of costs
- Based on historical usage patterns
- 80% confidence interval

**4. Recommendations:**
- Right-sizing recommendations
- Reserved Instance recommendations
- Savings Plan recommendations

**5. Filtering Options:**
- **Time range**: Last 3, 6, 12 months; custom dates
- **Granularity**: Daily, monthly
- **Service**: Specific AWS services
- **Linked Account**: For Organizations
- **Region**: By AWS region
- **Availability Zone**
- **Instance Type**
- **Usage Type**
- **Tags**: Custom cost allocation tags

**6. Grouping:**
- Service
- Linked account
- Region
- Instance type
- Usage type
- Tag

### Common Use Cases

**1. Identify Cost Drivers:**
```
Question: Which service costs the most?
Filter: Last 6 months
Group by: Service
Result: EC2 = 60%, RDS = 20%, S3 = 10%, Other = 10%
```

**2. Track Cost Trends:**
```
Question: How do costs trend over time?
View: Monthly costs for last 12 months
Insight: Costs increased 20% in last quarter
```

**3. Analyze by Environment:**
```
Question: Production vs Development costs?
Filter: Tag = Environment
Group by: Environment tag
Result: Production = $50K, Development = $10K
```

**4. Regional Cost Analysis:**
```
Question: Which region is most expensive?
Group by: Region
Result: us-east-1 = 70%, eu-west-1 = 20%, ap-south-1 = 10%
```

### Reserved Instance Recommendations

**What It Provides:**
- Analyzes historical On-Demand usage
- Recommends which RIs to purchase
- Shows potential savings
- Different RI terms (1-year, 3-year)
- Different payment options

**Recommendation Criteria:**
- Based on last 7, 30, or 60 days of usage
- Accounts for usage patterns
- Maximizes savings

**Example Recommendation:**
```
Instance Type: m5.large in us-east-1
Current: On-Demand (running 24/7)
Recommendation: 1-year All Upfront Standard RI
Estimated Savings: $1,200/year (40%)
```

### Right-Sizing Recommendations

**What It Provides:**
- Identifies underutilized instances
- Recommends smaller instance types
- Estimates cost savings

**How It Works:**
- Analyzes CloudWatch metrics (CPU, memory, network)
- Identifies instances consistently below threshold
- Recommends downsizing

**Example:**
```
Instance: m5.2xlarge (8 vCPU, 32 GB RAM)
Average CPU: 10%
Average Memory: 20%
Recommendation: Downsize to m5.large (2 vCPU, 8 GB RAM)
Savings: $150/month
```

### Cost Explorer API
- Programmatic access to cost data
- Build custom cost dashboards
- Automate cost analysis
- **Pricing**: $0.01 per API request

---

## 5. AWS Budgets

### What is AWS Budgets?
- **Set custom cost and usage budgets**
- Receive alerts when exceeded
- Track against budget thresholds
- Free tier: First 2 budgets free, $0.02/day per budget after

### Budget Types

**1. Cost Budget:**
- Track actual costs
- Alert when costs exceed threshold
- Example: Alert if monthly cost > $1,000

**2. Usage Budget:**
- Track usage of specific services
- Measured in units (hours, GB, requests)
- Example: Alert if EC2 usage > 1,000 hours/month

**3. Savings Plans Budget:**
- Track Savings Plans utilization
- Alert on low utilization
- Example: Alert if utilization < 90%

**4. Reservation Budget:**
- Track RI utilization and coverage
- Alert on underutilized RIs
- Example: Alert if RI utilization < 80%

### Budget Configuration

**1. Budget Amount:**
- **Fixed**: Same amount each period ($1,000/month)
- **Planned**: Different amounts per period (varies by month)

**2. Budget Period:**
- Daily
- Monthly
- Quarterly
- Annually

**3. Filters:**
- Specific services
- Linked accounts
- Regions
- Tags
- Instance types

**4. Alert Thresholds:**
- Absolute value ($500)
- Percentage of budget (80%)
- Forecasted to exceed

**5. Notifications:**
- Email to recipients
- SNS topic (for automation)
- Chatbot (Slack, Chime)

### Budget Alert Types

**Actual:**
- Alert when actual cost/usage exceeds threshold
- Example: Alert when actual cost > $800

**Forecasted:**
- Alert when forecasted cost/usage will exceed budget
- Uses ML to predict
- Example: Alert if forecasted to exceed $1,000 by end of month

### Budget Actions
- **Automated responses** to budget alerts
- Apply IAM policies
- Stop EC2 or RDS instances
- Target specific groups or users

**Example Budget Action:**
```
Budget: Monthly EC2 costs
Threshold: 100% of budget ($1,000)
Action: Apply IAM policy to deny new EC2 launches
```

### Budget Templates
- **Pre-configured budgets** for common scenarios
- Zero Spend Budget (Free Tier monitoring)
- Monthly Cost Budget
- Daily Savings Plans Coverage Budget

### Best Practices

**1. Start Simple:**
- Create overall monthly cost budget
- Add service-specific budgets later

**2. Use Multiple Thresholds:**
- 50% warning
- 80% alert
- 100% critical

**3. Set Forecasted Alerts:**
- Early warning of budget overruns
- Time to take corrective action

**4. Use SNS for Automation:**
- Trigger Lambda functions
- Automate responses (stop instances, notify teams)

**5. Tag-Based Budgets:**
- Budget per project, team, or environment
- Require cost allocation tags

**Example Budget Setup:**
```
Budget Name: Monthly AWS Costs
Type: Cost Budget
Amount: $5,000/month
Period: Monthly

Alerts:
- 50% ($2,500): Email to finance@company.com
- 80% ($4,000): Email to management@company.com
- 100% ($5,000): Email + SNS to ops-team
- Forecasted 100%: Email to CTO

Filters:
- All services
- All regions
```

---

## 6. AWS Cost and Usage Reports (CUR)

### What is CUR?
- **Most comprehensive cost and usage data**
- Detailed line-item billing information
- Delivered to S3 bucket
- Can be queried with Athena
- Free service (pay for S3 storage)

### Key Features

**Data Included:**
- Line-item details for each service
- Resource IDs
- Usage amounts
- Costs and charges
- Cost allocation tags
- Reserved Instance details
- Savings Plans information

**Format Options:**
- CSV
- Parquet (compressed, columnar)

**Time Granularity:**
- Hourly
- Daily
- Monthly

**Versioning:**
- Overwrite existing report
- Create new report version

### Setting Up CUR

**Steps:**
1. Create S3 bucket for reports
2. Set up CUR in Billing Console
3. Configure report details:
   - Report name
   - Time granularity
   - Include resource IDs (optional)
   - Data integration (Athena, Redshift, QuickSight)
4. Reports delivered daily

**S3 Structure:**
```
s3://my-cur-bucket/
  └── reports/
      └── my-cur-report/
          └── 20260101-20260201/
              ├── my-cur-report-Manifest.json
              ├── my-cur-report-00001.parquet
              └── my-cur-report-00002.parquet
```

### Querying CUR with Athena

**Setup:**
1. Enable Athena integration in CUR settings
2. CUR creates Glue tables automatically
3. Query using Athena

**Example Queries:**

**Total Cost by Service:**
```sql
SELECT 
    line_item_product_code,
    SUM(line_item_unblended_cost) AS cost
FROM cur_database.cur_table
WHERE year = '2026' AND month = '01'
GROUP BY line_item_product_code
ORDER BY cost DESC;
```

**Daily Cost Trend:**
```sql
SELECT 
    line_item_usage_start_date,
    SUM(line_item_unblended_cost) AS daily_cost
FROM cur_database.cur_table
WHERE year = '2026' AND month = '01'
GROUP BY line_item_usage_start_date
ORDER BY line_item_usage_start_date;
```

**Cost by Tag:**
```sql
SELECT 
    resource_tags_user_environment,
    SUM(line_item_unblended_cost) AS cost
FROM cur_database.cur_table
WHERE year = '2026' AND month = '01'
GROUP BY resource_tags_user_environment;
```

### Visualizing with QuickSight
- Connect QuickSight to CUR data in S3
- Create dashboards and visualizations
- Share reports with stakeholders

---

## 7. AWS Cost Allocation Tags

### What are Cost Allocation Tags?
- **Tags to organize and track AWS costs**
- Key-value pairs attached to resources
- Appear in Cost Explorer and CUR
- Enable cost tracking by project, team, environment

### Tag Types

**1. AWS-Generated Tags:**
- Automatically applied by AWS
- Prefix: `aws:`
- Examples:
  - `aws:createdBy`
  - `aws:cloudformation:stack-name`

**2. User-Defined Tags:**
- Created by you
- Custom key-value pairs
- Examples:
  - `Environment: Production`
  - `Project: WebApp`
  - `Team: Engineering`
  - `CostCenter: 12345`

### Activating Tags

**Steps:**
1. Tag resources in AWS Console or via API
2. Go to **Billing → Cost Allocation Tags**
3. **Activate user-defined tags**
4. Wait 24 hours for tags to appear in reports

### Best Practices

**1. Define Tagging Strategy:**
- Standardize tag keys and values
- Document tagging policy
- Enforce with AWS Organizations Tag Policies

**2. Common Tag Categories:**
- **Environment**: Production, Development, Staging
- **Project**: Project or application name
- **Owner**: Team or individual responsible
- **Cost Center**: For chargeback
- **Compliance**: Data classification, compliance requirements

**3. Automate Tagging:**
- Use CloudFormation or Terraform to tag resources
- AWS Systems Manager for bulk tagging
- Lambda to auto-tag based on criteria

**4. Enforce Tagging:**
- IAM policies to require tags
- AWS Config rules to check compliance
- Service Control Policies (SCPs) in Organizations

**Example Tagging Policy:**
```
Required Tags:
- Environment: [Production | Development | Staging]
- Project: <ProjectName>
- Owner: <EmailAddress>
- CostCenter: <CostCenterCode>

Enforcement:
- IAM policy denies resource creation without required tags
- Config rule flags non-compliant resources
```

---

## 8. AWS Organizations and Consolidated Billing

### Consolidated Billing

**What is it?**
- **Single bill for all accounts** in an Organization
- Pay from master/management account
- Volume discounts applied across all accounts
- Free feature

**Benefits:**

**1. Single Payment:**
- One bill for all accounts
- Simplifies accounting

**2. Volume Discounts:**
- Aggregate usage across accounts
- Higher tier pricing applies sooner
- Savings on S3, EC2 data transfer, etc.

**3. Reserved Instance Sharing:**
- RIs purchased in one account can apply to others
- Automatic across organization
- Can disable RI sharing per account

**4. Savings Plans Sharing:**
- Same as RI sharing
- Applied across member accounts

**Example Volume Discount:**
```
Account A: 5 TB data transfer → $0.09/GB
Account B: 5 TB data transfer → $0.09/GB
Account C: 5 TB data transfer → $0.09/GB

Separate: 15 TB × $0.09 = $1,350

Consolidated: 15 TB
- First 10 TB × $0.09 = $900
- Next 5 TB × $0.085 = $425
Total: $1,325
Savings: $25
```

### Cost Allocation in Organizations

**Track costs per account:**
- Cost Explorer: Filter by linked account
- CUR: Separate line items per account
- Budgets: Set per account

**Best Practices:**
- Separate accounts per environment (Prod, Dev, Test)
- Separate accounts per project or team
- Use cost allocation tags across all accounts

---

## 9. Cost Optimization Strategies

### 1. Right-Sizing

**What is Right-Sizing?**
- Match instance types to actual workload needs
- Downsize overprovisioned resources
- Continuous process

**How to Right-Size:**
1. **Monitor Metrics**: CloudWatch CPU, memory, network
2. **Identify Underutilized**: CPU < 20%, Memory < 40%
3. **Test Smaller Instances**: Validate performance
4. **Implement Changes**: Resize during maintenance window
5. **Monitor Post-Change**: Ensure performance is acceptable

**Tools:**
- Cost Explorer Right-Sizing Recommendations
- AWS Compute Optimizer
- CloudWatch metrics and alarms

**Potential Savings:**
- 20-50% reduction in EC2 costs
- Similar savings for RDS, ElastiCache

---

### 2. Purchasing Options Optimization

**Strategy:**
- Use RIs or Savings Plans for steady workloads
- Use Spot for fault-tolerant, flexible workloads
- Use On-Demand for spiky, unpredictable workloads

**Example Mix:**
```
Web Application:
- Baseline (70%): Reserved Instances or Savings Plans
- Variable (20%): On-Demand for scaling
- Batch Processing (10%): Spot Instances
```

**RI/Savings Plan Strategy:**
- Analyze usage patterns
- Start with shorter term (1-year)
- Gradually increase coverage
- Target 60-80% coverage for predictable workloads

---

### 3. Auto Scaling

**Benefits:**
- Scale down during low usage
- Avoid overprovisioning
- Pay only for needed capacity

**Implementation:**
- EC2 Auto Scaling
- DynamoDB Auto Scaling
- Aurora Auto Scaling
- ECS Service Auto Scaling

**Example:**
```
Application without Auto Scaling:
- Provisioned for peak: 10 instances × 24/7
- Cost: 10 × 730 hours × $0.05 = $365/month

With Auto Scaling:
- Average: 4 instances (scaled 2-10 based on load)
- Cost: 4 × 730 hours × $0.05 = $146/month
- Savings: $219/month (60%)
```

---

### 4. Storage Optimization

**S3 Lifecycle Policies:**
- Transition to cheaper storage classes
- Delete old objects automatically

**Example Policy:**
```
Day 0-30: S3 Standard
Day 30-90: S3 Standard-IA
Day 90-365: S3 Glacier Flexible Retrieval
Day 365+: S3 Glacier Deep Archive or delete
```

**EBS Optimization:**
- Delete unused volumes
- Create snapshots and delete old volumes
- Use gp3 instead of gp2 (lower cost, better performance)
- Delete old snapshots

**RDS Storage:**
- Delete unnecessary automated backups
- Use Aurora Serverless for variable workloads
- Archive old data to S3

---

### 5. Network Optimization

**Reduce Data Transfer Costs:**
- Use CloudFront for content delivery
- Keep resources in same region
- Use VPC endpoints instead of NAT Gateways for AWS services
- Compress data before transfer

**Example:**
```
Without CloudFront:
- 100 TB/month from EC2 to internet
- Cost: 100,000 GB × $0.09 = $9,000

With CloudFront:
- EC2 to CloudFront: Free (same region)
- CloudFront to internet: 100,000 GB × $0.085 = $8,500
- Savings: $500/month
```

---

### 6. Serverless Architectures

**Benefits:**
- Pay only for actual usage
- No idle capacity costs
- Automatic scaling

**Serverless Options:**
- Lambda instead of EC2
- Aurora Serverless instead of RDS
- DynamoDB On-Demand instead of provisioned
- Fargate instead of EC2 for containers

**Example:**
```
API Backend:
- EC2 (t3.medium 24/7): $30/month minimum
- Lambda: $0 (within free tier for low traffic)
  Or $5-10/month for moderate traffic
```

---

### 7. Delete Unused Resources

**Common Waste:**
- Stopped but not terminated EC2 instances (EBS charges)
- Unattached EBS volumes
- Old snapshots
- Unused Elastic IPs
- Old AMIs
- Idle Load Balancers
- Underutilized RDS instances

**Cleanup Process:**
- Use AWS Config to identify unused resources
- Implement tagging to track resource owners
- Automated cleanup with Lambda
- Regular audits (monthly or quarterly)

---

### 8. Use AWS Compute Optimizer

**What is Compute Optimizer?**
- **ML-powered recommendations**
- Optimal EC2 instance types
- Auto Scaling group configurations
- EBS volume configurations
- Lambda function memory settings

**How It Works:**
- Analyzes CloudWatch metrics
- Uses machine learning
- Recommends optimized configurations
- Estimates cost savings

**Pricing:**
- Free for recommendations based on last 14 days
- Enhanced recommendations (3 months): Additional charge

---

### 9. Monitor and Review Regularly

**Establish Review Cadence:**
- Weekly: Monitor budgets and alerts
- Monthly: Review Cost Explorer, identify anomalies
- Quarterly: Deep dive analysis, right-sizing, RI/SP review
- Annually: Strategic planning, TCO analysis

**Key Metrics to Track:**
- Total monthly cost
- Cost per service
- Cost per environment/project
- Cost per customer (for SaaS)
- Cost trends (month-over-month, year-over-year)

---

## 10. Additional Cost Management Tools

### AWS Trusted Advisor

**What is it?**
- **Automated best practice checks**
- Cost optimization recommendations
- Part of Support plans

**Cost Optimization Checks:**

**Free Tier (Basic/Developer Support):**
- Service limits
- Some security checks

**Full Tier (Business/Enterprise Support):**
- Underutilized EC2 instances
- Idle RDS instances
- Unassociated Elastic IPs
- Low utilization EBS volumes
- Underutilized RIs
- EC2 Reserved Instance optimization

**Accessing Trusted Advisor:**
- AWS Console → Trusted Advisor
- API for programmatic access
- CloudWatch Events for automated actions

---

### AWS Pricing Calculator

**What is it?**
- **Estimate costs for AWS services**
- Create detailed cost estimates
- Share and export estimates

**Features:**
- Service-by-service configuration
- Multiple pricing models
- Regional pricing
- Grouping (by service, by architecture tier)
- Export to CSV, PDF

**Use Cases:**
- Architecture planning
- Budget approval
- Proof of concept costing
- Migration planning

**Example:**
```
Architecture: Web Application
- 3× m5.large EC2 instances (On-Demand): $182/month
- Application Load Balancer: $25/month
- RDS db.m5.large (Multi-AZ): $300/month
- 500 GB S3 Standard: $11.50/month
- 1 TB data transfer: $90/month
Total: $608.50/month
```

---

### AWS Migration Hub (TCO Analysis)

**Migration Evaluator** (formerly TSO Logic):
- Build business case for cloud migration
- Assess on-premises infrastructure
- Project AWS costs
- Compare TCO (on-premises vs AWS)

---

### Third-Party Tools

**Popular Options:**
- **CloudHealth** (VMware): Multi-cloud cost management
- **CloudCheckr**: Cost optimization and security
- **Spot.io**: Automated Spot Instance management
- **ProsperOps**: Autonomous RI/SP management
- **Kubecost**: Kubernetes cost monitoring

---

## 11. Cost Optimization Pillars (Well-Architected)

### AWS Well-Architected Framework - Cost Optimization

**5 Design Principles:**

**1. Implement Cloud Financial Management**
- Establish cost transparency
- Dedicated team or individual
- Regular reviews

**2. Adopt a Consumption Model**
- Pay only for what you use
- Scale up/down based on demand
- No overprovisioning

**3. Measure Overall Efficiency**
- Measure business value
- Cost per transaction
- Cost per user

**4. Stop Spending on Undifferentiated Heavy Lifting**
- Use managed services
- Focus on business value, not infrastructure

**5. Analyze and Attribute Expenditure**
- Understand who is spending what
- Cost allocation tags
- Chargeback/showback models

**Best Practices:**
- Practice Cloud Financial Management
- Expenditure and usage awareness
- Cost-effective resources
- Manage demand and supply
- Optimize over time

---

## 12. Exam Tips Summary

### Key Concepts

✅ **EC2 Pricing Models**
- **On-Demand**: No commitment, short-term
- **Reserved**: 1-3 year commitment, up to 72% savings
- **Savings Plans**: Flexible, $/hour commitment
- **Spot**: Up to 90% savings, can be interrupted
- **Dedicated Hosts**: BYOL, compliance

✅ **Cost Explorer**
- Visualize and analyze costs
- Forecasting
- Right-sizing and RI recommendations
- Filter and group by tags, service, region

✅ **AWS Budgets**
- Set cost and usage budgets
- Actual and forecasted alerts
- 4 types: Cost, Usage, Savings Plans, Reservation
- Budget Actions for automation

✅ **Cost Allocation Tags**
- Track costs by project, team, environment
- Must be activated in Billing Console
- Appear in Cost Explorer and CUR after 24 hours

✅ **Consolidated Billing**
- Single bill for all accounts in Organization
- Volume discounts across accounts
- RI and Savings Plans sharing

✅ **Optimization Strategies**
- Right-sizing (match instance to workload)
- Use RIs/Savings Plans for steady workloads
- Spot for fault-tolerant workloads
- Auto Scaling to avoid overprovisioning
- S3 Lifecycle policies
- Delete unused resources

### Common Scenarios

**Scenario 1: Reduce EC2 costs for steady workload**
- **Solution**: Purchase Reserved Instances or Savings Plans
- 1-year or 3-year commitment, up to 72% savings

**Scenario 2: Batch processing workload, flexible timing**
- **Solution**: Spot Instances
- Up to 90% savings, handle interruptions gracefully

**Scenario 3: Track costs per project**
- **Solution**: Cost allocation tags
- Tag resources with Project tag, filter in Cost Explorer

**Scenario 4: Alert when monthly cost exceeds $5,000**
- **Solution**: AWS Budgets
- Create cost budget with alert at $5,000 threshold

**Scenario 5: Identify underutilized EC2 instances**
- **Solution**: Cost Explorer Right-Sizing Recommendations
- Or AWS Compute Optimizer

**Scenario 6: Reduce S3 storage costs for old data**
- **Solution**: S3 Lifecycle policies
- Transition to Glacier or Deep Archive after X days

**Scenario 7: Detailed cost analysis and querying**
- **Solution**: Cost and Usage Reports (CUR) + Athena
- Query with SQL for custom analysis

**Scenario 8: Single bill for multiple AWS accounts**
- **Solution**: AWS Organizations with Consolidated Billing
- Volume discounts and RI sharing

---

## 13. Hands-On Practice

### Lab 1: Cost Explorer
1. Open Cost Explorer in Billing Console
2. View last 6 months of costs
3. Group by Service
4. Filter by specific tag
5. Create forecast for next 3 months

### Lab 2: AWS Budgets
1. Create monthly cost budget ($100)
2. Set alert thresholds (50%, 80%, 100%)
3. Configure email notifications
4. Test by creating resources to trigger alert

### Lab 3: Cost Allocation Tags
1. Tag EC2 instances with Environment and Project tags
2. Activate tags in Billing Console
3. Wait 24 hours
4. Filter Cost Explorer by tags

### Lab 4: Reserved Instance Purchase
1. Review RI recommendations in Cost Explorer
2. Analyze potential savings
3. Purchase 1-year RI for steady workload (test with t3.micro)
4. Verify RI application in next bill

### Lab 5: Right-Sizing
1. Launch oversized EC2 instance (e.g., m5.xlarge)
2. Monitor CloudWatch metrics (CPU, network)
3. Use Cost Explorer right-sizing recommendations
4. Downsize to appropriate instance type

---

## 14. Additional Resources

### AWS Documentation
- [AWS Pricing](https://aws.amazon.com/pricing/)
- [Cost Management](https://aws.amazon.com/aws-cost-management/)
- [Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)
- [Well-Architected Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/)

### Tools
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS TCO Calculator (Legacy)](https://aws.amazon.com/tco-calculator/)
- [AWS Free Tier](https://aws.amazon.com/free/)

### Whitepapers
- Cost Optimization Pillar - AWS Well-Architected Framework
- Cost Optimization Best Practices

---

## Quick Reference

| Tool | Purpose | Key Feature |
|------|---------|-------------|
| **Cost Explorer** | Visualize and analyze costs | Graphs, forecasting, recommendations |
| **AWS Budgets** | Set cost/usage budgets | Alerts, actions, tracking |
| **CUR** | Detailed billing data | Line-item details, query with Athena |
| **Cost Allocation Tags** | Track costs by category | Tag resources, filter in tools |
| **Trusted Advisor** | Best practice checks | Cost optimization recommendations |
| **Pricing Calculator** | Estimate costs | Plan and budget for AWS services |
| **Compute Optimizer** | ML-powered recommendations | Optimal instance types and sizes |
| **Consolidated Billing** | Single bill for Organization | Volume discounts, RI sharing |

---

**Next Module:** [14-Practice →](../14-Practice/README.md)

**Previous Module:** [← 12-Architecture-Patterns](../12-Architecture-Patterns/README.md)

