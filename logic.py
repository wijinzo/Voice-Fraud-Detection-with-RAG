import os
import pandas as pd
import models
import config

CATEGORIES = ["非詐騙", "假冒公務員詐騙", "投資理財詐騙", "匯款詐騙", "交友詐騙", "假冒親友詐騙", "其他詐騙"]
SYSTEM_PROMPT = f"請依照案件描述進行分類，回傳「類型」與「一句理由」。類型須為：{', '.join(CATEGORIES)}"

def transcribe_audio(audio_filepath):
    if not audio_filepath: return {"text": ""}
    try:
        with open(audio_filepath, "rb") as file:
            transcription = models.groq_client.audio.transcriptions.create(
                file=(os.path.basename(audio_filepath), file.read()),
                model=config.WHISPER_MODEL_NAME,
                response_format="json", 
                temperature=0.0
            )
        return {"text": transcription.text}
    except Exception as e:
        print(f"❌ Groq Error: {e}")
        return {"text": ""}

async def process_single_case_async(user_input, progress=None):
    if not models.retriever: return pd.DataFrame()

    if progress: progress(0.3, desc="檢索中...")
    
    # 1. 檢索
    similar_nodes = await models.retriever.aretrieve(user_input)
    filtered_nodes = [n for n in similar_nodes if n.score >= config.SIMILARITY_THRESHOLD]

    # 2. 構建 Context
    retrieved_texts = []
    if not filtered_nodes:
        retrieved_text = "無相似案例"
    else:
        for i, n in enumerate(filtered_nodes, 1):
            content = n.node.get_content()
            snippet = content.strip().replace("\n", " ")[:500]
            retrieved_texts.append(f"--- 相似案例 {i} (Score={n.score:.3f}) ---\n{snippet}\n")
        retrieved_text = "\n".join(retrieved_texts)

    if progress: progress(0.6, desc="LLM 分析中...")

    # 3. LLM 判斷
    prompt = f"案件描述：\n{user_input[:800]}\n\n相似案例：\n{retrieved_text}\n\n{SYSTEM_PROMPT}"
    
    try:
        response = await models.llm.acomplete(prompt)
        answer_text = response.text.strip().replace("\n", "")
    except Exception as e:
        answer_text = f"錯誤: {e}"

    # 4. 解析結果
    matched_type = "其他"
    reason = answer_text
    
    if "理由：" in answer_text:
        try:
            parts = answer_text.split("理由：")
            type_part = parts[0].replace("類型：", "").strip()
            reason = parts[1].strip()
            for cat in CATEGORIES:
                if cat in type_part:
                    matched_type = cat
                    break
        except: pass
    else:
        for cat in CATEGORIES:
            if cat in answer_text:
                matched_type = cat
                break
    
    # 風險判斷
    if matched_type == "非詐騙":
        risk = "低風險" if not filtered_nodes else "潛在風險(資訊不足)"
    else:
        max_s = max((n.score for n in filtered_nodes), default=0)
        risk = "高風險" if max_s >= config.HIGH_RISK_THRESHOLD else "疑似風險"

    return pd.DataFrame([{
        "Dialogue": user_input,
        "predicted_type": matched_type,
        "risk_level": risk,
        "similar_cases": retrieved_text,
        "reason": reason
    }])
