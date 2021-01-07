# tfjs-to-tflite
A simple python script to convert a tfjs-layers model (model.json) to a tflite model.

## Setup
This script requires the following dependences:
* [python3](https://www.python.org/downloads/)
* [tensorflow](https://www.tensorflow.org/install/pip)
* [tensorflowjs](https://pypi.org/project/tensorflowjs/) (python package)

Simply make sure that these packages are installed after cloning this repository and you're good to go!

## Usage

Usage is of the script is as follows:
* Windows: `python tfjs-to-tflite.py <path/to/input/file.json>`
* Linux/MacOS: `python3 tfjs-to-tflite.py <path/to/input/file.json>`

NOTE: The default name for a tfjs layers file is "model.json".
