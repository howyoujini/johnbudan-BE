from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse


def init_views(app: FastAPI) -> None:
    from src.views import router as v1_router

    @app.get("/ping")
    def ping() -> str:
        return "pong"

    app.include_router(v1_router, prefix="/v1")


def create_app() -> FastAPI:
    """
    Create FastAPI application
    """

    app = FastAPI(
        openapi_url="/openapi.json",
        default_response_class=ORJSONResponse,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_views(app)

    #
    @app.on_event("startup")
    async def startup() -> None:
        ...

    #
    @app.on_event("shutdown")
    async def shutdown() -> None:
        ...

    #
    return app


app = create_app()
