from fastapi import FastAPI

from app.server.routes.obj import router as SimpleRouter

app = FastAPI()
app.include_router(SimpleRouter, tags=["Simple"], prefix="/simple")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
