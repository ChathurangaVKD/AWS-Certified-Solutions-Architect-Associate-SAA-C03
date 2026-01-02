# Module 02: Identity and Access Management (IAM)

## 📚 Overview

AWS Identity and Access Management (IAM) is a critical service for securely controlling access to AWS resources. This module covers IAM users, groups, roles, policies, and security best practices essential for the SAA-C03 exam.

**Exam Weight**: ~15-20% (appears in Security domain and throughout the exam)

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- ✅ Create and manage IAM users, groups, and roles
- ✅ Write and apply IAM policies using JSON
- ✅ Implement Multi-Factor Authentication (MFA)
- ✅ Understand IAM best practices and security principles
- ✅ Configure cross-account access
- ✅ Implement identity federation
- ✅ Use IAM roles for EC2 instances and services

---

## 📖 Table of Contents

1. [IAM Overview](#1-iam-overview)
2. [IAM Users](#2-iam-users)
3. [IAM Groups](#3-iam-groups)
4. [IAM Roles](#4-iam-roles)
5. [IAM Policies](#5-iam-policies)
6. [Multi-Factor Authentication (MFA)](#6-multi-factor-authentication-mfa)
7. [IAM Best Practices](#7-iam-best-practices)
8. [Identity Federation](#8-identity-federation)
9. [Exam Tips](#-exam-tips)
10. [Practice Questions](#-practice-questions)

---

## 1. IAM Overview

### 1.1 What is IAM?

**AWS Identity and Access Management** allows you to:
- Control WHO can access your AWS resources (Authentication)
- Control WHAT they can do (Authorization)
- Manage access centrally
- No additional charge (free service)

### 1.2 Key Concepts

```
┌─────────────────────────────────────────┐
│           IAM Components                │
├─────────────────────────────────────────┤
│                                         │
│  Users    →  Individual people/apps    │
│  Groups   →  Collection of users       │
│  Roles    →  Permissions for services  │
│  Policies →  Define permissions        │
│                                         │
└─────────────────────────────────────────┘
```

### 1.3 IAM Features

- **Global Service**: Not region-specific
- **Granular Permissions**: Precise control over resources
- **Temporary Credentials**: For roles and federated users
- **MFA Support**: Extra layer of security
- **Identity Federation**: Integrate with corporate directories
- **Free**: No additional cost

**Exam Tip**: 🎯 IAM is a global service - changes apply to all regions instantly.

---

## 2. IAM Users

### 2.1 What is an IAM User?

An IAM user represents a person or application that interacts with AWS.

**Characteristics:**
- Permanent credentials
- Can have console access (password)
- Can have programmatic access (access keys)
- Maximum 5,000 users per AWS account

### 2.2 Creating IAM Users

**Two Types of Access:**

1. **AWS Management Console Access**
   - Requires username and password
   - Can enable MFA
   - For human users

2. **Programmatic Access**
   - Access Key ID + Secret Access Key
   - For CLI, SDK, API calls
   - For applications and scripts

```bash
# Example: Using access keys with CLI
aws configure
AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name: us-east-1
Default output format: json
```

### 2.3 User Credentials

**Password Policy:**
- Minimum length
- Require specific character types
- Password expiration
- Prevent password reuse
- Require administrator reset

**Access Keys:**
- Each user can have max 2 active access keys
- Rotate regularly (security best practice)
- Never embed in code or commit to version control
- Use IAM roles instead when possible

**Exam Tip**: 🎯 NEVER share access keys. Use roles for EC2 instead of embedding keys.

---

## 3. IAM Groups

### 3.1 What is an IAM Group?

A collection of IAM users with shared permissions.

**Key Points:**
- Simplifies permission management
- Users can belong to multiple groups
- Groups cannot be nested (no groups within groups)
- No default group

### 3.2 Common Group Patterns

```
Organization Structure:
├── Administrators
│   ├── Full AWS access
│   └── Users: Alice, Bob
├── Developers
│   ├── EC2, S3, RDS access
│   └── Users: Charlie, Diana, Eve
├── Operators
│   ├── Read-only + CloudWatch
│   └── Users: Frank, Grace
└── Auditors
    ├── Read-only access
    └── Users: Henry, Iris
```

### 3.3 Best Practices

- ✅ Assign permissions to groups, not individual users
- ✅ Use descriptive group names (e.g., "S3-Admins", "EC2-ReadOnly")
- ✅ Review group memberships regularly
- ❌ Don't create groups for each individual user

**Exam Tip**: 🎯 Groups are for organizing users, not nesting other groups.

---

## 4. IAM Roles

### 4.1 What is an IAM Role?

A set of permissions that can be assumed by trusted entities.

**Key Differences from Users:**
- No permanent credentials
- Temporary security credentials
- Can be assumed by users, applications, or services
- Use cases: EC2 instances, Lambda functions, cross-account access

### 4.2 Role Components

**Trust Policy** (Who can assume the role):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "ec2.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
  }]
}
```

**Permissions Policy** (What they can do):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
```

### 4.3 Common Role Use Cases

**1. EC2 Instance Role:**
```
EC2 Instance → Assumes Role → Access S3/DynamoDB/etc.
```
**Benefits**: No access keys needed in application code

**2. Cross-Account Access:**
```
User in Account A → Assumes Role → Access resources in Account B
```

**3. Service-to-Service:**
```
Lambda Function → Assumes Role → Access RDS/S3/etc.
```

**4. Federated Users:**
```
Corporate User → SAML/OIDC → Assumes Role → AWS Access
```

### 4.4 EC2 Instance Roles (Instance Profiles)

```
Application on EC2:
  ↓
IAM Role attached to instance
  ↓
Temporary credentials auto-rotated
  ↓
Access AWS services securely
```

**Best Practice**: Always use IAM roles for EC2 instead of embedding access keys.

**Exam Tip**: 🎯 Roles provide temporary credentials. Perfect for EC2 and Lambda.

---

## 5. IAM Policies

### 5.1 What is an IAM Policy?

JSON documents that define permissions.

**Policy Types:**
1. **AWS Managed Policies**: Created and maintained by AWS
2. **Customer Managed Policies**: Created and maintained by you
3. **Inline Policies**: Embedded directly in a user/group/role

### 5.2 Policy Structure

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ListBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::my-bucket",
      "Condition": {
        "StringLike": {
          "s3:prefix": ["home/${aws:username}/*"]
        }
      }
    }
  ]
}
```

**Components:**
- **Version**: Policy language version (always "2012-10-17")
- **Statement**: One or more permission statements
  - **Sid**: Statement ID (optional, for readability)
  - **Effect**: "Allow" or "Deny"
  - **Action**: AWS service actions (e.g., "s3:GetObject")
  - **Resource**: ARN of resources affected
  - **Condition**: Optional conditions for when policy applies

### 5.3 Policy Examples

**Read-Only S3 Access:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::my-bucket",
      "arn:aws:s3:::my-bucket/*"
    ]
  }]
}
```

**EC2 Start/Stop Only:**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "ec2:StartInstances",
      "ec2:StopInstances"
    ],
    "Resource": "*",
    "Condition": {
      "StringEquals": {
        "ec2:ResourceTag/Environment": "Development"
      }
    }
  }]
}
```

### 5.4 Permission Evaluation Logic

```
Decision Flow:
1. By default, everything is DENIED
2. Check for explicit DENY → If yes, DENY (end)
3. Check for explicit ALLOW → If yes, ALLOW
4. If no explicit ALLOW → DENY (implicit)
```

**Key Rule**: 🔴 **Explicit DENY always wins!**

### 5.5 Policy Variables

Use variables for dynamic permissions:

```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "arn:aws:s3:::my-bucket/home/${aws:username}/*"
}
```

**Common Variables:**
- `${aws:username}` - IAM user name
- `${aws:userid}` - Unique IAM user ID
- `${aws:PrincipalAccount}` - Account ID
- `${aws:CurrentTime}` - Current date/time

**Exam Tip**: 🎯 Explicit DENY overrides all ALLOW statements.

---

## 6. Multi-Factor Authentication (MFA)

### 6.1 What is MFA?

Additional layer of security beyond password.

**Something you know** (password) + **Something you have** (MFA device)

### 6.2 MFA Device Types

**1. Virtual MFA Device:**
- Google Authenticator
- Microsoft Authenticator  
- Authy
- Most common and convenient

**2. Hardware MFA Device:**
- Gemalto token
- YubiKey
- Physical device

**3. U2F Security Key:**
- YubiKey
- Supports multiple root and IAM users

### 6.3 When to Use MFA

**Required for:**
- ✅ Root account (always!)
- ✅ IAM users with administrative access
- ✅ IAM users accessing sensitive data

**Best Practice:**
- Enable MFA for all users with console access
- Use MFA for programmatic access to sensitive operations

### 6.4 MFA with CLI

```bash
# Get temporary credentials with MFA
aws sts get-session-token \
  --serial-number arn:aws:iam::123456789012:mfa/username \
  --token-code 123456

# Returns temporary credentials valid for 12 hours
```

**Exam Tip**: 🎯 Always enable MFA on root account. It's a critical security best practice.

---

## 7. IAM Best Practices

### 7.1 Security Best Practices

1. **Lock Away Root User Credentials**
   - Enable MFA on root account
   - Don't use root for everyday tasks
   - Delete root access keys

2. **Grant Least Privilege**
   - Start with minimal permissions
   - Add permissions as needed
   - Review and remove unused permissions

3. **Use Groups to Assign Permissions**
   - Don't attach policies directly to users
   - Easier to manage at scale

4. **Use Roles for Applications**
   - Never embed access keys in code
   - Use IAM roles for EC2, Lambda, etc.

5. **Rotate Credentials Regularly**
   - Change passwords periodically
   - Rotate access keys every 90 days
   - Remove unused credentials

6. **Enable MFA**
   - Especially for privileged users
   - Root account and administrators

7. **Use Policy Conditions**
   - Restrict by IP address
   - Require MFA
   - Time-based restrictions

8. **Monitor Activity**
   - Use CloudTrail for API logging
   - Review IAM credential reports
   - Set up alerts for unusual activity

### 7.2 AWS Managed Policies to Know

| Policy Name | Description |
|-------------|-------------|
| **AdministratorAccess** | Full access to all AWS services |
| **PowerUserAccess** | Admin access except IAM |
| **ReadOnlyAccess** | Read-only access to all services |
| **IAMFullAccess** | Full access to IAM only |
| **AmazonS3ReadOnlyAccess** | Read-only access to S3 |
| **AmazonEC2FullAccess** | Full access to EC2 |

### 7.3 Principle of Least Privilege

**Bad Example** ❌:
```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```

**Good Example** ✅:
```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject"
  ],
  "Resource": "arn:aws:s3:::my-specific-bucket/folder/*"
}
```

**Exam Tip**: 🎯 Least privilege = minimum permissions needed to do the job.

---

## 8. Identity Federation

### 8.1 What is Identity Federation?

Allows users to access AWS using credentials from external identity providers.

**Benefits:**
- Single sign-on (SSO) experience
- Centralized user management
- No need to create IAM users for everyone
- Leverage existing corporate directory

### 8.2 Federation Methods

**1. SAML 2.0 Federation:**
- Corporate Active Directory
- Microsoft ADFS
- Custom SAML 2.0 providers

```
User → Corporate Login → SAML Assertion → AWS STS → Temporary Credentials
```

**2. Web Identity Federation:**
- Login with Amazon
- Login with Facebook
- Login with Google
- Sign in with Apple

**3. AWS SSO (IAM Identity Center):**
- Centralized access management
- Integrated with AWS Organizations
- Support for SAML 2.0 applications

**4. Custom Identity Broker:**
- Your own application authenticates users
- Calls AWS STS directly
- Returns temporary credentials

### 8.3 AWS STS (Security Token Service)

**Provides temporary, limited-privilege credentials:**

```bash
# Assume role
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/MyRole \
  --role-session-name my-session

# Returns:
# - AccessKeyId
# - SecretAccessKey
# - SessionToken
# - Expiration (default 1 hour, max 12 hours)
```

**Key STS APIs:**
- `AssumeRole` - Assume a role
- `AssumeRoleWithSAML` - For SAML federation
- `AssumeRoleWithWebIdentity` - For web identity federation
- `GetSessionToken` - MFA authentication
- `GetFederationToken` - For identity broker

**Exam Tip**: 🎯 Federation = external identities accessing AWS. Always uses STS for temporary credentials.

---

## 🎯 Exam Tips

### Must Know for Exam

1. **IAM Basics:**
   - Users = long-term credentials
   - Roles = temporary credentials
   - Groups = collection of users (no nesting)
   - Policies = define permissions in JSON

2. **Policy Evaluation:**
   - Default = Deny
   - Explicit Deny > Explicit Allow
   - Need explicit Allow to access

3. **Best Practices:**
   - Never use root account for daily tasks
   - Always enable MFA on root
   - Use roles for EC2 (not access keys)
   - Grant least privilege
   - Rotate credentials regularly

4. **Cross-Account Access:**
   - Use IAM roles
   - Define trust relationship
   - Switch roles in console or CLI

5. **Federation:**
   - SAML 2.0 for corporate directories
   - Web identity for social logins
   - Always uses AWS STS
   - Returns temporary credentials

### Common Exam Scenarios

**Scenario 1**: *"An application running on EC2 needs to access S3. How should credentials be provided?"*
- **Answer**: Attach an IAM role to the EC2 instance

**Scenario 2**: *"A company wants employees to access AWS using their corporate credentials."*
- **Answer**: Configure SAML 2.0 federation with corporate identity provider

**Scenario 3**: *"A policy allows S3 access, but another policy explicitly denies it. What happens?"*
- **Answer**: Access is denied (explicit deny always wins)

**Scenario 4**: *"How to grant temporary access to an external auditor?"*
- **Answer**: Create an IAM role with required permissions, auditor assumes the role

### Exam Keywords Mapping

| Keyword | Think This |
|---------|------------|
| "Temporary credentials" | IAM Role / STS |
| "Corporate directory" | SAML 2.0 Federation |
| "Social login" | Web Identity Federation |
| "EC2 needs access" | IAM Role (Instance Profile) |
| "Cross-account" | IAM Role with trust policy |
| "Least privilege" | Minimal permissions needed |
| "MFA" | Extra security layer |

---

## 📝 Practice Questions

### Question 1
**An application running on an EC2 instance needs to access objects in an S3 bucket. What is the MOST secure way to grant access?**

A) Store AWS credentials in the application code  
B) Create an IAM user and share the access keys  
C) Attach an IAM role to the EC2 instance  
D) Make the S3 bucket publicly accessible

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: Attaching an IAM role to EC2 is the most secure method. It provides temporary credentials that are automatically rotated, and credentials don't need to be stored in code.
</details>

### Question 2
**A company wants to enforce that all API calls to S3 must be authenticated with MFA. Which IAM feature should be used?**

A) IAM Groups  
B) IAM Policy Conditions  
C) IAM Access Analyzer  
D) Service Control Policies

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation**: IAM policy conditions can enforce MFA. Example condition: `"aws:MultiFactorAuthPresent": "true"`
</details>

### Question 3
**What happens when an IAM policy explicitly denies an action, but another policy explicitly allows the same action?**

A) The action is allowed  
B) The action is denied  
C) The policies conflict and fail  
D) The newer policy takes precedence

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation**: Explicit deny always overrides explicit allow. This is a fundamental rule of IAM policy evaluation.
</details>

### Question 4
**A company needs to allow employees to access AWS using their existing corporate Active Directory credentials. What should they implement?**

A) Create IAM users for each employee  
B) Use Web Identity Federation  
C) Configure SAML 2.0 federation  
D) Share the root account credentials

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: SAML 2.0 federation allows users to authenticate with corporate Active Directory and access AWS with temporary credentials via STS.
</details>

### Question 5
**Which IAM entity can be used to define permissions but cannot have permissions attached directly to it?**

A) IAM User  
B) IAM Group  
C) IAM Role  
D) IAM Policy

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation**: IAM groups are used to organize users and assign permissions, but policies are attached to the group, not permissions directly. Also, groups cannot be nested.
</details>

### Question 6
**A solutions architect needs to provide an external company temporary access to an S3 bucket for 7 days. What is the BEST approach?**

A) Create an IAM user with an access key  
B) Make the S3 bucket public  
C) Create an IAM role and share the assume role credentials  
D) Share the AWS account password

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation**: IAM roles can be assumed by external entities using trust policies. The external company can assume the role to get temporary credentials. After 7 days, you can remove the role or modify the trust policy.
</details>

---

## 🔗 Additional Resources

### AWS Official Documentation
- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [STS API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/)

### Hands-On Labs
1. **Create IAM Users and Groups**: Set up a group structure for your organization
2. **Write Custom IAM Policies**: Create least-privilege policies for specific use cases
3. **Attach Role to EC2**: Launch EC2 with IAM role and access S3
4. **Enable MFA**: Enable virtual MFA device on your IAM user
5. **Cross-Account Access**: Set up role assumption between two accounts

### Next Steps
- ✅ Complete this module
- ➡️ **Next**: [Module 03: Compute Services](../03-Compute/README.md)
- ⬅️ **Previous**: [Module 01: AWS Fundamentals](../01-AWS-Fundamentals/README.md)

---

**Module Progress**: 🎯 IAM Mastered  
**Estimated Study Time**: 6-8 hours  
**Difficulty**: ⭐⭐ Intermediate

---

[⬅️ Back to Main README](../README.md) | [Next Module: Compute ➡️](../03-Compute/README.md)

