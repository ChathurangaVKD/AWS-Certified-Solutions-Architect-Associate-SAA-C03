# ⚡ Fast Learning - Security & Compliance

> **Time to Complete**: 60-75 minutes | **Exam Weight**: ~20-25%

## 🎯 Must-Know Concepts (5 Minutes)

### Security Service Selector (KSS-WCGI)
```
ENCRYPTION KEYS? → KMS (Key Management Service)
SECRETS/PASSWORDS? → Secrets Manager
CERTIFICATES? → ACM (Certificate Manager)
FIREWALL? → Security Groups, NACLs, WAF
DDoS PROTECTION? → Shield (Standard/Advanced)
COMPLIANCE? → CloudTrail, Config, Inspector
IDENTITY? → IAM, Cognito, Directory Service
DETECTION? → GuardDuty, Macie, Detective
```

**Memory Aid**: "Keys Secure Secrets, While Controlling Guarding Identity"

## 📊 Quick Reference Tables

### Encryption Services Matrix
| Service | Type | Use Case | Key Management |
|---------|------|----------|----------------|
| **KMS** | Encryption keys | Encrypt AWS resources | AWS managed or Customer |
| **CloudHSM** | Hardware module | Regulatory compliance | Customer only |
| **Secrets Manager** | Secret rotation | DB credentials, API keys | Auto-rotation |
| **Parameter Store** | Config/secrets | App config, simple secrets | Free tier available |
| **ACM** | SSL/TLS certs | HTTPS/TLS | AWS managed, auto-renew |

### Security Monitoring Services
| Service | What It Does | Detects | Cost Model |
|---------|--------------|---------|------------|
| **GuardDuty** | Threat detection | Malicious activity, anomalies | Events analyzed |
| **Macie** | Data security | Sensitive data in S3 (PII) | GB scanned |
| **Inspector** | Vulnerability assessment | EC2/ECR vulnerabilities | Assessments run |
| **Detective** | Security investigation | Root cause analysis | GB ingested |
| **Security Hub** | Central dashboard | Aggregates findings | Checks run |

## 🔥 Exam Hot Topics

### 1. KMS Key Types (Critical!)
```
AWS MANAGED KEYS
├── Free
├── Auto-rotation every year (mandatory)
├── Format: aws/service-name (e.g., aws/s3)
└── Use: Default encryption

CUSTOMER MANAGED KEYS (CMK)
├── $1/month per key
├── Optional auto-rotation (yearly)
├── Full control over key policies
├── Can be disabled/deleted
└── Use: Custom requirements, compliance

AWS OWNED KEYS
├── Free
├── Used by AWS for multiple accounts
├── No visibility or control
└── Use: DynamoDB encryption (default)
```

**Memory Aid**: "AMC" = AWS (free, auto), Customer (control, cost), Owned (opaque)

### 2. Data Encryption States
```
ENCRYPTION AT REST
├── KMS for most AWS services
├── S3: SSE-S3, SSE-KMS, SSE-C
├── EBS: Encrypted volumes
├── RDS: Encryption at creation
└── DynamoDB: Server-side encryption

ENCRYPTION IN TRANSIT
├── SSL/TLS (HTTPS)
├── VPN (Site-to-Site)
├── Direct Connect + VPN
├── Client-side encryption
└── AWS services use TLS by default
```

### 3. WAF, Shield, Firewall Manager
| Service | Layer | Purpose | Use Case |
|---------|-------|---------|----------|
| **WAF** | Layer 7 | Web app firewall | SQL injection, XSS protection |
| **Shield Standard** | Layer 3/4 | DDoS protection | Free, automatic |
| **Shield Advanced** | Layer 3/4/7 | Enhanced DDoS | $3K/month, 24/7 support |
| **Firewall Manager** | Multiple | Central management | Multi-account security |

**WAF Rules**:
- IP addresses
- HTTP headers/body
- Query strings
- Geographic location
- Rate limiting

### 4. AWS Config vs CloudTrail
| Feature | CloudTrail | Config |
|---------|------------|--------|
| **Purpose** | Who did what | Resource compliance |
| **Tracks** | API calls | Resource configuration changes |
| **Question** | "Who launched this EC2?" | "Is S3 bucket encrypted?" |
| **Output** | Event logs | Configuration snapshots |
| **Rules** | N/A | Compliance rules |
| **Remediation** | No | Yes (with Systems Manager) |

**Memory Aid**: "Trail = Trail of actions, Config = Configuration compliance"

## 💡 Common Exam Scenarios

### Scenario 1: Encrypt Existing Unencrypted EBS
**Q**: Need to encrypt unencrypted EBS volume
**✅ ANSWER**: Create snapshot → Copy with encryption → Create volume from encrypted snapshot

### Scenario 2: Rotate Database Credentials
**Q**: Automate database password rotation every 30 days
**✅ ANSWER**: AWS Secrets Manager with automatic rotation (not Parameter Store)

### Scenario 3: Protect Against DDoS
**Q**: Web application needs DDoS protection
- **Basic (free)**: Shield Standard (auto-enabled)
- **Advanced**: Shield Advanced + WAF + Route 53

### Scenario 4: Detect Unauthorized Access
**Q**: Get alerts on suspicious activity in AWS account
**✅ ANSWER**: Enable GuardDuty (threat detection)

### Scenario 5: Find Sensitive Data in S3
**Q**: Discover S3 buckets containing credit card numbers or PII
**✅ ANSWER**: Amazon Macie

### Scenario 6: Audit API Calls
**Q**: Track who deleted an S3 object
**✅ ANSWER**: CloudTrail (logs all API calls)

### Scenario 7: Ensure Compliance
**Q**: Verify all S3 buckets are encrypted and private
**✅ ANSWER**: AWS Config with compliance rules

### Scenario 8: Cross-Account Access Securely
**Q**: Account A needs to access resources in Account B
**✅ ANSWER**: IAM roles with trust policy (not sharing credentials)

## 🎓 Speed Learning Tips

### KMS Envelope Encryption
```
HOW IT WORKS:
1. Data Encryption Key (DEK) encrypts data
2. CMK encrypts DEK
3. Store encrypted data + encrypted DEK together

WHY:
├── Faster (encrypt locally)
├── Less network traffic
├── Better performance for large data
└── CMK never leaves KMS
```

### S3 Security Layers (Defense in Depth)
```
1. IAM Policies (user permissions)
2. Bucket Policies (resource-based)
3. S3 Block Public Access (account-level)
4. Encryption (SSE-S3, SSE-KMS, SSE-C)
5. Versioning + MFA Delete
6. VPC Endpoints (private access)
7. CloudTrail (audit access)
8. Macie (detect sensitive data)
```

### Secrets Manager vs Parameter Store
| Feature | Secrets Manager | Parameter Store |
|---------|----------------|-----------------|
| **Rotation** | ✅ Automatic (RDS, etc.) | ❌ Manual |
| **Cost** | $$$  ($0.40/secret/month) | Free (standard), $ (advanced) |
| **Integration** | RDS, Redshift, DocumentDB | Any service |
| **Cross-region** | Replicate secrets | Must copy manually |
| **Use Case** | DB credentials, API keys | App config, simple values |

**Decision**: Need rotation? → Secrets Manager, Otherwise → Parameter Store

## 📝 Rapid-Fire Facts

### KMS Important Limits
- **Max request rate**: 5,500/10,000/30,000 (depends on key type)
- **Max data size**: 4 KB (use envelope encryption for larger)
- **Auto-rotation**: Every 365 days (CMK only)
- **Key deletion**: 7-30 day waiting period
- **Regions**: Multi-region keys available

### CloudTrail Best Practices
✅ Enable in all regions
✅ Enable log file validation (integrity)
✅ Encrypt logs with KMS
✅ Store in S3 with lifecycle policy
✅ Monitor with CloudWatch Logs
✅ Use Organizations trail (multi-account)
✅ Enable for management + data events

### GuardDuty Data Sources
- VPC Flow Logs
- CloudTrail event logs  
- DNS logs
- EKS audit logs
- S3 data events
- RDS login events
- EBS volume data
- Lambda network activity

### Compliance Programs (Sample)
- **PCI DSS** - Payment cards
- **HIPAA** - Healthcare
- **SOC 1/2/3** - Security controls
- **ISO 27001** - Information security
- **FedRAMP** - US government
- **GDPR** - EU data protection

## 🚀 5-Minute Master Review

### Security Best Practices Checklist
✅ **Identity**: MFA on root + all users
✅ **Access**: Least privilege, use roles
✅ **Detection**: GuardDuty, CloudTrail, Config
✅ **Infrastructure**: Security groups, NACLs
✅ **Data**: Encrypt at rest + in transit
✅ **Incident**: CloudTrail, backup, playbooks
✅ **Compliance**: Config rules, automated checks

### Encryption Decision Tree
```
1. What to encrypt?
   DATA AT REST → KMS, SSE
   DATA IN TRANSIT → TLS/SSL, VPN
   
2. Who manages keys?
   AWS → AWS managed keys (free)
   YOU → Customer managed keys ($)
   COMPLIANCE → CloudHSM (dedicated)
   
3. For S3, what level of control?
   SIMPLE → SSE-S3
   AUDIT TRAIL → SSE-KMS
   YOUR KEYS → SSE-C
   BEFORE UPLOAD → Client-side
```

### Certificate Management
```
ACM (AWS Certificate Manager)
├── Free SSL/TLS certificates
├── Auto-renewal
├── Integration: ALB, CloudFront, API Gateway
├── Regional (except CloudFront = us-east-1)
└── Cannot export private key

IMPORT CERTIFICATES
├── Third-party certificates
├── Manual renewal
├── Can export
└── Use when: Existing certs, special requirements
```

### Common Mistakes to Avoid
❌ Not enabling MFA on root account
❌ Using root account for daily tasks
❌ Sharing IAM credentials
❌ Forgetting CloudTrail in all regions
❌ Not encrypting sensitive data
❌ Public S3 buckets with sensitive data
❌ Using Parameter Store when rotation needed
❌ Not enabling GuardDuty for threat detection
❌ Storing secrets in code or environment variables
❌ Not using Shield Standard (it's free!)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. What rotates DB passwords automatically? __
2. Which service detects PII in S3? __
3. Can you encrypt existing unencrypted RDS? __
4. What tracks API calls? __
5. What's the cost of Shield Standard? __
6. KMS key max data size? __
7. What detects threats using ML? __
8. What checks resource compliance? __

---

### Shared Responsibility Model - Security
```
AWS RESPONSIBILITY (Security OF the cloud)
├── Physical security of data centers
├── Hardware/infrastructure
├── Network infrastructure
├── Managed service operations
└── Hypervisor

CUSTOMER RESPONSIBILITY (Security IN the cloud)
├── Data encryption (at rest & in transit)
├── IAM (users, groups, roles, policies)
├── OS patches and updates
├── Application security
├── Network configuration (SG, NACL)
├── Firewall configuration
└── Compliance validation
```

### AWS Organizations - Security Features
- **Service Control Policies (SCP)**: Limit permissions
- **Consolidated billing**: Security cost tracking
- **CloudTrail**: Organization trail
- **GuardDuty**: Delegated administrator
- **Security Hub**: Central security view
- **Config**: Organization rules

### AWS Systems Manager - Session Manager
- **Purpose**: Secure shell access to EC2
- **No SSH keys needed**: IAM-based access
- **Auditing**: CloudTrail logs all sessions
- **No bastion host**: Direct access via console/CLI
- **Port 22**: Not required (uses port 443)

## ⏱️ Next Steps
- Time spent: ~60-75 min
- Practice: Enable GuardDuty, create KMS key, CloudTrail
- Ready for: Security practice questions
- Move to: Module 08 - Application Integration

---

**Quick Answers**: 
1) AWS Secrets Manager
2) Amazon Macie
3) No (must create new from snapshot with encryption)
4) AWS CloudTrail
5) Free (automatically enabled)
6) 4 KB (use envelope encryption for more)
7) Amazon GuardDuty
8) AWS Config

