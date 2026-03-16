import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY")
)

# Tool 1: Get trending topics
@tool
def get_trending_topics(platform: str) -> str:
    """
    Get current trending topics for a social media platform.
    Use this when the user asks about trends or what's popular.
    
    Args:
        platform: The social media platform (e.g., 'youtube', 'tiktok', 'instagram')
    """
    platform = platform.lower()
    
    trends = {
        "youtube": [
            "AI-generated content and tutorials",
            "Short-form vertical videos (Shorts)",
            "Documentary-style storytelling",
            "Gaming livestreams and highlights",
            "Health and wellness vlogs"
        ],
        "tiktok": [
            "Dance challenges",
            "Life hacks and tips",
            "Comedy skits",
            "ASMR content",
            "Fashion hauls"
        ],
        "instagram": [
            "Reels with trending audio",
            "Behind-the-scenes content",
            "Carousel educational posts",
            "Aesthetic photography",
            "Collaboration posts"
        ]
    }
    
    if platform in trends:
        trend_list = "\n".join([f"• {t}" for t in trends[platform]])
        return f"Current trending topics on {platform.title()}:\n{trend_list}"
    else:
        return f"I don't have trend data for {platform}. Try youtube, tiktok, or instagram."


# Tool 2: Get content format recommendations
@tool
def get_content_format_recommendations(niche: str) -> str:
    """
    Get recommended content formats for a specific content niche.
    Use this when the user asks about what content formats or types to use.
    
    Args:
        niche: The content niche or topic (e.g., 'fitness', 'cooking', 'tech', 'beauty')
    """
    niche = niche.lower()
    
    recommendations = {
        "fitness": {
            "formats": [
                "Workout follow-along videos (10-30 minutes)",
                "Quick exercise tutorials (60-90 seconds for Reels/Shorts)",
                "Before/after transformation posts",
                "Form check and technique breakdowns",
                "Day-in-the-life fitness routines",
                "Meal prep and nutrition tips"
            ],
            "tips": "Fitness content performs best with clear demonstrations, high energy, and measurable results. Use good lighting to show form clearly."
        },
        "cooking": {
            "formats": [
                "Recipe tutorials with step-by-step instructions",
                "Quick recipe Reels (30-60 seconds)",
                "Ingredient spotlights",
                "Kitchen hack videos",
                "Mukbang and food reviews"
            ],
            "tips": "Overhead shots work great for cooking. Show the final dish early to hook viewers."
        },
        "tech": {
            "formats": [
                "Product reviews and unboxings",
                "Tutorial walkthroughs",
                "Tech news roundups",
                "Comparison videos",
                "Setup tours"
            ],
            "tips": "Tech audiences value depth and honesty. Include timestamps for longer content."
        },
        "beauty": {
            "formats": [
                "Get ready with me (GRWM) videos",
                "Product reviews and swatches",
                "Tutorial transformations",
                "Skincare routines",
                "Haul videos"
            ],
            "tips": "Good lighting is essential. Close-up shots help show product application clearly."
        }
    }
    
    if niche in recommendations:
        rec = recommendations[niche]
        format_list = "\n".join([f"• {f}" for f in rec["formats"]])
        return f"Recommended content formats for {niche}:\n\n{format_list}\n\nTip: {rec['tips']}"
    else:
        # Generic response for unknown niches
        return f"""Recommended content formats for {niche}:

• Educational tutorials explaining key concepts
• Behind-the-scenes content showing your process
• Quick tips in short-form video format (Reels/Shorts)
• Q&A sessions addressing audience questions
• Collaboration content with others in your niche
• Story-driven content that connects emotionally

Tip: Test different formats and see what resonates with your specific audience."""


# System prompt for the agent
system_prompt = """You are AlgoRhythm, a helpful social media strategy assistant.
You help content creators understand trends and optimize their content strategy.

When users ask about trends, use the get_trending_topics tool.
When users ask about content formats or what type of content to create, use the get_content_format_recommendations tool.

Be helpful, specific, and encouraging. Give actionable advice."""

# Create the agent with tools
tools = [get_trending_topics, get_content_format_recommendations]

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=system_prompt
)
