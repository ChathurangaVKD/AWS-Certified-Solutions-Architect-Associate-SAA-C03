# Networking - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company wants to create an isolated network in AWS where they can launch resources. Which AWS service should they use?

A. AWS Direct Connect  
B. Amazon VPC  
C. AWS Transit Gateway  
D. Amazon Route 53  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Amazon VPC** (Virtual Private Cloud) provides isolated network environment
- Logically isolated section of AWS Cloud
- Complete control over networking (IP ranges, subnets, route tables, gateways)
- Can create public and private subnets

**VPC Key Components**:
- **CIDR Block**: IP address range (e.g., 10.0.0.0/16)
- **Subnets**: Subdivisions within VPC
- **Route Tables**: Control traffic routing
- **Internet Gateway**: Access to internet
- **NAT Gateway**: Outbound internet for private subnets

**References:** Amazon VPC, VPC Fundamentals
</details>

---

### Question 2
A private subnet contains EC2 instances that need to download software updates from the internet. The instances should NOT be directly accessible from the internet. What should be configured?

A. Internet Gateway  
B. NAT Gateway  
C. Virtual Private Gateway  
D. VPC Peering  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **NAT Gateway** enables outbound internet access for private subnets
- Instances remain private (no inbound from internet)
- Placed in public subnet
- Route private subnet traffic to NAT Gateway

**NAT Gateway vs NAT Instance**:

| Feature | NAT Gateway | NAT Instance |
|---------|-------------|--------------|
| **Managed** | AWS-managed | Customer-managed |
| **Availability** | Highly available (AZ) | Single instance |
| **Bandwidth** | Up to 45 Gbps | Instance type dependent |
| **Cost** | Hourly + data transfer | Instance cost |
| **Maintenance** | AWS handles | Customer handles |

**Configuration**:
1. Create NAT Gateway in public subnet
2. Update private subnet route table
3. Route 0.0.0.0/0 to NAT Gateway

**References:** NAT Gateway, Private Subnet Internet Access
</details>

---

### Question 3
A company has a VPC with CIDR 10.0.0.0/16. They want to divide it into subnets. How many IP addresses are available in a /24 subnet?

A. 128  
B. 256  
C. 251  
D. 254  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **/24 subnet** has 256 total IP addresses (2^8)
- **AWS reserves 5 IP addresses** in each subnet:
  - .0: Network address
  - .1: VPC router
  - .2: DNS server
  - .3: Future use
  - .255: Broadcast

- **Available**: 256 - 5 = **251 IP addresses**

**CIDR Calculations**:
- /16: 65,536 IPs (65,531 usable)
- /24: 256 IPs (251 usable)
- /28: 16 IPs (11 usable)

**References:** VPC CIDR, Subnet Sizing
</details>

---

### Question 4
An application running in a VPC needs to connect to AWS services (S3, DynamoDB) without traversing the internet. What should be configured?

A. NAT Gateway  
B. Internet Gateway  
C. VPC Endpoint  
D. VPN Connection  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **VPC Endpoints** provide private connectivity to AWS services
- Traffic stays within AWS network
- No internet gateway or NAT required
- Enhanced security and performance

**VPC Endpoint Types**:

| Type | Services | Implementation | Cost |
|------|----------|----------------|------|
| **Gateway** | S3, DynamoDB | Route table entry | Free |
| **Interface** | Most AWS services | ENI in subnet | Hourly + data |

**Gateway Endpoint Benefits**:
- No data transfer charges
- Better performance
- No internet exposure
- Policy control

**References:** VPC Endpoints, Private Connectivity
</details>

---

### Question 5
A company wants to connect their on-premises data center to AWS with a dedicated, private network connection. Which service should they use?

A. AWS VPN  
B. AWS Direct Connect  
C. Internet Gateway  
D. VPC Peering  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Direct Connect** provides dedicated physical connection
- Bypasses public internet
- More consistent performance
- Reduced bandwidth costs

**Direct Connect vs VPN**:

| Feature | Direct Connect | Site-to-Site VPN |
|---------|----------------|------------------|
| **Connection** | Dedicated fiber | Internet-based |
| **Bandwidth** | 1 Gbps to 100 Gbps | Up to 1.25 Gbps |
| **Latency** | Low, consistent | Variable |
| **Cost** | Higher (port + data) | Lower |
| **Setup Time** | Weeks/months | Minutes |
| **Encryption** | Not by default | Yes (IPSec) |

**Use Cases**:
- Large data transfers
- Consistent performance needed
- Hybrid cloud architectures
- Compliance requirements

**References:** AWS Direct Connect, Hybrid Connectivity
</details>

---

### Question 6
A company needs to route traffic between multiple VPCs in different AWS accounts. What is the MOST scalable solution?

A. VPC Peering between all VPCs  
B. AWS Transit Gateway  
C. Multiple VPN connections  
D. Internet Gateway  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Transit Gateway** is central hub for VPCs
- Connects multiple VPCs, on-premises networks
- Simplifies network topology
- Scalable (up to 5000 VPCs)

**Transit Gateway vs VPC Peering**:

| Feature | Transit Gateway | VPC Peering |
|---------|----------------|-------------|
| **Topology** | Hub-and-spoke | Mesh (1-to-1) |
| **Scalability** | Thousands of VPCs | Limited |
| **Routing** | Centralized | Per peering |
| **Cost** | Higher | Lower (small scale) |
| **Cross-Region** | Yes | Yes |

**Peering Limitations**:
- Non-transitive (must peer each VPC)
- Complex with many VPCs (N*(N-1)/2 connections)

**References:** AWS Transit Gateway, VPC Connectivity
</details>

---

### Question 7
An application needs to resolve domain names. Where should the DNS server be configured in a VPC?

A. Custom DNS server on EC2  
B. Use AWS-provided DNS at .2 address  
C. Use Route 53 Resolver  
D. Both B and C  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- **VPC DNS** is available at base IP + 2 (e.g., 10.0.0.2)
- **Route 53 Resolver** provides DNS resolution
  - Resolves AWS resources
  - Forwards to on-premises DNS
  - Inbound/outbound endpoints

**DNS Options**:
- **AWS-provided DNS**: Default, automatic
- **Route 53 Resolver**: Advanced, hybrid scenarios
- **Custom DNS**: Full control, more management

**enableDnsHostnames**: EC2 instances get public DNS names
**enableDnsSupport**: Amazon-provided DNS enabled

**References:** VPC DNS, Route 53 Resolver
</details>

---

### Question 8
A company wants to protect their web application from DDoS attacks and filter malicious traffic. Which AWS services should be used? (Choose TWO)

A. AWS WAF  
B. AWS Shield  
C. Security Groups  
D. AWS GuardDuty  
E. Network ACLs  

<details>
<summary>Show Answer</summary>

**Answer: A, B**

**Explanation:**
- **AWS Shield**: DDoS protection
  - **Standard**: Free, automatic, common attacks
  - **Advanced**: Paid, advanced attacks, 24/7 support, cost protection

- **AWS WAF**: Web Application Firewall
  - Filter HTTP/HTTPS requests
  - SQL injection, XSS protection
  - Custom rules
  - Integration with CloudFront, ALB, API Gateway

**DDoS Protection Layers**:
1. **Shield Standard**: Network/transport layer (free)
2. **Shield Advanced**: Application layer, enhanced
3. **WAF**: Application-level filtering
4. **CloudFront**: Absorb traffic at edge

**Other Options**:
- **Security Groups**: Instance-level firewall, not DDoS
- **NACLs**: Subnet-level firewall, not DDoS
- **GuardDuty**: Threat detection, not prevention

**References:** AWS Shield, AWS WAF, DDoS Protection
</details>

---

### Question 9
An application needs to distribute traffic across EC2 instances in multiple Availability Zones. The instances fail health checks intermittently. What should be configured?

A. Increase health check interval  
B. Configure unhealthy threshold  
C. Use health check grace period  
D. Disable health checks  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **Unhealthy threshold**: Number of consecutive failed checks before marking unhealthy
- Prevents temporary issues from removing instances
- Balance between responsiveness and stability

**Health Check Parameters**:
- **HealthCheckIntervalSeconds**: Time between checks (5-300s)
- **HealthyThresholdCount**: Consecutive successes to mark healthy
- **UnhealthyThresholdCount**: Consecutive failures to mark unhealthy
- **HealthCheckTimeoutSeconds**: Time to wait for response

**Best Practices**:
- Set appropriate thresholds for application
- Monitor health check metrics
- Use ALB health checks for HTTP endpoints
- Consider application startup time

**References:** ELB Health Checks, Health Check Configuration
</details>

---

### Question 10
A company wants to route traffic based on the geographic location of users. Which Route 53 routing policy should be used?

A. Simple Routing  
B. Weighted Routing  
C. Geolocation Routing  
D. Latency-based Routing  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Geolocation Routing** routes based on user's geographic location
- Routes by continent, country, or state
- Use cases: Content localization, compliance, load distribution

**Route 53 Routing Policies**:

| Policy | Use Case |
|--------|----------|
| **Simple** | Single resource |
| **Weighted** | A/B testing, gradual rollout |
| **Latency** | Best performance for users |
| **Failover** | Active-passive DR |
| **Geolocation** | Route by user location |
| **Geoproximity** | Route by resource location + bias |
| **Multivalue** | Multiple IPs, health checks |

**Geolocation vs Latency**:
- **Geolocation**: Based on WHERE user is
- **Latency**: Based on WHICH region has lowest latency

**References:** Route 53 Routing Policies, Geolocation Routing
</details>

---

### Question 11
A Security Group allows inbound traffic on port 443 from 0.0.0.0/0. What outbound rule is needed for responses?

A. Allow port 443 outbound to 0.0.0.0/0  
B. Allow ephemeral ports outbound  
C. No outbound rule needed  
D. Allow all traffic outbound  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Security Groups are stateful**
- If inbound is allowed, return traffic automatically allowed
- No need to configure outbound rule for responses
- Only need outbound rules for instance-initiated traffic

**Security Groups vs NACLs**:

| Feature | Security Groups | NACLs |
|---------|----------------|-------|
| **State** | Stateful | Stateless |
| **Level** | Instance | Subnet |
| **Rules** | Allow only | Allow and Deny |
| **Return Traffic** | Automatic | Must configure |
| **Evaluation** | All rules | Ordered rules |

**References:** Security Groups, Stateful Firewalls
</details>

---

### Question 12
A company needs to block specific IP addresses from accessing their application. Which is the MOST appropriate solution?

A. Security Group Deny rules  
B. Network ACL Deny rules  
C. AWS WAF IP set rules  
D. Route 53 DNS filtering  

<details>
<summary>Show Answer</summary>

**Answer: B or C (Context dependent)**

**Explanation:**

**For network-level blocking**:
- **Network ACLs** support Deny rules
- Evaluated before traffic reaches instances
- Can block IP ranges at subnet level

**For application-level blocking**:
- **AWS WAF** with IP set match conditions
- More flexible filtering
- Works with CloudFront, ALB, API Gateway

**Security Groups limitations**:
- **Cannot create Deny rules** (only Allow)
- Cannot block specific IPs

**Best Practice**:
- **NACL**: Network-level IP blocking
- **WAF**: Application-level, geographic blocking, rate limiting

**References:** Network ACLs, AWS WAF, IP Blocking
</details>

---

### Question 13
A company has resources in two VPCs in the same region and wants them to communicate privately. What should be configured?

A. Internet Gateway  
B. VPC Peering  
C. AWS Transit Gateway  
D. VPN Connection  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **VPC Peering** connects two VPCs privately
- Same or different regions
- Same or different accounts
- Uses AWS network (no internet)

**VPC Peering Requirements**:
- Non-overlapping CIDR blocks
- Accept peering request
- Update route tables in both VPCs
- Update security groups if needed

**VPC Peering Characteristics**:
- Not transitive (VPC A ↔ VPC B, VPC B ↔ VPC C, but NOT A ↔ C)
- 1-to-1 connection
- No single point of failure
- No bandwidth bottleneck

**When to use Transit Gateway instead**:
- Many VPCs (>3-4)
- Complex routing
- Need transitive routing

**References:** VPC Peering, VPC Connectivity
</details>

---

### Question 14
An application running on EC2 instances needs to maintain client connections to the same instance for session persistence. Which load balancer feature should be enabled?

A. Cross-Zone Load Balancing  
B. Connection Draining  
C. Sticky Sessions  
D. Health Checks  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Sticky Sessions** (Session Affinity) routes requests from same client to same instance
- Uses cookies to track sessions
- Duration-based or application-based cookies

**ALB Sticky Session Types**:
- **Duration-based**: LB-generated cookie (AWSALB)
- **Application-based**: Application-generated cookie

**Sticky Sessions Limitations**:
- Can cause uneven load distribution
- Instance failure = lost sessions

**Better Alternative**: 
- Store sessions in ElastiCache or DynamoDB
- True stateless architecture

**References:** Sticky Sessions, Session Persistence
</details>

---

### Question 15
A company wants to use custom domain name with CloudFront distribution. What must be configured?

A. Route 53 CNAME record only  
B. SSL/TLS certificate in ACM and Route 53 alias  
C. CloudFront custom origin  
D. S3 bucket name matching domain  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
**Requirements for custom domain**:
1. **SSL/TLS Certificate in ACM** (us-east-1 region)
2. **Alternate Domain Names** (CNAMEs) in CloudFront
3. **Route 53 Alias Record** pointing to CloudFront distribution

**Configuration Steps**:
1. Request/import certificate in ACM (us-east-1)
2. Add alternate domain names to CloudFront
3. Associate ACM certificate with distribution
4. Create Route 53 alias record

**Certificate Requirements**:
- Must be in us-east-1 for CloudFront
- Domain name must match
- Can use wildcard (*.example.com)

**References:** CloudFront Custom Domains, ACM with CloudFront
</details>

---

### Question 16
A company needs a highly available solution for connecting on-premises data center to AWS. What should be implemented?

A. Single Direct Connect connection  
B. Redundant Direct Connect connections to different locations  
C. Site-to-Site VPN as backup to Direct Connect  
D. Both B and C (Maximum redundancy)  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
**Maximum High Availability**:
- Multiple Direct Connect connections in different locations
- Site-to-Site VPN as backup
- Redundant customer routers
- Multiple VPN tunnels

**HA Architecture Layers**:
1. **Redundant DX connections**: Different locations
2. **Redundant customer routers**: No single point failure
3. **VPN backup**: Failover if DX fails
4. **Multiple VPN tunnels**: AWS provides 2 tunnels per connection

**Benefits**:
- 99.99% availability possible
- Automatic failover
- Protection against location/connection failures

**References:** Direct Connect High Availability, Hybrid Network HA
</details>

---

### Question 17
An application needs to resolve private DNS names between on-premises network and AWS VPC. What should be configured?

A. VPC Peering  
B. Route 53 Private Hosted Zone  
C. Route 53 Resolver Endpoints  
D. AWS PrivateLink  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- **Route 53 Resolver Endpoints** enable DNS resolution between on-premises and AWS
- **Inbound Endpoints**: On-premises queries AWS resources
- **Outbound Endpoints**: AWS queries on-premises resources

**Endpoint Types**:
- **Inbound**: On-premises → AWS VPC
- **Outbound**: AWS VPC → On-premises (with forwarding rules)

**Configuration**:
1. Create inbound/outbound endpoints in VPC
2. Configure forwarding rules
3. Update on-premises DNS to forward to inbound endpoint
4. Create rules to forward to on-premises DNS

**Use Cases**:
- Hybrid cloud DNS resolution
- Migrate workloads with DNS dependencies
- Unified naming across environments

**References:** Route 53 Resolver, Hybrid DNS
</details>

---

### Question 18
A company wants to share services (like NLB) from one VPC with other VPCs/accounts without VPC peering. Which service enables this?

A. VPC Peering  
B. AWS PrivateLink  
C. Transit Gateway  
D. VPN Connection  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS PrivateLink** provides private connectivity to services
- Expose services via VPC Endpoint Services
- Consumers access via Interface VPC Endpoints
- No VPC peering, Internet Gateway, NAT required

**PrivateLink Architecture**:
- **Provider**: Creates Endpoint Service (backed by NLB)
- **Consumer**: Creates Interface VPC Endpoint
- **Connection**: Private, within AWS network

**Benefits**:
- Simplified network management
- No CIDR overlap issues
- Enhanced security (private connectivity)
- Scalable (thousands of consumers)

**Use Cases**:
- SaaS applications
- Shared services
- Third-party services
- Marketplace applications

**References:** AWS PrivateLink, VPC Endpoint Services
</details>

---

### Question 19
A company wants to implement a global accelerator for their application with static IP addresses and deterministic routing. Which service should be used?

A. Amazon CloudFront  
B. AWS Global Accelerator  
C. Route 53 with Latency Routing  
D. Elastic Load Balancing  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- **AWS Global Accelerator** provides static anycast IPs
- Routes traffic over AWS global network
- Deterministic, fast failover
- Health checks and instant failover

**Global Accelerator vs CloudFront**:

| Feature | Global Accelerator | CloudFront |
|---------|-------------------|------------|
| **Use Case** | TCP/UDP apps | HTTP/HTTPS content |
| **Caching** | No | Yes |
| **Static IP** | Yes (2 anycast) | No |
| **Failover** | Instant (< 30s) | DNS-based |
| **Protocol** | TCP, UDP | HTTP, HTTPS, WebSocket |

**Global Accelerator Benefits**:
- Static IPs (no DNS changes)
- AWS network routing (better performance)
- Health-based routing
- Traffic dials for blue/green deployments

**Use Cases**:
- Gaming (UDP)
- IoT
- VoIP
- Non-HTTP applications

**References:** AWS Global Accelerator, Global Traffic Management
</details>

---

### Question 20
A web application receives sudden traffic spikes. The company wants to protect backend servers from being overwhelmed. What should be implemented at the Network ACL level?

A. Allow all traffic  
B. Rate limiting  
C. Connection draining  
D. NACLs don't support rate limiting, use WAF  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- **NACLs** provide basic allow/deny rules
- **No rate limiting capabilities**
- **AWS WAF** provides rate limiting

**Rate Limiting Solutions**:

| Service | Level | Capability |
|---------|-------|------------|
| **AWS WAF** | Application (L7) | Rate-based rules |
| **API Gateway** | API | Throttling |
| **Shield Advanced** | Network | DDoS mitigation |
| **NACL** | Network (L4) | No rate limiting |

**WAF Rate-Based Rule**:
- Block IPs exceeding request threshold
- 5-minute time window
- Example: Block if > 2000 requests in 5 minutes

**Best Practice for Traffic Spikes**:
1. Auto Scaling for capacity
2. WAF for rate limiting
3. CloudFront for caching
4. ElastiCache for session/data

**References:** AWS WAF Rate Limiting, DDoS Protection
</details>

---

## Summary

**Total Questions**: 20  
**Topics Covered**:
- Amazon VPC (CIDR, Subnets, Route Tables)
- NAT Gateway vs NAT Instance
- VPC Endpoints (Gateway vs Interface)
- Security Groups vs Network ACLs
- AWS Direct Connect
- AWS Transit Gateway vs VPC Peering
- Route 53 Routing Policies
- Elastic Load Balancing (ALB, NLB features)
- CloudFront with Custom Domains
- AWS PrivateLink
- AWS Global Accelerator
- Route 53 Resolver
- AWS WAF and Shield

**Exam Tips**:

**VPC Fundamentals**:
- **Public Subnet**: Route to Internet Gateway
- **Private Subnet**: Route to NAT Gateway
- **AWS reserves 5 IPs** per subnet (.0, .1, .2, .3, .255)

**Connectivity**:
- **VPC Peering**: 1-to-1, non-transitive
- **Transit Gateway**: Hub-and-spoke, transitive
- **Direct Connect**: Dedicated connection
- **VPN**: Internet-based, encrypted

**Security**:
- **Security Groups**: Stateful, instance-level, allow only
- **NACLs**: Stateless, subnet-level, allow and deny
- **WAF**: Application-level filtering
- **Shield**: DDoS protection

**VPC Endpoints**:
- **Gateway**: S3, DynamoDB (free)
- **Interface**: Most services (hourly charge)

**DNS**:
- **Route 53**: DNS service with multiple routing policies
- **Resolver**: Hybrid DNS between on-premises and AWS

**Load Balancers**:
- **ALB**: Layer 7, HTTP/HTTPS, advanced routing
- **NLB**: Layer 4, TCP/UDP, static IP, extreme performance
- **CLB**: Legacy

**Global Services**:
- **CloudFront**: CDN, caching
- **Global Accelerator**: Static IPs, TCP/UDP, no caching

**Next Steps**:
- Understand when to use each connectivity option
- Know difference between Security Groups and NACLs
- Memorize Route 53 routing policies and use cases
- Practice VPC design scenarios

