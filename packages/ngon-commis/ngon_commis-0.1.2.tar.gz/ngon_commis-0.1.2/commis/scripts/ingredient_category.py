from enum import Enum

class Category(str, Enum):
    """Defines the category of an ingredient."""
    
    #: Ingredient do the basic operation
    COMMON = "common"
    #: Unclassified ingredient
    UNCLASSIFIED = "unclassified"
    #: Hidden ingredient
    HIDDEN = "hidden"
    #: Ingredient related to image processing
    IMAGE = "image_processing"