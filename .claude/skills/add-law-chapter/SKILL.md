---
name: add-law-chapter
description: 為行政書士試験學習網站新增一個法律章節的完整教材。輸入目標法律/章節後，自動產出：①雙語法條教材（日文+繁體中文+白話講解）、②收集過去問並製作練習問題、③更新 mkdocs.yml 與 README、④build、deploy、commit & push。當需要在 gyoseishoshi-test 專案中新增民法/行政法的新章節時使用。
compatibility: Designed for Claude Code. Requires internet access for WebSearch/WebFetch. mkdocs at /Users/kevinshu/Library/Python/3.9/bin/mkdocs.
allowed-tools: Read Write Edit Glob Grep Bash WebSearch WebFetch
---

## 輸入參數

- **目標法律/章節**: 例如「民法第三編 債権」「民法第四編 親族」
- **文件目錄前綴**: 教材放在 `docs/civil-code/` 或 `docs/admin-law/` 等
- **XML 參照**: `references/civil-code.xml`（如有）

## 執行流程

### Phase 1：準備

1. **確認章節清單**
   - 詢問或確認目標章節列表與條文範圍，例如：
     ```
     第1章 総則（第399条〜第411条）
     第2章 契約（第521条〜第696条）
     ```
   - 確認輸出目錄命名（例：`civil-code/book3-obligations/`）

2. **讀取格式規範**
   - 閱讀 `references/teaching-format.md`（教材格式）
   - 閱讀 `references/practice-format.md`（練習問題格式）

3. **確認來源素材**
   - 若有 XML：`Grep` 找出章節條文
   - 若無 XML：記下需要從 e-Gov 或記憶中補全的條文

---

### Phase 2：製作法條教材

對每個章節執行：

4. **建立教材檔案**（`docs/civil-code/[目錄]/chXX-[slug].md`）
   - 格式完全依照 `references/teaching-format.md`
   - 每條條文：日文原文 → 繁體中文翻譯 → 白話講解
   - 白話講解**必須完全用繁體中文**（法律術語可保留日文，說明文字用中文）
   - 頻出條文標注 `【重要】`，有修正的標注 `【改正】`

---

### Phase 3：收集過去問並製作練習問題

對每個章節執行：

5. **搜尋過去問**
   - WebSearch: `行政書士 過去問 [章節主題關鍵字] 択一`
   - 目標：找到具體的年度、問題番号（例：「令和3年度 問28」）
   - 重點搜尋網站：gyosyo.info、goukakudojyo.com、法律系考試準備網站

6. **驗證題目**
   - WebFetch 實際取得題目原文
   - 確認：選項文字、正解、判例引用（如：最判平12.4.14）
   - **禁止自行編造題目**；若找不到足夠的過去問，可以基於教材出題但需明確標注「[出題例]」

7. **建立練習問題檔案**（`docs/practice/[目錄]/chXX-[slug].md`）
   - 格式完全依照 `references/practice-format.md`
   - 題目與解說**一律用日文**；答案中的「中文要點」用繁體中文

---

### Phase 4：整合

8. **更新 mkdocs.yml**
   - 在 `nav:` 中對應位置插入新的教材章節（`docs/civil-code/...`）
   - 插入新的練習問題章節（`docs/practice/...`）
   - 參考現有結構確認插入位置

9. **更新 README.md**
   - 更新「目前收錄範圍」的教材清單與練習問題清單
   - 更新「専案結構」目錄樹

---

### Phase 5：Build、Deploy、Commit

10. **Build 驗證**
    ```bash
    /Users/kevinshu/Library/Python/3.9/bin/mkdocs build --quiet
    ```
    確認零錯誤後繼續。

11. **部署**
    ```bash
    /Users/kevinshu/Library/Python/3.9/bin/mkdocs gh-deploy --quiet
    ```

12. **Commit & Push**
    ```bash
    git add [所有新增/修改的檔案]
    git commit -m "feat: add [法律名稱] bilingual materials and practice questions"
    git push origin main
    ```

---

## 注意事項

- **錨點規則**：MkDocs 對日文標題只保留數字作為錨點。`## 第388条（法定地上権）` → `#388`，`### 第3条の2` → `#32`。建立條文連結前先確認
- **白話講解語言**：必須完全用繁體中文撰寫，即使是法律概念也要加中文說明
- **題目真實性**：過去問必須有出處（年度+問題番号），不可偽造
- **台灣法比較**：白話講解中可加入「與台灣民法的差異」說明，幫助考生對照理解
