import requests
import json


class HyperCornAPI:
    def __init__(self):
        self.ip_server = "https://hypercornapi-4oojabxrfa-rj.a.run.app"

    def images_satelite_ndvi(self, min_coords, max_coords, date):
        min_long, min_lat = min_coords
        max_long, max_lat = max_coords
        response = json.loads(requests.get(
            f"{self.ip_server}/images/satelite_ndvi/", params={"min_long": min_long, "min_lat": min_lat, "max_long": max_long, "max_lat": max_lat, "date": date}).content)
        return response

    def segmentation_kmeans(self, image_path):
        if type(image_path) == str:
            file = open(image_path, 'rb')
        else:
            file = image_path.tobytes()
        files = {"file": (file.name, file, "multipart/form-data")}
        response = json.loads(requests.post(url=f"{self.ip_server}/segmentation/kmeans/",
                                            files=files).content)
        return response

    def segmentation_binarize(self, image_path, min_value, max_value):
        if type(image_path) == str:
            file = open(image_path, 'rb')
        else:
            file = image_path.tobytes()
        files = {"file": (file.name, file, "multipart/form-data")}
        data_binarize = {"min_value": min_value, "max_value": max_value}
        response = json.loads(requests.post(url=f"{self.ip_server}/segmentation/binarize/",
                                            files=files, data=data_binarize).content)
        return response
