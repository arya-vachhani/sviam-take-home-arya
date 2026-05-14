"""
Session classifier stub.

TODO: Implement this.

Your classify function should take a session dict and return a classification.
Wire up your LLM call here — use any provider/model you want.
"""

import json


def classify_session(session: dict) -> dict:
    """
    Classify a coding session as organic / pasted / ai_generated.

    Args:
        session: A session dict with keys: session_id, problem_id, language,
                 session_duration_seconds, code, events

    Returns:
        {
            "session_id": "session_01",
            "label": "organic" | "pasted" | "ai_generated",
            "confidence": "low" | "medium" | "high",
            "reason": "One-line explanation of why this classification."
        }
    """
    # TODO: Build your prompt from the session data.
    # TODO: Call your LLM (OpenAI, Anthropic, Groq, local model, etc.)
    # TODO: Parse the response into the expected format.

    # Placeholder — replace this entirely.
    return {
        "session_id": session["session_id"],
        "label": "organic",
        "confidence": "low",
        "reason": "Not implemented yet.",
    }
