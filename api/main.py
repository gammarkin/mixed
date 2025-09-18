from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes.todo as todo_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example route
@app.get("/")
def read_root():
    return {"message": "API is running"}

app.include_router(todo_router.router, prefix="/todos", tags=["todos"])

# Import and include your routers here
# from .routers import todo
# app.include_router(todo.router, prefix