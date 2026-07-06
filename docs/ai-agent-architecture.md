                                ┌──────────────────────────────┐
                                │           User               │
                                └──────────────┬───────────────┘
                                               │
                                               │ HTTPS
                                               ▼
                               ┌──────────────────────────────┐
                               │        Streamlit UI          │
                               │        (Frontend)            │
                               └──────────────┬───────────────┘
                                              │ REST API
                                              ▼
                     ┌────────────────────────────────────────────────┐
                     │            FastAPI Backend                     │
                     │                                                │
                     │  Logging Middleware                            │
                     │  Global Exception Handler                      │
                     │  API Versioning                                │
                     └──────────────┬─────────────────────────────────┘
                                    │
              ┌─────────────────────┼───────────────────────┐
              │                     │                       │
              ▼                     ▼                       ▼
      Chat Controller       Upload Controller        Health Endpoint
              │                     │
              ▼                     ▼
        Chat Service        Ingestion Service
              │                     │
              │             File Loaders
              │       (.txt /.md /.pdf)
              │                     │
              ▼                     ▼
          RAG Service          Chunking Service
              │                     │
              ▼                     ▼
      Retrieval Service      Embedding Service
              │                     │
              └──────────────┬──────┘
                             │
                             ▼
                    Chroma Vector Database
                             ▲
                             │
                   Similarity Search Results
                             │
                             ▼
                    Prompt Builder Service
                             │
                             ▼
                       Ollama (LLM)
                             │
                             ▼
                      Generated Response
                             │
                             ▼
                        FastAPI Response
                             │
                             ▼
                        Streamlit UI