                    Amazon Route53
                          │
                          ▼
                  Application Load Balancer
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
      ECS/Fargate                    ECS/Fargate
      Frontend                       Backend
          │                               │
          │                               ▼
          │                       Amazon EFS
          │                               │
          │                               ▼
          │                        Chroma Database
          │
          └──────────────┬────────────────┘
                         ▼
                   Ollama Service
                  (GPU EC2 / ECS GPU)
                         │
                         ▼
                  Enterprise Documents