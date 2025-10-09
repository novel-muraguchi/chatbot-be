from fastapi import APIRouter

from chatbot_be.api.v1.healthcheck import router as healthcheck_router

router = APIRouter()
router.include_router(healthcheck_router, prefix="/healthcheck", tags=["healthcheck"])
