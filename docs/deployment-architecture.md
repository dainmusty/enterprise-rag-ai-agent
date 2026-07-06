                   GitHub Repository
                           │
            GitHub Actions CI/CD Pipeline
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
 Docker Build                          Unit Tests
        │
        ▼
 Docker Images
        │
        ▼
 Docker Compose
        │
 ┌──────┴──────────┬──────────────┐
 │                 │              │
 ▼                 ▼              ▼
FastAPI       Streamlit      Ollama
Container     Container      Container
        │
        ▼
 Chroma Persistent Volume
        │
        ▼
       Data Volume