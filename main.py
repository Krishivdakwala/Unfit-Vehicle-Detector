from UnfitDetection import vehicleFinder
from NumberPlateRecog import ImgToStr
import numpy as np
import os

for filename in os.listdir(r"D:\Useful\Deep Learning pypypypy\Safer India hackathon\Solution\Unfit-Vehicle-Detector\detected_plates"):
    if filename.endswith(".png"):
        print(filename)
        vehicleFinder(ImgToStr(filename))
