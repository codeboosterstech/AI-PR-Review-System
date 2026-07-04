# AI-PR-Review-System

Step -1
frontend/ → Next.js application
backend/ → FastAPI application
docs/ → Notes, API documentation, architecture diagrams
screenshots/ → Images for the README and portfolio

Step 2 
Move into the backend folder:

cd backend

Create a virtual environment:

python -m venv venv

Activate it:

Linux (Codespaces):

source venv/bin/activate

Upgrade pip:

pip install --upgrade pip

Install the required packages:

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv httpx groq
What each package does
Package	Purpose
FastAPI	Backend framework
Uvicorn	Runs the FastAPI server
SQLAlchemy	Database ORM
psycopg2-binary	PostgreSQL driver (Supabase)
python-dotenv	Loads environment variables
httpx	Makes HTTP requests (e.g., GitHub API)
groq	Official Groq Python SDK

Step - 3 
Backend Folder Structure

Why this structure?
main.py → Starts the API.
config.py → Loads environment variables.
database.py → Connects to Supabase.
models.py → Database tables.
schemas.py → Request/response validation.
github_service.py → GitHub API logic.
semgrep_service.py → Security scanning.
ai_service.py → Groq integration.
review_service.py → Coordinates the review workflow.

Each file has a single responsibility, making the code easier to understand and test.

Step -- 4
components/ → Reusable UI components
services/ → API calls to FastAPI
types/ → Shared TypeScript interfaces

Step --5 
Deep dive into Backend 
Q1. What is FastAPI?

Answer:

FastAPI is a modern Python web framework used to build REST APIs. It is fast, easy to use, supports automatic API documentation, and uses Python type hints for validation.

Q2. What is Uvicorn?

Answer:

Uvicorn is an ASGI server that runs FastAPI applications and handles incoming HTTP requests.

Q3. Why do we write app = FastAPI()?

Answer:

It creates the FastAPI application object. Uvicorn looks for this object to know which application to run.

main.py in backend/app folder is the main file 

STEP--6
API Workflow
Browser
   │
HTTP Request
   │
   ▼
FastAPI
   │
Python Function
   │
   ▼
JSON Response
   │
HTTP Response
   │
   ▼
Browser

ProjectArchitecture

                User
                  │
                  ▼
        Next.js Frontend
                  │
         HTTP Request
                  │
                  ▼
          FastAPI Backend
      ┌──────────┼───────────┐
      │          │           │
      ▼          ▼           ▼
 GitHub API   Semgrep     Groq AI
      │          │           │
      └──────────┼───────────┘
                 ▼
            Supabase DB
                 │
                 ▼
         HTTP Response
                 │
                 ▼
            Next.js UI

HTTP Methods
| Action | HTTP Method |
| ------ | ----------- |
| Read   | GET         |
| Create | POST        |
| Update | PUT         |
| Delete | DELETE      |

Status Codes
| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

