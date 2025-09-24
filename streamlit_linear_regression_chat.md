# Streamlit 線性回歸互動應用對話紀錄

## 對話摘要

### 使用者需求
- 建立一個 Streamlit 應用，用於線性回歸資料生成與視覺化。
- 功能包含：
  - 資料生成：
    - 產生 n 個資料點 (x, y)，n 可由使用者設定 (100~1000)。
    - y = ax + b + noise，a 係數由使用者設定 (-10~10)。
    - noise 為常態分布 N(0, var)，var 可由使用者設定 (0~1000)。
  - 線性回歸可視化：
    - 繪製資料點。
    - 用紅色繪製線性回歸線。
  - 離群值辨識：
    - 標註距離回歸線最遠的前 5 個點。
  - 使用者介面：
    - 透過滑桿或輸入框調整參數 (n, a, var)。
    - 顯示生成圖與回歸結果。

### 錯誤排查

1. **ModuleNotFoundError: No module named 'plotly'**
   - 錯誤訊息出現在 `import plotly.graph_objects as go`。

2. **原因**
   - Python 環境中沒有安裝 Plotly。

3. **解決方法**
   - 確認使用的 Python 環境一致。
   - 安裝套件：
     ```bash
     pip install plotly
     ```
   - 若在 Streamlit Cloud 上部署，需建立 `requirements.txt`：
     ```text
     streamlit
     plotly
     numpy
     pandas
     ```
   - 重新啟動應用：
     ```bash
     streamlit run app.py
     ```

4. **替代方案**
   - 可改用 Matplotlib 與 Streamlit 繪圖，避免在雲端部署時出現模組缺失問題，同時保持功能完整。

### 下一步
- 使用者詢問是否可以將對話輸出成 Markdown 檔案。

