Interview Questions

Q1- Why don't we write every endpoint inside main.py?
Ans - main.py is the application entry point. Its responsibility is only to create the FastAPI application and register routers. If every endpoint is placed in main.py, the file becomes difficult to read, maintain, debug, and extend. Splitting APIs into separate router files allows different developers to work independently and makes the project scalable.

Q2- What is APIRouter?
Ans: It routes HTTP requests.
APIRouter groups related API endpoints into separate modules. It helps organize the application by feature, allowing each module to handle a specific set of routes. The main application then includes these routers to create one complete API.

Q3- Why does main.py call include_router()?
Ans: include router helps to navigate from the main.py to the new api requested file and execute it
Flow
Browser
↓
FastAPI Application
↓
include_router()
↓
Health Router
↓
Specific Endpoint
↓
Python Function
↓
JSON Response

Q4: What is Separation of Concerns?
Every file should have one responsibility.Separation of Concerns (SoC)
main.py
↓
Start application

health.py
↓
Health endpoints

Q5: Loose Coupling
Loose coupling means designing software components so they depend on each other as little as possible. This makes it easier to replace, update, or test one component without affecting the rest of the application.

Simple Real-Life Example

Imagine your phone charger.

Phone
   │
USB-C Port
   │
   ▼
Any Compatible Charger

You can use:

Samsung charger
Google charger

Q6: Hight Level Design (HLD)
A High-Level Design (HLD) describes the overall architecture of a system. It explains the major components, how they communicate, the technologies used, and the data flow, without going into implementation details.

| HLD                | LLD                    |
| ------------------ | ---------------------- |
| Big picture        | Implementation details |
| Components         | Classes & Functions    |
| Architecture       | Code                   |
| Data Flow          | Algorithms             |
| Used by Architects | Used by Developers     |

Q7: Why did you use BaseSettings instead of os.getenv()?"
BaseSettings provides automatic loading, type validation, and centralized configuration management. It reduces repetitive code and makes configuration easier to maintain as the application grows.

