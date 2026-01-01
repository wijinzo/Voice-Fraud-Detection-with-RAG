# 🎙️ 本地端防詐騙語音分析系統

使用 RAG（檢索增強生成）與大型語言模型，即時分析臨櫃提款，判斷是否為詐騙，已讓行員即時阻詐。

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange.svg)

## ✨ 功能特色

- 🎤 **即時語音辨識**：使用 Groq Whisper 進行高品質中文語音轉文字
- 🔍 **RAG 相似案例檢索**：從詐騙案例資料庫中檢索相似案例
- 🤖 **LLM 智慧分析**：使用 Google Gemini 進行詐騙類型判斷
- ⚡ **風險等級評估**：自動評估通話的詐騙風險等級
- 🖥️ **Web 介面**：簡潔易用的 Gradio 網頁介面

## 🏗️ 系統架構

```
語音輸入 → Whisper 語音辨識 → 繁體中文轉換 → RAG 相似案例檢索 → Gemini LLM 分析 → 風險評估
```

## 📋 詐騙類型分類

系統可識別以下詐騙類型：
- 非詐騙
- 假冒公務員詐騙
- 投資理財詐騙
- 匯款詐騙
- 交友詐騙
- 假冒親友詐騙
- 其他詐騙

## 🚀 快速開始

### 前置需求

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) 套件管理工具

### 安裝步驟

1. **Clone 專案**
   ```bash
   git clone https://github.com/yourusername/fraud-detection.git
   cd fraud-detection
   ```
   
   下載整個 RAG index 資料夾(也可以自己建立)，並儲存在storage_index資料夾:
   ```bash
   https://drive.google.com/drive/folders/1mFhQCAoh9RCt5iH0W5zjAYbfIKMtHO1h?usp=sharing
   ```

2. **建立環境變數**
   
   複製 `.env.example` 為 `.env` 並填入您的 API Keys：
   ```bash
   cp .env.example .env
   ```
   
   編輯 `.env` 檔案：
   ```env
   GOOGLE_API_KEY=your_google_api_key
   GROQ_API_KEY=your_groq_api_key
   HF_TOKEN=your_huggingface_token
   ```

3. **安裝依賴**
   ```bash
   uv sync
   ```

4. **執行應用程式**
   ```bash
   uv run python app.py
   ```

5. **開啟瀏覽器**
   
   前往 `http://127.0.0.1:7860` 使用系統

## 🔑 API Keys 取得方式

| API Key | 取得網址 |
|---------|----------|
| Google API Key | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| Groq API Key | [Groq Console](https://console.groq.com/keys) |
| HuggingFace Token | [HuggingFace Settings](https://huggingface.co/settings/tokens) |

## 📁 專案結構

```
fraud-detection/
├── app.py              # Gradio 主應用程式
├── config.py           # 設定檔（API Keys、參數）
├── models.py           # 模型初始化（Embedding、LLM、RAG Index）
├── logic.py            # 業務邏輯（語音辨識、案例分析）
├── rag_data.txt        # RAG 知識庫資料
├── storage_index/      # 向量索引儲存目錄 (須將步驟1下載的資料夾放在這裡)
├── pyproject.toml      # 專案依賴設定
└── .env                # 環境變數（API Keys）
```

## ⚙️ 設定參數

可在 `config.py` 中調整以下參數：

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `CHAR_THRESHOLD` | 最小分析字數 | 100 |
| `TOP_K_LIMIT` | RAG 檢索數量 | 5 |
| `SIMILARITY_THRESHOLD` | 相似度閾值 | 0.7 |
| `HIGH_RISK_THRESHOLD` | 高風險閾值 | 0.8 |
| `EMBEDDING_MODEL_NAME` | Embedding 模型 | `BAAI/bge-large-zh-v1.5` |
| `LLM_MODEL_NAME` | LLM 模型 | `gemini-2.5-flash` |

## 🛠️ 技術棧

- **語音辨識**: Groq Whisper Large V3
- **Embedding**: BAAI/bge-large-zh-v1.5
- **LLM**: Google Gemini 2.5 Flash
- **RAG 框架**: LlamaIndex
- **Web UI**: Gradio
- **繁簡轉換**: OpenCC

## 📝 使用說明

1. 點擊錄音按鈕開始錄製
2. 說出通話內容
3. 點擊停止結束錄音
4. 系統會自動分析並顯示：
   - 辨識出的文字
   - 詐騙類型判斷
   - 風險等級
   - 相似歷史案例
   - 判斷理由

## ⚠️ 注意事項

- 首次執行需下載 Embedding 模型（約 1.3 GB），請耐心等待
- 請確保 `storage_index/` 資料夾存在且包含預建的索引
- 建議使用穩定的網路連線以確保 API 呼叫正常

## 📄 License

MIT License

---

Made with ❤️ for fraud prevention
