from mcp.server.fastmcp import FastMCP
import requests
import warnings

# warnings.filterwarnings("ignore")

mcp = FastMCP("mandi-price-server")

BASE_URL = "https://api.data.gov.in/resource/35985678-0d79-46b4-9ed6-6f13308a1d24"
API_KEY = "579b464db66ec23bdd000001f39eb4f168814cff5dd4ef0431c669e1"

@mcp.tool()
def get_mandi_prices(state: str, district: str = None, commodity: str = None) -> str:
    """
    Fetches mandi price data for a specific state, optional district, and optional commodity.
    
    Args:
        state: Name of the state (e.g., "Punjab")
        district: Name of the district (optional)
        commodity: Name of the commodity (optional)
    
    Returns:
        Formatted string with modal prices or an error message.
    """
    try:
        state = state.title()
        district = district.title() if district else None
        commodity = commodity.lower() if commodity else None  

        # Build query parameters 
        params = {
            "api-key": API_KEY,
            "format": "json",
            "filters[State]": state,
            "limit": 50  
        }
        if district:
            params["filters[District]"] = district
        if commodity:
            params["filters[Commodity]"] = commodity.title()  

        # api request
        resp = requests.get(BASE_URL, params=params, timeout=20)
        resp.raise_for_status()
        data = resp.json()

        if "records" not in data or not data["records"]:
            return f" No records found for {commodity or 'any commodity'} in {state}" + (f", {district}" if district else "")


        results = []
        for record in data["records"]:
            if "Commodity" in record and "Market" in record and "State" in record and "Modal_Price" in record:
                comm = record["Commodity"]
                mandi_state = record["State"]
                market = record["Market"]
                modal_price = record["Modal_Price"]

                #check case senstivity
                if (commodity is None or commodity.lower() == comm.lower()) and (district is None or record.get("District", "").title() == district):
                    results.append(
                        f"• {comm} in {market}, {record.get('District', '')}, {mandi_state}: Modal Price ₹{modal_price} (per {record.get('unit', 'quintal')})"
                    )

        if results:
            return "\n".join(results[:10])  #top 10 results
        else:
            return f"No prices found for {commodity or 'any commodity'} in {state}" + (f", {district}" if district else "")

    except requests.exceptions.RequestException as e:
        return f"Network error: Could not connect to the government data portal. Details: {str(e)}"
    except Exception as e:
        return f"error occurred: {str(e)}"


if __name__ == "__main__":
    print("Starting Mandi Price MCP server…")
    mcp.run("stdio")
