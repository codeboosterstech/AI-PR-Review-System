"""
backend folder creation --> app folder creation --> main.py file creation
python -m venv venv
source venv/bin/activate  -- virtual env activation

uvicorn app.main:app --reload
"""

#Basic API Creation

from fastapi import FastAPI

app = FastAPI(
    title = "AI Powered Pull Request System using Groq API",
    description = "Backend API for AI-powered Pull Request Review and Security Analysis",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {
        "status" :"True",
        "message" : "welcome to AI Pull Request Review System"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "The system is healthy"
        }

@app.get("/veera")
def veera():
    return{
        "status": "True",
        "message": "Veera's Test API endpoint"
    }

@app.get("/priyanka")
def priyanka():
    return {
        "status": "Test Check",
        "message": "API response Test Check"
    }

@app.get("/about")
def about():
    return {
        "project": "AI PR Review System",
        "Platform": "Github Codespaces",
        "Database": "Supabase",
        "Security": "Semgrep",
        "model": "openai/gpt-oss-120b",
        "Inference Provider": "Groq API"
    }

@app.get("/developer")
def developer():
    return {
        "name" : "veerakumar",
        "role" : "Agentic AI engineer",
        "goal" : "Place in a Good Company with Minimum 15+ LPA"
    }

@app.get("/project")
def project():
    return {
        "project name" : "test",
        "current module" : "Testing",
        "status" :"True"
    }

@app.get("/motivation")
def motivation():
    return {
        "status" :  "Pass",
        "message" : "Sun rises in the east"
    }