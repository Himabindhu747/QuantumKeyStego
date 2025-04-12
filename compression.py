
import zlib

def compress_image_bytes(image_bytes):
    """Compresses image bytes using zlib."""
    return zlib.compress(image_bytes)

def decompress_image_bytes(compressed_bytes):
    """Decompresses zlib-compressed image bytes."""
    return zlib.decompress(compressed_bytes)

def compress_file(input_path, output_path):
    """Reads a file, compresses its contents, and saves to output path."""
    with open(input_path, 'rb') as f_in:
        data = f_in.read()
    compressed = compress_image_bytes(data)
    with open(output_path, 'wb') as f_out:
        f_out.write(compressed)

def decompress_file(input_path, output_path):
    """Reads a compressed file, decompresses its contents, and saves to output path."""
    with open(input_path, 'rb') as f_in:
        compressed = f_in.read()
    decompressed = decompress_image_bytes(compressed)
    with open(output_path, 'wb') as f_out:
        f_out.write(decompressed)
