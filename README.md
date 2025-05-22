# MedBot

![MedBot Logo](assets/MedBot%20logo.png)

MedBot is an intelligent, context-aware medical question answering system that leverages advanced language models and semantic search to provide accurate, professional, and contextually relevant answers to medical queries. Designed for both healthcare professionals and the general public, MedicalQA delivers reliable information sourced from a curated medical knowledge base, MedQuad.

---

## Features

- **Natural Language Medical Q&A:** Ask any medical question and receive detailed, professional answers.
- **Contextual Retrieval:** Uses semantic search to find the most relevant documents from a medical knowledge base.
- **Source Transparency:** Each answer is accompanied by clickable sources, document IDs, and similarity scores for transparency and trust.
- **Image Context Support:** Optionally enhances answers using image context (when available).
- **Modern UI:** Built with Streamlit for an interactive and user-friendly web interface.
- **API Ready:** FastAPI backend for easy integration with other applications or services.

---

## Technologies Used

- Python
- OpenAI GPT (or compatible LLM)
- LangChain
- FAISS (vector search)
- Streamlit (UI)
- FastAPI (API)
- Pandas, PyTorch, HuggingFace Embeddings

---

## Getting Started

### Prerequisites

- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/)
- (Optional) CUDA-enabled GPU for faster embedding

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/MedicalQA.git
    cd MedicalQA
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your OpenAI API key:**
    - Set your API key in the environment or directly in the code as shown in `app.py`.

4. **Prepare the knowledge base:**
    - Place your medical data CSV (e.g., `medquad_data.csv`) in the project directory.

5. **Run the application:**
    - **Streamlit UI:**
      ```bash
      streamlit run streamui.py
      ```
    - **FastAPI backend:**
      ```bash
      uvicorn app:app --reload
      ```

---

## Usage

- Open the Streamlit app in your browser.
- Ask any medical question in the chat interface.
- Optionally, upload an image for context-aware answers.
- Review the answer and its sources for transparency.

---

## Example

![Demo Screenshot](assets/demo_screenshot.png)

---

## Project Structure

```
MedicalQA/
│
├── app.py                # FastAPI backend and core logic
├── streamui.py           # Streamlit user interface
├── medquad_data.csv      # Medical knowledge base (example)
├── assets/
│   └── MedBot logo.png   # Project logo
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Disclaimer

**This project is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider with any questions regarding a medical condition.**

---

## License

[MIT License](LICENSE)

---

## Acknowledgements

- [OpenAI](https://openai.com/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
