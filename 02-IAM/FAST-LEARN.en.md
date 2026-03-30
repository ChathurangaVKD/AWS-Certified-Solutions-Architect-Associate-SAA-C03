# ⚡ Fast Learning - IAM (Identity & Access Management)

> **Time to Complete**: 45-60 minutes | **Exam Weight**: ~15-20%

## 🎯 Must-Know Concepts (5 Minutes)

### The IAM Trinity (UPGR)
```
USERS → GROUPS → POLICIES → ROLES
People   Collections   Permissions   Services
```

**Memory Aid**: "U Go Play Rugby" = Users, Groups, Policies, Roles

### Golden Rules
1. **Root user** = Never use for daily tasks
2. **IAM users** = People & applications
3. **Roles** = AWS services & temporary access
4. **Policies** = JSON documents defining permissions
5. **Groups** = Organize users, apply policies

## 📊 Quick Reference Tables

### IAM Components at a Glance
| Component | Who/What | Credentials | Best For |
|-----------|----------|-------------|----------|
| **Users** | People/Apps | Long-term | Individual access |
| **Groups** | User collections | None | Organize by job function |
| **Roles** | AWS services | Temporary | EC2, Lambda, cross-account |
| **Policies** | JSON rules | None | Define permissions |

### Policy Types (MIIR)
| Type | Scope | Use Case |
|------|-------|----------|
| **M**anaged - AWS | Pre-built by AWS | Common permissions |
| **M**anaged - Customer | You create & reuse | Custom reusable |
| **I**nline | Attached to 1 entity | 1:1 strict relationship |
| **I**dentity-based | Users/Groups/Roles | Who can do what |
| **R**esource-based | Resources (S3, etc) | Who can access this |

## 🔥 Exam Hot Topics

### 1. IAM Policy Structure (VESPARC)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow/Deny",
    "Principal": "who",
    "Action": "service:operation",
    "Resource": "arn:aws:service:region:account:resource",
    "Condition": "optional conditions"
  }]
}
```

**Memory Aid**: **V**ery **E**ffective **S**tatements **P**rovide **A**ctions on **R**esources with **C**onditions

### 2. Explicit Deny Wins!
```
Decision Flow:
1. Default = DENY
2. Check for explicit DENY → If yes, DENY (stop here)
3. Check for explicit ALLOW → If yes, ALLOW
4. If no ALLOW found → DENY
```

**Rule**: Explicit DENY > Explicit ALLOW > Default DENY

### 3. Cross-Account Access
```
Account A                    Account B
├── User needs access   →   ├── Resource (S3)
└── Assume Role         →   └── Trust Policy
```

**Steps**: Create role in Account B → Add trust policy → User assumes role

## 💡 Common Exam Scenarios

### Scenario 1: Grant EC2 Access to S3
**Question**: EC2 instance needs to access S3 bucket
**❌ WRONG**: Store credentials on EC2
**✅ CORRECT**: Create IAM role, attach to EC2 instance

### Scenario 2: Temporary Access for Third Party
**Question**: External auditor needs temporary access
**✅ CORRECT**: Use IAM role with trust policy, provide temporary credentials

### Scenario 3: Restrict by IP Address
**Question**: Allow S3 access only from office IP
**✅ CORRECT**: Use Condition with `aws:SourceIp`

```json
"Condition": {
  "IpAddress": {
    "aws:SourceIp": "203.0.113.0/24"
  }
}
```

### Scenario 4: MFA for Sensitive Operations
**Question**: Require MFA to delete S3 objects
**✅ CORRECT**: Use Condition with `aws:MultiFactorAuthPresent`

## 🎓 Speed Learning Tips

### 1-Minute Drill
- **Users** = Long-term credentials
- **Roles** = Temporary credentials
- **Groups** = Cannot be nested (no groups in groups)
- **Policies** = JSON permissions documents
- **IAM** = Global service (not regional)

### MFA Options (VHAS)
| Type | Example | Use Case |
|------|---------|----------|
| **V**irtual | Google Authenticator | Most common |
| **H**ardware | YubiKey | High security |
| **A**WS | AWS device | AWS-specific |
| **S**MS | Text message | Deprecated (not recommended) |

### Access Types
```
1. CONSOLE ACCESS
   └── Username + Password (+ MFA)

2. PROGRAMMATIC ACCESS
   └── Access Key ID + Secret Access Key
```

## 📝 Rapid-Fire Facts

### IAM Best Practices (Top 10)
1. ✅ Enable MFA for root account
2. ✅ Never use root for daily tasks
3. ✅ Create individual IAM users
4. ✅ Use groups to assign permissions
5. ✅ Grant least privilege
6. ✅ Use roles for EC2/Lambda
7. ✅ Rotate credentials regularly
8. ✅ Use strong password policy
9. ✅ Monitor with CloudTrail
10. ✅ Remove unnecessary credentials

### Important Limits
- Max **5,000 users** per account
- Max **300 groups** per account
- User can be in max **10 groups**
- Max **2 access keys** per user
- Max **10 managed policies** per user/group/role

### Policy Evaluation Logic
```
1. Start with DENY (default)
2. Evaluate all policies
3. Explicit DENY? → DENY immediately
4. Explicit ALLOW? → ALLOW
5. No ALLOW? → DENY
```

## 🔐 Security Features Quick Guide

### Password Policy Components
- Minimum length
- Require uppercase
- Require lowercase
- Require numbers
- Require symbols
- Password expiration
- Prevent reuse

### Access Keys Best Practices
- Never commit to code repositories
- Rotate every 90 days
- Delete if not used
- Use IAM roles instead when possible

## 🚀 5-Minute Master Review

### The IAM Cheat Sheet
1. **Users**: Permanent credentials, max 2 access keys
2. **Groups**: Organize users, can't nest, no credentials
3. **Roles**: Temporary credentials, for services & cross-account
4. **Policies**: JSON permissions, explicit deny wins
5. **Root**: Enable MFA, lock away, never use daily
6. **Service**: Global (not regional), free
7. **Best Practice**: Least privilege always

### Common Mistakes to Avoid
❌ Using root account for daily tasks
❌ Embedding credentials in code
❌ Creating access keys when role would work
❌ Granting broad permissions (use least privilege)
❌ Forgetting to rotate credentials
❌ Not enabling MFA on privileged accounts
❌ Thinking groups can contain groups (they can't!)

## 🎯 Exam Practice Speedrun

**Policy Decision Questions** (Answers at bottom)

1. User has ALLOW in identity policy, DENY in resource policy. Result? __
2. No explicit policies attached to user. Result? __
3. Best way to give EC2 access to DynamoDB? __
4. Can groups be nested? __
5. IAM is regional or global? __
6. Maximum access keys per user? __

---

### Must-Memorize Policy Conditions

| Condition | Purpose | Example Use |
|-----------|---------|-------------|
| `aws:SourceIp` | IP restriction | Office-only access |
| `aws:MultiFactorAuthPresent` | Require MFA | Sensitive operations |
| `aws:CurrentTime` | Time-based | Business hours only |
| `aws:SecureTransport` | Force HTTPS | Secure connections |
| `aws:userid` | Specific user | User-specific access |

## ⏱️ Next Steps
- Time spent: ~45-60 min
- Practice: Write sample policies
- Ready for: IAM practice questions
- Move to: Module 03 - Compute

---

**Quick Answers**: 
1) DENY (explicit deny wins)
2) DENY (default)
3) IAM Role attached to EC2
4) No
5) Global
6) 2

