import os
from dotenv import load_dotenv

# 1. 載入 .env 裡的 API Key
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Constants
CHAR_THRESHOLD = 100
TOP_K_LIMIT = 5
SIMILARITY_THRESHOLD = 0.7 
HIGH_RISK_THRESHOLD = 0.8

# Paths
STORAGE_DIR = "./storage_index"
DATA_FILE = "./cases.csv"

# Model Configs
EMBEDDING_MODEL_NAME = "BAAI/bge-large-zh-v1.5"
LLM_MODEL_NAME = "gemini-2.5-flash"
WHISPER_MODEL_NAME = "whisper-large-v3"
