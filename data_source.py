import requests
import pandas as pd
from datetime import datetime

class DataSource:
    def __init__(self):
        self.url = "https://opensky-network.org/api/states/all"
        # Europe lat,lon values (lat1, lat2, lon1, lon2)
        self.bbox = (35.0, 70.0, -10.0, 40.0)

    def get_planes_in_europe(self):
        try:
            params = {
                "lamin": self.bbox[0],
                "lamax": self.bbox[1],
                "lomin": self.bbox[2],
                "lomax": self.bbox[3]
            }
            resp = requests.get(self.url, params=params, timeout=10)
            data = resp.json()
            count = len(data.get("states", []))
            return pd.DataFrame([{
                "time": datetime.utcnow(),
                "count": count
            }])
        except Exception as e:
            print(f"Error fetching flight data: {e}")
            return pd.DataFrame()
