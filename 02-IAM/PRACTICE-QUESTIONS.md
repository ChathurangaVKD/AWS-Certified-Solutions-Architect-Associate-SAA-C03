# IAM - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
An application running on Amazon EC2 instances needs to access objects in an Amazon S3 bucket. What is the MOST secure way to grant this access?

A. Create an IAM user with programmatic access and store the access keys on the EC2 instance  
B. Create an IAM role with S3 permissions and attach it to the EC2 instance  
C. Make the S3 bucket public and allow anonymous access  
D. Use the root account credentials on the EC2 instance  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- IAM roles provide temporary security credentials that rotate automatically
- No need to manage or embed long-term credentials
- Most secure and AWS-recommended approach
- Option A: Access keys are long-term credentials, security risk if exposed
- Option C: Violates security best practices
- Option D: Never use root credentials for applications
- **Best Practice**: Always use IAM roles for EC2 instances

**References:** IAM Roles, EC2 Instance Profiles, AWS Security Best Practices
</details>

---

### Question 2
A company needs to grant temporary access to external auditors to review CloudTrail logs in S3. The access should expire after 7 days. What is the BEST solution?

A. Create IAM users for auditors and delete them after 7 days  
B. Create IAM roles and provide auditors with temporary security credentials using AWS STS  
C. Share the root account credentials for 7 days  
D. Create an S3 pre-signed URL valid for 7 days  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS STS (Security Token Service) generates temporary credentials
- IAM roles can be assumed by external users via federation
- Credentials automatically expire based on session duration
- Option A: Requires manual deletion, operational overhead
- Option C: Never share root credentials
- Option D: Pre-signed URLs work but IAM roles are more comprehensive
- **Best for temporary access**: STS with IAM roles

**References:** AWS STS, Temporary Security Credentials, Cross-Account Access
</details>

---

### Question 3
A solutions architect is writing an IAM policy to deny access to all S3 buckets except one specific bucket named "production-data". Which policy element should be used?

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::production-data",
        "arn:aws:s3:::production-data/*"
      ]
    },
    {
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    }
  ]
}
```

What is the correct approach?

A. Use Allow effect for the specific bucket only  
B. Use Deny effect for all buckets except the one  
C. Use both Allow for specific bucket and implicit Deny for others  
D. Use resource-based policy on S3 bucket  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- IAM uses default Deny for all actions not explicitly allowed
- Allow access to "production-data" bucket explicitly
- All other buckets are implicitly denied
- No need for explicit Deny statement for other buckets
- **IAM Evaluation Logic**: Explicit Deny > Allow > Implicit Deny
- Simpler policy: Just Allow the specific bucket

**Correct Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::production-data",
        "arn:aws:s3:::production-data/*"
      ]
    }
  ]
}
```

**References:** IAM Policy Evaluation Logic, S3 IAM Policies
</details>

---

### Question 4
A company has a requirement that all IAM users must use Multi-Factor Authentication (MFA) before they can delete any S3 objects. How can this be enforced?

A. Enable MFA Delete on the S3 bucket  
B. Create an IAM policy with a condition requiring MFA  
C. Use AWS Organizations Service Control Policies  
D. Configure S3 bucket policy to require MFA  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- IAM policy condition `aws:MultiFactorAuthPresent` enforces MFA
- Can be applied to specific actions like `s3:DeleteObject`

**Example Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:DeleteObject",
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

- Option A: MFA Delete protects versioning but requires bucket owner MFA
- Option C: SCPs can enforce but IAM policy is more direct
- Option D: Can work but IAM policy is standard approach

**References:** IAM Policy Conditions, MFA with IAM Policies
</details>

---

### Question 5
A development team needs read-only access to all EC2 instances, but write access should only be granted during business hours (9 AM - 5 PM). How can this be implemented?

A. Use time-based IAM policy conditions  
B. Manually attach/detach policies during business hours  
C. Use AWS Lambda to modify IAM policies based on time  
D. Create two separate IAM groups and move users between them  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- IAM supports time-based conditions using `aws:CurrentTime`
- Can specify date/time ranges for policy evaluation

**Example Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": "*",
      "Condition": {
        "DateGreaterThan": {"aws:CurrentTime": "2026-01-01T09:00:00Z"},
        "DateLessThan": {"aws:CurrentTime": "2026-01-01T17:00:00Z"}
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "ec2:Get*",
        "ec2:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

- Read-only access always allowed
- Write access only during specified hours
- Other options require manual intervention or complex automation

**References:** IAM Policy Conditions, Time-Based Access Control
</details>

---

### Question 6
A company wants to allow users to change their own passwords but nothing else. Which AWS managed policy should be attached?

A. IAMFullAccess  
B. IAMUserChangePassword  
C. IAMReadOnlyAccess  
D. PowerUserAccess  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- `IAMUserChangePassword` is an AWS managed policy for self-service password changes
- Follows principle of least privilege
- Allows users to manage only their own passwords
- Option A: Too permissive, full IAM access
- Option C: Read-only, can't change passwords
- Option D: Almost full access except IAM

**Alternative**: Create custom policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:ChangePassword",
        "iam:GetAccountPasswordPolicy"
      ],
      "Resource": "arn:aws:iam::*:user/${aws:username}"
    }
  ]
}
```

**References:** AWS Managed Policies, Self-Service Password Management
</details>

---

### Question 7
An organization has multiple AWS accounts. They want to centrally manage permissions across all accounts. What is the BEST solution?

A. Create identical IAM policies in each account  
B. Use AWS Organizations with Service Control Policies (SCPs)  
C. Use IAM roles in each account  
D. Share IAM users across accounts  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Service Control Policies (SCPs) set permission boundaries for entire AWS accounts
- Applied at organization, OU, or account level
- Centrally managed from master/management account
- Maximum permissions available, individual IAM policies still needed
- Option A: Not centralized, difficult to maintain
- Option C: Roles help with cross-account access but don't centrally manage permissions
- Option D: IAM users cannot be shared across accounts

**SCP Example** (Deny all regions except us-east-1):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

**References:** AWS Organizations, Service Control Policies
</details>

---

### Question 8
A company uses SAML 2.0 to allow employees to access AWS using their corporate Active Directory credentials. What type of access is this?

A. IAM user access  
B. Root account access  
C. Federated access  
D. Programmatic access  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Federation allows users to access AWS using existing corporate credentials
- SAML 2.0 is a standard for identity federation
- Users authenticate with corporate IdP (like Active Directory)
- IdP provides temporary AWS credentials via IAM role assumption
- No need to create IAM users for each employee
- **Types of Federation**: SAML 2.0, OpenID Connect, Custom Identity Broker

**Federation Flow**:
1. User authenticates with corporate IdP
2. IdP generates SAML assertion
3. User presents assertion to AWS STS
4. STS returns temporary credentials
5. User accesses AWS with temp credentials

**References:** Identity Federation, SAML 2.0, AWS STS
</details>

---

### Question 9
Which statement about IAM policies is correct?

A. Identity-based policies are attached to resources  
B. Resource-based policies are attached to IAM identities  
C. Identity-based policies define permissions for users, groups, and roles  
D. Resource-based policies cannot specify principals from other accounts  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Identity-based policies**: Attached to users, groups, roles (who can do what)
- **Resource-based policies**: Attached to resources like S3, SQS (who can access this resource)
- Option A: Incorrect, identity-based policies attach to identities
- Option B: Incorrect, resource-based policies attach to resources
- Option D: Incorrect, resource-based policies CAN specify cross-account principals

**Examples**:
- Identity-based: IAM user policy, role policy
- Resource-based: S3 bucket policy, KMS key policy, Lambda function policy

**References:** IAM Policy Types, Identity vs Resource-based Policies
</details>

---

### Question 10
A Lambda function needs to access DynamoDB tables. What is the correct way to grant permissions?

A. Create an IAM user for the Lambda function  
B. Create an IAM execution role for the Lambda function  
C. Add permissions directly to the Lambda function  
D. Use resource-based policy on DynamoDB  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Lambda execution role defines what the function can access
- Role is assumed by Lambda service when function executes
- Attach policies to role (e.g., AmazonDynamoDBFullAccess or custom policy)
- Option A: Lambda functions cannot use IAM users
- Option C: No such mechanism, must use IAM roles
- Option D: DynamoDB doesn't have resource-based policies like S3

**Lambda Execution Role Policy Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:Query"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/MyTable"
    }
  ]
}
```

**References:** Lambda Execution Roles, Service Roles
</details>

---

### Question 11
What does the following IAM policy condition do?

```json
"Condition": {
  "IpAddress": {
    "aws:SourceIp": "203.0.113.0/24"
  }
}
```

A. Allows access only from the specified IP range  
B. Denies access from the specified IP range  
C. Logs access from the specified IP range  
D. Routes traffic through the specified IP range  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Condition restricts policy effectiveness to requests from specified IP range
- When used with "Effect": "Allow", grants access only from those IPs
- When used with "Effect": "Deny", denies access from those IPs
- Does not log or route traffic
- **Use Case**: Restrict access to corporate network IPs

**Complete Policy Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

**References:** IAM Policy Conditions, IP-based Access Control
</details>

---

### Question 12
A company wants to ensure that IAM users cannot create EC2 instances larger than t3.medium. How can this be enforced?

A. Use IAM policy with condition checking instance type  
B. Use AWS Config rules  
C. Use AWS Budgets  
D. Use EC2 instance limits  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- IAM policy conditions can restrict EC2 instance types
- Condition key: `ec2:InstanceType`

**Policy Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringEquals": {
          "ec2:InstanceType": ["t3.micro", "t3.small", "t3.medium"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:network-interface/*",
        "arn:aws:ec2:*:*:volume/*",
        "arn:aws:ec2:*:*:key-pair/*",
        "arn:aws:ec2:*:*:security-group/*",
        "arn:aws:ec2:*::image/*"
      ]
    }
  ]
}
```

- Option B: Config rules detect compliance, don't prevent actions
- Option C: Budgets monitor costs, don't restrict actions
- Option D: Service limits are for account-wide quotas, not policy-based restrictions

**References:** IAM Policy Conditions, EC2 Instance Type Restrictions
</details>

---

### Question 13
What is the maximum number of IAM groups a user can belong to?

A. 5  
B. 10  
C. 20  
D. Unlimited  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- An IAM user can be a member of up to 10 groups
- This is an AWS service limit/quota
- Groups simplify permission management
- If more complex permissions needed, use multiple policies or roles

**IAM Limits (Key ones for exam)**:
- Users per account: 5,000 (default)
- Groups per account: 300
- Groups per user: 10
- Managed policies per user/group/role: 10
- Inline policy size: 2,048 characters for users, 10,240 for roles

**References:** IAM Quotas and Limits
</details>

---

### Question 14
A developer accidentally committed AWS access keys to a public GitHub repository. What should be done IMMEDIATELY?

A. Change the password of the IAM user  
B. Delete the GitHub repository  
C. Deactivate and delete the exposed access keys  
D. Enable MFA on the account  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Exposed credentials must be deactivated/deleted immediately
- Prevents unauthorized access using compromised keys
- Steps: Deactivate keys → Create new keys → Delete old keys → Review CloudTrail
- Option A: Passwords are separate from access keys
- Option B: Deleting repo doesn't help if already cloned/indexed
- Option D: MFA doesn't protect already-exposed keys

**Incident Response Steps**:
1. Deactivate compromised keys immediately
2. Review CloudTrail for unauthorized activity
3. Create new access keys
4. Delete compromised keys
5. Scan code repositories
6. Implement secrets management (AWS Secrets Manager, Parameter Store)

**References:** AWS Security Best Practices, Incident Response
</details>

---

### Question 15
Which IAM entity can have both trust policy and permissions policy?

A. IAM User  
B. IAM Group  
C. IAM Role  
D. IAM Policy  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **IAM Roles** have two types of policies:
  - **Trust Policy**: Defines who can assume the role (principal)
  - **Permissions Policy**: Defines what the role can do (actions)
- Users and Groups don't have trust policies
- Policies are documents, not entities with other policies

**Trust Policy Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Permissions Policy Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**References:** IAM Roles, Trust Policies, Role Assumption
</details>

---

### Question 16
A company needs to provide third-party vendors access to specific S3 buckets without creating IAM users. What is the BEST approach?

A. Share root account credentials  
B. Create cross-account IAM roles with external ID  
C. Make S3 buckets public  
D. Use S3 pre-signed URLs  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Cross-account roles allow external accounts to access resources
- External ID adds security layer preventing confused deputy problem
- Vendor assumes role from their AWS account
- No need to manage IAM users

**Setup**:
1. Create IAM role in your account
2. Trust policy allows vendor's AWS account
3. Include External ID for security
4. Vendor assumes role using STS AssumeRole

**Trust Policy with External ID**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::VENDOR-ACCOUNT-ID:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "unique-external-id-123"
        }
      }
    }
  ]
}
```

**References:** Cross-Account Access, External ID, Confused Deputy Problem
</details>

---

### Question 17
What is the default effect when no IAM policy explicitly allows or denies an action?

A. Allow  
B. Deny  
C. Prompt for approval  
D. Log the action  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- IAM uses **implicit deny** by default
- All actions denied unless explicitly allowed
- **Evaluation Logic**: Explicit Deny → Allow → Implicit Deny
- Cannot override explicit Deny with Allow
- Must have explicit Allow to perform action

**Policy Evaluation Flow**:
1. Deny evaluation: If any policy has explicit Deny → DENY
2. Organizations SCPs: Applied as permission boundary
3. Resource-based policies: Evaluated
4. Identity-based policies: If any has Allow → ALLOW
5. IAM permissions boundaries: Applied as filter
6. Session policies: Applied for assumed roles
7. Default: DENY (if no explicit Allow)

**References:** IAM Policy Evaluation Logic
</details>

---

### Question 18
A company wants to grant temporary access to S3 objects for unauthenticated users for 1 hour. What should be used?

A. IAM user credentials  
B. S3 pre-signed URLs  
C. S3 bucket policy  
D. IAM role  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Pre-signed URLs grant time-limited access to S3 objects
- No AWS credentials needed by end user
- URL contains authentication information
- Expires after specified duration

**Generate Pre-signed URL (AWS CLI)**:
```bash
aws s3 presign s3://my-bucket/object.pdf --expires-in 3600
```

**Use Cases**:
- Temporary download links
- Upload forms for unauthenticated users
- Sharing private content without making public
- Time-limited access to resources

- Option A: Requires creating users, not for temporary/anonymous
- Option C: Bucket policies are not time-limited
- Option D: Roles require authentication

**References:** S3 Pre-signed URLs, Temporary Access
</details>

---

### Question 19
What is the purpose of IAM permissions boundaries?

A. To set maximum permissions an IAM entity can have  
B. To grant additional permissions beyond policies  
C. To replace IAM policies  
D. To encrypt IAM credentials  

<details>
<summary>Show Answer</summary>

**Answer: A**

**Explanation:**
- Permissions boundaries set maximum permissions limit
- Cannot grant more permissions than boundary allows
- Even if identity policy allows, boundary can restrict
- **Use Case**: Delegate permission management safely

**Example Scenario**:
- Set permissions boundary on developers
- Developers can create IAM roles for Lambda
- But those roles cannot exceed boundary permissions
- Prevents privilege escalation

**Effective Permissions** = Identity Policy ∩ Permissions Boundary

```json
// Permissions Boundary
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:*",
        "lambda:*"
      ],
      "Resource": "*"
    }
  ]
}
```

Even if identity policy allows IAM actions, boundary prevents it.

**References:** IAM Permissions Boundaries, Delegated Administration
</details>

---

### Question 20
Which of the following actions require MFA for the root account according to AWS best practices? (Choose TWO)

A. Logging into AWS Console  
B. Changing account settings  
C. Launching EC2 instances  
D. Deleting S3 buckets  
E. Viewing billing information  

<details>
<summary>Show Answer</summary>

**Answer: A, B**

**Explanation:**
- AWS best practices: Enable MFA on root account immediately
- Root account should be protected with MFA
- MFA required for sensitive operations
- Some actions like changing account settings require root + MFA

**Root Account Best Practices**:
1. ✅ Enable MFA on root account
2. ✅ Don't use root for everyday tasks
3. ✅ Delete root access keys (use IAM users instead)
4. ✅ Create IAM users for administrative tasks
5. ✅ Use root only for tasks requiring root
6. ✅ Secure root credentials (password manager)

**Tasks Requiring Root Account**:
- Change account settings
- Close AWS account
- Change AWS Support plan
- Restore IAM user permissions
- Register as seller in Reserved Instance Marketplace
- Configure S3 bucket for MFA Delete
- Sign up for GovCloud

**References:** Root Account Best Practices, MFA, AWS Account Security
</details>

---

## Summary

**Total Questions**: 20  
**Topics Covered**:
- IAM Roles and Temporary Credentials (STS)
- IAM Policies (Identity-based, Resource-based, Conditions)
- Multi-Factor Authentication (MFA)
- Cross-Account Access and External ID
- Identity Federation (SAML 2.0)
- Service Control Policies (SCPs)
- IAM Best Practices
- Permissions Boundaries
- Pre-signed URLs
- Root Account Security

**Exam Tips**:
1. **Always prefer IAM roles over access keys** for AWS services
2. **Use STS** for temporary credentials
3. **Policy Evaluation**: Explicit Deny > Allow > Implicit Deny
4. **Root account**: Enable MFA, don't use for daily tasks
5. **Federation**: Use existing corporate credentials
6. **Cross-account**: Use roles with external ID for third parties
7. **Permissions boundaries**: Set maximum permissions cap
8. **Groups limit**: User can belong to max 10 groups
9. **Pre-signed URLs**: Temporary access for unauthenticated users
10. **Principle of least privilege**: Grant minimum permissions needed

**Common Exam Scenarios**:
- EC2 accessing S3 → Use IAM role
- Temporary external access → STS with IAM role
- Corporate SSO → SAML 2.0 federation
- Third-party vendor → Cross-account role with External ID
- Time-limited anonymous access → Pre-signed URLs
- Restrict actions → IAM policy conditions
- Multi-account governance → AWS Organizations with SCPs

**Next Steps**:
- Review IAM policy evaluation logic
- Practice writing IAM policies with conditions
- Understand difference between identity-based and resource-based policies
- Study cross-account access patterns
- Review AWS security best practices

