# GetBingAddress
This Python script leverages the Bing Maps API to provide an easy way to convert addresses to geographic coordinates (latitude and longitude) and vice versa. Given a set of coordinates or an address along with a valid Bing API key, this script will return the corresponding address or coordinates.

## Requirements
- Python 3.x
- pandas
- geocoder

## Installation
```bash
pip install pandas
pip install geocoder
```

## Usage
### Geocoding an Address
```python
from GetBingAddress import get_bing_geocode

# Geocoding an address
longitude, latitude = get_bing_geocode('1600 Amphitheatre Parkway, Mountain View, CA', '<Your Bing API Key>')
```

### Reverse Geocoding
```python
from GetBingAddress import get_bing_reverse_geocode

# Reverse geocoding
address = get_bing_reverse_geocode(37.422408, -122.085609, '<Your Bing API Key>')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
