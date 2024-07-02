import requests
import json
from hypercorn_api.utilities import Utilities
from numpy import array

utilities = Utilities()


class HyperCornAPI:
    def __init__(self):
        self.ip_server = "https://hypercornapi-4oojabxrfa-rj.a.run.app"

    def images_satelite_ndvi(self, min_coords, max_coords, date):
        min_long, min_lat = min_coords
        max_long, max_lat = max_coords
        response = json.loads(requests.get(
            f"{self.ip_server}/images/satelite_ndvi/", params={"min_long": min_long, "min_lat": min_lat, "max_long": max_long, "max_lat": max_lat, "date": date}).content)
        response = {"image": array(response["image"])}

        return response

    def segmentation_kmeans(self, image):
        files = utilities.get_file_image(image)
        response = json.loads(requests.post(url=f"{self.ip_server}/segmentation/kmeans/",
                                            files=files).content)
        return response

    def segmentation_binarize(self, image, min_value, max_value):
        files = utilities.get_file_image(image)
        data_binarize = {"min_value": min_value, "max_value": max_value}
        response = json.loads(requests.post(url=f"{self.ip_server}/segmentation/binarize/",
                                            files=files, data=data_binarize).content)
        return response
