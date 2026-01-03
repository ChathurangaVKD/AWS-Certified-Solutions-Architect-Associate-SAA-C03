# ⚡ Fast Learning - Networking & Content Delivery

> **Time to Complete**: 75-90 minutes | **Exam Weight**: ~20-25%

## 🎯 Must-Know Concepts (5 Minutes)

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

**Memory Aid**: "VPC Secures Internet Networks Globally"

## 📊 Quick Reference Tables

### VPC Components Quick Matrix
| Component | Level | State | Default | Allow/Deny |
|-----------|-------|-------|---------|------------|
| **Security Group** | Instance | Stateful | Deny all inbound | Allow only |
| **NACL** | Subnet | Stateless | Allow all | Allow & Deny |
| **Route Table** | Subnet | N/A | Local routes | Routes only |
| **Internet Gateway** | VPC | N/A | None | All traffic |
| **NAT Gateway** | AZ | N/A | None | Outbound only |

### Security Group vs NACL (Critical!)
| Feature | Security Group | NACL |
|---------|----------------|------|
| **Level** | Instance (ENI) | Subnet |
| **Rules** | Allow only | Allow & Deny |
| **State** | Stateful (return auto) | Stateless (need both) |
| **Order** | All evaluated | Numbered order |
| **Default** | Deny inbound, allow outbound | Allow all |
| **Association** | Multiple per instance | One per subnet |

**Memory Aid**: "SG = Stateful Good guy (allow only), NACL = Stateless Number rules (allow/deny)"

## 🔥 Exam Hot Topics

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
├── No direct route to Internet Gateway
├── Uses NAT Gateway for outbound internet
├── Use: Databases, app servers
└── Not directly accessible from internet
```

**Key**: Route table determines public vs private!

### 3. VPC Connectivity Options
| Option | Use Case | Bandwidth | Cost |
|--------|----------|-----------|------|
| **Internet Gateway** | Public internet access | Unlimited | Free |
| **NAT Gateway** | Private → Internet (outbound) | 45 Gbps | $$$ |
| **VPC Peering** | Connect 2 VPCs | No bandwidth limit | $ |
| **Transit Gateway** | Hub for multiple VPCs | 50 Gbps/attachment | $$ |
| **VPN** | On-prem to AWS (encrypted) | Up to 1.25 Gbps | $ |
| **Direct Connect** | Dedicated on-prem to AWS | 1-100 Gbps | $$$ |
| **PrivateLink** | Private access to services | 10 Gbps | $$ |

### 4. Route 53 Routing Policies
| Policy | Use Case | How It Works |
|--------|----------|--------------|
| **Simple** | Single resource | Returns one value |
| **Weighted** | A/B testing, gradual migration | % to each resource |
| **Latency** | Best performance | Lowest latency region |
| **Failover** | Active-passive DR | Health check based |
| **Geolocation** | Location-based content | Based on user location |
| **Geoproximity** | Traffic flow based on geography | Distance + bias |
| **Multi-value** | Multiple IPs with health checks | Returns multiple values |

## 💡 Common Exam Scenarios

### Scenario 1: EC2 Can't Access Internet
**Checklist**:
1. ✅ Is subnet public? (route to IGW)
2. ✅ Does instance have public IP?
3. ✅ Security group allows outbound?
4. ✅ NACL allows outbound + inbound return?
5. ✅ Route table has 0.0.0.0/0 → IGW?

### Scenario 2: Private Subnet Needs Internet Access
**Q**: Database in private subnet needs to download patches
**✅ ANSWER**: Deploy NAT Gateway in public subnet + route 0.0.0.0/0 → NAT

### Scenario 3: Connect Multiple VPCs
**Q**: 3 VPCs need to communicate
**❌ WRONG**: 3 separate VPC peering (doesn't scale)
**✅ CORRECT**: AWS Transit Gateway (hub and spoke)

### Scenario 4: On-Premises to AWS
**Q**: Need secure connection from data center to VPC
- **Fast setup, encrypted**: Site-to-Site VPN
- **Dedicated, high bandwidth**: Direct Connect
- **Both (redundancy)**: Direct Connect + VPN backup

### Scenario 5: Block Specific IP Address
**Q**: Need to block malicious IP from accessing resources
**❌ WRONG**: Security Group (can't deny)
**✅ CORRECT**: NACL (supports deny rules) or AWS WAF

### Scenario 6: Route Based on User Location
**Q**: EU users → EU resources, US users → US resources
**✅ ANSWER**: Route 53 Geolocation routing policy

### Scenario 7: Expose Service to Other AWS Accounts
**Q**: Provide private access to your service for customers
**✅ ANSWER**: AWS PrivateLink (VPC Endpoint Service)

## 🎓 Speed Learning Tips

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
✅ No transitive peering (A-B-C: A can't reach C)
✅ CIDR blocks can't overlap
❌ No overlapping CIDR
❌ No edge-to-edge routing

### CloudFront Key Concepts
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
├── OAI (Origin Access Identity) - S3 only via CloudFront
├── Signed URLs/Cookies - Restrict access
├── Geo-restriction - Block countries
└── WAF - Web application firewall
```

## 📝 Rapid-Fire Facts

### Subnet CIDR Size Guide
| CIDR | Total IPs | Usable IPs | Common Use |
|------|-----------|------------|------------|
| /28 | 16 | 11 | Very small subnet |
| /27 | 32 | 27 | Small subnet |
| /26 | 64 | 59 | Medium subnet |
| /25 | 128 | 123 | Medium subnet |
| /24 | 256 | 251 | **Most common** |
| /20 | 4,096 | 4,091 | Large subnet |
| /16 | 65,536 | 65,531 | **Max VPC size** |

### NAT Instance vs NAT Gateway
| Feature | NAT Gateway | NAT Instance |
|---------|-------------|--------------|
| **Managed** | AWS | You |
| **Availability** | HA in AZ | Use script for failover |
| **Bandwidth** | 45 Gbps | Instance type dependent |
| **Cost** | Higher | Lower |
| **Security Group** | N/A | Yes (manage yourself) |
| **Bastion** | No | Can use as bastion |
| **Preferred** | ✅ Yes | ❌ Legacy |

### VPC Endpoint Types
```
INTERFACE ENDPOINT (PrivateLink)
├── ENI in subnet
├── Most AWS services
├── Costs per hour + data
└── Example: EC2, SNS, CloudWatch

GATEWAY ENDPOINT
├── Route table target
├── S3 and DynamoDB only
├── FREE!
└── Preferred for S3/DynamoDB
```

**Memory Aid**: "Gateway for S3 & DynamoDB = Free, Interface for everything else = Fee"

### Direct Connect
- **Speed**: 1 Gbps, 10 Gbps, 100 Gbps
- **Setup Time**: Weeks to months
- **Encryption**: Not encrypted (use VPN over DX)
- **Use Case**: Consistent, high-throughput
- **Virtual Interfaces**: Public VIF, Private VIF, Transit VIF

## 🚀 5-Minute Master Review

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

### Security Best Practices
✅ Use private subnets for databases
✅ Use security groups as primary firewall
✅ Use NACLs as additional layer
✅ Enable VPC Flow Logs
✅ Use VPC endpoints for AWS services
✅ Never put databases in public subnet
✅ Use NAT Gateway (not NAT Instance)
✅ Implement defense in depth

### Common Mistakes to Avoid
❌ Forgetting 5 reserved IPs per subnet
❌ Using NAT Instance instead of NAT Gateway
❌ Putting NAT Gateway in private subnet
❌ Thinking VPC peering is transitive (it's not!)
❌ Overlapping CIDR blocks for peering
❌ Only outbound rules in NACL (it's stateless!)
❌ Using Security Groups to deny (use NACL)
❌ Not using VPC endpoints for S3/DynamoDB (costs!)

## 🎯 Exam Practice Speedrun

**Quick Questions** (Answers at bottom)

1. How many IPs reserved per subnet? __
2. Security Groups are stateful or stateless? __
3. Can Security Groups deny traffic? __
4. Max VPC CIDR size? __
5. Which is free: Interface or Gateway VPC endpoint? __
6. VPC peering is transitive? __
7. What provides HA NAT? __
8. Route 53 policy for DR? __

---

### Global Accelerator vs CloudFront
| Feature | CloudFront | Global Accelerator |
|---------|------------|-------------------|
| **Purpose** | Cache content | Route to optimal endpoint |
| **Use Case** | Static/dynamic content | Non-HTTP (TCP/UDP) |
| **Caching** | Yes | No |
| **IPs** | Changes | Static (2 Anycast) |
| **Protocols** | HTTP/HTTPS | Any (TCP/UDP) |

### Elastic IP Facts
- Static public IPv4 address
- Persists when instance stopped
- Can remap to another instance
- Max 5 per region (soft limit)
- Charged if not attached to running instance
- Free if attached to running instance

## ⏱️ Next Steps
- Time spent: ~75-90 min
- Practice: Create VPC, subnets, route tables, security groups
- Ready for: Networking practice questions
- Move to: Module 07 - Security

---

**Quick Answers**: 
1) 5 (first 4 + last 1)
2) Stateful
3) No (only allow)
4) /16 (65,536 IPs)
5) Gateway endpoint (S3/DynamoDB)
6) No
7) NAT Gateway
8) Failover routing policy

