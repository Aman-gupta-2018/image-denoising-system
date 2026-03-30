import argparse
import cv2
import numpy as np

# Image denoising functions

def gaussian_denoise(image, kernel_size=5):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def median_denoise(image, kernel_size=5):
    return cv2.medianBlur(image, kernel_size)


def nlm_denoise(image, h=10):
    return cv2.fastNlMeansDenoisingColored(image, None, h, h, 7, 21)


def bilateral_denoise(image, diameter=9, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)


def morphological_denoise(image, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# CLI Application

def main():
    parser = argparse.ArgumentParser(description='Image Denoising CLI Application')
    parser.add_argument('input', type=str, help='Path to the input image')
    parser.add_argument('output', type=str, help='Path to save the denoised image')
    parser.add_argument('--method', type=str, choices=['gaussian', 'median', 'nlm', 'bilateral', 'morphological'], required=True, help='Denoising method to use')
    parser.add_argument('--kernel', type=int, default=5, help='Kernel size for the filters')

    args = parser.parse_args()

    # Load the image
    image = cv2.imread(args.input)

    if image is None:
        print(f'Error: Could not load image {args.input}')
        return

    # Denoise the image based on the selected method
    if args.method == 'gaussian':
        denoised_image = gaussian_denoise(image, args.kernel)
    elif args.method == 'median':
        denoised_image = median_denoise(image, args.kernel)
    elif args.method == 'nlm':
        denoised_image = nlm_denoise(image)
    elif args.method == 'bilateral':
        denoised_image = bilateral_denoise(image, args.kernel)
    elif args.method == 'morphological':
        denoised_image = morphological_denoise(image, args.kernel)

    # Save the denoised image
    cv2.imwrite(args.output, denoised_image)
    print(f'Denoised image saved at {args.output}')

if __name__ == '__main__':
    main()