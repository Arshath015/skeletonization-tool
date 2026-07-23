Zhang-Suen Skeletonization Library
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
One-line pitch: A Python library for Zhang-Suen skeletonization.
## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Case Studies](#case-studies)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)
## Overview
The Zhang-Suen skeletonization technique is a widely used method for reducing binary images to their skeletal representations.
## Tech Stack
* Python 3.10
* NumPy
* OpenCV
## Architecture
```
           +---------------+
           |  Input Image  |
           +---------------+
                   |
                   |
                   v
           +---------------+
           |  Thresholding  |
           +---------------+
                   |
                   |
                   v
           +---------------+
           |  Zhang-Suen    |
           |  Skeletonization|
           +---------------+
                   |
                   |
                   v
           +---------------+
           |  Output Image  |
           +---------------+
```
## Theoretical Background
The Zhang-Suen skeletonization technique is based on the idea of iteratively removing pixels from the boundary of the object in the image. The technique uses a set of rules to determine which pixels to remove at each iteration.
## Installation
To install the library, run the following commands:
```
pip install -r requirements.txt
git clone https://github.com/user/skeletonization-tool.git
```
## Usage
To use the library, import the `ZhangSuenSkeletonization` class from the `src.skeletonization` module and call the `skeletonize` method:
```
from src.skeletonization import ZhangSuenSkeletonization
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
skeleton = ZhangSuenSkeletonization().skeletonize(image)
```
## API Reference
* `ZhangSuenSkeletonization` class:
  * `__init__`: Initializes the Zhang-Suen skeletonization object.
  * `skeletonize`: Applies the Zhang-Suen skeletonization technique to the input image.
* `ImageLoader` class:
  * `__init__`: Initializes the image loader object.
  * `load_image`: Loads the input image from file.
* `CLI` class:
  * `__init__`: Initializes the CLI object.
  * `run`: Runs the CLI application.
## Case Studies
See [case_studies/skeletonization_use_case.md](case_studies/skeletonization_use_case.md) for a real-world example of using the Zhang-Suen skeletonization technique.
## Testing
To run the tests, use the following command:
```
pytest tests/
```
## Limitations
The library currently only supports binary images.
## Roadmap
* Add support for color images.
* Improve performance using parallel processing.
## License
The library is licensed under the MIT License.

---
**Last updated:** 2026-07-23
