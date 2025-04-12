
import cv2

def extract_key_lsb(stego_image_path, key_length_bits):
    """
    Extracts the binary key from the LSBs of the blue channel in the stego image.
    
    Args:
        stego_image_path: Path to the stego image.
        key_length_bits: Number of bits to extract (length of original binary key).
    
    Returns:
        Extracted binary key as a string.
    """
    image = cv2.imread(stego_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {stego_image_path}")
    
    blue_channel = image[:, :, 0].flatten()

    binary_key = ''
    for i in range(key_length_bits):
        binary_key += str(blue_channel[i] & 1)

    return binary_key
