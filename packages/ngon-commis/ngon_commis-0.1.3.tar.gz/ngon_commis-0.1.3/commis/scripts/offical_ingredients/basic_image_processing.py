import typing as T
import cv2
import numpy as np

from ..commis import BaseIngredient
from ..commis import Category

# Example 1
class ReadImage(BaseIngredient):
    """Read an image from a path."""
    
    category = Category.IMAGE
    
    def __init__(self):
        super().__init__()
        self.add_pinch("image_path", str)
        self.add_taste("image", np.ndarray)
    
    def run(self):
        path = self.get_pinch("image_path")
        image = cv2.imread(path)
        self.set_taste("image", image)

# Example 2
class ReadImageV2(BaseIngredient):
    """Read an image from a path."""
    
    category = Category.IMAGE
    outputs = ["image"]
    
    def run(self, image_path: str = "") -> np.ndarray:
        return cv2.imread(image_path)
