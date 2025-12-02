from mcp.server.fastmcp import FastMCP
import requests

# Create MCP server
mcp = FastMCP("Weather_Server")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location"""
    api_key = "ef26729e3293f548a12501e499cb08a1"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Could not fetch weather for {location}."
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {location} is {weather} with a temperature of {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="streamable-http")
