from fastapi import FastAPI
from app.routers import chat

app = FastAPI()

app.include_router(chat.router)

@app.get('/')
def root():
    return {
        "message": "Welcome to the chat API",
        "routes": [
            {"path": "/chat", "description": "Start a chat"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
