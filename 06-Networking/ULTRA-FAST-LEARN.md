# 06: Networking - Ultra Fast Learning 🚀

## VPC Basics
- **Regional** resource (spans all AZs)
- **Max 5 VPCs** per region (soft limit)
- **CIDR range**: /16 to /28
- **AWS reserves 5 IPs** per subnet (first 4 + last 1)

### Private IP Ranges
- `10.0.0.0/8` → 10.0.0.0 to 10.255.255.255
- `172.16.0.0/12` → 172.16.0.0 to 172.31.255.255
- `192.168.0.0/16` → 192.168.0.0 to 192.168.255.255

## VPC Components

### Subnets
- **AZ-specific** (one subnet = one AZ)
- **Public**: Has route to Internet Gateway
- **Private**: No route to internet
- **Reserved IPs**: .0 (network), .1 (router), .2 (DNS), .3 (future), .255 (broadcast)

### Internet Gateway (IGW)
- **One per VPC**
- Enables internet access for public subnets
- Horizontally scaled, HA

### NAT Gateway
- **AZ-specific** (deploy one per AZ for HA)
- Allows **private** subnets to access internet (outbound only)
- **Managed** by AWS
- **NAT Instance**: EC2-based, cheaper, you manage

### Route Tables
- Controls routing for subnets
- **Main route table**: Default for VPC
- **Custom route tables**: Explicit associations
- **Most specific route wins**

## Security

### Security Groups (SG)
- **Stateful**: Return traffic auto-allowed
- **Allow rules only** (no deny)
- **Instance level**
- Default: All outbound allowed, all inbound denied
- Can reference other SGs

### Network ACL (NACL)
- **Stateless**: Must allow both directions
- **Allow AND deny rules**
- **Subnet level**
- Rules numbered, evaluated in order (lowest first)
- Default NACL: Allow all in/out
- Custom NACL: Deny all in/out

### SG vs NACL
| Feature | Security Group | NACL |
|---------|----------------|------|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow + Deny |
| Order | All evaluated | Number order |
| Applies | Explicit association | All in subnet |

## VPC Connectivity

### VPC Peering
- **Connect 2 VPCs** (same or cross-region)
- **Not transitive** (A-B, B-C ≠ A-C)
- **No overlapping CIDR**
- Update route tables

### VPC Endpoints
- **Private connection** to AWS services (no IGW/NAT)
- **Gateway Endpoint**: S3, DynamoDB (free, route table)
- **Interface Endpoint**: Everything else (PrivateLink, ENI, $)

### Transit Gateway
- **Hub-and-spoke** network topology
- Connect thousands of VPCs
- **Transitive** routing
- Works with Direct Connect, VPN

### VPN
- **Site-to-Site VPN**: On-premises to AWS
- **Virtual Private Gateway**: VPN endpoint on AWS side
- **Customer Gateway**: VPN device on customer side
- **Encrypted** traffic over internet

### Direct Connect
- **Dedicated private connection** (not internet)
- Consistent network, reduced costs
- 1 Gbps or 10 Gbps
- Setup takes **weeks/months**

## Route 53

### Routing Policies
1. **Simple**: Single resource, no health checks
2. **Weighted**: % traffic to different resources (A/B testing)
3. **Latency**: Lowest latency region
4. **Failover**: Primary/secondary (DR)
5. **Geolocation**: Based on user location
6. **Geoproximity**: Based on resource location (bias)
7. **Multi-value**: Up to 8 healthy records (simple with health checks)

### Health Checks
- Monitor endpoints (HTTP, HTTPS, TCP)
- **Interval**: 30 sec (standard) or 10 sec (fast)
- **Threshold**: Default 3 consecutive checks
- Can monitor **CloudWatch alarms**

### Record Types
- **A**: IPv4 address
- **AAAA**: IPv6 address
- **CNAME**: Alias to another domain (not root)
- **Alias**: AWS resource (can use for root domain)

## CloudFront
- **CDN** (Content Delivery Network)
- **400+ edge locations**
- Cache content closer to users
- **Origins**: S3, ALB, EC2, custom HTTP
- **TTL**: Default 24 hours
- **Geo-restriction**: Whitelist/blacklist countries
- **Signed URLs/Cookies**: Restrict access
- **OAI (Origin Access Identity)**: S3 bucket access only via CloudFront

## Quick Exam Tips
- **VPC**: Regional, max 5 per region
- **Subnet**: AZ-specific, 5 IPs reserved
- **IGW**: One per VPC, public internet access
- **NAT Gateway**: Private to internet (outbound)
- **Security Group**: Stateful, allow only
- **NACL**: Stateless, allow + deny, subnet level
- **VPC Peering**: Not transitive
- **Transit Gateway**: Transitive, hub-and-spoke
- **VPN**: Encrypted over internet
- **Direct Connect**: Dedicated private link
- **Route 53**: DNS, 7 routing policies
- **CloudFront**: CDN, 400+ edge locations
- **Endpoint**: Private connection to AWS services

