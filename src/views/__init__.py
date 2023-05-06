from fastapi.routing import APIRouter
from src.views import main

router = APIRouter()


router.include_router(main.router, prefix="/users", tags=["johnbudan"])
