# 餘弦相似度計算器

這是一個輕量級的 Python 專案，用於計算兩個向量之間的**餘弦相似度**。餘弦相似度是一種衡量兩個非零向量之間夾角餘弦值的度量方法，常用於判斷文本相似度、推薦系統中的物品相似度等場景。

## 特點

* **簡單易用**：提供一個簡單的函數 `calculate_cosine_similarity` 即可完成計算。
* **NumPy 優化**：內部使用 NumPy 進行向量操作，提高計算效率。
* **錯誤處理**：自動檢查輸入向量的維度是否一致。

## 安裝

本專案需要 `numpy` 函式庫。如果你尚未安裝，可以使用 pip 進行安裝：

```bash
pip install numpy
```

使用方法
將 cosine_similarity.py 文件下載到你的專案中，然後像這樣導入並使用它：

```bash
from cosine_similarity import calculate_cosine_similarity

# 定義你的向量
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# 計算餘弦相似度
similarity = calculate_cosine_similarity(vector1, vector2)

print(f"兩個向量的餘弦相似度為: {similarity}")

# 你也可以使用 NumPy 陣列
import numpy as np
np_vector1 = np.array([1, 0, 1])
np_vector2 = np.array([0, 1, 1])

np_similarity = calculate_cosine_similarity(np_vector1, np_vector2)
print(f"兩個 NumPy 向量的餘弦相似度為: {np_similarity}")

```

範例
運行 cosine_similarity.py 文件將會看到一些預設的範例輸出：
```
python cosine_similarity.py
```

貢獻
歡迎任何形式的貢獻，包括但不限於：

* 提交 Bug 報告

* 提出新功能建議

* 改進程式碼或文件

授權
本專案採用 Apache 2.0 授權。詳情請參閱 LICENSE 文件。
