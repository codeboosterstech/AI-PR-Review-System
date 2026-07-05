from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/")
def home():
    return{
        "success": True,
        "message": "Welcome to AI PR Review Platform"
    }

@router.get("/health")
def health():
    return{
        "status" : True,
        "message" : "Health Check is success"
    }
