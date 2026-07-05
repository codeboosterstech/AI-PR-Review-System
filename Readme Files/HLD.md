                           AI PR Review Platform
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                            │
│              Next.js + TypeScript + Tailwind               │
└─────────────────────────────────────────────────────────────┘
                           │
                    REST API (HTTPS)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                          │
│                                                             │
│  Health API                                                 │
│  GitHub API                                                 │
│  Review API                                                 │
│  Authentication                                              │
└─────────────────────────────────────────────────────────────┘
          │               │                 │
          ▼               ▼                 ▼
    GitHub Service   AI Service     Security Service
          │               │                 │
          ▼               ▼                 ▼
      GitHub API      Groq/OpenAI       Semgrep
                           │
                           ▼
                    Review Service
                           │
                           ▼
                  Supabase PostgreSQL