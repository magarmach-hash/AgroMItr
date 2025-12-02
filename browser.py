from mcp.server.fastmcp import FastMCP
import asyncio
from playwright.async_api import async_playwright
import warnings

mcp = FastMCP("playwright-scraper-server")

@mcp.tool()
async def playwright_scraper(url: str) -> str:
    """
    Scrapes the content of a given URL using a Playwright browser instance.
    
    Args:
        url: The URL to scrape.
        
    Returns:
        The text content of the page, or an error message if scraping fails.
    """
    try:
        async with async_playwright() as p:
            # Launch a headless Chromium browser
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)   $navigate to url
            content = await page.inner_text('body')
            await browser.close()
            return content
            
    except Exception as e:
        warnings.warn(f"An error occurred during Playwright scraping: {e}")
        return f"An error occurred: {str(e)}. Failed to scrape content from {url}."

if __name__ == "__main__":
    print("Starting Playwright Scraper MCP server…")
    mcp.run("stdio")
