import gradio as gr
import asyncio
import config
import logic
import models

async def analyze_async(audio, progress=gr.Progress()):
    if audio is None: 
        yield "未錄音", "", "", "", ""
        return

    progress(0.1, desc="語音辨識中...")
    # Use the logic module's transcription function
    res = logic.transcribe_audio(audio)
    
    # Use the OpenCC instance from models
    text = models.cc.convert(res["text"])
    
    yield text, "分析中...", "分析中...", "...", "..."

    if len(text) >= config.CHAR_THRESHOLD:
        df = await logic.process_single_case_async(text, progress)
        if not df.empty:
            row = df.iloc[0]
            yield row["Dialogue"], row["predicted_type"], row["risk_level"], row["similar_cases"], row["reason"]
        else:
            yield text, "失敗", "失敗", "失敗", "失敗"
    else:
        yield text, "字數不足", "N/A", "N/A", "N/A"

with gr.Blocks() as demo:
    gr.Markdown("# 🎙️ 本地端防詐騙分析系統")
    mic = gr.Audio(sources=["microphone"], type="filepath", label="錄音")
    with gr.Row():
        txt = gr.Textbox(label="辨識文字", lines=5)
        sim = gr.Textbox(label="相似案例", lines=8)
    with gr.Row():
        p_type = gr.Label(label="類型")
        risk = gr.Label(label="風險")
        reason = gr.Label(label="理由")
    
    mic.change(analyze_async, mic, [txt, p_type, risk, sim, reason])

if __name__ == "__main__":
    demo.launch()
