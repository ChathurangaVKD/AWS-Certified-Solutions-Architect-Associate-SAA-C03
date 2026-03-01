# Targeted Practice Questions - Common Weak Areas

These questions focus specifically on topics where candidates commonly struggle in SAA-C03 practice exams.

---

## Section 1: IAM Policy Evaluation & Cross-Account Access (20 Questions)

### Question 1
A company has an S3 bucket with a bucket policy that explicitly denies access to all users. An IAM user has been granted full S3 admin permissions via an IAM policy attached to their user account. What will happen when the user tries to access objects in the bucket?

**A)** The user can access the bucket because IAM policies take precedence over bucket policies  
**B)** Access is denied because explicit deny always takes precedence  
**C)** The user can only read objects but cannot write  
**D)** Access depends on which policy was created first

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- In AWS policy evaluation, an explicit DENY always wins, regardless of any ALLOW statements
- The evaluation order is: Explicit DENY → Explicit ALLOW → Implicit DENY (default)
- Even though the IAM policy allows full S3 access, the explicit deny in the bucket policy overrides it
- This is a critical concept for the exam: **DENY ALWAYS WINS**

**Key Point:** Any explicit deny in any policy (identity-based, resource-based, SCPs, permission boundaries) will deny access, regardless of any allows.
</details>

---

### Question 2
A Solutions Architect needs to allow an IAM user in Account A (111111111111) to access an S3 bucket in Account B (222222222222). The user needs to copy files from Account A's S3 bucket to Account B's S3 bucket. Which approach is MOST appropriate?

**A)** Create an IAM role in Account B that the user can assume  
**B)** Use a resource-based bucket policy in Account B  
**C)** Share IAM credentials between accounts  
**D)** Create a VPC peering connection

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- When copying between S3 buckets in different accounts, you need access to BOTH buckets simultaneously
- **IAM Role (Option A)**: When you assume a role, you temporarily give up your original permissions, so you couldn't access Account A's bucket
- **Resource-based policy (Option B - Correct)**: Allows cross-account access while retaining original permissions, enabling access to both buckets
- Option C violates security best practices
- Option D is for networking, not S3 access

**Scenario Pattern:** 
- Need sequential access to resources → IAM Role
- Need simultaneous access to resources in both accounts → Resource-based policy

**Policy Example:**
```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111111111111:user/username"},
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::account-b-bucket/*"
}
```
</details>

---

### Question 3
A company uses AWS Organizations with multiple accounts. They want to prevent any user, including the root user, from launching EC2 instances in the us-east-1 region across all accounts. How can this be achieved?

**A)** Create an IAM policy denying EC2 actions in us-east-1 and attach it to all users  
**B)** Use AWS Config to detect and terminate instances in us-east-1  
**C)** Create a Service Control Policy (SCP) denying EC2 actions in us-east-1  
**D)** Enable region restrictions in the AWS Management Console

<details>
<summary>Answer</summary>

**Correct Answer: C**

**Explanation:**
- **Service Control Policies (SCPs)** are the only way to restrict the root user in member accounts
- SCPs act as guardrails and affect ALL users including root
- They don't grant permissions; they set maximum permissions boundaries

**Why others are wrong:**
- **A**: IAM policies don't affect the root user
- **B**: Config is for compliance detection/remediation, not prevention
- **D**: No such feature exists

**SCP Example:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": "ec2:RunInstances",
    "Resource": "*",
    "Condition": {
      "StringEquals": {
        "aws:RequestedRegion": "us-east-1"
      }
    }
  }]
}
```

**Key Point:** SCPs don't affect service-linked roles and are the only way to restrict root users in AWS Organizations.
</details>

---

### Question 4
An application needs to access AWS services using temporary credentials. The application runs on-premises and users authenticate via Active Directory. What is the BEST solution?

**A)** Create IAM users for each employee and provide access keys  
**B)** Use AWS IAM Identity Center (SSO) with SAML federation  
**C)** Create an IAM role and provide the role credentials to the application  
**D)** Use Cognito User Pools

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **SAML 2.0 federation** with AWS IAM Identity Center is designed for corporate identity integration
- Provides temporary credentials via STS (Security Token Service)
- No need to create IAM users for each employee
- Follows AWS best practice of federation instead of IAM users

**Flow:**
```
User → Active Directory → SAML IdP → AWS STS → Temporary Credentials
```

**Why others are wrong:**
- **A**: Long-term credentials are security risk, violates best practices
- **C**: Roles need to be assumed by a principal; static role credentials don't exist
- **D**: Cognito User Pools are for web/mobile app user authentication, not enterprise AD integration (though Cognito Identity Pools could work with proper setup, IAM Identity Center is more appropriate for AD)

**Exam Tip:** Active Directory + AWS access = SAML federation or AWS IAM Identity Center
</details>

---

### Question 5
A developer has permissions via an IAM policy that allows all S3 actions. However, a permission boundary is attached that only allows read operations on S3. What actions can the developer perform?

**A)** All S3 actions because IAM policies take precedence  
**B)** Only read operations on S3  
**C)** No actions because of conflicting policies  
**D)** Only write operations on S3

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Permission boundaries** set the MAXIMUM permissions a user can have
- Effective permissions = IAM policy ∩ Permission boundary
- Even though the IAM policy allows all actions, the permission boundary limits to read-only

**Visual representation:**
```
IAM Policy: {S3:*}
Permission Boundary: {S3:Get*, S3:List*}
Effective Permissions: {S3:Get*, S3:List*} (intersection)
```

**Use Case:** Permission boundaries are commonly used when delegating user/role creation to prevent privilege escalation.

**Example:**
- Admin can create users but permission boundary ensures they can't create a user with more permissions than the boundary allows.
</details>

---

### Question 6
A company has multiple AWS accounts and wants to implement centralized user access management for AWS console and CLI access across all accounts. Which solution provides this with the LEAST operational overhead?

**A)** Create IAM users in each account and manage credentials centrally  
**B)** Use AWS IAM Identity Center (AWS SSO) with automatic provisioning  
**C)** Implement cross-account IAM roles and distribute assume-role instructions  
**D)** Use AWS Directory Service in each account

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **AWS IAM Identity Center (formerly AWS SSO)** is designed exactly for this use case
- Provides single sign-on across multiple AWS accounts and applications
- Supports automatic user provisioning from identity sources (Active Directory, Okta, Azure AD, etc.)
- Users get temporary credentials automatically
- Least operational overhead

**Features:**
- One login for multiple accounts
- Integrates with AWS Organizations
- SAML 2.0 compatible
- Can use AWS's built-in directory or external IdP

**Why others are wrong:**
- **A**: High operational overhead (manage users in each account)
- **C**: Complex for users, requires manual assume-role process
- **D**: Still requires individual account management

**Exam Pattern:** "Centralized access" + "multiple accounts" + "least overhead" = AWS IAM Identity Center
</details>

---

### Question 7
An IAM policy grants access to S3, but there's also an SCP that denies S3 access, and a permission boundary that allows S3 access. What is the effective permission?

**A)** Allow access (permission boundary wins)  
**B)** Deny access (SCP deny wins)  
**C)** Allow access (IAM policy wins)  
**D)** No access (conflicting policies cancel out)

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- Policy evaluation logic in AWS:
  1. Explicit DENY in ANY policy → Access DENIED (stops here)
  2. Check if action allowed by ALL applicable boundaries (Identity policy AND Permission boundary AND SCP)
  3. If not explicitly allowed → Implicit DENY

**Evaluation Order:**
```
SCP: DENY S3 → [Access Denied - stops here]
Permission Boundary: ALLOW S3
IAM Policy: ALLOW S3
```

**Key Rule:** A single explicit deny anywhere overrides all allows.

**Real-world Example:**
```
Organization SCP: Denies launching instances in certain regions
↓
Overrides ALL other policies, even account admin policies
```
</details>

---

### Question 8
A third-party security auditing company needs temporary access to your AWS account to perform compliance scans. What is the MOST secure way to grant this access?

**A)** Create an IAM user with temporary password that expires in 24 hours  
**B)** Create an IAM role with an External ID and provide the role ARN to the third party  
**C)** Share root account credentials temporarily  
**D)** Create an access key and share it, then delete after audit

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **External ID** is specifically designed for the "confused deputy" problem in cross-account scenarios
- Prevents a third party from assuming your role using another customer's account

**How it works:**
1. You create a role that trusts the third-party account
2. You set a unique External ID (like a password between you and the third party)
3. Third party can only assume the role if they provide the correct External ID

**Role Trust Policy Example:**
```json
{
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::AUDITOR-ACCOUNT:root"},
  "Action": "sts:AssumeRole",
  "Condition": {
    "StringEquals": {
      "sts:ExternalId": "unique-external-id-12345"
    }
  }
}
```

**Why others are wrong:**
- **A**: IAM users are for long-term access; roles provide temporary credentials
- **C**: Never share root credentials!
- **D**: Access keys are long-term credentials, security risk

**Exam Tip:** "Third-party access" + "cross-account" = IAM Role with External ID
</details>

---

### Question 9
An application running on EC2 needs to access DynamoDB. What is the MOST secure way to provide credentials?

**A)** Store AWS access keys in environment variables on the EC2 instance  
**B)** Attach an IAM role to the EC2 instance  
**C)** Embed access keys in the application code  
**D)** Store credentials in an S3 bucket and retrieve them at runtime

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **IAM roles for EC2** provide temporary credentials automatically
- Credentials rotate automatically
- No need to store long-term credentials
- Uses EC2 instance metadata service to retrieve credentials

**How it works:**
```
EC2 Instance → Instance Profile (IAM Role) → Temporary credentials from STS
                                            → Access DynamoDB
```

**Benefits:**
- Automatic credential rotation (multiple times per day)
- No credentials to manage or store
- Credentials never leave AWS infrastructure
- Can be updated without restarting instance

**Why others are wrong:**
- **A, C, D**: All involve storing long-term credentials, which is a security risk

**Exam Pattern:** "EC2 needs to access AWS service" = IAM Role attached to EC2
</details>

---

### Question 10
A company wants to ensure that their developers can only launch t3.micro and t3.small instances. How can this be enforced?

**A)** Create a resource-based policy on EC2  
**B)** Use an IAM policy with a condition on ec2:InstanceType  
**C)** Configure AWS Config rules to terminate non-compliant instances  
**D)** Use AWS Systems Manager to enforce instance type restrictions

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- IAM policy conditions can restrict specific instance types
- This prevents the action from succeeding in the first place (prevention)

**Policy Example:**
```json
{
  "Effect": "Allow",
  "Action": "ec2:RunInstances",
  "Resource": "arn:aws:ec2:*:*:instance/*",
  "Condition": {
    "StringEquals": {
      "ec2:InstanceType": ["t3.micro", "t3.small"]
    }
  }
}
```

**Why others are wrong:**
- **A**: EC2 doesn't support resource-based policies (only identity-based and SCPs)
- **C**: Config is detective (after the fact), not preventive
- **D**: Systems Manager doesn't prevent instance launches

**Condition Keys to Remember:**
- `ec2:InstanceType` - Instance type restriction
- `aws:RequestedRegion` - Region restriction
- `aws:SourceIp` - IP-based restriction
- `aws:SecureTransport` - Require HTTPS

**Exam Tip:** Prevention (IAM policy condition) is better than detection (Config).
</details>

---

## Section 2: Database Selection & Configuration (20 Questions)

### Question 11
A company needs a database for a high-traffic e-commerce application. They require SQL compatibility, automatic failover, and the ability to serve read traffic from up to 15 read replicas. Which solution meets these requirements?

**A)** Amazon RDS for MySQL with Multi-AZ and 5 read replicas  
**B)** Amazon Aurora MySQL with Multi-AZ and 15 read replicas  
**C)** Amazon DynamoDB with Global Tables  
**D)** Amazon RDS for PostgreSQL with Multi-AZ

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Aurora** supports up to 15 read replicas (RDS only supports 5)
- Aurora MySQL is SQL-compatible
- Aurora Multi-AZ provides automatic failover (6 copies across 3 AZs)
- Aurora is designed for high-traffic applications

**Aurora Advantages:**
- 5x performance of standard MySQL
- Storage auto-scales (10GB → 128TB)
- Faster replication (typically <100ms lag)
- Backtrack feature (point-in-time recovery without restore)

**Why others are wrong:**
- **A**: RDS only supports up to 5 read replicas (not 15)
- **C**: DynamoDB is NoSQL, not SQL-compatible
- **D**: Doesn't mention read replicas, and RDS limited to 5

**Exam Tip:** "15 read replicas" or "highest performance" = Aurora
</details>

---

### Question 12
An application requires a database that can handle 100,000 reads per second with single-digit millisecond latency. Data access patterns are unpredictable. Cost optimization is important. Which database is MOST appropriate?

**A)** Amazon RDS with read replicas  
**B)** Amazon DynamoDB with on-demand pricing  
**C)** Amazon Aurora with provisioned IOPS  
**D)** Amazon ElastiCache

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **DynamoDB** is designed for high throughput (millions of requests per second)
- Single-digit millisecond latency
- **On-demand pricing** is perfect for unpredictable access patterns
- Auto-scales to workload
- No need to provision capacity

**Why DynamoDB**:
- Fully managed NoSQL
- Scales horizontally
- No read replica management needed
- Pay-per-request with on-demand mode

**Why others are wrong:**
- **A**: RDS isn't designed for 100K+ reads/sec
- **C**: Aurora is powerful but requires capacity planning
- **D**: ElastiCache is for caching, not primary database

**Access Pattern Decision:**
```
Unpredictable → DynamoDB On-Demand
Predictable → DynamoDB Provisioned
Need SQL → RDS/Aurora
```

**Exam Pattern:** "Unpredictable traffic" + "high throughput" = DynamoDB On-Demand
</details>

---

### Question 13
A financial application requires a database solution that supports ACID transactions, can handle multiple record updates atomically, and needs SQL querying. The application has predictable traffic patterns. What is the BEST solution?

**A)** DynamoDB with transactions enabled  
**B)** Amazon RDS for PostgreSQL with Multi-AZ  
**C)** Amazon Aurora Serverless  
**D)** Amazon Redshift

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **ACID transactions** + **SQL querying** points to relational database
- RDS PostgreSQL fully supports ACID transactions
- Multi-AZ provides high availability
- Predictable traffic suits RDS's provisioned capacity model

**ACID Requirements:**
- **A**tomicity: All or nothing
- **C**onsistency: Data integrity
- **I**solation: Concurrent transactions don't interfere
- **D**urability: Committed data persists

**Why others are wrong:**
- **A**: While DynamoDB supports transactions, it's NoSQL (no SQL querying capability)
- **C**: Aurora Serverless is good, but overkill if traffic is predictable; standard RDS is more cost-effective
- **D**: Redshift is for data warehousing/analytics, not transactional workloads

**Database Selection:**
```
ACID + SQL + Predictable → RDS
ACID + SQL + Variable → Aurora (Serverless for highly variable)
ACID + NoSQL → DynamoDB with transactions
```
</details>

---

### Question 14
A company is migrating an on-premises MySQL database to AWS. They need to minimize downtime and keep the source database operational during migration. What is the BEST approach?

**A)** Take a database backup, upload to S3, restore to RDS  
**B)** Use AWS Database Migration Service (DMS) with continuous replication  
**C)** Export database to CSV files and import to RDS  
**D)** Use AWS DataSync to sync the database

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **AWS DMS** is specifically designed for database migrations with minimal downtime
- Supports continuous data replication (CDC - Change Data Capture)
- Source database remains operational during migration

**DMS Migration Process:**
1. **Full Load**: Initial complete data copy
2. **CDC (Change Data Capture)**: Replicate ongoing changes
3. **Cutover**: Switch application to target database

**Why others are wrong:**
- **A**: Requires downtime (backup/restore period)
- **C**: Manual, error-prone, significant downtime
- **D**: DataSync is for file transfers, not databases

**Migration Types:**
- **Homogeneous** (MySQL → MySQL): DMS alone
- **Heterogeneous** (MySQL → PostgreSQL): DMS + Schema Conversion Tool (SCT)

**Exam Tip:** "Minimal downtime database migration" = DMS with CDC
</details>

---

### Question 15
An application needs to cache session data for thousands of concurrent users. The cache must support automatic failover and data persistence. Which solution is MOST appropriate?

**A)** Amazon ElastiCache for Memcached with multiple nodes  
**B)** Amazon ElastiCache for Redis with Multi-AZ  
**C)** DynamoDB with DAX  
**D)** RDS with read replicas

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Redis with Multi-AZ** provides:
  - Automatic failover
  - Data persistence (RDB + AOF)
  - Replication
  - Backup and restore

**Redis vs Memcached:**
```
Feature              | Redis | Memcached
---------------------|-------|----------
Persistence          | ✅    | ❌
Multi-AZ failover    | ✅    | ❌
Backups              | ✅    | ❌
Replication          | ✅    | ❌
Complex data types   | ✅    | ❌ (strings only)
```

**Why others are wrong:**
- **A**: Memcached doesn't support persistence or automatic failover
- **C**: DAX is specifically for DynamoDB caching
- **D**: RDS is not appropriate for session caching (too slow, too expensive)

**Session Store Requirements:**
```
Need persistence + failover → Redis
Simple cache, no persistence → Memcached
```

**Exam Tip:** "Persistence" or "backup" or "Multi-AZ" for caching = Redis
</details>

---

### Question 16
A company needs to store 500 TB of data for a data warehouse solution with complex SQL queries. The data is accessed regularly but queries can tolerate a few seconds of latency. What is the MOST cost-effective solution?

**A)** Amazon Aurora with Provisioned IOPS  
**B)** Amazon Redshift with dense compute nodes  
**C)** Amazon RDS for PostgreSQL  
**D)** Amazon Athena querying data in S3

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Amazon Redshift** is specifically designed for data warehousing
- Columnar storage optimized for analytics
- Handles petabyte-scale data
- Cost-effective for large datasets with complex queries

**Why Redshift:**
- Massively parallel processing (MPP)
- Column-oriented storage
- Data compression
- Result caching
- Mature product with SQL support

**Node Types:**
- **DC2 (Dense Compute)**: Better price/performance for < 500GB
- **RA3 (Managed Storage)**: Separate compute/storage scaling, better for 500GB+ (exam may expect this, but question says 500TB, both could work)

**Why others are wrong:**
- **A**: Aurora is for transactional workloads, not analytics
- **C**: RDS not designed for data warehousing scale
- **D**: Athena is serverless but performance isn't as good as Redshift for regular, complex queries

**Data Warehouse Decision:**
```
Ad-hoc queries on S3 → Athena
Regular complex queries, 500GB-PB → Redshift
Real-time analytics → Kinesis Analytics
```

**Exam Tip:** "Data warehouse" + "TB/PB scale" = Redshift
</details>

---

### Question 17
An application stores user profiles in a database. Each user profile is a JSON document with varying attributes. Users are identified by email address and frequently need to query by country. What database is MOST suitable?

**A)** Amazon RDS with JSON columns  
**B)** Amazon DynamoDB with a Global Secondary Index  
**C)** Amazon DocumentDB  
**D)** Amazon S3 with Athena

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **DynamoDB** is ideal for key-value and document storage
- Native JSON support
- **Global Secondary Index (GSI)** allows querying by country (alternate query pattern)
- Fully managed, high performance

**DynamoDB Design:**
```
Primary Key: email (partition key)
GSI: country (partition key) + email (sort key)

Queries:
- Get user by email → Query on main table
- Get users by country → Query on GSI
```

**Why others are wrong:**
- **A**: RDS works but less optimal for flexible schemas
- **C**: DocumentDB (MongoDB-compatible) works but DynamoDB is simpler and more cost-effective for this use case
- **D**: S3 + Athena is for analytics, not operational data store

**DynamoDB vs DocumentDB:**
```
DynamoDB:
- Key-value + document
- Serverless scaling
- Single-digit millisecond latency
- Pay per request available

DocumentDB:
- Full MongoDB compatibility
- Need MongoDB features (aggregation pipelines, etc.)
- Managed instances (not serverless)
```

**Exam Tip:** "JSON documents" + "key-value access" = DynamoDB
</details>

---

### Question 18
A gaming application stores player scores that need to be ranked globally. The leaderboard must update in real-time and support range queries like "top 100 players." What solution is BEST?

**A)** DynamoDB with sort keys  
**B)** ElastiCache for Redis with sorted sets  
**C)** RDS with indexed rankings  
**D)** Elasticsearch

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Redis Sorted Sets** are specifically designed for leaderboards
- Maintain automatic ordering
- O(log N) time complexity for most operations
- Atomic operations
- Real-time updates

**Redis Commands:**
```
ZADD leaderboard 9500 "player1"  # Add score
ZREVRANGE leaderboard 0 99        # Get top 100
ZRANK leaderboard "player1"       # Get player's rank
ZINCRBY leaderboard 50 "player1"  # Increment score
```

**Why Redis wins:**
- Sub-millisecond latency
- Built-in sorted sets
- Atomic increment operations
- Range queries built-in

**Why others are wrong:**
- **A**: DynamoDB would require complex design and can't efficiently maintain global rankings
- **C**: RDS too slow for real-time updates at scale
- **D**: Elasticsearch is for full-text search, not optimized for this

**Redis Use Cases to Remember:**
- Leaderboards (sorted sets)
- Real-time analytics (counters)
- Session store (key-value)
- Pub/Sub messaging
- Rate limiting

**Exam Tip:** "Leaderboard" or "ranked list" or "real-time scores" = Redis Sorted Sets
</details>

---

### Question 19
A company has an RDS MySQL database in us-east-1. They need a disaster recovery solution in us-west-2 with an RTO of 5 minutes and RPO of 1 minute. What is the BEST solution?

**A)** RDS Multi-AZ in us-east-1  
**B)** RDS read replica in us-west-2, promote in case of disaster  
**C)** Regular snapshots to S3 with cross-region copy  
**D)** AWS Backup with cross-region replication

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Cross-region read replica** provides:
  - Asynchronous replication (RPO typically < 1 minute)
  - Can be promoted to standalone DB (RTO ~ 5 minutes)
  - Always up-to-date replica ready in DR region

**Multi-AZ vs Read Replica:**
```
Multi-AZ:
- Same region (AZ-level failure)
- Automatic failover (60-120 sec)
- Synchronous replication
- RTO: ~2 min, RPO: ~0

Cross-Region Read Replica:
- Different region (region-level failure)
- Manual promotion
- Asynchronous replication
- RTO: ~5 min, RPO: ~1 min
```

**Why others are wrong:**
- **A**: Multi-AZ only protects against AZ failure, not region failure
- **C**: Snapshots have RPO in hours (snapshot frequency)
- **D**: Similar to C, backup-based solutions have higher RTO/RPO

**DR Strategy Selection:**
```
RTO/RPO Requirements → Solution
Minutes/Seconds      → Read Replica
Hours/Hours          → Automated Snapshots
Days/Hours           → Manual Backups
```

**Exam Tip:** "Cross-region DR" + "low RTO/RPO" = Cross-region read replica
</details>

---

### Question 20
An application needs to store structured data with the following requirements: millions of writes per second, predictable query patterns (key-value lookups), and the ability to automatically delete items after 30 days. Which solution is MOST suitable?

**A)** DynamoDB with on-demand capacity and TTL enabled  
**B)** Aurora with auto-scaling  
**C)** RDS with automated backups  
**D)** ElastiCache for Redis

<details>
<summary>Answer</summary>

**Correct Answer: A**

**Explanation:**
- **DynamoDB** handles millions of requests per second
- **TTL (Time to Live)** automatically deletes expired items (no cost for deletes)
- **On-demand capacity** handles unpredictable write volumes
- Key-value lookups are DynamoDB's strength

**DynamoDB TTL:**
```
- Set TTL attribute (unix timestamp)
- DynamoDB automatically deletes expired items within 48 hours
- No write capacity consumed for deletes
- Perfect for temporary data (sessions, logs, events)
```

**Why others are wrong:**
- **B, C**: RDS/Aurora can't scale to millions of writes/sec
- **D**: ElastiCache is for caching, not primary data store

**DynamoDB Features for Exam:**
- **TTL**: Auto-delete expired items
- **Streams**: Capture item-level changes
- **Global Tables**: Multi-region replication
- **On-Demand**: Auto-scaling, pay per request
- **Provisioned**: Set capacity, lower cost if predictable
- **DAX**: Microsecond latency caching layer

**Exam Tip:** "Millions of requests/sec" + "key-value" = DynamoDB
</details>

---

## Section 3: Networking (VPC, Security Groups, Load Balancers) (20 Questions)

### Question 21
An application running in a private subnet needs to access S3 and DynamoDB without traversing the internet. What is the MOST cost-effective solution?

**A)** Deploy a NAT Gateway and route traffic through it  
**B)** Create VPC endpoints for S3 and DynamoDB  
**C)** Use AWS PrivateLink for S3 and DynamoDB  
**D)** Create an internet gateway and security rules

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **VPC Gateway Endpoints** for S3 and DynamoDB are FREE
- Traffic stays within AWS network
- No internet gateway or NAT required
- Update route table to point to endpoint

**VPC Endpoint Types:**
```
Gateway Endpoints (FREE):
- S3
- DynamoDB
- Uses route table entries

Interface Endpoints ($0.01/hour + data):
- Most other AWS services (100+)
- Uses ENI with private IP
- Powered by AWS PrivateLink
```

**Why others are wrong:**
- **A**: NAT Gateway costs $0.045/hour + data transfer charges
- **C**: PrivateLink is for interface endpoints (costs money); S3/DynamoDB use gateway endpoints
- **D**: Internet gateway requires public IPs and NAT

**Configuration:**
```
1. Create Gateway Endpoint for S3
2. Create Gateway Endpoint for DynamoDB
3. Associate with route table
4. Update security groups (allow HTTPS)
```

**Exam Tip:** "Private subnet access to S3/DynamoDB" = Gateway VPC Endpoints (free)
</details>

---

### Question 22
A company needs to route traffic to EC2 instances based on the URL path: /api/* should go to API servers and /web/* should go to web servers. Which load balancer should be used?

**A)** Classic Load Balancer  
**B)** Network Load Balancer  
**C)** Application Load Balancer  
**D)** Gateway Load Balancer

<details>
<summary>Answer</summary>

**Correct Answer: C**

**Explanation:**
- **Application Load Balancer (ALB)** operates at Layer 7 (HTTP/HTTPS)
- Supports path-based routing
- Also supports host-based routing, HTTP header routing, query string routing

**ALB Routing Example:**
```
Rule 1: Path = /api/* → Target Group: API-Servers
Rule 2: Path = /web/* → Target Group: Web-Servers
Rule 3: Default → Target Group: Default-Servers
```

**Load Balancer Comparison:**
```
ALB (Layer 7):
- HTTP/HTTPS/gRPC
- Path, host, header routing
- WebSockets, HTTP/2
- Lambda targets
- Use: Web apps, microservices

NLB (Layer 4):
- TCP/UDP/TLS
- Ultra-high performance
- Static IP support
- Use: Extreme performance needs, non-HTTP

GWLB (Layer 3):
- Deploy security appliances
- GENEVE protocol
- Use: Firewalls, IDS/IPS

CLB (Legacy):
- Layer 4 and 7
- Don't use for new applications
```

**Why others are wrong:**
- **A**: CLB doesn't support path-based routing
- **B**: NLB is Layer 4, no awareness of HTTP paths
- **D**: GWLB is for security appliances

**Exam Tip:** "Path-based" or "host-based" or "HTTP header" routing = ALB
</details>

---

### Question 23
An application needs to handle millions of requests per second with the lowest possible latency. The application uses TCP protocol. Which load balancer is MOST appropriate?

**A)** Application Load Balancer  
**B)** Network Load Balancer  
**C)** Classic Load Balancer  
**D)** Gateway Load Balancer

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **Network Load Balancer (NLB)** is designed for extreme performance
- Layer 4 (TCP/UDP)
- Handles millions of requests per second
- Ultra-low latency
- Preserves source IP

**NLB Performance:**
- Millions of requests per second
- ~100 microseconds latency
- Sudden traffic spikes
- Static IP addresses

**When to use NLB:**
- Extreme performance requirements
- TCP/UDP protocols
- Static IP address needed
- Preserve source IP address
- PrivateLink support

**Why others are wrong:**
- **A**: ALB has more latency due to Layer 7 processing
- **C**: CLB is legacy, lower performance
- **D**: GWLB is for security appliances

**Exam Scenario Patterns:**
```
"Path-based routing" → ALB
"Highest performance" + "TCP" → NLB
"Static IP required" → NLB
"WebSockets" → ALB
"Security appliances" → GWLB
```
</details>

---

### Question 24
A company has VPC-A (10.0.0.0/16) and VPC-B (10.1.0.0/16). They create a VPC peering connection between them. Instances in VPC-A cannot connect to instances in VPC-B. What is the MOST likely cause?

**A)** VPC peering doesn't support cross-AZ communication  
**B)** Route tables haven't been updated to route traffic to the peering connection  
**C)** Security groups are blocking all traffic  
**D)** VPCs must be in the same region for peering

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **VPC peering requires manual route table updates**
- Peering connection is not automatically added to route tables
- Must add routes in BOTH VPCs

**Required Configuration:**
```
VPC-A Route Table:
10.1.0.0/16 → pcx-xxxxx (peering connection)

VPC-B Route Table:
10.0.0.0/16 → pcx-xxxxx (peering connection)
```

**Complete VPC Peering Checklist:**
1. ✅ Create peering connection
2. ✅ Accept peering (if cross-account)
3. ✅ Update route tables in BOTH VPCs
4. ✅ Update security groups to allow traffic
5. ✅ Update NACLs if using custom rules

**Why others are wrong:**
- **A**: VPC peering works across AZs
- **C**: Possible, but route tables are more commonly forgotten
- **D**: VPC peering works cross-region

**Common Exam Trap:** Forgetting to update route tables on BOTH sides of the peering.
</details>

---

### Question 25
An application requires a solution to inspect and filter traffic for SQL injection and XP attacks before it reaches the Application Load Balancer. Which AWS service should be used?

**A)** AWS Shield  
**B)** AWS WAF  
**C)** AWS GuardDuty  
**D)** Network ACL

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **AWS WAF (Web Application Firewall)** protects against Layer 7 attacks
- Filters HTTP/HTTPS traffic
- Managed rules for OWASP Top 10 (including SQL injection, XSS)
- Can attach to ALB, CloudFront, API Gateway, AppSync

**WAF Protections:**
```
SQL Injection:
- Inspects query strings, body, headers
- Blocks malicious SQL patterns

Cross-Site Scripting (XSS):
- Detects JavaScript injection attempts
- Blocks malicious scripts

Rate Limiting:
- Limit requests per IP (DDoS protection)

Geo-blocking:
- Block countries

IP filtering:
- Allowlist/blocklist IPs
```

**WAF Web ACL Example:**
```
Rule 1: Block known bad IPs
Rule 2: Rate limit (1000 req/5min per IP)
Rule 3: AWS Managed Rule - SQL Injection
Rule 4: AWS Managed Rule - XSS
Rule 5: Geo-block certain countries
Default: Allow
```

**Why others are wrong:**
- **A**: Shield is for DDoS (Layer 3/4), not application attacks
- **C**: GuardDuty is threat detection, not prevention
- **D**: NACL is Layer 4, can't inspect HTTP content

**Security Service Comparison:**
```
Layer 3/4 DDoS → Shield
Layer 7 attacks → WAF
Threat detection → GuardDuty
Vulnerability scanning → Inspector
```

**Exam Tip:** "SQL injection" or "XSS" or "Layer 7 protection" = WAF
</details>

---

### Question 26
A company has EC2 instances in private subnets that need outbound internet access to download software patches, but should not be accessible from the internet. What is the correct solution?

**A)** Attach an internet gateway and use security groups to block inbound traffic  
**B)** Deploy a NAT Gateway in a public subnet  
**C)** Use VPC peering to another VPC with internet access  
**D)** Deploy a NAT instance in a private subnet

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **NAT Gateway** enables outbound internet access from private subnets
- NAT Gateway itself must be in a public subnet
- Prevents inbound connections from internet

**Architecture:**
```
Private Subnet (10.0.1.0/24)
└─ EC2 instances
   └─ Route: 0.0.0.0/0 → NAT Gateway

Public Subnet (10.0.0.0/24)
└─ NAT Gateway
   └─ Route: 0.0.0.0/0 → Internet Gateway

Internet Gateway
```

**NAT Gateway vs NAT Instance:**
```
NAT Gateway (Recommended):
- Managed by AWS
- High availability within AZ
- Scales automatically to 45 Gbps
- No maintenance
- Cost: $0.045/hour + data transfer

NAT Instance:
- You manage EC2 instance
- Must handle HA yourself
- Limited by instance type
- Can use as bastion host
- Cheaper for low traffic
```

**High Availability NAT:**
```
Create NAT Gateway in each AZ
Private subnets route to NAT in same AZ
```

**Why others are wrong:**
- **A**: Internet gateway gives inbound access (if instances have public IPs)
- **C**: VPC peering can't route to internet gateway (edge-to-edge routing not supported)
- **D**: NAT must be in public subnet, not private

**Exam Tip:** "Private subnet outbound internet" = NAT Gateway
</details>

---

### Question 27
A company uses a Network Load Balancer to distribute traffic to EC2 instances. The security team needs to see the source IP addresses of clients in the application logs. What should be configured?

**A)** Enable access logs on the NLB  
**B)** The source IP is automatically preserved with NLB; configure the application to log it  
**C)** Enable proxy protocol on the NLB and application  
**D)** Use an Application Load Balancer instead

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **NLB preserves the source IP address** by default
- No additional configuration needed on NLB
- Application just needs to log the source IP from the connection

**Load Balancer Source IP Handling:**
```
NLB (Layer 4):
- Source IP preserved automatically
- Application sees real client IP
- No headers needed

ALB (Layer 7):
- Source IP is the ALB's IP
- Real client IP in X-Forwarded-For header
- Application must read header
```

**Why others are wrong:**
- **A**: Access logs show aggregate data, not for application logging
- **C**: Proxy protocol is for when you need additional connection info beyond source IP, not required for basic source IP preservation
- **D**: Changing to ALB would lose source IP (would be in header instead)

**Exam Comparison:**
```
Scenario: Need to see client IP

NLB: Automatically available as source IP
ALB: Available in X-Forwarded-For header
CLB: Depends on protocol (TCP = source IP, HTTP = header)
```

**Exam Tip:** "NLB" + "source IP" = Already preserved, just log it
</details>

---

### Question 28
An application spans multiple VPCs: VPC-A connects to VPC-B, and VPC-B connects to VPC-C via VPC peering. Instances in VPC-A cannot reach instances in VPC-C. What is the reason?

**A)** VPC peering connections don't support transitive routing  
**B)** Maximum of 2 VPCs can be peered  
**C)** VPC peering requires all VPCs in the same region  
**D)** Security groups need to be configured

<details>
<summary>Answer</summary>

**Correct Answer: A**

**Explanation:**
- **VPC peering is NOT transitive**
- If A ↔ B and B ↔ C, traffic cannot flow A → B → C
- Must create direct peering connection A ↔ C

**Visual:**
```
❌ This doesn't work:
VPC-A ↔ VPC-B ↔ VPC-C (A cannot reach C)

✅ This works:
VPC-A ↔ VPC-B
VPC-A ↔ VPC-C
VPC-B ↔ VPC-C
(Full mesh peering)
```

**VPC Peering Limitations (Exam Favorites!):**
- ❌ No transitive routing
- ❌ No edge-to-edge routing (can't route to Internet Gateway, VPN, Direct Connect)
- ❌ No overlapping CIDR blocks
- ✅ Can peer cross-region
- ✅ Can peer cross-account

**Solution for Many VPCs:**
```
1-5 VPCs: VPC Peering (manageable)
5+ VPCs: Transit Gateway (hub-spoke model, transitive routing supported)
```

**Exam Tip:** "VPC-A → VPC-B → VPC-C" = Not possible with peering alone (NOT transitive)
</details>

---

### Question 29
A Security Group has the following inbound rules:
- Rule 1: Allow port 22 from 10.0.0.0/16
- Rule 2: Allow port 443 from 0.0.0.0/0

An instance tries to connect to another instance in the same security group on port 3306. Will it succeed?

**A)** Yes, instances in the same security group can communicate automatically  
**B)** No, port 3306 is not explicitly allowed  
**C)** Yes, because all outbound traffic is allowed by default  
**D)** No, need to configure NACL rules

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- Security groups are **stateful** but only allow explicitly defined traffic
- Instances in the same security group do NOT automatically have access to each other
- Port 3306 is not in the inbound rules, so connection will be blocked

**Common Misconception:** "Same security group = automatic access" (FALSE!)

**To Allow Communication:**
```
Option 1: Add rule allowing port 3306 from specific IPs
Option 2: Add rule allowing port 3306 from the security group itself

Example Rule:
Type: MySQL/Aurora
Protocol: TCP
Port: 3306
Source: sg-xxxxx (same security group ID)
```

**Security Group Rules:**
```
Inbound Rules:
- Define what can connect TO instances
- Evaluated: ALL rules (most permissive wins)
- Default: Deny all

Outbound Rules:
- Define what instances can connect TO
- Default: Allow all
- Stateful: Return traffic automatically allowed
```

**Exam Tip:** Don't assume instances in same security group can communicate; check rules explicitly.
</details>

---

### Question 30
A company needs to connect their on-premises data center to AWS with a dedicated private connection. The connection will transfer terabytes of data daily. Setup time is not critical, but consistent high bandwidth and low latency are required. What is the BEST solution?

**A)** Site-to-Site VPN  
**B)** AWS Direct Connect  
**C)** VPN over Direct Connect  
**D)** AWS DataSync over internet

<details>
<summary>Answer</summary>

**Correct Answer: B**

**Explanation:**
- **AWS Direct Connect** provides dedicated private connection
- High bandwidth (1 Gbps → 100 Gbps)
- Consistent performance (doesn't use internet)
- Low latency
- Cost-effective for large data transfers

**Direct Connect vs VPN:**
```
Direct Connect:
- Dedicated connection
- 1-100 Gbps
- Consistent performance
- Setup: Weeks/months
- Cost: Higher upfront, lower per GB
- Use: Large sustained data transfer

Site-to-Site VPN:
- Over internet
- Up to 1.25 Gbps per tunnel
- Performance varies with internet
- Setup: Minutes/hours
- Cost: Lower upfront, higher per GB
- Use: Quick setup, backup, smaller transfer
```

**Best Practice:**
```
Primary: Direct Connect
Backup: Site-to-Site VPN
= Hybrid connectivity with failover
```

**Direct Connect Components:**
```
On-Premises
└─ Customer Router
   └─ Cross-Connect
      └─ AWS Direct Connect Location
         └─ AWS Router
            └─ Virtual Private Gateway (VGW) or Transit Gateway
               └─ VPCs
```

**Why others are wrong:**
- **A**: VPN limited bandwidth, uses internet (inconsistent performance)
- **C**: Good for security, but question doesn't mention encryption requirement
- **D**: DataSync is transfer service, not connectivity solution

**Exam Tip:** "Large consistent data transfer" + "dedicated connection" = Direct Connect
</details>

---

---

## Answer Key

### Section 1: IAM (Questions 1-10)
1. B  2. B  3. C  4. B  5. B  
6. B  7. B  8. B  9. B  10. B

### Section 2: Database (Questions 11-20)
11. B  12. B  13. B  14. B  15. B  
16. B  17. B  18. B  19. B  20. A

### Section 3: Networking (Questions 21-30)
21. B  22. C  23. B  24. B  25. B  
26. B  27. B  28. A  29. B  30. B

---

## Scoring Guide

- **27-30 correct**: Excellent! You have strong understanding of these weak areas
- **23-26 correct**: Good! Review the explanations for questions you missed
- **19-22 correct**: Fair. These topics need focused study
- **< 19 correct**: Need significant review. Study the detailed explanations and notes

---

## Study Recommendations Based on Your Score

**If you scored < 7 in Section 1 (IAM)**:
1. Review FLASHCARDS.md: Cards 1-5
2. Study WEAK-AREAS-STUDY-NOTES.md: IAM Deep Dive section
3. Review AWS documentation on policy evaluation logic
4. Create your own policy examples

**If you scored < 7 in Section 2 (Database)**:
1. Review FLASHCARDS.md: Cards 6-10
2. Study WEAK-AREAS-STUDY-NOTES.md: Database Selection Matrix
3. Create a decision tree for database selection
4. Practice matching requirements to database types

**If you scored < 7 in Section 3 (Networking)**:
1. Review FLASHCARDS.md: Cards 11-15
2. Study WEAK-AREAS-STUDY-NOTES.md: Networking Mastery section
3. Draw network diagrams for each scenario
4. Practice VPC configuration scenarios

---

*Continue to additional sections (Storage, Security, Architecture Patterns, Cost Optimization) in follow-up practice sessions.*

