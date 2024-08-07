from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import calculator

app = FastAPI(
    title="A basic calculator application",
    summary="""This application will expose endpoints that perform basic calculation functions""",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculator.router)
