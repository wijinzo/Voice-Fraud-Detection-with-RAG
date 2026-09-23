# AI Fraud Detection Research

This repository brings together two related AI research projects focused on fraud prevention and identity verification.

## Research Modules

### Face Recognition

Development history and demonstration notebook for the face-recognition research module.

- Location: `face-recognition/`
- Notebook: `face-recognition/notebooks/face-recognition-development-and-demo.ipynb`

### Voice Fraud Detection with RAG

A local voice-fraud analysis system that combines speech recognition, retrieval-augmented generation, and a large language model to assess fraud risk.

- Location: `voice-fraud-detection-rag/`
- Module documentation: `voice-fraud-detection-rag/README.md`

## Repository Structure

```text
AI-Fraud-Detection-Research/
|-- face-recognition/
|   |-- README.md
|   `-- notebooks/
|       `-- face-recognition-development-and-demo.ipynb
|-- voice-fraud-detection-rag/
|   |-- README.md
|   |-- app.py
|   |-- config.py
|   |-- logic.py
|   |-- models.py
|   |-- pyproject.toml
|   |-- rag_data.txt
|   `-- uv.lock
|-- .gitignore
`-- README.md
```

## Running the Voice Fraud Detection Module

```powershell
cd voice-fraud-detection-rag
Copy-Item .env.example .env
uv sync
uv run python app.py
```

Add the required API keys to `.env` before starting the application. The `.env` file is excluded from Git.

## Data and Privacy

Do not commit API keys, private face images, confidential voice recordings, or personally identifiable information. Large generated indexes and local model artifacts should remain outside Git unless a dedicated artifact-storage solution is used.
