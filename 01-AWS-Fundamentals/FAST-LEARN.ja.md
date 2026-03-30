# ⚡ Fast Learning - AWS Fundamentals

> **完了時間**: 30-45分 | **試験配点**: 基礎領域として約10%

## 🎯 必須理解コンセプト（5分）

### AWS グローバルインフラ - 3つの柱
```
REGIONS → AVAILABILITY ZONES → EDGE LOCATIONS
  30+           3-6 per region        400+
Isolated      Independent DCs      CDN endpoints
```

**記憶法: "RAE" = Regions, AZs, Edge**

### 覚えるべき重要な数字
- **Regions**: 世界で30以上
- **1リージョンあたりのAZ数**: 最低3、通常3-6
- **Edge Locations**: 400以上（最も数が多い）
- **Local Zones**: 超低遅延向けにリージョンを拡張する仕組み

## 📊 クイックリファレンステーブル

### リージョン選定基準 (CPAS)
| Factor | 問うべきこと |
|--------|-------------|
| **C**ompliance | データ主権・法令要件を満たせるか？ |
| **P**roximity | ユーザーはどこにいるか？ |
| **A**vailability | 必要サービスがそのリージョンで使えるか？ |
| **S**pending | コストは許容範囲か？ |

### Well-Architected Framework - 6つの柱 (OSCRPS)
| Pillar | 重要な問い | クイックヒント |
|--------|------------|----------------|
| **O**perational Excellence | 運用・監視できる設計か？ | 自動化を徹底 |
| **S**ecurity | データとシステムを守れているか？ | 多層防御 |
| **C**ost Optimization | 無駄なコストを減らせるか？ | 使った分だけ払う |
| **R**eliability | 障害から復旧できるか？ | Multi-AZを基本に |
| **P**erformance Efficiency | リソース選定は適切か？ | ワークロードに合わせる |
| **S**ustainability | 環境負荷を最小化できるか？ | 利用効率を最適化 |

## 🔥 試験頻出トピック

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

**覚え方**: AWS = HARDWARE側、あなた = SOFTWARE & DATA側

### 2. 高可用性（HA）パターン
```
✅ CORRECT: 同一リージョン内の複数AZに分散配置
❌ WRONG: 単一AZのみ
❌ WRONG: HA目的で複数リージョン（それはDRの文脈）
```

### 3. AWS 管理ツール - 使い分け早見表
| Tool | 最適な用途 | 試験での典型シナリオ |
|------|------------|----------------------|
| Console | 画面操作・学習向け | 単発タスク |
| CLI | 自動化・スクリプト | 繰り返し作業 |
| SDK | アプリコードから操作 | アプリ開発 |
| CloudFormation | Infrastructure as Code | 環境の再現 |

## 💡 よくある試験シナリオ

### Scenario 1: レイテンシを最小化したい
**質問**: 欧州ユーザーの遅延が高い
**答え**: EUリージョン（例: `eu-west-1`）に配置し、静的コンテンツは CloudFront を利用

### Scenario 2: 高可用性を確保したい
**質問**: データセンター障害でもアプリを継続稼働させたい
**答え**: 同一リージョンの複数AZへ配置（Multi-AZ）

### Scenario 3: 災害対策（DR）
**質問**: リージョン全体障害に備えたい
**答え**: 別リージョンへバックアップ／レプリケーション

### Scenario 4: データコンプライアンス
**質問**: データを国外に出せない
**答え**: 対象国内リージョンを選び、データレジデンシー要件を検証

## 🎓 速習のコツ

### 1分ドリル
- Region = 地理的なエリア（複数のAZを含む）
- AZ = 独立したデータセンター群
- Edge = キャッシュ配信拠点（低遅延化）

### AWS Organizations - マルチアカウント管理
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

**主要コンセプト:**
- **Organizations**: 複数アカウントを中央管理
- **OUs (Organizational Units)**: アカウントを論理的にグルーピング
- **SCPs (Service Control Policies)**: 「最大権限」のガードレール
- **Consolidated Billing**: 請求一本化＋ボリュームディスカウント

### Service Control Policies (SCPs) - 試験超重要
```
❌ SCPs DO NOT grant permissions
✅ SCPs set maximum permissions (guardrails)
❌ SCPs DO NOT affect management account
✅ SCPs affect all member accounts
✅ Effective permissions = IAM policy AND SCP
```

**SCPの典型ユースケース:**
| Scenario | SCP Action |
|----------|------------|
| 利用リージョンを制限 | 許可リージョン外の操作をDeny |
| 暗号化を必須化 | 暗号化なしリソース作成をDeny |
| 組織離脱を防止 | `organizations:LeaveOrganization` をDeny |
| CloudTrail保護 | ログ削除・改ざん操作をDeny |

**SCP クイック例:**
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
| セットアップ | 手動 | 自動（数分） |
| ガードレール | 手動SCP | 事前定義 + カスタム |
| アカウント作成 | 手動 | Account Factory |
| 向いている用途 | 柔軟カスタム | 迅速導入・ベストプラクティス |

**試験のコツ**: Control Tower = Organizations + Automation + Best Practices

### AWS Resource Access Manager (RAM)
**目的**: AWSアカウント間でリソース共有

**最頻出ユースケース**: VPC Subnet Sharing
```
Networking Account
└── VPC with Subnets
    ↓ (shared via RAM)
Application Accounts
└── Launch EC2 in shared subnets
```

**メリット:**
- ✅ ネットワーク管理を一元化
- ✅ VPC乱立を抑制
- ✅ IPアドレス利用を効率化
- ✅ リソース重複を回避

**その他の共有可能リソース:**
- VPC Subnets（最頻出）
- Transit Gateway
- Route 53 Resolver rules
- Aurora clusters
- License Manager configs

### Consolidated Billing の利点
1. **Single Bill**: 全アカウントを1つの請求に集約
2. **Volume Discounts**: 利用量合算で単価優遇
3. **RI Sharing**: Reserved Instancesをアカウント横断で共有
4. **Cost Allocation**: 組織全体でタグ配賦

**例:**
```
Account 1: 500 GB S3
Account 2: 800 GB S3
Account 3: 700 GB S3
Total: 2,000 GB → 上位料金ティアが全体に適用
```
- Multi-AZ = High Availability
- Multi-Region = Disaster Recovery

### 避けるべきよくあるミス
❌ AZ と Region を混同する
❌ Edge Locations = Regions だと誤解する
❌ HAなのに単一AZで構成する
❌ すべてのサービスが全リージョンで使えると思い込む
❌ 責任共有モデルの境界を忘れる

## 📝 ラピッドファイア事実集

**Global vs Regional サービス:**
- **Global**: IAM, CloudFront, Route 53, WAF
- **Regional**: EC2, RDS, VPC, Lambda, S3（グローバル名前空間に注意）

**Service Categories (CSDMANS):**
- **C**ompute: EC2, Lambda
- **S**torage: S3, EBS, EFS
- **D**atabase: RDS, DynamoDB
- **M**onitoring: CloudWatch, CloudTrail
- **A**nalytics: Athena, EMR
- **N**etworking: VPC, Route 53
- **S**ecurity: IAM, KMS, Secrets Manager

## 🚀 5分マスターレビュー

1. **Infrastructure**: Regions → AZs → Edge Locations（カバー範囲大→小）
2. **HA戦略**: 同一リージョン内の複数AZを使う
3. **DR戦略**: 別リージョンへバックアップ
4. **Well-Architected**: 6つの柱（OSCRPS）
5. **責任共有**: AWS = インフラ側、あなた = データ/設定側
6. **リージョン選定**: Compliance → Proximity → Availability → Spending（CPAS）

## 🎯 試験練習スピードラン

**Quick Questions**（答えは下）
1. 1リージョンあたりのAZ最小数は？ __
2. 低遅延CDNを提供するのは？ __
3. Hypervisor の保護責任者は？ __
4. HAのために複数配置するのは？ __
5. IAMはグローバル？リージョナル？ __

---

**Answers**: 1) 3  2) CloudFront/Edge Locations  3) AWS  4) AZs  5) Global

## ⏱️ 次のステップ
- 学習時間: 約30分
- 準備完了: Practice questions
- 次へ: Module 02 - IAM
