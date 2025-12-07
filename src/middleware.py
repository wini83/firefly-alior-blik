from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def register_middlewares(app: FastAPI, settings):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
