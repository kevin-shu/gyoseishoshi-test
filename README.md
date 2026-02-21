# 行政書士試験 學習資料

日本行政書士試験準備用的法條對照網站。提供日文原文、繁體中文翻譯、白話講解三層結構，方便中文母語者理解日本法律。

## 目的

- 為準備行政書士試験的中文母語考生提供雙語法條參考資料
- 每條條文包含：**日文原文**（現行法）→ **繁體中文翻譯** → **白話講解**（考試重點解說）
- 標注重要改正變更點【改正】及考試頻出條文【重要】

## 目前收錄範圍

### 法條教材

- **民法第一編 総則**（第 1 条〜第 174 条の 2）— 全 7 章完成
- **民法第二編 物権**（第 175 条〜第 398 条の 22）— 全 7 章完成
- **民法第三編 債権 第一・二章**（第 399 条〜第 696 条）— 全 2 章完成
- **行政法総論** — 理論體系 7 章完成
- **行政事件訴訟法**（第 1 条〜第 46 条）— 全 5 章完成
- **行政手続法**（第 1 条〜第 46 条）— 全 5 章完成（小章節合併）
- **行政不服審査法**（第 1 条〜第 87 条）— 全 6 章完成
- **基礎知識**（一般知識・諸法令・情報通信・文章理解）— 全 4 章完成

### 練習問題（過去問）

- **民法第一編 総則** — 全 7 章完成（択一式 32 題 + 記述式 5 題）
- **民法第二編 物権** — 全 7 章完成（択一式 16 題）
- **民法第三編 債権 第一・二章** — 全 2 章完成（択一式 12 題 + 出題例 4 題）
- **行政事件訴訟法** — 全 5 章完成
- **行政手続法** — 全 5 章完成
- **行政不服審査法** — 全 6 章完成
- **基礎知識** — 全 4 章完成

## 行政法 出題範圍

行政書士試験中配分最高的科目（112 分 / 300 分 = 37.3%），由以下法律群構成：

### 主要 6 大領域

| 法律 | 略稱 | 択一式 | 其他出題 | 重要度 |
|------|------|--------|----------|--------|
| 行政法総論（一般的法理論） | 行政総論 | ~3 題 | 多肢選択頻出 | ★★★ |
| 行政手続法 | 行手法 | ~3 題 | 記述式偶有 | ★★★ |
| 行政不服審査法 | 行審法 | ~3 題 | | ★★★ |
| 行政事件訴訟法 | 行訴法 | ~3-4 題 | 記述式幾乎每年出 | ★★★★ |
| 国家賠償法 | 国賠法 | ~2 題 | | ★★☆ |
| 地方自治法 | 地自法 | ~3-4 題 | | ★★★ |

### 補助法律（不定期出題）

- 情報公開法（行政機関の保有する情報の公開に関する法律）
- 公文書管理法（公文書等の管理に関する法律）
- 行政代執行法

### 行政法 出題形式

| 形式 | 題數 | 配分 |
|------|------|------|
| 5 肢択一式 | 19 題 | 76 分 |
| 多肢選択式（穴埋め） | 2 題 | 16 分 |
| 記述式（40 字） | 1 題 | 20 分 |
| **合計** | **22 題** | **112 分** |

## 基礎知識科目 出題範圍

基礎知識科目（14 題 / 56 分）有**足切り**：24 分未満即不合格。令和 6 年度起從舊「一般知識等」改名並擴充為四大分類。

### 四大分類與近年出題數

| 分類 | R4 (2022) | R5 (2023) | R6 (2024) | R7 (2025) |
|------|:---------:|:---------:|:---------:|:---------:|
| 一般知識（政治・経済・社会） | 7 | 7 | 5 | 6 |
| 行政書士法等関連諸法令 | — | — | 2 | 2 |
| 情報通信・個人情報保護 | 4 | 4 | 4 | 3 |
| 文章理解 | 3 | 3 | 3 | 3 |

> R6 起新增「行政書士法等関連諸法令」，壓縮一般知識出題數。全題 5 肢択一式、每題 4 分。

### 各分類核心考點

| 分類 | 主要出題對象 |
|------|-------------|
| 一般知識 | 各國政治體制、日本選挙制度、行政改革、國際組織、GDP・為替、社会保障、少子高齢化、時事問題 |
| 諸法令 | 行政書士法、戸籍法、住民基本台帳法（條文知識直接出題） |
| 情報通信・個人情報保護 | 個人情報保護法、情報公開法、公文書管理法、IT 用語、生成 AI、マイナンバー |
| 文章理解 | 要旨把握・空欄補充・文章並替（評論文、正答率 90% 以上） |

## 技術

- [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — 靜態網站產生器
- CJK 全文搜尋（日文 + 中文）— 透過 [jieba](https://github.com/fxsjy/jieba) 中文分詞
- 深色 / 淺色模式切換
- 字體：Noto Sans JP

## 資料來源

- [e-Gov 法令検索 — 民法](https://laws.e-gov.go.jp/law/129AC0000000089) — 民法原始出處
  - 本地副本：[`references/civil-code.xml`](references/civil-code.xml)（令和 8 年 4 月 1 日施行版）
- [e-Gov 法令検索 — 行政手続法](https://laws.e-gov.go.jp/law/405AC0000000088)
- [e-Gov 法令検索 — 行政不服審査法](https://laws.e-gov.go.jp/law/426AC0000000068)
- [e-Gov 法令検索 — 行政事件訴訟法](https://laws.e-gov.go.jp/law/337AC0000000139)
- [e-Gov 法令検索 — 国家賠償法](https://laws.e-gov.go.jp/law/322AC0000000125)
- [e-Gov 法令検索 — 地方自治法](https://laws.e-gov.go.jp/law/322AC0000000067)
- 翻譯及講解為自行編寫，並與官方 XML 逐條比對校正

## 本地啟動

```bash
# 建立虛擬環境（首次）
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate

# 安裝依賴（首次）
pip install mkdocs-material jieba

# 啟動開發伺服器
mkdocs serve
```

瀏覽器開啟 http://127.0.0.1:8000

## 部署

網站透過 GitHub Pages 部署，使用 `gh-pages` 分支。

```bash
# 啟動虛擬環境
source venv/bin/activate

# 建構並部署到 GitHub Pages
mkdocs gh-deploy
```

部署完成後網站位於：https://kevin-shu.github.io/gyoseishoshi-test/

GitHub Pages 設定：**Settings → Pages → Source: Deploy from a branch → Branch: `gh-pages` / `/ (root)`**

## 專案結構

```
├── mkdocs.yml                         # MkDocs 配置
├── docs/
│   ├── index.md                       # 首頁（章節索引）
│   ├── study-plan.md                  # 學習計畫
│   ├── civil-code/
│   │   ├── book1-general/             # 民法 第一編 総則（條文對照）
│   │   │   ├── ch01-general-rules.md  # 第1章 通則
│   │   │   ├── ch02-persons.md        # 第2章 人
│   │   │   ├── ch03-juridical-persons.md
│   │   │   ├── ch04-things.md         # 第4章 物
│   │   │   ├── ch05-juridical-acts.md # 第5章 法律行為
│   │   │   ├── ch06-periods.md        # 第6章 期間の計算
│   │   │   └── ch07-prescription.md   # 第7章 時効
│   │   └── book2-property/            # 民法 第二編 物権（條文對照）
│   │       ├── ch01-general-rules.md  # 第1章 総則（物権変動・登記）
│   │       ├── ch02-possession.md     # 第2章 占有権
│   │       ├── ch03-ownership.md      # 第3章 所有権
│   │       ├── ch04-land-rights.md    # 第4〜6章 用益物権
│   │       ├── ch05-security-interests.md # 第7〜8章 留置権・先取特権
│   │       ├── ch06-pledge.md         # 第9章 質権
│   │       └── ch07-mortgage.md       # 第10章 抵当権
│   ├── admin-law/
│   │   ├── general-theory/            # 行政法 総論（理論體系）
│   │   │   ├── ch01-principles.md     # 第1章 基本原理
│   │   │   ├── ch02-organization.md   # 第2章 行政組織
│   │   │   ├── ch03-legislation.md    # 第3章 行政立法
│   │   │   ├── ch04-admin-acts.md     # 第4章 行政行為
│   │   │   ├── ch05-discretion.md     # 第5章 行政裁量
│   │   │   ├── ch06-non-coercive.md   # 第6章 非権力的行為形式
│   │   │   └── ch07-enforcement.md    # 第7章 実効性確保
│   │   ├── litigation/                # 行政事件訴訟法（條文對照）
│   │   │   ├── ch01-general.md        # 第1章 総則
│   │   │   ├── ch02-appeal-litigation.md # 第2章 抗告訴訟
│   │   │   ├── ch03-party-litigation.md  # 第3章 当事者訴訟
│   │   │   ├── ch04-public-institutional.md # 第4章 民衆訴訟・機関訴訟
│   │   │   └── ch05-supplementary.md  # 第5章 補則
│   │   ├── procedure/                 # 行政手続法（條文對照）
│   │   │   ├── ch01-general.md        # 第1章 総則
│   │   │   ├── ch02-application.md    # 第2章 申請に対する処分
│   │   │   ├── ch03-adverse.md        # 第3章 不利益処分
│   │   │   ├── ch04-guidance.md       # 第4章 行政指導・処分等の求め
│   │   │   └── ch05-public-comments.md # 第5章 届出・意見公募手続・補則
│   │   └── appeal/                    # 行政不服審査法（條文對照）
│   │       ├── ch01-general.md        # 第1章 総則
│   │       ├── ch02-review-request.md # 第2章 審査請求
│   │       ├── ch03-reinvestigation.md # 第3章 再調査の請求
│   │       ├── ch04-re-appeal.md      # 第4章 再審査請求
│   │       ├── ch05-council.md        # 第5章 行政不服審査会等
│   │       └── ch06-supplementary.md  # 第6章 補則
│   ├── basic-knowledge/               # 基礎知識（教材）
│   │   ├── ch01-political-economy.md  # 一般知識（政治・経済・社会）
│   │   ├── ch02-related-statutes.md   # 行政書士法等関連諸法令
│   │   ├── ch03-info-privacy.md       # 情報通信・個人情報保護
│   │   └── ch04-reading-comprehension.md # 文章理解
│   └── practice/
│       ├── book1-general/             # 民法 第一編 総則（練習問題）
│       │   ├── ch01-general-rules.md  # 択一式 2題
│       │   ├── ch02-persons.md        # 択一式 6題 + 記述式 1題
│       │   ├── ch03-juridical-persons.md # 択一式 3題
│       │   ├── ch04-things.md         # 択一式 2題
│       │   ├── ch05-juridical-acts.md # 択一式 10題 + 記述式 2題
│       │   ├── ch06-periods.md        # 択一式 1題
│       │   └── ch07-prescription.md   # 択一式 8題 + 記述式 2題
│       ├── book2-property/            # 民法 第二編 物権（練習問題）
│       │   ├── ch01-general-rules.md  # 択一式 3題
│       │   ├── ch02-possession.md     # 択一式 2題
│       │   ├── ch03-ownership.md      # 択一式 2題
│       │   ├── ch04-land-rights.md    # 択一式 2題
│       │   ├── ch05-security-interests.md # 択一式 2題
│       │   ├── ch06-pledge.md         # 択一式 2題
│       │   └── ch07-mortgage.md       # 択一式 3題
│       ├── admin-litigation/          # 行政事件訴訟法（練習問題）
│       ├── admin-procedure/           # 行政手続法（練習問題）
│       ├── admin-appeal/              # 行政不服審査法（練習問題）
│       └── basic-knowledge/           # 基礎知識（練習問題）
├── references/
│   ├── civil-code.xml                 # e-Gov 官方民法 XML
│   ├── 行政事件訴訟法.xml
│   ├── 行政手続法.xml
│   ├── 行政不服審査法.xml
│   ├── 国家賠償法.xml
│   └── 地方自治法.xml
└── scripts/
    └── extract_articles.py            # XML 條文抽出腳本
```
