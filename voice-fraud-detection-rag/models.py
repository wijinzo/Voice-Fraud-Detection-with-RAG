import os
import pandas as pd
from opencc import OpenCC
from groq import Groq

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI

import config

# Initialize simple tools
cc = OpenCC('s2t')
groq_client = Groq(api_key=config.GROQ_API_KEY)

# Initialize Models
print("⏳ 正在載入 Embedding 模型 ...")
embed_model = HuggingFaceEmbedding(
    model_name=config.EMBEDDING_MODEL_NAME, 
    token=config.HF_TOKEN
)

print("⏳ 正在載入 Gemini LLM...")
llm = GoogleGenAI(model=config.LLM_MODEL_NAME, api_key=config.GOOGLE_API_KEY)

# Load Data and RAG Index
print("⏳ 正在載入 RAG Index...")
try:
    if os.path.exists(config.STORAGE_DIR):
        storage_context = StorageContext.from_defaults(persist_dir=config.STORAGE_DIR)
        index = load_index_from_storage(storage_context, embed_model=embed_model)
        retriever = index.as_retriever(
            similarity_top_k=config.TOP_K_LIMIT,
            similarity_cutoff=config.SIMILARITY_THRESHOLD
        )
        print("✅ Index 載入成功")
    else:
        print(f"❌ 錯誤：找不到索引資料夾 {config.STORAGE_DIR}")
        index = None
        retriever = None
except Exception as e:
    print(f"❌ Index 載入失敗 (可能是 embedding 模型維度不合): {e}")
    index = None
    retriever = None


'''
# test用
print("⏳ 正在載入原始 DataFrame...")
try:
    df_cases = pd.read_csv(config.DATA_FILE) 
    print(f"✅ 資料載入成功，共 {len(df_cases)} 筆")
except Exception as e:
    print(f"⚠️ 無法讀取原始資料檔: {e}")
'''
# df_cases 不需要，但要宣告讓 logic.py 不報錯
df_cases = pd.DataFrame()
