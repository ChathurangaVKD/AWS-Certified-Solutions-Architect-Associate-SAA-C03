# IAM - Mermaid Diagrams

## IAM Components Overview

### IAM Core Components Relationship

```mermaid
graph TB
    subgraph "IAM Components"
        Users[IAM Users<br/>People & Applications]
        Groups[IAM Groups<br/>Collection of Users]
        Roles[IAM Roles<br/>For Services & Temporary Access]
        Policies[IAM Policies<br/>JSON Documents]
    end
    
    subgraph "AWS Services"
        EC2[EC2]
        S3[S3]
        RDS[RDS]
        Lambda[Lambda]
    end
    
    Users -->|Member of| Groups
    Groups -->|Attached| Policies
    Users -->|Attached| Policies
    Roles -->|Attached| Policies
    
    Policies -->|Grants Permissions to| EC2
    Policies -->|Grants Permissions to| S3
    Policies -->|Grants Permissions to| RDS
    Policies -->|Grants Permissions to| Lambda
    
    EC2 -->|Assumes| Roles
    Lambda -->|Assumes| Roles
    
    style Users fill:#FF9900
    style Groups fill:#FF9900
    style Roles fill:#FF9900
    style Policies fill:#146EB4
```

### IAM Hierarchy and Structure

```mermaid
graph TB
    Root[AWS Account Root User<br/>⚠️ Complete Access]
    
    Root --> AdminGroup[Administrators Group]
    Root --> DevGroup[Developers Group]
    Root --> OpsGroup[Operations Group]
    
    AdminGroup --> AdminPolicy[AdministratorAccess<br/>Policy]
    DevGroup --> DevPolicy[Developer Policy<br/>Limited EC2, S3, RDS]
    OpsGroup --> OpsPolicy[Operations Policy<br/>Read-Only + CloudWatch]
    
    AdminGroup --> User1[Alice]
    AdminGroup --> User2[Bob]
    
    DevGroup --> User3[Charlie]
    DevGroup --> User4[Diana]
    
    OpsGroup --> User5[Eve]
    
    User1 -.Additional Policy.-> MFAPolicy[MFA Policy]
    
    style Root fill:#C00
    style AdminGroup fill:#FF9900
    style DevGroup fill:#FF9900
    style OpsGroup fill:#FF9900
    style AdminPolicy fill:#146EB4
```

## IAM Users and Authentication

### User Authentication Flow

```mermaid
sequenceDiagram
    actor User
    participant Console as AWS Console
    participant IAM
    participant MFA as MFA Device
    participant Service as AWS Service
    
    User->>Console: Enter Username & Password
    Console->>IAM: Validate Credentials
    IAM->>Console: Request MFA Token
    Console->>User: Prompt for MFA
    User->>MFA: Generate Token
    MFA->>User: 6-digit Code
    User->>Console: Enter MFA Token
    Console->>IAM: Validate MFA
    IAM->>Console: Session Token
    Console->>User: Access Granted
    User->>Service: Perform Action
    Service->>IAM: Verify Permissions
    IAM->>Service: Allow/Deny
    Service->>User: Result
    
    style IAM fill:#FF9900
    style MFA fill:#146EB4
```

### Access Keys for Programmatic Access

```mermaid
graph LR
    subgraph "IAM User"
        User[User: Developer]
        AccessKey[Access Key ID:<br/>AKIAIOSFODNN7EXAMPLE]
        SecretKey[Secret Access Key:<br/>wJalrXUtnFEMI/K7MDENG/...]
    end
    
    subgraph "Client Tools"
        CLI[AWS CLI]
        SDK[AWS SDK]
        API[Direct API Calls]
    end
    
    subgraph "AWS Services"
        S3[S3]
        EC2[EC2]
        DynamoDB[DynamoDB]
    end
    
    User --> AccessKey
    User --> SecretKey
    
    AccessKey --> CLI
    SecretKey --> CLI
    
    AccessKey --> SDK
    SecretKey --> SDK
    
    AccessKey --> API
    SecretKey --> API
    
    CLI --> S3
    SDK --> EC2
    API --> DynamoDB
    
    style User fill:#FF9900
    style AccessKey fill:#569A31
    style SecretKey fill:#C00
```

## IAM Groups

### Groups Management Pattern

```mermaid
graph TB
    subgraph "Organization"
        Dev[Developers Group]
        QA[QA Group]
        Ops[Operations Group]
        Data[Data Scientists Group]
        Admin[Administrators Group]
    end
    
    subgraph "Users"
        U1[Alice] -.Member.-> Dev
        U2[Bob] -.Member.-> Dev
        U3[Charlie] -.Member.-> QA
        U4[Diana] -.Member.-> Ops
        U5[Eve] -.Member.-> Data
        U6[Frank] -.Member.-> Admin
        
        U2 -.Also Member.-> QA
        U5 -.Also Member.-> Dev
    end
    
    subgraph "Policies"
        Dev --> P1[EC2 Full Access<br/>S3 Read/Write<br/>RDS Access]
        QA --> P2[EC2 Read Only<br/>S3 Read Only]
        Ops --> P3[CloudWatch Full<br/>EC2 Start/Stop<br/>Systems Manager]
        Data --> P4[S3 Full Access<br/>Glue & Athena<br/>SageMaker]
        Admin --> P5[AdministratorAccess]
    end
    
    style Dev fill:#FF9900
    style QA fill:#FF9900
    style Ops fill:#FF9900
    style Data fill:#FF9900
    style Admin fill:#C00
```

## IAM Roles

### IAM Role Assumption Flow

```mermaid
sequenceDiagram
    participant EC2 as EC2 Instance
    participant STS as AWS STS
    participant Role as IAM Role
    participant S3 as S3 Bucket
    
    Note over EC2: Instance has IAM Role attached
    EC2->>STS: AssumeRole Request
    STS->>Role: Validate Trust Policy
    Role->>STS: Trust Policy Valid
    STS->>EC2: Temporary Security Credentials<br/>(Access Key + Secret + Token)
    Note over EC2: Credentials valid for 1 hour
    EC2->>S3: Access S3 using temporary credentials
    S3->>Role: Check Permissions Policy
    Role->>S3: Allow/Deny
    S3->>EC2: Return Data
    
    style EC2 fill:#FF9900
    style STS fill:#146EB4
    style Role fill:#569A31
```

### Common Role Use Cases

```mermaid
graph TB
    subgraph "AWS Service Roles"
        EC2Role[EC2 Instance Role<br/>Access S3, DynamoDB, etc.]
        LambdaRole[Lambda Execution Role<br/>Access CloudWatch Logs]
        ECSRole[ECS Task Role<br/>Access AWS Services]
    end
    
    subgraph "Cross-Account Access"
        AccountA[Account A<br/>Production]
        AccountB[Account B<br/>Development]
        CrossRole[Cross-Account Role]
        
        AccountB -.Assume.-> CrossRole
        CrossRole -.Access.-> AccountA
    end
    
    subgraph "Federated Access"
        SAML[SAML 2.0 Provider<br/>Active Directory]
        WebIdentity[Web Identity Federation<br/>Google, Facebook, Amazon]
        FedRole[Federated Role]
        
        SAML -.Authenticate.-> FedRole
        WebIdentity -.Authenticate.-> FedRole
    end
    
    EC2[EC2 Instance] --> EC2Role
    Lambda[Lambda Function] --> LambdaRole
    ECS[ECS Task] --> ECSRole
    
    style EC2Role fill:#FF9900
    style LambdaRole fill:#FF9900
    style CrossRole fill:#569A31
    style FedRole fill:#146EB4
```

### Role Trust Policy vs Permission Policy

```mermaid
graph LR
    subgraph "IAM Role Components"
        TrustPolicy[Trust Policy<br/>WHO can assume this role?]
        PermPolicy[Permission Policy<br/>WHAT can they do?]
    end
    
    subgraph "Trust Policy Example"
        TP1["Trusted Entity:<br/>• EC2 Service<br/>• Another AWS Account<br/>• SAML Provider<br/>• Web Identity"]
    end
    
    subgraph "Permission Policy Example"
        PP1["Allowed Actions:<br/>• s3:GetObject<br/>• s3:PutObject<br/>• dynamodb:Query<br/>• logs:CreateLogGroup"]
    end
    
    TrustPolicy --> TP1
    PermPolicy --> PP1
    
    Entity[EC2/User/Service] -->|1. Can I assume?| TrustPolicy
    TrustPolicy -->|2. Assume Role| STS[AWS STS]
    STS -->|3. Temporary Credentials| Entity
    Entity -->|4. What can I do?| PermPolicy
    PermPolicy -->|5. Allow/Deny| Action[AWS Service Action]
    
    style TrustPolicy fill:#FF9900
    style PermPolicy fill:#146EB4
    style STS fill:#569A31
```

## IAM Policies

### Policy Types Overview

```mermaid
graph TB
    subgraph "Policy Types"
        Identity[Identity-based Policies<br/>Attached to Users, Groups, Roles]
        Resource[Resource-based Policies<br/>Attached to Resources like S3]
        Permission[Permissions Boundary<br/>Maximum Permissions Limit]
        SCP[Service Control Policies<br/>AWS Organizations]
        Session[Session Policies<br/>Temporary Credentials]
        ACL[Access Control Lists<br/>Legacy]
    end
    
    Identity --> User[IAM User]
    Identity --> Group[IAM Group]
    Identity --> Role[IAM Role]
    
    Resource --> S3Bucket[S3 Bucket Policy]
    Resource --> SQS[SQS Queue Policy]
    Resource --> Lambda[Lambda Resource Policy]
    
    Permission -.Limits.-> Identity
    SCP -.Limits.-> Account[AWS Accounts]
    
    style Identity fill:#FF9900
    style Resource fill:#146EB4
    style Permission fill:#569A31
    style SCP fill:#8C4FFF
```

### Policy Evaluation Logic

```mermaid
flowchart TD
    Start([API Request]) --> Default{Default Deny}
    
    Default --> Explicit{Explicit Deny<br/>Exists?}
    Explicit -->|Yes| Deny([❌ DENY])
    Explicit -->|No| SCP{SCP<br/>Allows?}
    
    SCP -->|No| Deny
    SCP -->|Yes| Boundary{Permission Boundary<br/>Allows?}
    
    Boundary -->|No| Deny
    Boundary -->|Yes| Identity{Identity Policy<br/>Allows?}
    
    Identity -->|No| Resource{Resource Policy<br/>Allows?}
    Identity -->|Yes| Allow([✅ ALLOW])
    
    Resource -->|Yes| Allow
    Resource -->|No| Deny
    
    style Start fill:#232F3E
    style Allow fill:#569A31
    style Deny fill:#C00
    style Explicit fill:#FF9900
```

### Policy Structure Example

```mermaid
graph TB
    Policy[IAM Policy JSON]
    
    Policy --> Version[Version: 2012-10-17]
    Policy --> Statement[Statement Array]
    
    Statement --> Stmt1[Statement 1]
    Statement --> Stmt2[Statement 2]
    
    Stmt1 --> Effect1[Effect: Allow]
    Stmt1 --> Action1[Action: s3:GetObject]
    Stmt1 --> Resource1[Resource: arn:aws:s3:::bucket/*]
    Stmt1 --> Condition1[Condition: IpAddress]
    
    Stmt2 --> Effect2[Effect: Deny]
    Stmt2 --> Action2[Action: s3:DeleteBucket]
    Stmt2 --> Resource2[Resource: arn:aws:s3:::bucket]
    
    style Policy fill:#FF9900
    style Effect1 fill:#569A31
    style Effect2 fill:#C00
```

## Multi-Factor Authentication (MFA)

### MFA Authentication Process

```mermaid
sequenceDiagram
    actor User
    participant Device as MFA Device
    participant AWS
    participant IAM
    
    User->>AWS: Login with Password
    AWS->>IAM: Validate Password
    IAM->>AWS: Password Valid
    AWS->>User: Request MFA Token
    User->>Device: Request Token
    Device->>Device: Generate Time-based Token
    Device->>User: Display 6-digit Code
    User->>AWS: Enter MFA Code
    AWS->>IAM: Validate MFA Token
    IAM->>AWS: MFA Valid
    AWS->>User: Access Granted ✅
    
    style IAM fill:#FF9900
    style Device fill:#146EB4
```

### MFA Device Types

```mermaid
graph TB
    MFA[MFA Options]
    
    MFA --> Virtual[Virtual MFA Device]
    MFA --> Hardware[Hardware MFA Device]
    MFA --> U2F[U2F Security Key]
    
    Virtual --> GoogleAuth[Google Authenticator]
    Virtual --> Authy[Authy]
    Virtual --> Microsoft[Microsoft Authenticator]
    
    Hardware --> Gemalto[Gemalto Token]
    Hardware --> SurePass[SurePassID]
    
    U2F --> Yubikey[YubiKey]
    
    style MFA fill:#FF9900
    style Virtual fill:#146EB4
    style Hardware fill:#569A31
    style U2F fill:#8C4FFF
```

## Cross-Account Access

### Cross-Account Role Assumption

```mermaid
sequenceDiagram
    participant UserA as User in Account A<br/>(Dev Account)
    participant STSA as STS Account A
    participant Role as Cross-Account Role<br/>in Account B
    participant STSb as STS Account B
    participant S3 as S3 in Account B<br/>(Prod Account)
    
    Note over UserA,S3: Setup: Account B creates role trusting Account A
    
    UserA->>STSA: Authenticate
    STSA->>UserA: Session Credentials
    UserA->>STSb: AssumeRole (Account B Role)
    STSb->>Role: Check Trust Policy
    Role->>STSb: Account A is Trusted
    STSb->>UserA: Temporary Credentials
    Note over UserA: Credentials valid 15min-12hrs
    UserA->>S3: Access S3 with temp credentials
    S3->>UserA: Return Data
    
    style Role fill:#FF9900
    style STSb fill:#146EB4
```

### Cross-Account Architecture

```mermaid
graph TB
    subgraph "Account A - Development (111111111111)"
        DevUser[Developer User]
        DevGroup[Developers Group]
        AssumePolicy[Assume Role Policy<br/>sts:AssumeRole]
        
        DevUser --> DevGroup
        DevGroup --> AssumePolicy
    end
    
    subgraph "Account B - Production (222222222222)"
        ProdRole[Production-ReadOnly-Role]
        TrustPolicy[Trust Policy:<br/>Trust Account 111111111111]
        PermPolicy[Permission Policy:<br/>S3 Read, EC2 Describe]
        ProdResources[Production Resources<br/>S3, EC2, RDS]
        
        ProdRole --> TrustPolicy
        ProdRole --> PermPolicy
        PermPolicy --> ProdResources
    end
    
    AssumePolicy -.AssumeRole.-> ProdRole
    
    style DevUser fill:#FF9900
    style ProdRole fill:#569A31
    style TrustPolicy fill:#146EB4
```

## Identity Federation

### SAML 2.0 Federation Flow

```mermaid
sequenceDiagram
    actor User
    participant IdP as Identity Provider<br/>(Active Directory/ADFS)
    participant AWS
    participant STS as AWS STS
    participant Console as AWS Console
    
    User->>IdP: 1. Login with corporate credentials
    IdP->>User: 2. Authenticate
    IdP->>User: 3. Return SAML Assertion
    User->>STS: 4. AssumeRoleWithSAML + SAML Assertion
    STS->>STS: 5. Validate SAML Assertion
    STS->>User: 6. Temporary Security Credentials
    User->>Console: 7. Access AWS Console
    
    style IdP fill:#FF9900
    style STS fill:#146EB4
```

### Web Identity Federation (Cognito)

```mermaid
graph TB
    User[Mobile/Web User]
    
    User --> Social{Choose Provider}
    
    Social --> Google[Google]
    Social --> Facebook[Facebook]
    Social --> Amazon[Amazon]
    Social --> Apple[Apple]
    
    Google --> Cognito[Amazon Cognito]
    Facebook --> Cognito
    Amazon --> Cognito
    Apple --> Cognito
    
    Cognito --> STS[AWS STS]
    STS --> TempCreds[Temporary AWS Credentials]
    
    TempCreds --> S3[Access S3]
    TempCreds --> DynamoDB[Access DynamoDB]
    TempCreds --> Lambda[Invoke Lambda]
    
    style User fill:#232F3E
    style Cognito fill:#FF9900
    style STS fill:#146EB4
    style TempCreds fill:#569A31
```

## IAM Best Practices

### Security Best Practices Flow

```mermaid
flowchart TD
    Start([IAM Best Practices]) --> Root[🔐 Secure Root Account]
    
    Root --> RootMFA[Enable MFA on Root]
    Root --> RootNoUse[Don't use Root for daily tasks]
    Root --> RootKeys[Delete Root Access Keys]
    
    RootNoUse --> Users[Create Individual IAM Users]
    Users --> Groups[Use Groups for Permissions]
    Groups --> LeastPriv[Apply Least Privilege]
    
    LeastPriv --> Policies[Use AWS Managed Policies]
    Policies --> Review[Regular Access Review]
    
    Review --> MFA[Enable MFA for All Users]
    MFA --> Rotate[Rotate Credentials Regularly]
    Rotate --> Conditions[Use Policy Conditions]
    
    Conditions --> Roles[Use Roles for Applications]
    Roles --> Monitor[Monitor with CloudTrail]
    Monitor --> End([Secure IAM Setup ✅])
    
    style Start fill:#232F3E
    style Root fill:#C00
    style End fill:#569A31
    style LeastPriv fill:#FF9900
```

### Permission Boundary Pattern

```mermaid
graph TB
    subgraph "Permission Evaluation"
        MaxPerm[Maximum Permissions<br/>Permission Boundary]
        IdentityPerm[Identity Policy<br/>What user can do]
        Effective[Effective Permissions<br/>Intersection]
        
        MaxPerm --> Effective
        IdentityPerm --> Effective
    end
    
    subgraph "Example"
        Boundary["Boundary Policy:<br/>• Allow: EC2, S3, RDS<br/>• Region: us-east-1"]
        
        UserPolicy["User Policy:<br/>• Allow: EC2:*<br/>• Allow: S3:*<br/>• Allow: Lambda:*<br/>• All Regions"]
        
        Result["Effective Permission:<br/>• Allow: EC2:* (us-east-1)<br/>• Allow: S3:* (us-east-1)<br/>❌ No RDS (not in user policy)<br/>❌ No Lambda (not in boundary)"]
    end
    
    Boundary -.AND.-> Result
    UserPolicy -.AND.-> Result
    
    style Effective fill:#569A31
    style Result fill:#FF9900
```

## IAM Access Analyzer

### Access Analyzer Architecture

```mermaid
graph TB
    Analyzer[IAM Access Analyzer]
    
    Analyzer --> Scan{Scan Resources}
    
    Scan --> S3[S3 Buckets]
    Scan --> IAM[IAM Roles]
    Scan --> Lambda[Lambda Functions]
    Scan --> SQS[SQS Queues]
    Scan --> KMS[KMS Keys]
    Scan --> Secrets[Secrets Manager]
    
    S3 --> Findings[Access Findings]
    IAM --> Findings
    Lambda --> Findings
    SQS --> Findings
    KMS --> Findings
    Secrets --> Findings
    
    Findings --> Alert{External Access<br/>Detected?}
    
    Alert -->|Yes| Notify[SNS Notification<br/>Security Team]
    Alert -->|Yes| Report[Generate Report]
    Alert -->|No| Safe[No Action Needed]
    
    style Analyzer fill:#FF9900
    style Findings fill:#146EB4
    style Notify fill:#C00
    style Safe fill:#569A31
```

## IAM Database Authentication

### RDS IAM Authentication Flow

```mermaid
sequenceDiagram
    participant App as Application
    participant IAM
    participant RDS as RDS MySQL/PostgreSQL
    
    Note over App: Has IAM Role with rds-db:connect permission
    
    App->>IAM: Request Authentication Token
    IAM->>IAM: Verify IAM Credentials
    IAM->>App: Return Auth Token (15 min validity)
    
    App->>RDS: Connect with username + auth token
    RDS->>IAM: Validate Token
    IAM->>RDS: Token Valid
    RDS->>App: Connection Established
    
    Note over App,RDS: Benefits: No password storage, IAM centralized auth, SSL enforced
    
    style IAM fill:#FF9900
    style RDS fill:#3B48CC
```

