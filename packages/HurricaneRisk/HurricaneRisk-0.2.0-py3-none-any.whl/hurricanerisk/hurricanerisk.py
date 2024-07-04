# hurricane_risk.py

import geopandas as gpd
import zipfile
import os
from shapely.geometry import Point
import io
import requests
import pandas as pd

class HurricaneRisk:
    SHAPEFILE_URL = "https://www.nhc.noaa.gov/gis/forecast/archive/wsp_120hr5km_latest.zip"
    
    def __init__(self):
        self.gdfs = self.load_all_shapefiles()

    def load_all_shapefiles(self):
        knot_values = ["34knt", "50knt", "64knt"]
        gdfs = {}
        for knot in knot_values:
            gdfs[knot] = self.download_and_convert_to_gdf(knot)
        return gdfs

    def download_and_convert_to_gdf(self, knots):
        """
        Download a shapefile from the given URL, unzip it, and convert it to a GeoDataFrame.
        Only processes shapefiles containing the text "64knt".
        """
        r = requests.get(self.SHAPEFILE_URL)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(path="tmp_shapefile")

        shapefile_path = None
        for filename in os.listdir("tmp_shapefile"):
            if filename.endswith(".shp") and knots in filename:
                shapefile_path = os.path.join("tmp_shapefile", filename)
                break

        if shapefile_path is None:
            return gpd.GeoDataFrame()

        gdf = gpd.read_file(shapefile_path)

        for filename in os.listdir("tmp_shapefile"):
            os.remove(os.path.join("tmp_shapefile", filename))
        os.rmdir("tmp_shapefile")

        return gdf

    def check_point(self, lat, lon, knots):
        gdf = self.gdfs[knots]
        point = Point(lon, lat)
        contains_point = gdf[gdf.contains(point)]

        if not contains_point.empty:
            return contains_point['PERCENTAGE'].values[0]
        else:
            return 'Not Applicable'

    def address_to_lat_lon(self, address):
        url = f"https://geocode.xyz/{address}?json=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'latt' in data and 'longt' in data:
                lat = data['latt']
                lon = data['longt']
                return float(lat), float(lon)
            else:
                return None, None
        except requests.exceptions.RequestException:
            return None, None
        

    def run(self, addresses):
        if isinstance(addresses, str):
            addresses = [addresses]
        elif not isinstance(addresses, list):
            raise ValueError("Addresses should be a string or a list of strings")

        results = []

        knot_values = ["34knt", "50knt", "64knt"]

        for address in addresses[:100]:
            lat, lon = self.address_to_lat_lon(address)
            result_dict = {
                "Address": address,
                "Latitude": lat if lat else "N/A",
                "Longitude": lon if lon else "N/A"
            }

            if lat and lon:
                for knot in knot_values:
                    probability = self.check_point(lat, lon, knot)
                    result_dict[f"Probability_{knot}"] = probability
            else:
                for knot in knot_values:
                    result_dict[f"Probability_{knot}"] = "Unable to fetch coordinates"

            results.append(result_dict)

        df = pd.DataFrame(results)
        df.rename(columns={
            'Probability_34knt':'Tropical Storm Force (>= 39mph)',
            'Probability_50knt':'Severe Tropical Storm (>= 58 mph)',
            'Probability_64knt':'Hurricane Force (>= 74 mph)'
        }, inplace=True)
        
        self.dataset = df

        return df
    
    def export(self, filename):
        if self.dataset is not None:
            self.dataset.to_excel(filename, index=False, engine='openpyxl')
        else:
            raise ValueError("No data available to export. Please process addresses first.")
