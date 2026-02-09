# 行政書士試験 民法學習資料

日本行政書士試験準備用的民法條文對照網站。提供日文原文、繁體中文翻譯、白話講解三層結構，方便中文母語者理解日本民法。

## 目的

- 為準備行政書士試験的中文母語考生提供雙語法條參考資料
- 每條條文包含：**日文原文**（現行法）→ **繁體中文翻譯** → **白話講解**（考試重點解說）
- 標注 2020 年民法改正變更點【改正】及考試頻出條文【重要】

## 目前收錄範圍

- **民法第一編 総則**（第 1 条〜第 174 条の 2）— 全 7 章完成

## 技術

- [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — 靜態網站產生器
- CJK 全文搜尋（日文 + 中文）— 透過 [jieba](https://github.com/fxsjy/jieba) 中文分詞
- 深色 / 淺色模式切換
- 字體：Noto Sans JP

## 資料來源

- [e-Gov 法令検索 — 民法](https://laws.e-gov.go.jp/law/129AC0000000089) — 原始出處
  - 本地副本：[`references/civil-code.xml`](references/civil-code.xml)（令和 8 年 4 月 1 日施行版）
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
│   │   └── book1-general/             # 第一編 総則（條文對照）
│   │       ├── ch01-general-rules.md  # 第1章 通則
│   │       ├── ch02-persons.md        # 第2章 人
│   │       ├── ch03-juridical-persons.md
│   │       ├── ch04-things.md         # 第4章 物
│   │       ├── ch05-juridical-acts.md # 第5章 法律行為
│   │       ├── ch06-periods.md        # 第6章 期間の計算
│   │       └── ch07-prescription.md   # 第7章 時効
│   └── practice/
│       └── book1-general/             # 第一編 総則（練習問題）
│           ├── ch01-general-rules.md  # 択一式 2題
│           ├── ch02-persons.md        # 択一式 6題 + 記述式 1題
│           ├── ch03-juridical-persons.md # 択一式 3題
│           ├── ch04-things.md         # 択一式 2題
│           ├── ch05-juridical-acts.md # 択一式 10題 + 記述式 2題
│           ├── ch06-periods.md        # 択一式 1題
│           └── ch07-prescription.md   # 択一式 8題 + 記述式 2題
└── references/
    └── civil-code.xml                 # e-Gov 官方民法 XML（校正用）
```
