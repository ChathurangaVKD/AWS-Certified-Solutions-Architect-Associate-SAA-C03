# 04: Storage Services - Ultra Fast Learning 🚀

## S3 Storage Classes
| Class | Use Case | Retrieval | Min Storage | Availability |
|-------|----------|-----------|-------------|--------------|
| Standard | Frequent access | Instant | None | 99.99% |
| Intelligent-Tiering | Unknown pattern | Instant | None | 99.9% |
| Standard-IA | Infrequent | Instant | 30 days | 99.9% |
| One Zone-IA | Non-critical | Instant | 30 days | 99.5% |
| Glacier Instant | Archive + instant | Instant | 90 days | 99.9% |
| Glacier Flexible | Archive | 1-5 min to 12 hr | 90 days | 99.99% |
| Glacier Deep Archive | Long-term | 12-48 hours | 180 days | 99.99% |

**Mnemonic: S-I-S-O-G³** (Standard, Intelligent, Standard-IA, One Zone, 3 Glaciers)

## S3 Key Features

### Versioning
- Keep multiple versions of objects
- Protects from accidental deletes
- Once enabled, can only **suspend** (not disable)
- Delete marker on delete (can restore)

### Encryption
- **SSE-S3**: AWS managed keys (AES-256)
- **SSE-KMS**: AWS KMS managed keys (audit trail)
- **SSE-C**: Customer provided keys
- **Client-Side**: Encrypt before upload

### Replication
- **CRR**: Cross-Region (compliance, latency)
- **SRR**: Same-Region (log aggregation, test/prod sync)
- Requires versioning enabled
- Only new objects replicated (existing objects need batch job)

### Lifecycle Policies
- Transition actions (move to cheaper class)
- Expiration actions (delete after X days)
- Apply to prefixes or tags

### S3 Performance
- **3,500 PUT/COPY/POST/DELETE** per second per prefix
- **5,500 GET/HEAD** per second per prefix
- **Multipart upload**: Required >5GB, recommended >100MB
- **S3 Transfer Acceleration**: CloudFront edge locations for upload
- **Byte-Range Fetches**: Parallel downloads

## EBS (Elastic Block Store)

### EBS Volume Types
| Type | IOPS | Throughput | Use Case |
|------|------|------------|----------|
| gp3 | 16K | 1000 MB/s | General, cost-effective |
| gp2 | 16K | 250 MB/s | General, burst |
| io2/io1 | 64K/256K | 4000 MB/s | High performance DB |
| st1 | 500 | 500 MB/s | Big data, logs |
| sc1 | 250 | 250 MB/s | Cold storage |

**SSD (gp, io)**: Small random I/O, databases  
**HDD (st, sc)**: Large sequential I/O, big data

### EBS Features
- **AZ-locked**: Must be in same AZ as EC2
- **Snapshots**: Stored in S3, incremental, cross-region copy
- **Encryption**: Uses KMS, transparent, snapshot encrypted too
- **Multi-Attach**: io1/io2 only, max 16 instances (cluster)

## EFS (Elastic File System)
- **Network file system** (NFS v4.1)
- **Multi-AZ**, can mount to multiple EC2
- **Linux only** (not Windows)
- **10x cost** of gp2 EBS
- **Auto-scaling**, pay per use
- **Performance modes**: General Purpose, Max I/O
- **Throughput modes**: Bursting, Provisioned, Elastic
- **Storage classes**: Standard, IA (lifecycle policy)

## Storage Gateway
- **Hybrid cloud** storage
- **Types**:
  - **File Gateway**: S3 via NFS/SMB
  - **Volume Gateway**: iSCSI, cached or stored
  - **Tape Gateway**: Virtual tapes to S3/Glacier

## Snow Family
- **Snowcone**: 8 TB, edge computing
- **Snowball Edge**: 80 TB storage + compute
- **Snowmobile**: 100 PB, truck
- **Use case**: TB/PB data transfer, limited bandwidth

## FSx
- **FSx for Windows**: Windows file server, SMB, AD integration
- **FSx for Lustre**: High-performance computing, ML, 100+ GB/s
- **FSx for NetApp ONTAP**: NFS, SMB, iSCSI
- **FSx for OpenZFS**: NFS, up to 1M IOPS

## Quick Exam Tips
- **S3**: Object storage, unlimited, 5 TB max object
- **S3 Standard**: 99.99% availability, 11 nines durability
- **Glacier**: Minutes to hours retrieval
- **EBS**: Block storage, AZ-locked, persistent
- **Instance Store**: Ephemeral, lost on stop
- **EFS**: Multi-AZ file system, Linux only
- **Lifecycle**: Automate transitions between storage classes
- **Versioning**: Protects from deletes, cannot disable once enabled
- **MFA Delete**: Extra protection for versioned buckets
- **S3 encryption in transit**: HTTPS (SSL/TLS)
- **Presigned URL**: Temporary access (default 3600 sec)

