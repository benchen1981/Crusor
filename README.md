# AIIS-WH2 — 汽車價格預測

## 👨‍💻 作者
**陳宥興 Ben Chen**
**學號：5114050015**
- GitHub: [@benchen1981](https://github.com/benchen1981)
- Email: benchen1981@gmail.com
- Supervising professor: HUAN CHEN

**資料集：** Vehicle Dataset from CarDekho (Kaggle)
**資料來源：** https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

**專案目標/簡介：** Vehicle Dataset from CarDekho (Kaggle)
  建構一套「二手車價預測自動化系統」，涵蓋資料前處理、特徵工程、線性回歸建模、多模型比較、模型評估（含預測/信賴區間），使用 CRISP-DM 和規範驅動開發（Open Spec）的端對端專案，產生自動化Web部署（Streamlit）、一鍵打包及GitHub/Replit自動發佈。

- **GPT 輔助內容**: 本專案的核心架構、程式碼實作、以及分析流程均由 GPT 輔助完成
- **NotebookLM 摘要**: 研究摘要基於 NotebookLM 對網路上線性回歸分析相關解法的研究
- **Kaggle Community**: 提供車輛資料集
- **Scikit-learn Team**: 提供優秀的機器學習庫
- **CRISP-DM Methodology**: 提供系統性的資料探勘流程

## 技術重點
- pandas/sklearn資料分析建模
- matplotlib/seaborn數據視覺化
- Streamlit互動式Web應用
- PowerPoint報告/專案流程文件自動產出
- SDD Spec Driven、CRISP-DM數據科學全流程

## 如何運行
1. 下載Kaggle資料集並放置 `data/CAR DETAILS FROM CAR DEKHO.csv`
2. 安裝依賴：`pip install -r requirements.txt`
3. 啟動Web：`bash auto_deploy.sh` 或 `streamlit run Streamlit_app.py`
4. 查看 img/prediction_results.png 取得預測結果圖表

## Replit 執行
點擊 README 上方「Run on Replit」按鈕一鍵啟動體驗。

## 1.資料集取得方式
  1.登入Kaggle並打開連結
  2.點擊「Download」取得CSV檔案
  3.將檔案放置專案 data/ 資料夾

## 目錄內容
AIIS-WH2/
│
├── README.md                  # 專案說明書（含Replit按鈕/圖示）
├── SPEC.md                    # SDD專案規格
├── CRISP_DM_NOTEBOOK.ipynb    # 完整流程Jupyter Notebook
├── Streamlit_app.py           # Streamlit一鍵啟動版
├── auto_deploy.sh             # 自動部署命令、啟動腳本
├── requirements.txt           # 依賴Python套件清單
├── data/
│   └── CAR DETAILS FROM CAR DEKHO.csv
├── img/
│   └── 預測結果圖表.png
├── reports/
│   ├── summary_report.pptx    # 總結報告與GPT、NotebookLM標註
│   └── session_dialog.pdf     # 對話過程匯出PDF
└── spec/
    └── OpenSpec.yaml          # Open Spec SDD

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
