# Module 06: Networking & Content Delivery

## Overview
Networking is a critical component of AWS Solutions Architecture. This module covers VPC, Route 53, CloudFront, and other networking services.

## Learning Objectives
- Design and implement VPCs with subnets, route tables, and gateways
- Configure Route 53 for DNS management and routing policies
- Implement content delivery with CloudFront
- Understand Direct Connect and VPN options
- Master security groups and NACLs

---

## 1. Amazon VPC (Virtual Private Cloud)

### What is VPC?
- **Logically isolated network** in AWS cloud
- **Regional resource** (spans all AZs in region)
- Control IP address range, subnets, route tables, gateways
- Maximum **5 VPCs per region** (soft limit)

### CIDR (Classless Inter-Domain Routing)
- Method for IP address allocation
- Format: `a.b.c.d/x` where x is subnet mask (0-32)
- Example: `10.0.0.0/16` = 65,536 IP addresses
- **Allowed CIDR block sizes**: /16 to /28

**Private IP Ranges (RFC 1918)**:
- `10.0.0.0/8` → 10.0.0.0 to 10.255.255.255
- `172.16.0.0/12` → 172.16.0.0 to 172.31.255.255
- `192.168.0.0/16` → 192.168.0.0 to 192.168.255.255

### VPC Components

#### Subnets
- **AZ-specific** (within one AZ)
- **Public Subnet**: Has route to Internet Gateway
- **Private Subnet**: No route to internet
- **AWS reserves 5 IPs** in each subnet (first 4 + last 1)
  - Example in `10.0.0.0/24`:
    - `10.0.0.0`: Network address
    - `10.0.0.1`: VPC router
    - `10.0.0.2`: DNS server
    - `10.0.0.3`: Reserved for future use
    - `10.0.0.255`: Broadcast (not supported, but reserved)

#### Internet Gateway (IGW)
- Allow communication between VPC and internet
- **One IGW per VPC**
- Horizontally scaled, redundant, highly available
- Performs NAT for instances with public IPv4

#### NAT Gateway
- **Managed NAT service**
- Allow private subnet instances to access internet
- **Created in specific AZ**
- Uses Elastic IP
- **Pay per hour + data processed**
- **5 Gbps bandwidth** (scales to 45 Gbps)
- High availability within AZ (create in multiple AZs for redundancy)

**NAT Gateway vs NAT Instance**:
| Feature | NAT Gateway | NAT Instance |
|---------|-------------|--------------|
| Managed | AWS managed | Self-managed |
| Bandwidth | 5-45 Gbps | Depends on instance type |
| HA | HA within AZ | Use script for failover |
| Cost | Pay per hour + GB | Instance cost |
| Security Groups | Cannot be associated | Can be used |
| Bastion | Cannot be used as bastion | Can be used |

#### Route Tables
- Control traffic routing
- Each subnet must be associated with route table
- **Main route table**: Default for subnets without explicit association

Example Public Subnet Route Table:
```
Destination       Target
10.0.0.0/16      local
0.0.0.0/0        igw-xxxxx
```

Example Private Subnet Route Table:
```
Destination       Target
10.0.0.0/16      local
0.0.0.0/0        nat-xxxxx
```

---

## 2. VPC Security

### Security Groups (SG)
- **Stateful** firewall (return traffic automatically allowed)
- Operates at **instance level**
- **Allow rules only** (no deny rules)
- All inbound traffic **denied by default**
- All outbound traffic **allowed by default**
- Can reference other security groups

Example Security Group Rules:
```
Inbound:
Type        Protocol  Port    Source
HTTP        TCP       80      0.0.0.0/0
HTTPS       TCP       443     0.0.0.0/0
SSH         TCP       22      my-ip/32
Custom      TCP       3000    sg-xxxxx (app tier SG)

Outbound:
Type        Protocol  Port    Destination
All traffic All       All     0.0.0.0/0
```

### Network ACLs (NACLs)
- **Stateless** firewall (return traffic must be explicitly allowed)
- Operates at **subnet level**
- **Allow AND Deny rules**
- Rules evaluated in **number order** (lowest first)
- Default NACL **allows all** inbound/outbound
- Custom NACL **denies all** inbound/outbound by default

**NACL vs Security Group**:
| Feature | NACL | Security Group |
|---------|------|----------------|
| Level | Subnet | Instance |
| Rules | Allow + Deny | Allow only |
| Stateful | No (stateless) | Yes (stateful) |
| Order | Numbered, processed in order | All rules evaluated |
| Default | Allow all | Deny all inbound |

Example NACL:
```
Inbound:
Rule #  Type        Protocol  Port    Source          Allow/Deny
100     HTTP        TCP       80      0.0.0.0/0       ALLOW
200     HTTPS       TCP       443     0.0.0.0/0       ALLOW
300     SSH         TCP       22      10.0.0.0/16     ALLOW
*       All traffic All       All     0.0.0.0/0       DENY

Outbound:
Rule #  Type        Protocol  Port    Destination     Allow/Deny
100     Custom      TCP       1024-65535  0.0.0.0/0   ALLOW (ephemeral)
*       All traffic All       All     0.0.0.0/0       DENY
```

---

## 3. VPC Connectivity

### VPC Peering
- Connect **two VPCs** privately using AWS network
- **Non-transitive** (must create peering for each connection)
- Can peer across regions and accounts
- **Must not have overlapping CIDR blocks**
- Update route tables in both VPCs

### VPC Endpoints
- Access AWS services **without Internet Gateway**
- Stay within AWS private network
- **Powered by AWS PrivateLink**

#### Interface Endpoints (powered by PrivateLink)
- **ENI** with private IP in your subnet
- Supports most AWS services
- **Pay per hour + data processed**
- Security groups applicable

#### Gateway Endpoints
- **Gateway** as target in route table
- **Free**
- Only for **S3 and DynamoDB**
- Specify in route table

Example Route Table with Gateway Endpoint:
```
Destination            Target
10.0.0.0/16           local
pl-xxxxx (S3 prefix)  vpce-xxxxx
```

### AWS PrivateLink
- Securely expose service to thousands of VPCs
- **Service VPC**: Network Load Balancer
- **Customer VPC**: Interface Endpoint (ENI)
- Does not require VPC peering, IGW, NAT, route tables
- **Best way to expose service to other VPCs**

### Transit Gateway
- **Hub-and-spoke** network topology
- Connect **thousands of VPCs** and on-premises networks
- **Regional resource** (can peer across regions)
- Works with Direct Connect, VPN
- Route tables for controlling traffic flow
- Supports **IP multicast** (only AWS service)

---

## 4. Hybrid Connectivity

### AWS Site-to-Site VPN
- Connect on-premises network to AWS
- **Encrypted** connection over internet
- **Two VPN tunnels** for redundancy
- **Quick to set up** (minutes)

**Components**:
- **Virtual Private Gateway (VGW)**: VPN concentrator on AWS side
- **Customer Gateway (CGW)**: Physical device/software on customer side

**Limitations**:
- Uses public internet (variable bandwidth/latency)
- Speed limited by internet connection

### AWS Direct Connect (DX)
- **Dedicated private connection** from on-premises to AWS
- **Consistent network performance**
- **Reduce bandwidth costs** for high-volume traffic
- **Takes 1+ month to establish**

**Connection Types**:
- **Dedicated Connection**: 1 Gbps, 10 Gbps, 100 Gbps
- **Hosted Connection**: 50 Mbps to 10 Gbps (via AWS Partner)

**Direct Connect Gateway**:
- Connect to **multiple VPCs** in different regions (same account)

**Direct Connect + VPN**:
- VPN over Direct Connect for IPsec-encrypted connection
- Extra layer of security

### AWS Client VPN
- **Managed OpenVPN** service
- Connect individual users to AWS or on-premises
- **Secure TLS connection**
- Uses AWS PrivateLink

---

## 5. Amazon Route 53

### What is Route 53?
- Highly available and scalable **DNS service**
- **100% SLA availability**
- Domain registration
- DNS routing
- Health checking

### Route 53 Record Types
- **A**: IPv4 address
- **AAAA**: IPv6 address
- **CNAME**: Hostname to hostname (cannot use for zone apex)
- **Alias**: AWS resource (can use for zone apex)
- **NS**: Name servers for hosted zone
- **MX**: Mail servers
- **TXT**: Text information
- **SOA**: Start of authority
- **CAA**: Certificate authority authorization

### Hosted Zones
- Container for DNS records
- **Public Hosted Zone**: Routes internet traffic
- **Private Hosted Zone**: Routes traffic within VPC
- **$0.50 per hosted zone/month**

### Route 53 Routing Policies

#### 1. Simple Routing
- Route to **single resource**
- Can return **multiple values** (client chooses randomly)
- No health checks

#### 2. Weighted Routing
- Distribute traffic across resources based on **weights**
- Weights: 0-255
- Use case: Load balancing, A/B testing
- Health checks supported

Example:
```
Record 1: 70% traffic (weight 70)
Record 2: 20% traffic (weight 20)
Record 3: 10% traffic (weight 10)
```

#### 3. Latency Routing
- Route based on **lowest latency**
- AWS measures latency from user to AWS regions
- Health checks supported

#### 4. Failover Routing
- Active-passive failover
- **Primary** and **Secondary** records
- Health check on primary
- Automatic failover to secondary if primary unhealthy

#### 5. Geolocation Routing
- Route based on **user's geographic location**
- Specify by continent, country, or US state
- **Default location** for no match
- Use case: Content localization, restrict distribution

#### 6. Geoproximity Routing
- Route based on **geographic location** of users and resources
- **Bias** to shift traffic (1 to 99 = expand, -1 to -99 = shrink)
- Must use **Route 53 Traffic Flow**

#### 7. Multi-Value Answer Routing
- Return **multiple values/resources** (up to 8)
- Health checks for each value
- **Not a substitute for ELB** (client-side load balancing)

### Route 53 Health Checks
- Monitor endpoint health
- **Types**:
  - Endpoint monitoring (IP or domain)
  - Calculated health checks (combine results)
  - CloudWatch alarms (private resources)
- Health checkers from **multiple locations worldwide** (default 15)
- Interval: 30 seconds (standard) or 10 seconds (fast)
- Integration with CloudWatch alarms

### Route 53 Traffic Flow
- Visual editor for complex routing configurations
- Versioning support
- Reusable across hosted zones

### DNSSEC
- Protect against DNS spoofing
- Route 53 supports:
  - **DNSSEC for domain registration**
  - **DNSSEC signing** (not automatic, must configure)

---

## 6. Amazon CloudFront

### What is CloudFront?
- **Content Delivery Network (CDN)**
- **400+ Points of Presence** globally
- DDoS protection, AWS Shield, AWS WAF integration
- Cache content at edge locations
- Reduce latency for users

### CloudFront Origins
- **S3 Bucket**:
  - Distribute files globally
  - Enhanced security with Origin Access Control (OAC)
  - Can be used as ingress (upload to S3)
- **Custom Origin (HTTP)**:
  - ALB, EC2 instance, S3 website
  - Any HTTP backend

### CloudFront vs S3 Cross-Region Replication

| CloudFront | S3 CRR |
|------------|--------|
| Global edge network | Select specific regions |
| Files cached for TTL | Files replicated in real-time |
| Great for static content | Great for dynamic content |
| Read-only | Read-write |

### CloudFront Caching
- **Cache based on**:
  - Headers
  - Query strings
  - Cookies
- Cache lives in each edge location
- **TTL** (Time To Live): 0 seconds to 1 year
- Invalidate cache: Full or partial paths

### CloudFront Security

**Geo Restriction**
- Whitelist or Blacklist countries
- Use case: Copyright laws

**HTTPS**
- **Viewer Protocol Policy**:
  - Redirect HTTP to HTTPS
  - HTTPS only
- **Origin Protocol Policy**:
  - HTTP only
  - HTTPS only
  - Match viewer

**Signed URLs / Signed Cookies**
- Control access to content
- **Signed URL**: Individual file access
- **Signed Cookie**: Multiple files access
- Attach policy (URL expiration, IP ranges, trusted signers)
- Use AWS Account (root) or CloudFront Key Pairs (not recommended)

**CloudFront vs S3 Pre-Signed URL**:
| CloudFront Signed URL | S3 Pre-Signed URL |
|----------------------|-------------------|
| Access to path (multiple files) | Access to individual file |
| Account-wide key pairs | IAM principal signing |
| Filter by IP, date, expiration | Limited lifetime |
| Leverage caching | Direct S3 access |

**Field-Level Encryption**
- Encrypt specific fields at edge
- Uses asymmetric encryption
- Up to 10 fields
- Use case: Protect sensitive data (credit cards)

### CloudFront Price Classes
- **Price Class All**: All edge locations (best performance)
- **Price Class 200**: Most regions, excludes expensive
- **Price Class 100**: Only least expensive regions

### CloudFront Origin Groups
- **High availability** and **failover**
- Primary and secondary origin
- Automatic failover on failure

### CloudFront Functions vs Lambda@Edge

| Feature | CloudFront Functions | Lambda@Edge |
|---------|---------------------|-------------|
| **Runtime** | JavaScript | Node.js, Python |
| **Triggers** | Viewer request/response | All 4 CloudFront events |
| **Execution** | Edge location | Regional edge cache |
| **Max duration** | < 1 ms | 5-10 seconds |
| **Max memory** | 2 MB | 128 MB - 10 GB |
| **Use case** | Lightweight, high-scale | CPU-intensive, network access |
| **Pricing** | $0.10 per million | $0.60 per million + duration |

---

## 7. AWS Global Accelerator

### What is Global Accelerator?
- Improve global application **availability and performance**
- **2 Anycast IP addresses** (static)
- Traffic routed through AWS global network
- DDoS protection (AWS Shield)

### Global Accelerator vs CloudFront

| Global Accelerator | CloudFront |
|-------------------|------------|
| Proxies traffic to applications | Caches content |
| Good for TCP/UDP | Good for HTTP/HTTPS |
| Static IP addresses | Dynamic IP addresses |
| Deterministic routing | Content-based routing |
| Gaming, IoT, VoIP | Static/dynamic web content |

---

## 8. AWS PrivateLink (VPC Endpoint Services)

### What is AWS PrivateLink?
- Securely expose services to other VPCs
- **Does not require VPC peering, IGW, NAT, route tables**
- Requires **Network Load Balancer** (service VPC)
- Requires **ENI** (customer VPC)
- Most secure way to expose service

---

## Practice Questions

1. **Which VPC component allows outbound internet access for private subnets?**
   - A. Internet Gateway
   - B. NAT Gateway
   - C. Virtual Private Gateway
   - D. VPC Peering
   
   **Answer**: B

2. **What is the maximum size of a CIDR block in a VPC?**
   - A. /8
   - B. /16
   - C. /24
   - D. /28
   
   **Answer**: B

3. **Which Route 53 routing policy would you use for active-passive failover?**
   - A. Simple
   - B. Weighted
   - C. Failover
   - D. Latency
   
   **Answer**: C

4. **What is the difference between Security Groups and NACLs?**
   - A. SGs are stateful, NACLs are stateless
   - B. SGs are stateless, NACLs are stateful
   - C. Both are stateful
   - D. Both are stateless
   
   **Answer**: A

---

## Hands-On Labs

### Lab 1: VPC with Public and Private Subnets
1. Create VPC with CIDR 10.0.0.0/16
2. Create public subnet (10.0.1.0/24)
3. Create private subnet (10.0.2.0/24)
4. Create and attach Internet Gateway
5. Create NAT Gateway in public subnet
6. Configure route tables
7. Launch EC2 in each subnet

### Lab 2: Security Groups and NACLs
1. Create security group for web tier (allow 80, 443)
2. Create security group for app tier (allow 3000 from web SG)
3. Configure NACL for subnet
4. Test connectivity

### Lab 3: Route 53 Routing Policies
1. Register domain (or use existing)
2. Create hosted zone
3. Create A records with different routing policies
4. Test weighted routing
5. Configure health checks
6. Test failover routing

### Lab 4: CloudFront Distribution
1. Create S3 bucket with static website
2. Create CloudFront distribution
3. Configure OAC for S3 origin
4. Test content delivery
5. Configure cache invalidation

---

## Key Takeaways

✅ VPC is regional, subnets are AZ-specific  
✅ Internet Gateway for public subnets, NAT Gateway for private subnets  
✅ Security Groups are stateful (instance-level), NACLs are stateless (subnet-level)  
✅ VPC Peering is non-transitive, must create for each connection  
✅ Gateway Endpoints (free) for S3/DynamoDB, Interface Endpoints for other services  
✅ Transit Gateway for hub-and-spoke connectivity  
✅ Direct Connect for dedicated private connection (1+ month setup)  
✅ Route 53 Alias records can point to AWS resources (zone apex supported)  
✅ CloudFront for caching static content, Global Accelerator for TCP/UDP performance  
✅ Use Route 53 health checks for automatic failover  

---

## Additional Resources

- [Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [Route 53 Developer Guide](https://docs.aws.amazon.com/route53/)
- [CloudFront Developer Guide](https://docs.aws.amazon.com/cloudfront/)
- [VPC Scenarios](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenarios.html)

---

**Previous Module**: [Module 05: Database Services](../05-Database/README.md)  
**Next Module**: [Module 07: Security & Compliance](../07-Security/README.md)

