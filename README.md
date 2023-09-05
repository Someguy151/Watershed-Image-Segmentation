# Watershed Image Segmentation

**Author**: Jonathan Hooper  
**Course**: EECE 566  
**Date**: May 12, 2023

## Abstract

This project employs a Python-based implementation of the watershed algorithm to segment buildings in aerial images using the OpenCV library. The approach involves image pre-processing, morphological operations, distance transform computation, and the application of the watershed algorithm. The segmentation results indicate high accuracy in building detection. This research finds applications in urban planning, disaster management, and more.

## Changes

[Changelog](CHANGELOG.md)

## Features

- **Python and OpenCV**: Utilizes the power of OpenCV for image processing and segmentation.
- **Custom Thresholding**: A unique thresholding function for pre-processing images.
- **High Accuracy**: Proven results in differentiating individual buildings in aerial images.

## Methodology

1. **Image Pre-Processing**: Convert images into grayscale.
2. **Thresholding**: Custom global thresholding function for binarizing the grayscale image.
3. **Morphological Operations**: Noise removal through erosion and dilation.
4. **Distance Transform**: Calculate shortest distance to a background pixel.
5. **Local Maxima Identification**: Identify sure foreground areas.
6. **Generating Markers**: Create markers for the watershed algorithm.
7. **Watershed Algorithm Application**: Flood landscape from markers, resulting in segmented regions.

## Results

- Successful delineation of individual buildings in aerial images.
- The efficiency of the algorithm is influenced by the complexity of the input images.
- Areas for improvement: Handling of shadows or adjoining structures leading to false boundaries.

## How to Use

**Introduction**
This project implements the watershed segmentation algorithm for image processing.

**Prerequisites**
- Python 3.8 or above.
- OpenCV library. Install using `pip install opencv-python`.

**Installation/Setup**
1. Clone the repository using: `git clone git@github.com:Someguy151/Watershed-Image-Segmentation.git`
2. Navigate to the project directory: `cd Watershed-Image-Segmentation`

**Basic Usage**
Run the main script with: `python watershed_segmentation.py`

**Advanced Usage**  
- To segment a different image, modify the `image_path` variable in the main script.
- Tweak the kernel size in the `image_segmentation` function for different results.

**Configuration**  
Adjust the threshold value in the `threshold` function to fit specific images.

**Troubleshooting**  
- If you encounter a "library not found" error, ensure you've installed all dependencies.
- Image not displaying? Ensure the image path is correct.

**Screenshots**  


**Support and Contribution**  
For issues, please raise a ticket in the GitHub repository. Contributions via pull requests are welcome.

**License**  
This project is released under the MIT License.

**Contact**  
For further queries, reach out at jonathanhooper3@hotmail.com.

## References
1. [The Watershed Transformation Applied to Image Segmentation](https://people.cmm.minesparis.psl.eu/users/beucher/wtshed.html)
2. [Image Segmentation with Watershed Algorithm - OpenCV](https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/source/py_tutorials/py_imgproc/py_watershed/py_watershed.rst)
3. [Image Segmentation with Watershed Algorithm - Scikit-image](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_watershed.html)
