
import pandas as pd
import geocoder
import logging
from time import sleep

# Initialize logging
logging.basicConfig(level=logging.INFO)

def get_bing_geocode(address, key):
    """ 
    Get geographic coordinates for a given address using Bing Maps API.

    Parameters:
    address (str): The address to geocode.
    key (str): The Bing Maps API key.

    Returns:
    tuple: longitude and latitude
    """
    try:
        g = geocoder.bing(address, key=key, timeout=10)
        results = g.json

        if results:
            return results['lng'], results['lat']
        else:
            logging.warning(f"No result for address: {address}")
            return None, None

    except Exception as e:
        logging.error(f"Error geocoding address {address}: {str(e)}")
        return None, None

# Example usage
if __name__ == "__main__":
    lng, lat = get_bing_geocode('1600 Amphitheatre Parkway, Mountain View, CA', '<Your Bing API Key>')
    print(f"Longitude: {lng}, Latitude: {lat}")
