# HyperCornAPI-Python-Wrapper

This is a python wrapper to use HyperCornAPI, an API designed to seamlessly integrate with HyperApp (under construction) and others projects too. HyperCornAPI seeks becoming in an advanced tool for cropps. This documentation provides comprehensive guidance and best practices for developers seeking to harness HyperCornAPI's powerful capabilities for image and spectrum processing with python. Visite us in github [HyperCorn](https://github.com/HyperCorn) 

# Support 
Does your business or project depend on HyperCornAPI?. Please do not hesitate to contact us to our bussines e-mail: [hypercorncordoba@gmail.com](mailto:hypercorncordoba@gmail.com) for support and to discuss your needs.

## Table of Contents

- [Installation](#installation)

- [Uses](#uses)


## Installation

To start using the wrapper, please install the [hypercorn-api](https://pypi.org/project/hypercorn-api/) pip package. Open your terminal and run the following command:


```bash
pip install hypercorn-api
```

## Uses
Before using the functionalities, initialize HyperCornAPI with your credentials. If you don't have them,  [contact us for support](#suport).However, in this version there is no authentication.
```python
from hypercorn_api import HyperCornAPI

# Initialize the API 
hypercorn_api = HyperCornAPI()
```
In a update we will put authentication.

### Images 
This tag is for operations to retrieve images from different sources.

#### Satellite Images - NDVI
To retrieve satellite images with NDVI (Normalized Difference Vegetation Index) using HyperCornAPI, use the following function call:


```python
images_satelite_ndvi = hypercorn_api.images_satelite_ndvi( (46.16, -16.15),(46.51, -15.58),"2024-06-06" )
```


The `images_satelite_ndvi` function takes the following parameters:

1. **Min Coords (tuple)**:  This is the minimum coordinates for the bottom-left corner of the area of interest. First term is longitude, and second is latitude
   - In the Example: `(46.16, -16.15)`

2. **Max Coords (tuple)**: This is the maximum coordinates for the top-right corner of the area of interest. First term is longitude, and second latitude
   - In the Example: `(46.51, -15.58)`

3. **Date (string)**: Specifies the date for which you want to retrieve the satellite image.
   - In the Example: `"2024-06-06"`

The function returns a dictionary with the following structure:

- **image_list (list)**: A list that contains the retrieved satellite images. The values of the pixels are in the ranges (0,1)

### Segmentation
This tag is for operations to retrieve segmented images.

#### Kmeans
Operation for segmenting images uses the k-means algorithm in HyperCornAPI. To retrieve the segmented images, use the following function call:
```python
segmented_image = hypercorn_api.segmentation_kmeans("path/to/your/image")
```

The `segmentation_kmeans` is a function in HyperCornAPI taking into account the following parameters:

1. **image_path (string)**: This is the file path to the image that you want to segment.
   - In the Example: `"path/to/your/image"`

The function returns a dictionary with the following structure:

- **segmented_image (list)**: A list representing the segmented image, where each element corresponds to a segment.


#### Binarize
Operation for segmenting images using binarize in HyperCornAPI. To retrieve the segmented images, use the following function call:
```python
segmented_image = hypercorn_api.segmentation_binarize("path/to/your/tif_image",0.5,0.85)
```

The `segmentation_binarize` function in HyperCornAPI takes the following parameters:

1. **image_path (string)**: Specifies the file path to the image to segment. The file must be in .tif format. 	
   - In the Example: `"path/to/your/tif_image"`

2. **min_value**: Specifies the min value for binarization. 
   - In the Example: `0.5`

2. **max_value**: Specifies the max value for binarization. 
   - In the Example: `0.85`

**Note**: Pixels with values less than `min_value` or greater than `max_value` are set to 0, and pixels with values between `min_value` and `max_value` are set to 1, resulting in a binary (black and white) image.

The function returns a dictionary with the following structure:

- **segmented_image (list)**: A list representing the segmented binary image, where each element is either 0 or 1 based on the specified min_value and max_value.





