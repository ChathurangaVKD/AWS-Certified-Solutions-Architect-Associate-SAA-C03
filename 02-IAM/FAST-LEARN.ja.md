# ⚡ Fast Learning - IAM (Identity & Access Management)

> **完了時間**: 45-60分 | **試験配点**: 約15-20%

## 🎯 必須理解コンセプト（5分）

### IAMの三位一体 (UPGR)
```
USERS → GROUPS → POLICIES → ROLES
People   Collections   Permissions   Services
```

**記憶法**: "U Go Play Rugby" = Users, Groups, Policies, Roles

### 黄金ルール
1. **Root user** = 日常タスクでは絶対に使わない
2. **IAM users** = 人とアプリケーション
3. **Roles** = AWSサービスと一時アクセス
4. **Policies** = 権限を定義するJSONドキュメント
5. **Groups** = ユーザーを整理し、ポリシーを適用

## 📊 クイックリファレンステーブル

### IAMコンポーネント早見表
| Component | Who/What | Credentials | Best For |
|-----------|----------|-------------|----------|
| **Users** | People/Apps | Long-term | Individual access |
| **Groups** | User collections | None | Organize by job function |
| **Roles** | AWS services | Temporary | EC2, Lambda, cross-account |
| **Policies** | JSON rules | None | Define permissions |

### ポリシータイプ (MIIR)
| Type | Scope | Use Case |
|------|-------|----------|
| **M**anaged - AWS | AWSが事前作成 | 一般的な権限 |
| **M**anaged - Customer | 自分で作成して再利用 | カスタム再利用 |
| **I**nline | 1エンティティにアタッチ | 1:1の厳密な関係 |
| **I**dentity-based | Users/Groups/Roles | 誰が何をできるか |
| **R**esource-based | Resources (S3, etc) | 誰がこれにアクセスできるか |

## 🔥 試験頻出トピック

### 1. IAMポリシー構造 (VESPARC)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow/Deny",
    "Principal": "who",
    "Action": "service:operation",
    "Resource": "arn:aws:service:region:account:resource",
    "Condition": "optional conditions"
  }]
}
```

**記憶法**: **V**ery **E**ffective **S**tatements **P**rovide **A**ctions on **R**esources with **C**onditions

### 2. Explicit Deny が最優先！
```
Decision Flow:
1. デフォルト = DENY
2. 明示的DENYを確認 → あればDENY（ここで終了）
3. 明示的ALLOWを確認 → あればALLOW
4. ALLOWがなければ → DENY
```

**ルール**: Explicit DENY > Explicit ALLOW > Default DENY

### 3. クロスアカウントアクセス
```
Account A                    Account B
├── User needs access   →   ├── Resource (S3)
└── Assume Role         →   └── Trust Policy
```

**手順**: Account Bでロール作成 → trust policy追加 → ユーザーがロールを引き受ける

## 💡 よくある試験シナリオ

### Scenario 1: EC2にS3アクセスを付与
**Question**: EC2インスタンスがS3バケットにアクセスする必要がある
**❌ WRONG**: EC2に認証情報を保存する
**✅ CORRECT**: IAM roleを作成し、EC2インスタンスにアタッチする

### Scenario 2: サードパーティへの一時アクセス
**Question**: 外部監査人に一時的なアクセスが必要
**✅ CORRECT**: trust policy付きのIAM roleを使用し、一時認証情報を提供する

### Scenario 3: IPアドレスで制限
**Question**: オフィスIPからのみS3アクセスを許可したい
**✅ CORRECT**: `aws:SourceIp` を使ったConditionを使用

```json
"Condition": {
  "IpAddress": {
    "aws:SourceIp": "203.0.113.0/24"
  }
}
```

### Scenario 4: 機密操作にMFA必須
**Question**: S3オブジェクト削除時にMFAを要求したい
**✅ CORRECT**: `aws:MultiFactorAuthPresent` を使ったConditionを使用

## 🎓 速習のコツ

### 1分ドリル
- **Users** = 長期認証情報
- **Roles** = 一時認証情報
- **Groups** = ネスト不可（groupsの中にgroupsは不可）
- **Policies** = JSON権限ドキュメント
- **IAM** = グローバルサービス（リージョナルではない）

### MFAオプション (VHAS)
| Type | Example | Use Case |
|------|---------|----------|
| **V**irtual | Google Authenticator | 最も一般的 |
| **H**ardware | YubiKey | 高セキュリティ |
| **A**WS | AWS device | AWS固有 |
| **S**MS | Text message | 非推奨（推奨されない） |

### アクセスタイプ
```
1. CONSOLE ACCESS
   └── Username + Password (+ MFA)

2. PROGRAMMATIC ACCESS
   └── Access Key ID + Secret Access Key
```

## 📝 ラピッドファイア事実集

### IAMベストプラクティス（Top 10）
1. ✅ rootアカウントでMFAを有効化
2. ✅ 日常タスクでrootを使わない
3. ✅ 個別のIAM usersを作成
4. ✅ 権限付与はgroupsを使用
5. ✅ 最小権限を付与
6. ✅ EC2/Lambdaにはrolesを使用
7. ✅ 認証情報を定期的にローテーション
8. ✅ 強力なpassword policyを使用
9. ✅ CloudTrailで監視
10. ✅ 不要な認証情報を削除

### 重要な上限値
- 1アカウントあたり最大 **5,000 users**
- 1アカウントあたり最大 **300 groups**
- 1ユーザーは最大 **10 groups** に所属可能
- 1ユーザーあたり最大 **2 access keys**
- 1 user/group/roleあたり最大 **10 managed policies**

### ポリシー評価ロジック
```
1. DENY（デフォルト）から開始
2. すべてのポリシーを評価
3. 明示的DENYあり？ → 即DENY
4. 明示的ALLOWあり？ → ALLOW
5. ALLOWなし？ → DENY
```

## 🔐 セキュリティ機能クイックガイド

### Password Policyの構成要素
- 最小文字数
- 大文字を必須化
- 小文字を必須化
- 数字を必須化
- 記号を必須化
- パスワード有効期限
- 再利用防止

### Access Keysのベストプラクティス
- コードリポジトリに絶対にコミットしない
- 90日ごとにローテーション
- 未使用なら削除
- 可能ならIAM rolesを代わりに使う

## 🚀 5分マスターレビュー

### IAMチートシート
1. **Users**: 永続的な認証情報、access keysは最大2つ
2. **Groups**: ユーザー整理用、ネスト不可、認証情報なし
3. **Roles**: 一時認証情報、サービス用＆クロスアカウント用
4. **Policies**: JSON権限、explicit denyが優先
5. **Root**: MFA有効化、厳重保管、日常利用しない
6. **Service**: グローバル（リージョナルではない）、無料
7. **Best Practice**: 常に最小権限

### 避けるべきよくあるミス
❌ 日常タスクでrootアカウントを使う
❌ コードに認証情報を埋め込む
❌ roleで足りるのにaccess keysを作成する
❌ 広すぎる権限を付与する（最小権限を使う）
❌ 認証情報ローテーションを忘れる
❌ 特権アカウントでMFAを有効化しない
❌ groupsの中にgroupsを入れられると思い込む（できない！）

## 🎯 試験練習スピードラン

**Policy Decision Questions** (答えは下部)

1. User has ALLOW in identity policy, DENY in resource policy. Result? __
2. No explicit policies attached to user. Result? __
3. Best way to give EC2 access to DynamoDB? __
4. Can groups be nested? __
5. IAM is regional or global? __
6. Maximum access keys per user? __

---

### 必ず暗記すべきPolicy Conditions

| Condition | Purpose | Example Use |
|-----------|---------|-------------|
| `aws:SourceIp` | IP制限 | オフィス限定アクセス |
| `aws:MultiFactorAuthPresent` | MFA必須化 | 機密操作 |
| `aws:CurrentTime` | 時間ベース | 営業時間のみ |
| `aws:SecureTransport` | HTTPS強制 | 安全な接続 |
| `aws:userid` | 特定ユーザー | ユーザー別アクセス |

## ⏱️ 次のステップ
- 学習時間: 約45-60分
- 演習: サンプルポリシーを書く
- 準備完了: IAM practice questions
- 次へ: Module 03 - Compute

---

**Quick Answers**: 
1) DENY (explicit deny wins)
2) DENY (default)
3) IAM Role attached to EC2
4) No
5) Global
6) 2
