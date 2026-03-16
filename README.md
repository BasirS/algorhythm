# 🎯 AlgoRhythm

**AI-powered social media strategy assistant for content creators.**

AlgoRhythm helps creators discover trending topics and optimize their content strategy across platforms like YouTube, TikTok, and Instagram.

## Features

- **Trend Discovery**: Get real-time trending topics for YouTube, TikTok, and Instagram
- **Content Format Recommendations**: Personalized format suggestions based on your niche (fitness, cooking, tech, beauty, and more)
- **Conversational Interface**: Natural language chat UI for easy interaction
- **API Access**: RESTful endpoints for integration into other tools

## Tech Stack

- **Backend:** FastAPI, LangGraph, LangChain
- **LLM:** Google Gemini 2.0 Flash
- **Observability:** LangSmith Tracing
- **Deployment:** Render

## Live Demo

👉 **[Try AlgoRhythm](https://algorhythm-59it.onrender.com/ui)**

*Note: Free tier may take ~50s to wake up on first request.*

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/chat` | POST | Send message to agent |
| `/ui` | GET | Web chat interface |
| `/docs` | GET | Interactive API docs |

## Example Queries

```
"What's the best Pokémon game right now?"
"Why is the earth not flat?"
"How should I grow my mukbang channel?"
```

## Local Development

```bash
# Clone the repo
git clone https://github.com/BasirS/algorhythm.git
cd algorhythm

# Create environment
python:m venv .venv
source .venv/bin/activate

# Install dependencies
pip install:r requirements.txt

# Set environment variables
export GOOGLE_API_KEY=your_key
export LANGSMITH_API_KEY=your_key
export LANGSMITH_TRACING=true

# Run locally
uvicorn app.main:app:-reload:-port 8000
```

## Author

[Basir Abdul Samad](https://github.com/BasirS)

---

*Built with LangGraph and deployed on Render.*
