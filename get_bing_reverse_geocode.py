
import pandas as pd
import geocoder
import logging
from time import sleep

# Initialize logging
logging.basicConfig(level=logging.INFO)

def get_bing_reverse_geocode(longitude, latitude, key):
    """
    Get address for a given set of geographic coordinates using Bing Maps API.

    Parameters:
    longitude (float): The longitude of the location.
    latitude (float): The latitude of the location.
    key (str): The Bing Maps API key.

    Returns:
    str: Address
    """
    try:
        g = geocoder.bing([latitude, longitude], method='reverse', key=key, timeout=10)
        results = g.json

        if results:
            return results['address']
        else:
            logging.warning(f"No result for coordinates: {latitude}, {longitude}")
            return None

    except Exception as e:
        logging.error(f"Error reverse geocoding coordinates {latitude}, {longitude}: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    address = get_bing_reverse_geocode(37.422408, -122.085609, '<Your Bing API Key>')
    print(f"Address: {address}")
