
from key_utils import generate_random_key, key_to_binary, binary_to_key, hash_key_sha256
from stego_encoder import embed_key_lsb
from stego_decoder import extract_key_lsb
from compression import compress_file, decompress_file
import os

def main():
    # Setup paths
    original_image = 'test_data/cover_image.png'
    stego_image = 'test_data/stego_image.png'
    compressed_stego = 'test_data/stego_image_compressed.bin'
    decompressed_stego = 'test_data/stego_image_decompressed.png'
    recovered_key_file = 'test_data/recovered_key.txt'

    # Step 1: Generate key and convert to binary
    key = generate_random_key(256)  # 256-bit key
    key_binary = key_to_binary(key)
    print(f"Original Key (hex): {key.hex()}")

    # Step 2: Embed key into image using LSB
    embed_key_lsb(original_image, key_binary, stego_image)

    # Step 3: Compress the stego image
    compress_file(stego_image, compressed_stego)

    # Step 4: Decompress it back (simulating transmission)
    decompress_file(compressed_stego, decompressed_stego)

    # Step 5: Extract key from decompressed image
    extracted_binary = extract_key_lsb(decompressed_stego, len(key_binary))
    recovered_key = binary_to_key(extracted_binary)

    # Step 6: Verify integrity (hash check)
    original_hash = hash_key_sha256(key).hex()
    recovered_hash = hash_key_sha256(recovered_key).hex()

    with open(recovered_key_file, 'w') as f:
        f.write(recovered_key.hex())

    print(f"Recovered Key (hex): {recovered_key.hex()}")
    print(f"Integrity Check Passed: {original_hash == recovered_hash}")

if __name__ == '__main__':
    main()
