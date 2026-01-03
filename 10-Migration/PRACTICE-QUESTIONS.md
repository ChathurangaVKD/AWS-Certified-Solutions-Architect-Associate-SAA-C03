# Migration & Transfer Services - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company wants to migrate a large on-premises application to AWS quickly with minimal changes. The application runs on virtual machines and must be operational within 2 weeks. Which migration strategy should be used?

A. Refactor the application to use Lambda and DynamoDB  
B. Rehost (Lift and Shift) using AWS Application Migration Service  
C. Repurchase by moving to a SaaS solution  
D. Replatform by migrating to containers on ECS  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Rehost (Lift and Shift) is the fastest migration strategy
- AWS Application Migration Service (MGN) automates server migration
- Moves VMs to EC2 with minimal changes
- Meets the 2-week deadline requirement
- Option A (Refactor) takes months of development
- Option C (Repurchase) requires finding and adopting new software
- Option D (Replatform) requires containerization effort

**References:** 6 R's of Migration, AWS Application Migration Service
</details>

---

### Question 2
A solutions architect needs to migrate 50 TB of data from an on-premises NFS server to Amazon S3. The company has a 100 Mbps internet connection. Which service is MOST appropriate?

A. AWS DataSync  
B. AWS Snowball  
C. AWS Direct Connect  
D. AWS Transfer Family  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- 50 TB over 100 Mbps would take approximately 46 days
- Snowball is designed for large data transfers with limited bandwidth
- Can transfer 50-80 TB per device in about a week
- DataSync works over network but would be too slow
- Direct Connect is for ongoing connectivity, not one-time migration
- Transfer Family is for SFTP/FTPS access to S3

**Calculation:** 50 TB = 400,000 Gb ÷ 100 Mbps = 4,000,000 seconds ≈ 46 days

**References:** AWS Snowball, Data Transfer Services
</details>

---

### Question 3
A company wants to migrate an Oracle database to Amazon Aurora PostgreSQL. The database schemas and stored procedures need to be converted. Which combination of services should be used?

A. AWS DMS only  
B. AWS Schema Conversion Tool (SCT) only  
C. AWS SCT to convert schema, then AWS DMS to migrate data  
D. AWS DataSync to transfer the database  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- This is a heterogeneous migration (different database engines)
- SCT converts schemas, stored procedures, and functions
- DMS migrates the actual data with minimal downtime
- DMS alone doesn't convert schemas for heterogeneous migrations
- SCT alone doesn't migrate data
- DataSync is for file systems, not databases

**References:** AWS DMS, Schema Conversion Tool, Heterogeneous Migration
</details>

---

### Question 4
A company needs to continuously replicate data from an on-premises MySQL database to Amazon RDS for MySQL for analytics purposes. The source database must remain operational. Which AWS service should be used?

A. AWS DataSync  
B. AWS Database Migration Service (DMS) with CDC  
C. AWS Snowball Edge  
D. Amazon S3 Transfer Acceleration  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DMS supports continuous data replication using Change Data Capture (CDC)
- Source database remains operational during migration
- Homogeneous migration (MySQL to MySQL)
- Keeps source and target in sync
- DataSync is for file systems, not databases
- Snowball is for one-time transfers
- S3 Transfer Acceleration is for S3 uploads

**References:** AWS DMS, Change Data Capture, Database Replication
</details>

---

### Question 5
A solutions architect needs to transfer data between Amazon EFS in us-east-1 and Amazon S3 in us-west-2 on a daily basis. Which service provides automated, scheduled transfers?

A. AWS DataSync  
B. AWS Snow Family  
C. AWS Transfer Family  
D. Amazon S3 Cross-Region Replication  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- DataSync supports transfers between AWS storage services
- Can schedule tasks (hourly, daily, weekly)
- Supports EFS to S3 transfers
- Automated and managed service
- Snow Family is for physical device transfers
- Transfer Family is for SFTP/FTPS access
- S3 CRR is for S3-to-S3 only

**References:** AWS DataSync, Scheduled Data Transfer
</details>

---

### Question 6
A company is migrating a legacy application to AWS but wants to minimize changes. The application uses a specific OS version and custom drivers that aren't compatible with cloud-native services. Which migration strategy is MOST appropriate?

A. Refactor to serverless architecture  
B. Replatform to managed services  
C. Rehost (Lift and Shift) to EC2  
D. Repurchase a SaaS solution  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Rehost (Lift and Shift) moves application as-is
- EC2 supports custom OS and drivers
- Minimal changes required
- Fast migration path
- Refactor requires re-architecting
- Replatform may not support custom requirements
- Repurchase requires finding compatible SaaS

**References:** Migration Strategies, Rehost Pattern
</details>

---

### Question 7
An organization wants to track the progress of migrating 200 applications across multiple AWS accounts and regions. Which service provides centralized visibility?

A. AWS CloudWatch  
B. AWS Migration Hub  
C. AWS Systems Manager  
D. AWS Config  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Migration Hub provides centralized tracking of migrations
- Aggregates progress from multiple migration tools
- Supports multi-account and multi-region tracking
- Integrates with DMS, Application Migration Service, etc.
- CloudWatch monitors resources, not migrations
- Systems Manager manages infrastructure
- Config tracks configuration compliance

**References:** AWS Migration Hub, Migration Tracking
</details>

---

### Question 8
A company needs to migrate data from an on-premises HDFS cluster to Amazon S3. The data must be encrypted in transit. Which service should be used?

A. AWS Snowball  
B. AWS DataSync  
C. AWS Direct Connect  
D. AWS Storage Gateway  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DataSync supports HDFS as a source
- Encrypts data in transit with TLS
- Automated and fast data transfer
- Can transfer to S3
- Snowball doesn't support HDFS directly
- Direct Connect is for network connectivity
- Storage Gateway is for hybrid storage, not migration

**References:** AWS DataSync, HDFS Migration
</details>

---

### Question 9
A database migration using AWS DMS needs to handle large transactions and minimize the impact on the source database performance. How should the replication instance be sized?

A. Use the smallest instance to minimize costs  
B. Use an instance type based on the source database workload and data volume  
C. Always use the largest instance available  
D. Instance size doesn't affect DMS performance  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Replication instance size affects performance
- Should be based on workload, data volume, and complexity
- Larger instances handle more throughput and complex transformations
- Undersizing causes slow migration and potential source impact
- Oversizing wastes money
- Proper sizing requires workload analysis

**References:** AWS DMS, Replication Instance Sizing
</details>

---

### Question 10
A company wants to migrate an on-premises Microsoft SQL Server database to AWS. They want to minimize management overhead and maintain compatibility. Which target should they choose?

A. Amazon RDS for SQL Server  
B. Microsoft SQL Server on EC2  
C. Amazon Aurora PostgreSQL  
D. Amazon DynamoDB  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- RDS for SQL Server is managed service (minimal overhead)
- Maintains SQL Server compatibility
- This is a "Replatform" strategy
- Option B requires managing EC2 and OS (more overhead)
- Option C requires heterogeneous migration and code changes
- Option D is NoSQL, requires application re-architecture

**References:** AWS RDS, Replatform Strategy
</details>

---

### Question 11
During a database migration with AWS DMS, which task type should be used to perform an initial data load followed by ongoing replication?

A. Full Load only  
B. CDC (Change Data Capture) only  
C. Full Load + CDC  
D. Multiple Full Load tasks  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Full Load + CDC is the most common migration pattern
- Full Load transfers existing data
- CDC replicates ongoing changes
- Minimizes downtime
- Full Load only doesn't capture changes after initial load
- CDC only doesn't transfer existing data
- Multiple Full Loads don't capture changes

**References:** AWS DMS, Migration Task Types
</details>

---

### Question 12
A company has 500 TB of data to migrate from on-premises to AWS. The internet connection is 1 Gbps, but business requirements prohibit using the full bandwidth. Which solution is MOST cost-effective?

A. Use AWS DataSync with bandwidth throttling  
B. Order multiple AWS Snowball devices  
C. Upgrade internet connection to 10 Gbps  
D. Use AWS Direct Connect with 10 Gbps connection  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- 500 TB is very large, Snowball is designed for this
- Even with 1 Gbps, transfer would take months
- Can't use full bandwidth due to business requirements
- Snowball is faster and more cost-effective for large migrations
- DataSync with throttling would be too slow
- Upgrading connection is expensive
- Direct Connect requires time to provision

**References:** AWS Snowball, Large Data Migration
</details>

---

### Question 13
An application stores data in an on-premises SMB file share. The company wants to migrate this data to AWS and continue accessing it via SMB protocol. Which solution should be implemented?

A. Use DataSync to transfer to S3, then use S3 File Gateway  
B. Use DataSync to transfer to FSx for Windows File Server  
C. Use Snowball to transfer to EFS  
D. Use Storage Gateway Volume Gateway  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DataSync supports SMB as source
- FSx for Windows File Server provides native SMB protocol
- Seamless migration path for Windows file shares
- S3 File Gateway presents S3 as NFS/SMB but uses S3 storage
- EFS doesn't natively support SMB (uses NFS)
- Volume Gateway is for block storage

**References:** AWS DataSync, FSx for Windows File Server
</details>

---

### Question 14
A company is using AWS DMS to migrate a database. They need to ensure the data is encrypted both in transit and at rest. How can this be achieved?

A. DMS doesn't support encryption  
B. Enable SSL/TLS for connections and use encrypted RDS instances  
C. Use VPN for all connections  
D. Encryption is automatic and cannot be configured  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DMS supports encryption in transit using SSL/TLS
- Target RDS instances can use encryption at rest
- Replication instance can also be encrypted
- Both source and target connections should use SSL
- VPN adds security but isn't required for encryption
- Encryption must be explicitly configured

**References:** AWS DMS Security, Encryption
</details>

---

### Question 15
A solutions architect needs to schedule a DataSync task to run every day at 2 AM UTC. How can this be configured?

A. DataSync doesn't support scheduling  
B. Use the built-in task scheduling in DataSync  
C. Use EventBridge to trigger DataSync tasks  
D. Use Lambda with cron expressions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DataSync has built-in task scheduling
- Can schedule hourly, daily, weekly, or custom intervals
- No additional services required
- EventBridge could also trigger tasks but isn't necessary
- Lambda is unnecessary complexity
- Scheduling is a native DataSync feature

**References:** AWS DataSync, Task Scheduling
</details>

---

### Question 16
A company wants to retire legacy applications that are no longer used as part of their cloud migration. Which migration strategy does this represent?

A. Rehost  
B. Replatform  
C. Retire  
D. Retain  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Retire strategy identifies and turns off unused applications
- Reduces cost and complexity
- Part of the 6 R's migration framework
- Rehost moves applications to cloud
- Replatform optimizes during migration
- Retain keeps applications on-premises

**References:** 6 R's of Migration, Retire Strategy
</details>

---

### Question 17
During a database migration, AWS DMS replication instance is in the same VPC as the target RDS database but cannot connect. What is the MOST likely cause?

A. The replication instance is too small  
B. The target RDS security group doesn't allow inbound traffic from the replication instance  
C. DMS doesn't support RDS as a target  
D. SSL must be disabled on RDS  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Security groups must allow traffic between DMS and RDS
- Common misconfiguration during DMS setup
- Need to add inbound rule to RDS security group
- Instance size doesn't affect connectivity
- DMS fully supports RDS as target
- SSL is optional, not a blocker

**References:** AWS DMS, VPC Security Groups
</details>

---

### Question 18
A company is planning a large-scale migration to AWS and needs to assess their current environment, plan the migration, and track progress. Which AWS service provides this comprehensive approach?

A. AWS Migration Hub  
B. AWS Application Discovery Service  
C. Both Migration Hub and Application Discovery Service  
D. AWS CloudEndure  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Application Discovery Service discovers on-premises resources
- Collects server specifications, performance data, dependencies
- Migration Hub tracks migration progress
- Together they provide complete migration solution
- Application Discovery feeds data into Migration Hub
- CloudEndure is now AWS Application Migration Service

**References:** Migration Hub, Application Discovery Service
</details>

---

### Question 19
A company wants to use AWS DataSync to transfer data but needs to verify that files are identical at source and destination. Which DataSync feature ensures this?

A. DataSync doesn't verify data  
B. Built-in data integrity verification  
C. Manual MD5 checksum comparison  
D. Use CloudWatch to monitor transfers  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- DataSync automatically verifies data integrity
- Checks data at source and destination
- Ensures data consistency after transfer
- Built-in feature, no manual intervention needed
- CloudWatch monitors progress but doesn't verify integrity

**References:** AWS DataSync, Data Integrity
</details>

---

### Question 20
An organization is migrating applications to AWS and wants to refactor a monolithic application into microservices. Which migration strategy is being used?

A. Rehost  
B. Replatform  
C. Refactor/Re-architect  
D. Repurchase  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Refactor/Re-architect reimagines application architecture
- Breaking monolith into microservices is classic refactoring
- Uses cloud-native features (ECS, Lambda, etc.)
- Most complex but provides maximum cloud benefits
- Rehost moves as-is
- Replatform makes minimal optimizations
- Repurchase moves to SaaS

**References:** 6 R's of Migration, Refactor Strategy
</details>

---

## Summary

### Key Concepts Tested:
1. **6 R's of Migration**: Rehost, Replatform, Repurchase, Refactor, Retire, Retain
2. **AWS DataSync**: File transfer, scheduling, integrity verification
3. **AWS DMS**: Database migration, CDC, homogeneous vs heterogeneous
4. **AWS Schema Conversion Tool**: Converting database schemas
5. **AWS Migration Hub**: Tracking migration progress
6. **AWS Snowball**: Large data transfers with limited bandwidth
7. **Migration Strategies**: When to use each approach

### Exam Tips:
- ✅ Rehost (Lift and Shift) is fastest migration
- ✅ Heterogeneous migrations require SCT + DMS
- ✅ Homogeneous migrations use DMS only
- ✅ Use Snowball when data > 10 TB or bandwidth limited
- ✅ DataSync for ongoing/scheduled transfers over network
- ✅ DMS supports continuous replication with CDC
- ✅ Full Load + CDC is most common DMS task type
- ✅ Migration Hub tracks multi-account/multi-region migrations
- ✅ DataSync supports NFS, SMB, HDFS, and S3

