import os
from dotenv import load_dotenv

# Load environment variables BEFORE importing agent
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from app.agent import agent

# Create FastAPI app
app = FastAPI(
    title="AlgoRhythm API",
    description="Social media strategy assistant powered by AI",
    version="1.0.0"
)

# Mount static files for UI
app.mount("/static", StaticFiles(directory="static"), name="static")


# Request/Response models
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # Invoke the agent with the user's message
        result = agent.invoke({
            "messages": [HumanMessage(content=request.message)]
        })
        
        # Extract the final response
        response_content = result["messages"][-1].content
        
        return ChatResponse(response=response_content)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UI endpoint
@app.get("/ui")
def serve_ui():
    return FileResponse("static/index.html")


# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to AlgoRhythm API. Go to /ui for the chat interface or /docs for API documentation."}
