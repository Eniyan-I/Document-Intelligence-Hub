<h1>Document Intelligence Hub</h1>
<p>An advanced, local-first Retrieval-Augmented Generation (RAG) application built with Python, LangChain, and Streamlit. This hub allows users to upload PDF documents and interact with them contextually through a local Llama 3.2 model, ensuring complete data privacy and zero external API dependencies.</p>
<h2>Features</h2>
<li>Local AI Inference: Powered by Llama 3.2 running locally via Ollama for fast, secure, and private document querying.</li>
<li>Semantic Search & Indexing: Utilizes FAISS as a high-performance vector store paired with nomic-embed-text embeddings for precise context retrieval.</li>
<li>Advanced Document Processing: Implements recursive text chunking and robust PDF parsing utilities to handle complex document structures.</li>
<li>Declarative RAG Pipeline: Built using LangChain Expression Language (LCEL) to cleanly orchestrate context retrieval, prompt formatting, and output parsing.</li>
<li>Optimized Streamlit UI: Features a responsive interface incorporating resource caching (st.cache_resource) and secure temporary file handling for peak performance and minimal memory overhead.</li>
<h2>Technology Stack</h2>
<li>Orchestration: LangChain (LCEL)</li>
<li>LLM & Embeddings: Ollama (Llama 3.2, nomic-embed-text)</li>
<li>Vector Database: FAISS</li>
<li>Frontend & Utilities: Streamlit, Python</li>
<h2>Project Structure</h2>
Ensure you have Python 3.10+ installed along with Ollama running locally.
<p></p>

```bash
document-intelligence-hub/
│
├── app.py              # Main Streamlit application interface
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
