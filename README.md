# AIIS-WH2 — 汽車價格預測

## 👨‍💻 作者
**陳宥興 Ben Chen**
**學號：5114050015**
- GitHub: [@benchen1981](https://github.com/benchen1981)
- Email: benchen1981@gmail.com
- Supervising professor: HUAN CHEN

**資料集：** Vehicle Dataset from CarDekho (Kaggle)
**資料來源：** https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

簡介：使用 CRISP-DM 和規範驅動開發（Open Spec）的端對端專案。包含 Notebook、Python Script、Streamlit Replit-ready）、Dockerfile 和自動化部署Script。

- **GPT 輔助內容**: 本專案的核心架構、程式碼實作、以及分析流程均由 GPT 輔助完成
- **NotebookLM 摘要**: 研究摘要基於 NotebookLM 對網路上線性回歸分析相關解法的研究
- **Kaggle Community**: 提供車輛資料集
- **Scikit-learn Team**: 提供優秀的機器學習庫
- **CRISP-DM Methodology**: 提供系統性的資料探勘流程

## 快速啟動 (本機端)
1. 從 Kaggle 下載資料集，並將其放置在 `data/vehicle_data.csv` 目錄下
2. 建立虛擬環境並安裝相依性
3. 執行 notebook 或 pipeline

## Replit / Streamlit Cloud
此程式庫包含 `streamlit_app/streamlit_app.py` 檔案，並在 Replit 上部署

## 目錄內容
- `/notebooks/analysis.ipynb` — 包含 CRISP-DM 步驟和完整建模流程（線性回歸、多元線性回歸、自回歸）、特徵選擇、模型評估和圖表（含置信區間/預測區間）的 Jupyter notebook.
- `/src/pipeline.py` — 該 notebook 的可複現程式版本。.
- `/streamlit_app/streamlit_app.py` — 用於快速預測的 Streamlit 使用者介面.
- `/specs` — Open Spec SDD files (INIT → REQUIREMENTS → DESIGN → TASKS → IMPLEMENTATION).
- `/deploy` — Dockerfile 和部署程式.
- `/reports` — PDF and PowerPoint 範本.

## ChatGPT Prompt 內容
Task：制作一個Python軟體開發專案, 包含生成自動部署命令腳本及一鍵啟動版
1. 資料來源
資料集名稱： Vehicle Dataset from Cardekho
來源： Kaggle
連結： https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
說明： 此資料集包含 13 個特徵（例如 year, km_driven, fuel, mileage, engine,
  請明確標示資料集來源與連結。
2. 分析任務
  使用線性回歸 (Linear Regression) 模型進行預測、多元線性回歸 (Multiple Linear Regression)、及 Auto Regression。
  必須執行 特徵選擇 (Feature Selection) 與 模型評估 (Model Evaluation)。
  結果部分需包含請提供預測圖(加上信賴區間或預測區間)
3. 遵循 CRISP-DM 流程完成從資料理解、建模到評估的全過程
   Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment
4. 使用Open Spec套件完成Spec Driven Development，SDD 流程：INIT → REQUIREMENTS → DESIGN → TASKS → IMPLEMENTATION
將完整專案打包，用 Python 標準庫 zipfile 批量打包分析程式、圖表、Spec文件、README
5.產生一整套 repo scaffold, 產生完整的 Jupyter/py 腳本並向我說明如何下載資料與執行（含圖表輸出）, 
6.直接生成可在 Replit 上自動化部署的 Streamlit script及完整步驟說明
7.將整個專案打包成 zip 並提供下載。
8.幫我建立 GitHub repo 並推上去（GitHub 使用者名稱:benchen1981,個 repo 名稱:AIIS-WH2
9.在 notebook 中執行完整 pipeline


## MIT License
Copyright (c) 2025 Ben Chen
Permission is hereby granted, free of charge, to any person obtaining a copy...
10.自動產生一份「GitHub README 預覽範例（含 Replit 按鈕與圖示）」
11.生成動部署命令腳本，一鍵啟動版
12.所有與你的對話，以 pdfCrowd 或其他方式須匯出為 PDF
13.用 NotebookLM 對網路上同主題的解法進行研究，並撰寫一份 100 字以上的摘要，放入報告中。
14.在總結報告中(power point)明確標示「GPT 輔助內容」與「NotebookLM 摘要」
