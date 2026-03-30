# ⚡ Fast Learning - Networking & Content Delivery

> **完了時間**: 75-90 分 | **試験配点**: ~20-25%

## 🎯 必須理解コンセプト（5分）

### Networking Foundation (VPC-SING)
```
VPC → Virtual Private Cloud (your private network)
SUBNETS → Divide VPC into segments (public/private)
INTERNET GATEWAY → Connect to internet
NAT GATEWAY → Private subnet outbound internet
ROUTE TABLES → Traffic routing rules
SECURITY GROUPS → Instance-level firewall (stateful)
NACLs → Subnet-level firewall (stateless)
```

**記憶法**: "VPC Secures Internet Networks グローバルly"

## 📊 クイックリファレンステーブル

### VPC Components 早見表
| Component | Level | State | デフォルト | Allow/Deny |
|-----------|-------|-------|---------|------------|
| **Security Group** | Instance | Stateful | Deny all inbound | Allow のみ |
| **NACL** | Subnet | Stateless | Allow all | Allow & Deny |
| **Route Table** | Subnet | N/A | Local routes | Routes のみ |
| **Internet Gateway** | VPC | N/A | なしne | All traffic |
| **NAT Gateway** | AZ | N/A | なしne | Outbound のみ |

### Security Group vs NACL (Critical!)
| Feature | Security Group | NACL |
|---------|----------------|------|
| **Level** | Instance (ENI) | Subnet |
| **Rules** | Allow のみ | Allow & Deny |
| **State** | Stateful (return auto) | Stateless (need both) |
| **Order** | All evaluated | Numbered order |
| **デフォルト** | Deny inbound, allow outbound | Allow all |
| **Association** | Multiple per instance | One per subnet |

**記憶法**: "SG = Stateful Good guy (allow のみ), NACL = Stateless Number rules (allow/deny)"

## 🔥 試験頻出トピック

### 1. VPC CIDR Blocks
```
VALID RANGES: /16 to /28
Example: 10.0.0.0/16 = 65,536 IPs

PRIVATE IP RANGES (RFC 1918)
├── 10.0.0.0/8      (10.0.0.0 - 10.255.255.255)
├── 172.16.0.0/12   (172.16.0.0 - 172.31.255.255)
└── 192.168.0.0/16  (192.168.0.0 - 192.168.255.255)

RESERVED IPs (per subnet, first 4 + last 1)
10.0.0.0/24 example:
├── 10.0.0.0   - Network address
├── 10.0.0.1   - VPC router
├── 10.0.0.2   - DNS server
├── 10.0.0.3   - Future use
└── 10.0.0.255 - Broadcast (not used but reserved)
```

**Usable IPs** = Total - 5 (e.g., /24 = 256 - 5 = 251 usable)

### 2. Public vs Private Subnet
```
PUBLIC SUBNET
├── Has route to Internet Gateway (0.0.0.0/0 → IGW)
├── Instances get public IPs
├── Use: Web servers, load balancers
└── Internet accessible

PRIVATE SUBNET
├── なし direct route to Internet Gateway
├── Uses NAT Gateway for outbound internet
├── Use: Databases, app servers
└── なしt directly accessible from internet
```

**Key**: Route table determines public vs private!

### 3. VPC Connectivity Options
| Option | 用途 | Bandwidth | Cost |
|--------|----------|-----------|------|
| **Internet Gateway** | Public internet access | Unlimited | Free |
| **NAT Gateway** | Private → Internet (outbound) | 45 Gbps | $$$ |
| **VPC Peering** | Connect 2 VPCs | なし bandwidth limit | $ |
| **Transit Gateway** | Hub for multiple VPCs | 50 Gbps/attachment | $$ |
| **VPN** | On-prem to AWS (encrypted) | Up to 1.25 Gbps | $ |
| **Direct Connect** | Dedicated on-prem to AWS | 1-100 Gbps | $$$ |
| **PrivateLink** | Private access to services | 10 Gbps | $$ |

### 4. Route 53 Routing Policies
| Policy | 用途 | How It Works |
|--------|----------|--------------|
| **Simple** | Single resource | Returns one value |
| **Weighted** | A/B testing, gradual migration | % to each resource |
| **Latency** | Best performance | Lowest latency region |
| **Failover** | Active-passive DR | Health check based |
| **Geolocation** | Location-based content | Based on user location |
| **Geoproximity** | Traffic flow based on geography | Distance + bias |
| **Multi-value** | Multiple IPs with health checks | Returns multiple values |

## 💡 よくある試験シナリオ

### Scenario 1: EC2 Can't Access Internet
**Checklist**:
1. ✅ Is subnet public? (route to IGW)
2. ✅ Does instance have public IP?
3. ✅ Security group allows outbound?
4. ✅ NACL allows outbound + inbound return?
5. ✅ Route table has 0.0.0.0/0 → IGW?

### Scenario 2: Private Subnet Needs Internet Access
**質問**: Database in private subnet needs to download patches
**✅ 正解**: Deploy NAT Gateway in public subnet + route 0.0.0.0/0 → NAT

### Scenario 3: Connect Multiple VPCs
**質問**: 3 VPCs need to communicate
**❌ 誤り**: 3 separate VPC peering (doesn't scale)
**✅ 正解**: AWS Transit Gateway (hub and spoke)

### Scenario 4: On-Premises to AWS
**質問**: Need secure connection from data center to VPC
- **Fast setup, encrypted**: Site-to-Site VPN
- **Dedicated, high bandwidth**: Direct Connect
- **Both (redundancy)**: Direct Connect + VPN backup

### Scenario 5: Block Specific IP Address
**質問**: Need to block malicious IP from accessing resources
**❌ 誤り**: Security Group (can't deny)
**✅ 正解**: NACL (supports deny rules) or AWS WAF

### Scenario 6: Route Based on User Location
**質問**: EU users → EU resources, US users → US resources
**✅ 正解**: Route 53 Geolocation routing policy

### Scenario 7: Expose Service to Other AWS アカウントs
**質問**: Provide private access to your service for customers
**✅ 正解**: AWS PrivateLink (VPC Endpoint Service)

## 🎓 速習のコツ

### VPC Flow Logs
```
CAPTURES: IP traffic to/from ENIs
STORAGE: CloudWatch Logs or S3
LEVELS: VPC, Subnet, or ENI
USE: Troubleshooting, security analysis

Does NOT capture:
❌ Metadata (169.254.169.254)
❌ DHCP
❌ AWS DNS
❌ Windows license activation
```

### VPC Peering Rules
✅ Can peer across regions
✅ Can peer across accounts
✅ なし transitive peering (A-B-C: A can't reach C)
✅ CIDR blocks can't overlap
❌ なし overlapping CIDR
❌ なし edge-to-edge routing

### CloudFront 主要コンセプト
```
WHAT: Content Delivery Network (CDN)
WHERE: 400+ edge locations globally
USE CASES:
├── Static content (S3)
├── Dynamic content (API, video)
├── HTTPS required
└── DDoS protection (AWS Shield)

ORIGINS:
├── S3 bucket (static)
├── EC2 instance
├── ALB/ELB
├── Custom HTTP server
└── MediaPackage

SECURITY:
├── OAI (Origin Access Identity) - S3 のみ via CloudFront
├── Signed URLs/Cookies - Restrict access
├── Geo-restriction - Block countries
└── WAF - Web application firewall
```

## 📝 ラピッドファイア事実集

### Subnet CIDR Size Guide
| CIDR | Total IPs | Usable IPs | Common Use |
|------|-----------|------------|------------|
| /28 | 16 | 11 | Very small subnet |
| /27 | 32 | 27 | Small subnet |
| /26 | 64 | 59 | Medium subnet |
| /25 | 128 | 123 | Medium subnet |
| /24 | 256 | 251 | **最も一般的** |
| /20 | 4,096 | 4,091 | Large subnet |
| /16 | 65,536 | 65,531 | **最大 VPC size** |

### NAT Instance vs NAT Gateway
| Feature | NAT Gateway | NAT Instance |
|---------|-------------|--------------|
| **Managed** | AWS | You |
| **Availability** | HA in AZ | Use script for failover |
| **Bandwidth** | 45 Gbps | Instance type dependent |
| **Cost** | Higher | Lower |
| **Security Group** | N/A | Yes (manage yourself) |
| **Bastion** | なし | Can use as bastion |
| **Preferred** | ✅ Yes | ❌ 旧世代 |

### VPC Endpoint Types
```
INTERFACE ENDPOINT (PrivateLink)
├── ENI in subnet
├── Most AWS services
├── Costs per hour + data
└── Example: EC2, SNS, CloudWatch

GATEWAY ENDPOINT
├── Route table target
├── S3 and DynamoDB のみ
├── FREE!
└── Preferred for S3/DynamoDB
```

**記憶法**: "Gateway for S3 & DynamoDB = Free, Interface for everything else = Fee"

### Direct Connect
- **Speed**: 1 Gbps, 10 Gbps, 100 Gbps
- **Setup Time**: Weeks to months
- **Encryption**: なしt encrypted (use VPN over DX)
- **用途**: Consistent, high-throughput
- **Virtual Interfaces**: Public VIF, Private VIF, Transit VIF

## 🚀 5分マスターレビュー

### Networking Decision Tree
```
1. Need internet access from public subnet?
   → Internet Gateway + Public IP + Route
   
2. Need internet access from private subnet?
   → NAT Gateway (in public subnet)
   
3. Need to connect VPCs?
   2 VPCs → VPC Peering
   3+ VPCs → Transit Gateway
   
4. Need to connect on-premises?
   Quick/encrypted → VPN
   Dedicated/fast → Direct Connect
   
5. Need to block IPs?
   → NACL or AWS WAF
   
6. Need DNS routing?
   By location → Geolocation
   By latency → Latency-based
   Disaster recovery → Failover
```

### Security ベストプラクティス
✅ Use private subnets for databases
✅ Use security groups as primary firewall
✅ Use NACLs as additional layer
✅ Enable VPC Flow Logs
✅ Use VPC endpoints for AWS services
✅ Never put databases in public subnet
✅ Use NAT Gateway (not NAT Instance)
✅ Implement defense in depth

### 避けるべきよくあるミス
❌ Forgetting 5 reserved IPs per subnet
❌ Using NAT Instance instead of NAT Gateway
❌ Putting NAT Gateway in private subnet
❌ Thinking VPC peering is transitive (it's not!)
❌ Overlapping CIDR blocks for peering
❌ Only outbound rules in NACL (it's stateless!)
❌ Using Security Groups to deny (use NACL)
❌ なしt using VPC endpoints for S3/DynamoDB (costs!)

## 🎯 試験練習スピードラン

**Quick 質問s**（答えは下）

1. How many IPs reserved per subnet? __
2. Security Groups are stateful or stateless? __
3. Can Security Groups deny traffic? __
4. 最大 VPC CIDR size? __
5. Which is free: Interface or Gateway VPC endpoint? __
6. VPC peering is transitive? __
7. What provides HA NAT? __
8. Route 53 policy for DR? __

---

### グローバル Accelerator vs CloudFront
| Feature | CloudFront | グローバル Accelerator |
|---------|------------|-------------------|
| **目的** | Cache content | Route to optimal endpoint |
| **用途** | Static/dynamic content | なしn-HTTP (TCP/UDP) |
| **Caching** | Yes | なし |
| **IPs** | Changes | Static (2 Anycast) |
| **Protocols** | HTTP/HTTPS | Any (TCP/UDP) |

### Elastic IP Facts
- Static public IPv4 address
- Persists when instance stopped
- Can remap to another instance
- 最大 5 per region (soft limit)
- Charged if not attached to running instance
- Free if attached to running instance

## ⏱️ 次のステップ
- 学習時間: ~75-90分
- 演習: Create VPC, subnets, route tables, security groups
- 準備完了: Networking practice questions
- 次へ: Module 07 - Security

---

**Quick 答えs**: 
1) 5 (first 4 + last 1)
2) Stateful
3) なし (のみ allow)
4) /16 (65,536 IPs)
5) Gateway endpoint (S3/DynamoDB)
6) なし
7) NAT Gateway
8) Failover routing policy

