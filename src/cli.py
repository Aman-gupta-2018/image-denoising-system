# Command line interface

import argparse
from src.denoisers.traditional import TraditionalDenoiser

def main():
    parser = argparse.ArgumentParser(description='Image Denoising CLI')
    parser.add_argument('image', type=str, help='Path to the image to be denoised')
    args = parser.parse_args()
    image = load_image(args.image)
    denoised_image = TraditionalDenoiser.gaussian_blur(image)
    save_image(denoised_image, 'denoised_image.png')

if __name__ == '__main__':
    main()
