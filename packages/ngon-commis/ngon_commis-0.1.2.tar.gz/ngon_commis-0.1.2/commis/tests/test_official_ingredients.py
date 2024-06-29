import pytest

from ..scripts.offical_ingredients.basic_image_processing import ReadImage, ReadImageV2

@pytest.mark.parametrize("path,image_size", [("tests/picsum.png",(225, 225, 3))])
def test_ReadImage(path, image_size):
    ri = ReadImage()
    ri(path)
    assert ri.tastes['image'].value.shape == image_size
    ri(image_path=path)
    assert ri.tastes['image'].value.shape == image_size

@pytest.mark.parametrize("path,image_size", [("tests/picsum.png",(225, 225, 3))])
def test_ReadImageV2(path, image_size):
    ri = ReadImageV2()
    ri(path)
    assert ri.tastes['image'].value.shape == image_size
    ri(image_path=path)
    assert ri.tastes['image'].value.shape == image_size
