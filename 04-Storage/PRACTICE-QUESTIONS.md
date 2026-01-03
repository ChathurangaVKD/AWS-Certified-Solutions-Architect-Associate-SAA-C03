# Storage Services - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company needs to store frequently accessed data with the lowest latency and highest throughput. Cost is not the primary concern. Which S3 storage class should be used?

A. S3 Standard  
B. S3 Intelligent-Tiering  
C. S3 Standard-IA  
D. S3 One Zone-IA  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **S3 Standard** provides:
  - Millisecond latency
  - High throughput
  - 99.99% availability
  - 11 9's durability
  - Designed for frequently accessed data

**S3 Storage Classes Comparison**:
- **Standard**: Frequent access, highest cost
- **Intelligent-Tiering**: Unknown/changing patterns, automatic tiering
- **Standard-IA**: Infrequent access, lower cost, retrieval fees
- **One Zone-IA**: Infrequent, single AZ, lowest IA cost
- **Glacier**: Archive, minutes to hours retrieval
- **Glacier Deep Archive**: Long-term archive, 12+ hours retrieval

**References:** S3 Storage Classes, S3 Standard
</details>

---

### Question 2
A company stores infrequently accessed data in S3 Standard-IA. They need to access this data immediately when required. What is the retrieval time?

A. 12 hours  
B. 3-5 hours  
C. 1-5 minutes  
D. Milliseconds (immediate)  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- **S3 Standard-IA** provides immediate access (milliseconds)
- "IA" means Infrequent Access, not slow access
- Lower storage cost than Standard
- Retrieval fees apply per GB
- Minimum storage duration: 30 days
- Minimum object size: 128 KB

**S3 Retrieval Times**:
- **Standard/Standard-IA/One Zone-IA**: Milliseconds
- **Intelligent-Tiering**: Milliseconds
- **Glacier Instant Retrieval**: Milliseconds
- **Glacier Flexible Retrieval**: 
  - Expedited: 1-5 minutes
  - Standard: 3-5 hours
  - Bulk: 5-12 hours
- **Glacier Deep Archive**:
  - Standard: 12 hours
  - Bulk: 48 hours

**References:** S3 Standard-IA, S3 Retrieval Times
</details>

---

### Question 3
A company needs to store compliance data that must be retained for 7 years and accessed once or twice per year. Cost optimization is critical. Which storage solution is MOST cost-effective?

A. S3 Standard  
B. S3 Glacier Flexible Retrieval  
C. S3 Glacier Deep Archive  
D. S3 Intelligent-Tiering  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **S3 Glacier Deep Archive** is cheapest S3 storage class
- Designed for long-term retention (7-10+ years)
- Retrieval time: 12-48 hours (acceptable for rare access)
- Lowest cost per GB
- Perfect for compliance, regulatory archives

**Cost Comparison (approximate)**:
- **Deep Archive**: $0.00099/GB/month (cheapest)
- **Glacier Flexible**: $0.0036/GB/month
- **Standard-IA**: $0.0125/GB/month
- **Standard**: $0.023/GB/month

**When to Use**:
- **Deep Archive**: Rarely accessed, 7+ years retention
- **Glacier Flexible**: Occasionally accessed archives
- **Standard-IA**: Monthly access
- **Standard**: Frequent access

**References:** S3 Glacier Deep Archive, Archive Storage
</details>

---

### Question 4
A web application serves static content (images, CSS, JS) to global users. The content is stored in S3. What is the BEST way to improve performance and reduce latency?

A. Enable S3 Transfer Acceleration  
B. Use CloudFront with S3 as origin  
C. Enable S3 Cross-Region Replication  
D. Use S3 Standard storage class  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **CloudFront** is AWS's CDN (Content Delivery Network)
- Caches content at 400+ edge locations globally
- Reduces latency for users worldwide
- Reduces load on origin S3 bucket

**CloudFront Benefits**:
- Low latency (content served from nearest edge)
- High transfer speeds
- DDoS protection (AWS Shield)
- SSL/TLS support
- Reduced S3 data transfer costs

**Other Options**:
- **Transfer Acceleration**: Speeds up uploads to S3, not downloads
- **Cross-Region Replication**: Multi-region redundancy, not CDN
- **Storage class**: Doesn't affect delivery performance

**References:** Amazon CloudFront, S3 with CloudFront
</details>

---

### Question 5
A company needs block storage for an EC2 instance running a database that requires consistent high IOPS. Which storage option should be used?

A. Instance Store  
B. EBS General Purpose SSD (gp3)  
C. EBS Provisioned IOPS SSD (io2)  
D. Amazon EFS  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **EBS Provisioned IOPS SSD (io2/io2 Block Express)** for high-performance databases
- Consistent IOPS performance
- Up to 64,000 IOPS per volume (io2)
- Up to 256,000 IOPS (io2 Block Express)
- 99.999% durability

**EBS Volume Types**:

| Type | Use Case | IOPS | Throughput |
|------|----------|------|------------|
| **gp3** | General purpose | 16,000 | 1,000 MB/s |
| **io2** | High-performance databases | 64,000 | 1,000 MB/s |
| **io2 Block Express** | Largest databases | 256,000 | 4,000 MB/s |
| **st1** | Big data, data warehouses | 500 | 500 MB/s |
| **sc1** | Cold storage | 250 | 250 MB/s |

**When to Use**:
- **io2**: Databases needing high, consistent IOPS
- **gp3**: Most workloads, cost-effective
- **st1**: Throughput-intensive, sequential
- **Instance Store**: Temporary, highest performance

**References:** EBS Volume Types, Provisioned IOPS
</details>

---

### Question 6
An application requires shared file storage accessible from multiple EC2 instances across multiple Availability Zones using NFS protocol. Which service should be used?

A. Amazon EBS  
B. Amazon S3  
C. Amazon EFS  
D. Instance Store  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Amazon EFS** (Elastic File System) provides:
  - Shared NFS file system
  - Multi-AZ access
  - Automatic scaling
  - Linux-compatible (NFS v4)
  - Concurrent access from 1000s of instances

**Storage Service Comparison**:

| Service | Protocol | Multi-Instance | Multi-AZ | Use Case |
|---------|----------|----------------|----------|----------|
| **EBS** | Block | No (single instance) | No | Databases, boot volumes |
| **EFS** | NFS | Yes | Yes | Shared file storage |
| **FSx for Windows** | SMB | Yes | Yes | Windows file shares |
| **S3** | HTTP/S | Yes | Yes | Object storage |

**EFS Performance Modes**:
- **General Purpose**: Low latency, most workloads
- **Max I/O**: Higher latency, massive parallel access

**EFS Throughput Modes**:
- **Bursting**: Throughput scales with size
- **Provisioned**: Set throughput independent of size

**References:** Amazon EFS, Shared File Storage
</details>

---

### Question 7
A company wants to automatically move S3 objects to cheaper storage classes based on access patterns. They don't want to manage this manually. What should they use?

A. S3 Lifecycle Policies  
B. S3 Intelligent-Tiering  
C. Manual scripts  
D. AWS Lambda functions  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Intelligent-Tiering** automatically moves objects between tiers
- Monitors access patterns
- No retrieval fees (unlike IA classes)
- Small monthly monitoring fee per object

**Intelligent-Tiering Access Tiers**:
1. **Frequent Access**: Default, accessed frequently
2. **Infrequent Access**: 30 days no access
3. **Archive Instant Access**: 90 days no access
4. **Archive Access** (optional): 90-270 days no access
5. **Deep Archive Access** (optional): 180-730 days no access

**Intelligent-Tiering vs Lifecycle**:
- **Intelligent-Tiering**: Automatic based on access, no retrieval fees
- **Lifecycle**: Rule-based transitions, set schedule

**When to Use**:
- **Intelligent-Tiering**: Unknown or changing access patterns
- **Lifecycle**: Known patterns (e.g., move to Glacier after 90 days)

**References:** S3 Intelligent-Tiering, Automatic Cost Optimization
</details>

---

### Question 8
A company needs to ensure S3 objects are encrypted at rest. They want AWS to manage the encryption keys. Which encryption method should be used?

A. SSE-C (Customer-Provided Keys)  
B. SSE-S3 (S3-Managed Keys)  
C. SSE-KMS (KMS-Managed Keys)  
D. Client-Side Encryption  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **SSE-S3** uses S3-managed encryption keys
- AWS handles all key management
- AES-256 encryption
- No additional cost
- Simplest encryption option

**S3 Encryption Options**:

| Method | Key Management | Cost | Use Case |
|--------|----------------|------|----------|
| **SSE-S3** | AWS manages | Free | Simple encryption |
| **SSE-KMS** | AWS KMS | KMS API costs | Audit trail, key rotation |
| **SSE-C** | Customer provides | Free | Customer controls keys |
| **Client-Side** | Customer | Free | Encrypt before upload |

**SSE-KMS Benefits** (when needed):
- Audit trail (CloudTrail)
- Key rotation
- Granular permissions
- Envelope encryption

**For exam**: If question says "AWS manages keys, simplest", choose SSE-S3

**References:** S3 Encryption, SSE-S3, SSE-KMS
</details>

---

### Question 9
A company needs to replicate S3 objects from us-east-1 to eu-west-1 for disaster recovery. What feature should be enabled?

A. S3 Versioning  
B. S3 Cross-Region Replication (CRR)  
C. S3 Same-Region Replication (SRR)  
D. S3 Transfer Acceleration  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Cross-Region Replication (CRR)** replicates objects across regions
- Automatic, asynchronous replication
- Requires versioning enabled on both buckets
- Use cases: Compliance, disaster recovery, latency reduction

**CRR Requirements**:
1. Versioning enabled on source and destination
2. Appropriate IAM permissions
3. Different AWS regions

**CRR vs SRR**:
- **CRR**: Different regions, disaster recovery, compliance
- **SRR**: Same region, log aggregation, replication between accounts

**Replication Options**:
- **Replication Time Control (RTC)**: 99.99% replicated within 15 minutes
- **Delete marker replication**: Optional
- **Existing object replication**: Manual batch operation

**References:** S3 Cross-Region Replication, Disaster Recovery
</details>

---

### Question 10
An application generates temporary data that needs high-performance storage. The data can be lost if the instance stops. Which storage should be used?

A. EBS General Purpose SSD  
B. EBS Provisioned IOPS SSD  
C. Instance Store  
D. Amazon EFS  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Instance Store** provides:
  - Ephemeral storage (temporary)
  - Physically attached to host
  - Highest IOPS performance
  - No additional cost
  - Data lost on instance stop/termination

**Instance Store Characteristics**:
- **Performance**: Millions of IOPS possible
- **Persistence**: Data lost on stop/terminate
- **Size**: Varies by instance type
- **Use cases**: Cache, buffers, temporary data, scratch data

**Instance Store vs EBS**:
- **Instance Store**: Temporary, highest performance, free
- **EBS**: Persistent, network-attached, survives stop/start

**Exam Tip**: Look for keywords:
- "Temporary", "can be lost", "cache" → Instance Store
- "Persistent", "database", "survives restart" → EBS

**References:** EC2 Instance Store, Ephemeral Storage
</details>

---

### Question 11
A company wants to ensure deleted S3 objects can be recovered for 30 days. What should be enabled?

A. S3 Lifecycle Policies  
B. S3 Versioning  
C. S3 Object Lock  
D. MFA Delete  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Versioning** preserves all versions of objects
- Deleted objects become delete markers (recoverable)
- Previous versions retained
- Protection against accidental deletion

**S3 Versioning Features**:
- Stores all versions (including deleted)
- Recover from accidental deletes
- Recover from application failures
- Can suspend (not disable completely)
- Each version counted for storage costs

**Related Features**:
- **MFA Delete**: Requires MFA to delete versions or suspend versioning
- **Object Lock**: WORM (Write Once Read Many), compliance
- **Lifecycle**: Transition or delete versions after time period

**Best Practice**: Enable versioning + lifecycle to delete old versions

**References:** S3 Versioning, Data Protection
</details>

---

### Question 12
A Windows application running on EC2 needs shared file storage accessible via SMB protocol. Which service should be used?

A. Amazon EFS  
B. Amazon FSx for Windows File Server  
C. Amazon EBS  
D. Amazon S3  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon FSx for Windows File Server**:
  - Native Windows file system
  - SMB protocol support
  - Active Directory integration
  - Windows NTFS features
  - Multi-AZ deployment

**FSx Family**:
- **FSx for Windows**: Windows workloads, SMB, AD
- **FSx for Lustre**: HPC, ML, high-performance
- **FSx for NetApp ONTAP**: Enterprise NAS, multi-protocol
- **FSx for OpenZFS**: Linux workloads, snapshots

**File Storage Options**:
- **Windows apps**: FSx for Windows (SMB)
- **Linux apps**: EFS (NFS)
- **HPC/ML**: FSx for Lustre
- **Block storage**: EBS

**References:** Amazon FSx for Windows, SMB File Shares
</details>

---

### Question 13
A company needs to store petabytes of data for machine learning training with the fastest possible throughput. Which storage service is MOST appropriate?

A. Amazon S3  
B. Amazon EFS  
C. Amazon FSx for Lustre  
D. Amazon EBS  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **FSx for Lustre** designed for:
  - High-performance computing (HPC)
  - Machine learning
  - Media processing
  - Sub-millisecond latencies
  - Hundreds of GB/s throughput
  - Millions of IOPS

**FSx for Lustre Features**:
- Integrates with S3 (lazy loading)
- POSIX-compliant file system
- Scratch and persistent deployment types
- Scales to petabytes

**Deployment Types**:
- **Scratch**: Temporary, highest performance, no replication
- **Persistent**: Long-term, replication, automatic failover

**ML/HPC Storage**:
- **Training**: FSx for Lustre (from S3)
- **Inference**: EFS or S3
- **Dataset storage**: S3
- **Processing**: FSx for Lustre

**References:** Amazon FSx for Lustre, HPC Storage
</details>

---

### Question 14
A company wants to move infrequently accessed EBS snapshots to cheaper storage automatically. What feature should be used?

A. S3 Lifecycle Policies  
B. EBS Snapshot Archive  
C. EBS Cold HDD volumes  
D. Amazon Glacier  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **EBS Snapshot Archive** tier:
  - 75% cheaper than standard snapshots
  - For snapshots stored 90+ days
  - Restore time: 24-72 hours
  - Minimum 90-day storage

**EBS Snapshot Management**:
- **Standard**: Fast restore (minutes), higher cost
- **Archive**: Cheaper, slower restore (24-72 hrs)
- Automatic archival with lifecycle policies

**EBS Snapshot Features**:
- Incremental backups (only changed blocks)
- Stored in S3 (managed by AWS)
- Cross-region copy available
- Fast Snapshot Restore (FSR) for instant recovery

**Use Cases**:
- **Standard**: Frequent restores, DR
- **Archive**: Compliance, long-term retention

**References:** EBS Snapshots, Snapshot Archive
</details>

---

### Question 15
An application writes data to S3 frequently. The company wants to be notified immediately when objects are created. What should be configured?

A. S3 Event Notifications  
B. CloudWatch Logs  
C. AWS Config  
D. CloudTrail  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **S3 Event Notifications** trigger on bucket events
- Near real-time notifications
- Destinations: SNS, SQS, Lambda

**S3 Events**:
- Object created (PUT, POST, COPY, CompleteMultipartUpload)
- Object deleted
- Object restored from Glacier
- Replication events
- Lifecycle transitions

**Event Notification Setup**:
```json
{
  "Event": "s3:ObjectCreated:*",
  "Queue": "arn:aws:sqs:us-east-1:123456789012:MyQueue"
}
```

**Common Patterns**:
- **S3 → Lambda**: Process uploaded files
- **S3 → SQS**: Queue processing
- **S3 → SNS**: Multi-subscriber notifications

**Alternative**: EventBridge (more advanced filtering)

**References:** S3 Event Notifications, Event-Driven Architecture
</details>

---

### Question 16
A company needs to ensure S3 objects are never deleted or overwritten for regulatory compliance. Which feature should be used?

A. S3 Versioning  
B. S3 Object Lock  
C. MFA Delete  
D. S3 Lifecycle Policies  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Object Lock** provides WORM (Write Once Read Many)
- Prevents deletion/overwrite for specified retention period
- Compliance and governance modes

**Object Lock Modes**:
- **Compliance**: Can't be overwritten/deleted by anyone (even root)
- **Governance**: Users with special permissions can override
- **Legal Hold**: Indefinite protection, manually removed

**Object Lock vs Versioning**:
- **Versioning**: Protects but versions can be deleted
- **Object Lock**: Enforces retention, truly immutable

**Requirements**:
- Versioning must be enabled
- Set at bucket creation
- Retention period or legal hold

**Use Cases**:
- Financial records
- Healthcare data (HIPAA)
- Legal documents
- Regulatory compliance

**References:** S3 Object Lock, WORM Compliance
</details>

---

### Question 17
An application needs to upload large files (100 GB+) to S3 with optimal performance. What should be used?

A. Single PUT operation  
B. S3 Multipart Upload  
C. S3 Transfer Acceleration  
D. AWS DataSync  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Multipart Upload**:
  - Upload large objects in parts
  - Parts uploaded in parallel (better throughput)
  - Can pause/resume
  - Recommended for files > 100 MB
  - Required for files > 5 GB

**Multipart Upload Benefits**:
- Improved throughput (parallel uploads)
- Quick recovery from network issues
- Pause and resume uploads
- Upload before knowing final size

**Best Practices**:
- Use for files > 100 MB
- Required for files > 5 GB
- Upload parts in parallel
- Configure lifecycle to abort incomplete uploads

**Transfer Acceleration**:
- Different feature (uses CloudFront edge locations)
- Speeds up uploads via edge locations
- Can combine with Multipart Upload

**References:** S3 Multipart Upload, Large File Uploads
</details>

---

### Question 18
A company wants to access S3 from EC2 instances without using internet gateway or NAT. What should be configured?

A. VPN Connection  
B. AWS Direct Connect  
C. VPC Endpoint for S3 (Gateway Endpoint)  
D. VPC Peering  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **VPC Endpoint for S3** (Gateway Endpoint):
  - Private connection from VPC to S3
  - No internet required
  - No data transfer charges
  - Traffic stays within AWS network

**VPC Endpoint Types**:

| Type | Services | Cost | Implementation |
|------|----------|------|----------------|
| **Gateway** | S3, DynamoDB | Free | Route table entry |
| **Interface** | Most AWS services | Hourly + data | ENI in subnet |

**S3 Endpoint Benefits**:
- Enhanced security (no internet exposure)
- Better performance
- No NAT Gateway costs
- Control access via endpoint policies

**Configuration**:
1. Create Gateway Endpoint for S3
2. Select VPC and route tables
3. Configure endpoint policy (optional)
4. S3 traffic automatically routed

**References:** VPC Endpoints, S3 Gateway Endpoint, Private Connectivity
</details>

---

### Question 19
A database backup is stored in S3. The company wants to ensure the backup can be restored quickly if needed. What feature should be enabled?

A. S3 Transfer Acceleration  
B. S3 Versioning  
C. S3 Cross-Region Replication  
D. Enable S3 Retrieval directly  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Versioning** for backup protection:
  - Immediate access to all versions
  - Protect against accidental deletion/overwrite
  - Quick recovery (millisecond retrieval)
  - Keep multiple backup versions

**Backup Best Practices**:
1. Enable versioning
2. Use lifecycle policies to transition old versions
3. Enable Cross-Region Replication for DR
4. Tag backup objects
5. Test restore procedures

**Additional Protection**:
- **CRR**: Geographic redundancy
- **Object Lock**: Immutable backups
- **MFA Delete**: Prevent accidental deletion

**Storage Class**: Use Standard or Standard-IA for quick restore

**References:** S3 for Backups, Versioning, Backup Strategies
</details>

---

### Question 20
A company has data in S3 Standard storage. Objects accessed within 30 days should remain in Standard, but older objects should move to S3 Glacier. How can this be automated?

A. S3 Intelligent-Tiering  
B. S3 Lifecycle Policies  
C. AWS Lambda function  
D. Manual migration  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Lifecycle Policies** automate transitions and expiration
- Rule-based transitions between storage classes
- Can filter by prefix or tags
- No code required

**Lifecycle Policy Example**:
```json
{
  "Rules": [
    {
      "Id": "MoveToGlacier",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ]
    }
  ]
}
```

**Lifecycle Actions**:
- **Transition**: Move to different storage class
- **Expiration**: Delete objects
- **NoncurrentVersionTransition**: Transition previous versions
- **NoncurrentVersionExpiration**: Delete previous versions
- **AbortIncompleteMultipartUpload**: Clean up incomplete uploads

**Transition Rules**:
- Standard → Standard-IA (30 days min)
- Standard → Glacier (0 days min)
- Can't transition backwards (Glacier → Standard)

**References:** S3 Lifecycle Policies, Storage Class Transitions
</details>

---

## Summary

**Total Questions**: 20  
**Topics Covered**:
- S3 Storage Classes and Use Cases
- S3 Encryption (SSE-S3, SSE-KMS, SSE-C)
- S3 Versioning and Object Lock
- S3 Replication (CRR, SRR)
- S3 Lifecycle Policies
- S3 Event Notifications
- EBS Volume Types (gp3, io2, st1, sc1)
- EBS Snapshots and Archive
- Amazon EFS (Shared NFS File Storage)
- Amazon FSx (Windows, Lustre)
- Instance Store
- VPC Endpoints for S3
- CloudFront with S3

**Exam Tips**:

**S3 Storage Classes Decision Tree**:
1. **Frequent access** → S3 Standard
2. **Infrequent access (immediate)** → Standard-IA or One Zone-IA
3. **Archive (immediate access)** → Glacier Instant Retrieval
4. **Archive (minutes-hours)** → Glacier Flexible Retrieval
5. **Archive (12+ hours)** → Glacier Deep Archive
6. **Unknown pattern** → Intelligent-Tiering

**EBS Volume Types**:
- **Databases (high IOPS)** → io2/io2 Block Express
- **General purpose** → gp3
- **Big data (throughput)** → st1
- **Infrequent access** → sc1
- **Temporary** → Instance Store

**File Storage**:
- **Windows (SMB)** → FSx for Windows
- **Linux (NFS), shared** → EFS
- **HPC/ML** → FSx for Lustre
- **Single instance** → EBS

**S3 Features**:
- **Versioning**: Protect from deletion, enable CRR
- **Object Lock**: WORM compliance
- **Lifecycle**: Automate transitions/expiration
- **CRR**: Cross-region disaster recovery
- **Event Notifications**: Trigger Lambda/SQS/SNS

**Cost Optimization**:
- Use Intelligent-Tiering for unknown patterns
- Lifecycle policies for known patterns
- Archive tier for long-term retention
- VPC Endpoint to avoid NAT costs

**Performance**:
- CloudFront for global distribution
- Multipart Upload for large files
- Transfer Acceleration for distance
- VPC Endpoint for private connectivity

**Next Steps**:
- Memorize S3 storage class use cases and costs
- Understand when to use each EBS volume type
- Know file storage options (EFS vs FSx)
- Practice lifecycle policy configurations

