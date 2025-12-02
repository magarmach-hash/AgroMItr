from mcp.server.fastmcp import FastMCP
import os
import requests
import json
import warnings

mcp = FastMCP("gemini-search-server")

@mcp.tool()
def gemini_search(query: str) -> str:
    """
    Searches the web using the Gemini API's built-in search grounding.
    
    Args:
        query: The search query.
        
    Returns:
        A concise summary of the search results with sources.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        warnings.warn("GEMINI_API_KEY not found in environment variables.")
        return "Error: GEMINI_API_KEY is not set."

    apiUrl = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

    payload = {
        "contents": [{"parts": [{"text": query}]}],
        "tools": [{"google_search": {}}],
        "systemInstruction": {
            "parts": [{"text": "Provide a concise, single-paragraph summary of the search results."}]
        },
    }

    try:
        response = requests.post(
            apiUrl, 
            headers={'Content-Type': 'application/json'},
            data=json.dumps(payload)
        )
        response.raise_for_status()
        result = response.json()
        
        candidate = result.get("candidates", [{}])[0]
        text = candidate.get("content", {}).get("parts", [{}])[0].get("text", "No result text.")
        
        # Add sources if they exist
        sources = candidate.get("groundingMetadata", {}).get("groundingAttributions", [])
        if sources:
            source_list = [f"- {s.get('web', {}).get('title', 'Unknown Title')} ({s.get('web', {}).get('uri', 'Unknown URI')})" for s in sources]
            text += "\n\nSources:\n" + "\n".join(source_list)

        return text

    except requests.exceptions.RequestException as e:
        return f"Error during search: {str(e)}"

if __name__ == "__main__":
    print("✅ Starting Gemini Search MCP server…")
    mcp.run("stdio")
