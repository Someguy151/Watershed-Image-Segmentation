import os

def test_image_existence():
    image_path = "images/istanbul12.jpg"
    assert os.path.exists(image_path) == True, "Image not found at " + str(image_path)
    

if __name__ == "__main__":
    test_image_existence()
