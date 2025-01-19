from fastapi import APIRouter

ExampleRouter = APIRouter(prefix="", tags=["Example Router"])

@ExampleRouter.get("/")
async def get_root():
    return { "detail": "Simpliest API seems to be working!" }
