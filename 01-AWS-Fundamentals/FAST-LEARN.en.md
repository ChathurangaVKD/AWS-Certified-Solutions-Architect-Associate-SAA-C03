# ⚡ Fast Learning - AWS Fundamentals

> **Time to Complete**: 30-45 minutes | **Exam Weight**: ~10% foundation

## 🎯 Must-Know Concepts (5 Minutes)

### AWS Global Infrastructure - The 3 Pillars
```
REGIONS → AVAILABILITY ZONES → EDGE LOCATIONS
  30+           3-6 per region        400+
Isolated      Independent DCs      CDN endpoints
```

**Memory Aid: "RAE" = Regions, AZs, Edge**

### Key Numbers to Remember
- **Regions**: 30+ worldwide
- **AZs per Region**: Minimum 3, typically 3-6
- **Edge Locations**: 400+ (most numerous)
- **Local Zones**: Extended regions for ultra-low latency

## 📊 Quick Reference Tables

### Region Selection Criteria (CPAS)
| Factor | Question to Ask |
|--------|----------------|
| **C**ompliance | Data sovereignty laws? |
| **P**roximity | Where are users located? |
| **A**vailability | Service available here? |
| **S**pending | What's the cost? |

### Well-Architected Framework - 6 Pillars (OSCRPS)
| Pillar | Key Question | Quick Tip |
|--------|--------------|-----------|
| **O**perational Excellence | Run & monitor? | Automate everything |
| **S**ecurity | Protect data? | Defense in depth |
| **C**ost Optimization | Reduce cost? | Pay for what you use |
| **R**eliability | Recover from failures? | Multi-AZ always |
| **P**erformance Efficiency | Right resources? | Match workload |
| **S**ustainability | Minimize impact? | Optimize utilization |

## 🔥 Exam Hot Topics

### 1. Shared Responsibility Model
```
AWS RESPONSIBILITY (Security OF the cloud)
├── Physical security
├── Hardware/infrastructure
├── Network infrastructure
└── Hypervisor

CUSTOMER RESPONSIBILITY (Security IN the cloud)
├── Data encryption
├── IAM permissions
├── OS patches
├── Application security
└── Network configuration
```

**Mnemonic**: AWS = HARDWARE, You = SOFTWARE & DATA

### 2. High Availability Pattern
```
✅ CORRECT: Deploy across multiple AZs in same region
❌ WRONG: Single AZ deployment
❌ WRONG: Multiple regions for HA (that's DR, not HA)
```

### 3. AWS Management Tools - Quick Pick
| Tool | Best For | Exam Scenario |
|------|----------|---------------|
| Console | Visual, learning | One-time tasks |
| CLI | Automation, scripts | Repeatable tasks |
| SDK | Application code | Building apps |
| CloudFormation | Infrastructure as Code | Replicate environments |

## 💡 Common Exam Scenarios

### Scenario 1: Minimize Latency
**Question**: Users in Europe experience high latency
**Answer**: Deploy in EU region (eu-west-1) + use CloudFront for static content

### Scenario 2: Ensure High Availability
**Question**: Application must survive data center failure
**Answer**: Deploy across multiple AZs in same region

### Scenario 3: Disaster Recovery
**Question**: Protect against region-wide failure
**Answer**: Backup/replicate to different region

### Scenario 4: Data Compliance
**Question**: Data cannot leave country
**Answer**: Choose region in that country + verify data residency

## 🎓 Speed Learning Tips

### 1-Minute Drill
- Region = Geography (multiple buildings)
- AZ = Building (independent data center)
- Edge = Cache point (faster delivery)

### AWS Organizations - Multi-Account Management
```
STRUCTURE:
Root (Organization)
├── Management Account (pays bills, full access)
├── Production OU
│   ├── App Account
│   └── DB Account
└── Development OU
    └── Dev Accounts
```

**Key Concepts:**
- **Organizations**: Manage multiple accounts centrally
- **OUs (Organizational Units)**: Group accounts logically
- **SCPs (Service Control Policies)**: Maximum permissions guardrails
- **Consolidated Billing**: Single bill, volume discounts

### Service Control Policies (SCPs) - CRITICAL FOR EXAM
```
❌ SCPs DO NOT grant permissions
✅ SCPs set maximum permissions (guardrails)
❌ SCPs DO NOT affect management account
✅ SCPs affect all member accounts
✅ Effective permissions = IAM policy AND SCP
```

**Common SCP Use Cases:**
| Scenario | SCP Action |
|----------|------------|
| Restrict to specific regions | Deny all actions outside allowed regions |
| Require encryption | Deny creating unencrypted resources |
| Prevent leaving org | Deny organizations:LeaveOrganization |
| Protect CloudTrail | Deny deletion/modification of logs |

**SCP Quick Example:**
```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": ["us-east-1", "eu-west-1"]
    }
  }
}
```

### Control Tower vs Organizations
| Feature | Organizations | Control Tower |
|---------|---------------|---------------|
| Setup | Manual | Automated (minutes) |
| Guardrails | Manual SCPs | Pre-built + custom |
| Accounts | Manual creation | Account Factory |
| Best For | Custom/flexible | Quick/best practices |

**Exam Tip**: Control Tower = Organizations + Automation + Best Practices

### AWS Resource Access Manager (RAM)
**Purpose**: Share resources across AWS accounts

**Most Common Use**: VPC Subnet Sharing
```
Networking Account
└── VPC with Subnets
    ↓ (shared via RAM)
Application Accounts
└── Launch EC2 in shared subnets
```

**Benefits:**
- ✅ Centralized network management
- ✅ Reduced VPC sprawl
- ✅ Efficient IP usage
- ✅ No resource duplication

**Other Shareable Resources:**
- VPC Subnets (most tested)
- Transit Gateway
- Route 53 Resolver rules
- Aurora clusters
- License Manager configs

### Consolidated Billing Benefits
1. **Single Bill**: One payment for all accounts
2. **Volume Discounts**: Combined usage = better pricing
3. **RI Sharing**: Reserved Instances shared across accounts
4. **Cost Allocation**: Tags work across organization

**Example:**
```
Account 1: 500 GB S3
Account 2: 800 GB S3
Account 3: 700 GB S3
Total: 2,000 GB → Higher pricing tier applies to all
```
- Multi-AZ = High Availability
- Multi-Region = Disaster Recovery

### Common Mistakes to Avoid
❌ Confusing AZ with Region
❌ Thinking Edge Locations = Regions
❌ Deploying to single AZ for HA
❌ Assuming all services in all regions
❌ Forgetting shared responsibility boundaries

## 📝 Rapid-Fire Facts

**Global vs Regional Services:**
- **Global**: IAM, CloudFront, Route 53, WAF
- **Regional**: EC2, RDS, VPC, Lambda, S3 (global namespace)

**Service Categories (CSDMANS):**
- **C**ompute: EC2, Lambda
- **S**torage: S3, EBS, EFS
- **D**atabase: RDS, DynamoDB
- **M**onitoring: CloudWatch, CloudTrail
- **A**nalytics: Athena, EMR
- **N**etworking: VPC, Route 53
- **S**ecurity: IAM, KMS, Secrets Manager

## 🚀 5-Minute Master Review

1. **Infrastructure**: Regions → AZs → Edge Locations (largest to smallest coverage)
2. **HA Strategy**: Always use multiple AZs in same region
3. **DR Strategy**: Backup to different region
4. **Well-Architected**: 6 pillars (OSCRPS)
5. **Shared Responsibility**: AWS = infrastructure, You = data/config
6. **Region Selection**: Compliance → Proximity → Availability → Spending (CPAS)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)
1. How many AZs minimum per region? __
2. What provides low-latency CDN? __
3. Who secures the hypervisor? __
4. For HA, deploy across multiple __? 
5. IAM is global or regional? __

---

**Answers**: 1) 3  2) CloudFront/Edge Locations  3) AWS  4) AZs  5) Global

## ⏱️ Next Steps
- Time spent: ~30 min
- Ready for: Practice questions
- Move to: Module 02 - IAM

