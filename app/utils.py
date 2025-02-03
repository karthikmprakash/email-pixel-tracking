from pathlib import Path


def get_image_bytes(image_path: Path) -> bytes:
    """
    Reads an image from the local storage and returns its byte data.

    :param image_path: Path to the image file
    :return: Byte data of the image
    """
    try:
        with open(image_path, "rb") as image_file:
            return image_file.read()
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
