import os
from app.fallback import fallback_process

def process_with_ai(text: str):
    # Simulate AI failure if no API key
    if not os.getenv("OPENAI_API_KEY"):
        return fallback_process(text)

    try:
        # Placeholder for real AI call
        return {
            "category": "AI_Detected",
            "summary": text[:80],
            "actions": ["Be cautious", "Verify source"]
        }
    except Exception:
        return fallback_process(text)