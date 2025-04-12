
import cv2
import numpy as np
from PIL import Image

def embed_key_lsb(cover_image_path, binary_key, output_image_path):
    """
    Embeds a binary key into the LSBs of the blue channel of an RGB image.
    """
    image = cv2.imread(cover_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {cover_image_path}")
    
    rows, cols, _ = image.shape
    total_pixels = rows * cols

    if len(binary_key) > total_pixels:
        raise ValueError("Key is too long to embed in the image.")

    # Flatten the blue channel
    blue_channel = image[:, :, 0].flatten()

    # Embed the key into the LSB of the blue channel
    for i in range(len(binary_key)):
        blue_channel[i] = (blue_channel[i] & ~1) | int(binary_key[i])

    # Reshape and replace the blue channel
    image[:, :, 0] = blue_channel.reshape(rows, cols)

    # Save the stego image
    cv2.imwrite(output_image_path, image)
    print(f"Stego image saved to {output_image_path}")

def load_image_as_rgb(image_path):
    """Loads an image and returns its RGB representation."""
    img = Image.open(image_path)
    return img.convert('RGB')
