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
1. Download dataset from Kaggle and place as `data/vehicle_data.csv` (instructions below).
2. Create virtualenv and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run the notebook or pipeline:
```bash
jupyter notebook notebooks/analysis.ipynb
# or
python src/pipeline.py --input data/vehicle_data.csv
```

## Replit / Streamlit Cloud
This repo includes `streamlit_app/streamlit_app.py`. To deploy on Replit:
- Create a new Replit project, upload the repo files (or use "import from GitHub"), set `run` command to `streamlit run streamlit_app/streamlit_app.py --server.port=$PORT --server.enableCORS=false`.
- See `deploy/deploy_replit.sh` for automated helper.

[![Run on Replit](https://replit.com/badge/github/benchen1981/AIIS-WH2)](https://replit.com)

## What's inside
- `/notebooks/analysis.ipynb` — Jupyter notebook with CRISP-DM steps and full modeling pipeline (Linear Regression, Multiple Linear Regression, Auto Regression), feature selection, model evaluation, plots (with confidence/prediction intervals).
- `/src/pipeline.py` — Reproducible script version of the notebook.
- `/streamlit_app/streamlit_app.py` — Streamlit UI for quick predictions.
- `/specs` — Open Spec SDD files (INIT → REQUIREMENTS → DESIGN → TASKS → IMPLEMENTATION).
- `/deploy` — Dockerfile and deployment scripts.
- `/reports` — Templates for PDF and PowerPoint (placeholders).

## Notes / Limitations
- This package does **not** include the Kaggle dataset due to licensing and size. Download instructions are below.
- I cannot push directly to your GitHub account or call external services on your behalf. I included `git_push_instructions.sh` to run locally.

## License
MIT
