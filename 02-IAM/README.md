# Module 02: Identity and Access Management (IAM)

## Overview
IAM is a foundational service for securing your AWS environment. It controls authentication and authorization for AWS resources.

## Learning Objectives
- Understand IAM users, groups, roles, and policies
- Implement least privilege access
- Configure Multi-Factor Authentication (MFA)
- Work with IAM policies
- Understand identity federation

---

## 1. IAM Core Components

### IAM Users
- **Individual identity** with unique credentials
- Used by people or applications
- Long-term credentials (password and/or access keys)
- Maximum **5,000 users per AWS account**
- Best Practice: Create individual users, don't share credentials

### IAM Groups
- **Collection of IAM users**
- Permissions assigned to group apply to all members
- Users can belong to **multiple groups** (up to 10)
- Groups **cannot be nested**
- Best Practice: Assign permissions to groups, not individual users

### IAM Roles
- **Temporary credentials** for AWS services or users
- No permanent credentials (password/access keys)
- **AssumeRole** API to obtain temporary credentials
- Use cases:
  - EC2 instance accessing S3
  - Cross-account access
  - Federation (SAML, OIDC)
  - AWS service-to-service access

### IAM Policies
- **JSON documents** that define permissions
- Attached to users, groups, or roles
- Types:
  - **Identity-based policies**: Attached to identities
  - **Resource-based policies**: Attached to resources (S3 buckets, SQS queues)
  - **AWS managed policies**: Created and maintained by AWS
  - **Customer managed policies**: Created and maintained by you
  - **Inline policies**: Embedded directly in a user, group, or role

---

## 2. IAM Policy Structure

### Policy Document Example
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadAccess",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

### Policy Elements

| Element | Description | Required |
|---------|-------------|----------|
| **Version** | Policy language version (use "2012-10-17") | Yes |
| **Statement** | Array of individual statements | Yes |
| **Sid** | Statement ID (optional identifier) | No |
| **Effect** | "Allow" or "Deny" | Yes |
| **Principal** | Account/user/role to which policy applies | Sometimes |
| **Action** | List of actions (e.g., "s3:GetObject") | Yes |
| **Resource** | ARN of resources the action applies to | Yes |
| **Condition** | Conditions for when policy is in effect | No |

### Policy Evaluation Logic

```
By default: Implicit Deny
↓
Explicit Deny? → DENY (stops here)
↓
Explicit Allow? → ALLOW
↓
Otherwise → DENY
```

**Key Rule**: **Explicit DENY always wins**

---

## 3. IAM Best Practices

### Security Best Practices

1. **Enable MFA for privileged users**
   - Virtual MFA devices (Google Authenticator, Authy)
   - Hardware MFA devices (YubiKey, Gemalto)
   - SMS text message (not recommended for root)

2. **Use roles instead of access keys**
   - For EC2 instances: Use instance roles
   - For applications: Use service roles
   - For cross-account access: Use cross-account roles

3. **Apply least privilege principle**
   - Grant only necessary permissions
   - Start with minimum and add as needed
   - Use IAM Access Analyzer

4. **Rotate credentials regularly**
   - Password policy for users
   - Rotate access keys
   - Use AWS Secrets Manager for application credentials

5. **Use policy conditions for extra security**
   - Restrict by IP address
   - Require MFA
   - Restrict by time
   - Require SSL/TLS

6. **Monitor IAM activity**
   - Enable CloudTrail
   - Review IAM Credential Report
   - Use IAM Access Advisor

---

## 4. IAM Policies in Detail

### AWS Managed Policies
Pre-built policies maintained by AWS
- **AdministratorAccess**: Full access to all AWS services
- **PowerUserAccess**: Admin access except IAM
- **ReadOnlyAccess**: Read-only access to all services
- **Billing**: Access to billing console

### Customer Managed Policies
Custom policies you create
- Reusable across multiple users/groups/roles
- Version controlled (up to 5 versions)
- Maximum size: 6,144 characters

### Inline Policies
Directly embedded in user/group/role
- One-to-one relationship
- Deleted when the identity is deleted
- Use for strict one-to-one relationship requirements

### Permission Boundaries
- Advanced feature to set **maximum permissions**
- Does NOT grant permissions itself
- Used with IAM users and roles
- Useful for delegating permission management

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:*",
        "rds:*"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 5. IAM Roles Deep Dive

### EC2 Instance Roles
- Attach IAM role to EC2 instance
- Temporary credentials automatically rotated
- Applications use AWS SDK/CLI without hardcoded credentials

```bash
# No need to configure credentials on EC2
# AWS SDK automatically uses instance role
aws s3 ls
```

### Service Roles
- Allow AWS services to perform actions on your behalf
- Example: Lambda execution role, ECS task role

### Cross-Account Roles
- Allow access from one AWS account to another
- Trust policy defines which accounts can assume the role

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

---

## 6. IAM Security Tools

### IAM Credentials Report (Account-level)
- Lists all users and credential status
- Password age, MFA status, access key age
- Downloaded as CSV
- Generated on-demand

### IAM Access Advisor (User-level)
- Shows service permissions granted to user
- Shows when services were last accessed
- Use to implement least privilege

### IAM Access Analyzer
- Identifies resources shared with external entities
- Analyzes resource policies (S3, KMS, SQS, etc.)
- Generates findings for public or cross-account access
- Validates policies against AWS best practices

### IAM Policy Simulator
- Test and troubleshoot IAM policies
- Simulate API calls without making actual requests
- Available in console and via API

---

## 7. Identity Federation

### What is Identity Federation?
Allow users to access AWS using existing corporate credentials

### Federation Options

#### 1. SAML 2.0 Federation
- Integrate with Microsoft Active Directory, ADFS
- Enterprise identity providers
- Single Sign-On (SSO) to AWS Console
- Temporary credentials via STS

#### 2. Custom Identity Broker
- When identity provider is not compatible with SAML 2.0
- Broker determines authentication and returns credentials
- Uses STS AssumeRole or GetFederationToken

#### 3. Web Identity Federation
- Let users sign in via Amazon, Facebook, Google
- Use Amazon Cognito (recommended)
- For mobile and web applications

#### 4. AWS Single Sign-On (AWS SSO)
- Centrally manage SSO access to multiple AWS accounts
- Integrated with AWS Organizations
- Support for SAML 2.0 identity providers
- Built-in IdP or connect to external IdP

#### 5. AWS Directory Service
- **AWS Managed Microsoft AD**: Full Microsoft AD in AWS
- **AD Connector**: Proxy to on-premises AD
- **Simple AD**: Standalone directory powered by Samba 4

---

## 8. IAM with AWS Organizations

### Service Control Policies (SCPs)
- Define maximum permissions for accounts
- Applied at Organization, OU, or account level
- Does NOT grant permissions
- Affects all users and roles, including root
- Does NOT affect service-linked roles

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "ec2:Region": ["us-east-1", "us-west-2"]
        }
      }
    }
  ]
}
```

---

## 9. IAM Advanced Features

### IAM Conditions
Provide fine-grained access control

**Common Condition Keys**:
- `aws:SourceIp`: Restrict by IP address
- `aws:RequestedRegion`: Restrict by region
- `aws:MultiFactorAuthPresent`: Require MFA
- `aws:SecureTransport`: Require HTTPS
- `aws:CurrentTime`: Time-based restrictions

```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*",
  "Condition": {
    "Bool": {
      "aws:MultiFactorAuthPresent": "true"
    }
  }
}
```

### Resource Tags in Policies
- Use tags to control access
- Attribute-Based Access Control (ABAC)

```json
{
  "Effect": "Allow",
  "Action": "ec2:StartInstance",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "ec2:ResourceTag/Owner": "${aws:username}"
    }
  }
}
```

---

## 10. IAM Limits and Quotas

| Resource | Default Limit |
|----------|---------------|
| Users per account | 5,000 |
| Groups per account | 300 |
| Roles per account | 1,000 |
| Policies per user/group/role | 10 managed policies |
| Customer managed policies per account | 1,500 |
| Policy size | 2,048 characters (inline), 6,144 (managed) |
| Groups per user | 10 |
| Access keys per user | 2 |

---

## Practice Questions

1. **Which IAM entity should be used to give an EC2 instance permissions to access S3?**
   - A. IAM User
   - B. IAM Group
   - C. IAM Role
   - D. IAM Policy
   
   **Answer**: C (IAM Role - specifically an instance role)

2. **What happens when an explicit Deny and an explicit Allow conflict in IAM policies?**
   - A. Allow takes precedence
   - B. Deny takes precedence
   - C. The first statement wins
   - D. An error is generated
   
   **Answer**: B (Explicit Deny always wins)

3. **Which IAM security tool shows the last time a service was accessed?**
   - A. IAM Credentials Report
   - B. IAM Access Advisor
   - C. IAM Policy Simulator
   - D. IAM Access Analyzer
   
   **Answer**: B

4. **What is the maximum number of groups an IAM user can belong to?**
   - A. 5
   - B. 10
   - C. 20
   - D. Unlimited
   
   **Answer**: B

---

## Hands-On Labs

### Lab 1: Create IAM Users and Groups
1. Create three IAM users (dev1, dev2, admin1)
2. Create two groups (Developers, Administrators)
3. Assign AWS managed policies to groups
4. Add users to appropriate groups
5. Test permissions by logging in as different users

### Lab 2: Create Custom IAM Policy
1. Create a custom policy that allows:
   - Read-only access to S3
   - Full access to EC2 in us-east-1 only
2. Attach policy to a test user
3. Use Policy Simulator to test

### Lab 3: Configure MFA
1. Enable virtual MFA for root user
2. Enable MFA for IAM users
3. Create policy requiring MFA for sensitive actions

### Lab 4: IAM Roles for EC2
1. Create an IAM role with S3 read access
2. Launch EC2 instance with this role
3. SSH into instance and verify S3 access without credentials

### Lab 5: Cross-Account Access
1. Create a role in Account A
2. Configure trust policy for Account B
3. Assume role from Account B to access resources in Account A

---

## Security Checklist

- [ ] Root account MFA is enabled
- [ ] Root account is not used for daily tasks
- [ ] Individual IAM users created for each person
- [ ] Strong password policy configured
- [ ] MFA enabled for privileged users
- [ ] Least privilege principle applied
- [ ] IAM roles used instead of access keys where possible
- [ ] Access keys rotated regularly
- [ ] Unnecessary credentials removed
- [ ] CloudTrail logging enabled
- [ ] IAM Access Analyzer enabled
- [ ] Regular IAM Credentials Report review

---

## Key Takeaways

✅ IAM is global (not region-specific)  
✅ Root user should be secured with MFA and not used for daily tasks  
✅ Use IAM roles for EC2 instances and AWS services  
✅ Explicit DENY always overrides ALLOW  
✅ Follow the principle of least privilege  
✅ Use groups to assign permissions to users  
✅ Enable MFA for privileged users  
✅ Regularly review permissions using IAM tools  
✅ Use federation for enterprise environments  
✅ Service Control Policies (SCPs) set maximum permissions in Organizations  

---

## Additional Resources

- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [IAM Policy Simulator](https://policysim.aws.amazon.com/)
- [IAM JSON Policy Elements Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)

---

**Previous Module**: [Module 01: AWS Fundamentals](../01-AWS-Fundamentals/README.md)  
**Next Module**: [Module 03: Compute Services](../03-Compute/README.md)

