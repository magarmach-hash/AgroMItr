from fastmcp import FastMCP
from deep_translator import GoogleTranslator

mcp = FastMCP("translation-server")

# Convert any input to English
def to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        print("Translation error:", e)
        return text

# Convert English output back to target language
def from_english(text, target_lang="hi"):
    try:
        return GoogleTranslator(source='en', target=target_lang).translate(text)
    except Exception as e:
        print("Translation error:", e)
        return text

# MCP Tool: bidirectional translation
@mcp.tool()
def translate_bidirectional(user_input: str, user_lang: str = "auto") -> str:
    """
    1. Detect language and translate input to English
    2. (You can call your LLM/model here with English input)
    3. Translate model output back to user's language
    """
    # Step 1: to English
    english_input = to_english(user_input)

    # Step 2: Generate response in English (stub)
    model_output = f"[Model output for]: {english_input}"  # Replace with actual LLM call

    # Step 3: Back to original language
    if user_lang == "auto":
        # Try to detect
        translated_back = GoogleTranslator(source='en', target='auto').translate(model_output)
    else:
        translated_back = from_english(model_output, target_lang=user_lang)

    return translated_back

if __name__ == "__main__":
    print("Starting bidirectional translation MCP server...")
    mcp.run(transport="stdio")
