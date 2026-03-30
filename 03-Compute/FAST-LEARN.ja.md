# ⚡ Fast Learning - Compute Services

> **完了時間**: 60-90 分 | **試験配点**: ~20-25%

## 🎯 必須理解コンセプト（5分）

### Computeサービス選定ガイド
```
NEED VMS? → EC2
NEED SERVERLESS? → Lambda
NEED CONTAINERS? → ECS/EKS/Fargate
NEED PAAS? → Elastic Beanstalk
NEED AUTO-SCALE? → Auto Scaling Group
NEED LOAD BALANCE? → ALB/NLB/GWLB
```

**記憶法**: "VeLoCiraptor Eats Lamb" = VM, Lambda, Containers, Elastic Beanstalk, Auto Scale, Load Balance

## 📊 クイックリファレンステーブル

### EC2インスタンスタイプ (CRAM-FACTS-PIG)
| Family | Name | 用途 | Example |
|--------|------|----------|---------|
| **C** | Compute | CPU重視 | バッチ処理, gaming |
| **R** | RAM | メモリ重視 | Databases, caching |
| **M** | Medium | 汎用 | Web servers, apps |
| **T** | Tiny/Turbo | Burstable | Dev/test, low traffic |
| **P/G** | GPU | Graphics/ML | 機械学習, rendering |
| **I/D/H** | I/O | ストレージ重視 | Databases, data warehousing |

**Format**: `t3.medium` = Family(t) + Generation(3) + Size(medium)

### EC2料金モデル (OSRSD)
| Model | Discount | Commitment | 用途 | Interruption |
|-------|----------|------------|----------|--------------|
| **O**n-Demand | 0% | なしne | 短期・予測困難 | なし |
| **S**pot | Up to 90% | なしne | 耐障害性あり | あり (2分 notice) |
| **R**eserved | Up to 72% | 1-3 years | 常時稼働 | なし |
| **S**avings Plans | Up to 66% | 1-3 years | 柔軟 | なし |
| **D**edicated | 0% | なしne/1-3 yr | Compliance, licensing | なし |

## 🔥 試験頻出トピック

### 1. Load Balancer選定（最重要）
| Type | レイヤー | Protocol | 用途 | 主要機能 |
|------|-------|----------|----------|--------------|
| **ALB** | 7 | HTTP/HTTPS | Microservices, containers | Path/host routing, Lambda targets |
| **NLB** | 4 | TCP/UDP/TLS | Extreme performance | Static IP, millions req/s |
| **GWLB** | 3 | IP | Security appliances | Firewalls, IDS/IPS |
| **CLB** | 4 & 7 | HTTP/TCP | 旧世代 (避ける) | Deprecated |

**記憶法**: "ALN your Goals" = ALB (apps), NLB (network), GWLB (gateway)

### 2. Auto Scalingポリシー
```
1. TARGET TRACKING (最も一般的)
   └── "Keep CPU at 50%"
   
2. STEP SCALING
   └── CPU 60-70% → +1 instance
   └── CPU 70-80% → +2 instances
   
3. SCHEDULED SCALING
   └── "Add 10 instances at 8 AM daily"
   
4. PREDICTIVE SCALING
   └── ML-based forecasting
```

**試験のコツ**: Target Tracking = Set it and forget it (easiest)

### 3. Placement Groups
| Type | Placement | AZ | 用途 | 最大 Performance |
|------|-----------|-----|----------|-----------------|
| **Cluster** | Same rack | Single | HPC, low latency | 10 Gbps |
| **Spread** | Different racks | Multi | Critical instances | 7/AZ max |
| **Partition** | Different racks | Multi | Distributed apps (Hadoop) | Multiple partitions |

**記憶法**: "CSP" = Cluster (Speed), Spread (Safety), Partition (Parts)

### 4. Lambda 基本事項
```
MAX TIMEOUT: 15 分
MAX MEMORY: 10,240 MB (10 GB)
MAX /tmp STORAGE: 10 GB
MAX DEPLOYMENT SIZE: 50 MB (zipped), 250 MB (unzipped)
CONCURRENT EXECUTIONS: 1,000 (デフォルト, can increase)
```

**Pricing**: Pay per request + duration (GB-seconds)

## 💡 よくある試験シナリオ

### Scenario 1: コスト最適化
**質問**: Database runs 24/7, how to reduce cost?
**✅ 正解**: Reserved Instances (1-3 year commitment)

### Scenario 2: 変動トラフィック対応
**質問**: Traffic spikes unpredictably, need to scale
**✅ 正解**: Auto Scaling Group with Target Tracking policy

### Scenario 3: 極限パフォーマンスが必要
**質問**: Need millions of requests/sec, static IP
**✅ 正解**: Network Load Balancer (NLB)

### Scenario 4: マイクロサービスのルーティング
**質問**: Route /api to API servers, /images to image servers
**✅ 正解**: Application Load Balancer with path-based routing

### Scenario 5: 短時間処理・サーバーレス
**質問**: Process images when uploaded, run < 5分
**✅ 正解**: Lambda triggered by S3 event

### Scenario 6: 中断許容のバッチジョブ
**質問**: バッチ処理, can restart if interrupted
**✅ 正解**: Spot Instances (up to 90% cheaper)

### Scenario 7: 低遅延HPCクラスター
**質問**: High-performance computing, need lowest latency
**✅ 正解**: Cluster Placement Group

## 🎓 速習のコツ

### EC2 User Data vs Metadata
```
USER DATA (Bootstrap)
└── Scripts run at launch
└── http://169.254.169.254/latest/user-data

METADATA (Instance info)
└── Instance info, IP, security groups
└── http://169.254.169.254/latest/meta-data
```

### Auto Scalingの重要概念
- **Min**: Minimum instances (always running)
- **Desired**: Current target
- **最大**: 最大imum instances (cost limit)
- **Cooldown**: Wait period (デフォルト 300s)
- **Health Check**: EC2 status or ELB health

### Load Balancer機能マトリクス
| Feature | ALB | NLB | GWLB |
|---------|-----|-----|------|
| Path routing | ✅ | ❌ | ❌ |
| Host routing | ✅ | ❌ | ❌ |
| Lambda targets | ✅ | ❌ | ❌ |
| Static IP | ❌ | ✅ | ❌ |
| PrivateLink | ❌ | ✅ | ✅ |
| Cross-zone LB | ✅ (always) | ❌ (optional) | ✅ |

## 📝 ラピッドファイア事実集

### Reserved Instanceの種類
1. **Standard**: 72% discount, can't change instance family
2. **Convertible**: 66% discount, can change instance family
3. **Scheduled**: For predictable schedules

### Savings Plansの種類
1. **Compute**: 最も柔軟 (EC2, Lambda, Fargate)
2. **EC2**: 柔軟性は低め (specific instance family)
3. **SageMaker**: ML workloads のみ

### Container Services 使い分け
| Service | Management | 用途 |
|---------|------------|----------|
| **ECS** | AWS-native | AWS-のみ containers |
| **EKS** | Kubernetes | K8s compatibility |
| **Fargate** | Serverless | サーバー管理不要 |

**記憶法**: ECS = Easy, EKS = Kubernetes, Fargate = Forget servers

### Lambdaトリガー（主要）
- API Gateway (REST APIs)
- S3 Events (upload/delete)
- DynamoDB Streams
- CloudWatch Events/EventBridge
- SQS queues
- SNS topics
- ALB targets

## 🚀 5分マスターレビュー

### Compute意思決定ツリー
```
1. サーバーが必要か？ 
   NO → Lambda (if < 15分) or Fargate
   あり → Continue
   
2. 24/7で常時稼働か？
   あり → Reserved Instances
   NO → Continue
   
3. 中断を許容できるか？
   あり → Spot Instances
   NO → On-Demand
   
4. ロードバランサーが必要か？
   HTTP/HTTPS → ALB
   TCP/extreme performance → NLB
   Security appliances → GWLB
```

### Auto Scalingベストプラクティス
✅ Use Target Tracking (最もシンプル)
✅ Multi-AZ for high availability
✅ Use ELB health checks (better than EC2)
✅ Set appropriate cooldown period
✅ Monitor with CloudWatch

### 避けるべきよくあるミス
❌ Using On-Demand for steady workloads (use Reserved)
❌ なしt using Auto Scaling for variable loads
❌ Single AZ deployment (no HA)
❌ ALB for TCP/UDP (use NLB)
❌ Forgetting Spot can be interrupted
❌ Lambda for long-running tasks (15分 max)

## 🎯 試験練習スピードラン

**Quick 質問s**（答えは下）

1. Lambdaの最大タイムアウトは？ __
2. マイクロサービスに最適なLBは？ __
3. 耐障害性ワークロードで最安の料金モデルは？ __
4. Spread placement groupでAZあたり最大インスタンス数は？ __
5. Static IPを持つLBは？ __
6. Auto Scaling cooldown デフォルト? __
7. ALBは何層？ __
8. Reserved Instancesは中断される？ __

---

### Instance Store vs EBS
```
INSTANCE STORE (Ephemeral)
├── Physically attached
├── Very fast
├── Data lost on stop/terminate
└── Use: Temporary data, cache

EBS (Persistent)
├── Network attached
├── Fast
├── Data persists
└── Use: Database, OS, permanent data
```

### EBSボリュームタイプ早見表
| Type | IOPS | Throughput | 用途 |
|------|------|------------|----------|
| gp3/gp2 | 16,000 | 1,000 MB/s | 汎用 (boot) |
| io2/io1 | 64,000+ | 1,000 MB/s | Databases, critical |
| st1 | 500 | 500 MB/s | Big data, logs |
| sc1 | 250 | 250 MB/s | Cold data |

## ⏱️ 次のステップ
- 学習時間: ~60-90分
- 演習: Launch EC2, create ASG, configure ALB
- 準備完了: Compute practice questions
- 次へ: Module 04 - Storage

---

**Quick 答えs**: 
1) 15 分
2) ALB (Application Load Balancer)
3) Spot Instances (up to 90% off)
4) 7 instances
5) NLB (Network Load Balancer)
6) 300 seconds
7) レイヤー 7 (Application)
8) なし

