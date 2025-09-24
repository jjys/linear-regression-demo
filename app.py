import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("互動式線性回歸與離群值分析")

# 使用者可調整參數
n = st.slider("資料點數量 n", min_value=100, max_value=1000, value=200, step=50)
a = st.slider("斜率 a", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
b = st.number_input("截距 b", value=0.0)
var = st.slider("噪聲方差 var", min_value=0.0, max_value=1000.0, value=50.0, step=1.0)

# -----------------------------
# 資料生成
# -----------------------------
np.random.seed(42)
x = np.random.uniform(0, 100, n)
noise = np.random.normal(0, np.sqrt(var), n)
y = a * x + b + noise
data = pd.DataFrame({"x": x, "y": y})

# -----------------------------
# 線性回歸
# -----------------------------
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

# 計算離群值距離
residuals = np.abs(y - y_pred)
top5_idx = residuals.argsort()[-5:][::-1]

# -----------------------------
# Plotly 繪圖
# -----------------------------
fig = go.Figure()

# 所有資料點
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='資料點',
    marker=dict(color='blue', size=8),
    text=[f"x: {xi:.2f}<br>y: {yi:.2f}" for xi, yi in zip(x, y)],
    hoverinfo='text'
))

# 迴歸線
fig.add_trace(go.Scatter(
    x=x, y=y_pred,
    mode='lines',
    name='迴歸線',
    line=dict(color='red', width=2)
))

# 前5離群值
fig.add_trace(go.Scatter(
    x=x[top5_idx],
    y=y[top5_idx],
    mode='markers+text',
    name='前5離群值',
    marker=dict(color='orange', size=12, line=dict(color='black', width=1)),
    text=[f"({x[i]:.1f},{y[i]:.1f})" for i in top5_idx],
    textposition='top center',
    hoverinfo='text'
))

fig.update_layout(
    title="互動式線性回歸與離群值",
    xaxis_title="x",
    yaxis_title="y",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    width=800,
    height=500
)

st.plotly_chart(fig)

# -----------------------------
# 顯示回歸結果
# -----------------------------
st.subheader("迴歸結果")
st.write(f"斜率 (a_estimated): {model.coef_[0]:.3f}")
st.write(f"截距 (b_estimated): {model.intercept_:.3f}")

# 顯示前5離群值
st.subheader("前5離群值")
st.dataframe(data.iloc[top5_idx].assign(Residual=residuals[top5_idx]))
