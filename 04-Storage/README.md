# Module 04: Storage Services

## 📚 Overview

AWS storage services for SAA-C03 exam: S3, EBS, EFS, Storage Gateway, and Snow Family.

**Exam Weight**: ~15-20%

---

## 🎯 Key Services

1. **Amazon S3** - Object storage
2. **Amazon EBS** - Block storage for EC2
3. **Amazon EFS** - File storage (NFS)
4. **AWS Storage Gateway** - Hybrid cloud storage
5. **AWS Snow Family** - Physical data transfer
6. **Amazon FSx** - Managed file systems

---

## 1. Amazon S3

### Overview
- **Simple Storage Service** - Object storage
- Unlimited storage
- Objects up to 5 TB
- 11 nines durability (99.999999999%)
- Globally unique bucket names

### Storage Classes

| Class | Use Case | Durability | Availability | Min Storage |
|-------|----------|------------|--------------|-------------|
| **Standard** | Frequently accessed | 11 9's | 99.99% | None |
| **Intelligent-Tiering** | Unknown/changing patterns | 11 9's | 99.9% | None |
| **Standard-IA** | Infrequently accessed | 11 9's | 99.9% | 30 days |
| **One Zone-IA** | Infrequent, non-critical | 11 9's | 99.5% | 30 days |
| **Glacier Instant** | Archive, instant retrieval | 11 9's | 99.9% | 90 days |
| **Glacier Flexible** | Archive, minutes-hours | 11 9's | 99.99% | 90 days |
| **Glacier Deep Archive** | Long-term archive | 11 9's | 99.99% | 180 days |

**Mnemonic: "SIG-GIZ-OD"**
- Standard, Intelligent, Glacier (3 types), One Zone, Deep Archive

### S3 Features

**Versioning:**
- Keep multiple versions of objects
- Protects against accidental deletion
- Once enabled, can only suspend (not disable)

**Lifecycle Policies:**
- Transition objects between storage classes
- Expire objects after specified time
- Examples:
  - Move to IA after 30 days
  - Move to Glacier after 90 days
  - Delete after 365 days

**Replication:**
- **CRR** (Cross-Region Replication): Different regions
- **SRR** (Same-Region Replication): Same region
- Requires versioning enabled
- Use cases: Compliance, lower latency, disaster recovery

**Encryption:**
- **SSE-S3**: AWS managed keys
- **SSE-KMS**: AWS KMS managed keys
- **SSE-C**: Customer-provided keys
- **Client-Side**: Encrypt before upload

**Access Control:**
- Bucket policies (JSON)
- IAM policies
- ACLs (legacy)
- Block Public Access (default)

**S3 Transfer Acceleration:**
- Upload to edge location → CloudFront → S3
- Faster transfers over long distances
- Uses AWS backbone network

**S3 Event Notifications:**
- Trigger Lambda, SQS, SNS
- Events: Object created, deleted, restored

### S3 Performance

**Multipart Upload:**
- Required for objects > 5 GB
- Recommended for objects > 100 MB
- Upload parts in parallel

**S3 Select:**
- Retrieve subset of data using SQL
- Filter at S3 (less data transfer)
- Up to 400% faster, 80% cheaper

**Request Rates:**
- 3,500 PUT/COPY/POST/DELETE per second per prefix
- 5,500 GET/HEAD per second per prefix

---

## 2. Amazon EBS

### Overview
**Elastic Block Store** - Block-level storage for EC2

**Characteristics:**
- AZ-specific (attach only to EC2 in same AZ)
- Persist independently from EC2 instance
- Automatically replicated within AZ
- Can detach and reattach
- Maximum size: 64 TB per volume

### EBS Volume Types

| Type | Name | IOPS | Throughput | Use Case |
|------|------|------|------------|----------|
| **gp3** | General Purpose SSD | 3,000-16,000 | 125-1,000 MB/s | Boot volumes, virtual desktops |
| **gp2** | General Purpose SSD | 3-16,000 | Based on size | Legacy general purpose |
| **io2** | Provisioned IOPS SSD | 64,000 | 1,000 MB/s | Databases, critical apps |
| **io1** | Provisioned IOPS SSD | 64,000 | 1,000 MB/s | Legacy provisioned IOPS |
| **st1** | Throughput Optimized HDD | 500 | 500 MB/s | Big data, data warehouses |
| **sc1** | Cold HDD | 250 | 250 MB/s | Infrequent access, lowest cost |

**Decision Guide:**
- **SSD (gp3/io2)**: Transactional workloads, boot volumes
- **HDD (st1/sc1)**: Throughput-intensive, big data (cannot be boot)

### EBS Features

**Snapshots:**
- Incremental backups to S3
- First snapshot = full copy
- Subsequent = only changes
- Can copy across regions
- Can create AMI from snapshot

**Encryption:**
- At-rest and in-transit encryption
- Uses AWS KMS
- Minimal performance impact
- Encrypt existing volume via snapshot

**Multi-Attach (io1/io2 only):**
- Attach same volume to multiple EC2 instances
- All instances in same AZ
- Maximum 16 instances
- Use: Clustered applications

---

## 3. Amazon EFS

### Overview
**Elastic File System** - Managed NFS file system

**Characteristics:**
- Multi-AZ, regional service
- Automatically scales (petabytes)
- NFSv4.1 protocol
- Linux only
- Can mount to 1000s of EC2 instances

### EFS Performance Modes

**1. General Purpose:**
- Low latency
- Default mode
- Use: Web serving, CMS

**2. Max I/O:**
- Higher latency
- Higher aggregate throughput
- Use: Big data, media processing

### EFS Throughput Modes

**1. Bursting:**
- Throughput scales with file system size
- Default mode

**2. Provisioned:**
- Set throughput independent of size
- Pay for provisioned throughput

**3. Elastic:**
- Automatically scales throughput
- Pay for what you use

### EFS Storage Classes

- **Standard**: Frequently accessed
- **IA (Infrequent Access)**: Cost-optimized for files not accessed daily
- **Lifecycle Management**: Automatically move files to IA

---

## 4. AWS Storage Gateway

### Overview
**Hybrid cloud storage** - Bridge between on-premises and AWS

### Types

**1. File Gateway (NFS/SMB):**
- Store files as objects in S3
- Local cache for frequently accessed data
- Use: File shares, backup

**2. Volume Gateway:**
- Block storage volumes
- Two modes:
  - **Cached Volumes**: Frequently accessed data cached locally
  - **Stored Volumes**: Full dataset local, async backup to S3
- Use: Disaster recovery, backup

**3. Tape Gateway:**
- Virtual tape library (VTL)
- Replace physical tape infrastructure
- Store tapes in Glacier
- Use: Archive, compliance

---

## 5. AWS Snow Family

### Overview
**Physical devices** for data migration and edge computing

### Devices

**1. Snowcone:**
- Smallest device
- **8 TB** (HDD) or **14 TB** (SSD) storage
- 4 GB RAM, 2 CPUs
- Can run EC2 instances
- Portable, rugged
- Use: Edge computing, remote locations

**2. Snowball Edge:**
- **Storage Optimized**: 80 TB storage
- **Compute Optimized**: 42 TB storage + more compute
- Can run EC2, Lambda locally
- Cluster multiple devices
- Use: Large data migrations, edge processing

**3. Snowmobile:**
- **100 PB** capacity
- Shipping container on truck
- GPS tracked, armed security
- Use: Data center migration, massive datasets

### When to Use Snow

**Use Snow Family when:**
- Limited bandwidth
- High network costs
- Transfer time > 1 week over network
- Offline data transfer needed
- Edge computing required

**Formula**: If transfer takes > 1 week via network, use Snow

---

## 6. Amazon FSx

### FSx for Windows File Server
- Managed Windows file system
- **SMB** protocol
- Active Directory integration
- Fully managed backups
- SSD and HDD options
- Use: Windows applications, home directories

### FSx for Lustre
- High-performance file system
- **POSIX-compliant**
- Sub-millisecond latencies
- Integrates with S3
- Scales to 100s GB/s throughput
- Use: HPC, machine learning, video processing

---

## 🎯 Storage Decision Matrix

```
Need storage?
├─ Object storage for files/backups? → S3
├─ Block storage for EC2? → EBS
├─ Shared file system (Linux)? → EFS
├─ Shared file system (Windows)? → FSx for Windows
├─ High-performance computing? → FSx for Lustre
├─ Hybrid cloud integration? → Storage Gateway
└─ Offline/physical data transfer? → Snow Family
```

---

## 📊 Storage Comparison

| Feature | S3 | EBS | EFS | FSx Windows |
|---------|----|----|-----|-------------|
| **Type** | Object | Block | File (NFS) | File (SMB) |
| **Access** | HTTP/API | Mount to EC2 | Mount (NFS) | Mount (SMB) |
| **Scope** | Regional | AZ | Regional | Regional/Multi-AZ |
| **Sharing** | Via URL/API | Single EC2* | Multiple EC2 | Multiple instances |
| **Max Size** | Unlimited | 64 TB/volume | Unlimited | 64 TB |
| **Use Case** | Files, backups | Boot disk, DB | Shared files | Windows apps |

*Except io1/io2 Multi-Attach (max 16 EC2)

---

## 🎯 Exam Tips

### Common Scenarios

**Scenario**: *Store millions of images uploaded by users*
→ **S3 Standard** (unlimited storage, HTTP access)

**Scenario**: *Shared file system for Linux EC2 instances across AZs*
→ **Amazon EFS**

**Scenario**: *Persistent block storage for EC2 database*
→ **EBS (io2 for high performance)**

**Scenario**: *Archive data, rarely accessed, lowest cost*
→ **S3 Glacier Deep Archive**

**Scenario**: *Transfer 50 TB data from on-premises to AWS, limited bandwidth*
→ **AWS Snowball Edge**

**Scenario**: *Windows file shares with Active Directory*
→ **FSx for Windows File Server**

**Scenario**: *HPC workload needing sub-ms latency*
→ **FSx for Lustre**

**Scenario**: *Backup on-prem files to AWS*
→ **File Gateway**

### Key Points to Remember

**S3:**
- Bucket names = globally unique
- Objects up to 5 TB (multipart for > 5 GB)
- 11 nines durability, 99.99% availability (Standard)
- Versioning protects against deletion
- Transfer Acceleration for long-distance uploads

**EBS:**
- AZ-specific (not regional)
- Snapshots stored in S3 (incremental)
- gp3/io2 = SSD (boot volumes, databases)
- st1/sc1 = HDD (big data, cannot boot)
- Max 64 TB per volume

**EFS:**
- Regional, Multi-AZ by default
- Automatically scales to petabytes
- Pay for what you use
- Linux only (NFSv4.1)
- Can mount to 1000s of instances

**Snow Family:**
- Snowcone: 8-14 TB
- Snowball: 42-80 TB
- Snowmobile: 100 PB
- Use when transfer > 1 week over network

### Exam Keyword Mapping

| Keyword | Service |
|---------|---------|
| "Object storage" | S3 |
| "Block storage for EC2" | EBS |
| "Shared file system (Linux)" | EFS |
| "Windows file shares" | FSx for Windows |
| "HPC, high performance" | FSx for Lustre |
| "Archive, lowest cost" | S3 Glacier Deep Archive |
| "Offline data transfer" | Snow Family |
| "Hybrid cloud storage" | Storage Gateway |
| "Multipart upload" | S3 (objects > 100 MB) |
| "11 nines durability" | S3 |
| "Provisioned IOPS" | EBS io2/io1 |

---

## 📝 Practice Questions

### Question 1
**A company needs to store 500 TB of archival data that is accessed once per year. Cost is the primary concern. Which storage solution should they use?**

A) S3 Standard  
B) S3 Glacier Flexible Retrieval  
C) S3 Glacier Deep Archive  
D) EBS Cold HDD

<details>
<summary>Show Answer</summary>

**Answer: C**

S3 Glacier Deep Archive is the lowest cost storage class, perfect for data accessed rarely (once or twice per year). Retrieval time is 12-48 hours, which is acceptable for the use case.
</details>

### Question 2
**An application requires a shared file system that can be accessed by multiple Linux EC2 instances across different Availability Zones. Which service should be used?**

A) Amazon S3  
B) Amazon EBS  
C) Amazon EFS  
D) Instance Store

<details>
<summary>Show Answer</summary>

**Answer: C**

Amazon EFS provides a shared NFS file system that can be mounted by multiple EC2 instances across different AZs. EBS is AZ-specific and typically attaches to a single instance.
</details>

### Question 3
**A company needs to transfer 50 TB of data from their on-premises data center to AWS. They have limited bandwidth (10 Mbps). What is the most appropriate solution?**

A) Use AWS Direct Connect  
B) Upload via S3 Transfer Acceleration  
C) Use AWS Snowball Edge  
D) Use AWS DataSync

<details>
<summary>Show Answer</summary>

**Answer: C**

At 10 Mbps, transferring 50 TB would take approximately 46 days. AWS Snowball Edge is designed for this scenario - physical device shipped to customer, data loaded locally, then shipped to AWS.
</details>

---

## 🔗 Additional Resources

- [S3 User Guide](https://docs.aws.amazon.com/s3/)
- [EBS User Guide](https://docs.aws.amazon.com/ebs/)
- [EFS User Guide](https://docs.aws.amazon.com/efs/)
- [Storage Gateway Guide](https://docs.aws.amazon.com/storagegateway/)

---

**Estimated Study Time**: 6-8 hours  
**Difficulty**: ⭐⭐⭐

[⬅️ Previous: Compute](../03-Compute/README.md) | [Next: Database ➡️](../05-Database/README.md) | [📚 Main](../README.md)

