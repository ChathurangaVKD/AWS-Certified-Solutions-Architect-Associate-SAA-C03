# Module 04: Storage Services

## Overview
AWS provides various storage services for different use cases. This module covers S3, EBS, EFS, and other storage options.

## Learning Objectives
- Master Amazon S3 storage classes and features
- Understand EBS volume types and performance
- Implement EFS for shared file storage
- Learn data migration and backup strategies
- Understand storage optimization and lifecycle policies

---

## 1. Amazon S3 (Simple Storage Service)

### What is S3?
- **Object storage** service
- Store and retrieve any amount of data
- **11 9's durability** (99.999999999%)
- Scalable, secure, highly available

### S3 Key Concepts

**Buckets**
- Containers for objects
- **Globally unique name** (across all AWS accounts)
- Defined at **region level**
- Naming: 3-63 characters, lowercase, no underscores

**Objects**
- Files stored in buckets
- **Key**: Full path (prefix + object name)
  - Example: `s3://my-bucket/folder1/folder2/file.txt`
- **Value**: Content (max **5 TB**)
- **Metadata**: Key-value pairs
- **Version ID**: If versioning enabled
- **Tags**: Key-value pairs (up to 10)

### S3 Storage Classes

| Storage Class | Use Case | Availability | Min Duration | Retrieval Fee |
|---------------|----------|--------------|--------------|---------------|
| **S3 Standard** | Frequently accessed | 99.99% | None | No |
| **S3 Intelligent-Tiering** | Unknown/changing access | 99.9% | None | No |
| **S3 Standard-IA** | Infrequently accessed | 99.9% | 30 days | Yes |
| **S3 One Zone-IA** | Infrequent, non-critical | 99.5% | 30 days | Yes |
| **S3 Glacier Instant Retrieval** | Archive, instant access | 99.9% | 90 days | Yes |
| **S3 Glacier Flexible Retrieval** | Archive, minutes-hours | 99.99% | 90 days | Yes |
| **S3 Glacier Deep Archive** | Long-term archive | 99.99% | 180 days | Yes |

**Glacier Retrieval Options**:
- **Expedited**: 1-5 minutes (Flexible Retrieval)
- **Standard**: 3-5 hours (Flexible), 12 hours (Deep Archive)
- **Bulk**: 5-12 hours (Flexible), 48 hours (Deep Archive)

### S3 Versioning
- **Protect against accidental deletes**
- Store all versions of an object
- Enable at **bucket level**
- Suspended (not disabled) - preserves existing versions
- Delete marker for deleted objects

### S3 Replication

**Cross-Region Replication (CRR)**
- Replicate to bucket in **different region**
- Use cases: Compliance, lower latency, cross-account

**Same-Region Replication (SRR)**
- Replicate within **same region**
- Use cases: Log aggregation, live replication

**Requirements**:
- Versioning must be enabled (source and destination)
- IAM permissions for S3
- Buckets can be in different accounts

**Features**:
- Asynchronous replication
- Can replicate delete markers
- No chaining (bucket1 → bucket2 → bucket3)

### S3 Lifecycle Rules
- Automate object transitions between storage classes
- Automate object expiration/deletion

```json
{
  "Rules": [
    {
      "Id": "Archive-old-logs",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "logs/"
      },
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
```

### S3 Security

**Encryption**

*Encryption at Rest*:
- **SSE-S3**: AWS manages keys (AES-256)
  - Header: `x-amz-server-side-encryption: AES256`
- **SSE-KMS**: AWS KMS manages keys
  - Header: `x-amz-server-side-encryption: aws:kms`
  - CloudTrail audit trail
  - Quota limits (API calls to KMS)
- **SSE-C**: Customer provides keys
  - Must use HTTPS
  - Key provided in every request
- **Client-Side Encryption**: Encrypt before upload

*Encryption in Transit*:
- **SSL/TLS** (HTTPS endpoints)
- Force encryption with bucket policy

**Access Control**

*Bucket Policies*:
- JSON-based policies
- Grant public access
- Force encryption
- Grant cross-account access

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

*Access Control Lists (ACLs)*:
- Legacy (not recommended)
- Grant basic permissions

*IAM Policies*:
- Control user/role access

**Block Public Access**:
- Account-level or bucket-level
- 4 settings (recommend all enabled)
- Overrides other policies

### S3 Advanced Features

**S3 Object Lock**
- WORM (Write Once Read Many)
- **Governance mode**: Users with special permissions can modify
- **Compliance mode**: No one can modify, even root
- **Retention period** or **Legal hold**

**S3 Access Points**
- Simplify managing access to shared datasets
- Each access point has own policy
- Can restrict to VPC

**S3 Object Lambda**
- Modify objects before retrieval
- Use Lambda functions
- Use cases: Redact PII, resize images, watermark

**S3 Event Notifications**
- React to events (create, delete, restore)
- Destinations: SNS, SQS, Lambda
- EventBridge for advanced filtering

**S3 Performance**
- **3,500 PUT/COPY/POST/DELETE** per second per prefix
- **5,500 GET/HEAD** per second per prefix
- No limit on number of prefixes

**Multipart Upload**:
- Recommended for files > 100 MB
- Required for files > 5 GB
- Parallelize uploads
- Restart failed uploads

**S3 Transfer Acceleration**:
- Upload to edge location → AWS backbone network → S3
- Compatible with multipart upload

**S3 Byte-Range Fetches**:
- Parallelize GETs
- Download partial objects
- Resilient to failures

**S3 Select & Glacier Select**:
- Retrieve subset of object using SQL
- Server-side filtering
- Less network transfer, lower cost

**S3 Batch Operations**:
- Perform bulk operations on objects
- Uses S3 Inventory for object list
- Actions: Copy, invoke Lambda, restore, tags

---

## 2. Amazon EBS (Elastic Block Store)

### What is EBS?
- **Block storage** for EC2 instances
- Network drive (not physical)
- Persist data after instance termination
- Bound to **specific AZ**
- Provisioned capacity (GB and IOPS)

### EBS Volume Types

#### General Purpose SSD

**gp3 (Latest)**
- **3,000 IOPS baseline** (regardless of size)
- **125 MB/s throughput baseline**
- Can provision up to **16,000 IOPS** and **1,000 MB/s**
- **1 GB - 16 TB**
- Cost-effective

**gp2 (Previous generation)**
- Size and IOPS linked
- **3 IOPS per GB**
- Burst to 3,000 IOPS (for volumes < 1 TB)
- Max **16,000 IOPS** at 5,334 GB
- **1 GB - 16 TB**

#### Provisioned IOPS SSD

**io2 Block Express**
- **Sub-millisecond latency**
- **256,000 IOPS**, 4,000 MB/s
- **4 GB - 64 TB**
- 1,000 IOPS per GB
- Most expensive

**io2**
- **64,000 IOPS**
- **1,000 MB/s**
- **4 GB - 16 TB**
- **99.999% durability**

**io1**
- **64,000 IOPS**
- **1,000 MB/s**
- **4 GB - 16 TB**
- **99.8-99.9% durability**

**Use case**: Databases, critical applications

#### Hard Disk Drives (HDD)

**st1 (Throughput Optimized)**
- **500 MB/s throughput**
- **500 IOPS**
- **125 GB - 16 TB**
- Use case: Big data, data warehouses, log processing

**sc1 (Cold HDD)**
- **250 MB/s throughput**
- **250 IOPS**
- **125 GB - 16 TB**
- Lowest cost
- Use case: Infrequently accessed data

**Note**: Only **gp2/gp3 and io1/io2** can be used as boot volumes

### EBS Multi-Attach
- Attach **same EBS volume** to multiple EC2 instances
- Only for **io1/io2** family
- Same AZ
- Up to **16 instances**
- Use case: Clustered Linux applications (not Windows)

### EBS Snapshots
- **Backup of EBS volume**
- Stored in S3 (managed by AWS)
- Can copy across AZs or regions
- Incremental (only changed blocks)

**Snapshot Features**:
- **EBS Snapshot Archive**: 75% cheaper, 24-72 hours to restore
- **Recycle Bin**: Recover deleted snapshots (1 day to 1 year retention)
- **Fast Snapshot Restore (FSR)**: No latency on first use (expensive)

### EBS Encryption
- Encrypted at rest using KMS
- Encrypted in transit
- All snapshots encrypted
- Minimal impact on latency
- To encrypt unencrypted volume:
  1. Create snapshot
  2. Encrypt snapshot (copy)
  3. Create volume from encrypted snapshot

---

## 3. Amazon EFS (Elastic File System)

### What is EFS?
- **Managed NFS** (Network File System)
- Shared storage for multiple EC2 instances
- Works across **multiple AZs**
- Highly available, scalable, expensive (3x gp2)
- Pay per use (no capacity provisioning)

### EFS Features
- **POSIX file system**
- **Thousands of concurrent connections**
- **10+ GB/s throughput**
- **Petabyte-scale**
- **Linux only** (POSIX), not Windows

### EFS Performance Modes

**General Purpose** (default)
- Latency-sensitive (web servers, CMS)
- Max throughput: 7,000 file ops/sec

**Max I/O**
- Higher latency
- Highly parallel
- Big data, media processing
- Max throughput: 500,000+ file ops/sec

### EFS Throughput Modes

**Bursting** (default)
- Throughput scales with storage size
- 50 MB/s per TB
- Burst to 100 MB/s

**Provisioned**
- Set throughput independent of storage
- Example: 1 TB storage, 100 MB/s throughput

**Elastic** (recommended)
- Automatically scales
- Up to 3 GB/s read, 1 GB/s write
- Good for unpredictable workloads

### EFS Storage Classes

**Standard**
- Frequently accessed files
- Multi-AZ

**Infrequent Access (EFS-IA)**
- Lower cost for infrequently accessed files
- Lifecycle policy (e.g., move after 60 days)
- Up to 92% lower cost

**One Zone**
- Single AZ
- 47% cost savings vs Standard
- Good for dev/test

**One Zone-IA**
- Single AZ + Infrequent Access
- 93% cost savings vs Standard

---

## 4. Amazon FSx

### FSx for Windows File Server
- **Fully managed Windows file system**
- SMB protocol, Windows NTFS
- Active Directory integration
- **Multi-AZ** for high availability
- Backed up to S3
- Use case: Windows applications, SQL Server, Active Directory

### FSx for Lustre
- **High-performance file system**
- **Machine Learning, HPC, video processing**
- Scales to **100s GB/s, millions of IOPS**
- Sub-millisecond latencies
- Integration with S3
  - Read S3 as file system
  - Write output back to S3

**Deployment Options**:
- **Scratch**: Temporary, no replication, high burst
- **Persistent**: Long-term, replicated in AZ

### FSx for NetApp ONTAP
- Managed NetApp ONTAP
- NFS, SMB, iSCSI protocols
- Works with Linux, Windows, macOS
- Storage auto-scales
- Snapshots, replication, low-cost compression

### FSx for OpenZFS
- Managed OpenZFS file system
- NFS protocol
- Up to 1 million IOPS
- Point-in-time snapshots

---

## 5. AWS Storage Gateway

### What is Storage Gateway?
- **Hybrid cloud storage**
- Bridge on-premises and cloud storage
- Use cases: Disaster recovery, backup, tiered storage

### Storage Gateway Types

**File Gateway**
- Store files in S3 (Standard, IA, One Zone-IA, Intelligent-Tiering)
- NFS and SMB protocols
- Active Directory integration
- Local cache for frequently accessed data

**Volume Gateway**
- Block storage using iSCSI
- Backed by S3, snapshots to EBS
- **Stored Volumes**: Entire dataset on-premises, async backup to AWS
- **Cached Volumes**: Frequently accessed data cached on-premises

**Tape Gateway**
- Virtual Tape Library (VTL)
- iSCSI interface
- Backup to S3 and Glacier
- Integrate with existing backup software

### Storage Gateway Hardware Appliance
- Physical appliance for locations without virtualization
- Pre-installed with Storage Gateway software

---

## 6. AWS Snow Family

### Data Migration

**AWS Snowcone**
- **Small, portable** (2.1 kg)
- **8 TB HDD** or **14 TB SSD**
- Use for edge computing, storage, data transfer
- Can run EC2 instances & Lambda (via AWS IoT Greengrass)
- **DataSync** pre-installed

**AWS Snowball Edge**
- **Petabyte-scale** data transfer
- Alternative to moving data over network
- Pay per data transfer job

*Snowball Edge Storage Optimized*:
- **80 TB HDD** capacity
- 40 vCPUs, 80 GB RAM
- Object storage and block storage

*Snowball Edge Compute Optimized*:
- **42 TB HDD** or **28 TB NVMe**
- 104 vCPUs, 416 GB RAM
- Optional GPU

**AWS Snowmobile**
- **Exabyte-scale** (1 EB = 1,000 PB)
- **100 PB** per Snowmobile
- Ruggedized shipping container on a truck
- Use for data center migration

### Edge Computing
- Process data while it's being created at edge locations
- Use cases: Preprocessing, machine learning, transcoding

**Snowcone & Snowball Edge**
- Can run EC2 instances or Lambda functions
- Long-term deployment options (1-3 years discounted)

---

## 7. AWS Transfer Family

- Fully managed file transfer service
- **Protocols**: FTP, FTPS, SFTP
- Store in **S3 or EFS**
- Managed infrastructure (scalable, reliable, high available)
- Use case: Sharing files, public datasets, CRM, ERP

---

## 8. AWS DataSync

- Move large amounts of data **to and from AWS**
- **On-premises** to AWS (NFS, SMB, HDFS, S3 API)
- **AWS to AWS** (different storage services)
- Replication can be scheduled
- Preserves file permissions and metadata
- One DataSync agent task can use **10 Gbps**
- Supports: S3, EFS, FSx

---

## 9. AWS Backup

- Fully managed backup service
- Centrally manage backups across AWS services
- Supported services: EC2, EBS, EFS, FSx, RDS, Aurora, DynamoDB, DocumentDB, Neptune, Storage Gateway
- **Backup plans**: Frequency, retention, transition to cold storage
- **Cross-region** and **cross-account** backups
- **Backup Vault Lock**: WORM, even root can't delete

---

## Storage Comparison

| Service | Type | Protocol | Use Case |
|---------|------|----------|----------|
| **S3** | Object | HTTP/HTTPS | Static content, backups, archives |
| **Glacier** | Object Archive | HTTP/HTTPS | Long-term archives |
| **EBS** | Block | - | Boot volumes, databases (single instance) |
| **Instance Store** | Block | - | Temporary, high IOPS |
| **EFS** | File (NFS) | NFS | Shared file system (Linux) |
| **FSx Windows** | File (SMB) | SMB | Windows applications |
| **FSx Lustre** | File | Lustre | HPC, ML |

---

## Practice Questions

1. **Which S3 storage class provides the lowest cost for long-term archival data?**
   - A. S3 Standard-IA
   - B. S3 Glacier Instant Retrieval
   - C. S3 Glacier Deep Archive
   - D. S3 One Zone-IA
   
   **Answer**: C

2. **Which EBS volume type is required for Multi-Attach feature?**
   - A. gp3
   - B. gp2
   - C. io1/io2
   - D. st1
   
   **Answer**: C

3. **Which AWS service allows you to share file storage across multiple EC2 instances in different AZs?**
   - A. EBS
   - B. Instance Store
   - C. EFS
   - D. S3
   
   **Answer**: C

4. **What is the maximum size of a single object in S3?**
   - A. 5 MB
   - B. 5 GB
   - C. 500 GB
   - D. 5 TB
   
   **Answer**: D

---

## Hands-On Labs

### Lab 1: S3 Lifecycle Policies
1. Create S3 bucket with versioning
2. Upload multiple files
3. Create lifecycle rule:
   - Transition to IA after 30 days
   - Transition to Glacier after 90 days
   - Delete after 365 days
4. Test with simulated dates

### Lab 2: EBS Snapshots
1. Create EBS volume and attach to EC2
2. Create files on volume
3. Take snapshot
4. Create volume from snapshot in different AZ
5. Attach to new EC2 instance

### Lab 3: EFS Setup
1. Create EFS file system
2. Launch 2 EC2 instances in different AZs
3. Mount EFS on both instances
4. Create file on instance 1
5. Verify file appears on instance 2

### Lab 4: S3 Cross-Region Replication
1. Create source bucket with versioning
2. Create destination bucket in different region
3. Configure replication rule
4. Upload files and verify replication
5. Test delete marker replication

---

## Key Takeaways

✅ S3 is object storage with 11 9's durability, globally unique bucket names  
✅ S3 Glacier Deep Archive is cheapest for long-term archival  
✅ EBS volumes are AZ-specific, must snapshot to move across AZs  
✅ io1/io2 volumes support Multi-Attach (up to 16 instances)  
✅ EFS is shared NFS for Linux, works across multiple AZs  
✅ FSx for Windows for SMB, FSx for Lustre for HPC/ML  
✅ Use S3 lifecycle policies to automatically transition storage classes  
✅ Snowball for petabyte-scale data transfer, Snowmobile for exabyte  
✅ Enable S3 versioning before replication  
✅ DataSync for online data transfer, Snow Family for offline  

---

## Additional Resources

- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
- [Amazon EFS Documentation](https://docs.aws.amazon.com/efs/)
- [AWS Snow Family](https://aws.amazon.com/snow/)

---

**Previous Module**: [Module 03: Compute Services](../03-Compute/README.md)  
**Next Module**: [Module 05: Database Services](../05-Database/README.md)

