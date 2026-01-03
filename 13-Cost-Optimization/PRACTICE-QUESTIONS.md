# Cost Optimization - Practice Questions

## Exam-Standard Questions (SAA-C03)

---

### Question 1
A company has a web application running on 20 EC2 instances that operate 24/7 with consistent usage. The instances have been running for 2 years and are expected to run for at least 2 more years. What is the MOST cost-effective pricing model?

A. On-Demand Instances  
B. 1-year Reserved Instances with No Upfront payment  
C. 3-year Reserved Instances with All Upfront payment  
D. Spot Instances  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Steady-state workload running 24/7 is perfect for Reserved Instances
- 3-year term provides highest discount (up to 72%)
- All Upfront payment provides maximum savings
- Expected to run 2+ years, so 3-year commitment is justified
- On-Demand is most expensive
- Spot Instances can be interrupted
- 1-year RI provides lower discount than 3-year

**References:** Reserved Instances, Cost Optimization
</details>

---

### Question 2
A company runs batch processing jobs that can be interrupted and resumed without data loss. The jobs run for 4-6 hours daily. What is the MOST cost-effective compute option?

A. On-Demand Instances  
B. Reserved Instances  
C. Spot Instances  
D. Dedicated Hosts  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Spot Instances provide up to 90% savings vs On-Demand
- Batch processing is fault-tolerant (can handle interruptions)
- Jobs can checkpoint and resume
- Perfect use case for Spot
- On-Demand is too expensive
- Reserved requires commitment (not needed for 4-6 hours daily)
- Dedicated Hosts are most expensive

**References:** Spot Instances, Fault-Tolerant Workloads
</details>

---

### Question 3
A solutions architect needs to reduce S3 storage costs for 500 TB of log data. Logs older than 30 days are rarely accessed but must be retained for 7 years for compliance. What should be done?

A. Keep all data in S3 Standard  
B. Use S3 lifecycle policies to transition data to S3 Glacier Deep Archive after 30 days  
C. Delete logs after 30 days  
D. Use S3 Intelligent-Tiering for all data  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- S3 Glacier Deep Archive is cheapest storage class ($0.00099/GB/month)
- Lifecycle policies automatically transition objects
- Meets 7-year retention requirement
- Transition after 30 days when access becomes rare
- S3 Standard costs $0.023/GB/month (23x more expensive)
- Deleting violates compliance
- Intelligent-Tiering costs more than Glacier Deep Archive

**Savings:** 500 TB × ($0.023 - $0.00099) × 12 months = ~$132,000/year

**References:** S3 Lifecycle Policies, S3 Glacier Deep Archive
</details>

---

### Question 4
An application uses a mix of EC2 instances (different families and sizes) across multiple regions, along with Fargate and Lambda. The usage is steady and predictable. Which pricing model provides the MOST flexibility and savings?

A. EC2 Reserved Instances  
B. Compute Savings Plans  
C. EC2 Instance Savings Plans  
D. On-Demand Instances  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Compute Savings Plans apply to EC2, Fargate, and Lambda
- Most flexible (any instance family, region, size)
- Up to 66% discount
- Automatically applies to eligible usage
- EC2 RIs only cover EC2, not Fargate/Lambda
- EC2 Instance Savings Plans limited to specific instance family
- On-Demand provides no discount

**References:** Compute Savings Plans, Flexible Pricing
</details>

---

### Question 5
A company wants to identify which EC2 instances are underutilized and could be downsized to reduce costs. Which AWS tool provides this recommendation?

A. AWS Budgets  
B. AWS Cost Explorer with Right-Sizing Recommendations  
C. AWS Trusted Advisor  
D. Both B and C  

<details>
<summary>Show Answer</summary>

**Answer: D**

**Explanation:**
- Cost Explorer provides right-sizing recommendations
- Trusted Advisor also provides underutilized instance recommendations
- Both analyze CloudWatch metrics (CPU, memory, network)
- Both suggest smaller instance types and estimate savings
- Budgets sets spending limits but doesn't analyze utilization
- Using both tools provides comprehensive insights

**References:** Cost Explorer, Trusted Advisor, Right-Sizing
</details>

---

### Question 6
A development team runs EC2 instances Monday-Friday, 9 AM-6 PM. The instances sit idle outside business hours. What is the MOST cost-effective approach?

A. Use Reserved Instances  
B. Use Spot Instances  
C. Use Instance Scheduler to automatically stop instances outside business hours  
D. Manually stop instances daily  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Instance Scheduler automates start/stop based on schedules
- Running only 45 hours/week instead of 168 hours saves ~73%
- No manual intervention required
- Reserved Instances charge 24/7 whether running or not
- Spot Instances could be interrupted during work hours
- Manual stopping is error-prone and requires effort

**Savings:** Running 45/168 hours = 73% time savings

**References:** Instance Scheduler, Cost Optimization
</details>

---

### Question 7
A company has multiple AWS accounts and wants to get volume discounts and consolidated billing. What should they implement?

A. AWS Budgets  
B. AWS Cost Explorer  
C. AWS Organizations with consolidated billing  
D. AWS Marketplace  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- AWS Organizations enables consolidated billing
- Combines usage across all accounts for volume discounts
- Single bill for all accounts
- Shared Reserved Instances and Savings Plans
- Cost Explorer and Budgets are reporting tools
- Marketplace is for purchasing software

**References:** AWS Organizations, Consolidated Billing
</details>

---

### Question 8
An application stores 1 PB of data in S3 with unpredictable access patterns. Some objects are accessed frequently, others rarely. What is the MOST cost-effective storage solution?

A. S3 Standard for all objects  
B. S3 Intelligent-Tiering  
C. Manually move objects to different storage classes  
D. S3 Glacier for all objects  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- S3 Intelligent-Tiering automatically moves objects between access tiers
- Optimizes costs without manual intervention
- Monitoring fee: $0.0025/1000 objects
- No retrieval fees for Frequent/Infrequent tiers
- S3 Standard wastes money on infrequently accessed data
- Manual management is operationally intensive
- Glacier has retrieval delays for frequent access

**References:** S3 Intelligent-Tiering, Unknown Access Patterns
</details>

---

### Question 9
A company wants to forecast their AWS costs for the next 6 months based on current usage trends. Which tool should they use?

A. AWS Budgets  
B. AWS Cost Explorer with forecasting  
C. AWS Trusted Advisor  
D. AWS Cost and Usage Report  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Cost Explorer provides cost forecasting up to 12 months
- Based on historical usage patterns
- Interactive graphs showing predictions
- 80% confidence interval
- Budgets sets alerts but doesn't forecast
- Trusted Advisor provides recommendations
- Cost and Usage Report is for detailed analysis

**References:** Cost Explorer, Cost Forecasting
</details>

---

### Question 10
A company has 50 m5.large instances running continuously in us-east-1 with consistent usage. They want to purchase Reserved Instances. What type provides the highest discount?

A. Standard RI, 1-year, No Upfront  
B. Standard RI, 3-year, All Upfront  
C. Convertible RI, 3-year, All Upfront  
D. Convertible RI, 1-year, Partial Upfront  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Standard RIs provide higher discount than Convertible (up to 72%)
- 3-year term provides higher discount than 1-year
- All Upfront payment provides highest discount
- Consistent usage makes 3-year commitment viable
- Convertible RIs have lower discount (up to 54%)
- Partial/No Upfront have lower discounts

**References:** Reserved Instances, Discount Maximization
</details>

---

### Question 11
An RDS database runs continuously but only needs Multi-AZ during business hours for high availability. How can costs be optimized?

A. This is not possible; Multi-AZ cannot be toggled  
B. Disable Multi-AZ outside business hours, re-enable during business hours  
C. Use Aurora Serverless  
D. Use read replicas instead of Multi-AZ  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Multi-AZ can be enabled/disabled (causes brief downtime)
- For non-production databases, can disable outside business hours
- Reduces costs by ~50% when disabled
- Can be scripted/automated with Lambda
- Aurora Serverless has different use case
- Read replicas don't provide automatic failover

**Note:** This is only suitable for non-production workloads

**References:** RDS Multi-AZ, Cost Optimization
</details>

---

### Question 12
A company wants to track costs by department (Engineering, Marketing, Finance). How should they implement this?

A. Create separate AWS accounts for each department  
B. Use Cost Allocation Tags and activate them in the Billing console  
C. Use different regions for each department  
D. Create separate VPCs for each department  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Cost Allocation Tags enable tracking costs by custom dimensions
- Tag resources with "Department" key and values
- Activate tags in Billing console to appear in reports
- View costs grouped by department in Cost Explorer
- Separate accounts add management overhead
- Regions don't affect cost tracking
- VPCs don't enable cost tracking

**References:** Cost Allocation Tags, Cost Tracking
</details>

---

### Question 13
A Lambda function is configured with 3008 MB memory but only uses 512 MB. The function runs 10 million times per month. What should be done to optimize costs?

A. Increase memory to 10 GB  
B. Reduce memory allocation to 512 MB  
C. Switch to EC2  
D. Keep current configuration  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Lambda charges based on GB-seconds (memory × duration)
- Allocating 3008 MB when only 512 MB is used wastes money
- Reducing to 512 MB reduces costs ~6x
- Right-sizing memory is critical for Lambda cost optimization
- Increasing memory increases costs
- EC2 adds operational overhead
- Current configuration is wasteful

**Calculation:** 3008 MB vs 512 MB = 5.86x cost reduction

**References:** Lambda Pricing, Right-Sizing
</details>

---

### Question 14
A company has Reserved Instances that are expiring soon. They want to know if they should renew. Which Cost Explorer feature helps with this decision?

A. Cost forecasting  
B. Reserved Instance Utilization report  
C. Right-sizing recommendations  
D. Savings Plans recommendations  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- RI Utilization report shows how much Reserved capacity is used
- High utilization (>80%) indicates RI should be renewed
- Low utilization suggests downsizing or not renewing
- Also shows RI Coverage (what % of usage is covered)
- Cost forecasting predicts future costs
- Right-sizing is for instance size optimization
- Savings Plans recommendations compare to RIs

**References:** Reserved Instance Utilization, Cost Explorer
</details>

---

### Question 15
Data transfer costs are high for a web application serving static content globally. How can data transfer costs be reduced?

A. Use S3 Transfer Acceleration  
B. Use CloudFront as a CDN  
C. Move data to Glacier  
D. Use larger EC2 instances  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- CloudFront reduces data transfer from origin
- Caches content at edge locations globally
- Data transfer from CloudFront to users is cheaper than from EC2/S3
- Free data transfer from S3/EC2 to CloudFront
- S3 Transfer Acceleration accelerates uploads, doesn't reduce costs
- Glacier is for archival, not active content
- Instance size doesn't affect transfer costs

**References:** CloudFront, Data Transfer Costs
</details>

---

### Question 16
A company wants to set a budget of $10,000/month and receive alerts at 80% and 100% of budget. Which service should be used?

A. AWS Cost Explorer  
B. AWS Budgets  
C. CloudWatch Alarms  
D. AWS Trusted Advisor  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- AWS Budgets creates custom cost and usage budgets
- Set thresholds (80%, 100%) for alerts
- Sends SNS notifications when thresholds are exceeded
- Can set monthly, quarterly, or annual budgets
- Cost Explorer analyzes costs but doesn't alert
- CloudWatch monitors resources, not costs
- Trusted Advisor provides recommendations

**References:** AWS Budgets, Cost Alerts
</details>

---

### Question 17
A company has a mix of Convertible and Standard Reserved Instances. They want to change instance families due to application changes. Which RIs can be modified?

A. Only Standard RIs  
B. Only Convertible RIs  
C. Both can be modified  
D. Neither can be modified  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Convertible RIs can change instance family, OS, and tenancy
- Provides flexibility for changing requirements
- Standard RIs cannot change instance family
- Standard RIs can only change instance size within same family
- Trade-off: Convertible RIs have lower discount (54% vs 72%)

**References:** Reserved Instances, Convertible vs Standard
</details>

---

### Question 18
A database requires 3000 IOPS consistently. Currently using GP3 with 16,000 IOPS provisioned. What should be done to optimize costs?

A. Switch to GP2  
B. Reduce provisioned IOPS to 3000 on GP3  
C. Switch to Magnetic storage  
D. Keep current configuration  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- GP3 allows independent provisioning of IOPS
- Reduce from 16,000 to 3,000 IOPS to reduce costs
- Still provides required performance
- GP2 IOPS scale with volume size (less flexible)
- Magnetic storage has unpredictable performance
- Current configuration over-provisions by 5x

**References:** EBS GP3, Cost Optimization
</details>

---

### Question 19
A company wants to identify unused EBS volumes and old snapshots to reduce costs. Which tools can help?

A. AWS Trusted Advisor only  
B. AWS Cost Explorer only  
C. Both Trusted Advisor and custom scripts/AWS Config  
D. AWS Budgets  

<details>
<summary>Show Answer</summary>

**Answer: C**

**Explanation:**
- Trusted Advisor identifies unattached EBS volumes
- Custom scripts can identify old snapshots
- AWS Config Rules can detect unattached volumes
- Combine multiple approaches for comprehensive cleanup
- Cost Explorer shows costs but doesn't identify unused resources
- Budgets sets limits but doesn't identify waste

**References:** Trusted Advisor, Resource Cleanup
</details>

---

### Question 20
A company runs a web application with unpredictable traffic that can spike 10x instantly. They want to minimize costs while ensuring performance. What architecture should be used?

A. Fixed number of EC2 On-Demand instances  
B. EC2 Auto Scaling with target tracking + Spot Instances  
C. Large Reserved Instances  
D. Manual scaling with CloudWatch alarms  

<details>
<summary>Show Answer</summary>

**Answer: B**

**Explanation:**
- Auto Scaling automatically adjusts capacity based on demand
- Target tracking scales based on metrics (CPU, requests, etc.)
- Spot Instances reduce costs (up to 90%) for scale-out capacity
- Can combine On-Demand (baseline) + Spot (spikes)
- Fixed capacity wastes money during low traffic
- Reserved Instances charge for capacity even if unused
- Manual scaling is slow and error-prone

**References:** Auto Scaling, Spot Instances, Cost Optimization
</details>

---

## Summary

### Key Concepts Tested:
1. **EC2 Pricing Models**: On-Demand, Reserved, Savings Plans, Spot, Dedicated
2. **Reserved Instances**: Standard vs Convertible, payment options, discounts
3. **Savings Plans**: Compute vs EC2 Instance, flexibility
4. **Spot Instances**: Use cases, interruption handling, savings
5. **S3 Cost Optimization**: Storage classes, lifecycle policies
6. **Cost Management Tools**: Cost Explorer, Budgets, Trusted Advisor
7. **Right-Sizing**: Identifying underutilized resources
8. **Cost Allocation Tags**: Tracking costs by department/project
9. **Data Transfer Costs**: CloudFront, inter-region transfers
10. **Instance Scheduler**: Stopping resources outside business hours

### Exam Tips:
- ✅ Steady 24/7 workloads → Reserved Instances or Savings Plans (up to 72% savings)
- ✅ Fault-tolerant batch processing → Spot Instances (up to 90% savings)
- ✅ Unpredictable/mixed workloads → Compute Savings Plans (most flexible)
- ✅ Dev/test environments → Instance Scheduler (stop outside hours)
- ✅ Infrequent access after 30 days → S3 Glacier Deep Archive
- ✅ Unknown access patterns → S3 Intelligent-Tiering
- ✅ Cost tracking by department → Cost Allocation Tags
- ✅ Identify underutilized resources → Cost Explorer Right-Sizing + Trusted Advisor
- ✅ Budget alerts → AWS Budgets
- ✅ Standard RI (72%) vs Convertible RI (54%) discount
- ✅ CloudFront reduces data transfer costs
- ✅ 3-year All Upfront provides maximum RI discount

