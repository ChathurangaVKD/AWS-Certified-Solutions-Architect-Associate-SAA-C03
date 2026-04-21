# Security & Compliance - Mermaid Diagrams

## AWS KMS (Key Management Service)

### KMS Architecture

```mermaid
graph TB
    subgraph KMS_Service_Group["KMS Service"]
        CMK["Customer Master Key<br/>Never leaves KMS<br/>FIPS 140-2 Level 2"]
        
        Symmetric["Symmetric CMK<br/>AES-256<br/>Same key encrypt/decrypt"]
        Asymmetric["Asymmetric CMK<br/>RSA or ECC<br/>Public + Private keys"]
        
        CMK --> Symmetric
        CMK --> Asymmetric
    end
    
    subgraph Key_Types_Group["Key Types"]
        AWSManaged["AWS Managed Keys<br/>aws/service-name<br/>Free, Auto-rotate yearly"]
        CustomerManaged["Customer Managed Keys<br/>$1/month<br/>Optional rotation"]
        AWSOwned["AWS Owned Keys<br/>Shared across accounts<br/>Free, Not visible"]
    end
    
    subgraph Applications_Group["Applications"]
        App[Application]
        S3[S3]
        EBS[EBS]
        RDS[RDS]
    end
    
    App -->|API Call| Symmetric
    S3 --> AWSManaged
    EBS --> CustomerManaged
    RDS --> CustomerManaged
    
    CloudTrail["CloudTrail<br/>Audit all key usage"] -.Logs.-> CMK
    
    classDef style1 fill:#FF9900
    class CMK style1
    classDef style2 fill:#569A31
    class Symmetric style2
```

### KMS Envelope Encryption

```mermaid
sequenceDiagram
    participant App as Application
    participant KMS as AWS KMS
    participant S3 as Amazon S3
    
    Note over App,S3: Encrypt Large File (&gt; 4 KB(
    
    App->>KMS: GenerateDataKey(CMK(
    KMS->>KMS: Generate Data Key
    KMS->>App: Return Plaintext Data Key + Encrypted Data Key
    
    App->>App: Encrypt file with Plaintext Data Key
    App->>App: Delete Plaintext Data Key from memory
    App->>S3: Upload Encrypted File + Encrypted Data Key
    
    Note over App,S3: Decrypt File
    
    S3->>App: Download Encrypted File + Encrypted Data Key
    App->>KMS: Decrypt(Encrypted Data Key(
    KMS->>App: Return Plaintext Data Key
    App->>App: Decrypt file with Plaintext Data Key
    App->>App: Delete Plaintext Data Key from memory
    
    Note over App,S3: Benefits: Encrypt unlimited data size, Network overhead only for small Data Key
    
```

### KMS Key Policies

```mermaid
graph TB
    Request[API Request to use KMS Key]
    
    Request --> KeyPolicy{"Key Policy<br/>Allows?"}
    
    KeyPolicy -->|No| Deny1["❌ DENY"]
    KeyPolicy -->|Yes| IAMPolicy{"IAM Policy<br/>Allows?"}
    
    IAMPolicy -->|No| Deny2["❌ DENY"]
    IAMPolicy -->|Yes| Grant{"Grant<br/>Allows?"}
    
    Grant -->|Not Required| Allow["✅ ALLOW"]
    Grant -->|Yes| Allow
    Grant -->|No| Deny3["❌ DENY"]
    
    DefaultPolicy["Default Key Policy:<br/>Gives root user full access<br/>Enables IAM policies"]
    
    CustomPolicy["Custom Key Policy:<br/>Specific users/roles<br/>Cross-account access<br/>Key administrators<br/>Key users"]
    
    KeyPolicy -.Can be.-> DefaultPolicy
    KeyPolicy -.Can be.-> CustomPolicy
    
    classDef style1 fill:#569A31
    class Allow style1
    classDef style2 fill:#C00
    class Deny1 style2
    classDef style3 fill:#C00
    class Deny2 style3
    classDef style4 fill:#C00
    class Deny3 style4
    classDef style5 fill:#FF9900
    class KeyPolicy style5
```

## CloudHSM

### CloudHSM vs KMS

```mermaid
graph TB
    subgraph AWS_KMS_Group["AWS KMS"]
        KMS[KMS]
        KMS_Features["• Multi-tenant<br/>• AWS manages hardware<br/>• FIPS 140-2 Level 2<br/>• Automatic backups<br/>• Free tier available<br/>• Integrates with AWS services"]
    end
    
    subgraph AWS_CloudHSM_Group["AWS CloudHSM"]
        HSM[CloudHSM]
        HSM_Features["• Single-tenant dedicated HSM<br/>• You manage keys<br/>• FIPS 140-2 Level 3<br/>• No free tier<br/>• Industry-standard APIs<br/>• PKCS#11, JCE, CNG"]
    end
    
    subgraph Use_Cases_Group["Use Cases"]
        KMS --> KMS_Use["• Most AWS workloads<br/>• S3, EBS encryption<br/>• Simple key management<br/>• Cost-effective"]
        
        HSM --> HSM_Use["• Contractual requirements<br/>• Regulatory compliance<br/>• FIPS 140-2 Level 3<br/>• Custom key store for KMS"]
    end
    
    classDef style1 fill:#FF9900
    class KMS style1
    classDef style2 fill:#569A31
    class HSM style2
```

## Secrets Manager vs Parameter Store

### Secrets Manager and Parameter Store Comparison

```mermaid
graph TB
    subgraph AWS_Secrets_Manager_Group["AWS Secrets Manager"]
        SM[Secrets Manager]
        SM_Features["Features:<br/>💰 $0.40/secret/month + API calls<br/>🔄 Automatic rotation<br/>🔐 Encrypt with KMS<br/>🎯 RDS integration<br/>📊 Cross-account access<br/>⏱️ Rotation: Lambda function"]
        
        SM_Use["Use Cases:<br/>• Database credentials<br/>• API keys requiring rotation<br/>• OAuth tokens<br/>• RDS password rotation"]
    end
    
    subgraph Systems_Manager_Parameter_Store_Group["Systems Manager Parameter Store"]
        PS[Parameter Store]
        
        Standard["Standard Parameters<br/>✅ Free<br/>📏 4 KB limit<br/>📊 10,000 parameters<br/>⚠️ No rotation"]
        
        Advanced["Advanced Parameters<br/>💰 $0.05/parameter/month<br/>📏 8 KB limit<br/>📊 100,000 parameters<br/>📋 Parameter policies<br/>⏱️ Manual rotation"]
        
        PS --> Standard
        PS --> Advanced
        
        PS_Use["Use Cases:<br/>• Configuration data<br/>• License keys<br/>• AMI IDs<br/>• Application parameters<br/>• Cost-sensitive scenarios"]
    end
    
    Both["Both Support:<br/>✅ KMS encryption<br/>✅ CloudFormation<br/>✅ IAM permissions<br/>✅ CloudWatch Events"]
    
    SM -.Features.-> SM_Features
    SM -.Use.-> SM_Use
    PS -.Use.-> PS_Use
    
    classDef style1 fill:#FF9900
    class SM style1
    classDef style2 fill:#569A31
    class PS style2
```

### Secrets Manager Rotation

```mermaid
sequenceDiagram
    participant App as Application
    participant SM as Secrets Manager
    participant Lambda as Rotation Lambda
    participant RDS as RDS Database
    
    Note over SM: Rotation interval: 30 days
    
    SM->>Lambda: Trigger rotation
    Lambda->>SM: CreateSecret (new password(
    Lambda->>RDS: Create new user credentials
    RDS->>Lambda: Success
    Lambda->>SM: SetSecret (update with new password(
    Lambda->>RDS: Test new credentials
    RDS->>Lambda: Connection successful
    Lambda->>SM: FinishSecret (mark as current(
    SM->>Lambda: DeleteSecret (old version after grace period(
    
    Note over App,RDS: Application automatically gets new credentials
    
    App->>SM: GetSecretValue
    SM->>App: Return current secret
    App->>RDS: Connect with new credentials
    
```

## AWS WAF & Shield

### AWS WAF Architecture

```mermaid
graph TB
    Internet[Internet Traffic]
    
    subgraph AWS_WAF_Web_ACL_Group["AWS WAF Web ACL"]
        WAF["AWS WAF<br/>Web Application Firewall"]
        
        Rules[WAF Rules]
        
        Rules --> Rule1["SQL Injection<br/>Protection"]
        Rules --> Rule2["Cross-Site Scripting<br/>XSS Protection"]
        Rules --> Rule3["Rate-based Rules<br/>DDoS mitigation"]
        Rules --> Rule4["Geo-blocking<br/>Country restrictions"]
        Rules --> Rule5["IP Reputation Lists<br/>Known bad IPs"]
        Rules --> Rule6["Custom Rules<br/>Size constraints, regex"]
    end
    
    subgraph Protected_Resources_Group["Protected Resources"]
        CloudFront["CloudFront<br/>Distribution"]
        ALB["Application<br/>Load Balancer"]
        API[API Gateway]
        AppSync[AWS AppSync]
    end
    
    Internet --> WAF
    WAF --> Rules
    
    Rules -->|Allow| CloudFront
    Rules -->|Allow| ALB
    Rules -->|Allow| API
    Rules -->|Allow| AppSync
    Rules -->|Block| Blocked["❌ Blocked Traffic"]
    
    ManagedRules["AWS Managed Rules<br/>Pre-configured rule sets<br/>OWASP Top 10"]
    
    WAF -.Can use.-> ManagedRules
    
    classDef style1 fill:#FF9900
    class WAF style1
    classDef style2 fill:#C00
    class Blocked style2
```

### AWS Shield Standard vs Advanced

```mermaid
graph TB
    Shield["AWS Shield<br/>DDoS Protection"]
    
    Shield --> Standard["Shield Standard<br/>✅ FREE<br/>✅ Automatic<br/>✅ Layer 3/4 protection<br/>✅ All AWS customers"]
    
    Shield --> Advanced["Shield Advanced<br/>💰 $3,000/month<br/>✅ Layer 3/4/7 protection<br/>✅ 24/7 DDoS Response Team<br/>✅ Cost protection<br/>✅ Real-time notifications"]
    
    subgraph Standard_Protection_Group["Standard Protection"]
        Standard --> S_Features["• SYN/UDP floods<br/>• Reflection attacks<br/>• Network layer DDoS<br/>• Automatic detection"]
    end
    
    subgraph Advanced_Protection_Group["Advanced Protection"]
        Advanced --> A_Features["• Enhanced detection<br/>• Advanced reporting<br/>• CloudFront, Route 53, ELB<br/>• Global Threat Dashboard<br/>• WAF included at no cost"]
        
        Advanced --> DRT["AWS DDoS Response Team<br/>24/7 access<br/>Incident response"]
    end
    
    Use["Use Shield Advanced when:<br/>• High-value applications<br/>• Potential large-scale DDoS<br/>• Need expert support<br/>• Want cost protection"]
    
    classDef style1 fill:#569A31
    class Standard style1
    classDef style2 fill:#FF9900
    class Advanced style2
```

## Amazon GuardDuty

### GuardDuty Architecture

```mermaid
graph TB
    subgraph Data_Sources_Group["Data Sources"]
        VPCFlow[VPC Flow Logs]
        CloudTrailLogs[CloudTrail Events]
        DNSLogs[DNS Logs]
        K8sLogs[Kubernetes Audit Logs]
        S3Logs[S3 Data Events]
    end
    
    subgraph GuardDuty_Group["GuardDuty"]
        GD["Amazon GuardDuty<br/>Intelligent Threat Detection<br/>Machine Learning"]
        
        Analysis["Threat Analysis<br/>• Anomaly detection<br/>• ML algorithms<br/>• Threat intelligence feeds<br/>• Known malicious IPs"]
        
        GD --> Analysis
    end
    
    subgraph Findings_Group["Findings"]
        Finding1["Compromised EC2 Instance<br/>Bitcoin mining"]
        Finding2[Unauthorized API Calls]
        Finding3[Reconnaissance Activity]
        Finding4[Suspicious DNS queries]
        Finding5[Unusual S3 access]
    end
    
    subgraph Actions_Group["Actions"]
        EventBridge[EventBridge Rules]
        SNS[SNS Notifications]
        Lambda[Lambda Remediation]
        SecurityHub[Security Hub Integration]
    end
    
    VPCFlow --> GD
    CloudTrailLogs --> GD
    DNSLogs --> GD
    K8sLogs --> GD
    S3Logs --> GD
    
    Analysis --> Finding1
    Analysis --> Finding2
    Analysis --> Finding3
    Analysis --> Finding4
    Analysis --> Finding5
    
    Finding1 --> EventBridge
    Finding2 --> EventBridge
    
    EventBridge --> SNS
    EventBridge --> Lambda
    EventBridge --> SecurityHub
    
    Features["Features:<br/>✅ 30-day free trial<br/>✅ Continuous monitoring<br/>✅ No agents required<br/>✅ Low overhead<br/>💰 Pay per million events analyzed"]
    
    classDef style1 fill:#FF9900
    class GD style1
    classDef style2 fill:#569A31
    class Analysis style2
```

## Amazon Inspector

### Inspector Assessment

```mermaid
graph TB
    subgraph Resources_Group["Resources to Scan"]
        EC2[EC2 Instances]
        ECR[ECR Container Images]
        Lambda[Lambda Functions]
    end
    
    subgraph Inspector_Group["Amazon Inspector"]
        Inspector["Amazon Inspector<br/>Automated Security Assessment"]
        
        Scans[Continuous Scans]
        
        CVE["CVE Detection<br/>Common Vulnerabilities<br/>and Exposures"]
        Network["Network Reachability<br/>Analysis"]
        Package["Software package<br/>vulnerabilities"]
        
        Inspector --> Scans
        Scans --> CVE
        Scans --> Network
        Scans --> Package
    end
    
    subgraph Findings_Group["Risk Findings"]
        Critical[Critical Vulnerabilities]
        High[High Risk]
        Medium[Medium Risk]
        Low[Low Risk]
    end
    
    subgraph Integration_Group["Integration & Remediation"]
        SecurityHub[Security Hub]
        EventBridge[EventBridge]
        SSM["Systems Manager<br/>Patch Manager"]
        
        EventBridge --> SSM
    end
    
    subgraph Features_Group["Key Features"]
        Features["✅ Continuous scanning<br/>✅ Risk scoring<br/>✅ Remediation guidance<br/>✅ Integration with CI/CD<br/>💰 Pay per assessment"]
    end
    
    EC2 --> Inspector
    ECR --> Inspector
    Lambda --> Inspector
    
    CVE --> Critical
    CVE --> High
    CVE --> Medium
    CVE --> Low
    
    Network --> High
    Network --> Medium
    
    Package --> Critical
    Package --> High
    Package --> Medium
    Package --> Low
    
    Critical --> SecurityHub
    Critical --> EventBridge
    High --> EventBridge
    Medium --> SecurityHub
    
    Inspector -.-> Features
    
    classDef inspectorStyle fill:#FF9900,stroke:#333,stroke-width:2px,color:#fff
    classDef criticalStyle fill:#C00,stroke:#333,stroke-width:2px,color:#fff
    classDef highStyle fill:#FF6B00,stroke:#333,stroke-width:2px,color:#fff
    classDef mediumStyle fill:#FFA500,stroke:#333,stroke-width:2px,color:#fff
    classDef lowStyle fill:#FFD700,stroke:#333,stroke-width:2px,color:#000
    classDef resourceStyle fill:#3B48CC,stroke:#333,stroke-width:2px,color:#fff
    classDef scanStyle fill:#569A31,stroke:#333,stroke-width:2px,color:#fff
    classDef integrationStyle fill:#146EB4,stroke:#333,stroke-width:2px,color:#fff
    classDef featureStyle fill:#232F3E,stroke:#FF9900,stroke-width:2px,color:#fff
    
    class Inspector inspectorStyle
    class Critical criticalStyle
    class High highStyle
    class Medium mediumStyle
    class Low lowStyle
    class EC2,ECR,Lambda resourceStyle
    class Scans,CVE,Network,Package scanStyle
    class SecurityHub,EventBridge,SSM integrationStyle
    class Features featureStyle
```

## AWS Macie

### Macie Data Discovery

```mermaid
graph TB
    subgraph S3_Buckets_Group["S3 Buckets"]
        Bucket1["S3 Bucket 1<br/>Customer Data"]
        Bucket2["S3 Bucket 2<br/>Financial Records"]
        Bucket3["S3 Bucket 3<br/>Logs"]
    end
    
    subgraph Amazon_Macie_Group["Amazon Macie"]
        Macie["Amazon Macie<br/>ML-powered Data Security"]
        
        ML["Machine Learning<br/>Classification"]
        
        Detects["Detection:<br/>• PII Personal Info<br/>• PHI Health Info<br/>• Financial data<br/>• Credentials<br/>• API keys"]
    end
    
    subgraph Findings_Group["Findings"]
        PII["PII Found<br/>Credit cards, SSN"]
        Unencrypted["Unencrypted<br/>Sensitive Data"]
        PublicAccess["Publicly Accessible<br/>Sensitive Data"]
        Policy["Policy Findings<br/>Encryption disabled"]
    end
    
    subgraph Actions_Group["Actions"]
        EventBridge[EventBridge]
        SNS[SNS Alert]
        SecurityHub[Security Hub]
        Remediate["Auto-Remediation<br/>Lambda"]
    end
    
    Bucket1 --> Macie
    Bucket2 --> Macie
    Bucket3 --> Macie
    
    Macie --> ML
    ML --> Detects
    
    Detects --> PII
    Detects --> Unencrypted
    Detects --> PublicAccess
    Detects --> Policy
    
    PII --> EventBridge
    PublicAccess --> EventBridge
    
    EventBridge --> SNS
    EventBridge --> SecurityHub
    EventBridge --> Remediate
    
    classDef style1 fill:#FF9900
    class Macie style1
    classDef style2 fill:#C00
    class PII style2
```

## AWS Certificate Manager (ACM)

### ACM Certificate Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Request: Request Certificate
    Request --> Validation: Domain Validation Required
    
    Validation --> DNS: DNS Validation
    Validation --> Email: Email Validation
    
    DNS --> Issued: Add CNAME record
    Email --> Issued: Click email link
    
    Issued --> InUse: Associate with resource
    InUse --> AutoRenew: Auto-renewal (60 days before expiry(
    AutoRenew --> InUse: Renewed
    
    InUse --> Revoked: Revoke Certificate
    Revoked --> [*]
    
    note right of Issued
        Certificate valid for 13 months
        Free for AWS resources
    end note
    
    note right of AutoRenew
        Automatic renewal
        if validation stays valid
    end note
```

### ACM Integration

```mermaid
graph TB
    ACM["AWS Certificate Manager<br/>Free SSL/TLS Certificates"]
    
    subgraph Supported_Services_Group["Supported Services"]
        ELB["Elastic Load Balancer<br/>ALB, NLB, CLB"]
        CloudFront["CloudFront<br/>Distributions"]
        API[API Gateway]
        ElasticBeanstalk[Elastic Beanstalk]
        AppRunner[App Runner]
    end
    
    subgraph Certificate_Types_Group["Certificate Types"]
        Public["Public Certificates<br/>✅ Free<br/>✅ Auto-renewal<br/>✅ CA-signed"]
        
        Private["Private Certificates<br/>💰 $400/month for CA<br/>✅ Internal use<br/>✅ AWS Private CA"]
    end
    
    ACM --> Public
    ACM --> Private
    
    Public --> ELB
    Public --> CloudFront
    Public --> API
    Public --> ElasticBeanstalk
    Public --> AppRunner
    
    Private --> Internal["Internal Applications<br/>Private APIs"]
    
    Note["Note: Cannot export public certs<br/>Can export private certs<br/>Not supported on EC2 directly"]
    
    classDef style1 fill:#FF9900
    class ACM style1
    classDef style2 fill:#569A31
    class Public style2
```

## AWS Security Services Overview

### Security Services Map

```mermaid
mindmap
    root((AWS Security Services))
        Identity & Access
            IAM
            Cognito
            Directory Service
            SSO
        Detection
            GuardDuty
            Inspector
            Macie
            Detective
            Security Hub
        Protection
            WAF
            Shield
            Firewall Manager
        Data Protection
            KMS
            CloudHSM
            Secrets Manager
            Certificate Manager
        Compliance
            Artifact
            Audit Manager
            Config
        Incident Response
            Systems Manager
            CloudFormation
            Lambda
```

### Defense in Depth Strategy

```mermaid
graph TB
    Start[Internet Traffic]
    
    Layer1["Layer 1: Edge Protection • Route 53 with health checks • CloudFront with WAF • Shield Standard/Advanced"]
    
    Layer2["Layer 2: Network • VPC with NACLs • Security Groups • Network Firewall"]
    
    Layer3["Layer 3: Compute • IAM roles for EC2 • Instance hardening • Patch management • Inspector scans"]
    
    Layer4["Layer 4: Application • WAF rules • API authentication • Input validation"]
    
    Layer5["Layer 5: Data • Encryption at rest KMS • Encryption in transit TLS • S3 bucket policies • Macie scanning"]
    
    Layer6["Layer 6: Monitoring • CloudTrail logging • GuardDuty threats • Security Hub compliance • CloudWatch alarms"]
    
    Start --> Layer1
    Layer1 --> Layer2
    Layer2 --> Layer3
    Layer3 --> Layer4
    Layer4 --> Layer5
    Layer5 --> Layer6
    
    Layer6 --> Response["Incident Response • Automated remediation • Security team alerts • Forensics & analysis"]
    
    classDef style1 fill:#FF9900
    class Layer1 style1
    classDef style2 fill:#569A31
    class Layer3 style2
    classDef style3 fill:#146EB4
    class Layer5 style3
    classDef style4 fill:#C00
    class Response style4
```

