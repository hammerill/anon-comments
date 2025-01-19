from fastapi import FastAPI

from routers.example_router import ExampleRouter

app = FastAPI()

app.include_router(ExampleRouter)
