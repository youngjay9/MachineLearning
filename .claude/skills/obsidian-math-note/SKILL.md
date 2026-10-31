---
name: obsidian-math-note
description: 把對話中練習的數學題整理成 Obsidian 筆記，寫入 vault：公式用 LaTeX、程式範例用 Python（先實際執行再貼輸出），並收錄對話中的觀念說明與比較表。當使用者要求「把這題寫進 Obsidian／vault」「整理成數學筆記」時使用。
argument-hint: <vault 內的筆記路徑，例如 01-Topics/Machine-Learning/洪ML/ch03-一次函數.md>
---

# 把數學練習寫成 Obsidian 筆記

## 參數

`$ARGUMENTS` 是筆記的寫入路徑：

- 相對路徑：視為相對於 vault 根目錄 `/Users/jay/Documents/Obsidian-My-Learning`。
- 絕對路徑：必須位於上述 vault 底下，否則停下來問使用者。
- 沒有 `.md` 副檔名就補上。上層目錄不存在就建立。
- 沒給參數：根據題目所屬的書與章節，提議一個 `01-Topics/Machine-Learning/<書名簡稱>/chNN-<主題>.md` 路徑，先問使用者再寫。
- **檔案已存在**：先讀它，把新內容合併進去（新增段落、更新 `updated`），不要整份覆蓋。

## 內容來源

只整理**這段對話裡實際出現過**的東西：題目、程式、執行結果、觀念說明、比較表。不要另外補一堆對話沒提過的延伸主題；真的有必要補充的，放在「延伸」段落並保持簡短。

## 寫作規則

1. **數學一律用 LaTeX**：行內用 `$...$`，獨立公式用 `$$ ... $$`（前後各自一行）。推導過程寫成多行 `$$`，不要寫成純文字的 `3*x - 18`。
2. **程式用 ```python 區塊**。貼進筆記前，在專案 `ml-learning/` 目錄下用 `uv run python` 實際執行（畫圖的程式加 `MPLBACKEND=Agg`），把真實輸出貼在 ```text 區塊。輸出與預期不符時，修正說明，不要編造輸出。
3. 如果練習程式存在 repo 裡，在筆記中註明路徑（例如 `ml-learning/hung_ml/ch03/ex_linear_function.py`）。
4. 對話中的比較表照原樣保留為 Markdown 表格，可以修正錯誤或補上執行時發現的差異（例如 dtype）。
5. 用中文寫，語氣與 vault 其他筆記一致：先一句話摘要，再分段，避免空泛的套話。

## 筆記格式

依照 vault 既有慣例（參考 `01-Topics/python/*.md`）：

```markdown
---
title: <標題>
type: note
status: active
created: <今天 YYYY-MM-DD>
updated: <今天 YYYY-MM-DD>
source: claude
related:
  - "[[讀書計劃]]"
tags:
  - math
  - <主題，例如 linear-function、numpy>
aliases:
  - <常用搜尋詞>
---

# <標題>

> 一句話摘要：這題在練什麼。

> 本篇範例皆以 Python <版本> 實際執行，輸出與文中相同。

## 題目
## 數學觀念（LaTeX）
## Python 實作
## 觀念說明（對話中的解釋，各自一個小節）
## 易混淆／比較
## 🔗 相關
```

沒有內容的段落直接省略，不要留空標題。

## 完成後

回報寫入的完整路徑、各段落一行摘要，以及執行程式時用的 Python 版本。不要自動 git commit vault。
