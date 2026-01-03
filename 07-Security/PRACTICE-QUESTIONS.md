# Security - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company wants to encrypt data at rest in S3 with full control over encryption keys including custom rotation policies and audit trails. Which encryption method should be used?

A. SSE-S3 (Server-Side Encryption with S3-Managed Keys)  
B. SSE-KMS with AWS managed keys  
C. SSE-KMS with Customer Managed Keys (CMK)  
D. SSE-C (Customer-Provided Keys)  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **SSE-KMS with Customer Managed Keys (CMK)** provides complete control
- Create, manage, rotate encryption keys
- CloudTrail audit trail for key usage
- Fine-grained access control via key policies
- Automatic or manual key rotation

**S3 Encryption Options Comparison**:

| Method | Key Management | Rotation | Audit Trail | Cost |
|--------|----------------|----------|-------------|------|
| **SSE-S3** | AWS | AWS handles | No | Free |
| **SSE-KMS (AWS managed)** | AWS | Annual (automatic) | Yes (CloudTrail) | KMS API charges |
| **SSE-KMS (CMK)** | Customer | On-demand/annual | Yes (CloudTrail) | KMS API charges |
| **SSE-C** | Customer provides | Customer manages | No | Free |

**CMK Benefits**:
- Custom rotation schedule (enable automatic yearly rotation)
- Disable/enable keys
- Define key policies and grants
- Cross-account access
- Complete audit trail

**References:** AWS KMS, S3 Encryption, Customer Managed Keys
</details>

---

### Question 2
An application needs to securely store database credentials that should be automatically rotated every 30 days. Which AWS service is MOST appropriate?

A. AWS Systems Manager Parameter Store  
B. AWS Secrets Manager  
C. AWS KMS  
D. Amazon S3 with encryption  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Secrets Manager** designed specifically for secrets with built-in rotation
- Automatic rotation for RDS, DocumentDB, Redshift, Amazon Redshift
- Lambda-based custom rotation for other services
- Versioning and immediate rotation

**Secrets Manager Features**:
- Automatic rotation (configurable schedule)
- Built-in integration with AWS databases
- Encryption at rest (KMS)
- Fine-grained access control (IAM)
- Audit capability (CloudTrail)
- Cross-region replication
- Version management

**Secrets Manager vs Parameter Store**:

| Feature | Secrets Manager | Parameter Store (Standard) | Parameter Store (Advanced) |
|---------|----------------|----------------------------|----------------------------|
| **Automatic Rotation** | Yes | No | No |
| **Built-in RDS Integration** | Yes | No | No |
| **Cost** | $0.40/secret/month + API calls | Free | $0.05/parameter/month |
| **Secret Size** | 64 KB | 4 KB | 8 KB |
| **Encryption** | Always (KMS) | Optional (KMS) | Optional (KMS) |
| **Use Case** | DB credentials, API keys | Configuration, non-rotating secrets | Configuration, larger values |

**Rotation Configuration**:
```json
{
  "automaticallyAfterDays": 30,
  "rotationLambdaARN": "arn:aws:lambda:...",
  "rotationEnabled": true
}
```

**References:** AWS Secrets Manager, Secrets Rotation, Credential Management
</details>

---

### Question 3
A company must ensure that all API calls across their AWS organization are logged and stored for 7 years for compliance. Which services should be configured?

A. CloudWatch Logs with 7-year retention  
B. CloudTrail with S3 storage and Glacier lifecycle  
C. AWS Config with long-term storage  
D. VPC Flow Logs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS CloudTrail** records all API calls (management and data events)
- Store logs in S3 for long-term retention
- Use S3 Lifecycle policies to transition to Glacier for cost optimization

**CloudTrail Configuration**:
1. Enable CloudTrail in all regions
2. Store logs in S3 bucket
3. Enable log file validation (integrity checking)
4. Configure S3 Lifecycle policy:
   - Transition to Glacier after 90 days
   - Retain for 7 years

**CloudTrail Features**:
- **Management Events**: Control plane operations (CreateInstance, DeleteBucket)
- **Data Events**: Data plane operations (S3 GetObject, Lambda invocations)
- **Insights Events**: Detect unusual activity
- **Multi-region**: Capture events from all regions
- **Multi-account**: Organization trail
- **Log file integrity**: Detect tampering

**Best Practice Configuration**:
```json
{
  "Trail": {
    "IsMultiRegionTrail": true,
    "IncludeGlobalServiceEvents": true,
    "IsOrganizationTrail": true,
    "EnableLogFileValidation": true
  }
}
```

**S3 Lifecycle for Cost Optimization**:
```json
{
  "Rules": [
    {
      "Transitions": [
        {"Days": 90, "StorageClass": "GLACIER"},
        {"Days": 180, "StorageClass": "DEEP_ARCHIVE"}
      ],
      "Expiration": {"Days": 2555}  // 7 years
    }
  ]
}
```

**References:** AWS CloudTrail, Compliance Logging, Long-term Retention
</details>

---

### Question 4
A company wants to detect and respond to security threats in their AWS environment automatically. Which service provides intelligent threat detection?

A. AWS CloudTrail  
B. Amazon GuardDuty  
C. AWS Config  
D. AWS Security Hub  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon GuardDuty** provides intelligent, continuous threat detection
- Uses machine learning and threat intelligence
- Analyzes multiple data sources automatically
- No infrastructure to manage

**GuardDuty Data Sources**:
1. **AWS CloudTrail Events**: Unusual API calls, unauthorized deployments
2. **VPC Flow Logs**: Malicious IP addresses, unusual traffic patterns
3. **DNS Logs**: Domain generation algorithms, C&C communication
4. **EKS Audit Logs**: Kubernetes security events
5. **S3 Data Events**: Suspicious access patterns
6. **Lambda Network Activity**: Suspicious connections

**GuardDuty Finding Types**:
- **Reconnaissance**: Port scanning, unusual API activity
- **Instance Compromise**: Malware, cryptocurrency mining, backdoor
- **Account Compromise**: Credential misuse, unusual behavior
- **Bucket Compromise**: Suspicious S3 access
- **Persistence**: IAM changes, unauthorized access

**GuardDuty vs Other Security Services**:

| Service | Purpose | Detection Type | Response |
|---------|---------|----------------|----------|
| **GuardDuty** | Threat detection | Automated ML-based | EventBridge rules |
| **Security Hub** | Centralized findings | Aggregation | Manual/automated |
| **Inspector** | Vulnerability scanning | Agent/agentless scans | Manual remediation |
| **Macie** | Data protection | PII/sensitive data | Manual/automated |
| **Config** | Compliance | Rule-based | Remediation actions |

**Automated Response Pattern**:
GuardDuty Finding → EventBridge → Lambda → Isolate Instance/Block IP

**References:** Amazon GuardDuty, Threat Detection, Security Automation
</details>

---

### Question 5
A company needs to ensure all S3 buckets are encrypted and not publicly accessible. Which service can continuously monitor and evaluate compliance?

A. AWS CloudTrail  
B. AWS Config  
C. Amazon GuardDuty  
D. AWS Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Config** continuously monitors and records resource configurations
- Evaluates compliance against desired configurations
- Provides configuration history and change tracking
- Automated or manual remediation

**AWS Config Key Features**:

**Config Rules** (Managed and Custom):
- `s3-bucket-public-read-prohibited`
- `s3-bucket-public-write-prohibited`
- `s3-bucket-server-side-encryption-enabled`
- `encrypted-volumes`
- `required-tags`
- `approved-amis-by-id`

**Config Components**:
1. **Configuration Recorder**: Captures resource configurations
2. **Config Rules**: Define desired configurations
3. **Remediation Actions**: Automatic fixes via SSM Automation
4. **Conformance Packs**: Packaged compliance rules
5. **Aggregators**: Multi-account/region view

**Example: S3 Encryption Compliance**:
```json
{
  "ConfigRule": {
    "ConfigRuleName": "s3-encryption-enabled",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
    }
  },
  "RemediationConfiguration": {
    "Automatic": true,
    "TargetType": "SSM_DOCUMENT",
    "TargetIdentifier": "AWS-EnableS3BucketEncryption"
  }
}
```

**Config vs CloudTrail vs GuardDuty**:
- **Config**: WHAT (configuration state, compliance)
- **CloudTrail**: WHO/WHEN (API calls, audit trail)
- **GuardDuty**: THREATS (security threats, anomalies)

**References:** AWS Config, Compliance Monitoring, Configuration Management
</details>

---

### Question 6
An organization wants to centrally manage security findings from multiple AWS accounts and security services. Which service should be used?

A. Amazon GuardDuty  
B. AWS Security Hub  
C. AWS Config  
D. Amazon Inspector  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Security Hub** provides centralized security and compliance view
- Aggregates findings from multiple AWS services and accounts
- Security standards compliance (CIS, PCI-DSS, AWS Foundational Security Best Practices)
- Automated compliance checks

**Security Hub Integrations**:

**AWS Services**:
- Amazon GuardDuty (threat detection)
- Amazon Inspector (vulnerability assessment)
- Amazon Macie (data protection)
- AWS IAM Access Analyzer (IAM policy analysis)
- AWS Firewall Manager (firewall rule management)
- AWS Config (compliance rules)
- Amazon Detective (security investigation)

**Third-Party Integrations**:
- Splunk, Palo Alto Networks, Trend Micro, etc.

**Security Hub Features**:
1. **Consolidated Dashboard**: Single pane of glass
2. **Security Standards**: CIS AWS Foundations, PCI-DSS, AWS Best Practices
3. **Automated Checks**: Continuous compliance evaluation
4. **Finding Aggregation**: From all integrated services
5. **Custom Insights**: Create custom views
6. **Automated Remediation**: EventBridge + Lambda/SSM

**Security Hub Workflow**:
```
Multiple Accounts → Security Hub Master Account
↓
Findings from GuardDuty, Inspector, Macie, Config, IAM Access Analyzer
↓
Security Standards Compliance Checks
↓
Consolidated Dashboard + Automated Remediation
```

**Use Cases**:
- Multi-account security management
- Compliance reporting
- Security posture assessment
- Automated remediation workflows

**References:** AWS Security Hub, Centralized Security Management
</details>

---

### Question 7
A company wants to detect when S3 buckets contain sensitive personally identifiable information (PII). Which service should be used?

A. Amazon GuardDuty  
B. Amazon Macie  
C. AWS Config  
D. Amazon Inspector  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon Macie** is data security service that discovers and protects sensitive data
- Uses machine learning to identify PII, financial data, credentials
- Automated S3 bucket inventory and classification
- Continuous monitoring and alerts

**Macie Capabilities**:

**Data Discovery**:
- Credit card numbers
- Social security numbers
- Passport numbers
- Driver's license numbers
- Bank account numbers
- Personal health information
- Authentication credentials

**Macie Features**:
1. **Automated Discovery Jobs**: Scan S3 buckets
2. **Sensitive Data Types**: Pre-built and custom identifiers
3. **Bucket Inventory**: Complete S3 bucket assessment
4. **Policy Findings**: Public access, encryption, replication issues
5. **Sensitive Data Findings**: Location and type of sensitive data
6. **Integration**: Security Hub, EventBridge for automation

**Macie Finding Types**:

| Category | Examples |
|----------|----------|
| **Policy Findings** | Public bucket, unencrypted, no versioning |
| **Sensitive Data Findings** | PII detected, credentials found |

**Automated Response Pattern**:
```
Macie Detects PII → EventBridge → Lambda → 
  - Encrypt bucket
  - Update bucket policy
  - Send SNS notification
  - Create Jira ticket
```

**Macie vs Other Services**:
- **Macie**: Data privacy, PII detection in S3
- **GuardDuty**: Threat detection, malicious activity
- **Inspector**: Vulnerability scanning (EC2, ECR, Lambda)
- **Config**: Configuration compliance

**References:** Amazon Macie, Data Protection, PII Detection
</details>

---

### Question 8
A company wants to analyze IAM policies to identify resources shared with external entities. Which service provides this capability?

A. AWS IAM Policy Simulator  
B. IAM Access Analyzer  
C. AWS Trusted Advisor  
D. AWS Config  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **IAM Access Analyzer** uses automated reasoning to analyze resource policies
- Identifies resources shared with external principals
- Validates IAM policies against best practices
- Generates findings for review

**IAM Access Analyzer Features**:

**1. External Access Analysis**:
- S3 buckets
- IAM roles
- KMS keys
- Lambda functions
- SQS queues
- Secrets Manager secrets
- SNS topics

**2. Policy Validation**:
- Check policy grammar
- Security warnings
- Errors and suggestions
- Best practice recommendations

**3. Policy Generation**:
- Generate policies based on CloudTrail activity
- Least privilege policies
- Review and refine

**Finding Types**:
```json
{
  "FindingType": "ExternalAccess",
  "Resource": "arn:aws:s3:::my-bucket",
  "Principal": {
    "AWS": "123456789012"  // External account
  },
  "Condition": {},
  "Action": ["s3:GetObject"]
}
```

**Access Analyzer vs Other Tools**:

| Tool | Purpose |
|------|---------|
| **Access Analyzer** | External access, policy validation, policy generation |
| **Policy Simulator** | Test policy effects |
| **Trusted Advisor** | Best practices, cost optimization |
| **Config** | Resource configuration compliance |

**Use Cases**:
- Identify unintended external access
- Validate policies before deployment
- Generate least-privilege policies
- Continuous monitoring for access changes

**References:** IAM Access Analyzer, Policy Analysis, External Access Detection
</details>

---

### Question 9
A web application needs protection against common web exploits like SQL injection and cross-site scripting (XSS). Which AWS service provides this protection?

A. AWS Shield  
B. AWS WAF  
C. Security Groups  
D. Network ACLs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS WAF** (Web Application Firewall) protects against common web exploits
- Filters HTTP/HTTPS requests based on rules
- Integrates with CloudFront, ALB, API Gateway, AppSync
- Managed rules and custom rules

**AWS WAF Capabilities**:

**1. Managed Rule Groups**:
- AWS Managed Rules (Core Rule Set, Known Bad Inputs, SQL Database, etc.)
- AWS Marketplace Rules (third-party)
- Rate-based rules (DDoS protection)

**2. Custom Rules**:
- IP address filtering
- Geographic blocking
- String/regex matching
- Size constraints
- SQL injection protection
- XSS protection

**3. Request Filtering**:
```json
{
  "Rule": {
    "Name": "BlockSQLInjection",
    "Statement": {
      "SqliMatchStatement": {
        "FieldToMatch": {
          "QueryString": {}
        }
      }
    },
    "Action": {"Block": {}}
  }
}
```

**WAF Components**:

| Component | Description |
|-----------|-------------|
| **Web ACL** | Container for rules |
| **Rules** | Match conditions + action |
| **Rule Groups** | Collection of reusable rules |
| **IP Sets** | List of IP addresses |
| **Regex Pattern Sets** | Regex patterns |

**Rate-Based Rule** (DDoS Protection):
```json
{
  "RateBasedStatement": {
    "Limit": 2000,
    "AggregateKeyType": "IP"
  }
}
```

**WAF vs Shield**:
- **WAF**: Application-level (Layer 7) filtering, custom rules
- **Shield Standard**: Network/transport (Layer 3/4) DDoS protection, automatic, free
- **Shield Advanced**: Enhanced DDoS protection, cost protection, 24/7 support

**Common WAF Rules**:
1. Block SQL injection attempts
2. Block XSS attacks
3. Rate limiting (prevent abuse)
4. Geographic restrictions
5. IP blacklist/whitelist
6. String/pattern matching

**References:** AWS WAF, Web Application Security, OWASP Protection
</details>

---

### Question 10
A company wants to protect their application from DDoS attacks and ensure cost protection during large-scale attacks. Which service provides these features?

A. AWS WAF  
B. AWS Shield Standard  
C. AWS Shield Advanced  
D. Security Groups  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Shield Advanced** provides enhanced DDoS protection with cost protection
- 24/7 access to DDoS Response Team (DRT)
- Advanced attack detection and mitigation
- Cost protection against scaling charges during attacks

**Shield Comparison**:

| Feature | Shield Standard | Shield Advanced |
|---------|----------------|-----------------|
| **Cost** | Free | $3,000/month |
| **Protection Level** | Network/Transport (L3/L4) | Network + Application (L3/L4/L7) |
| **DDoS Response Team** | No | 24/7 access |
| **Cost Protection** | No | Yes (scaling charges) |
| **Advanced Detection** | Basic | Enhanced, real-time |
| **Health-based Detection** | No | Yes |
| **Application Layer** | Via WAF | Included + WAF |

**Shield Advanced Features**:

**1. Cost Protection**:
- Protects against scaling charges during DDoS attacks
- Covers: EC2, ELB, CloudFront, Route 53, Global Accelerator

**2. DDoS Response Team (DRT)**:
- 24/7 expert support
- Attack analysis and mitigation
- Custom mitigation rules

**3. Advanced Metrics**:
- Real-time attack visibility
- Historical attack data
- Integration with CloudWatch

**4. Protection Scope**:
- CloudFront distributions
- Route 53 hosted zones
- Global Accelerator accelerators
- Elastic Load Balancers
- EC2 Elastic IP addresses

**5. Health-Based Detection**:
- Monitors application health
- Proactive mitigation
- Route 53 health checks integration

**When to Use Shield Advanced**:
- Business-critical applications
- High-profile websites
- Cannot tolerate downtime
- Need cost protection
- Want expert DRT support

**Best Practice Architecture**:
```
Users → CloudFront (Shield Advanced) → 
  ALB (Shield Advanced + WAF) → 
    EC2 instances (Auto Scaling)
```

**References:** AWS Shield Advanced, DDoS Protection, Cost Protection
</details>

---

### Question 11
A company needs to scan EC2 instances and container images for software vulnerabilities. Which service should be used?

A. Amazon GuardDuty  
B. Amazon Inspector  
C. AWS Security Hub  
D. Amazon Macie  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon Inspector** provides automated vulnerability assessment
- Scans EC2 instances, container images (ECR), Lambda functions
- Network reachability analysis
- Package vulnerability detection (CVEs)

**Amazon Inspector v2 Features**:

**1. Continuous Scanning**:
- Automated, continuous assessment
- No agents needed for ECR
- SSM agent for EC2 (automatic deployment)

**2. Vulnerability Detection**:
- **CVE (Common Vulnerabilities and Exposures)**
- OS packages
- Application dependencies
- Network exposure

**3. Resource Types**:
- **EC2 Instances**: OS and application vulnerabilities
- **ECR Container Images**: Image vulnerabilities
- **Lambda Functions**: Code and package vulnerabilities

**4. Risk Scoring**:
- Inspector score (0-10)
- Severity: Critical, High, Medium, Low, Informational
- Prioritization based on exploitability and CVSS

**5. Integration**:
- Security Hub (centralized findings)
- EventBridge (automated remediation)
- AWS Organizations (multi-account)

**Inspector Finding Example**:
```json
{
  "FindingType": "PACKAGE_VULNERABILITY",
  "Severity": "HIGH",
  "Title": "CVE-2021-44228 - Apache Log4j",
  "Description": "Remote code execution vulnerability",
  "Recommendation": "Update to version 2.17.0 or later",
  "AffectedResources": ["i-1234567890abcdef0"]
}
```

**Inspector vs Other Services**:
- **Inspector**: Vulnerability scanning (EC2, ECR, Lambda)
- **GuardDuty**: Threat detection (malicious activity)
- **Macie**: Data protection (PII in S3)
- **Config**: Configuration compliance

**Automated Remediation**:
```
Inspector Finding → EventBridge → Lambda → 
  - Patch instance (SSM Patch Manager)
  - Update image
  - Create ticket
```

**References:** Amazon Inspector, Vulnerability Assessment, CVE Detection
</details>

---

### Question 12
A company wants to enforce that all new EC2 instances must have encrypted EBS volumes. How can this be enforced across the organization?

A. AWS Config rule with manual remediation  
B. Service Control Policy (SCP) in AWS Organizations  
C. IAM policy on each user  
D. AWS Lambda function to check instances  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Service Control Policies (SCPs)** provide centralized, preventive controls
- Applied at organization, OU, or account level
- Cannot be overridden by anyone in member accounts
- Maximum permission boundaries

**SCP Example - Enforce Encrypted EBS**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyUnencryptedEBSVolumes",
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances",
        "ec2:CreateVolume"
      ],
      "Resource": "arn:aws:ec2:*:*:volume/*",
      "Condition": {
        "Bool": {
          "ec2:Encrypted": "false"
        }
      }
    }
  ]
}
```

**SCPs vs Other Controls**:

| Method | Prevention | Detection | Scope | Override |
|--------|-----------|-----------|-------|----------|
| **SCP** | Yes | No | Organization/OU/Account | Cannot override |
| **IAM Policy** | Yes | No | User/Role/Group | Admin can change |
| **Config Rule** | No | Yes | Account | Detection only |
| **Lambda** | Possible | Yes | Custom | Complex |

**SCP Best Practices**:

**1. Preventive Controls**:
- Deny unencrypted resources
- Deny public S3 buckets
- Restrict regions
- Prevent root user actions

**2. Example - Region Restriction**:
```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": ["us-east-1", "us-west-2"]
    }
  }
}
```

**3. Example - Deny Public S3**:
```json
{
  "Effect": "Deny",
  "Action": [
    "s3:PutBucketPublicAccessBlock"
  ],
  "Resource": "*",
  "Condition": {
    "Bool": {
      "s3:BlockPublicAcls": "false"
    }
  }
}
```

**SCP Evaluation Logic**:
1. Explicit Deny in SCP → DENY
2. SCP allows + IAM allows → ALLOW
3. Default → DENY

**Multi-Layer Security**:
- **SCP**: Preventive (organization-wide)
- **Config**: Detective (compliance monitoring)
- **Automated Remediation**: Corrective (fix non-compliant)

**References:** AWS Organizations SCPs, Preventive Controls, Multi-Account Governance
</details>

---

### Question 13
A company needs to ensure S3 objects cannot be deleted for 7 years and even the root account cannot override this. Which feature should be configured?

A. S3 Versioning with Lifecycle policies  
B. S3 Object Lock in Compliance Mode  
C. S3 Object Lock in Governance Mode  
D. MFA Delete  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **S3 Object Lock in Compliance Mode** enforces WORM (Write Once Read Many)
- Cannot be overridden by anyone, including root account
- Retention period cannot be shortened
- Object versions cannot be deleted during retention period

**Object Lock Modes**:

| Feature | Governance Mode | Compliance Mode |
|---------|----------------|-----------------|
| **Override** | Yes (with special permission) | No (even root cannot) |
| **Delete** | Can be deleted with permission | Cannot be deleted |
| **Retention Change** | Can shorten with permission | Cannot shorten |
| **Use Case** | Internal governance | Regulatory compliance |

**Object Lock Components**:

**1. Retention Modes**:
- **Compliance**: Immutable, regulatory compliance
- **Governance**: Flexible, internal policies

**2. Retention Period**:
- Fixed period (days/years)
- Protect-until date

**3. Legal Hold**:
- Indefinite protection
- On/off toggle
- Independent of retention period
- Requires `s3:PutObjectLegalHold` permission

**Configuration Requirements**:
1. **Versioning must be enabled** (object lock requires versioning)
2. **Object Lock enabled at bucket creation** (cannot enable later)
3. **Default retention settings** (optional, can be per-object)

**Compliance Mode Example**:
```json
{
  "ObjectLockConfiguration": {
    "ObjectLockEnabled": "Enabled",
    "Rule": {
      "DefaultRetention": {
        "Mode": "COMPLIANCE",
        "Years": 7
      }
    }
  }
}
```

**Legal Hold Example**:
```bash
aws s3api put-object-legal-hold \
  --bucket my-bucket \
  --key document.pdf \
  --legal-hold Status=ON
```

**Compliance Use Cases**:
- SEC Rule 17a-4 (financial services)
- HIPAA (healthcare)
- FINRA (financial industry)
- Legal documents
- Regulatory archives

**Object Lock vs Other Protection**:
- **Versioning**: Can delete versions
- **MFA Delete**: Adds MFA but can still delete
- **Object Lock Governance**: Can override with permissions
- **Object Lock Compliance**: True immutability

**References:** S3 Object Lock, WORM Compliance, Regulatory Requirements
</details>

---

### Question 14
A company wants to provide temporary, limited-privilege access to third-party vendors to perform specific tasks in their AWS account. What is the BEST approach?

A. Create IAM users with passwords  
B. Share root account credentials temporarily  
C. Create cross-account IAM roles with external ID  
D. Create access keys and share them  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Cross-account IAM roles with External ID** provide secure temporary access
- No long-term credentials needed
- External ID prevents confused deputy problem
- Fine-grained permissions with session duration limits

**Cross-Account Access Architecture**:

**1. Trust Policy** (in your account):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::VENDOR-ACCOUNT:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "UniqueExternalId12345"
        }
      }
    }
  ]
}
```

**2. Permissions Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ]
    }
  ]
}
```

**External ID - Confused Deputy Prevention**:

**The Problem**:
- Vendor uses same role name for all customers
- Attacker could trick vendor into accessing your resources

**The Solution**:
- Unique External ID per customer
- Vendor must provide correct External ID to assume role
- Prevents unauthorized access

**Implementation Steps**:

**Your Account**:
1. Create IAM role for vendor
2. Set trust policy with vendor's account ID
3. Add External ID condition (vendor provides this)
4. Attach permissions policy (least privilege)
5. Configure session duration (1-12 hours)

**Vendor Account**:
1. Configure to assume role
2. Provide External ID when assuming
3. Receive temporary credentials
4. Credentials auto-expire after session duration

**AssumeRole Example** (vendor side):
```bash
aws sts assume-role \
  --role-arn arn:aws:iam::YOUR-ACCOUNT:role/VendorRole \
  --role-session-name vendor-session \
  --external-id UniqueExternalId12345 \
  --duration-seconds 3600
```

**Benefits**:
- ✅ No long-term credentials
- ✅ Automatic credential rotation
- ✅ Auditable (CloudTrail)
- ✅ Time-limited access
- ✅ Revocable (delete role)
- ✅ Prevents confused deputy

**Best Practices**:
1. Always use External ID
2. Principle of least privilege
3. Short session durations (1-2 hours)
4. Monitor with CloudTrail
5. Review permissions regularly
6. Use MFA for sensitive roles

**References:** Cross-Account Access, External ID, Confused Deputy Problem, IAM Roles
</details>

---

### Question 15
A company needs to rotate SSL/TLS certificates for their application load balancers automatically. Which service should they use?

A. AWS Certificate Manager (ACM)  
B. AWS Secrets Manager  
C. AWS KMS  
D. IAM Server Certificates  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- **AWS Certificate Manager (ACM)** provides free SSL/TLS certificates
- Automatic renewal (no manual intervention)
- Automatic deployment to integrated services
- Free for public certificates

**ACM Features**:

**1. Automatic Renewal**:
- ACM automatically renews certificates before expiration
- No downtime during renewal
- Deploys renewed certificate automatically

**2. Supported Services**:
- Elastic Load Balancing (ALB, NLB, CLB)
- Amazon CloudFront
- Amazon API Gateway
- AWS App Runner
- AWS Elastic Beanstalk

**3. Certificate Types**:
- **Public Certificates**: Free, validated via DNS or email
- **Private Certificates**: Paid, via AWS Private CA

**4. Validation Methods**:
- **DNS Validation**: Add CNAME record (recommended)
- **Email Validation**: Email to domain contacts

**ACM vs IAM Certificates**:

| Feature | ACM | IAM Server Certificates |
|---------|-----|-------------------------|
| **Cost** | Free | Manual management |
| **Renewal** | Automatic | Manual |
| **Regions** | Regional (us-east-1 for CloudFront) | Global |
| **Integration** | Native AWS services | Limited |
| **Management** | AWS managed | Self-managed |

**ACM Certificate Request**:
```bash
aws acm request-certificate \
  --domain-name example.com \
  --subject-alternative-names *.example.com \
  --validation-method DNS
```

**DNS Validation (Route 53)**:
```bash
# ACM provides CNAME record
# Add to Route 53:
Name: _abc123.example.com
Type: CNAME
Value: _xyz789.acm-validations.aws
```

**CloudFront Requirement**:
- Certificate must be in **us-east-1** region
- Must be public certificate
- Can use wildcard (*.example.com)

**Certificate Monitoring**:
- CloudWatch metrics for expiration
- EventBridge events for renewal status
- AWS Health Dashboard notifications

**Best Practices**:
1. Use DNS validation (faster, automatic)
2. Use ACM for all supported services
3. Monitor certificate expiration (backup)
4. Use wildcard for subdomains
5. Enable automatic renewal

**References:** AWS Certificate Manager, SSL/TLS Certificates, Automatic Renewal
</details>

---

### Question 16
A company wants to centrally manage firewall rules across multiple AWS accounts and VPCs. Which service should be used?

A. Security Groups  
B. Network ACLs  
C. AWS Firewall Manager  
D. AWS WAF  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **AWS Firewall Manager** centrally configures and manages firewall rules
- Works across accounts and resources in AWS Organizations
- Ensures consistent security policies
- Automatic policy application to new resources

**Firewall Manager Capabilities**:

**1. Supported Policies**:
- AWS WAF rules (ALB, CloudFront, API Gateway)
- AWS Shield Advanced protections
- VPC Security Groups
- AWS Network Firewall rules
- Route 53 Resolver DNS Firewall
- Third-party firewall appliances

**2. Policy Types**:

| Policy Type | Scope | Use Case |
|-------------|-------|----------|
| **WAF Policy** | CloudFront, ALB, API Gateway | Web application protection |
| **Shield Advanced** | CloudFront, ALB, EIP | DDoS protection |
| **Security Group** | EC2, ENI | VPC-level firewall |
| **Network Firewall** | VPC | Stateful firewall |
| **DNS Firewall** | VPC | DNS query filtering |

**3. Policy Application**:
- Automatically applied to all accounts in organization
- Applied to new resources automatically
- Centralized compliance monitoring

**Firewall Manager Example Use Case**:

**Scenario**: Enforce WAF rules across all ALBs in organization

**Configuration**:
```json
{
  "Policy": {
    "PolicyName": "EnforceWAFOnAllALBs",
    "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "IncludeMap": {
      "ACCOUNT": ["*"]  // All accounts
    },
    "RemediationEnabled": true,
    "SecurityServicePolicyData": {
      "Type": "WAF",
      "ManagedServiceData": {
        "RuleGroups": ["AWSManagedRulesCommonRuleSet"]
      }
    }
  }
}
```

**Benefits**:
1. **Centralized Management**: Single console for all accounts
2. **Automatic Compliance**: Policies auto-applied
3. **Consistent Security**: Same rules everywhere
4. **Reduced Overhead**: No manual configuration per account
5. **Visibility**: Compliance dashboard

**Firewall Manager vs Manual Management**:

| Aspect | Firewall Manager | Manual |
|--------|-----------------|--------|
| **Setup** | Once (centralized) | Per account/resource |
| **New Resources** | Automatic | Manual |
| **Compliance** | Monitored | Manual checks |
| **Updates** | Centralized | Per account |
| **Accounts** | Multi-account | Single account |

**Common Policies**:

**1. Common WAF Rules**:
- SQL injection protection
- XSS protection
- Rate limiting

**2. Security Group Rules**:
- Restrict SSH (port 22) to corporate IPs
- Deny all unauthorized outbound traffic

**3. DNS Firewall**:
- Block known malicious domains
- Data exfiltration prevention

**Prerequisites**:
- AWS Organizations enabled
- Firewall Manager administrator account
- AWS Config enabled in all accounts
- AWS Config Service-Linked Role

**References:** AWS Firewall Manager, Centralized Security Management, Multi-Account Firewall
</details>

---

### Question 17
A developer accidentally commits AWS credentials to a public GitHub repository. What immediate actions should be taken? (Choose THREE)

A. Change the IAM user's password  
B. Deactivate and delete the exposed access keys immediately  
C. Review CloudTrail logs for unauthorized activity  
D. Enable MFA on the account  
E. Create new access keys before deleting old ones  
F. Check AWS Personal Health Dashboard  

<details>
<summary>Show Answer</summary>

**Answer: B, C, E**

**Explanation:**

**Immediate Response Steps**:

**1. Deactivate/Delete Exposed Credentials (B)**:
- **FIRST**: Deactivate keys immediately
- **SECOND**: Review activity
- **THIRD**: Delete keys after creating new ones

```bash
# Deactivate immediately
aws iam update-access-key \
  --access-key-id AKIAIOSFODNN7EXAMPLE \
  --status Inactive \
  --user-name compromised-user

# After review, delete
aws iam delete-access-key \
  --access-key-id AKIAIOSFODNN7EXAMPLE \
  --user-name compromised-user
```

**2. Review CloudTrail Logs (C)**:
- Check for unauthorized API calls
- Identify scope of compromise
- Document affected resources

```bash
# Check recent activity
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIA... \
  --max-items 50
```

**3. Create New Credentials Before Deleting (E)**:
- Ensure application continuity
- Update applications with new keys
- Then delete compromised keys

**Complete Incident Response Checklist**:

**Immediate (Minutes)**:
- [ ] Deactivate exposed credentials
- [ ] Alert security team
- [ ] Check GuardDuty for findings

**Short-term (Hours)**:
- [ ] Review CloudTrail logs (7-90 days)
- [ ] Identify unauthorized actions
- [ ] Assess damage (new resources, data access)
- [ ] Create new credentials
- [ ] Update applications
- [ ] Delete old credentials
- [ ] Revoke temporary credentials (if role assumed)

**Medium-term (Days)**:
- [ ] Review IAM policies (reduce permissions)
- [ ] Enable MFA (not immediate priority but important)
- [ ] Implement AWS Secrets Manager
- [ ] Set up CloudWatch alarms for unusual activity
- [ ] Review security groups, NACLs
- [ ] Check for backdoors (IAM users, roles)

**Long-term (Weeks)**:
- [ ] Implement AWS SSO
- [ ] Enforce MFA organization-wide
- [ ] Use IAM roles instead of access keys
- [ ] Implement secrets rotation
- [ ] Security training
- [ ] Code repository scanning (git-secrets)
- [ ] Implement preventive controls

**CloudTrail Investigation Queries**:
```sql
-- Find all actions by compromised key
SELECT eventTime, eventName, awsRegion, sourceIPAddress, userAgent
FROM cloudtrail_logs
WHERE userIdentity.accessKeyId = 'AKIA...'
ORDER BY eventTime DESC

-- Look for suspicious patterns
-- - CreateUser, CreateAccessKey (persistence)
-- - RunInstances (cryptocurrency mining)
-- - PutBucketPolicy (data exfiltration)
-- - CreateRole, AttachRolePolicy (privilege escalation)
```

**GuardDuty Findings to Check**:
- UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration
- Persistence:IAMUser/UserPermissions
- PrivilegeEscalation:IAMUser/AdministrativePermissions
- Impact:IAMUser/MaliciousIPCaller

**Why Other Options are Wrong**:
- **A (Password)**: Access keys and passwords are separate
- **D (MFA)**: Important but not immediate priority
- **F (PHD)**: Doesn't relate to credential exposure

**Prevention Strategies**:
1. **Never commit credentials** to version control
2. Use **IAM roles** for applications
3. Implement **AWS Secrets Manager** or **Parameter Store**
4. Use **git-secrets** or **git-hound** to scan repositories
5. Enable **AWS GuardDuty** for detection
6. Rotate credentials regularly
7. Use **short-lived credentials** (STS)
8. Implement **AWS SSO** for users

**References:** Incident Response, Credential Exposure, CloudTrail Analysis, Security Best Practices
</details>

---

### Question 18
A company wants to ensure data encryption in transit between their on-premises data center and AWS. Which connectivity option provides encryption by default?

A. AWS Direct Connect  
B. AWS Site-to-Site VPN  
C. Internet Gateway  
D. AWS PrivateLink  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Site-to-Site VPN** uses IPsec to encrypt data in transit
- Encryption is built-in and automatic
- No additional configuration needed for encryption

**Connectivity Options Comparison**:

| Option | Encryption | Speed | Setup | Cost |
|--------|-----------|-------|-------|------|
| **Site-to-Site VPN** | Yes (IPsec) | Up to 1.25 Gbps | Minutes | Low |
| **Direct Connect** | No (but can add) | 1-100 Gbps | Weeks | High |
| **DX + VPN** | Yes | 1-100 Gbps | Weeks | High |
| **Internet** | HTTPS only | Variable | Immediate | Very low |

**Site-to-Site VPN Features**:

**1. Encryption**:
- IPsec tunnel
- AES-256-GCM or AES-128-GCM encryption
- SHA-2 hashing
- DH (Diffie-Hellman) groups

**2. Redundancy**:
- AWS provides 2 VPN tunnels per connection
- Active/passive or active/active
- Multi-AZ availability

**3. Dynamic Routing**:
- BGP support
- Automatic failover
- Route propagation

**VPN Configuration**:
```json
{
  "VPNConnection": {
    "IKEVersions": ["ikev2"],
    "Phase1EncryptionAlgorithms": ["AES256-GCM-16"],
    "Phase1IntegrityAlgorithms": ["SHA2-256"],
    "Phase1DHGroupNumbers": [14],
    "Phase2EncryptionAlgorithms": ["AES256-GCM-16"],
    "Phase2IntegrityAlgorithms": ["SHA2-256"]
  }
}
```

**Direct Connect Encryption**:

**Option 1: DX + Public VIF + VPN**:
- VPN over Direct Connect
- Encrypted but complex

**Option 2: DX + VPN (Separate)**:
- Direct Connect for primary (unencrypted)
- VPN for backup (encrypted)

**Option 3: MACsec** (Direct Connect):
- Layer 2 encryption
- 10 Gbps and 100 Gbps connections only
- Not available for all locations

**When to Choose**:

**Site-to-Site VPN**:
- Need immediate encryption
- Budget-conscious
- Bandwidth < 1 Gbps adequate
- Quick setup required

**Direct Connect**:
- Large data transfers
- Consistent performance needed
- Can add VPN for encryption
- Long-term investment

**Best Practice - Hybrid**:
- Primary: Direct Connect (performance)
- Backup: VPN (encrypted, failover)
- Provides both performance and encryption

**References:** Site-to-Site VPN, Direct Connect, Encryption in Transit, Hybrid Connectivity
</details>

---

### Question 19
A company wants to ensure EC2 instances can only launch in approved VPCs and subnets. How can this be enforced at the organization level?

A. IAM policy condition checking VPC ID  
B. Service Control Policy (SCP) with VPC condition  
C. AWS Config rule  
D. Security Group rules  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Service Control Policy (SCP)** provides organization-wide preventive control
- Can restrict actions based on VPC/subnet
- Cannot be bypassed by member accounts
- Enforced before IAM policies

**SCP Example - Restrict to Approved VPCs**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RequireApprovedVPC",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:subnet/*",
      "Condition": {
        "StringNotEquals": {
          "ec2:Vpc": [
            "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-approved1",
            "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-approved2"
          ]
        }
      }
    }
  ]
}
```

**SCP Example - Restrict to Approved Subnets**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RequireApprovedSubnets",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:subnet/*",
      "Condition": {
        "StringNotLike": {
          "ec2:Subnet": [
            "arn:aws:ec2:*:*:subnet/subnet-12345678",
            "arn:aws:ec2:*:*:subnet/subnet-87654321"
          ]
        }
      }
    }
  ]
}
```

**Useful EC2 Condition Keys**:

| Condition Key | Use Case |
|---------------|----------|
| `ec2:Vpc` | Restrict to specific VPCs |
| `ec2:Subnet` | Restrict to specific subnets |
| `ec2:InstanceType` | Limit instance types |
| `ec2:Region` | Region restrictions |
| `ec2:Tenancy` | Dedicated vs default |
| `ec2:RootDeviceType` | EBS vs instance store |

**Multi-Layer Enforcement**:

**Layer 1 - SCP (Preventive)**:
```json
// Organization-wide restriction
{
  "Effect": "Deny",
  "Action": "ec2:RunInstances",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "ec2:Vpc": "arn:aws:ec2:*:*:vpc/vpc-approved*"
    }
  }
}
```

**Layer 2 - IAM Policy (Preventive)**:
```json
// Account-level additional restrictions
{
  "Effect": "Allow",
  "Action": "ec2:RunInstances",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "ec2:Subnet": [
        "arn:aws:ec2:*:*:subnet/subnet-prod1",
        "arn:aws:ec2:*:*:subnet/subnet-prod2"
      ]
    }
  }
}
```

**Layer 3 - Config (Detective)**:
```json
// Detect non-compliant instances
{
  "ConfigRuleName": "instances-in-approved-subnets",
  "Source": {
    "Owner": "CUSTOM_LAMBDA",
    "SourceIdentifier": "arn:aws:lambda:..."
  }
}
```

**Why SCP is Best**:
1. **Organization-wide**: Applies to all accounts
2. **Preventive**: Blocks before creation
3. **Cannot override**: Even admins cannot bypass
4. **Centralized**: Managed from master account
5. **Inherited**: Applied to OUs and child accounts

**Comparison**:
- **SCP**: Preventive, organization-wide, cannot override
- **IAM**: Preventive, account-level, admins can change
- **Config**: Detective, alerts after creation
- **Security Groups**: Network-level, not launch control

**References:** Service Control Policies, VPC Restrictions, EC2 Launch Controls
</details>

---

### Question 20
A company needs to monitor and respond to unusual API activity patterns that might indicate compromised credentials. Which service combination is MOST effective?

A. CloudTrail + CloudWatch Logs  
B. GuardDuty + EventBridge + Lambda  
C. Config + SNS  
D. Inspector + Security Hub  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **GuardDuty** uses ML to detect unusual API activity automatically
- **EventBridge** routes findings to automated response
- **Lambda** executes remediation actions
- Fully automated threat detection and response

**Automated Threat Response Architecture**:

```
CloudTrail Events (API calls)
      ↓
GuardDuty (ML-based analysis)
      ↓
Finding: UnauthorizedAccess:IAMUser/MaliciousIPCaller
      ↓
EventBridge Rule
      ↓
Lambda Function
      ↓
Automated Response:
  - Isolate instance
  - Disable credentials
  - Create snapshot
  - Send SNS notification
  - Create support ticket
```

**GuardDuty Finding Example**:
```json
{
  "schemaVersion": "2.0",
  "accountId": "123456789012",
  "region": "us-east-1",
  "partition": "aws",
  "id": "finding-id",
  "arn": "arn:aws:guardduty:...",
  "type": "UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom",
  "service": {
    "serviceName": "guardduty",
    "detectorId": "detector-id",
    "action": {
      "actionType": "AWS_API_CALL",
      "awsApiCallAction": {
        "api": "RunInstances",
        "serviceName": "ec2.amazonaws.com",
        "callerType": "Remote IP",
        "remoteIpDetails": {
          "ipAddressV4": "198.51.100.0",
          "organization": {
            "isp": "Malicious ISP"
          },
          "geoLocation": {
            "lat": 39.0,
            "lon": -77.0
          }
        }
      }
    }
  },
  "severity": 8,
  "title": "API call originated from a known malicious IP address",
  "description": "API RunInstances was invoked from a known malicious IP address"
}
```

**EventBridge Rule** (routes GuardDuty findings):
```json
{
  "source": ["aws.guardduty"],
  "detail-type": ["GuardDuty Finding"],
  "detail": {
    "severity": [7, 8, 9],  // High and Critical only
    "type": [
      "UnauthorizedAccess:IAMUser/MaliciousIPCaller",
      "UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration",
      "PrivilegeEscalation:IAMUser/AdministrativePermissions"
    ]
  }
}
```

**Lambda Response Function** (Python example):
```python
import boto3

def lambda_handler(event, context):
    finding = event['detail']
    finding_type = finding['type']
    severity = finding['severity']
    
    iam = boto3.client('iam')
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    
    # Extract compromised credentials
    if 'resource' in finding:
        resource = finding['resource']
        
        # If IAM user compromised
        if resource['resourceType'] == 'AccessKey':
            access_key_id = resource['accessKeyDetails']['accessKeyId']
            user_name = resource['accessKeyDetails']['userName']
            
            # Disable access key
            iam.update_access_key(
                UserName=user_name,
                AccessKeyId=access_key_id,
                Status='Inactive'
            )
            
            # Attach deny-all policy
            iam.attach_user_policy(
                UserName=user_name,
                PolicyArn='arn:aws:iam::aws:policy/AWSDenyAll'
            )
            
        # If EC2 instance compromised
        elif resource['resourceType'] == 'Instance':
            instance_id = resource['instanceDetails']['instanceId']
            
            # Create snapshot for forensics
            volumes = ec2.describe_volumes(
                Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}]
            )
            for volume in volumes['Volumes']:
                ec2.create_snapshot(
                    VolumeId=volume['VolumeId'],
                    Description=f'Forensic snapshot - GuardDuty finding {finding["id"]}'
                )
            
            # Isolate instance (change to quarantine SG)
            ec2.modify_instance_attribute(
                InstanceId=instance_id,
                Groups=['sg-quarantine']  # Denies all traffic
            )
            
            # Optionally stop instance
            ec2.stop_instances(InstanceIds=[instance_id])
    
    # Send notification
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:security-alerts',
        Subject=f'GuardDuty Finding: {finding_type}',
        Message=f"""
        Severity: {severity}
        Type: {finding_type}
        Description: {finding['description']}
        
        Automated actions taken:
        - Credentials disabled
        - Instance isolated
        - Forensic snapshots created
        - Security team notified
        """
    )
    
    return {
        'statusCode': 200,
        'body': 'Automated response completed'
    }
```

**Common GuardDuty Finding Types for API Activity**:

| Finding Type | Description | Response |
|--------------|-------------|----------|
| **UnauthorizedAccess:IAMUser/MaliciousIPCaller** | API calls from malicious IP | Disable credentials |
| **UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration** | Credentials used outside AWS | Rotate credentials |
| **PrivilegeEscalation:IAMUser/AdministrativePermissions** | User gained admin permissions | Revoke permissions |
| **Persistence:IAMUser/UserPermissions** | User created new access keys | Review and delete |
| **Impact:IAMUser/AnomalousBehavior** | Unusual API activity | Investigate |

**Complete Response Playbook**:

**Detection** (GuardDuty):
- Continuous monitoring
- ML-based anomaly detection
- Threat intelligence feeds

**Routing** (EventBridge):
- Filter by severity
- Route to appropriate response

**Response** (Lambda):
- Disable credentials
- Isolate resources
- Create forensic snapshots
- Alert security team
- Create incident ticket

**Investigation** (Manual):
- Review CloudTrail logs
- Analyze scope of compromise
- Identify affected resources
- Root cause analysis

**Remediation** (Manual/Automated):
- Rotate credentials
- Update IAM policies
- Remove backdoors
- Apply security patches
- Update security groups

**Prevention** (Long-term):
- Implement MFA
- Use IAM roles
- Enforce least privilege
- Regular access reviews
- Security training

**Why This Combination is Best**:
1. **GuardDuty**: Intelligent detection (no manual rules)
2. **EventBridge**: Flexible routing
3. **Lambda**: Automated response (immediate action)
4. **Scalable**: No infrastructure
5. **Comprehensive**: Covers all AWS API activity

**Alternative (Manual)**:
- CloudTrail → CloudWatch Logs → Metric Filters → Alarms → SNS
- Requires manual pattern definition
- Less intelligent
- Manual response

**References:** GuardDuty, Automated Incident Response, EventBridge, Security Automation
</details>

---

## Summary

**Total Questions**: 20  
**Topics Covered**:
- AWS KMS (SSE-S3, SSE-KMS, CMK, Key Rotation)
- AWS Secrets Manager (Automatic Rotation)
- AWS CloudTrail (API Logging, Compliance)
- Amazon GuardDuty (Threat Detection)
- AWS Config (Compliance Monitoring)
- AWS Security Hub (Centralized Findings)
- Amazon Macie (PII Detection)
- IAM Access Analyzer (External Access, Policy Validation)
- AWS WAF (Web Application Firewall)
- AWS Shield (DDoS Protection)
- Amazon Inspector (Vulnerability Scanning)
- Service Control Policies (SCPs)
- S3 Object Lock (WORM Compliance)
- Cross-Account Access (External ID)
- AWS Certificate Manager (SSL/TLS)
- AWS Firewall Manager (Centralized Firewall Management)
- Incident Response (Credential Exposure)
- Site-to-Site VPN (Encryption in Transit)
- Automated Threat Response

**Exam Tips**:

**Encryption**:
- **SSE-S3**: AWS manages, simple, free
- **SSE-KMS (CMK)**: Full control, rotation, audit trail
- **SSE-C**: Customer provides keys
- **Object Lock Compliance**: Immutable, regulatory

**Secrets Management**:
- **Secrets Manager**: Automatic rotation, DB integration
- **Parameter Store**: Configuration, no auto-rotation

**Logging & Monitoring**:
- **CloudTrail**: WHO did WHAT and WHEN
- **Config**: WHAT changed and compliance
- **GuardDuty**: THREATS (malicious activity)

**Threat Detection**:
- **GuardDuty**: Intelligent threat detection
- **Inspector**: Vulnerability scanning
- **Macie**: PII/sensitive data in S3
- **Access Analyzer**: External access, policy validation

**DDoS Protection**:
- **Shield Standard**: Free, automatic, L3/L4
- **Shield Advanced**: Paid, DRT, cost protection
- **WAF**: Application-level filtering

**Compliance**:
- **Config**: Continuous compliance monitoring
- **Security Hub**: Centralized findings
- **SCPs**: Preventive controls

**Multi-Account Security**:
- **Organizations + SCPs**: Preventive controls
- **Security Hub**: Centralized findings
- **Firewall Manager**: Centralized firewall rules
- **GuardDuty**: Multi-account threat detection

**Cross-Account Access**:
- Use IAM roles with External ID
- Never share credentials
- Time-limited sessions

**Incident Response**:
1. Disable credentials immediately
2. Review CloudTrail
3. Assess damage
4. Remediate
5. Implement prevention

**Best Practices**:
1. Enable MFA everywhere
2. Use IAM roles instead of access keys
3. Implement least privilege
4. Enable CloudTrail in all regions
5. Use AWS Security Hub for central view
6. Automate threat response
7. Regular security audits
8. Encrypt everything (at rest and in transit)

**Next Steps**:
- Understand when to use each security service
- Practice writing SCPs and IAM policies
- Learn incident response procedures
- Review AWS security best practices
- Practice automated response patterns

