from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup
import requests

server = FastMCP()

@server.tool(name="WebScraper", description="Scrape text content from a given URL")
def scrape(url: str) -> str:
    """
    Scrapes the main text content from a URL using requests and BeautifulSoup.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove scripts and styles
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
        
        # Get text
        text = soup.get_text(separator="\n")
        text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])
        return text[:50]  
    except Exception as e:
        return f"Error scraping URL: {e}"

if __name__ == "__main__":
    print("Starting WebScraper MCP server on default port...")
    server.run()
