# 🎮 Interactive Playbooks

Self-contained HTML playbooks, one per topic. Open them on the [study site](https://chathurangavkd.github.io/AWS-Certified-Solutions-Architect-Associate-SAA-C03/playbooks/) or locally in any browser (no build step, no dependencies besides Google Fonts).

Each playbook has:

- **Lessons** — 5–15 minutes each, with comparison tables and exam traps
- **Simulators** — small interactive tools that show *why* an answer is right
- **Game** — 16 "pick the service" scenarios
- **Quiz** — 12–20 exam-style questions with explanations
- **Cheat sheet** — keyword → answer pairs for last-day review

| Playbook | Module | Interactive parts | Quiz |
|----------|--------|-------------------|------|
| [AWS Fundamentals](fundamentals.html) | 01 | "Where should it run?" tier picker, global/Regional/zonal sorter, shared-responsibility matrix, ARN decoder, Well-Architected pillar sorter | 20 |
| [IAM](iam.html) | 02 | Policy evaluation simulator, policy JSON builder, Allowed-or-Denied game | 12 |
| [EC2 & Scaling](ec2.html) | 03 | Instance-name decoder, stop/hibernate/terminate table, purchase-option break-even chart, target-tracking simulator, ALB rule router | 20 |
| [Serverless & Containers](serverless.html) | 03 | Compute picker, Lambda concurrency calculator, task role vs execution role sorter | 20 |
| [Storage](storage.html) | 04 | Lifecycle-rule builder with timeline, versioning simulator | 20 |
| [Database](database.html) | 05 | Database chooser, Multi-AZ availability lab, Aurora storage-quorum simulator, DynamoDB capacity calculator | 20 |
| [Networking](networking.html) | 06 | CIDR calculator, route-table simulator, peering mesh vs Transit Gateway | 18 |
| [Security](security.html) | 07 | Security group vs NACL packet simulator, KMS and encryption choices | 17 |
| [Application Integration](integration.html) | 08 | SQS message-lifecycle simulator, SNS filter policies, EventBridge rule matcher, Step Functions order workflow | 20 |
| [Monitoring](monitoring.html) | 09 | Which-service sorter, CloudWatch alarm M-of-N simulator, management vs data event picker | 20 |
| [Migration & Transfer](migration.html) | 10 | 7 Rs picker, network vs Snowball transfer-time calculator | 20 |
| [Analytics](analytics.html) | 11 | Pipeline builder, Kinesis shard calculator, Athena cost calculator | 20 |
| [Architecture Patterns](architecture.html) | 12 | HA failure simulator, RTO/RPO DR strategy picker, SQS vs direct-call spike chart | 20 |
| [Cost Optimization](cost.html) | 13 | Savings Plan / On-Demand / Spot blend calculator, data-transfer path pricing, NAT vs gateway endpoint savings | 20 |

**Progress** is stored in your browser's `localStorage` (one key prefix per playbook). Nothing is sent anywhere.

**Content** is original and follows the [Content Policy](../CONTENT-POLICY.md): no exam dumps or copyrighted questions. Prices in calculators are illustrative and labelled as such.
