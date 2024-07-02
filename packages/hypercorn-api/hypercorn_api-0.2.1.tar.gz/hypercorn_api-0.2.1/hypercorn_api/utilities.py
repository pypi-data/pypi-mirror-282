from numpy import ndarray
import msgpack_numpy as m


class Utilities:
    def get_file_image(self, image):
        if type(image) == str:
            path = image
            file = open(path, 'rb')
            files = {"file": file}
        elif type(image) == list or isinstance(image, ndarray):
            array = image
            encoding = m.packb(array)
            files = {"file": ("array.msgpack", encoding)}

        return files
