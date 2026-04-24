# Networking & Content Delivery - Mermaid Diagrams

## VPC Architecture

### VPC Complete Architecture

```mermaid
graph TB
    Internet["Internet"]
    
    subgraph VPC_10_0_0_0_16_Group["VPC: 10.0.0.0/16"]
        IGW[Internet Gateway]
        
        subgraph Availability_Zone_A_Group["Availability Zone A"]
            PublicSubnetA["Public Subnet<br/>10.0.1.0/24"]
            PrivateSubnetA["Private Subnet<br/>10.0.3.0/24"]
            
            WebServerA["Web Server<br/>10.0.1.10"]
            AppServerA["App Server<br/>10.0.3.10"]
            
            WebServerA --> PublicSubnetA
            AppServerA --> PrivateSubnetA
        end
        
        subgraph Availability_Zone_B_Group["Availability Zone B"]
            PublicSubnetB["Public Subnet<br/>10.0.2.0/24"]
            PrivateSubnetB["Private Subnet<br/>10.0.4.0/24"]
            
            WebServerB["Web Server<br/>10.0.2.10"]
            AppServerB["App Server<br/>10.0.4.10"]
            NATGW["NAT Gateway<br/>10.0.2.100"]
            
            WebServerB --> PublicSubnetB
            AppServerB --> PrivateSubnetB
            NATGW --> PublicSubnetB
        end
        
        RDS["RDS Multi-AZ<br/>Primary: AZ-A<br/>Standby: AZ-B"]
    end
    
    Internet <--> IGW
    IGW <--> PublicSubnetA
    IGW <--> PublicSubnetB
    
    PublicSubnetA -.Route.-> IGW
    PublicSubnetB -.Route.-> IGW
    
    PrivateSubnetA -.Route.-> NATGW
    PrivateSubnetB -.Route.-> NATGW
    NATGW -.Route.-> IGW
    
    AppServerA --> RDS
    AppServerB --> RDS
    
    classDef style1 fill:#FF9900
    class IGW style1
    classDef style2 fill:#569A31
    class NATGW style2
    classDef style3 fill:#146EB4
    class PublicSubnetA style3
    classDef style4 fill:#8C4FFF
    class PrivateSubnetA style4
```

### VPC Subnet CIDR Calculation

```mermaid
graph TB
    VPC["VPC: 10.0.0.0/16<br/>65,536 IP addresses"]
    
    VPC --> Subnet1["Public Subnet 1<br/>10.0.1.0/24<br/>256 IPs - 5 = 251 usable"]
    VPC --> Subnet2["Public Subnet 2<br/>10.0.2.0/24<br/>256 IPs - 5 = 251 usable"]
    VPC --> Subnet3["Private Subnet 1<br/>10.0.3.0/24<br/>256 IPs - 5 = 251 usable"]
    VPC --> Subnet4["Private Subnet 2<br/>10.0.4.0/24<br/>256 IPs - 5 = 251 usable"]
    
    Reserved["AWS Reserved IPs per Subnet:<br/>10.0.1.0 - Network address<br/>10.0.1.1 - VPC router<br/>10.0.1.2 - DNS server<br/>10.0.1.3 - Future use<br/>10.0.1.255 - Broadcast not supported but reserved"]
    
    Subnet1 -.Reserves.-> Reserved
    
    classDef style1 fill:#FF9900
    class VPC style1
    classDef style2 fill:#C00
    class Reserved style2
```

### Route Table Configuration

```mermaid
graph TB
    subgraph Public_Route_Table_Group["Public Route Table"]
        PRT[Public Route Table]
        PRT --> PR1["Destination: 10.0.0.0/16<br/>Target: local"]
        PRT --> PR2["Destination: 0.0.0.0/0<br/>Target: igw-xxxxx"]
        
        PRT -.Associated with.-> PublicSubnets["Public Subnets<br/>10.0.1.0/24<br/>10.0.2.0/24"]
    end
    
    subgraph Private_Route_Table_Group["Private Route Table"]
        PrivRT[Private Route Table]
        PrivRT --> PrivR1["Destination: 10.0.0.0/16<br/>Target: local"]
        PrivRT --> PrivR2["Destination: 0.0.0.0/0<br/>Target: nat-xxxxx"]
        
        PrivRT -.Associated with.-> PrivateSubnets["Private Subnets<br/>10.0.3.0/24<br/>10.0.4.0/24"]
    end
    
    IGW["Internet Gateway<br/>igw-xxxxx"] -.Routes to.-> PR2
    NATGW["NAT Gateway<br/>nat-xxxxx"] -.Routes to.-> PrivR2
    
    classDef style1 fill:#569A31
    class PRT style1
    classDef style2 fill:#FF9900
    class PrivRT style2
```

## Security Groups vs NACLs

### Security Groups vs Network ACLs

```mermaid
graph TB
    subgraph Security_Groups_Group["Security Groups"]
        SG["Security Group<br/>Instance Level<br/>Stateful"]
        
        SGRules["Rules:<br/>✅ Allow rules only<br/>✅ Can reference other SGs<br/>✅ Return traffic automatic<br/>✅ Evaluate all rules<br/>Default: Deny all inbound"]
        
        SGExample["Example:<br/>Inbound: SSH from 10.0.0.0/16<br/>Inbound: HTTP from 0.0.0.0/0<br/>Outbound: All traffic allowed"]
    end
    
    subgraph Network_ACLs_Group["Network ACLs"]
        NACL["Network ACL<br/>Subnet Level<br/>Stateless"]
        
        NACLRules["Rules:<br/>✅ Allow and Deny rules<br/>✅ Process in number order<br/>❌ Return traffic must be explicitly allowed<br/>✅ First match wins<br/>Default: Allow all"]
        
        NACLExample["Example:<br/>100: Allow HTTP from 0.0.0.0/0<br/>200: Allow HTTPS from 0.0.0.0/0<br/>300: Deny all from 10.0.5.0/24<br/>*: Deny all"]
    end
    
    Instance[EC2 Instance] --> SG
    SG --> Subnet[Subnet]
    Subnet --> NACL
    
    classDef style1 fill:#569A31
    class SG style1
    classDef style2 fill:#FF9900
    class NACL style2
```

### Traffic Flow with SG and NACL

```mermaid
sequenceDiagram
    participant Client
    participant NACL as Network ACL (Subnet(
    participant SG as Security Group (Instance(
    participant EC2 as EC2 Instance
    
    Note over Client,EC2: Inbound Traffic
    
    Client->>NACL: Request on port 80
    NACL->>NACL: Check Inbound Rules (stateless(
    NACL->>SG: Allow if rule matches
    SG->>SG: Check Inbound Rules (stateful(
    SG->>EC2: Allow if rule matches
    
    Note over Client,EC2: Response (Outbound from EC2(
    
    EC2->>SG: Response
    SG->>NACL: Auto-allow (stateful(
    NACL->>NACL: Check Outbound Rules (stateless(
    NACL->>Client: Allow if rule matches
    
    Note over Client,EC2: Security Group remembers the request<br/>Network ACL does not
    
```

## VPC Connectivity

### VPC Peering

```mermaid
graph TB
    subgraph VPC_A_10_0_0_0_16_Group["VPC A: 10.0.0.0/16"]
        VPC_A["VPC A<br/>us-east-1"]
        SubnetA["Subnet 10.0.1.0/24"]
        EC2_A[EC2 Instance A]
        
        SubnetA --> VPC_A
        EC2_A --> SubnetA
    end
    
    subgraph VPC_B_172_16_0_0_16_Group["VPC B: 172.16.0.0/16"]
        VPC_B["VPC B<br/>us-east-1"]
        SubnetB["Subnet 172.16.1.0/24"]
        EC2_B[EC2 Instance B]
        
        SubnetB --> VPC_B
        EC2_B --> SubnetB
    end
    
    subgraph VPC_C_192_168_0_0_16_Group["VPC C: 192.168.0.0/16"]
        VPC_C["VPC C<br/>eu-west-1"]
        SubnetC["Subnet 192.168.1.0/24"]
        EC2_C[EC2 Instance C]
        
        SubnetC --> VPC_C
        EC2_C --> SubnetC
    end
    
    VPC_A <-.Peering Connection.-> VPC_B
    VPC_A <-.Peering Connection.-> VPC_C
    
    Limitations["Limitations:<br/>❌ No transitive peering<br/>VPC C cannot access VPC B through VPC A<br/>❌ CIDR must not overlap<br/>✅ Cross-region supported<br/>✅ Cross-account supported"]
    
    classDef style1 fill:#FF9900
    class VPC_A style1
    classDef style2 fill:#569A31
    class VPC_B style2
    classDef style3 fill:#146EB4
    class VPC_C style3
```

### Transit Gateway

```mermaid
graph TB
    TGW["Transit Gateway<br/>Hub & Spoke Model<br/>Regional Resource"]
    
    VPC1["VPC 1<br/>10.0.0.0/16"]
    VPC2["VPC 2<br/>172.16.0.0/16"]
    VPC3["VPC 3<br/>192.168.0.0/16"]
    VPC4["VPC 4<br/>10.1.0.0/16"]
    
    VPN["VPN Connection<br/>On-Premises"]
    DX["Direct Connect<br/>On-Premises"]
    
    VPC1 <--> TGW
    VPC2 <--> TGW
    VPC3 <--> TGW
    VPC4 <--> TGW
    VPN <--> TGW
    DX <--> TGW
    
    TGW_Peer["Transit Gateway<br/>Another Region"] <-.Peering.-> TGW
    
    Benefits["Benefits:<br/>✅ Transitive routing<br/>✅ Hub and spoke topology<br/>✅ Works with VPN & Direct Connect<br/>✅ Cross-region peering<br/>✅ Single gateway for thousands of VPCs<br/>💰 Pay per attachment per hour"]
    
    classDef style1 fill:#FF9900
    class TGW style1
    classDef style2 fill:#569A31
    class VPC1 style2
```

### VPC Endpoints

```mermaid
graph TB
    subgraph VPC_10_0_0_0_16_Group["VPC: 10.0.0.0/16"]
        subgraph Private_Subnet_Group["Private Subnet"]
            EC2["EC2 Instance<br/>Private IP only<br/>No internet access"]
        end
        
        subgraph VPC_Endpoints_Group["VPC Endpoints"]
            InterfaceEP["Interface Endpoint<br/>ENI with Private IP<br/>Powered by PrivateLink"]
            GatewayEP["Gateway Endpoint<br/>Route table entry"]
        end
    end
    
    subgraph AWS_Services_Group["AWS Services"]
        S3[Amazon S3]
        DynamoDB[DynamoDB]
        SNS[SNS]
        SQS[SQS]
        Others[Other AWS Services]
    end
    
    EC2 -->|Private connection| InterfaceEP
    EC2 -->|Private connection| GatewayEP
    
    InterfaceEP -.PrivateLink.-> SNS
    InterfaceEP -.PrivateLink.-> SQS
    InterfaceEP -.PrivateLink.-> Others
    
    GatewayEP -.Free.-> S3
    GatewayEP -.Free.-> DynamoDB
    
    Comparison["Gateway Endpoint:<br/>✅ S3 and DynamoDB only<br/>✅ Free<br/>✅ Route table entry<br/><br/>Interface Endpoint:<br/>✅ Most AWS services<br/>💰 Pay per hour + data<br/>✅ ENI in subnet<br/>✅ Security groups apply"]
    
    classDef style1 fill:#FF9900
    class InterfaceEP style1
    classDef style2 fill:#569A31
    class GatewayEP style2
```

## Route 53

### Route 53 Routing Policies

```mermaid
graph TB
    Route53["Route 53<br/>DNS Service"]
    
    Route53 --> Simple["Simple Routing<br/>Single resource<br/>No health checks"]
    Route53 --> Weighted["Weighted Routing<br/>% traffic distribution<br/>A/B testing, gradual deployment"]
    Route53 --> Latency["Latency Routing<br/>Lowest latency<br/>Based on user location"]
    Route53 --> Failover["Failover Routing<br/>Active-Passive<br/>Health check based"]
    Route53 --> Geolocation["Geolocation Routing<br/>Based on user location<br/>Country/continent"]
    Route53 --> Geoproximity["Geoproximity Routing<br/>Route based on resource location<br/>Bias adjustment"]
    Route53 --> Multivalue["Multi-Value Routing<br/>Multiple resources<br/>Up to 8 healthy records"]
    
    Simple --> Example1["example.com -&gt; 1.2.3.4"]
    Weighted --> Example2["70% -&gt; us-east-1<br/>30% -&gt; eu-west-1"]
    Latency --> Example3["EU users -&gt; eu-west-1<br/>US users -&gt; us-east-1"]
    Failover --> Example4["Primary: us-east-1<br/>Secondary: eu-west-1"]
    
    classDef style1 fill:#8C4FFF
    class Route53 style1
    classDef style2 fill:#C00
    class Failover style2
    classDef style3 fill:#569A31
    class Latency style3
```

### Route 53 Health Checks and Failover

```mermaid
sequenceDiagram
    participant User
    participant Route53
    participant HealthCheck as Health Checker
    participant Primary as Primary (us-east-1(
    participant Secondary as Secondary (eu-west-1(
    
    loop Every 30 seconds (or 10s fast(
        HealthCheck->>Primary: HTTP/HTTPS/TCP Check
        Primary->>HealthCheck: 200 OK (Healthy(
    end
    
    User->>Route53: DNS Query for example.com
    Route53->>User: Return Primary IP
    User->>Primary: Connect
    
    Note over Primary: Primary Fails
    
    loop Health Check Failure
        HealthCheck->>Primary: HTTP Check
        Primary->>HealthCheck: Timeout/Error
    end
    
    Note over HealthCheck: After 3 consecutive failures<br/>Mark as Unhealthy
    
    User->>Route53: DNS Query for example.com
    Route53->>Route53: Primary Unhealthy
    Route53->>User: Return Secondary IP
    User->>Secondary: Connect
    
    Note over Primary: Primary Recovers
    
    loop Health Check Success
        HealthCheck->>Primary: HTTP Check
        Primary->>HealthCheck: 200 OK
    end
    
    Note over HealthCheck: After 3 consecutive successes<br/>Mark as Healthy
    
    Route53->>Route53: Fail back to Primary
    
```

## CloudFront

### CloudFront Distribution Architecture

```mermaid
graph TB
    subgraph Users_Worldwide_Group["Users Worldwide"]
        User1[User in NYC]
        User2[User in London]
        User3[User in Tokyo]
        User4[User in Sydney]
    end
    
    subgraph CloudFront_Edge_Locations_Group["CloudFront Edge Locations"]
        Edge1["Edge Location<br/>New York<br/>Cache"]
        Edge2["Edge Location<br/>London<br/>Cache"]
        Edge3["Edge Location<br/>Tokyo<br/>Cache"]
        Edge4["Edge Location<br/>Sydney<br/>Cache"]
    end
    
    subgraph Origin_Group["Origin"]
        S3["S3 Bucket<br/>us-east-1"]
        ALB["Application<br/>Load Balancer"]
        Custom["Custom Origin<br/>HTTP Server"]
    end
    
    User1 --> Edge1
    User2 --> Edge2
    User3 --> Edge3
    User4 --> Edge4
    
    Edge1 -.Cache Miss.-> S3
    Edge1 -.Cache Hit.-> User1
    
    Edge2 -.Cache Miss.-> ALB
    Edge3 -.Cache Miss.-> Custom
    
    OAI["Origin Access Identity<br/>Restrict S3 to CloudFront only"] -.Secures.-> S3
    
    Features["Features:<br/>✅ Global CDN with 400+ edge locations<br/>✅ DDoS protection<br/>✅ SSL/TLS support<br/>✅ Geo-restriction<br/>✅ Caching at edge<br/>✅ Compress objects automatically"]
    
    classDef style1 fill:#146EB4
    class Edge1 style1
    classDef style2 fill:#569A31
    class S3 style2
    classDef style3 fill:#FF9900
    class OAI style3
```

### CloudFront Cache Behavior

```mermaid
sequenceDiagram
    participant User
    participant Edge as CloudFront Edge
    participant Origin as Origin Server
    
    User->>Edge: Request /images/logo.png
    Edge->>Edge: Check cache
    
    alt Cache Hit
        Edge->>User: Return cached object
        Note over Edge,User: Fast response<br/>No origin request
    else Cache Miss
        Edge->>Origin: Request /images/logo.png
        Origin->>Edge: Return object + headers
        Edge->>Edge: Cache object (TTL from headers(
        Edge->>User: Return object
    end
    
    Note over Edge: Cached until TTL expires
    
    User->>Edge: Request /images/logo.png
    Edge->>Edge: Cache Hit
    Edge->>User: Return cached object
    
    Note over Edge: After TTL expires
    
    User->>Edge: Request /images/logo.png
    Edge->>Origin: If-Modified-Since request
    
    alt Object Modified
        Origin->>Edge: Return new object
        Edge->>Edge: Update cache
        Edge->>User: Return new object
    else Object Not Modified
        Origin->>Edge: 304 Not Modified
        Edge->>Edge: Refresh TTL
        Edge->>User: Return cached object
    end
    
```

## Hybrid Connectivity

### VPN Connection

```mermaid
graph TB
    subgraph On_Premises_Data_Center_Group["On-Premises Data Center"]
        OnPrem["Corporate Network<br/>192.168.0.0/16"]
        CGW["Customer Gateway<br/>Physical device<br/>Public IP: 203.0.113.1"]
        
        OnPrem --> CGW
    end
    
    Internet[Internet]
    
    subgraph AWS_Cloud_Group["AWS Cloud"]
        VGW["Virtual Private Gateway<br/>VPN endpoint on AWS side"]
        
        subgraph VPC_10_0_0_0_16_Group["VPC: 10.0.0.0/16"]
            PrivateSubnet[Private Subnet]
            EC2[EC2 Instances]
            RDS[(RDS Database)]
            
            PrivateSubnet --> EC2
            PrivateSubnet --> RDS
        end
        
        VGW --> PrivateSubnet
    end
    
    CGW <-.VPN Tunnel 1<br/>IPSec encrypted.-> Internet
    CGW <-.VPN Tunnel 2<br/>IPSec encrypted.-> Internet
    Internet <-.VPN Tunnels.-> VGW
    
    Features["Features:<br/>✅ Encrypted connection<br/>✅ Goes over internet<br/>✅ Quick to setup<br/>✅ Two tunnels for HA<br/>⚠️ Bandwidth limited by internet<br/>⚠️ Variable latency"]
    
    classDef style1 fill:#FF9900
    class VGW style1
    classDef style2 fill:#569A31
    class CGW style2
```

### Direct Connect

```mermaid
graph TB
    subgraph On_Premises_Group["On-Premises"]
        OnPrem[Corporate Data Center]
        Router[Customer Router]
        
        OnPrem --> Router
    end
    
    subgraph AWS_Direct_Connect_Location_Group["AWS Direct Connect Location"]
        DXLocation["Direct Connect Location<br/>Co-location facility"]
        DXRouter["AWS Direct Connect<br/>Router"]
        
        DXLocation --> DXRouter
    end
    
    subgraph AWS_Region_Group["AWS Region"]
        VGW[Virtual Private Gateway]
        
        subgraph VPC_Group["VPC"]
            Resources[AWS Resources]
        end
        
        VGW --> Resources
    end
    
    Router <-.Dedicated Private<br/>Connection.-> DXLocation
    DXRouter <-.AWS Private<br/>Network.-> VGW
    
    PublicVIF["Public VIF<br/>Access public AWS services<br/>S3, DynamoDB"] -.-> DXRouter
    PrivateVIF["Private VIF<br/>Access VPC resources"] -.-> VGW
    
    Features["Features:<br/>✅ Dedicated network connection<br/>✅ Consistent network performance<br/>✅ Reduced bandwidth costs<br/>✅ 1 Gbps or 10 Gbps<br/>⚠️ Takes weeks/months to set up<br/>💰 More expensive than VPN"]
    
    Backup["Backup VPN Connection<br/>over Internet"] -.Failover.-> VGW
    
    classDef style1 fill:#FF9900
    class DXRouter style1
    classDef style2 fill:#569A31
    class VGW style2
```

### AWS Global Accelerator

```mermaid
graph TB
    subgraph Users_Worldwide_Group["Users Worldwide"]
        User1[User in Asia]
        User2[User in Europe]
        User3[User in Americas]
    end
    
    subgraph AWS_Global_Accelerator_Group["AWS Global Accelerator"]
        AnyCast["2 Static Anycast IPs<br/>Global edge network"]
        
        Edge1["Edge Location<br/>Asia"]
        Edge2["Edge Location<br/>Europe"]
        Edge3["Edge Location<br/>Americas"]
        
        AnyCast --> Edge1
        AnyCast --> Edge2
        AnyCast --> Edge3
    end
    
    subgraph AWS_Regions_Group["AWS Regions"]
        subgraph us_east_1_Group["us-east-1"]
            ALB1["Application<br/>Load Balancer"]
            EC2_1[EC2 Instances]
            ALB1 --> EC2_1
        end
        
        subgraph eu_west_1_Group["eu-west-1"]
            ALB2["Application<br/>Load Balancer"]
            EC2_2[EC2 Instances]
            ALB2 --> EC2_2
        end
    end
    
    User1 --> AnyCast
    User2 --> AnyCast
    User3 --> AnyCast
    
    Edge1 -.AWS Private<br/>Network.-> ALB1
    Edge2 -.AWS Private<br/>Network.-> ALB2
    Edge3 -.AWS Private<br/>Network.-> ALB1
    
    HealthCheck["Health Checks<br/>Automatic failover"] -.Monitor.-> ALB1
    HealthCheck -.Monitor.-> ALB2
    
    Features["Features:<br/>✅ 2 static anycast IPs<br/>✅ Uses AWS global network<br/>✅ Faster than internet<br/>✅ Health checks & failover<br/>✅ DDoS protection with Shield<br/>Use: Gaming, IoT, VoIP, non-HTTP"]
    
    VsCloudFront["vs CloudFront:<br/>CloudFront: Cacheable content, HTTP<br/>Global Accelerator: TCP/UDP, static IPs, global performance"]
    
    classDef style1 fill:#FF9900
    class AnyCast style1
    classDef style2 fill:#146EB4
    class Edge1 style2
```

## Network Performance

### Enhanced Networking

```mermaid
graph TB
    EC2[EC2 Instance Types]
    
    EC2 --> ENA["Elastic Network Adapter ENA<br/>Up to 100 Gbps"]
    EC2 --> IntelVF["Intel 82599 VF<br/>Up to 10 Gbps<br/>Legacy"]
    
    ENA --> Features["Features:<br/>✅ Higher bandwidth<br/>✅ Higher PPS (packets per second[<br/>✅ Lower latency<br/>✅ Lower jitter<br/>✅ No additional cost"]
    
    ENA --> UseWith["Supported:<br/>• Most current gen instances<br/>• Some previous gen<br/>• Enabled by default on modern AMIs"]
    
    PlacementGroup[Cluster Placement Group] -.Combine with.-> ENA
    
    EFA["Elastic Fabric Adapter<br/>HPC & ML workloads<br/>OS-bypass for ultra-low latency"] --> ENA
    
    classDef style1 fill:#FF9900
    class ENA style1
    classDef style2 fill:#569A31
    class EFA style2
```

