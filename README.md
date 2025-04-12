# Secure Key Transmission Using Quantum-Aware Image Steganography
This repository implements a post-quantum compatible framework for secure cryptographic key exchange using LSB-based steganography and compression techniques. The system is designed for robust, lightweight, and integrity-verifiable transmission of keys over untrusted networks or cloud environments.

# 🧠 Project Overview
The system enables:
- Generation of a secure 256-bit key
- Optional encryption or hashing (AES/SHA-256)
- Bitwise conversion of key and LSB embedding into the blue channel of an image
- zlib-based compression and simulated transmission
- Key extraction and SHA-256 integrity verification

# 📁 Repository Structure
QuantumKeyStego/
├── main.py                      -- # Full pipeline execution
├── key_utils.py                -- # Key generation, encryption, hashing
├── stego_encoder.py             # LSB embedding into blue channel
├── stego_decoder.py             # LSB extraction and key reconstruction
├── compression.py               # zlib-based compression/decompression
├── quantum_sim.py               # (Optional) placeholder for quantum simulations
├── HOW_TO_RUN.txt               # Step-by-step execution instructions
├── README.md                    # This file
└── test_data/
    ├── cover_image.png          # Input image for testing
    ├── stego_image.png          # Output image with embedded key
    ├── stego_image_compressed.bin
    ├── stego_image_decompressed.png
    └── recovered_key.txt        # Final extracted key (hex)

# ⚙️ Dependencies
Install required Python libraries:

pip install opencv-python pillow pycryptodome numpy

# 🚀 How to Run
1. Add a 256x256 or larger PNG image as test_data/cover_image.png
2. Run the main pipeline:

   python main.py

3. Outputs:
- Stego image with embedded key
- Compressed image file
- Extracted and verified key
- Console log showing integrity verification result

# 🔐 Security Features
- Bitwise LSB embedding on the blue channel
- Optional AES encryption or SHA-256 hashing
- End-to-end key integrity verification using hash comparison
- Post-quantum cryptographic compatibility

# 📊 Future Work
- Add support for quantum key distribution simulation (QKD)
- Include quantum image embedding models (FRQI, NEQR)
- Extend to support secure multi-key embedding

# 📄 License
This project is intended for academic, research, and educational use only. All rights reserved by the original author.

# 📬 Contact
For any queries or collaboration requests, please contact:
📧 himabindu747@gmail.com
